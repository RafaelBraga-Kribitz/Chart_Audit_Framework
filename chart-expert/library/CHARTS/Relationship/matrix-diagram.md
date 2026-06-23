---
name: Matrix Diagram
category: Relationship
input_type: [matrix-grid, cat-multi-value]
it_variants: []
analytical_function: Correlation
visual_family: Diagram
shape_primitive: [Square, Circle, Dot]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-hue, color-value, area]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [E, J]
alternatives: [heat-map, correlation-matrix, scatter-matrix, bubble-heatmap]
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---

# Matrix Diagram

## Description
A Matrix Diagram (also called a relationship matrix or cross-matrix chart) displays relationships between two sets of items arranged in rows and columns. Each cell represents the intersection of one row-item and one column-item, and the cell mark — which can be a dot, symbol, colour fill, number, or glyph — indicates whether a relationship exists and optionally its strength, type, or priority. Matrix diagrams are used in quality management (QFD/House of Quality), project management, systems engineering, and network adjacency visualisation.

## When to Use
- Mapping which items from one set relate to items in another set (existence of relationships)
- Quality Function Deployment (QFD): mapping customer requirements to engineering characteristics
- Stakeholder mapping: which stakeholders are affected by which decisions
- Adjacency matrices for network visualisation as an alternative to node-link diagrams
- Showing the cross-impact of system components on each other

## When NOT to Use
- When the number of items on each axis is very large (> ~30×30) — cells become too small to read
- When the primary goal is to show numeric magnitude (use a heat map with a continuous colour scale)
- When the relationship type has too many distinct values to encode clearly with symbols
- When hierarchical or flow structure between items is the primary message (use a network or Sankey)

## Data Requirements
- Two categorical columns defining the row and column items
- One column defining the relationship value (binary, ordinal, or numeric)
- Optional: a relationship type column for symbol encoding

## Best Practices
- Use a clear symbol legend: blank = no relationship, small dot = weak, large dot = strong
- Group related rows and columns together to reveal block patterns
- Apply hierarchical clustering or manual sorting to align related items
- Label cells with numeric values when precision matters
- Keep the total number of cells manageable (< ~400 cells total for static charts)

## Common Mistakes
- E (MC-noise-as-difference): treating a "weak" symbol as categorically different from "no relationship" without defining the threshold
- J (silently-dropped-categories): failing to show all row × column combinations — absent cells look like "no relationship" when they may be missing data
- Using too many symbol types — readers cannot hold more than 4–5 distinct symbols in working memory
- Making the matrix asymmetric without documenting whether the relationship is directed

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 8))
for i, row in enumerate(row_items):
    for j, col in enumerate(col_items):
        val = matrix[i, j]
        if val > 0:
            ax.scatter(j, i, s=val * 100, color='steelblue', alpha=0.7)
ax.set_xticks(range(len(col_items))); ax.set_xticklabels(col_items, rotation=45, ha='right')
ax.set_yticks(range(len(row_items))); ax.set_yticklabels(row_items)
ax.grid(True, alpha=0.3)
plt.tight_layout()
```

### plotly
```python
import plotly.express as px
fig = px.scatter(df, x='col_item', y='row_item',
                 size='strength', color='relationship_type')
fig.show()
```

### altair
```python
import altair as alt
alt.Chart(df).mark_circle().encode(
    x='col_item:O',
    y='row_item:O',
    size=alt.Size('strength:Q', scale=alt.Scale(range=[0, 500])),
    color='type:N',
    tooltip=['row_item', 'col_item', 'strength']
)
```

### excel / tableau
- **Excel**: Create as a table; apply conditional formatting or insert shapes in cells to indicate relationship strength.
- **Tableau**: Drag two dimensions to Rows and Columns; drag a measure to Size and a dimension to Colour; set mark to Circle.

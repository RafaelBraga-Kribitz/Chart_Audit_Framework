---
name: Heat Map
category: Distribution
input_type: [matrix-grid, cat-multi-value, time-series]
it_variants: []
analytical_function: Distribution
visual_family: Chart
shape_primitive: [Square]
cardinality_fit: [medium, large, very-large]
audience: [Analytics, Technical, Executive]
complexity: Basic
encoding_channels: [position, color-value]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [E, J]
alternatives: [correlation-matrix, bubble-heatmap, contour-plot, radial-heatmap]
source: [datavizproject, datavizcatalogue]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---

# Heat Map

## Description
A Heat Map encodes values in a two-dimensional matrix using colour. Rows and columns represent categorical or temporal variables, and each cell's colour intensity encodes the magnitude of a numeric value at that intersection. Heat maps excel at revealing patterns, clusters, and outliers across many variable combinations simultaneously — things that would require reading many individual numbers from a table. They are widely used for temporal patterns (e.g., activity by hour × day), correlation matrices, and cross-tabulated metrics.

## When to Use
- Revealing patterns in a matrix of values across two categorical or temporal dimensions
- Identifying clusters, hotspots, or anomalies across many row-column combinations
- Showing correlation or similarity matrices (when exact values are less important than pattern)
- Calendar heatmaps for activity over time (commits, sales, events)
- Comparing performance across multiple metrics and groups in a compact grid

## When NOT to Use
- When exact numeric values need to be read precisely — colour perception is imprecise (add cell labels)
- When the matrix is sparse — many empty/zero cells make the chart cluttered and misleading
- When there are very few rows or columns (< 4 × 4) — a simple table or bar chart is clearer
- When a diverging scale is needed but the midpoint is not meaningful in the data context

## Data Requirements
- Two categorical or temporal columns defining rows and columns of the matrix
- One numeric column defining cell values
- All row-column combinations should ideally be populated; missing values need explicit handling

## Best Practices
- Choose colour scale type deliberately: sequential for one-directional data, diverging for data with a meaningful midpoint (e.g., correlation, deviation from target)
- Use a perceptually uniform scale (viridis, RdBu) — never use a rainbow/jet scale
- Annotate cells with numeric values when the matrix is small enough (< ~15×15)
- Cluster rows and columns by similarity (hierarchical clustering) to reveal blocks of related variables
- Include a colour legend with clearly labelled tick marks and units

## Common Mistakes
- E (MC-noise-as-difference): subtle colour differences in a poor colour scale are perceived as significant when the underlying difference is trivial
- J (silently-dropped-categories): missing row-column combinations are often rendered as white/zero and confused with true zeros
- Using a sequential scale on correlation data (which ranges -1 to 1) — diverging scale is required
- Displaying raw counts without normalising when rows or columns have very different totals (row-normalise or use rates)

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(pivot_df, cmap='viridis', annot=True, fmt='.1f',
            linewidths=0.5, ax=ax)
ax.set_title('Heat Map')
plt.tight_layout()
```
`cmap='RdBu_r'` for diverging. `vmin`/`vmax` to set colour scale bounds.

### plotly
```python
import plotly.express as px
fig = px.imshow(pivot_df, color_continuous_scale='Viridis',
                text_auto=True, aspect='auto')
fig.show()
```
`zmin`/`zmax` control colour range. `color_continuous_midpoint=0` for diverging.

### altair
```python
import altair as alt
alt.Chart(df).mark_rect().encode(
    x='column_var:O',
    y='row_var:O',
    color=alt.Color('value:Q', scale=alt.Scale(scheme='viridis')),
    tooltip=['row_var', 'column_var', 'value']
)
```

### excel / tableau
- **Excel**: Conditional Formatting > Colour Scales on a pivot table. For full custom control, use a 2D pivot table with colour scale rules.
- **Tableau**: Drag two dimensions to Rows and Columns; drag measure to Colour; set mark type to Square. Tableau calls this a Highlight Table.

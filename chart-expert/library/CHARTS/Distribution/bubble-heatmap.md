---
name: Bubble Heatmap
category: Distribution
input_type: [matrix-grid, cat-multi-value]
it_variants: []
analytical_function: Distribution
visual_family: Chart
shape_primitive: [Circle]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, area, color-value]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [E, J, F]
alternatives: [heat-map, scatter-matrix, correlation-matrix, bubble-chart]
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

# Bubble Heatmap

## Description
A Bubble Heatmap is a variant of a heat map that uses circles (bubbles) instead of coloured rectangles to fill matrix cells. Each bubble encodes two data dimensions simultaneously: its size encodes one numeric variable (e.g., magnitude or confidence) and its colour encodes another (e.g., direction, significance, or a different metric). This dual-encoding allows the chart to communicate more information per cell than a standard heat map while retaining the grid structure for pattern-finding across rows and columns.

## When to Use
- When two related numeric values need to be shown per matrix cell (e.g., effect size + significance, count + rate)
- Correlation matrices where both the magnitude and sign of correlation need simultaneous encoding
- Displaying ranked results across multiple metrics where two aspects (score and confidence) matter
- When a standard heat map loses nuance by encoding only one numeric dimension

## When NOT to Use
- When size and colour encode redundant information (use plain heat map instead)
- When the matrix is very dense (> ~20×20) — small bubbles become illegible
- When precise size comparison is needed — area perception is less accurate than length
- When only one numeric dimension exists per cell

## Data Requirements
- Two categorical columns (row and column dimensions)
- Two numeric columns: one for bubble size, one for bubble colour
- All cells should ideally be populated; sparse matrices with many missing bubbles are hard to interpret

## Best Practices
- Scale bubble area proportional to the value, not radius (smell F: bounding-box-geometry)
- Use size for the "primary" value (the one audiences compare most) and colour for a secondary qualifier
- Include a legend for both size and colour with clearly labelled reference bubbles
- Cap maximum bubble size so bubbles stay within their cell
- Use diverging colour scale when colour encodes a variable with a natural midpoint (e.g., correlation: -1 to +1)

## Common Mistakes
- F (bounding-box-geometry): scaling bubble radius (not area) to the value distorts magnitude perception
- E (MC-noise-as-difference): treating visually similar bubble sizes as meaningfully different
- J (silently-dropped-categories): missing cells rendered as absent bubbles vs. zero-size bubbles — the distinction matters
- Encoding the same variable in both size and colour (wastes an encoding channel)
- Allowing bubble overflow outside cell boundaries when values differ greatly in range

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
for i, row in enumerate(rows):
    for j, col in enumerate(cols):
        size = values_size[i, j]
        color = values_color[i, j]
        ax.scatter(j, i, s=size * 100, c=color, cmap='RdBu',
                   vmin=-1, vmax=1, alpha=0.8)
ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols)
ax.set_yticks(range(len(rows))); ax.set_yticklabels(rows)
plt.colorbar(ax.scatter([], [], c=[], cmap='RdBu', vmin=-1, vmax=1), label='Colour metric')
plt.tight_layout()
```

### plotly
```python
import plotly.express as px
fig = px.scatter(df, x='col_var', y='row_var',
                 size='size_metric', color='color_metric',
                 color_continuous_scale='RdBu', color_continuous_midpoint=0)
fig.update_layout(yaxis=dict(autorange='reversed'))
fig.show()
```

### altair
```python
import altair as alt
alt.Chart(df).mark_circle().encode(
    x='col_var:O',
    y='row_var:O',
    size=alt.Size('size_metric:Q', scale=alt.Scale(range=[0, 1000])),
    color=alt.Color('color_metric:Q', scale=alt.Scale(scheme='redblue', domainMid=0))
)
```

### excel / tableau
- **Excel**: Bubble chart with row/column as x/y coordinates, two additional data columns for size and colour.
- **Tableau**: Scatter plot with dimensions on Rows/Columns; drag size and colour measures to respective shelves. Set mark type to Circle.

---
name: Strip Plot
category: Distribution
input_type: [cat-value, demo-grouped]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Dot, Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [E]
alternatives: [jitter-plot, beeswarm-plot, dot-density-plot, violin-plot]
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

# Strip Plot

## Description
A Strip Plot (also called a dot strip chart or one-dimensional scatter plot) arranges all individual data points as dots along a single axis, with no offset or jitter applied. Points at identical values stack or overlap exactly. Unlike beeswarm or jitter plots, strip plots are the purest representation of the raw values on a single dimension — position on the axis is the only encoding, and the perpendicular axis carries no information. When overplotting occurs, transparency or symbol size reduction is the standard remedy.

## When to Use
- Displaying the full range and granularity of a continuous variable across groups
- When precise alignment of values on the axis is more important than resolving overlaps
- Supplementing summary charts (box plots, violin plots) by revealing the actual underlying points
- Very small datasets (n < ~50) where every point can be labelled or hovered

## When NOT to Use
- When significant overplotting occurs at n > ~100 per group (use jitter or beeswarm instead)
- When the density of points in different regions is what you want to communicate (use a density plot)
- When groups need lateral separation that makes the "no-offset" characteristic meaningless

## Data Requirements
- One continuous numeric column (the primary value axis)
- One optional categorical grouping column
- n per group: best at < 100 for non-overlapping legibility without jitter

## Best Practices
- Layer a box plot or violin plot behind the strip to provide summary statistics
- Use alpha transparency when some overlap is unavoidable
- Label individual notable points (outliers, specific cases) directly on the chart
- Separate groups clearly with visual spacing or colour
- Consider converting to a dot plot (counts) if many points share the same value

## Common Mistakes
- E (MC-noise-as-difference): strip plots with heavy overplotting mislead about density — dark stacks look like fewer points than they are
- Using strip plots for large n without any transparency, making them look like solid bars
- Confusing strip plot with beeswarm — strip plots do not apply collision detection

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

for i, (label, group) in enumerate(groups.items()):
    plt.scatter([i] * len(group), group, alpha=0.4, s=15)
plt.xticks(range(len(groups)), list(groups.keys()))
plt.ylabel('Value')
```

### plotly
```python
import plotly.express as px
fig = px.strip(df, x='group', y='value', stripmode='overlay')
# Set jitter=0 for true strip (no jitter)
fig.update_traces(jitter=0)
fig.show()
```

### altair
```python
import altair as alt
alt.Chart(df).mark_tick().encode(
    x='group:N',
    y='value:Q',
    color='group:N'
)
```
`mark_tick()` is Altair's native strip/tick mark — thin vertical lines at each value position.

### excel / tableau
- **Excel**: Scatter chart; all points in a group share the same x-value. Use multiple series for groups.
- **Tableau**: Drag measure to Rows, dimension to Columns; set mark type to Circle; disable jitter.

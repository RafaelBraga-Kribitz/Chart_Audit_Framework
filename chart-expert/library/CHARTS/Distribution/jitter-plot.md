---
name: Jitter Plot
category: Distribution
input_type: [cat-value, demo-grouped]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Dot]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [E]
alternatives: [beeswarm-plot, strip-plot, violin-plot, box-plot]
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

# Jitter Plot

## Description
A Jitter Plot is a one-dimensional scatter plot where random horizontal (or vertical) noise is added to each data point to prevent overplotting. Unlike a beeswarm plot (which uses deterministic collision detection), jitter is stochastic — each run may produce slightly different layouts. Every raw observation is visible at its true value on the primary axis, with the perpendicular offset being purely cosmetic. Jitter plots are simple to implement and effective for small to moderate datasets where seeing individual points is important.

## When to Use
- Showing all individual data points for a small to medium dataset (n < ~300 per group)
- Supplementing box plots or violin plots to reveal the actual data beneath summary statistics
- Quickly checking for outliers, clusters, or granularity issues (e.g., discrete values masquerading as continuous)
- Comparing distributions across a few groups in a lightweight, easy-to-generate chart

## When NOT to Use
- When n per group is large (> ~500) — overplotting persists even with jitter
- When reproducibility of point positions matters — jitter is random (use beeswarm instead)
- When the lateral displacement could be misread as carrying meaning
- When very precise comparison of individual points is needed (lateral jitter obscures exact x-position)

## Data Requirements
- One continuous numeric column (the value)
- One categorical grouping column (optional)
- n per group: ideally between 10 and 300

## Best Practices
- Set a fixed random seed for reproducibility when sharing charts
- Use transparency (alpha 0.3–0.6) when points overlap despite jitter
- Overlay a box plot or median line to give a summary statistic anchor
- Keep jitter width small enough that points remain visually associated with their group
- Use consistent point size — 3–5 pt is typically sufficient

## Common Mistakes
- E (MC-noise-as-difference): the random lateral spread is noise; do not interpret it as distributional features
- Using excessive jitter width so points appear to belong to a neighbouring group
- Forgetting to set a random seed — generates different charts on each run
- Applying jitter to truly continuous data when overplotting is not actually a problem

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(loc=1, scale=0.05, size=len(data))  # jitter
plt.scatter(x, data, alpha=0.5, s=20)
```
Or via seaborn: `sns.stripplot(data=df, x='group', y='value', jitter=True, alpha=0.6)`

### plotly
```python
import plotly.express as px
fig = px.strip(df, x='group', y='value', stripmode='overlay')
fig.show()
```
`px.strip` adds jitter automatically. Control with `jitter` parameter (0–1).

### altair
```python
import altair as alt
alt.Chart(df).mark_circle(size=30, opacity=0.5).encode(
    x=alt.X('group:N', axis=alt.Axis(labelAngle=0)),
    y='value:Q',
    xOffset=alt.XOffset('jitter:Q')
).transform_calculate(jitter='random()')
```

### excel / tableau
- **Excel**: Scatter chart with a RAND()-based helper column for jitter offset.
- **Tableau**: Add `RANDOM()` as a secondary axis or calculated field to create jitter offset; plot as Scatter.

---
name: Beeswarm Plot
category: Distribution
input_type: [cat-value, demo-grouped]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Dot]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [E]
alternatives: [strip-plot, jitter-plot, violin-plot, box-plot]
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

# Beeswarm Plot

## Description
A Beeswarm Plot is a one-dimensional scatter plot where individual data points are arranged along a single axis and spread sideways (using a collision-detection algorithm) to avoid overlap while remaining as close as possible to their true value position. Unlike jitter plots, the horizontal spread is deterministic and reflects local density — where points cluster together, the swarm widens. Every data point is visible, making this chart ideal for small to medium datasets where individual observations matter.

## When to Use
- Displaying every individual data point without overlap
- Comparing distributions across a small number of groups when n per group is small to moderate (< ~500)
- Combining with a box plot or summary glyph to show both shape and individual points
- Communicating audit results or clinical measurements where individual values are accountable

## When NOT to Use
- When n > ~500 per group — the swarm becomes too wide and/or too slow to render
- When exact x-position within the swarm carries no meaning and could mislead
- When categories are many (> 6–8) — chart becomes cluttered
- When a smooth distributional summary is sufficient (use violin or density plot instead)

## Data Requirements
- One continuous numeric column (the value, plotted on the primary axis)
- One categorical grouping column (determines swarm groups)
- n per group: best between 20 and 300

## Best Practices
- Overlay a median line or box plot summary so group centres are anchored
- Use consistent point size — too large causes excessive spread; too small loses readability
- Colour-code by a secondary categorical variable if additional stratification is needed
- Sort groups by median or mean for easier comparison
- Label outlier points individually when the data is an audit or diagnostic context

## Common Mistakes
- E (MC-noise-as-difference): interpreting swarm width differences as statistical significance without a test
- Applying beeswarm to very large n — the layout algorithm is O(n²) and the chart becomes unreadable
- Using jitter instead of beeswarm and calling it a beeswarm (jitter positions are random; beeswarm positions are deterministic)
- Omitting a summary statistic overlay, leaving audiences without a central-tendency anchor

## Implementation Notes

### matplotlib
Use the `beeswarm` package or `stripplot` from seaborn (with `dodge=True` for grouping):
```python
import seaborn as sns
sns.stripplot(data=df, x='group', y='value', jitter=False,
              dodge=True, size=4, alpha=0.7)
```
For true beeswarm (no random jitter), use the `beeswarm` or `beehive` libraries.

### plotly
Plotly does not have a native beeswarm; approximate with `px.strip` (which uses jitter):
```python
import plotly.express as px
fig = px.strip(df, x='group', y='value', stripmode='overlay')
fig.show()
```

### altair
```python
import altair as alt
alt.Chart(df).mark_circle(size=40).encode(
    x=alt.X('group:N'),
    y=alt.Y('value:Q'),
    color='group:N'
).transform_calculate(
    # Altair lacks native collision detection; use jitter or external layout
)
```
For true beeswarm in Altair, pre-compute x-offsets using a Python beeswarm library.

### excel / tableau
- **Excel**: No native beeswarm. Approximate with scatter plot and manually computed offsets.
- **Tableau**: Use a Jitter calculation (`RANDOM()`) as a workaround; true beeswarm requires pre-computed offsets imported as a field.

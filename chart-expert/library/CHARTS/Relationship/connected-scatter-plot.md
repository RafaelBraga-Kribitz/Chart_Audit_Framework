---
name: Connected Scatter Plot
category: Relationship
input_type: [xy-simple, time-series]
it_variants: []
analytical_function: Correlation
visual_family: Plot
shape_primitive: [Dot, Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-hue, motion]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [K, E, L]
alternatives: [scatter-plot, line-chart, bubble-chart, slope-chart]
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

# Connected Scatter Plot

## Description
A Connected Scatter Plot is a scatter plot where successive data points are joined by line segments in temporal or sequential order, revealing the path a bivariate observation traces through time (or another ordered sequence). Each point represents one time period's pair of (x, y) values, and the connecting lines show the direction and speed of change between periods. The overall path shape — loops, spirals, reversals — encodes the dynamic relationship between the two variables in a way that neither a pure scatter plot nor a line chart can achieve alone.

## When to Use
- Showing how the relationship between two variables evolves over time
- Economic and policy analysis where two rates or indices track jointly over years (e.g., unemployment vs. inflation Phillips curve)
- Tracking cyclical patterns in two correlated variables
- When temporal order of a bivariate relationship is the primary story

## When NOT to Use
- When n is large (> ~50 time steps) — the path becomes a tangled hairball
- When the audience cannot follow a directional path without annotation guides
- When the temporal order does not exist or is irrelevant to the question
- When only one variable changes over time (use a line chart)
- When the path crosses itself frequently, making the chart unreadable

## Data Requirements
- Two continuous numeric columns (x and y variables)
- One temporal or sequential ordering column
- n between 5 and ~50 time steps for readable path tracing

## Best Practices
- Add directional arrows at regular intervals or at the start/end to show time direction
- Label start and end points explicitly (e.g., first and last year)
- Use colour gradient along the path (early to late) as a secondary time encoding
- Annotate key events or inflection points directly on the path
- Order the time dimension explicitly before connecting — default sort may not be chronological

## Common Mistakes
- L (suspiciously-smooth-series): when the path looks too smooth, check whether data was pre-smoothed in a way that obscures real variability
- K (self-correlated scatter): axes that share a common driver will produce connected paths that appear cyclical without a true bivariate relationship
- E (MC-noise-as-difference): interpreting small path deviations as meaningful trajectory changes vs. measurement noise
- Missing directional annotations — readers cannot tell which direction time flows
- Connecting non-sequential observations (e.g., connecting alphabetically sorted categories instead of time-sorted)

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot(x, y, '-o', color='steelblue', linewidth=1.5, markersize=5, alpha=0.8)
# Add arrows for direction
for i in range(0, len(x) - 1, max(1, len(x)//10)):
    ax.annotate('', xy=(x[i+1], y[i+1]), xytext=(x[i], y[i]),
                arrowprops=dict(arrowstyle='->', color='steelblue', lw=1.5))
ax.scatter([x[0], x[-1]], [y[0], y[-1]], zorder=5, color=['green', 'red'], s=80)
ax.set_xlabel('Variable X'); ax.set_ylabel('Variable Y')
plt.tight_layout()
```

### plotly
```python
import plotly.express as px
fig = px.line(df.sort_values('time'), x='x', y='y',
              text='time_label', markers=True)
fig.update_traces(mode='lines+markers+text')
fig.show()
```

### altair
```python
import altair as alt
line = alt.Chart(df).mark_line().encode(x='x:Q', y='y:Q', order='time:T')
points = alt.Chart(df).mark_circle(size=60).encode(x='x:Q', y='y:Q', tooltip='time:T')
(line + points).interactive()
```

### excel / tableau
- **Excel**: Line chart with x and y data series, then switch to XY Scatter with Lines. Label start/end manually.
- **Tableau**: Scatter chart with a Path encoding using the time field. Set mark to Line and order by time.

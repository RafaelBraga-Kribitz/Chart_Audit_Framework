---
name: Bump Chart
category: Temporal
input_type: [time-series, cat-multi-value]
it_variants: []
analytical_function: Ranking
visual_family: Chart
shape_primitive: [Line, Circle]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive, Public]
complexity: Intermediate
encoding_channels: [position, color-hue]
tool_support: [d3, plotly, altair, matplotlib, tableau]
failure_modes: [D]
alternatives: [line-chart, slope-chart, parallel-coordinates]
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

# Bump Chart

## Description
A bump chart displays how the rank ordering of entities changes over multiple time periods, with the y-axis showing rank (1 = top) and smooth curves connecting each entity's rank at each time point. Unlike a line chart that shows absolute values, a bump chart focuses purely on relative ordering changes. Entities are typically colored distinctly and labeled at each end.

## When to Use
- Showing how competitive rankings change over time (sports leagues, market share ranks, survey positions)
- When rank changes are the primary story, not absolute value changes
- Small-to-medium numbers of entities (up to ~15) competing for ranked positions
- Communicating rises and falls in standing in a visually engaging way

## When NOT to Use
- Absolute values are more important than ranks (use a line chart)
- More than ~15 entities — lines become unreadably tangled
- Time periods are too few (2 periods — use a slope chart instead)
- Rank ties are common and need to be visually distinguishable

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| time period | ordered categorical or date | Each distinct ranking moment |
| entity | categorical | The items being ranked |
| rank | integer | 1 = highest; must be computed prior to plotting |

## Best Practices
- Invert the y-axis so rank 1 is at the top
- Use smooth sigmoid/spline curves between time points for visual appeal
- Label entities directly at both start and end rather than relying on a legend
- Use a distinct color per entity and keep the palette accessible
- Highlight a specific entity (bold, opaque) while graying out others for focused storytelling

## Common Mistakes
- Sorting or ordering by index rather than computing actual rank — see Smell D
- Using too many entities, making individual trajectories impossible to follow
- Using a bump chart when there are only two time points (use a slope chart)
- Coloring by rank position instead of entity identity, making trajectories impossible to trace

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
for entity in df['entity'].unique():
    sub = df[df['entity'] == entity]
    ax.plot(sub['period'], sub['rank'], marker='o', label=entity)
ax.invert_yaxis()
ax.legend(loc='right')
```
Smooth curves require scipy spline interpolation between period tick positions.

### plotly
Use `go.Scatter` with `line_shape='spline'`, one trace per entity, inverted y-axis.

### altair
`alt.Chart(df).mark_line(point=True, interpolate='monotone').encode(x='period:O', y=alt.Y('rank:Q', scale=alt.Scale(reverse=True)), color='entity:N')`

### excel / tableau
Tableau: Line chart with rank on y-axis (reversed), discrete time on x-axis, color by entity. Excel: Manual construction with a line chart.

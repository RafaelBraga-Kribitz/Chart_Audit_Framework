---
name: Stepped Line Graph
category: Temporal
input_type: [time-series, xy-simple]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Line]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [L]
alternatives: [line-chart, area-chart, candlestick-chart]
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

# Stepped Line Graph

## Description
A stepped line graph (also called a step chart) connects data points with horizontal and vertical segments rather than diagonal lines, creating a staircase effect. Each horizontal segment represents the constant value between two events, and the vertical segment marks the discrete change. This accurately represents data that changes instantaneously at specific moments and remains constant until the next change.

## When to Use
- Displaying data that holds a constant value until a discrete change event (e.g., interest rates, pricing tiers, inventory steps)
- Showing state-based or threshold-based metrics where interpolation is misleading
- Protocol or configuration values that take discrete steps over time
- Event-driven metrics where the previous value persists until the next event

## When NOT to Use
- Data changes continuously and interpolation is valid (use a standard line chart)
- The step pattern implies a precision that does not exist in the data
- Data is sparse with very long flat periods that overwhelm the chart space

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date or ordered numeric | Event timestamps; defines the step locations |
| value | numeric | The constant value held between events |
| series (optional) | categorical | For multiple step series |

## Best Practices
- Choose the step direction: pre-step (value changes at the start of the interval), mid-step, or post-step — match your data's semantics
- Label the step position convention if the audience may not be familiar
- For sparse data, annotate key step-change events directly on the chart
- Avoid interpolating smoothly between steps — that destroys the meaning — see Smell L

## Common Mistakes
- Using a diagonal line chart when data is actually step-constant, implying false interpolation — see Smell L
- Choosing the wrong step alignment (pre vs. post) and misrepresenting when changes took effect
- Applying too much visual noise (gridlines, tick marks) on long flat regions

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.step(df['date'], df['value'], where='post',
        color='steelblue', linewidth=1.5)
plt.tight_layout()
```
`where='pre'`, `'mid'`, or `'post'` controls step alignment.

### plotly
`go.Scatter(x=df['date'], y=df['value'], line_shape='hv')` (or `'vh'` for the opposite direction).

### altair
`alt.Chart(df).mark_line(interpolate='step-after').encode(x='date:T', y='value:Q')`

### excel / tableau
Excel: No direct step chart; workaround by duplicating data points. Tableau: Edit axis interpolation to "step" in line mark settings.

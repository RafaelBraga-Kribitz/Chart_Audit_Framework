---
name: Slope Chart
category: Temporal
input_type: [cat-multi-value, time-series]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Line, Dot]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Public]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [D]
alternatives: [bump-chart, dumbbell-plot, line-chart, bar-chart]
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

# Slope Chart

## Description
A slope chart compares values across exactly two time points (or two conditions) for multiple entities by drawing a line between the before and after values. The slope of each line encodes direction (increase or decrease) and magnitude of change. It is a simple, direct way to show change between two states without the complexity of a full time series.

## When to Use
- Comparing a metric before and after an event or intervention for multiple entities
- Showing which categories increased vs. decreased between two periods
- When exactly two time points are being compared (more points = line chart or bump chart)
- Highlighting which entities changed the most or reversed direction

## When NOT to Use
- More than two time points are being compared (use a line chart or bump chart)
- Too many entities create a spaghetti chart (limit to ~15 lines)
- Values are very similar and slopes are nearly flat, making differences hard to see (use a dumbbell plot instead)
- Part-to-whole relationships are the primary message

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| entity | categorical | The items being compared |
| before | numeric | Value at first time point |
| after | numeric | Value at second time point |
| category (optional) | categorical | For color grouping of entities |

## Best Practices
- Label both endpoints of each line directly on the chart
- Use color to encode category or direction (increase = green, decrease = red) rather than per-entity color when there are many lines
- Left-align start labels and right-align end labels for clean reading
- Ensure the y-axis starts at zero if relative magnitudes should be preserved
- Use consistent y-axis scale if comparing multiple slope charts side by side

## Common Mistakes
- Not sorting or ranking entities, making patterns hard to spot — see Smell D
- Using slope charts when the two time points are not directly comparable (different base populations)
- Adding more than two comparison points to a slope chart (becomes a cluttered line chart)
- Ignoring the baseline: slopes look steeper when the y-axis is truncated

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
for _, row in df.iterrows():
    ax.plot([0, 1], [row['before'], row['after']], 'o-', color='steelblue')
    ax.text(-0.05, row['before'], row['entity'], ha='right')
    ax.text(1.05, row['after'], row['entity'], ha='left')
ax.set_xticks([0, 1])
ax.set_xticklabels(['Before', 'After'])
```

### plotly
One `go.Scatter` trace per entity with `x=['Before', 'After']` and `y=[before_val, after_val]`.

### altair
`alt.Chart(df_melted).mark_line(point=True).encode(x='period:O', y='value:Q', color='entity:N', detail='entity:N')`

### excel / tableau
Tableau: Line chart with two-point time axis; one mark per entity. Excel: Line chart with two columns as x-axis points.

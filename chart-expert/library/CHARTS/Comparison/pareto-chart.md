---
name: Pareto Chart
category: Comparison
input_type: [cat-value]
it_variants: []
analytical_function: Ranking
visual_family: Chart
shape_primitive: [Bar, Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, d3, tableau, powerbi, excel]
failure_modes: [D, J]
alternatives: [bar-chart, horizontal-bar-chart, waterfall-chart]
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

# Pareto Chart

## Description
A Pareto chart combines a bar chart (categories sorted by frequency/magnitude, descending) with a cumulative percentage line overlaid on a secondary y-axis. Named after the Pareto Principle (the 80/20 rule), it helps identify the "vital few" factors that account for the majority of an effect. The bar chart shows individual category magnitudes; the cumulative line shows what percentage of the total is accounted for by categories up to that point.

## When to Use
- Quality control and root-cause analysis (identifying the most common defect types)
- Prioritization: finding the 20% of causes that drive 80% of outcomes
- Customer complaint analysis, bug category analysis, or cost driver identification
- When the cumulative contribution of ranked categories is the decision-relevant insight

## When NOT to Use
- Categories cannot be meaningfully ranked by frequency or magnitude (use a standard bar chart)
- The 80/20 or cumulative perspective adds no insight to the analysis
- Categories represent time periods (use a line chart or histogram instead)
- Relative composition of the total is more important than the cumulative ranking (use a stacked bar)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | The defect types, complaint categories, etc. |
| count / value | numeric | Frequency or magnitude; must be non-negative |

The chart requires pre-sorting by descending value and computing cumulative percentage.

## Best Practices
- Sort bars strictly by descending value — this is required, not optional — see Smell D
- Use a secondary y-axis (0–100%) for the cumulative percentage line
- Mark the 80% threshold with a horizontal reference line
- Use a single bar color; the cumulative line should use a contrasting color
- Label both the bar heights and the cumulative percentages at each point

## Common Mistakes
- Not sorting bars by descending value, defeating the entire purpose of the chart — see Smell D
- Silently dropping small categories instead of rolling them into "Other" — see Smell J
- Confusing the primary and secondary y-axes in interpretation
- Using a Pareto chart when categories have equal frequencies (the chart becomes a flat line with uniform bars)

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
df = df.sort_values('count', ascending=False)
df['cumulative_pct'] = df['count'].cumsum() / df['count'].sum() * 100

fig, ax1 = plt.subplots()
ax1.bar(df['category'], df['count'], color='steelblue')
ax2 = ax1.twinx()
ax2.plot(df['category'], df['cumulative_pct'], 'r-o', markersize=4)
ax2.set_ylim(0, 110)
ax2.axhline(80, color='gray', linestyle='--')
plt.tight_layout()
```

### plotly
Combine `go.Bar` (descending sorted) with `go.Scatter` on a secondary y-axis for the cumulative percentage.

### altair
Layer `mark_bar` with `mark_line` using a dual-axis; compute cumulative percentage as a transform.

### excel / tableau
Excel: Insert > Pareto Chart (built-in from Excel 2016+). Tableau: Dual-axis combining a bar (sorted) and a running total line chart.

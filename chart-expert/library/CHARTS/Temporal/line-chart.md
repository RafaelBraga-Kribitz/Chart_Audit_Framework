---
name: Line Chart
category: Temporal
input_type: [time-series, xy-simple]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Line]
cardinality_fit: [medium, large]
audience: [Executive, Analytics, Technical, Public]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [L, B]
alternatives: [area-chart, sparkline, slope-chart, stepped-line-graph]
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

# Line Chart

## Description
A line chart displays quantitative values over a continuous interval or time period by connecting data points with straight line segments. The x-axis typically encodes time or an ordered sequence, while the y-axis encodes the measured value. Multiple series can be overlaid using distinct colors to enable direct comparison of trends.

## When to Use
- Showing how a metric changes over time (revenue, temperature, user counts)
- Comparing the trajectory of multiple series across the same time period
- Identifying trends, cycles, and turning points in sequential data
- Communicating rate of change between periods

## When NOT to Use
- Data has fewer than 3 time points (use a bar chart or slope chart instead)
- Values represent discrete, unordered categories
- You need to show part-to-whole relationships (use stacked area or pie)
- The lines cross so frequently they become illegible (limit to ~5-7 series)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date or ordered numeric | Must be sorted ascending |
| value | numeric | The measured quantity |
| series (optional) | categorical | Used to differentiate multiple lines |

## Best Practices
- Start the y-axis at zero only when the baseline is meaningful; truncating can be appropriate for showing variance
- Use consistent time intervals on the x-axis to avoid visual distortion
- Label lines directly at their endpoints rather than relying solely on a legend
- Limit to 5-7 lines before considering small multiples
- Use a dashed or lighter style for projected/forecast portions — see Smell A

## Common Mistakes
- Interpolating over long gaps in data as if values are known — see Smell L
- Showing a flat line on a zero-variance metric as if it is informative — see Smell B
- Encoding rank changes with a line chart when a bump chart is clearer
- Using a line chart for nominal categorical x-axis data

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(df['date'], df['value'], color='steelblue', linewidth=1.5)
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.set_title('Metric Over Time')
plt.tight_layout()
```

### plotly
Use `px.line(df, x='date', y='value', color='series')` or `go.Scatter(mode='lines')`.

### altair
`alt.Chart(df).mark_line().encode(x='date:T', y='value:Q', color='series:N')`

### excel / tableau
Excel: Insert > Line Chart. Tableau: drag date to Columns, measure to Rows; Marks card set to Line.

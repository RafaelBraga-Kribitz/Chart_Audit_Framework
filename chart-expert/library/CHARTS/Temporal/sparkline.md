---
name: Sparkline
category: Temporal
input_type: [time-series, xy-simple]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Line]
cardinality_fit: [medium, large]
audience: [Executive, Analytics, Technical]
complexity: Basic
encoding_channels: [position]
tool_support: [matplotlib, plotly, d3, tableau, powerbi, excel]
failure_modes: [L, B]
alternatives: [line-chart, area-chart]
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

# Sparkline

## Description
A sparkline is a small, word-sized line chart stripped of axes, labels, and gridlines, designed to be embedded inline within text, tables, or dashboards. Coined by Edward Tufte, sparklines convey the overall shape and trend of a time series at a glance without occupying large chart space. They sacrifice precise readability for density and contextual embedding.

## When to Use
- Embedding trend context within a data table (e.g., one sparkline per row to show historical trend)
- Dashboard KPI cards where a small trend indicator supplements a current value
- Comparing the shape of many time series simultaneously across table rows
- When screen real estate is severely limited but trend direction is still important

## When NOT to Use
- Precise values at specific time points need to be read (use a full line chart)
- The audience is not data-literate and needs axis context to interpret the shape
- There are fewer than 5–6 data points (a single number or bar is cleaner)
- Zero-variance data that produces a flat line with no signal — see Smell B

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date or ordered numeric | Sorted ascending |
| value | numeric | The metric; scaled to fit tiny dimensions |
| entity | categorical | Row identifier when one sparkline per row |

## Best Practices
- Minimum of 10–20 data points for the trend shape to be meaningful
- Highlight the endpoint or maximum with a small dot in a contrasting color
- Keep all sparklines in a table on the same y-scale if direct comparison is intended; document if scales differ
- Avoid all decoration: no axes, no labels, minimal or no stroke weight variation
- Width:height aspect ratio around 4:1 to 6:1 works well

## Common Mistakes
- Showing a flat sparkline for a metric with zero or near-zero variance, implying stability when it just has no range — see Smell B
- Using different y-scales per sparkline without clear indication, making shapes incomparable
- Smoothing sparklines to the point that the original data pattern is lost — see Smell L
- Using sparklines in contexts where readers need to read off specific values

## Implementation Notes

### matplotlib
```python
fig, ax = plt.subplots(figsize=(2, 0.5))
ax.plot(values, color='steelblue', linewidth=1)
ax.plot(len(values)-1, values[-1], 'o', color='red', markersize=3)
ax.axis('off')
plt.tight_layout(pad=0)
```

### plotly
Create a tiny `go.Scatter` trace with `showgrid=False`, hidden axes, and a small `width`/`height` in the layout.

### altair
`alt.Chart(df).mark_line(size=1).encode(x='date:T', y='value:Q').properties(width=100, height=25)` and suppress axes.

### excel / tableau
Excel: Insert > Sparklines (built-in from Excel 2010+). Tableau: Use a small line chart mark in a table-style layout with suppressed axes.

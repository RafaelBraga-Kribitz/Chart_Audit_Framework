---
name: Range Area Chart
category: Temporal
input_type: [interval-range, time-series]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Area, Line]
cardinality_fit: [medium, large]
audience: [Analytics, Technical, Public]
complexity: Intermediate
encoding_channels: [position, color-hue, color-value]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [C, L, B]
alternatives: [nested-area-chart, error-bars, line-chart, candlestick-chart]
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

# Range Area Chart

## Description
A range area chart fills the space between a lower bound and an upper bound over time, creating a shaded band that represents variability, uncertainty, or min-max spread at each time point. Unlike a standard area chart which fills from zero to a line, a range area chart fills between two boundary lines, optionally with a central estimate line through the middle.

## When to Use
- Showing temperature highs and lows over time
- Displaying min/max or percentile spread for a time series
- Communicating forecast confidence bands around a central projection
- Comparing the spread of two or more time-varying ranges

## When NOT to Use
- The lower and upper bounds do not represent a meaningful interval (use two separate lines)
- Zero-variance data where the band would collapse — see Smell B
- When individual data points matter more than the envelope (use a scatter plot)
- More than 3–4 overlapping bands (visual clutter becomes severe)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date or ordered numeric | Sorted ascending |
| lower | numeric | Lower boundary of the range |
| upper | numeric | Upper boundary; must be >= lower |
| central (optional) | numeric | Mean, median, or point estimate |

## Best Practices
- Fill the band with a semi-transparent color and draw the boundary lines explicitly
- Center line should use a distinct, fully opaque stroke
- Label what the boundaries represent (e.g., "p10–p90", "min–max")
- Use consistent y-axis zero baseline when absolute magnitude matters
- Avoid implying the band boundaries are hard limits when they are probabilistic

## Common Mistakes
- Mislabeling a simple percentile range as a credible interval — see Smell C
- Smoothing band edges to hide actual data noise — see Smell L
- Zero-variance broadcast: showing a degenerate band when uncertainty is actually zero — see Smell B
- Overlapping multiple semi-transparent bands without clear labeling of each

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.fill_between(df['date'], df['lower'], df['upper'],
                alpha=0.3, color='steelblue', label='Range')
ax.plot(df['date'], df['central'], color='steelblue',
        linewidth=2, label='Central estimate')
ax.legend()
plt.tight_layout()
```

### plotly
Use `go.Scatter(fill='tonexty')` with a lower boundary trace followed by an upper boundary trace.

### altair
`alt.Chart(df).mark_area(opacity=0.3).encode(x='date:T', y='lower:Q', y2='upper:Q')`

### excel / tableau
Tableau: Use a dual-axis approach with band calculation fields for lower and upper bounds. Excel: Use an area chart with a transparent lower series and a stacked difference series.

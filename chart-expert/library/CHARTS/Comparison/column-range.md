---
name: Column Range Chart
category: Comparison
input_type: [interval-range, cat-multi-value]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical, Executive]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [plotly, matplotlib, d3, tableau, powerbi, excel]
failure_modes: [B]
alternatives: [span-chart, error-bars, candlestick-chart, column-range]
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

# Column Range Chart

## Description
A column range chart is the vertical (column-oriented) version of the span chart. It displays floating vertical bars where each bar's bottom and top positions represent the lower and upper bounds of a range for each category. The y-axis is continuous, and the bar neither starts from zero nor extends to the top — it floats between its two boundary values. Common in weather charts (daily temperature highs and lows) and financial charting.

## When to Use
- Showing daily/weekly high and low values (temperature, stock price, heart rate)
- Comparing the spread or variance of a metric across discrete categories
- When column-oriented layout is conventional for the domain (e.g., temperature charts)
- Displaying confidence or tolerance intervals per category in a vertical layout

## When NOT to Use
- Absolute magnitude from zero is the key comparison (use a standard bar chart)
- Too many categories make vertical floating bars too narrow to distinguish
- Time is continuous with many intervals (use a range area chart)
- Zero-variance data where columns collapse to horizontal lines — see Smell B

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical or date | X-axis grouping |
| lower | numeric | Bottom of each column (minimum value) |
| upper | numeric | Top of each column (maximum value); must be >= lower |
| central (optional) | numeric | Point estimate within the range |

## Best Practices
- Use a consistent fill color with a clear stroke to define column boundaries
- Add a point or crosshatch marker for the central value (mean/median)
- Label the y-axis clearly with the metric name and units
- Sort categories by lower bound, upper bound, or range width to reveal patterns
- Use gridlines to help readers map column tops and bottoms to axis values

## Common Mistakes
- Degenerate columns (lower == upper) from zero-variance data — see Smell B
- Omitting a central estimate when it is available, losing important information
- Using column range charts for data that should be on a continuous time axis (use range area)
- Not labeling whether the bounds represent min/max, IQR, or confidence intervals

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
for i, (cat, low, high) in enumerate(zip(categories, lowers, uppers)):
    ax.bar(i, high - low, bottom=low, width=0.6,
           color='steelblue', edgecolor='white', alpha=0.7)
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories, rotation=45, ha='right')
plt.tight_layout()
```

### plotly
`go.Bar(x=categories, base=lowers, y=[u - l for u, l in zip(uppers, lowers)])`

### altair
`alt.Chart(df).mark_bar().encode(x='category:N', y='lower:Q', y2='upper:Q')`

### excel / tableau
Excel: Stacked column chart with invisible lower series (same fill as background) + visible range series. Tableau: Gantt bar with continuous axis, lower bound encoded as the position.

---
name: Span Chart
category: Comparison
input_type: [interval-range, cat-multi-value]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Bar, Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [B]
alternatives: [error-bars, range-area-chart, dumbbell-plot, column-range]
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

# Span Chart

## Description
A span chart (also called a floating bar chart or range bar chart) displays the range between a minimum and maximum value for each category using a horizontal or vertical bar that "floats" between the two boundary values. Unlike a standard bar chart anchored at zero, span chart bars are anchored at their lower boundary and extend to their upper boundary, visually encoding the span or spread of each category.

## When to Use
- Comparing the range (min-max, IQR, or confidence interval) across categories
- Displaying temperature ranges, salary bands, or project duration ranges per category
- When the width of the interval, not an absolute value from zero, is the key comparison
- Budget ranges or cost estimates with minimum and maximum bounds per item

## When NOT to Use
- Absolute magnitude from zero is the primary comparison (use a standard bar chart)
- Data has zero or near-zero variance, making all spans degenerate — see Smell B
- Time series data (use a range area chart instead)
- Very many categories where floating bars become too dense

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | The groups being compared |
| lower | numeric | The lower boundary of the span |
| upper | numeric | The upper boundary; must be >= lower |
| central (optional) | numeric | Midpoint or median for an additional marker |

## Best Practices
- Sort categories by span width, lower bound, or upper bound depending on the story
- Use a consistent color for all bars unless color encodes a meaningful grouping
- Add a point marker for the central value (mean, median) inside each span when available
- Label span endpoints (lower and upper values) when precision is needed
- Use horizontal orientation when category labels are long

## Common Mistakes
- Showing span charts with zero-variance data where all spans collapse to points — see Smell B
- Using span charts to show absolute magnitude when a zero-based bar is more appropriate
- Conflating the span (range) with a confidence interval without documenting what the boundaries represent
- Not labeling what the lower and upper bounds represent

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
for _, row in df.iterrows():
    ax.plot([row['category'], row['category']],
            [row['lower'], row['upper']],
            color='steelblue', linewidth=8, solid_capstyle='butt', alpha=0.6)
    ax.plot(row['category'], row['central'], 'o',
            color='white', markersize=6, zorder=5)
plt.tight_layout()
```

### plotly
`go.Bar` with `base=df['lower']` and `y=df['upper'] - df['lower']` (or horizontal equivalent).

### altair
`alt.Chart(df).mark_bar().encode(x='category:N', y='lower:Q', y2='upper:Q')`

### excel / tableau
Tableau: Gantt bar mark with lower bound on the axis and span as the size. Excel: Stacked bar with invisible lower series plus visible difference series.

---
name: Waterfall Chart
category: Composition
input_type: [cat-value]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [I, J]
alternatives: [stacked-bar-100pct, funnel-chart, pareto-chart]
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
# Waterfall Chart

## Description
A Waterfall Chart (also called a Bridge Chart or Mario Chart) shows how an initial value is affected by a series of intermediate positive and negative contributions to arrive at a final value. Each bar floats at the cumulative running total from the previous bar, with bars coloured to indicate increases (typically green) or decreases (red). Subtotal and total bars touch the baseline. It is widely used in financial reporting to decompose P&L, budget variances, or cash flow changes.

## When to Use
- Decomposing a start value into contributing factors to reach an end value (e.g., revenue bridge)
- Financial analysis: P&L breakdown, budget vs. actuals variance, cash flow
- Showing the cumulative effect of sequential positive and negative changes

## When NOT to Use
- More than ~15 bars (chart becomes too wide to read)
- When showing temporal trends rather than cumulative contributions (use a line chart)
- When bars do not have a meaningful additive relationship

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| label | categorical (ordered) | Category name for each bar |
| value | numeric | Signed change (+/-) for intermediate bars; absolute for start/end |
| type | categorical | "increase", "decrease", "total", or "subtotal" — drives colour |

## Best Practices
- Use green for positive contributions, red for negative, grey for subtotals/totals
- Annotate each bar with its value (signed for intermediates, absolute for totals)
- Draw connector lines between bars to guide the eye
- Sort intermediate bars by magnitude if the sequence is not inherently ordered

## Common Mistakes
- Bars that are not additive (e.g., mixing percentage changes with absolute values) (smell I)
- Omitting subtotal bars in long sequences, making it hard to track running totals
- Using this chart for data that does not sum to a meaningful total
- Silently dropping near-zero items that are nonetheless important (smell J)

## Implementation Notes

### matplotlib
```python
# Compute running cumulative for bar bottoms
running = pd.Series(values).cumsum().shift(1).fillna(0)
colors = ['green' if v >= 0 else 'red' for v in values]
ax.bar(labels, np.abs(values), bottom=running, color=colors)
```

### plotly
`go.Waterfall(measure=measures, x=labels, y=values, connector=dict(line=dict(color='grey')))` — native waterfall trace.

### altair
Not natively supported; compute cumulative bottoms manually and use `mark_bar()` with `y` and `y2` encodings.

### excel / tableau
**Excel**: Insert → Waterfall Chart (Excel 2016+). **Tableau**: Use Gantt bar chart with cumulative calculated fields.

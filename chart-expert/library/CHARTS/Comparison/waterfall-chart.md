---
name: Waterfall Chart
category: Comparison
input_type: [cat-value]
it_variants: []
analytical_function: Deviation
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [plotly, matplotlib, d3, tableau, powerbi, excel]
failure_modes: [I, D]
alternatives: [bar-chart, pareto-chart, stacked-bar-chart]
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

# Waterfall Chart

## Description
A waterfall chart shows how an initial value is incrementally increased or decreased by a series of positive and negative contributions to reach a final total. Each bar "floats" at the cumulative running total, with upward bars (typically green) showing increases and downward bars (typically red) showing decreases. Opening and closing totals are shown as full-height anchored bars. It is the standard chart for financial variance analysis and bridge charts.

## When to Use
- Financial analysis: showing how revenues minus costs build to a profit figure
- Variance analysis: bridging from actual to plan, or from one period to the next
- Explaining what drove a change in a metric from a starting point to an ending point
- Budget waterfalls: showing how starting budget is consumed by each line item

## When NOT to Use
- Contributions are not additive or don't logically build on each other — see Smell I
- The order of contributions is arbitrary (the sequential order should be meaningful)
- Very many contributions (>12) make the chart too wide to read
- The audience needs to compare contribution magnitudes across multiple scenarios (use a grouped bar)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| label | string | Name of each step (revenue, COGS, operating expense, etc.) |
| value | numeric | Positive for increases, negative for decreases |
| type | categorical | "start", "increase", "decrease", or "total" — controls color and anchor |

## Best Practices
- Use green for positive contributions, red for negative, and gray/blue for start and total bars
- Show the running total value label on each bar
- Connector lines between bar tops can help readers track the cumulative value
- Sort contributions by magnitude only if the sequential narrative allows it
- Label the net change explicitly between the start and end totals

## Common Mistakes
- Using non-additive contributions that don't logically sum to the end total — see Smell I
- Placing contributions in an arbitrary order instead of a logical narrative sequence — see Smell D
- Omitting subtotals when there are many steps, making it hard to track intermediate running totals
- Confusing the floating bar baseline — each bar starts where the previous one ended

## Implementation Notes

### matplotlib
Requires manual computation of bar bottoms:
```python
import matplotlib.pyplot as plt
running = 0
for label, val in zip(labels, values):
    bottom = min(running, running + val)
    height = abs(val)
    color = 'green' if val > 0 else 'red'
    ax.bar(label, height, bottom=bottom, color=color)
    running += val
```

### plotly
`go.Waterfall(name='', measure=['relative','relative',...,'total'], x=labels, y=values)`

### altair
Not natively supported; requires pre-computed bottom and top values for each bar as a layered `mark_bar`.

### excel / tableau
Excel: Insert > Waterfall Chart (built-in from Excel 2016+). Tableau: Use stacked bar chart with invisible baseline bars and color-coded visible bars.

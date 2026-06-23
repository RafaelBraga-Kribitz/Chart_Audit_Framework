---
name: Butterfly Chart
category: Comparison
input_type: [demo-grouped, cat-multi-value]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive, Public]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [D, J]
alternatives: [population-pyramid, grouped-bar-chart, dumbbell-plot]
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

# Butterfly Chart

## Description
A butterfly chart (also called a back-to-back bar chart or tornado chart) places two horizontal bar series back-to-back, sharing a central categorical y-axis. One series extends to the left and the other to the right, allowing direct visual comparison of two groups across the same categories. The symmetrical layout makes it easy to see which group leads or lags for each category.

## When to Use
- Comparing two groups (e.g., male/female, before/after, product A/B) across multiple categories simultaneously
- Survey data where two groups answer the same set of questions
- Demographic breakdowns comparing two populations
- When the sign/direction of the difference (not just magnitude) is part of the message

## When NOT to Use
- More than two comparison groups (use a grouped bar chart or small multiples)
- The two series have very different value ranges, making the shared axis misleading
- Categories are too numerous to fit vertically without scrolling
- Part-to-whole is the primary message (use a stacked bar chart)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | Shared y-axis categories |
| group_left | numeric | Values for the left-facing series (will be negated visually) |
| group_right | numeric | Values for the right-facing series |

## Best Practices
- Use contrasting colors for the two series (one per side) and label them clearly
- The central axis should be a clean dividing line with category labels
- Use absolute values on both axes (not negative numbers for the left side)
- Sort categories by one group's value or by their difference to reveal patterns
- Include value labels at the ends of each bar for precise reading

## Common Mistakes
- Not sorting categories by a meaningful criterion — see Smell D
- Using the same color for both sides, making the two groups indistinguishable
- Silently dropping categories where one group has no data — see Smell J
- Using widely different x-axis scales on left and right, distorting apparent symmetry

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.barh(categories, group_right, color='steelblue', label='Group B')
ax.barh(categories, [-v for v in group_left], color='coral', label='Group A')
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xticks([-max_val, -max_val/2, 0, max_val/2, max_val])
ax.set_xticklabels([str(max_val), str(max_val//2), '0',
                     str(max_val//2), str(max_val)])
ax.legend()
plt.tight_layout()
```

### plotly
Use two `go.Bar` traces with `orientation='h'`; negate the left-side values and customize tick labels to show absolute values.

### altair
Use two layered `mark_bar()` charts with one series negated; share the y-axis.

### excel / tableau
Tableau: Dual-axis horizontal bar chart; negate one measure and set axis labels to absolute. Excel: Manual workaround with a bar chart using negated values for one group.

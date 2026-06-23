---
name: Dumbbell Plot
category: Comparison
input_type: [cat-multi-value, demo-grouped]
it_variants: []
analytical_function: Comparison
visual_family: Plot
shape_primitive: [Line, Circle]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical, Executive]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [D]
alternatives: [slope-chart, lollipop-chart, grouped-bar-chart, dot-plot]
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

# Dumbbell Plot

## Description
A dumbbell plot (also called a connected dot plot or gap chart) displays two data points per row connected by a horizontal line, resembling a dumbbell weight. Each row represents a category, and the two endpoints represent two different groups, time points, or conditions. The gap between the endpoints immediately communicates both the direction and magnitude of the difference.

## When to Use
- Showing the difference between two values for each category (before/after, group A/B)
- When the gap and direction of change per category is the primary message
- A cleaner alternative to a grouped bar chart when only two groups are compared
- Highlighting which categories have the largest or smallest gaps

## When NOT to Use
- More than two comparison points per row (use a slope chart or parallel coordinates)
- The audience needs to compare absolute values across rows (the floating position makes this hard)
- Categories need to be compared on a common zero baseline (use a grouped bar chart)
- Very similar values where the connecting line becomes almost a point

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | Each row in the plot |
| value_start | numeric | First comparison point (e.g., Group A or Before) |
| value_end | numeric | Second comparison point (e.g., Group B or After) |

## Best Practices
- Sort rows by the gap (value_end - value_start) to reveal which categories changed most — see Smell D
- Use distinct colors for the two endpoint dots; keep the connecting line neutral gray
- Label the two point colors clearly in a legend or annotation
- Optionally add value labels at each endpoint
- Include a reference line or zero-gap line to show neutral position if relevant

## Common Mistakes
- Leaving categories in alphabetical or arbitrary order instead of sorting by gap — see Smell D
- Using the same color for both endpoints, making them indistinguishable
- Using a dumbbell plot when more than two comparison points exist (gets confusing)
- Placing the chart on a non-zero x-axis, making gap magnitudes non-comparable visually

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
for _, row in df.iterrows():
    ax.plot([row['value_start'], row['value_end']],
            [row['category'], row['category']],
            color='gray', linewidth=1.5, zorder=1)
    ax.scatter(row['value_start'], row['category'],
               color='steelblue', s=80, zorder=2)
    ax.scatter(row['value_end'], row['category'],
               color='coral', s=80, zorder=2)
plt.tight_layout()
```

### plotly
Combine `go.Scatter` for the connecting lines with `go.Scatter(mode='markers')` for the two endpoint series.

### altair
Layer `mark_rule` (connecting the two values on each row) with two `mark_point` transforms for the two endpoint groups.

### excel / tableau
Tableau: Dual-axis scatter plot with one axis per endpoint group; connect with a line mark. Excel: Line chart with two data series plotted against categories.

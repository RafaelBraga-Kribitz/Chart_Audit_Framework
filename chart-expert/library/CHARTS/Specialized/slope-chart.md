---
name: Slope Chart
category: Specialized
input_type: [cat-multi-value, time-series]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Line, Circle]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive]
complexity: Basic
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [J]
alternatives: [dumbbell-plot, bump-chart, line-chart]
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
# Slope Chart

## Description
A Slope Chart (also called a Slopegraph, popularised by Edward Tufte) shows change between exactly two time points or states for multiple categories. Each category is a line connecting its value at Point A (left axis) to its value at Point B (right axis). The slope of the line encodes direction and relative magnitude of change. Unlike a Bump Chart (ranks only) or a Dumbbell Plot (gaps on a single axis), a Slope Chart works with actual metric values on both axes.

## When to Use
- Before-and-after comparison for many categories across exactly two time points
- Showing which entities increased and which decreased, and by how much
- "Then vs. Now" comparisons: pre/post policy, start-of-year vs. end-of-year

## When NOT to Use
- More than 2 time points (use a Line Chart or Bump Chart)
- Too many crossing lines creating a visual tangle (limit to ~15 entities)
- When ranks not values are the story (use Bump Chart)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| entity | categorical | One line per entity |
| point_a | numeric | Value at the "before" state |
| point_b | numeric | Value at the "after" state |
| label_a | string | Label for the left axis column |
| label_b | string | Label for the right axis column |

## Best Practices
- Label entity names and values at both endpoints — avoid a separate legend
- Use colour to highlight entities with the largest slopes (positive and negative)
- Grey out unimportant entities to reduce clutter
- Sort left-axis values from high to low to reduce label overlap

## Common Mistakes
- Too many entity lines creating unreadable crossings — highlight top N, grey the rest
- Not labelling both endpoints, forcing viewers to trace lines across the chart
- Silently dropping entities with missing values at either endpoint (smell J)
- Using slope chart when more than 2 time points are available

## Implementation Notes

### matplotlib
```python
for _, row in df.iterrows():
    ax.plot([0, 1], [row.point_a, row.point_b], 'o-',
            color=color_map[row.entity], linewidth=1.5)
    ax.text(-0.05, row.point_a, f"{row.entity}: {row.point_a}", ha='right')
    ax.text(1.05, row.point_b, f"{row.entity}: {row.point_b}", ha='left')
ax.set_xticks([0, 1])
ax.set_xticklabels([label_a, label_b])
```

### plotly
`go.Scatter(x=[label_a, label_b], y=[val_a, val_b], mode='lines+markers+text', name=entity)` per entity.

### altair
`mark_line()` + `mark_point()` with a binary x encoding (before/after) and `color='entity:N'`.

### excel / tableau
**Tableau**: Line chart with two-period x-axis; label both ends. **Excel**: Line chart with two data columns as x-axis values.

---
name: Gantt Chart
category: Specialized
input_type: [interval-range, cat-multi-value]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics]
complexity: Basic
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, d3, tableau, powerbi, excel]
failure_modes: [J]
alternatives: [swimlane-chart, timeline-chart]
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
# Gantt Chart

## Description
A Gantt Chart is a horizontal bar chart where each bar represents a task or project phase, with its position encoding the start date and its length encoding the duration. The y-axis lists tasks; the x-axis is a time scale. Colour can encode task category, owner, or status. Dependency arrows can be added to show which tasks must complete before others begin. Developed by Henry Gantt around 1910–1915, it remains the standard project scheduling visualisation.

## When to Use
- Project planning and schedule communication
- Showing task durations, start/end dates, and dependencies on a timeline
- Progress tracking: planned vs. actual completion with colour distinction

## When NOT to Use
- Non-sequential or purely process-based workflows (use Flow Chart or Swimlane)
- Very large projects with hundreds of tasks where overview and detail are impossible simultaneously
- When task relationships and dependencies are more important than timing (use network CPM diagram)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| task | string | Task name |
| start | date/datetime | Task start date |
| end | date/datetime | Task end date |
| category | categorical (optional) | Group or owner; drives colour |
| completion | numeric [0–1] (optional) | Progress percentage for status overlay |
| dependencies | string (optional) | Comma-separated prerequisite task names |

## Best Practices
- Sort tasks by start date or by work breakdown structure (WBS) hierarchy
- Use a "today" vertical line marker for status reviews
- Colour-code by team/owner or status (On Track / At Risk / Complete)
- Limit to 20–30 tasks per view; provide drill-down or filtering for larger projects

## Common Mistakes
- Omitting dependency arrows when task sequencing is critical
- Not distinguishing planned vs. actual progress (single bar hides delays)
- Silently omitting tasks with missing dates (smell J)
- Using Gantt for work that has no time-bounded deliverables

## Implementation Notes

### matplotlib
```python
for i, row in tasks.iterrows():
    ax.barh(i, (row.end - row.start).days, left=row.start_num,
            color=category_color[row.category], edgecolor='white')
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels(tasks.task)
ax.xaxis_date()
```

### plotly
`go.Bar` with `orientation='h'`, `base=start_dates`, `x=durations` — or use `px.timeline()` from Plotly Express.

### altair
`mark_bar()` with `x=alt.X('start:T')`, `x2='end:T'`, `y='task:N'`.

### excel / tableau
**Excel**: Stacked bar chart with invisible first segment as offset. **Tableau**: Gantt Bar mark type with Start on Columns and Duration on Size.

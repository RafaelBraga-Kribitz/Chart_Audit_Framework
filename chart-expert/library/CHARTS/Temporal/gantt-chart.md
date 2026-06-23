---
name: Gantt Chart
category: Temporal
input_type: [interval-range, cat-value]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [plotly, matplotlib, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [timeline, bubble-timeline]
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

# Gantt Chart

## Description
A Gantt chart uses horizontal bars to represent tasks or activities, with each bar's length proportional to the duration of that task and its position along the time axis indicating when it starts and ends. Tasks are listed vertically, and the chart provides a clear view of project schedules, overlapping tasks, and resource allocation across time.

## When to Use
- Project management: visualizing task schedules, dependencies, and timelines
- Communicating a project roadmap to stakeholders
- Resource planning where task overlaps and concurrent activities need to be visible
- Sprint planning or release schedule visualization

## When NOT to Use
- Event sequences with no meaningful duration (use a timeline)
- More tasks than can fit vertically on a single screen (consider collapsing into phases)
- When task dependencies and their critical path are the primary focus (use a network diagram)
- Exact start/end times are not available

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| task | string | Task or activity name |
| start | date | Task start date/time |
| end | date | Task end date/time |
| category / resource (optional) | categorical | For color-coding by team, phase, or type |
| completion (optional) | numeric (0-1) | Percentage complete for progress overlay |

## Best Practices
- Sort tasks by start date or by project phase for logical reading order
- Use color to encode category or owner, not duration
- Add a vertical "today" line to indicate current progress
- For large projects, collapse into phase-level summaries with expandable detail
- Show dependencies as arrows only when they are few and critical

## Common Mistakes
- Overloading with hundreds of tasks, making the chart unreadable
- Using color for pure decoration rather than categorical information
- Showing Gantt charts without a visible current-date reference
- Conflating task completion percentage with time elapsed

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
fig, ax = plt.subplots(figsize=(10, 5))
for i, row in df.iterrows():
    ax.barh(row['task'], (row['end'] - row['start']).days,
            left=row['start'], color='steelblue', edgecolor='white')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.tight_layout()
```

### plotly
`px.timeline(df, x_start='start', x_end='end', y='task', color='category')`

### altair
`alt.Chart(df).mark_bar().encode(x='start:T', x2='end:T', y='task:N', color='category:N')`

### excel / tableau
Excel: Stacked bar chart workaround (hidden baseline bar + visible duration bar). Tableau: Gantt chart mark type with start date on x-axis and duration as size encoding.

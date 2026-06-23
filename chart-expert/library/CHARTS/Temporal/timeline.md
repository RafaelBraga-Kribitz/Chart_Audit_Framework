---
name: Timeline
category: Temporal
input_type: [event-time, interval-range]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Line, Dot, Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Public, Analytics]
complexity: Basic
encoding_channels: [position, color-hue, shape]
tool_support: [matplotlib, plotly, d3, tableau, powerbi]
failure_modes: []
alternatives: [gantt-chart, bubble-timeline, scatter-plot]
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

# Timeline

## Description
A timeline places events or milestones along a single temporal axis, using markers, labels, and optional connectors to show when events occurred and their sequence. It can represent point events (a single moment) or duration events (a span between start and end). Timelines are among the most intuitive and widely used visualizations for communicating chronology.

## When to Use
- Showing the sequence and timing of historical events, project milestones, or product releases
- Communicating a narrative where chronological order is the organizing principle
- Presenting a project schedule or roadmap at a high level
- Visualizing the lifecycle of items with discrete start/end moments

## When NOT to Use
- Events are so numerous they overlap and become illegible (use a Gantt chart or heatmap calendar)
- Quantitative comparison of event durations is the primary goal (use a Gantt chart)
- The relationship between events (not just sequence) is the story (use a flow diagram)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| event_date | date | Point timestamp for instantaneous events |
| start_date | date | For interval events |
| end_date | date | For interval events; null for point events |
| label | string | Event name / description |
| category (optional) | categorical | For color-coding lanes or groups |

## Best Practices
- Alternate labels above and below the axis line to prevent overlap for dense timelines
- Use visual hierarchy: larger or bolder markers for major milestones vs. minor events
- Group related events into lanes or color categories for multi-stream timelines
- Provide enough whitespace — cluttered timelines are harder to read than sparse ones
- Include a consistent, labeled time scale (year ticks, quarter marks)

## Common Mistakes
- Placing too many events at the same granularity without visual hierarchy
- Using proportionally incorrect spacing (equal visual spacing for unequal time intervals)
- Missing a consistent temporal scale that allows the reader to judge durations
- Labeling event names so long they overlap and become unreadable

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 3))
ax.hlines(0, xmin, xmax, color='gray', linewidth=1)
for i, (date, label) in enumerate(events):
    ax.plot(date, 0, 'o', color='steelblue', markersize=8)
    ax.text(date, 0.1 if i % 2 == 0 else -0.15, label,
            ha='center', va='bottom' if i % 2 == 0 else 'top', fontsize=8)
ax.axis('off')
plt.tight_layout()
```

### plotly
`go.Scatter` with `y=0` for all events and text annotations; or use `plotly.figure_factory.create_gantt` for interval events.

### altair
`alt.Chart(df).mark_point().encode(x='event_date:T', y=alt.value(0), tooltip='label:N')`

### excel / tableau
Tableau: SmartArt or a scatter chart with date on x-axis, constant y value, and text marks. Excel: Use SmartArt Timeline or format a scatter chart.

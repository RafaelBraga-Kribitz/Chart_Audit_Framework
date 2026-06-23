---
name: Swimlane Chart
category: Specialized
input_type: [cat-multi-value, interval-range]
it_variants: []
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Bar, Polygon, Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical, Executive]
complexity: Intermediate
encoding_channels: [position, color-hue, length]
tool_support: [matplotlib, plotly, d3]
failure_modes: [J]
alternatives: [gantt-chart, flow-chart]
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
# Swimlane Chart

## Description
A Swimlane Chart (also called a Cross-Functional Flowchart or Pool/Lane Diagram) extends a Flow Chart by organising process steps into horizontal (or vertical) lanes, each representing a different actor, department, team, or system. Steps within the same lane are the responsibility of that actor; handoffs between lanes show transitions of ownership. It is widely used in business process modelling (BPMN), UX journey maps, and cross-functional project documentation.

## When to Use
- Documenting business processes that cross multiple departments, teams, or systems
- Showing handoffs and responsibilities between actors in a workflow
- UX journey mapping showing user, system, and team touchpoints across stages
- BPMN process modelling and process improvement documentation

## When NOT to Use
- Processes owned by a single actor (use a simple flowchart)
- When timing and duration are more important than responsibility (use Gantt Chart)
- Very complex processes with many branches where a swimlane would become unwieldy

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| step_id | string | Unique process step identifier |
| step_label | string | Step description |
| lane | categorical | Actor/department responsible for this step |
| sequence | integer | Step order in the process |
| next_steps | string(s) | Connected step ids |
| type | categorical | "process", "decision", "start", "end" |

## Best Practices
- Use the same symbol conventions as Flow Charts within each lane
- Draw handoffs as arrows crossing lane boundaries — these are the key risk points
- Colour lanes distinctly but simply; too many colours reduces clarity
- Limit to 4–6 lanes per chart; split complex processes into sub-processes

## Common Mistakes
- Too many lanes making each lane too narrow to read
- Steps that span multiple lanes (unclear ownership — should be resolved before charting)
- Omitting handoff arrows between lanes, hiding cross-functional dependencies (smell J)
- Using swimlane for a single-actor process where a simple flowchart would suffice

## Implementation Notes

### matplotlib
```python
# Draw horizontal lane backgrounds
for i, lane in enumerate(lanes):
    ax.fill_between([0, chart_width], [i*lane_h, i*lane_h],
                    [(i+1)*lane_h, (i+1)*lane_h], alpha=0.1, color=colors[i])
    ax.text(-0.5, (i+0.5)*lane_h, lane, va='center', fontsize=10)
# Then draw steps as rectangles within each lane
```

### plotly
Use `go.Scatter` with text mode for step labels and shapes for lane backgrounds; add arrows via `add_annotation`.

### altair
Not well-suited; use `mark_rect()` for lane backgrounds and manual positioning for process steps.

### excel / tableau
**Excel**: Draw manually with shapes. **Tableau**: Not suited for process documentation. Dedicated tools: Lucidchart, draw.io, Microsoft Visio, Miro.

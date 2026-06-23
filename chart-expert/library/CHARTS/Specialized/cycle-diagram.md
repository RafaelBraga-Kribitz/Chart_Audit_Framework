---
name: Cycle Diagram
category: Specialized
input_type: [cat-multi-value]
it_variants: []
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Circle, Line, Polygon]
cardinality_fit: [small-N]
audience: [Executive, Public]
complexity: Basic
encoding_channels: [position, color-hue, angle]
tool_support: [matplotlib, d3]
failure_modes: []
alternatives: [flow-chart, sankey-diagram]
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
# Cycle Diagram

## Description
A Cycle Diagram represents a repeating, circular process where each stage feeds into the next and the last stage returns to the first. Stages are arranged in a circular or elliptical pattern with arrows showing the direction of the cycle. It is a conceptual rather than quantitative diagram, used to communicate continuous processes, feedback loops, recurring workflows, and systems thinking concepts. Common examples include product development cycles, the water cycle, sales cycles, and PDCA (Plan-Do-Check-Act).

## When to Use
- Representing a recurring process where no step has a definitive "start" or "end"
- Communicating continuous improvement cycles (PDCA, Agile sprints, OKR cycles)
- Showing ecological, biological, or physical cycles (water cycle, carbon cycle)
- When the circular flow metaphor reinforces the message of continuity and repetition

## When NOT to Use
- Linear processes with a clear start and end (use a Flow Chart)
- When the number of stages exceeds ~8 (the circular layout becomes crowded)
- When stage durations or volumes need to be encoded (use Gantt or Sankey instead)

## Data Requirements
A Cycle Diagram is primarily conceptual:
| Column | Type | Notes |
|--------|------|-------|
| stage | string | Name of each stage |
| order | integer | Sequence around the cycle |
| description | string (optional) | Brief stage description |
| duration | numeric (optional) | If stages have different durations, can be encoded in arc size |

## Best Practices
- Keep stage labels brief (1–3 words); use a sub-label or tooltip for description
- Use directional arrows between stages to communicate the direction of flow
- Limit to 4–8 stages; fewer stages allow more description per stage
- Apply distinct colours to stages to make them individually identifiable

## Common Mistakes
- More than 8 stages making the cycle impossible to read in circular layout
- Arrows that don't clearly indicate direction (bidirectional when the cycle is unidirectional)
- Using a cycle diagram for a linear process where there is no natural loop
- Unequal arc widths implying different stage durations when all stages are equal

## Implementation Notes

### matplotlib
```python
# Place n stages equally around a circle
n = len(stages)
angles = np.linspace(0, 2*np.pi, n, endpoint=False)
for i, (angle, stage) in enumerate(zip(angles, stages)):
    x, y = np.cos(angle), np.sin(angle)
    ax.scatter(x, y, s=2000, color=colors[i], zorder=5)
    ax.text(x*1.3, y*1.3, stage, ha='center', va='center')
    # Draw arrow to next stage
    next_angle = angles[(i+1) % n]
    ax.annotate('', xy=(np.cos(next_angle), np.sin(next_angle)),
                xytext=(x, y), arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))
ax.axis('equal')
ax.axis('off')
```

### plotly
Construct with `go.Scatter` circles for nodes and `add_annotation` arrows in arc shapes.

### altair
Use polar-coordinate `mark_point()` for stage nodes with computed circular positions.

### excel / tableau
**Excel/PowerPoint**: Use SmartArt → Cycle layouts. **Tableau**: Not suited for concept diagrams.

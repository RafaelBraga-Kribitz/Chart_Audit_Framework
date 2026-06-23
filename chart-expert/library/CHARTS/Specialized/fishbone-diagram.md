---
name: Fishbone Diagram
category: Specialized
input_type: [hierarchical-cat]
it_variants: []
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: []
failure_modes: []
alternatives: [mind-map, flow-chart, swot-diagram]
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
# Fishbone Diagram

## Description
Also known as an Ishikawa Diagram or Cause-and-Effect Diagram. A Fishbone Diagram maps the potential causes of a specific problem or effect. The "head" of the fish on the right contains the problem statement; the "spine" is the central horizontal arrow pointing to it; "bones" branching off the spine represent major cause categories (often the "6 Ms": Man, Machine, Material, Method, Measurement, Mother Nature). Sub-causes branch further off the main bones. It is a structured brainstorming and root-cause analysis tool, not a data visualisation.

## When to Use
- Root cause analysis sessions for quality problems, failures, or defects
- Structured brainstorming to systematically explore the causes of a problem
- Six Sigma, Lean, and quality management contexts (DMAIC Define/Analyse phases)

## When NOT to Use
- When data already points to specific causes (use data-driven analysis instead)
- Complex multi-effect problems (each Fishbone should address a single effect)
- When the output will be static documentation without the analysis team's context

## Data Requirements
A Fishbone Diagram is a qualitative, text-driven tool:
| Element | Content |
|---------|---------|
| Effect | The problem or outcome statement |
| Main cause categories | Major branches (e.g., People, Process, Technology, Environment) |
| Sub-causes | Supporting causes under each category |

## Best Practices
- State the effect (head) precisely and specifically — not "quality problems" but "5% defect rate in Line 2"
- Use 4–6 main cause categories; don't create too many bones that dilute focus
- Validate causes with data after the brainstorming session
- Circle the most likely or impactful causes for follow-up investigation

## Common Mistakes
- Too many bone levels making the diagram hard to read
- Vague cause labels that don't point to actionable root causes
- Using a fishbone as a final analysis rather than a starting point for data investigation
- Including solutions in a causes diagram

## Implementation Notes

### matplotlib
```python
# Custom drawing: central spine + angled category bones + sub-branches
ax.annotate('', xy=(0.9, 0.5), xytext=(0.1, 0.5),
            arrowprops=dict(arrowstyle='->', lw=3))
ax.text(0.95, 0.5, 'Problem', ha='left', va='center', fontsize=12, fontweight='bold')
# Draw each bone as an angled line with category label
```

### plotly
Not suited for this diagram type; use declarative drawing tools instead.

### altair
Not applicable.

### excel / tableau
**Excel/PowerPoint**: Draw manually with shapes and connectors. Dedicated tools: Lucidchart, draw.io, Miro, or Microsoft Visio for fishbone templates.

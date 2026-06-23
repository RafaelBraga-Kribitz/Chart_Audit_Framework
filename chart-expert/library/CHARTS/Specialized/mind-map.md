---
name: Mind Map
category: Specialized
input_type: [hierarchical-cat]
it_variants: []
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Circle, Line]
cardinality_fit: [small-N, medium]
audience: [Executive, Public]
complexity: Basic
encoding_channels: [position, color-hue, area]
tool_support: [d3]
failure_modes: []
alternatives: [organisational-chart, network-diagram, dendrogram]
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
# Mind Map

## Description
A Mind Map is a radial diagram that organises concepts hierarchically around a central topic. The central node contains the main idea; branches radiate outward to sub-topics, which in turn branch further. It is primarily a thinking and note-taking tool designed to mirror associative thinking, rather than a data visualisation for quantitative analysis. Colour, imagery, and curved organic branches are typical stylistic features popularised by Tony Buzan.

## When to Use
- Brainstorming and idea generation around a central topic
- Communicating the scope and structure of a project or concept to stakeholders
- Personal knowledge management and note synthesis
- Presenting qualitative thematic analysis results

## When NOT to Use
- Quantitative data where values, sizes, or frequencies matter (use a chart with data encoding)
- Very deep hierarchies that require precise navigation (use Org Chart or Dendrogram)
- When the audience expects a formal diagram with consistent node styles

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| id | string | Unique concept identifier |
| label | string | Concept text |
| parent_id | string | Parent concept id; null for central node |
| color | string (optional) | Branch colour |

## Best Practices
- Keep branch labels concise (1–3 words per node)
- Use colours to group thematic branches
- Limit depth to 3–4 levels; deeper hierarchies become cluttered
- Place the most important or frequently referenced topics on primary branches

## Common Mistakes
- Overloading nodes with full sentences instead of keywords
- Mixing quantitative data with conceptual structure (use a chart instead)
- Creating overly complex mind maps that require a legend to interpret
- Using mind maps for formal documentation where org charts or process flows are more appropriate

## Implementation Notes

### matplotlib
Not well-suited; use radial tree layout via NetworkX + graphviz or Matplotlib manually.

### plotly
Pre-compute radial tree positions and render with `go.Scatter` for nodes and lines for edges.

### altair
Not natively supported.

### excel / tableau
Not natively available. Use dedicated mind mapping tools: XMind, MindMeister, Miro, Coggle, or draw.io.

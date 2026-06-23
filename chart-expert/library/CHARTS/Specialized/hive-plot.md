---
name: Hive Plot
category: Specialized
input_type: [cat-multi-value, matrix-grid]
it_variants: []
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Line, Circle]
cardinality_fit: [medium, large]
audience: [Technical, Analytics]
complexity: Advanced
encoding_channels: [position, color-hue, color-value]
tool_support: [d3]
failure_modes: [J]
alternatives: [network-diagram, arc-diagram, parallel-coordinates]
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
# Hive Plot

## Description
A Hive Plot is a rational, rule-based approach to network visualisation that places nodes along a small number of linear radial axes (typically 2–4 axes at fixed angles), with edges drawn as curved lines between axes. Unlike force-directed network diagrams where layout is non-deterministic, hive plots impose a deliberate structure: the axis a node is placed on and its position along that axis are determined by meaningful node attributes (e.g., degree, community, type). This makes patterns in the network interpretable and reproducible. Developed by Martin Krzywinski.

## When to Use
- Exploring large or complex networks where force-directed layouts produce uninterpretable hairballs
- Comparing network structure across different subsets or time periods (same rules → comparable layout)
- When node attributes provide a meaningful 2D classification (e.g., type × degree)

## When NOT to Use
- Small networks (<30 nodes) where a standard node-link diagram is sufficient
- Networks without meaningful node attributes for axis assignment
- Audiences not willing to learn the axis-encoding convention before reading the chart

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| node_id | string | Unique node identifier |
| axis | categorical | Which radial axis the node is assigned to |
| position | numeric | Node's position along its axis (e.g., degree, betweenness) |
| source | string | Source node for each edge |
| target | string | Target node for each edge |
| edge_weight | numeric (optional) | Edge curve colour or opacity |

## Best Practices
- Define axis assignment rules explicitly and document them in the chart caption
- Assign axis position based on a quantitative node attribute for interpretable ordering
- Use 2–3 axes; more than 4 reduces the layout clarity advantage
- Duplicate an axis (same nodes on two adjacent axes) to show within-group connections

## Common Mistakes
- Arbitrary or undocumented axis assignment rules defeating the reproducibility purpose
- Silently dropping nodes without a valid axis assignment (smell J)
- Using hive plot without explaining the layout rules to the reader
- Confusing hive plot with radar chart (very different visual and purpose)

## Implementation Notes

### matplotlib
Not natively available; requires custom implementation of radial axis layout and Bezier curve rendering.

### plotly
Not natively supported; requires manual computation of node positions on radial axes and edge curves.

### altair
Not natively supported.

### excel / tableau
Not available. Use D3.js with the `d3-hive` plugin for production hive plots.

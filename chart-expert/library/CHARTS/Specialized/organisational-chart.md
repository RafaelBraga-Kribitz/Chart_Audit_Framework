---
name: Organisational Chart
category: Specialized
input_type: [hierarchical-cat]
it_variants: []
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Polygon, Line]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Public]
complexity: Basic
encoding_channels: [position, color-hue, shape]
tool_support: [d3, plotly, tableau, powerbi]
failure_modes: [J]
alternatives: [dendrogram, network-diagram, treemap]
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
# Organisational Chart

## Description
An Organisational Chart (Org Chart) displays the hierarchical structure of an organisation, showing reporting relationships between roles, people, or departments. Nodes represent individuals or positions; directed edges (typically top-to-bottom) indicate authority or reporting lines. It is one of the oldest and most universally understood diagram types in business, and is used for onboarding, restructuring planning, and authority communication.

## When to Use
- Communicating the formal reporting structure of an organisation or team
- Planning and communicating restructuring or headcount changes
- Showing role-based hierarchies in process documentation

## When NOT to Use
- Non-hierarchical relationship networks (use Network Diagram)
- Very large organisations (>100 nodes) that require interactive drill-down
- When informal relationships or dotted-line reporting dominate the structure

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| id | string | Unique identifier for each role or person |
| name | string | Display name |
| parent_id | string | Manager's id; null/empty for root (CEO) |
| title | string (optional) | Role title |
| department | categorical (optional) | For colour grouping by dept |

## Best Practices
- Lay out top-down (CEO at top) or left-right for wide organisations
- Colour-code by department or function for large charts
- Show direct-reports only at the next level; expand on demand for interactive versions
- Include a search/filter capability for organisations > 50 nodes

## Common Mistakes
- Including every contractor or temp role cluttering the primary hierarchy
- Not showing dotted-line reporting relationships where they are significant (smell J for missing structure)
- Using the same layout for very deep (10+ levels) vs. wide (many direct reports) hierarchies
- Outdated charts that no longer reflect the current structure

## Implementation Notes

### matplotlib
Not well-suited; use graphviz via `networkx.drawing.nx_agraph.graphviz_layout` with `prog='dot'`.

### plotly
Use `go.Sunburst` or `go.Treemap` for compact hierarchical views, or pre-compute top-down tree positions and render with `go.Scatter`.

### altair
Not natively supported; compute tree layout externally and render with `mark_point()` + `mark_rule()`.

### excel / tableau
**Excel**: Insert → SmartArt → Hierarchy for small orgs. **Tableau**: Not natively available for complex org charts; use network data + node-link diagram workaround.

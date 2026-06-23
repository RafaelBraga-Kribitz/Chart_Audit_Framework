---
name: Hyperbolic Tree
category: Specialized
input_type: [hierarchical-cat]
it_variants: []
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Circle, Line]
cardinality_fit: [large, very-large]
audience: [Technical]
complexity: Advanced
encoding_channels: [position, color-hue, area]
tool_support: [d3]
failure_modes: [J]
alternatives: [dendrogram, treemap, organisational-chart]
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
# Hyperbolic Tree

## Description
A Hyperbolic Tree (also called a Hyperbolic Browser) renders hierarchical data on a hyperbolic plane projected onto a circular disc (Poincaré disc model). The focus node is placed at the centre of the disc; its context (parent, siblings, children) occupies the middle ring; deeper or less relevant nodes crowd toward the edge where space compresses. The user can interactively "focus" on any node by repositioning it to the centre. Developed at Xerox PARC (Lamping, Rao, Pirolli, 1995), it enables exploration of very large hierarchies because the non-Euclidean layout allocates exponentially more space near the centre.

## When to Use
- Browsing or exploring large hierarchies (hundreds to thousands of nodes) interactively
- File system navigation, ontology exploration, taxonomy browsers
- When the key requirement is "show me the local context around a focused node" rather than the global structure

## When NOT to Use
- Static, non-interactive presentations where the fish-eye effect is disorienting without interaction
- Hierarchies with fewer than ~50 nodes (simpler tree/dendrogram is more readable)
- When precise comparison of node attributes across the hierarchy is needed

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| id | string | Unique node identifier |
| parent | string | Parent node id; null for root |
| label | string | Display name |
| value | numeric (optional) | Node weight for size encoding |

## Best Practices
- Always provide interactive focus navigation (click to re-centre a node)
- Show labels only for the centre node and immediate neighbours
- Provide breadcrumb navigation so users can track their position in the hierarchy
- Offer a "reset" button to return to the root view

## Common Mistakes
- Using a static hyperbolic tree without interaction (the layout is incomprehensible without re-centring)
- Too many labelled nodes cluttering the edge of the disc
- Silently dropping deep-level nodes that don't render at the initial zoom (smell J)
- Expecting audiences without training to understand the non-Euclidean layout

## Implementation Notes

### matplotlib
Not practically implementable; the projection requires real-time interaction and complex Möbius transformations.

### plotly
Not natively supported.

### altair
Not supported.

### excel / tableau
Not available. Use D3.js with hyperbolic tree projection libraries, or Inxight Software's H3 Viewer (the original Xerox PARC implementation).

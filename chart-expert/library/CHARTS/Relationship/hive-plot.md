---
name: Hive Plot
category: Relationship
input_type: [matrix-grid, hierarchical-cat]
it_variants: []
analytical_function: Correlation
visual_family: Diagram
shape_primitive: [Line, Circle]
cardinality_fit: [medium, large]
audience: [Technical, Analytics]
complexity: Advanced
encoding_channels: [position, angle, color-hue, color-value]
tool_support: [d3, matplotlib]
failure_modes: [E, J]
alternatives: [network-diagram, parallel-coordinates, arc-diagram, chord-diagram]
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
A Hive Plot is a rational, rule-based layout for network visualisation that addresses the "hairball" problem of force-directed network diagrams. Nodes are assigned to a small number of radial linear axes (typically 2–6) based on a meaningful categorical property (e.g., node type, module membership, degree quintile). Node position along each axis encodes a quantitative attribute (e.g., degree, betweenness centrality). Edges are drawn as curves connecting nodes on different axes. The resulting layout is deterministic, readable, and allows direct comparison of connectivity patterns between node categories.

## When to Use
- Visualising directed or undirected networks where node classification into 2–6 meaningful categories is possible
- Comparing connectivity between node categories (e.g., genes in different regulatory modules, neurons in different brain regions)
- When a standard network diagram produces an unreadable hairball due to high edge density
- Analytical biology, systems biology, genomics, and social network analysis contexts

## When NOT to Use
- When nodes cannot be meaningfully partitioned into a small number of axes categories
- When n (nodes) is very large (> ~1000) — axes become overcrowded
- When the edge topology (graph structure) is the primary message rather than inter-category connectivity
- For non-technical audiences — the axis-plus-curve layout requires explanation

## Data Requirements
- Node table: node ID, axis assignment (categorical), axis position (numeric)
- Edge table: source node ID, target node ID, optional weight
- Axis categories: 2–6 well-defined node types or roles

## Best Practices
- Assign axes to semantically distinct node roles that have biological/domain meaning
- Use edge colour or weight to encode edge attributes (direction, strength)
- Sort nodes along each axis by a quantitative attribute that reveals pattern (e.g., degree)
- Label each axis clearly with its node category name
- Use curved (Bezier) edges — straight edges between nodes on different axes become confusing at high density

## Common Mistakes
- E (MC-noise-as-difference): concluding that inter-category connectivity patterns differ between two hive plots without a statistical network comparison test
- J (silently-dropped-categories): self-loop edges (same-axis connections) are often omitted from hive plots without documentation
- Assigning too many axes (> 6) — the layout becomes as cluttered as a standard network diagram
- Using linear axes where a logarithmic scale would better spread nodes with power-law degree distributions

## Implementation Notes

### matplotlib
No native hive plot. Implement by:
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))
n_axes = 3
angles = np.linspace(0, 2 * np.pi, n_axes, endpoint=False)

# Draw axes as radial lines
for angle in angles:
    ax.plot([0, np.cos(angle)], [0, np.sin(angle)], 'k-', alpha=0.3)

# Place nodes on axes based on their position attribute
for node in nodes:
    angle = angles[node['axis']]
    r = node['position']
    ax.scatter(r * np.cos(angle), r * np.sin(angle), ...)

# Draw edges as Bezier curves using matplotlib.path or scipy interpolation
ax.axis('off')
plt.tight_layout()
```

### plotly
No native hive plot. Use `go.Scatter` with Bezier curve approximations (via intermediate control points) for edges, and scatter traces for nodes positioned at computed (x, y) coordinates.

### altair
No native support. Pre-compute all node and edge coordinates and use `mark_point` + `mark_line` (with curved path approximations).

### excel / tableau
Not supported. Use D3.js for production hive plots.

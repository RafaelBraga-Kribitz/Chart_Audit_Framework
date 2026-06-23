---
name: Sociogram
category: Specialized
input_type: [cat-multi-value, matrix-grid]
it_variants: []
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Circle, Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-hue, area]
tool_support: [d3, matplotlib, plotly]
failure_modes: [J]
alternatives: [network-diagram, arc-diagram]
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
# Sociogram

## Description
A Sociogram is a specialised type of Network Diagram developed for sociometry — the quantitative study of social relationships. Each node represents a person or actor; directed edges represent social choices (e.g., "I would choose to work with..."), rejections, or connections. Node position (often force-directed or circular) reveals social structure: popular individuals (high in-degree), isolates (no connections), cliques (densely connected subgroups), and bridges (nodes connecting otherwise separate groups). Developed by Jacob Moreno in the 1930s.

## When to Use
- Mapping social relationships, friendship networks, collaboration patterns within a group
- Identifying influencers, isolates, and group cliques in organisational or classroom research
- Visualising survey-based social network data (e.g., "who do you go to for advice?")

## When NOT to Use
- Large networks (>100 nodes) where individual actors and relationships cannot be traced
- Abstract or non-social relationship data (use a generic Network Diagram instead)
- When the network structure itself is less important than aggregate metrics (centrality scores in a table)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| from_actor | string | Source person/node |
| to_actor | string | Target person/node |
| type | categorical (optional) | Positive choice, negative choice, or neutral |
| weight | numeric (optional) | Strength of the relationship |

## Best Practices
- Use directed arrows for asymmetric relationships (A chooses B but B does not choose A)
- Size nodes by in-degree (number of incoming choices) to highlight popular actors
- Use colour to show group membership (classroom, team, department)
- Label all nodes in small-to-medium networks; use tooltips for larger ones

## Common Mistakes
- Displaying isolated nodes without disclosure (actors present but receiving no connections) (smell J)
- Using undirected edges when directional choices were collected
- Over-interpreting edge absence as rejection (not being chosen is not the same as being rejected)
- Force-directed layout varying across renders making comparison across time points impossible

## Implementation Notes

### matplotlib
```python
import networkx as nx
G = nx.DiGraph()
G.add_edges_from(edges)
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, node_size=[100*G.in_degree(n) for n in G.nodes()],
                 arrows=True, edge_color='grey', ax=ax)
```

### plotly
`go.Scatter` for nodes + `go.Scatter` with line mode for edges; add arrowheads via annotations.

### altair
Not natively supported for directed graph layouts; pre-compute positions with NetworkX.

### excel / tableau
Not natively available. Use NetworkX + matplotlib or specialised social network analysis software (UCINET, Gephi).

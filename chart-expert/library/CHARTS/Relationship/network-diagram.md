---
name: Network Diagram
category: Relationship
input_type: [matrix-grid, hierarchical-cat]
it_variants: []
analytical_function: Correlation
visual_family: Diagram
shape_primitive: [Circle, Line, Dot, Icon]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical, Executive]
complexity: Intermediate
encoding_channels: [position, color-hue, area, color-value, texture]
tool_support: [matplotlib, plotly, d3, tableau]
failure_modes: [E, J]
alternatives: [hive-plot, matrix-diagram, arc-diagram, chord-diagram]
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

# Network Diagram

## Description
A Network Diagram (also called Network Graph, Network Map, or Node-Link Diagram) represents entities (nodes) and the connections between them (edges/links) using dots and lines. Nodes are typically drawn as circles or icons; edges as straight or curved lines. Additional variables are encoded by node size (e.g., degree, importance), node colour (e.g., community, type), edge width (e.g., weight, frequency), and edge colour (e.g., relationship type, direction). Network diagrams reveal the structural organisation of connected systems — community clustering, hub nodes, bridging nodes, and overall connectivity density.

## When to Use
- Visualising interconnected systems where the structure of connections is the primary message
- Social network analysis: showing who is connected to whom
- Biological networks: protein-protein interactions, gene regulatory networks, metabolic pathways
- Infrastructure and dependency mapping: software packages, services, components
- When the node count is manageable (< ~200) for a readable layout

## When NOT to Use
- When n_nodes > ~200 without a layout strategy — the diagram becomes a "hairball"
- When the audience needs to read precise values — use a matrix diagram or table instead
- When connection density is very high (dense graphs look like solid masses) — use adjacency matrix or hive plot instead
- When hierarchical parent-child relationships are the main structure (use a tree diagram)

## Data Requirements
- Node table: node ID, optional attributes (type, size value, group/community)
- Edge table: source ID, target ID, optional attributes (weight, direction, type)
- Directed or undirected specification

## Best Practices
- Choose layout algorithm deliberately: force-directed (Fruchterman-Reingold) for general use; hierarchical for DAGs; circular for cyclic structures; geographic for spatial networks
- Size nodes by a meaningful attribute (degree, betweenness centrality, importance score)
- Colour nodes by community or type; use a clear legend
- Use edge width proportional to edge weight when weights are meaningful
- Add directional arrowheads for directed networks
- Apply community detection algorithms (Louvain, modularity) before drawing to group related nodes

## Common Mistakes
- E (MC-noise-as-difference): force-directed layouts are stochastic — node positions change on each run, making positional comparisons between renders meaningless
- J (silently-dropped-categories): isolated nodes (no edges) are often omitted from force-directed layouts — document whether isolates are included
- Displaying too many nodes and edges without filtering — hairball diagrams communicate nothing
- Using straight edges for directed networks without arrowheads — direction of connection is lost

## Implementation Notes

### matplotlib
```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.from_pandas_edgelist(edges_df, source='source', target='target',
                             edge_attr='weight')
pos = nx.spring_layout(G, seed=42)

fig, ax = plt.subplots(figsize=(12, 10))
node_sizes = [G.degree(n) * 100 for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='steelblue', alpha=0.8, ax=ax)
nx.draw_networkx_edges(G, pos, alpha=0.3, width=1, ax=ax)
nx.draw_networkx_labels(G, pos, font_size=8, ax=ax)
ax.axis('off')
plt.tight_layout()
```
Use `networkx` for graph computation; matplotlib for rendering. `nx.kamada_kawai_layout` or `nx.circular_layout` for alternative layouts.

### plotly
```python
import plotly.graph_objects as go
import networkx as nx

G = nx.from_pandas_edgelist(edges_df, 'source', 'target')
pos = nx.spring_layout(G, seed=42)

edge_x, edge_y = [], []
for u, v in G.edges():
    edge_x += [pos[u][0], pos[v][0], None]
    edge_y += [pos[u][1], pos[v][1], None]

fig = go.Figure()
fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=0.5, color='grey')))
node_x = [pos[n][0] for n in G.nodes()]
node_y = [pos[n][1] for n in G.nodes()]
fig.add_trace(go.Scatter(x=node_x, y=node_y, mode='markers+text', marker=dict(size=10, color='steelblue')))
fig.update_layout(showlegend=False)
fig.show()
```

### altair
No native network layout. Pre-compute node positions (via networkx) and render as layered `mark_rule` (edges) + `mark_circle` (nodes) with pre-computed x/y coordinates.

### excel / tableau
- **Excel**: SmartArt > Hierarchy for simple trees; no true force-directed network. Use external tools (Gephi, Cytoscape).
- **Tableau**: No native network diagram. Use pre-computed layouts (from networkx/gephi) imported as coordinate data, then plot as scatter with line marks.

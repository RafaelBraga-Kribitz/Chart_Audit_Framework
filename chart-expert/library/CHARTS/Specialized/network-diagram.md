---
name: Network Diagram
category: Specialized
input_type: [cat-multi-value]
it_variants: [IT029]
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Circle, Dot, Line]
cardinality_fit: [small-N, medium, large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-hue, area, length]
tool_support: [d3, plotly, matplotlib]
failure_modes: [J]
alternatives: [arc-diagram, chord-diagram, hive-plot]
source: [datavizproject, datavizcatalogue]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: flow
ibcs_status: preferred
questions: ["What structure or process does Network Diagram explain?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
---
# Network Diagram

## Description
A Network Diagram (also called a Graph Diagram or Node-Link Diagram) visualises entities as nodes and their relationships as edges (lines). Node size, colour, and label can encode attributes; edge thickness and colour can encode relationship strength or type. Layout algorithms (force-directed, hierarchical, circular) arrange nodes to minimise edge crossings and reveal structural patterns such as clusters, hubs, and bridges. Networks are used to represent social relationships, dependencies, communication flows, and biological interactions.

## When to Use
- Visualising relationships or connections between entities where the topology is the primary message
- Social network analysis, dependency graphs, knowledge graphs, citation networks
- Identifying clusters, central hubs, or bridge nodes within a network

## When NOT to Use
- Very dense networks with thousands of nodes and edges (becomes unreadable — use hive plot or matrix)
- Data without clear relational structure (use a standard chart type)
- When node positions have a natural ordering (use Arc Diagram or matrix for ordered data)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| source | string | Source node identifier |
| target | string | Target node identifier |
| weight | numeric (optional) | Edge weight or strength |
| node_attr | various (optional) | Node attribute for size/colour encoding |

## Best Practices
- Use force-directed layout as a default; switch to hierarchical for DAGs
- Size nodes by degree (connection count) or a meaningful attribute
- Filter to the top N nodes by degree for large networks; disclose filtering (smell J)
- Use colour to encode node communities or categories
- Annotate hub nodes with labels; avoid labelling all nodes in dense graphs

## Common Mistakes
- Displaying all nodes and edges in a dense graph creating an unreadable hairball
- Silently dropping low-degree nodes without disclosure (smell J)
- Using a random layout algorithm producing irreproducible positions
- Encoding too many visual variables (size + colour + shape) on nodes simultaneously


## Dashboard and other surfaces

status: placeholder

`Network Diagram` can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with arc-diagram, chord-diagram, hive-plot.

Suggested communication placement: **detail** zone. Vault coarse type, when a scraped template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
import networkx as nx
G = nx.from_pandas_edgelist(df, 'source', 'target')
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, node_size=300, node_color='steelblue',
                 edge_color='grey', with_labels=True, ax=ax)
```

### plotly
`go.Scatter` for nodes and `go.Scatter` with line mode for edges; compute positions via NetworkX layout then pass to Plotly.

### altair
Not natively supported; use NetworkX for layout and pass node positions to `mark_point()` + `mark_rule()`.

### excel / tableau
Not natively available. Use NetworkX + matplotlib or D3.js `d3.forceSimulation()` for production use.

---
name: Arc Diagram
category: Specialized
input_type: [cat-multi-value]
it_variants: [IT029]
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Line, Circle]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-hue, area]
tool_support: [d3, matplotlib, plotly]
failure_modes: [J]
alternatives: [network-diagram, chord-diagram]
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
questions: ["What structure or process does Arc Diagram explain?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
---
# Arc Diagram

## Description
An Arc Diagram places nodes along a single straight axis (usually horizontal) and draws semicircular arcs above (and sometimes below) the axis to represent edges between nodes. The arc radius is proportional to the distance between the two nodes on the axis. Arc thickness or colour can encode edge weight or category. Unlike force-directed network diagrams, the linear arrangement works well when nodes have a natural ordering (temporal, alphabetical, ranked) and makes long-distance connections clearly visible.

## When to Use
- Networks where nodes have a meaningful linear ordering (temporal sequences, ranked lists)
- Showing which nodes in a sequence interact with distant vs. adjacent neighbours
- Music, text, or genomic co-occurrence networks where sequence position matters
- When a force-directed network layout would be unstable or uninterpretable

## When NOT to Use
- Densely connected networks where arcs pile up into unreadable overlapping curves
- Data without a natural node ordering (use network diagram or chord diagram)
- Very large networks (>100 nodes) without interaction for filtering

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| source | string | Source node identifier |
| target | string | Target node identifier |
| weight | numeric (optional) | Arc thickness |
| order | integer / numeric | Linear position of each node on the axis |

## Best Practices
- Sort nodes by a meaningful attribute or by cluster membership to minimize arc crossings
- Use arc thickness to encode connection weight when available
- Colour arcs by category or community
- Place arcs alternately above and below the axis when bi-directional connections need distinction

## Common Mistakes
- Dense networks with many long arcs creating an unreadable stack
- Arbitrary node ordering that maximises crossing — sort to reduce crossings
- Silently omitting weak connections without disclosure (smell J)
- Not labelling nodes, making the diagram uninterpretable


## Dashboard and other surfaces

status: placeholder

`Arc Diagram` can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with network-diagram, chord-diagram.

Suggested communication placement: **detail** zone. Vault coarse type, when a scraped template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Draw arcs as semicircles
from matplotlib.patches import Arc
for src, tgt, w in edges:
    mid = (pos[src] + pos[tgt]) / 2
    radius = abs(pos[tgt] - pos[src]) / 2
    arc = Arc((mid, 0), 2*radius, 2*radius, angle=0,
              theta1=0, theta2=180, lw=w, color='steelblue', alpha=0.5)
    ax.add_patch(arc)
ax.scatter(list(pos.values()), [0]*len(pos), s=50, color='black', zorder=5)
```

### plotly
Use `go.Scatter` with parametric semicircle coordinates per edge.

### altair
Not natively supported; compute arc path coordinates manually.

### excel / tableau
Not natively available in either tool.

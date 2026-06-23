---
name: Sankey Diagram
category: Composition
input_type: [composition, cat-multi-value]
it_variants: []
analytical_function: Flow
visual_family: Diagram
shape_primitive: [Area, Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical, Executive]
complexity: Intermediate
encoding_channels: [length, area, color-hue]
tool_support: [matplotlib, plotly, d3, tableau]
failure_modes: [I, J]
alternatives: [alluvial-diagram, parallel-sets, flow-map]
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
# Sankey Diagram

## Description
Sankey Diagrams display flows and their quantities in proportion to one another using directed arrows or ribbons whose thickness encodes magnitude. Originally used to visualise steam engine efficiency, they are now widely applied to energy systems, budget flows, material flows, and user journey funnels. Flow arrows can combine or split at each node; colour distinguishes different flow types or stages.

## When to Use
- Showing how a quantity (energy, money, traffic, materials) flows through a system with multiple stages
- Illustrating where losses, splits, or conversions occur in a process
- Energy audits, budget breakdowns, website traffic flows, supply chain visualisation

## When NOT to Use
- Data representing categorical membership changes over time (use Alluvial Diagram)
- Flows are not proportional to a meaningful quantity (all flows equal)
- The network has cycles — Sankey requires a directed acyclic graph structure

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| source | string | Name of source node |
| target | string | Name of target node |
| value | numeric (≥0) | Flow volume / thickness |
| color | string (optional) | Flow or node colour grouping |

## Best Practices
- Arrange nodes left-to-right in process/temporal order
- Ensure flow conservation: total in ≈ total out at each node (except sources/sinks)
- Colour by source node or flow category — avoid rainbow schemes
- Label flows with absolute values for significant paths; use tooltips for minor ones
- Keep total node count below ~20 to maintain readability

## Common Mistakes
- Mixing scenarios vs actual flows, treating them as additive (smell I — stacked-mutually-exclusive)
- Silently dropping small flows below display threshold without disclosure (smell J)
- Flows that don't conserve quantity at nodes (implies missing data, not a design choice)
- Using Sankey for categorical membership where Alluvial Diagram is more appropriate

## Implementation Notes

### matplotlib
```python
from matplotlib.sankey import Sankey
Sankey(flows=[0.25, 0.15, -0.1, -0.3], labels=['In','Steam','-Loss','-Out'],
       orientations=[0, 1, -1, 0]).finish()
```

### plotly
```python
go.Sankey(
    node=dict(label=node_labels, color=node_colors),
    link=dict(source=sources, target=targets, value=values)
)
```

### altair
Not natively supported; requires custom Bezier curve rendering.

### excel / tableau
**Tableau**: No native Sankey; requires extensive calculated field and path-based polygon technique. **Excel**: Not natively supported; use third-party tools (SankeyMATIC, RAWGraphs).

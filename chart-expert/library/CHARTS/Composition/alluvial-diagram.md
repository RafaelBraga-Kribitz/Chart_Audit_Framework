---
name: Alluvial Diagram
category: Composition
input_type: [cat-multi-value, composition]
it_variants: []
analytical_function: Flow
visual_family: Diagram
shape_primitive: [Area, Line]
cardinality_fit: [medium, large]
audience: [Analytics, Public]
complexity: Intermediate
encoding_channels: [length, area, color-hue]
tool_support: [d3, plotly, tableau]
failure_modes: [I, J]
alternatives: [sankey-diagram, parallel-sets]
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
# Alluvial Diagram

## Description
An Alluvial Diagram is a type of flow diagram that shows how entities or quantities shift between categorical states across multiple time points or stages. Vertical blocks (nodes) represent categories at each stage; flowing ribbons (alluvions) between stages show how much volume moves from one category to another. The width of each ribbon is proportional to the quantity. It is closely related to the Sankey Diagram but emphasises categorical membership changes over time rather than directed energy/material flow.

## When to Use
- Tracking how a population changes membership across categories over time (e.g., party affiliation, product tier migration)
- Visualising customer journey stages or state transitions
- Showing how classifications or groupings reorganise across two or more time points

## When NOT to Use
- Data without a clear temporal or sequential dimension (use Parallel Sets)
- When the underlying flow is a continuous process rather than discrete category membership
- Fewer than 2 stages — use a simple bar or Sankey instead

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| stage | categorical / temporal | The column (time point or step) |
| category | categorical | Node identity at this stage |
| count | numeric (≥0) | Volume of flow |
| source_cat | categorical | Source node for each ribbon |
| target_cat | categorical | Target node for each ribbon |

## Best Practices
- Colour ribbons by source category to make origin tracking easy
- Order nodes consistently: largest-to-smallest or by a logical sequence
- Annotate nodes with total volumes
- Use interaction (hover) to highlight individual flow paths

## Common Mistakes
- Treating flows as causal (directional arrows imply causality when only correlation exists) (smell I)
- Silently dropping small flows below a display threshold without disclosure (smell J)
- Using this for process flows where Sankey Diagram is the correct choice
- Misaligning nodes across stages making ribbons cross unnecessarily

## Implementation Notes

### matplotlib
Not directly supported; use the `matplotlib-sankey` module or custom Bezier ribbon rendering.

### plotly
`go.Sankey` with node and link data models is the closest equivalent; Plotly does not distinguish Sankey from Alluvial natively.

### altair
Not natively supported; requires custom mark rendering with precomputed ribbon geometry.

### excel / tableau
**Tableau**: Achievable using path-based calculations and polygon marks. **Excel**: Not natively supported.

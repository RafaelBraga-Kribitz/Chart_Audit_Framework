---
name: Chord Diagram
category: Composition
input_type: [matrix-grid, cat-multi-value]
it_variants: []
analytical_function: Part-to-whole
visual_family: Diagram
shape_primitive: [Area, Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [angle, area, color-hue]
tool_support: [d3, plotly, matplotlib]
failure_modes: [I, J]
alternatives: [arc-diagram, sankey-diagram, network-diagram]
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
# Chord Diagram

## Description
A Chord Diagram visualises inter-relationships between entities arranged along a circle. Nodes (entities) are arcs on the circle's perimeter; chords (Bezier curves) connecting them represent relationships or flows between pairs. The width of each arc segment shows the total flow in/out of that entity; the width of each chord shows the magnitude of the relationship between two entities. Colour is used to group entities or distinguish flow direction.

## When to Use
- Showing pairwise relationships or flows between a moderate number of entities (6–20)
- Migration flows, trade relationships, communication patterns, import/export matrices
- When the relative magnitude of each entity's total connections matters alongside pairwise volumes

## When NOT to Use
- More than ~20 entities — chord overlaps create unreadable visual noise
- When directionality of flows is the primary focus (use Sankey Diagram)
- Sparse relationship matrices where most pairs have zero connection

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| source | categorical | Origin entity |
| target | categorical | Destination entity |
| value | numeric (≥0) | Flow or relationship strength |

Or equivalently: a square matrix where rows and columns are entities and cells are flow values.

## Best Practices
- Order entities around the circle to minimise chord crossings (related entities adjacent)
- Assign one colour per entity; use it for both the arc and all chords originating from that entity
- Provide interactive highlighting to trace individual chords on hover
- Label entity arc segments clearly; avoid labelling individual chords unless essential

## Common Mistakes
- Too many entities creating an impenetrable web of overlapping chords
- Non-symmetric matrices presented as symmetric (obscuring directionality) (smell I)
- Using equal arc widths when entities have very different total connection volumes
- Silently omitting weak connections without disclosure (smell J)

## Implementation Notes

### matplotlib
```python
# Use mpl-chord-diagram or pyCircos
from chord import Chord
Chord(matrix, names).show()
```

### plotly
No native chord; use community libraries like `plotly-chord` or implement via `go.Scatter` with Bezier path strings.

### altair
Not natively supported.

### excel / tableau
Not natively supported in either tool. Use D3.js `d3.chord()` for production implementations.

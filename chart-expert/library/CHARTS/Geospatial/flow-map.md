---
name: Flow Map
category: Geospatial
input_type: [cat-multi-value]
it_variants: []
analytical_function: Geographical
visual_family: Map
shape_primitive: [Line, Area]
cardinality_fit: [small-N, medium]
audience: [Analytics, Public]
complexity: Intermediate
encoding_channels: [position, length, area, color-hue]
tool_support: [d3, plotly, matplotlib]
failure_modes: [F, J]
alternatives: [connection-map, sankey-diagram, choropleth-map]
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
# Flow Map

## Description
A Flow Map uses arrows or curved lines on a geographic basemap to show the movement of people, goods, information, or other quantities between locations. Arrow thickness (or width) encodes the volume of flow. Direction is shown by arrowheads or Bezier curve orientation. Flow Maps are closely related to Sankey Diagrams but anchored to geographic coordinates. They are classic tools for migration, trade, and logistics visualisation.

## When to Use
- Showing directional movement or transfer of quantities between geographic locations
- Migration flows, trade flows, airline routes with volume encoding, supply chain movements
- When geographic origin and destination are both important, not just the volume

## When NOT to Use
- Non-directional connections (use Connection Map instead)
- Very many flow pairs creating a hairball of overlapping arrows
- When the geographic layout is less important than the flow magnitudes (use Sankey)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| origin_lat, origin_lon | numeric | WGS84 origin coordinates |
| dest_lat, dest_lon | numeric | WGS84 destination coordinates |
| volume | numeric (≥0) | Flow magnitude; encodes line width |
| label | string (optional) | Origin/destination name |

## Best Practices
- Use great-circle arcs (curved lines) rather than straight lines for geographic accuracy
- Scale line width proportionally to volume; normalise so the largest flow is readable
- Use directional arrowheads or curvature to indicate flow direction
- Aggregate minor flows into "Other" to avoid clutter (smell J)
- Filter to show only the top N flows by volume for readability

## Common Mistakes
- Too many overlapping flow lines creating a visual tangle without filtering
- Straight-line flows misrepresenting actual routing distance (smell F)
- Omitting low-volume flows without disclosure, potentially hiding important origins/destinations (smell J)
- Using equal line widths regardless of volume, hiding magnitude differences

## Implementation Notes

### matplotlib
```python
from mpl_toolkits.basemap import Basemap
m = Basemap(projection='merc', ...)
for _, row in flows.iterrows():
    x, y = m([row.origin_lon, row.dest_lon], [row.origin_lat, row.dest_lat])
    ax.annotate('', xy=(x[1], y[1]), xytext=(x[0], y[0]),
                arrowprops=dict(arrowstyle='->', lw=row.volume/scale))
```

### plotly
`go.Scattergeo` with pairs of coordinates per flow; control line width via `line.width`; use multiple traces for variable width.

### altair
`mark_line()` with geographic projection and pairs of points; variable stroke width requires separate computed column.

### excel / tableau
**Tableau**: Requires path-based calculation with paired origin/destination rows. Not available natively without data preparation.

---
name: Connection Map
category: Geospatial
input_type: [cat-multi-value]
it_variants: []
analytical_function: Geographical
visual_family: Map
shape_primitive: [Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Public]
complexity: Basic
encoding_channels: [position, color-hue, color-value]
tool_support: [d3, plotly, matplotlib, tableau]
failure_modes: [F, J]
alternatives: [flow-map, pin-map, network-diagram]
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
# Connection Map

## Description
A Connection Map (also called a Link Map or Spider Map) draws lines between pairs of geographic points to show relationships, links, or connectivity. Unlike a Flow Map, Connection Maps are typically non-directional and the lines do not encode volume through width — the mere existence of a connection is the primary message. They are commonly used to visualise airline routes, communication networks, collaboration links, or infrastructure connections.

## When to Use
- Showing existence and pattern of connections between geographic locations (routes, relationships)
- Network topology over a geographic basemap (airline routes, data centre interconnects)
- When directional flow volume is less important than the connection structure

## When NOT to Use
- When connection strength or volume needs to be encoded — use Flow Map instead
- Dense networks where every node connects to many others (lines overlap into a hairball)
- When the geographic layout is irrelevant — use a network diagram instead

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| from_lat, from_lon | numeric | WGS84 coordinates of the origin node |
| to_lat, to_lon | numeric | WGS84 coordinates of the destination node |
| weight | numeric (optional) | Connection strength for colour or opacity encoding |
| category | categorical (optional) | Route type or network layer |

## Best Practices
- Use great-circle arcs for long-distance connections rather than straight lines
- Use opacity or colour to encode connection frequency or strength when available
- Highlight hub nodes (high degree) with larger markers at connection endpoints
- Filter to show only meaningful connections; avoid plotting all edges in a dense graph

## Common Mistakes
- Too many connections creating an unreadable web — filter to significant edges (smell J)
- Straight Euclidean lines over a curved earth for long-distance connections (smell F)
- Equal-weight lines when connections have meaningfully different strengths
- Not distinguishing node identity from edge identity (missing node markers)

## Implementation Notes

### matplotlib
```python
for _, row in connections.iterrows():
    ax.plot([row.from_lon, row.to_lon], [row.from_lat, row.to_lat],
            'b-', alpha=0.3, linewidth=0.5, transform=ccrs.Geodetic())
```

### plotly
`go.Scattergeo` with paired coordinates per connection, `mode='lines'`; one trace per connection or use line grouping.

### altair
`mark_rule()` or `mark_line()` with geographic projection and paired latitude/longitude encodings.

### excel / tableau
**Tableau**: Path-based calculation with origin/destination rows in long format. Use Line mark type.

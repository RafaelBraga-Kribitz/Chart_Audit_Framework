---
name: Route Map
category: Geospatial
input_type: [cat-multi-value]
it_variants: []
analytical_function: Geographical
visual_family: Map
shape_primitive: [Line]
cardinality_fit: [small-N, medium]
audience: [Executive, Public]
complexity: Basic
encoding_channels: [position, color-hue, color-value]
tool_support: [plotly, d3, tableau]
failure_modes: [F]
alternatives: [connection-map, flow-map, transit-map]
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
# Route Map

## Description
A Route Map displays one or more paths or itineraries over a geographic basemap, tracing the actual or planned route between sequential waypoints. Unlike a Flow Map (which encodes volume through line width) or a Connection Map (which shows network topology), a Route Map emphasises the specific path taken — turns, roads, waterways, or air corridors — and is primarily used for navigation, logistics, travel, and delivery contexts.

## When to Use
- Showing a specific travel itinerary, delivery route, or expedition path
- Logistics and transportation planning where the actual path matters
- Historical route visualisation (trade routes, exploration journeys)

## When NOT to Use
- Multiple routes that require volume or comparison encoding (use Flow Map)
- When overall network structure is more important than individual path geometry (use Connection Map)
- Abstract process flows without geographic grounding

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| sequence | integer | Waypoint order along the route |
| latitude | numeric | WGS84 latitude of each waypoint |
| longitude | numeric | WGS84 longitude of each waypoint |
| label | string (optional) | Waypoint name |
| route_id | string (optional) | Distinguishes multiple routes |

## Best Practices
- Use actual road/path geometry from routing APIs rather than straight lines (smell F)
- Mark waypoints clearly with labelled pins or markers
- Colour-code multiple routes distinctly
- Include start and end markers to show direction without arrows if the route is clear

## Common Mistakes
- Drawing straight lines between waypoints when actual roads curve significantly (smell F)
- Using an unlabelled basemap making geographic context unclear
- Plotting too many routes simultaneously without colour distinction

## Implementation Notes

### matplotlib
```python
# Ordered waypoints connected by lines
ax.plot(df.lon, df.lat, 'b-o', linewidth=2, markersize=6)
for _, row in df.iterrows():
    ax.annotate(row.label, (row.lon, row.lat), textcoords='offset points', xytext=(5,5))
```

### plotly
`go.Scattermapbox(lat=lats, lon=lons, mode='lines+markers', text=labels)` with ordered waypoints.

### altair
`mark_line()` + `mark_point()` layers on a geographic projection with ordered longitude/latitude.

### excel / tableau
**Tableau**: Path-based visualisation with ordered sequence field. **Excel**: 3D Maps with path/route layer.

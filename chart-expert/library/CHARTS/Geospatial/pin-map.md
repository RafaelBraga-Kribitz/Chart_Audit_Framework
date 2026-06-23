---
name: Pin Map
category: Geospatial
input_type: [cat-value, xy-simple]
it_variants: []
analytical_function: Geographical
visual_family: Map
shape_primitive: [Dot, Icon]
cardinality_fit: [small-N, medium, large]
audience: [Executive, Analytics, Public]
complexity: Basic
encoding_channels: [position, color-hue, shape]
tool_support: [plotly, d3, tableau, powerbi]
failure_modes: [F]
alternatives: [bubble-map, dot-density-map, choropleth-map]
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
# Pin Map

## Description
Also known as a Point Map or Dot Map (exact locations). A Pin Map places a marker (pin, dot, or icon) at the precise geographic coordinates of each data point. Unlike Dot Density Maps (which place dots randomly within regions), each pin represents a specific, known location. Colour or icon shape can encode categorical attributes, and clustering handles dense areas to avoid overplotting.

## When to Use
- Displaying exact event or entity locations (stores, incidents, sensors, observations)
- Showing spatial distribution of individually located entities
- Simple maps for business operations, logistics, or field reporting

## When NOT to Use
- Data is aggregated to regional levels (use Choropleth or Bubble Map)
- Very large datasets without clustering (>10,000 points create overplotting)
- When overlapping points at the same location need to show counts (use Bubble Map)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| latitude | numeric | WGS84 decimal degrees |
| longitude | numeric | WGS84 decimal degrees |
| label | string (optional) | Tooltip or popup text |
| category | categorical (optional) | Pin colour or icon type |
| value | numeric (optional) | Encodes size if pins are variable |

## Best Practices
- Use clustering for dense datasets (cluster pins at low zoom, expand at high zoom)
- Size pins consistently unless encoding a quantitative variable
- Use colour to distinguish categories; keep palette to ≤6 distinct values
- Provide basemap context (streets, terrain, or satellite depending on audience)
- Include a legend if multiple pin categories are used

## Common Mistakes
- Placing pins at approximate region centroids when actual coordinates are unavailable (smell F — bounding-box-geometry)
- Using too many icon types that are hard to distinguish at small sizes
- Dense pin layers without clustering, making the map unreadable and performance-heavy
- Omitting pins for locations with missing coordinates without disclosure (smell J)

## Implementation Notes

### matplotlib
```python
import geopandas as gpd
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot(ax=ax, color='lightgrey')
ax.scatter(df.longitude, df.latitude, c=colors, s=10, zorder=5)
```

### plotly
`go.Scattermapbox(lat=lats, lon=lons, mode='markers', marker=dict(color=colors))` with `mapbox_style='open-street-map'`.

### altair
`mark_point()` on a geographic projection with `longitude='lon:Q'` and `latitude='lat:Q'`.

### excel / tableau
**Tableau**: Drag Latitude/Longitude to rows/columns, select Map view. **Excel**: 3D Maps or Bing Maps with point data.

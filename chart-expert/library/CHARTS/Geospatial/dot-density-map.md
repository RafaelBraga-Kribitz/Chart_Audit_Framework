---
name: Dot Density Map
category: Geospatial
input_type: [cat-value]
it_variants: []
analytical_function: Geographical
visual_family: Map
shape_primitive: [Dot]
cardinality_fit: [large, very-large]
audience: [Analytics, Public]
complexity: Intermediate
encoding_channels: [position, color-hue]
tool_support: [matplotlib, d3, plotly]
failure_modes: [F, J]
alternatives: [choropleth-map, pin-map, bubble-map]
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
# Dot Density Map

## Description
A Dot Density Map places one dot (or a dot representing N units) randomly within each geographic region in proportion to a count variable. Rather than shading entire polygons, the density of dots visually represents the concentration of the phenomenon. Multiple dot colours can represent different categories simultaneously, revealing spatial co-occurrence and segregation patterns that choropleth maps obscure.

## When to Use
- Visualising population distributions or counts where raw numbers (not rates) are meaningful
- Showing spatial clustering and concentration at a sub-region level
- Comparing the distribution of two or more groups (e.g., demographic distributions by category)
- When boundary-based choropleth would mask within-region variation

## When NOT to Use
- Data available only as aggregated regional totals with unknown within-region distribution
- When individual dot positions imply precise point locations (dots are randomly placed)
- Very low counts where individual dots can be placed as point features (use Pin Map instead)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| region_id | string | Geographic region identifier |
| count | numeric | Total count; each dot typically represents N units |
| category | categorical (optional) | Dot colour grouping |
| geometry | GeoJSON/shapefile | Polygon to randomly place dots within |

## Best Practices
- State the dot value clearly (e.g., "1 dot = 1,000 people")
- Use a dot value that produces enough dots for density perception without overcrowding
- Use distinct, high-contrast colours for multi-category dot maps
- Avoid placing dots outside land boundaries (mask with region polygon)

## Common Mistakes
- Dot positions implying exact individual locations (smell F — geometry misrepresentation)
- Using this map where data is aggregated and uniform within-region distribution is wrong
- Silently dropping small-count regions that generate 0 dots (smell J)
- Overcrowding: too many dots per region making them merge into a solid blob

## Implementation Notes

### matplotlib
```python
# Random dot placement within polygon bounds
import geopandas as gpd
from shapely.geometry import Point
gdf = gpd.read_file('regions.geojson').merge(df, on='region_id')
points = []
for _, row in gdf.iterrows():
    n_dots = int(row['count'] / dot_value)
    pts = random_points_in_polygon(row.geometry, n_dots)
    points.extend(pts)
gpd.GeoDataFrame(geometry=points).plot(ax=ax, markersize=1)
```

### plotly
Use `go.Scattermapbox` or `go.Scattergeo` with randomly generated lat/lon within each polygon.

### altair
Not directly supported for polygon-bounded random placement; requires pre-generated point coordinates.

### excel / tableau
**Tableau**: Not natively supported; requires pre-generated point data uploaded as a spatial file.

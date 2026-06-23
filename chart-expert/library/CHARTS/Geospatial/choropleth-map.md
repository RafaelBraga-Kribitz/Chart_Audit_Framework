---
name: Choropleth Map
category: Geospatial
input_type: [cat-value]
it_variants: []
analytical_function: Geographical
visual_family: Map
shape_primitive: [Polygon]
cardinality_fit: [medium, large]
audience: [Executive, Analytics, Public]
complexity: Basic
encoding_channels: [color-value, color-hue, area]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [F, J]
alternatives: [dot-density-map, bubble-map, cartogram]
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
# Choropleth Map

## Description
A Choropleth Map fills geographical regions (countries, states, counties, postal codes) with colours proportional to a data variable, revealing spatial patterns and variation across areas. A sequential or diverging colour ramp is typically used, where the progression from light to dark (or from one hue to another) represents low to high values. It is one of the most widely used thematic maps in journalism, policy, and analytics.

## When to Use
- Showing how a single variable (population density, income, vote share, prevalence) varies across geographic regions
- When regional boundaries are meaningful administrative units that the audience recognises
- Comparative overview of geographic variation at a glance

## When NOT to Use
- Raw count data without normalisation — large regions will always appear dominant (smell F)
- When precise values matter more than spatial pattern (a sorted bar chart is more readable)
- Very small geographic units at small zoom levels (polygons become invisible)
- Data that has no meaningful geographic aggregation

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| region_id | string | Geographic identifier (ISO code, FIPS, etc.) matching the geometry |
| value | numeric | Normalised metric (rate, proportion, per-capita) — avoid raw counts |
| geometry | GeoJSON/shapefile | Polygon boundaries for each region |

## Best Practices
- Always normalise values to density or rates — never encode raw population counts (smell F)
- Use sequential palette for one-directional data; diverging palette for deviation from a centre
- Include a clear colour legend with value breaks labelled
- Use equal-area map projections (Albers, Mollweide) to avoid perceptual distortion of larger regions
- Provide a basemap for orientation in less-familiar geographies

## Common Mistakes
- Encoding raw totals rather than normalised rates, making large regions dominate (smell F)
- Silently dropping regions with missing data rather than showing them as grey (smell J)
- Choosing a rainbow/spectral palette that introduces false visual boundaries
- Using Mercator projection which greatly exaggerates high-latitude regions

## Implementation Notes

### matplotlib
```python
import geopandas as gpd
gdf = gpd.read_file('regions.geojson').merge(df, on='region_id')
gdf.plot(column='value', cmap='Blues', legend=True, ax=ax)
```

### plotly
`go.Choropleth(locations=codes, z=values, locationmode='ISO-3', colorscale='Blues')` for world maps; `go.Choroplethmapbox` for custom GeoJSON.

### altair
`mark_geoshape()` with `color=alt.Color('value:Q', scale=alt.Scale(scheme='blues'))` and a GeoJSON feature source.

### excel / tableau
**Tableau**: Filled Map chart type with geographic role assigned to the region field. **Excel**: 3D Maps or Bing Maps add-in with filled regions.

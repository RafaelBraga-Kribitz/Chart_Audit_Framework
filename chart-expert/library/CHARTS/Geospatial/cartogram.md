---
name: Cartogram
category: Geospatial
input_type: [cat-value]
it_variants: []
analytical_function: Geographical
visual_family: Map
shape_primitive: [Polygon, Circle, Square]
cardinality_fit: [medium, large]
audience: [Analytics, Public]
complexity: Advanced
encoding_channels: [area, color-hue, color-value]
tool_support: [d3, matplotlib]
failure_modes: [F]
alternatives: [choropleth-map, bubble-map]
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
# Cartogram

## Description
A Cartogram distorts the geographic size or shape of regions so that their area is proportional to a data variable rather than their actual land area. A continuous cartogram (contiguous cartogram) reshapes polygons while preserving adjacency; a non-contiguous cartogram scales regions independently; a Dorling cartogram replaces regions with proportional circles arranged approximately in their geographic positions. Cartograms correct the perceptual bias of large-region dominance in Choropleth Maps.

## When to Use
- Communicating data where geographic land area is misleading (e.g., electoral maps where sparse rural regions visually dominate)
- When the message is explicitly "this region's data value, not its land area, is what matters"
- Population, GDP, or vote-count maps where absolute totals drive the story

## When NOT to Use
- Audiences unfamiliar with cartogram distortion who may find the result confusing
- When precise geographic orientation is needed (shapes are unrecognisable after distortion)
- Data without a strong absolute-count rationale for area distortion

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| region_id | string | Matches geometry identifier |
| value | numeric (≥0) | Target area or circle size |
| color_var | numeric / categorical (optional) | Secondary colour encoding |
| geometry | GeoJSON/shapefile | Original polygon boundaries |

## Best Practices
- Pair with a conventional map for reference so audiences understand what was distorted
- Label regions directly — recognition after distortion is harder
- Use the Dorling (circle) variant when shape recognition is not critical
- Explain the cartogram type and what variable drives the distortion in the caption

## Common Mistakes
- Using cartogram without a legend or explanation of what the area represents (smell F)
- Continuous cartogram distortion so extreme that regions become unrecognisable
- Applying a second variable (colour) without adjusting for the distorted geography's visual weight
- Using cartograms for data where normalised rates are more appropriate (use choropleth)

## Implementation Notes

### matplotlib
```python
# Use the cartogram library or geopandas with iterative Dougenik-Chrisman-Niemeyer algorithm
import cartogram
carto_gdf = cartogram.make_cartogram(gdf, 'value', iterations=5)
carto_gdf.plot(column='color_var', cmap='RdYlGn', ax=ax)
```

### plotly
No native cartogram support; pre-compute distorted geometry and pass as custom GeoJSON to `go.Choropleth`.

### altair
Use pre-computed distorted GeoJSON with `mark_geoshape()`.

### excel / tableau
Not natively available. Pre-compute cartogram geometry externally and import as custom spatial data.

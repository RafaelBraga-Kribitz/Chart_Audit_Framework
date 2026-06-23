---
name: Topographic Map
category: Geospatial
input_type: [xyz-trivariate]
it_variants: []
analytical_function: Geographical
visual_family: Map
shape_primitive: [Line, Area, Polygon]
cardinality_fit: [large, very-large]
audience: [Technical, Analytics]
complexity: Advanced
encoding_channels: [position, color-value, texture]
tool_support: [matplotlib, d3]
failure_modes: [F, G]
alternatives: [isoline-map, choropleth-map]
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
# Topographic Map

## Description
A Topographic Map represents the three-dimensional terrain of a geographic surface using elevation contour lines (isolines at fixed elevation intervals), colour hypsometric tinting (green-yellow-brown-white for low-to-high), and optionally hillshading (simulated light and shadow). In data visualisation contexts, the term is also used more broadly for any map that uses contour lines and shading to show a continuous z-variable over a 2D geographic surface, not limited to physical elevation.

## When to Use
- Representing elevation, bathymetry, or any continuous geographic surface variable
- Terrain analysis, wilderness navigation, geologic or environmental science communication
- When the full 3D character of a landscape needs to be communicated on a 2D surface

## When NOT to Use
- Non-geographic data (use a 2D contour plot or 3D surface plot)
- When administrative boundaries or discrete categories matter more than continuous terrain
- General business audiences who may not interpret contour intervals correctly

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| x / easting | numeric | Coordinate (projected) or longitude |
| y / northing | numeric | Coordinate (projected) or latitude |
| elevation | numeric | Z value (elevation in metres, or other continuous field) |

Typically stored as a raster DEM (Digital Elevation Model) in GeoTIFF format.

## Best Practices
- Use standard contour intervals appropriate to terrain scale (10 m, 50 m, 100 m intervals)
- Apply hillshading from northwest (standard cartographic convention) for 3D effect
- Use hypsometric tinting: green (low) → yellow → brown → white (high)
- Label index contours (every 5th line) with elevation values

## Common Mistakes
- Contour lines that cross each other (physically impossible; indicates data error) (smell F)
- Over-interpolation producing unrealistically smooth terrain (smell G)
- Using an inappropriate projection that distorts distances and elevations
- Omitting a scale bar and north arrow (essential for any topographic map)

## Implementation Notes

### matplotlib
```python
import rasterio
import numpy as np
with rasterio.open('dem.tif') as src:
    elev = src.read(1)
plt.contourf(elev, levels=20, cmap='terrain')
plt.contour(elev, levels=20, colors='k', linewidths=0.3, alpha=0.5)
plt.colorbar(label='Elevation (m)')
```

### plotly
`go.Surface(z=elev_array)` for interactive 3D; `go.Contour(z=elev_array)` for 2D contour version.

### altair
Not well-suited for raster-based topographic maps; use geopandas/matplotlib pipeline.

### excel / tableau
Not natively available. Use GIS tools (QGIS, ArcGIS, Google Earth Engine) for topographic maps.

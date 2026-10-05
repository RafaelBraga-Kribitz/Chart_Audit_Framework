---
name: Isoline Map
category: Geospatial
input_type: [xyz-trivariate]
it_variants: [IT012]
analytical_function: Geographical
visual_family: Map
shape_primitive: [Line, Area]
cardinality_fit: [large, very-large]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [position, color-value, color-hue]
tool_support: [matplotlib, plotly, d3]
failure_modes: [F, G]
alternatives: [choropleth-map, topographic-map]
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: spatial
ibcs_status: conditional
questions: ["Where is the measure concentrated?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: none
---
# Isoline Map

## Description
An Isoline Map (also called a Contour Map or Isarithmic Map) connects points of equal value with lines (isolines or contours), then optionally fills the areas between lines with a colour gradient. Common variants include isobars (equal pressure), isotherms (equal temperature), isohyets (equal rainfall), and contour lines for elevation. The result reveals continuous spatial gradients and allows readers to identify zones of similar values without relying on administrative boundaries.

## When to Use
- Visualising a continuously varying geographic field (temperature, rainfall, air pressure, elevation)
- Revealing gradient patterns and spatial variation in scientific or meteorological data
- When administrative boundaries are irrelevant and the underlying spatial continuity matters

## When NOT to Use
- Data is discrete or aggregated to regions (use Choropleth)
- Underlying data is too sparse for reliable interpolation
- Non-geographic continuous fields (use contour plot instead)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| latitude | numeric | Observation latitude |
| longitude | numeric | Observation longitude |
| value | numeric | Measured value at this point (temperature, pressure, etc.) |

Interpolation (e.g., kriging, IDW) is typically applied to generate a regular grid before contouring.

## Best Practices
- Apply appropriate spatial interpolation before contouring (kriging for physical phenomena)
- Label isolines with their value at regular intervals
- Use a diverging palette when values span a meaningful midpoint (e.g., 0°C freezing line)
- Show underlying data observation points to communicate data density
- Select contour intervals that match the natural resolution of the data

## Common Mistakes
- Over-smooth contours that imply more data than actually exists (smell G — KDE-over-atoms applied spatially)
- Using isolines without indicating the interpolation method or data density
- Choosing contour intervals too fine or too coarse, misrepresenting spatial resolution (smell F)
- Confusing isoline maps with choropleth maps (boundaries vs. gradients)

## Dashboard and other surfaces

status: placeholder

Isoline Map is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with `choropleth-map`, `topographic-map`. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
from scipy.interpolate import griddata
grid_z = griddata((lons, lats), values, (grid_lon, grid_lat), method='cubic')
plt.contourf(grid_lon, grid_lat, grid_z, levels=15, cmap='RdBu_r')
plt.contour(grid_lon, grid_lat, grid_z, levels=15, colors='k', linewidths=0.5)
```

### plotly
`go.Contour(x=lons, y=lats, z=values)` or `go.Densitymapbox` for map-projected contours.

### altair
Not natively supported; requires pre-generated contour geometry as GeoJSON.

### excel / tableau
Not natively available. Use GIS tools (QGIS, ArcGIS) or Python pre-processing.

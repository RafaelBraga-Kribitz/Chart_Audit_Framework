---
name: Profile Map
category: Geospatial
input_type: [xyz-trivariate, time-series]
it_variants: []
analytical_function: Geographical
visual_family: Map
shape_primitive: [Line, Area]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, length, color-value]
tool_support: [matplotlib, plotly, d3]
failure_modes: [F, G]
alternatives: [topographic-map, isoline-map]
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
# Profile Map

## Description
A Profile Map (also called an Elevation Profile, Cross-Section Map, or Terrain Profile) shows a vertical cross-section of terrain or another geographic variable along a defined transect line. The x-axis represents distance along the transect; the y-axis represents the variable (typically elevation, temperature, or concentration). It is often paired with a plan-view map showing where the transect line runs. Profiles are essential in geology, hydrology, environmental science, and route planning.

## When to Use
- Showing how elevation or another variable changes along a specific route or transect
- Terrain assessment for route planning (cycling, hiking, road design)
- Geology cross-sections, hydrological profiles, atmospheric cross-sections
- When a single slice through the geographic space reveals the key spatial pattern

## When NOT to Use
- When the full 2D spatial distribution matters (use Topographic Map or Choropleth)
- Multiple crossing transects that are better shown as an isoline or surface map
- Data without a clear linear geographic extent

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| distance | numeric | Distance along transect from start (km, m) |
| elevation | numeric | Elevation or variable value at each point |
| lat, lon | numeric (optional) | For georeferencing the transect |

## Best Practices
- Label start and end points of the transect with place names
- Include a small location map showing where the transect line runs
- Annotate major terrain features (peaks, valleys, passes) directly on the profile
- Use a 1:1 vertical exaggeration ratio only when terrain scale permits; disclose exaggeration factor

## Common Mistakes
- Excessive vertical exaggeration that misrepresents terrain steepness without disclosure (smell G)
- Sampling the transect at too coarse a resolution, missing important terrain features (smell F)
- Not labelling the vertical exaggeration ratio, leaving viewers to interpret slopes incorrectly
- Confusing the profile distance (along-path) with horizontal distance for sloped terrain

## Implementation Notes

### matplotlib
```python
ax.fill_between(distance, elevation, alpha=0.3, color='saddlebrown')
ax.plot(distance, elevation, color='saddlebrown', linewidth=1.5)
ax.set_xlabel('Distance (km)')
ax.set_ylabel('Elevation (m)')
```

### plotly
`go.Scatter(x=distance, y=elevation, fill='tozeroy', mode='lines')` for an interactive profile with hover distance/elevation.

### altair
`mark_area()` with `x='distance:Q'` and `y='elevation:Q'`; add `mark_line()` layer on top.

### excel / tableau
**Excel**: Area or Line chart with distance on x-axis and elevation on y-axis. **Tableau**: Line chart with distance dimension.

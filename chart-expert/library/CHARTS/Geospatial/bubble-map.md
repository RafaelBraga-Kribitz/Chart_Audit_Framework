---
name: Bubble Map
category: Geospatial
input_type: [cat-value, xy-simple]
it_variants: []
analytical_function: Geographical
visual_family: Map
shape_primitive: [Circle]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Public]
complexity: Basic
encoding_channels: [position, area, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [F, J]
alternatives: [choropleth-map, pin-map, dot-density-map]
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
# Bubble Map

## Description
A Bubble Map places proportionally sized circles at geographic locations or region centroids, encoding a quantitative variable through circle area. It addresses the key limitation of Choropleth Maps — that large regions appear dominant regardless of their data value — by encoding magnitude through symbol size rather than polygon colour. A second variable can optionally be encoded through bubble colour.

## When to Use
- Showing absolute quantities (population, revenue, cases) at geographic points or centroids
- When polygon area should not drive visual prominence (as in choropleth)
- Comparing raw counts across locations where size differences are significant
- Encoding two variables simultaneously: quantity (size) and category or secondary metric (colour)

## When NOT to Use
- Data is a rate or density already — Choropleth is more appropriate
- Too many overlapping bubbles at a given scale (use clustering or reduce to top N)
- Very similar values where small circle size differences are imperceptible

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| latitude | numeric | WGS84 decimal degrees (or use centroid of region) |
| longitude | numeric | WGS84 decimal degrees |
| value | numeric (≥0) | Encodes bubble area |
| label | string | Location name |
| color_var | categorical/numeric (optional) | Secondary encoding |

## Best Practices
- Scale bubble area (not radius) proportionally to the value: `radius ∝ sqrt(value)`
- Set a maximum bubble size to prevent overlap at dense locations
- Use semi-transparent bubbles (alpha ~0.5–0.7) to allow overlap visibility
- Provide a size legend with at least 3 reference bubbles

## Common Mistakes
- Scaling bubble radius (not area) proportionally, over-exaggerating large values
- Placing bubbles at rough region centroids without disclosing that coordinates are approximate (smell F)
- Overlapping bubbles at the same location hiding individual values (smell J)
- Using too many colour categories making the legend unreadable

## Implementation Notes

### matplotlib
```python
ax.scatter(df.lon, df.lat, s=df.value / scale_factor,
           alpha=0.5, c=colors, edgecolors='white', linewidths=0.5)
```

### plotly
`go.Scattermapbox(lat=lats, lon=lons, mode='markers', marker=dict(size=sizes, sizemode='area', sizeref=sizeref))`.

### altair
`mark_circle()` with `size=alt.Size('value:Q', scale=alt.Scale(range=[10, 2000]))` on a geographic projection.

### excel / tableau
**Tableau**: Scatter map with circle marks; drag measure to Size shelf. **Excel**: 3D Maps with bubble chart layer.

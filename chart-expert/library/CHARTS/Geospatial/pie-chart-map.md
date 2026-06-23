---
name: Pie Chart Map
category: Geospatial
input_type: [cat-multi-value]
it_variants: []
analytical_function: Geographical
visual_family: Map
shape_primitive: [Polygon, Circle]
cardinality_fit: [small-N, medium]
audience: [Analytics, Public]
complexity: Intermediate
encoding_channels: [position, angle, area, color-hue]
tool_support: [matplotlib, d3, plotly]
failure_modes: [F, I, J]
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
# Pie Chart Map

## Description
A Pie Chart Map (also called a Proportional Symbol Pie Map) places small pie charts at geographic locations or region centroids, where the pie slices show the compositional breakdown of a variable at each location and the overall pie size can encode total volume. It combines the geographic positioning of a Bubble Map with the part-to-whole encoding of a Pie Chart, allowing simultaneous visualisation of where something is concentrated and what it is composed of.

## When to Use
- Showing compositional breakdown of a variable across geographic locations simultaneously (e.g., energy source mix by region)
- When both the relative proportions and the geographic distribution need to be visible at once
- Election results by district (vote share composition + location)

## When NOT to Use
- More than 4–5 categories per pie (slices become unreadable at small pie sizes)
- Dense geography where many small pies overlap
- When precise value comparison across locations is needed (a small-multiple bar chart is more accurate)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| latitude | numeric | WGS84 latitude (centroid or exact location) |
| longitude | numeric | WGS84 longitude |
| category | categorical | Pie slice categories (must be mutually exclusive) |
| value | numeric (≥0) | Value per category per location; pies normalise to 100% |
| total | numeric (optional) | Overall pie size encoding |

## Best Practices
- Size pies proportionally to total (area ∝ total); use a reference pie in the legend
- Use the same consistent colour palette for categories across all pies
- Limit to ≤4 slice categories per pie
- Ensure pies don't overlap by filtering to top N locations or using clustering

## Common Mistakes
- All pies the same size, losing the total magnitude information (smell F — misrepresenting spatial context)
- Categories not mutually exclusive, inflating pie totals (smell I)
- Too many pies at high density making basemap unreadable (smell J)
- Placing pies at geographic centroids without disclosing the approximation (smell F)

## Implementation Notes

### matplotlib
```python
for _, row in gdf.iterrows():
    ax_inset = ax.inset_axes([row.lon, row.lat, pie_w, pie_h],
                              transform=ax.transData)
    ax_inset.pie(row[categories], colors=palette, startangle=90)
    ax_inset.set_aspect('equal')
```

### plotly
No native pie-chart-map; use `go.Scattermapbox` for markers and overlay via `add_traces` per location with pre-built SVG pie icons.

### altair
Not natively supported; requires custom mark composition with transformed coordinates.

### excel / tableau
Not natively available in standard configurations. Use D3.js for production-quality pie chart maps.

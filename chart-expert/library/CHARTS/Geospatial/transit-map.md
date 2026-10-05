---
name: Transit Map
category: Geospatial
input_type: [cat-multi-value]
it_variants: [IT029]
analytical_function: Geographical
visual_family: Map
shape_primitive: [Line, Dot]
cardinality_fit: [medium, large]
audience: [Public, Executive]
complexity: Intermediate
encoding_channels: [position, color-hue, shape]
tool_support: [d3, matplotlib]
failure_modes: [F]
alternatives: [route-map, connection-map, network-diagram]
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
ibcs_status: preferred
questions: ["Where is the measure concentrated on Transit Map?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
---
# Transit Map

## Description
A Transit Map (also called a Schematic Map or Metro Map) is a stylised, topologically accurate but geographically distorted representation of a transport network (subway, bus, rail). Pioneered by Harry Beck's 1933 London Underground map, transit maps sacrifice geographic accuracy for clarity: lines are simplified to horizontal, vertical, or 45-degree angles; stations are evenly spaced; the overall topology (which lines connect at which stations) is preserved but distances are not. The design priority is wayfinding legibility, not geographic fidelity.

## When to Use
- Communicating the topology and connectivity of a transit or infrastructure network to end users
- Any schematic network diagram where topological relationships matter more than geographic distances
- Network status dashboards for operations teams

## When NOT to Use
- When geographic distances or travel times need to be accurately represented
- Data visualisation contexts where geographic truth is essential (use Route Map or Connection Map)
- Very small or very large networks where the schematic simplification adds confusion

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| station_id | string | Unique station identifier |
| station_name | string | Display name |
| line_id | string | Transit line identifier (encodes colour) |
| sequence | integer | Station order on the line |
| lat, lon | numeric | Actual coordinates (for geographic mode) or schematic x/y |

## Best Practices
- Assign a distinct colour to each transit line; maintain consistency across all materials
- Distinguish interchange stations (where lines cross) from single-line stations
- Use consistent spacing between stations within a line
- Angle lines only at 0°, 45°, or 90° for the classic schematic aesthetic
- Label all stations clearly, offset from the line

## Common Mistakes
- Preserving geographic distances rather than simplifying to 45° angles (loses readability)
- Too many simultaneous lines at interchanges without clear visual separation
- Using geographic coordinates directly without schematic simplification (smell F — geographic truth where schematic clarity is needed)


## Dashboard and other surfaces

status: placeholder

`Transit Map` can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with route-map, connection-map, network-diagram.

Suggested communication placement: **breakdown** zone. Vault coarse type, when a scraped template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Manual schematic coordinates
for line, stations in lines.items():
    xs = [s['x'] for s in stations]
    ys = [s['y'] for s in stations]
    ax.plot(xs, ys, color=line_color[line], linewidth=6, solid_capstyle='round')
    ax.scatter(xs, ys, s=100, color='white', edgecolors=line_color[line], zorder=5)
ax.axis('off')
```

### plotly
Use `go.Scatter` with `mode='lines+markers'` and manual schematic x/y coordinates.

### altair
`mark_line()` + `mark_point()` with manual schematic coordinates; no geographic projection needed.

### excel / tableau
Not well-suited for transit map design. Use D3.js, Figma, or dedicated transit mapping tools (e.g., Rail Map Online, MapTiler).

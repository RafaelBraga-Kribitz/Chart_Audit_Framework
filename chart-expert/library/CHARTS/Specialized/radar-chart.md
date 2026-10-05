---
name: Radar Chart
category: Specialized
input_type: [cat-multi-value]
it_variants: [IT029]
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Polygon, Line, Area]
cardinality_fit: [small-N]
audience: [Executive, Analytics]
complexity: Basic
encoding_channels: [position, area, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [I, J]
alternatives: [parallel-coordinates, lollipop-chart, bar-chart]
source: [datavizproject, datavizcatalogue]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: magnitude
ibcs_status: avoid
questions: ["Which category is higher on Radar Chart?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: dashboard
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
---
# Radar Chart

## Description
Also known as a Spider Chart, Web Chart, or Polar Chart. A Radar Chart displays multivariate data on equidistant axes radiating from a central point. Each axis represents one variable; values are plotted along the axis and connected by a polygon. Multiple entities can be overlaid as separate polygons for comparison. The enclosed area gives a general "shape profile" for each entity, though it is sensitive to axis ordering.

## When to Use
- Comparing the multivariate profile of 2–4 entities across 5–10 dimensions
- Performance dashboards where the "shape" of strengths and weaknesses is the message
- Sports analytics (athlete skill profiles), product feature comparisons

## When NOT to Use
- More than 4–5 overlapping entities (polygons obscure each other)
- More than 10 axes (becomes hard to read and axes feel arbitrary)
- When precise value comparison on individual dimensions matters — use a bar chart
- Variables on incommensurable scales that haven't been normalised

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| entity | categorical | One polygon per entity |
| dimension | categorical | One axis per dimension |
| value | numeric | Value for this entity on this dimension; all dimensions should share a scale |

## Best Practices
- Normalise all axes to the same scale (0–100 or z-scores) before plotting
- Limit to 3–4 entities to avoid visual clutter
- Explicitly label each axis with its variable name and scale endpoint
- Use fill with transparency (alpha 0.2–0.4) when overlaying multiple polygons

## Common Mistakes
- Axes with different scales making the enclosed area meaningless (smell I)
- Polygon area comparison across entities ignoring that area depends on axis ordering
- Silently dropping axes with missing values for some entities (smell J)
- Using radar when a simple bar chart grouped by entity would be clearer


## Dashboard and other surfaces

status: placeholder

`Radar Chart` is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with parallel-coordinates, lollipop-chart, bar-chart. `ibcs_status: avoid` applies to that communication surface only.

Suggested communication placement: **score** zone. Vault coarse type, when a scraped template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
angles = np.linspace(0, 2*np.pi, n_dims, endpoint=False).tolist()
angles += angles[:1]  # close polygon
ax = plt.subplot(111, polar=True)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(dimensions)
for entity, values in entities.items():
    vals = values + values[:1]
    ax.plot(angles, vals, label=entity)
    ax.fill(angles, vals, alpha=0.25)
```

### plotly
`go.Scatterpolar(r=values, theta=dimensions, fill='toself')` per entity.

### altair
Not natively supported; use polar coordinate transformation manually.

### excel / tableau
**Excel**: Insert → Radar Chart. **Tableau**: Radar charts require calculated fields to convert to polar coordinates.

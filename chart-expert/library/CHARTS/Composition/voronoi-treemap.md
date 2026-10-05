---
name: Voronoi Treemap
category: Composition
input_type: [hierarchical-cat, composition]
it_variants: [IT024, IT007]
analytical_function: Part-to-whole
visual_family: Chart
ft_family: part-to-whole
shape_primitive: [Polygon]
cardinality_fit: [medium]
audience: [Executive, Analytics, Technical, Public]
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
complexity: Advanced
encoding_channels: [area]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bar-chart, line-chart, data-table]
ibcs_status: conditional
questions: ["How is the whole split on Voronoi Treemap?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: dashboard
source: [gap-list]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---
# Voronoi Treemap

## Description
A Voronoi treemap fills a shape with cells whose area encodes a value, without a rectangular treemap's aspect ratios.

## When to Use
- Hierarchical magnitudes in an analytical view

## When NOT to Use
- Precise comparison of close values

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | hierarchical-cat, composition | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Cells the reader must compare by area alone with no labels


## Dashboard and other surfaces

status: placeholder

`Voronoi Treemap` is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with bar-chart, line-chart, data-table. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Vault coarse type, when a scraped template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.


## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type hierarchical-cat before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Voronoi Treemap")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `hierarchical-cat`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes area. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

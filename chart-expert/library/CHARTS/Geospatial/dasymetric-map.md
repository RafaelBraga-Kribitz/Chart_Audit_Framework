---
name: Dasymetric Map
category: Geospatial
input_type: [cat-value]
it_variants: [IT026, IT005]
analytical_function: Geographical
visual_family: Map
shape_primitive: [Polygon]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [color-value]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [choropleth-map, bubble-map, data-table]
source: [gap-list]
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

# Dasymetric Map

## Description
A dasymetric map redistributes a value using a related land or population layer so the shade follows where the phenomenon can exist.

## When to Use
- Analyst and researcher maps of rates that official boundaries distort

## When NOT to Use
- A quick executive choropleth

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | cat-value | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- A redistribution with no stated layer

## Dashboard and other surfaces

status: placeholder

Dasymetric Map is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with `choropleth-map`, `bubble-map`, `data-table`. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type cat-value before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Dasymetric Map")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `cat-value`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes color-value. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

---
name: Hierarchical Edge Bundling
category: Relationship
input_type: [hierarchical-cat, matrix-grid]
it_variants: [IT024, IT037, IT021, IT028]
analytical_function: Flow
visual_family: Diagram
shape_primitive: [Line]
cardinality_fit: [large]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [sankey-diagram, flow-chart, data-table]
source: [gap-list]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: flow
ibcs_status: conditional
questions: ["How does quantity move between states?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: none
---

# Hierarchical Edge Bundling

## Description
Hierarchical edge bundling groups links that share an ancestor so a dense network becomes a set of bundles.

## When to Use
- Large adjacency structures in a technical review

## When NOT to Use
- A small network a node-link diagram can show
- A precise path reading

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | hierarchical-cat, matrix-grid | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Bundles that look like volume they do not encode

## Dashboard and other surfaces

status: placeholder

Hierarchical Edge Bundling is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with `sankey-diagram`, `flow-chart`, `data-table`. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type hierarchical-cat before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Hierarchical Edge Bundling")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `hierarchical-cat`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, color-hue. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

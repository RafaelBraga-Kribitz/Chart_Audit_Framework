---
name: RadViz
category: Relationship
input_type: [cat-multi-value]
it_variants: [IT029, IT031]
analytical_function: Correlation
visual_family: Plot
shape_primitive: [Dot]
cardinality_fit: [medium]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [position]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [scatter-plot, connected-scatter-plot, data-table]
source: [gap-list]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: correlation
ibcs_status: conditional
questions: ["Do the two measures move together, and where do they not?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: none
---

# RadViz

## Description
RadViz places features around a circle and pulls each point toward the features where it is high.

## When to Use
- A multivariate exploratory view

## When NOT to Use
- A claim about a precise distance

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | cat-multi-value | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Feature order that silently changes the picture

## Dashboard and other surfaces

status: placeholder

RadViz is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with `scatter-plot`, `connected-scatter-plot`, `data-table`. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type cat-multi-value before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("RadViz")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `cat-multi-value`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

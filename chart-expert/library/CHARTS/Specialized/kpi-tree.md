---
name: KPI Tree
category: Specialized
input_type: [hierarchical-cat]
it_variants: [IT024, IT037]
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Line]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics]
complexity: Basic
encoding_channels: [position]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [flow-chart, data-table]
source: [gap-list]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: none
ibcs_status: preferred
questions: ["What structure or process does the diagram explain?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
---

# KPI Tree

## Description
A KPI tree decomposes an outcome into the inputs of its formula. It is a model of the measure, not a chart of a time series.

## When to Use
- Explaining a formula to any audience
- From contribution margin down to hours and rate

## When NOT to Use
- A decorative org chart of departments

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | hierarchical-cat | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Nodes that are not actually in the formula

## Dashboard and other surfaces

status: placeholder

KPI Tree can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `flow-chart`, `data-table`.

Suggested communication placement: **detail** zone. Coarse template type, when a Databox or Zebra template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type hierarchical-cat before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("KPI Tree")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `hierarchical-cat`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

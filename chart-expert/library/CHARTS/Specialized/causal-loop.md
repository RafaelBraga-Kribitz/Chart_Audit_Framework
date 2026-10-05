---
name: Causal Loop Diagram
category: Specialized
input_type: [matrix-grid]
it_variants: [IT021, IT028]
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Intermediate
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

# Causal Loop Diagram

## Description
A causal loop diagram shows reinforcing and balancing feedback with signed arrows. It is a theory, not a measured flow.

## When to Use
- Systems conversations in strategy or R&D

## When NOT to Use
- A Sankey of real quantities

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | matrix-grid | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Arrows labeled as data when they are hypotheses

## Dashboard and other surfaces

status: placeholder

Causal Loop Diagram can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `flow-chart`, `data-table`.

Suggested communication placement: **detail** zone. Coarse template type, when a Databox or Zebra template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type matrix-grid before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Causal Loop Diagram")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `matrix-grid`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

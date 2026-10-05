---
name: Cumulative Flow Diagram
category: Temporal
input_type: [time-series, composition]
it_variants: [IT018, IT007, IT016, IT020, IT023]
analytical_function: Flow
visual_family: Chart
shape_primitive: [Area]
cardinality_fit: [medium]
audience: [Analytics, Technical]
complexity: Intermediate
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
ibcs_status: preferred
questions: ["How does quantity move between states?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
---

# Cumulative Flow Diagram

## Description
A cumulative flow diagram stacks the count of items in each workflow state over time. Band width is queue size.

## When to Use
- Development and operations flow
- Seeing a bottleneck as a widening band

## When NOT to Use
- A state model that is not a real sequence

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | time-series, composition | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- A stacked area of unrelated categories

## Dashboard and other surfaces

status: placeholder

Cumulative Flow Diagram can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `sankey-diagram`, `flow-chart`, `data-table`.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type time-series before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Cumulative Flow Diagram")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `time-series`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, color-hue. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

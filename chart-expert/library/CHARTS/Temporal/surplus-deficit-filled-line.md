---
name: Surplus-Deficit Filled Line
category: Temporal
input_type: [time-series]
it_variants: [IT018]
analytical_function: Deviation
visual_family: Chart
shape_primitive: [Line, Area]
cardinality_fit: [medium, large]
audience: [Executive, Analytics, Public]
complexity: Intermediate
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [diverging-bar, bullet-graph, waterfall-chart]
source: [chart.guide]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: deviation
ibcs_status: preferred
questions: ["How far is the result from the reference, and in which direction?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
---

# Surplus-Deficit Filled Line

## Description
A filled line shades the area between a series and its reference, one color above and another below, so surplus and deficit periods read at a glance.

## When to Use
- Balance of trade, budget versus actual over time, temperature against a normal

## When NOT to Use
- A reference that changes definition mid-series

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | time-series | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Color as the only sign of the direction
- A reference line that is not drawn

## Dashboard and other surfaces

status: placeholder

Surplus-Deficit Filled Line can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `diverging-bar`, `bullet-graph`, `waterfall-chart`.

Suggested communication placement: **variance** zone. Coarse template type, when a Databox or Zebra template is the layout: **Line**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type time-series before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Surplus-Deficit Filled Line")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `time-series`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, color-hue. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

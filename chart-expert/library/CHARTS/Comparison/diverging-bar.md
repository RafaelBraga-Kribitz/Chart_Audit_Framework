---
name: Diverging Bar
category: Comparison
input_type: [cat-value]
it_variants: [IT026, IT005]
analytical_function: Deviation
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Public]
complexity: Basic
encoding_channels: [position, length]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bullet-graph, waterfall-chart]
source: [gap-list]
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
related_kpis: [kpi.portfolio-and-project-management.estimated-versus-actual-project-cost, kpi.portfolio-and-project-management.estimated-versus-actual-project-time]
analysis_surface: plot
communication_surface: dashboard
---

# Diverging Bar

## Description
A diverging bar grows left or right from a baseline so the sign of the gap is the position.

## When to Use
- Actual versus plan
- Sentiment or surplus and deficit
- Executive variance

## When NOT to Use
- A baseline that is not meaningful

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | cat-value | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Sorting alphabetically
- A y-axis that does not include the baseline

## Dashboard and other surfaces

status: placeholder

Diverging Bar can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `bullet-graph`, `waterfall-chart`.

Suggested communication placement: **variance** zone. Coarse template type, when a Databox or Zebra template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type cat-value before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Diverging Bar")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `cat-value`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, length. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

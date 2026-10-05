---
name: Forest Plot
category: Comparison
input_type: [cat-value, interval-range]
it_variants: [IT026, IT005, IT040, IT017]
analytical_function: Comparison
visual_family: Plot
shape_primitive: [Dot, Line]
cardinality_fit: [medium]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [position]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bar-chart, dot-plot, data-table]
source: [gap-list]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: magnitude
ibcs_status: conditional
questions: ["Which category is larger, and by how much?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: none
---

# Forest Plot

## Description
A forest plot shows an estimate and an interval for each study, group, or model, often with a pooled mark.

## When to Use
- Research synthesis
- A data scientist comparing segments with uncertainty

## When NOT to Use
- A dashboard of point KPIs with no interval

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | cat-value, interval-range | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Intervals that are not the same statistic

## Dashboard and other surfaces

status: placeholder

Forest Plot is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with `bar-chart`, `dot-plot`, `data-table`. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type cat-value before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Forest Plot")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `cat-value`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

---
name: Frequency Polygon
category: Distribution
input_type: [xy-simple, demo-grouped]
it_variants: [IT001, IT034, IT011]
analytical_function: Distribution
visual_family: Chart
shape_primitive: [Line]
cardinality_fit: [medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [histogram, box-plot, strip-plot]
source: [gap-list]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: distribution
ibcs_status: preferred
questions: ["What is the shape and the tail, not only the average?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
---

# Frequency Polygon

## Description
A frequency polygon joins bin counts with a line so several distributions can be overlaid more lightly than histograms.

## When to Use
- Comparing a few distributions in an analysis notebook

## When NOT to Use
- A single precise bin count for an audit

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | xy-simple, demo-grouped | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Bins of unequal width drawn as if they were equal

## Dashboard and other surfaces

status: placeholder

Frequency Polygon can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `histogram`, `box-plot`, `strip-plot`.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type xy-simple before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Frequency Polygon")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `xy-simple`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

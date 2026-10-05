---
name: Radial Bar Chart
category: Comparison
input_type: [cat-value]
it_variants: [IT026, IT005]
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [angle, length]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bar-chart, dot-plot, data-table]
source: [datavizcatalogue]
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
communication_surface: dashboard
---

# Radial Bar Chart

## Description
A radial bar chart bends each bar into a concentric arc. Outer arcs look longer than inner arcs with the same value.

## When to Use
- A decorative summary of a handful of categories

## When NOT to Use
- Precise comparison
- More than a handful of categories

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | cat-value | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Sorting so the largest value sits on the inner ring

## Dashboard and other surfaces

status: placeholder

Radial Bar Chart can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `bar-chart`, `dot-plot`, `data-table`.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type cat-value before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Radial Bar Chart")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `cat-value`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes angle, length. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

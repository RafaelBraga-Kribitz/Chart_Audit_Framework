---
name: Icon Array
category: Composition
input_type: [composition]
it_variants: [IT007, IT016, IT020, IT023]
analytical_function: Part-to-whole
visual_family: Glyph
shape_primitive: [Icon]
cardinality_fit: [small-N]
audience: [Public, Executive]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [stacked-bar-chart, waffle-chart, data-table]
source: [gap-list]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: part-to-whole
ibcs_status: preferred
questions: ["How is the whole split, and which part matters?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
---

# Icon Array

## Description
An icon array shows a percent as a grid of marks, usually out of 100 or 10.

## When to Use
- Risk communication
- A share a public audience must feel

## When NOT to Use
- More than two or three classes
- Precise audit values

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | composition | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- A grid whose total is not obvious

## Dashboard and other surfaces

status: placeholder

Icon Array can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `stacked-bar-chart`, `waffle-chart`, `data-table`.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type composition before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Icon Array")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `composition`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, color-hue. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

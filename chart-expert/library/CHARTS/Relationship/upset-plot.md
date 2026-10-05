---
name: UpSet Plot
category: Relationship
input_type: [demo-grouped, matrix-grid]
it_variants: [IT011, IT021, IT028]
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Bar, Dot]
cardinality_fit: [medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, length]
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

# UpSet Plot

## Description
An UpSet plot shows intersection sizes of many sets. Dots mark which sets are in each intersection. Bars show the size.

## When to Use
- More than three sets, where a Venn diagram fails
- Research and product analytics

## When NOT to Use
- Two or three sets a bar can show

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | demo-grouped, matrix-grid | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Unsorted intersections
- A Venn of six sets

## Dashboard and other surfaces

status: placeholder

UpSet Plot can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `stacked-bar-chart`, `waffle-chart`, `data-table`.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type demo-grouped before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("UpSet Plot")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `demo-grouped`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, length. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

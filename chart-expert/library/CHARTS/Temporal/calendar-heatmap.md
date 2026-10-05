---
name: Calendar Heatmap
category: Temporal
input_type: [time-series, matrix-grid]
it_variants: [IT001, IT021]
analytical_function: Trend-over-time
visual_family: Chart
ft_family: change
shape_primitive: [Square]
cardinality_fit: [large]
audience: [Executive, Analytics, Technical, Public]
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
complexity: Basic
encoding_channels: [color-value, position]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bar-chart, line-chart, data-table]
ibcs_status: preferred
questions: ["How has the series changed over time on Calendar Heatmap?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: dashboard
source: [gap-list]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---
# Calendar Heatmap

## Description
A calendar heatmap maps one value onto each day in a year grid.

## When to Use
- Daily activity, outages, or publishing cadence
- A year at a glance

## When NOT to Use
- Comparing precise magnitudes
- More than one measure per day

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | time-series, matrix-grid | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- A color scale with no zero
- Tiny cells with no tooltip or table behind them


## Dashboard and other surfaces

status: placeholder

`Calendar Heatmap` can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with bar-chart, line-chart, data-table.

Suggested communication placement: **trend** zone. Vault coarse type, when a scraped template is the layout: **Heatmap**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.


## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type time-series before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Calendar Heatmap")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `time-series`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes color-value, position. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

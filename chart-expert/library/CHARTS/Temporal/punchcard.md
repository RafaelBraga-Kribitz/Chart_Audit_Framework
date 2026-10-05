---
name: Punchcard Plot
category: Temporal
input_type: [matrix-grid, time-series]
it_variants: [IT021, IT001]
analytical_function: Trend-over-time
visual_family: Plot
ft_family: change
shape_primitive: [Circle]
cardinality_fit: [medium]
audience: [Executive, Analytics, Technical, Public]
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
complexity: Intermediate
encoding_channels: [position, area]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bar-chart, line-chart, data-table]
ibcs_status: preferred
questions: ["How has the series changed over time on Punchcard Plot?", "Who is the audience, and is this the analysis surface or the communication surface?"]
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
# Punchcard Plot

## Description
A punchcard places a mark on a weekday-by-hour grid. Size or color encodes the count.

## When to Use
- When work, incidents, or traffic cluster in the week
- Operations analytics

## When NOT to Use
- Precise reading of small differences in area

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | matrix-grid, time-series | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Encoding the value only as area


## Dashboard and other surfaces

status: placeholder

`Punchcard Plot` can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with bar-chart, line-chart, data-table.

Suggested communication placement: **trend** zone. Vault coarse type, when a scraped template is the layout: **Line**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.


## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type matrix-grid before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Punchcard Plot")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `matrix-grid`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, area. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

---
name: Heikin-Ashi Chart
category: Temporal
input_type: [interval-range, time-series]
it_variants: [IT040, IT001]
analytical_function: Trend-over-time
visual_family: Chart
ft_family: change
shape_primitive: [Bar]
cardinality_fit: [medium]
audience: [Executive, Analytics, Technical, Public]
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
complexity: Advanced
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bar-chart, line-chart, data-table]
ibcs_status: conditional
questions: ["How has the series changed over time on Heikin-Ashi Chart?", "Who is the audience, and is this the analysis surface or the communication surface?"]
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
# Heikin-Ashi Chart

## Description
Heikin-Ashi replaces each open and close with a smoothed average of recent prices so the trend is easier to see and the exact price is harder to read.

## When to Use
- Trend direction in a trading notebook

## When NOT to Use
- Reporting an actual close to a finance audience
- Any KPI that is not a price

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | interval-range, time-series | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Treating the smoothed close as the real close


## Dashboard and other surfaces

status: placeholder

`Heikin-Ashi Chart` is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with bar-chart, line-chart, data-table. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **trend** zone. Vault coarse type, when a scraped template is the layout: **Line**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.


## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type interval-range before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Heikin-Ashi Chart")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `interval-range`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, color-hue. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

---
name: Survival Curve
category: Temporal
input_type: [time-series, interval-range]
it_variants: [IT018, IT040, IT017]
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Line]
cardinality_fit: [medium]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [position]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [line-chart, sparkline, area-chart]
source: [gap-list]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: change-over-time
ibcs_status: conditional
questions: ["How has the series changed over time?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: [kpi.sales-and-customer-service.customer-churn-rate, kpi.sales-and-customer-service.customer-retention]
analysis_surface: notebook
communication_surface: none
---

# Survival Curve

## Description
A survival curve shows the share of a cohort still in a state as time passes, accounting for cases that have not finished.

## When to Use
- Retention research, reliability, clinical or product cohorts

## When NOT to Use
- A simple churn percent with no time axis

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | time-series, interval-range | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Dropping censored cases and calling the rest a rate

## Dashboard and other surfaces

status: placeholder

Survival Curve is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with `line-chart`, `sparkline`, `area-chart`. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **trend** zone. Coarse template type, when a Databox or Zebra template is the layout: **Line**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type time-series before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Survival Curve")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `time-series`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

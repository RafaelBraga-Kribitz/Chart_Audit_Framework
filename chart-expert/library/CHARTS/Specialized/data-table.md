---
name: Data Table
category: Specialized
input_type: [cat-multi-value, matrix-grid]
it_variants: [IT029, IT031, IT021, IT028]
analytical_function: Comparison
visual_family: Table
shape_primitive: [Square]
cardinality_fit: [medium, large]
audience: [Executive, Analytics, Technical, Public]
complexity: Basic
encoding_channels: [position]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bar-chart, dot-plot]
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
ibcs_status: preferred
questions: ["Which category is larger, and by how much?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: [kpi.portfolio-and-project-management.estimated-versus-actual-project-cost, kpi.portfolio-and-project-management.estimated-versus-actual-project-time, kpi.portfolio-and-project-management.project-contribution-margin]
analysis_surface: plot
communication_surface: dashboard
---

# Data Table

## Description
A data table shows entities in rows and measures in columns. It is the right chart when the reader must look up a value.

## When to Use
- Detail zones
- Any audience that needs the number itself
- The most common scraped dashboard mark

## When NOT to Use
- A pattern that a bar would show faster, when lookup is not the job

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | cat-multi-value, matrix-grid | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Too many decimals
- No unit in the column header
- Color as the only encoding of a variance

## Dashboard and other surfaces

status: placeholder

Data Table can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `bar-chart`, `dot-plot`.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Table**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type cat-multi-value before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Data Table")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `cat-multi-value`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

---
name: Triangle Bar Chart
category: Comparison
input_type: [cat-value]
it_variants: [IT026]
analytical_function: Comparison
visual_family: Chart
ft_family: magnitude
shape_primitive: [Line]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Technical, Public]
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
complexity: Intermediate
encoding_channels: [position]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bar-chart, line-chart, data-table]
ibcs_status: preferred
questions: ["Which category is higher on Triangle Bar Chart?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: dashboard
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---
# Triangle Bar Chart

## Description
Triangle Bar Chart is the chart type catalogued under this name. Use it for a comparison question when the data match cat-value. On an analysis surface (notebook, pandas, or matplotlib) it can stay technical. On an executive or client surface, prefer a simpler cousin if this encoding is hard to read.

## When to Use
- A comparison question with data shaped as cat-value
- Confirm the encoding against the audience before it leaves a notebook

## When NOT to Use
- A different analytical question than Comparison
- An audience that cannot read the encoding, unless a simpler chart carries the message

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | cat-value | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Choosing it because the tool defaults to it
- Using it on an executive page when a bar, line, or table would answer the question


## Dashboard and other surfaces

status: placeholder

`Triangle Bar Chart` can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with bar-chart, line-chart, data-table.

Suggested communication placement: **score** zone. Vault coarse type, when a scraped template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.


## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type cat-value before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Triangle Bar Chart")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `cat-value`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

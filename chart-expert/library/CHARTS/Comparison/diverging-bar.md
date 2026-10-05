---
name: Diverging Bar
category: Comparison
input_type: [cat-value]
it_variants: [IT026]
analytical_function: Deviation
visual_family: Chart
ft_family: deviation
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Technical, Public]
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
complexity: Basic
encoding_channels: [position, length]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bar-chart, line-chart, data-table]
ibcs_status: preferred
questions: ["How far is the result from the reference on Diverging Bar?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: [kpi.accounting.customer-invoices-paid-through-electronic-sourcing, kpi.accounting.accuracy-of-expense-reimbursement-requests, kpi.accounting.by-electronic-invoices, kpi.accounting.employees-managing-the-accounting-processes, kpi.accounting.employees-allocated-to-execute-and-manage-financial-performance, kpi.accounting.employees-allocated-to-fixe-and-manage-financial-performance, kpi.accounting.employees-allocated-to-fixed-asset-management, kpi.accounting.employees-allocated-to-general-accounting-and-reporting]
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
# Diverging Bar

## Description
A diverging bar grows left or right from a baseline so the sign of the gap is the position.

## When to Use
- Actual versus plan
- Sentiment or surplus and deficit
- Executive variance

## When NOT to Use
- A baseline that is not meaningful

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | cat-value | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Sorting alphabetically
- A y-axis that does not include the baseline


## Dashboard and other surfaces

status: placeholder

`Diverging Bar` can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with bar-chart, line-chart, data-table.

Suggested communication placement: **variance** zone. Vault coarse type, when a scraped template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.


## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type cat-value before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Diverging Bar")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `cat-value`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, length. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

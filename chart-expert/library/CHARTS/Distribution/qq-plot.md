---
name: Q-Q Plot
category: Distribution
input_type: [xy-simple]
it_variants: [IT001]
analytical_function: Distribution
visual_family: Plot
ft_family: distribution
shape_primitive: [Dot]
cardinality_fit: [medium, large]
audience: [Executive, Analytics, Technical, Public]
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
complexity: Advanced
encoding_channels: [position]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bar-chart, line-chart, data-table]
ibcs_status: conditional
questions: ["What is the shape and the tail, not only the average, on Q-Q Plot?", "Who is the audience, and is this the analysis surface or the communication surface?"]
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
# Q-Q Plot

## Description
A Q-Q plot compares the quantiles of a sample with a reference distribution or another sample.

## When to Use
- Model checking in a notebook
- Asking whether a residual is roughly normal

## When NOT to Use
- A business dashboard

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | xy-simple | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- A diagonal that is decorative rather than the reference


## Dashboard and other surfaces

status: placeholder

`Q-Q Plot` is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with bar-chart, line-chart, data-table. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Vault coarse type, when a scraped template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.


## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type xy-simple before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Q-Q Plot")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `xy-simple`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

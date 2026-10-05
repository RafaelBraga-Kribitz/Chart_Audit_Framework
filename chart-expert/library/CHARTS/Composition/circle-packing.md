---
name: Circle Packing
category: Composition
input_type: [hierarchical-cat, composition]
it_variants: [IT024, IT007]
analytical_function: Part-to-whole
visual_family: Chart
ft_family: part-to-whole
shape_primitive: [Circle]
cardinality_fit: [medium]
audience: [Executive, Analytics, Technical, Public]
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
complexity: Intermediate
encoding_channels: [area]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [bar-chart, line-chart, data-table]
ibcs_status: preferred
questions: ["How is the whole split on Circle Packing?", "Who is the audience, and is this the analysis surface or the communication surface?"]
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
# Circle Packing

## Description
Circle packing nests circles whose area encodes value. It is distinct from a packed bubble that has no containment.

## When to Use
- A hierarchy when containment is the message

## When NOT to Use
- Precise rank of close values
- The existing packed-circle card when there is no nesting

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | hierarchical-cat, composition | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Radius used instead of area


## Dashboard and other surfaces

status: placeholder

`Circle Packing` can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with bar-chart, line-chart, data-table.

Suggested communication placement: **breakdown** zone. Vault coarse type, when a scraped template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.


## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type hierarchical-cat before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Circle Packing")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `hierarchical-cat`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes area. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

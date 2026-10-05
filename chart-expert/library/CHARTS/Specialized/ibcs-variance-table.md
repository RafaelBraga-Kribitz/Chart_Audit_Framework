---
name: IBCS Variance Table
category: Specialized
input_type: [cat-multi-value]
it_variants: [IT029, IT031]
analytical_function: Deviation
visual_family: Table
shape_primitive: [Bar, Line]
cardinality_fit: [medium, large]
audience: [Executive, Analytics]
complexity: Intermediate
encoding_channels: [position, length]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [diverging-bar, bullet-graph, waterfall-chart]
source: [gap-list]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: deviation
ibcs_status: preferred
questions: ["How far is the result from the reference, and in which direction?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
---

# IBCS Variance Table

## Description
An IBCS-style variance table puts the entity, actual, plan, absolute variance, percent variance, and a sparkline or bullet on one row.

## When to Use
- Finance, operations, and any actual-versus-plan communication
- Executive and analyst reviews

## When NOT to Use
- A table of unrelated metrics with traffic lights

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | cat-multi-value | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Variances with inconsistent signs
- A sparkline on a different scale per row without a note

## Dashboard and other surfaces

status: placeholder

IBCS Variance Table can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `diverging-bar`, `bullet-graph`, `waterfall-chart`.

Suggested communication placement: **variance** zone. Coarse template type, when a Databox or Zebra template is the layout: **Table**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type cat-multi-value before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("IBCS Variance Table")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `cat-multi-value`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, length. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

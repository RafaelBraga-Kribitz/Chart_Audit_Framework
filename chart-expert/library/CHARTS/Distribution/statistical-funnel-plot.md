---
name: Statistical Funnel Plot
category: Distribution
input_type: [xy-simple, cat-value]
it_variants: [IT001, IT034, IT026, IT005]
analytical_function: Deviation
visual_family: Plot
shape_primitive: [Dot]
cardinality_fit: [medium]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [position]
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
ibcs_status: conditional
questions: ["How far is the result from the reference, and in which direction?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: none
---

# Statistical Funnel Plot

## Description
A statistical funnel plot shows an estimate against its precision, with control limits that narrow as the sample grows. It is not a sales funnel.

## When to Use
- Institution or site comparisons in research and quality

## When NOT to Use
- A stage-conversion story

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | xy-simple, cat-value | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Limits that ignore the sample size

## Dashboard and other surfaces

status: placeholder

Statistical Funnel Plot is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with `diverging-bar`, `bullet-graph`, `waterfall-chart`. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **variance** zone. Coarse template type, when a Databox or Zebra template is the layout: **Funnel**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type xy-simple before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Statistical Funnel Plot")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `xy-simple`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

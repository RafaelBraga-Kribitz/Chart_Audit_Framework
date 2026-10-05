---
name: Ridgeline Plot
category: Distribution
input_type: [cat-value, demo-grouped]
it_variants: [IT026, IT005, IT011]
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Area]
cardinality_fit: [medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, area]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [histogram, box-plot, strip-plot]
source: [gap-list]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: distribution
ibcs_status: preferred
questions: ["What is the shape and the tail, not only the average?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
---

# Ridgeline Plot

## Description
Ridgelines stack partially overlapping density curves so several groups can be compared.

## When to Use
- A data scientist comparing distributions across segments

## When NOT to Use
- An executive score
- More groups than the overlap can bear

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | cat-value, demo-grouped | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Hidden baselines
- Densities with different sample sizes and no note

## Dashboard and other surfaces

status: placeholder

Ridgeline Plot can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `histogram`, `box-plot`, `strip-plot`.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type cat-value before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Ridgeline Plot")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `cat-value`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, area. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

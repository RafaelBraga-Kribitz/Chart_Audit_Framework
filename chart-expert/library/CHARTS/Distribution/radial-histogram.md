---
name: Radial Histogram
category: Distribution
input_type: [xy-simple]
it_variants: [IT001, IT034]
analytical_function: Distribution
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [length, angle]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [histogram, box-plot, strip-plot]
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: distribution
ibcs_status: conditional
questions: ["What is the shape and the tail, not only the average?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: none
---

# Radial Histogram

## Description
A radial histogram bins a cyclic variable (hour of day, compass direction, month) around a circle so the wrap-around is visible.

## When to Use
- Wind direction, time-of-day activity, seasonal counts in a notebook

## When NOT to Use
- A variable that is not cyclic

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | xy-simple | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Bar area that grows with radius and overstates the outer bins

## Dashboard and other surfaces

status: placeholder

Radial Histogram is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with `histogram`, `box-plot`, `strip-plot`. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type xy-simple before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Radial Histogram")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `xy-simple`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes length, angle. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

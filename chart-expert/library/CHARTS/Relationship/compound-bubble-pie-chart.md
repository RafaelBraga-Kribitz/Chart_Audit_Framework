---
name: Compound Bubble and Pie Chart
category: Relationship
input_type: [xyz-trivariate, composition]
it_variants: [IT012, IT007, IT016, IT020, IT023]
analytical_function: Correlation
visual_family: Chart
shape_primitive: [Circle]
cardinality_fit: [small-N]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [position, area, angle]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: [scatter-plot, connected-scatter-plot, data-table]
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: correlation
ibcs_status: avoid
questions: ["Do the two measures move together, and where do they not?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: none
---

# Compound Bubble and Pie Chart

## Description
Each bubble is itself a pie, so position, area, and angle all carry data at once.

## When to Use
- Recognizing the form when auditing a legacy report

## When NOT to Use
- Any decision page
- Precise reading of any of the three encodings

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | xyz-trivariate, composition | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
- Comparing slice angles across bubbles of different size

## Dashboard and other surfaces

status: placeholder

Compound Bubble and Pie Chart is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with `scatter-plot`, `connected-scatter-plot`, `data-table`. `ibcs_status: avoid` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Bubble**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type xyz-trivariate before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("Compound Bubble and Pie Chart")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `xyz-trivariate`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes position, area, angle. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.

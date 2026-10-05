---
name: Semi-Circle Donut Chart
category: Composition
input_type: [composition]
it_variants: [IT007]
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Polygon]
cardinality_fit: [small-N]
audience: [Executive, Public]
complexity: Basic
encoding_channels: [angle, area, color-hue]
tool_support: [matplotlib, plotly, d3, tableau, powerbi]
failure_modes: [I, J]
alternatives: [donut-chart, angular-gauge, bullet-graph]
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: part-to-whole
ibcs_status: avoid
questions: ["How is the whole split on Semi-Circle Donut Chart?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: dashboard
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
---
# Semi-Circle Donut Chart

## Description
A Semi-Circle Donut Chart is a half-ring variant of the Donut Chart, spanning 180 degrees instead of 360. It is commonly used as a progress or gauge indicator for a single primary metric alongside its complement (e.g., 72% complete vs 28% remaining). The flat bottom edge saves vertical space, making it popular in dashboard headers and KPI cards.

## When to Use
- Displaying a single percentage or progress value against a whole
- KPI dashboards where vertical space is at a premium
- When a gauge metaphor (speedometer-style) is more intuitive to the audience than a bar

## When NOT to Use
- Comparing multiple categories with more than 2 segments (a full donut or bar is clearer)
- Datasets that do not naturally express as a fraction of 100%
- High-precision comparisons where exact values matter

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| value | numeric [0–100] | The primary metric (percentage complete, share, etc.) |
| complement | numeric | Usually 100 − value; may be implicit |

## Best Practices
- Annotate the centre or below the arc with the numeric value prominently
- Use two segments only: primary metric and remainder
- Ensure the colour for the primary arc has high contrast against the background ring
- Add a text label for context (goal, benchmark, or category name)

## Common Mistakes
- Encoding more than 2 segments, which defeats the gauge purpose
- Omitting the numeric label, leaving readers to estimate arc length
- Using this chart for data that does not logically sum to 100% (smell I)
- Placing multiple semi-circle donuts in a grid without consistent scales


## Dashboard and other surfaces

status: placeholder

`Semi-Circle Donut Chart` is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with donut-chart, angular-gauge, bullet-graph. `ibcs_status: avoid` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Vault coarse type, when a scraped template is the layout: **Donut**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))
ax.pie([value, 100-value], startangle=180, counterclock=False,
       wedgeprops=dict(width=0.4))
ax.set_ylim(-1, 0.5)  # crop to upper semicircle
```

### plotly
Use `go.Pie` with `rotation=180`, `direction='clockwise'`, and limit data to 2 values; clip display using layout margins.

### altair
Not natively supported; requires custom arc transform with `theta` range limited to π.

### excel / tableau
**Tableau**: Dual-axis pie trick clipped to 180° using angle calculation. **Excel**: Doughnut chart with a transparent "filler" slice of 50%.

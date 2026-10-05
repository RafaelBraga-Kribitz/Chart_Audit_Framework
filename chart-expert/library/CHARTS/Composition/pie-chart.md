---
name: Pie Chart
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
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [I, J]
alternatives: [stacked-bar-100pct, donut-chart, waffle-chart]
source: [datavizproject, datavizcatalogue]
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
questions: ["How is the whole split on Pie Chart?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: dashboard
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
---
# Pie Chart

## Description
A Pie Chart divides a circle into proportional segments, where each arc length represents the share of a category in the total. The full circle equals 100% of the data. It gives readers a fast intuitive sense of proportional distribution but struggles with precision when segments are close in size.

## When to Use
- Showing part-to-whole composition with 2–5 categories
- One dominant slice needs to be communicated quickly to a non-technical audience
- Space is limited and a quick proportional overview suffices

## When NOT to Use
- More than 6–7 categories (slices become unreadably thin)
- Precise comparisons between categories are required
- Comparing multiple pie charts side-by-side (area comparison is unreliable)
- Data does not sum to a meaningful whole

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | Each unique value becomes one slice |
| value | numeric (≥0) | Determines arc length; values summed to 100% |

## Best Practices
- Order slices from largest to smallest, starting at 12 o'clock
- Limit to ≤6 slices; aggregate remainder into "Other"
- Label slices directly with percentage rather than relying on a legend
- Use a single sequential or categorical palette — avoid rainbow schemes
- Confirm all slices are mutually exclusive and collectively exhaustive

## Common Mistakes
- Too many thin slices making the chart illegible (smell J — silently dropped categories when grouping)
- Slices that overlap in meaning or are not mutually exclusive (smell I)
- Using 3-D perspective which distorts relative areas
- Comparing two pie charts side-by-side instead of using a grouped bar


## Dashboard and other surfaces

status: placeholder

`Pie Chart` is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with stacked-bar-100pct, donut-chart, waffle-chart. `ibcs_status: avoid` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Vault coarse type, when a scraped template is the layout: **Donut**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
```

### plotly
`go.Pie(labels=labels, values=values, hole=0)` — set `sort=False` to preserve explicit order.

### altair
`mark_arc()` with `theta=alt.Theta('value:Q')` and `color=alt.Color('category:N')`.

### excel / tableau
**Excel**: Insert → Charts → Pie. **Tableau**: Marks card → Pie; drag measure to Angle, dimension to Color.

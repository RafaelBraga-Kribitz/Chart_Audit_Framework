---
name: Donut Chart
category: Composition
input_type: [composition]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Polygon]
cardinality_fit: [small-N]
audience: [Executive, Public]
complexity: Basic
encoding_channels: [angle, area, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [I, J]
alternatives: [pie-chart, stacked-bar-100pct, waffle-chart]
source: [datavizproject, datavizcatalogue]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---
# Donut Chart

## Description
A Donut Chart is a Pie Chart with the centre removed, shifting the reader's focus from area comparison to arc-length comparison. The hollow centre is a design feature that can display a summary statistic or label. Because area is de-emphasised, viewers more naturally compare the relative lengths of arcs, which is a slightly more accurate perceptual task than comparing wedge areas.

## When to Use
- Same part-to-whole use cases as a Pie Chart, but when centre space is available for a KPI or total label
- Dashboards where a compact, visually distinct component is needed
- When branding/design guidelines prefer the ring aesthetic

## When NOT to Use
- More than 6 categories
- When precise per-segment values must be read off the chart
- Data categories are not mutually exclusive (smell I)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | Each unique value becomes one arc segment |
| value | numeric (≥0) | Proportional arc length |

## Best Practices
- Keep the hole ratio between 40–60% of the outer radius for readability
- Place the most important or largest slice starting at 12 o'clock
- Use centre text for a single summary number (total, selected segment %)
- Direct-label each segment; minimise legend use
- Limit palette to the number of segments — never exceed 7 colors

## Common Mistakes
- Using a donut where a single-number KPI tile would be clearer
- Overlapping labels when many thin slices are present (smell J)
- Non-exclusive categories creating misleading totals (smell I)
- Nesting two unrelated datasets in concentric rings without clear hierarchy

## Implementation Notes

### matplotlib
```python
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.0f%%',
                                   wedgeprops=dict(width=0.5), startangle=90)
ax.axis('equal')
```

### plotly
`go.Pie(labels=labels, values=values, hole=0.45)` — `hole` parameter controls donut width.

### altair
`mark_arc(innerRadius=60)` with `theta=alt.Theta('value:Q')` and `color=alt.Color('category:N')`.

### excel / tableau
**Excel**: Insert → Doughnut Chart. **Tableau**: Pie chart with a reduced mark size to create donut effect, or use a dual-axis trick.

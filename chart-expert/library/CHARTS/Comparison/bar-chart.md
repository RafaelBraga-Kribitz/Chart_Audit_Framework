---
name: Bar Chart
category: Comparison
input_type: [cat-value, cat-multi-value]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Technical, Public]
complexity: Basic
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [D, J]
alternatives: [horizontal-bar-chart, lollipop-chart, dot-plot, column-range]
source: [datavizproject, datavizcatalogue]
implementations:
  matplotlib: {status: verified, source_file: "chart-expert/library/_SNIPPETS/bar-chart_matplotlib.py", last_iterated: 2026-07-09}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---

# Bar Chart

## Description
A bar chart (vertical orientation, also called a column chart) represents categorical data with rectangular bars whose heights are proportional to the values they represent. Each bar corresponds to a category on the x-axis, and the y-axis encodes the quantitative value. It is the most fundamental and widely understood chart type for comparing discrete quantities across categories.

## When to Use
- Comparing a single quantitative value across a set of discrete categories
- Showing rankings or relative magnitudes when time is not the primary axis
- Displaying counts, totals, or averages for a categorical breakdown
- When the audience needs to precisely compare values using bar length

## When NOT to Use
- Category labels are long (use a horizontal bar chart to give labels space)
- More than ~15–20 categories (bars become too narrow; consider a dot plot or table)
- The variable on y-axis is continuous and ordered (use a histogram or line chart)
- Part-to-whole is the message (use a stacked or 100% bar chart)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | The groups being compared; x-axis |
| value | numeric | The measured quantity; y-axis |
| color_group (optional) | categorical | Only use if a secondary grouping is needed |

## Best Practices
- Always start the y-axis at zero — truncation makes length comparisons misleading
- Sort bars by value (descending or ascending) unless category order is intrinsically meaningful — see Smell D
- Use a single consistent color unless color encodes a meaningful distinction
- Add value labels directly on or above bars for precise reading
- Limit to ~12 bars before switching to horizontal orientation or a table

## Common Mistakes
- Not starting the y-axis at zero, exaggerating apparent differences
- Leaving bars in arbitrary/alphabetical order instead of sorting by value — see Smell D
- Silently omitting categories with zero or near-zero values — see Smell J
- Using 3D bars, which distort length perception

## Implementation Notes

### matplotlib

Verified 2026-07-09 — runnable snippet:
`chart-expert/library/_SNIPPETS/bar-chart_matplotlib.py` (inline fixture,
zero baseline, value-sorted categories, direct bar labels via `ax.bar_label`,
top/right spines hidden, Agg backend, non-empty PNG asserted). Core pattern:

```python
bars = ax.bar(cats_sorted, vals_sorted, color="#4477AA")
ax.bar_label(bars, padding=2)      # direct labels beat a legend for one series
ax.set_ylim(0, max(vals_sorted) * 1.15)  # zero baseline
ax.spines[["top", "right"]].set_visible(False)
```

### plotly
`px.bar(df, x='category', y='value', color='color_group')` or `go.Bar`.

### altair
`alt.Chart(df).mark_bar().encode(x=alt.X('category:N', sort='-y'), y='value:Q')`

### excel / tableau
Excel: Insert > Column Chart. Tableau: Drag measure to Rows, dimension to Columns; Marks card = Bar.

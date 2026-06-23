---
name: Horizontal Bar Chart
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
alternatives: [bar-chart, lollipop-chart, dot-plot, bullet-graph]
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

# Horizontal Bar Chart

## Description
A horizontal bar chart is a bar chart rotated 90 degrees so that categories are listed on the y-axis and bar lengths extend horizontally along the x-axis. This orientation is preferred when category labels are long, when there are many categories, or when a natural reading order (top-to-bottom) is desired. It is functionally identical to a vertical bar chart but better suited for label-heavy categorical data.

## When to Use
- Category labels are long words or phrases that would crowd a vertical x-axis
- More than ~8–10 categories where a vertical chart becomes cramped
- Ranking contexts where top-to-bottom order is intuitive (rank 1 at top)
- Survey results, demographic breakdowns, feature comparison lists

## When NOT to Use
- Time is the x-axis variable (horizontal time charts feel unnatural — use a vertical bar or line)
- Few categories with short labels (a vertical bar chart is more conventional)
- Part-to-whole relationships (use a stacked bar chart)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | The groups being compared; y-axis |
| value | numeric | The measured quantity; x-axis (must start at 0) |
| color_group (optional) | categorical | Secondary grouping for color encoding |

## Best Practices
- Sort bars by value (largest at top) unless natural order exists — see Smell D
- Always start the x-axis at zero
- Use direct labels at the end of each bar for precise reading
- Leave adequate whitespace between bars (bar gap ~25–50% of bar height)
- Use a single color unless a second categorical dimension needs encoding

## Common Mistakes
- Leaving categories in alphabetical or arbitrary order — see Smell D
- Starting the x-axis at a non-zero value, making bar lengths misleading
- Silently dropping zero-value categories — see Smell J
- Using too many colors for a single-series comparison, adding visual noise

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
df_sorted = df.sort_values('value', ascending=True)
fig, ax = plt.subplots()
ax.barh(df_sorted['category'], df_sorted['value'],
        color='steelblue', edgecolor='white')
ax.set_xlim(0)
plt.tight_layout()
```

### plotly
`px.bar(df, x='value', y='category', orientation='h')` with `category_orders`.

### altair
`alt.Chart(df).mark_bar().encode(y=alt.Y('category:N', sort='-x'), x='value:Q')`

### excel / tableau
Excel: Insert > Bar Chart (horizontal in Excel terminology). Tableau: Swap Rows/Columns from a standard bar chart.

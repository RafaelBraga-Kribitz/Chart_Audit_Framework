---
name: Stacked Bar Chart
category: Comparison
input_type: [composition, cat-multi-value]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Public]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [I, J, D]
alternatives: [grouped-bar-chart, stacked-area-chart, waffle-chart, pie-chart]
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

# Stacked Bar Chart

## Description
A stacked bar chart divides each bar into segments representing sub-categories, stacked vertically (or horizontally) so the total bar height represents the sum of all parts. It allows viewers to see both individual category totals and the contribution of each sub-category to that total simultaneously. A 100% stacked variant normalizes all bars to the same total height, showing proportions only.

## When to Use
- Showing how a total breaks down into additive parts across multiple categories
- Comparing both totals and composition simultaneously
- 100% stacked variant: when relative proportions across categories matter more than absolute totals
- A small number of clearly distinct sub-categories (3–5) that together form a logical whole

## When NOT to Use
- Sub-categories are not mutually exclusive additive parts — see Smell I
- Precise comparison of non-baseline segments is needed (their floating baseline makes comparison difficult)
- More than 5–6 sub-categories (too many colors; consider a grouped bar or small multiples)
- Individual sub-category trends over time are equally important as totals (use small multiples)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | Primary grouping on x-axis |
| sub_category | categorical | The stacking dimension; must be mutually exclusive |
| value | numeric | Non-negative; represents an additive part |

## Best Practices
- Place the most important or most stable sub-category at the bottom of each bar
- Use consistent colors across all stacked bars for the same sub-category
- For 100% stacked charts, label percentages directly within segments when space allows
- Avoid stacking more than 5 segments per bar
- Sort primary categories by total bar height unless a natural order exists

## Common Mistakes
- Stacking non-additive categories (e.g., overlapping user segments) — see Smell I
- Silently dropping small sub-categories without rolling into an "Other" category — see Smell J
- Using arbitrary primary category ordering instead of sorting by total — see Smell D
- Using too many sub-category colors, exceeding a readable palette

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
bottom = np.zeros(len(categories))
for sub, values, color in zip(sub_cats, values_matrix, colors):
    ax.bar(categories, values, bottom=bottom, label=sub, color=color)
    bottom += values
ax.legend()
plt.tight_layout()
```

### plotly
`px.bar(df, x='category', y='value', color='sub_category', barmode='stack')`

### altair
`alt.Chart(df).mark_bar().encode(x='category:N', y=alt.Y('value:Q', stack='zero'), color='sub_category:N')`

### excel / tableau
Excel: Insert > Stacked Column Chart. Tableau: Drag sub_category to Color and set Marks to Bar; stacking is automatic.

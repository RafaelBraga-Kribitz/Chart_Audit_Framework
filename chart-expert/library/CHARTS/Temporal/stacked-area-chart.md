---
name: Stacked Area Chart
category: Temporal
input_type: [time-series, composition]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Area]
cardinality_fit: [medium, large]
audience: [Analytics, Executive]
complexity: Intermediate
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [I, J, L]
alternatives: [area-chart, stream-graph, stacked-bar-chart, line-chart]
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

# Stacked Area Chart

## Description
A stacked area chart layers multiple area series on top of one another so that each series starts where the previous one ends. The total height at any x-position represents the sum of all series at that point. It combines a part-to-whole view with temporal trend, showing how category contributions change over time.

## When to Use
- Showing how sub-category contributions build to a total over time
- Tracking both individual category trends and the overall total simultaneously
- When series values are additive and mutually exclusive (e.g., revenue by product line)
- 3–7 categories that collectively form a meaningful whole

## When NOT to Use
- Series are not mutually exclusive additive parts of a whole — see Smell I
- Individual category trends are the primary story (use a multi-line chart instead)
- More than 7 categories (color differentiation breaks down)
- When precise comparison of non-baseline series is critical (their baseline shifts)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date or ordered numeric | Must be sorted ascending |
| value | numeric | Non-negative; represents part of a whole |
| category | categorical | The stacking dimension; mutually exclusive |

## Best Practices
- Order categories by stability: put the most stable series at the bottom baseline
- Normalize to 100% when relative composition matters more than absolute totals
- Limit to 5–7 categories with distinct, accessible colors
- Add a total line if the aggregate trend is equally important
- Consider small multiples if individual trends are obscured by stacking

## Common Mistakes
- Stacking non-additive series (e.g., overlapping customer segments) — see Smell I
- Silently dropping small categories into an "Other" bucket without labeling it — see Smell J
- Interpolating smoothly over gaps, implying continuous data — see Smell L
- Inferring trends for middle series whose visual baseline constantly shifts

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.stackplot(df['date'], [df[c] for c in categories],
             labels=categories, alpha=0.8)
ax.legend(loc='upper left')
ax.set_ylim(0)
plt.tight_layout()
```

### plotly
`px.area(df, x='date', y='value', color='category')` — plotly stacks by default.

### altair
`alt.Chart(df).mark_area().encode(x='date:T', y=alt.Y('value:Q', stack='zero'), color='category:N')`

### excel / tableau
Excel: Insert > Stacked Area. Tableau: Marks card to Area; drag category to Color, date to Columns, measure to Rows.

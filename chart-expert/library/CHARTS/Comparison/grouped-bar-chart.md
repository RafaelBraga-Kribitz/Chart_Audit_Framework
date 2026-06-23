---
name: Grouped Bar Chart
category: Comparison
input_type: [demo-grouped, cat-multi-value]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive, Technical]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [D, J]
alternatives: [stacked-bar-chart, faceted-bar-chart, radar-chart, dot-plot]
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

# Grouped Bar Chart

## Description
A grouped bar chart (also called a clustered bar chart) places bars for multiple sub-categories side by side within each primary category group. It allows simultaneous comparison of values both within a group (across sub-categories) and across groups for the same sub-category. The primary x-axis encodes the main category, grouped bars are color-coded by sub-category, and bar height encodes the value.

## When to Use
- Comparing multiple metrics or sub-groups across the same set of primary categories
- Survey data with multiple response groups (e.g., age groups) across multiple questions
- Before/after comparisons across several categories simultaneously
- When both within-group and across-group comparisons are important

## When NOT to Use
- More than 3–4 sub-groups per cluster (bars become too narrow; use small multiples instead)
- The goal is to see the total across sub-groups (use a stacked bar chart)
- Categories are too many (>8) to display cleanly as grouped clusters
- Time is the primary axis with many periods (use a line chart per group)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| primary_category | categorical | Main grouping on x-axis |
| sub_category | categorical | The within-group dimension; encoded by color |
| value | numeric | The measured quantity; y-axis |

## Best Practices
- Limit to 2–4 sub-groups within each cluster to maintain bar legibility
- Use a consistent, distinct color for each sub-category across all groups
- Sort primary categories by a meaningful criterion (e.g., by total, by main sub-group)
- Include a clear legend identifying sub-category colors
- Consider small multiples if comparing many sub-groups is equally important

## Common Mistakes
- Using too many sub-groups per cluster, making bars too thin to read — see Smell D
- Silently omitting sub-groups that have zero or missing values — see Smell J
- Using arbitrary category order instead of sorting by a meaningful criterion — see Smell D
- Making the chart too wide by including too many primary categories

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(len(categories))
width = 0.35
fig, ax = plt.subplots()
ax.bar(x - width/2, values_a, width, label='Group A', color='steelblue')
ax.bar(x + width/2, values_b, width, label='Group B', color='coral')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
plt.tight_layout()
```

### plotly
`px.bar(df, x='primary_category', y='value', color='sub_category', barmode='group')`

### altair
`alt.Chart(df).mark_bar().encode(x='primary_category:N', y='value:Q', color='sub_category:N', xOffset='sub_category:N')`

### excel / tableau
Excel: Insert > Clustered Column Chart. Tableau: Drag sub_category to Color; set Marks to Bar.

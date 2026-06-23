---
name: Dot Plot
category: Comparison
input_type: [cat-value, cat-multi-value]
it_variants: []
analytical_function: Comparison
visual_family: Plot
shape_primitive: [Dot]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [D, G]
alternatives: [lollipop-chart, bar-chart, dumbbell-plot, scatter-plot]
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---

# Dot Plot

## Description
A dot plot (Cleveland dot plot) uses a single dot per category to encode a quantitative value on a common scale, with categories listed along one axis and values along the other. Unlike a bar chart, a dot plot removes the bar fill, reducing visual weight and making it easier to compare values precisely using position rather than length. It is especially effective when the exact values, not the bar magnitudes, are the point.

## When to Use
- Comparing values across many categories where bar clutter would be excessive
- When precise positional reading is more important than the bar-length metaphor
- Survey ratings, test scores, or performance metrics across categories
- As a cleaner replacement for bar charts in academic or analytical publications

## When NOT to Use
- Zero-baseline comparison of magnitudes is the goal (bar charts communicate "how much" more naturally)
- Data has a natural stacked or part-to-whole structure
- Continuous distributions need to be shown (use a strip plot or jitter plot)
- The audience expects bars and may not intuitively read a dot plot

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | The items being compared |
| value | numeric | The measured quantity encoded as dot position |
| group (optional) | categorical | For overlaying multiple dot series per category |

## Best Practices
- Sort categories by value for easy ranking — see Smell D
- Add reference lines (grid lines or a vertical zero line) to aid positional reading
- Use a consistent dot size and color unless encoding a secondary dimension
- For multiple groups, use distinct colors and position dots horizontally adjacent per category
- Avoid adding fills or bars behind the dots — the minimalism is the point

## Common Mistakes
- Not sorting categories by value, making the chart hard to read — see Smell D
- Using KDE or smoothing where individual values should be shown as discrete dots — see Smell G
- Using dot plots for data with heavy overlap that requires jitter (use a jitter/strip plot instead)
- Confusing a dot plot (one dot per category) with a scatter plot (two continuous variables)

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
df_sorted = df.sort_values('value')
fig, ax = plt.subplots()
ax.scatter(df_sorted['value'], df_sorted['category'],
           color='steelblue', s=60, zorder=5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.grid(axis='x', linestyle='--', alpha=0.4)
plt.tight_layout()
```

### plotly
`px.scatter(df, x='value', y='category', color='group')` with `category_orders` to control y-axis sort.

### altair
`alt.Chart(df).mark_point(filled=True).encode(x='value:Q', y=alt.Y('category:N', sort='-x'), color='group:N')`

### excel / tableau
Tableau: Scatter plot with category on y-axis and value on x-axis, one mark per category row. Excel: Scatter chart with category labels as y-axis text.

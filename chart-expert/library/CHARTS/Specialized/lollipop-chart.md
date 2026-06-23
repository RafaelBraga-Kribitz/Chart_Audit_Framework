---
name: Lollipop Chart
category: Specialized
input_type: [cat-value, cat-multi-value]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Line, Circle]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive]
complexity: Basic
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [J]
alternatives: [bar-chart, dumbbell-plot, dot-plot]
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
# Lollipop Chart

## Description
A Lollipop Chart is a minimalist alternative to a Bar Chart, replacing the solid bar with a thin line (stem) terminating in a circle (dot). It encodes the same information as a bar chart (the length from baseline to dot value) but with less visual ink, reducing chart junk. The result is cleaner and more readable, particularly when comparing many items or when small differences between values need to be seen without the visual bulk of full bars.

## When to Use
- Ranking or comparing values across many categories where bar chart bulk would feel heavy
- When the chart already contains much visual information and minimalism is desirable
- Design-conscious reports and presentations where clean aesthetics matter

## When NOT to Use
- When the baseline (zero) must be visually emphasised to prevent misreading (bars are more anchoring)
- Very few categories where a bar chart's simplicity is preferable
- Data with uncertainty where error bars or confidence intervals are needed (use a bar or dumbbell)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | One lollipop per category |
| value | numeric | Determines the length of the stem |
| group | categorical (optional) | Colour grouping |

## Best Practices
- Always include a visible baseline at zero
- Sort by descending value for ranking-style comparisons
- Use colour to highlight specific categories (e.g., above/below average)
- Keep dot size consistent within a chart; avoid enlarging dots beyond 6–8px at standard size

## Common Mistakes
- Omitting the zero baseline, making relative lengths misleading
- Silently dropping categories with zero or null values (smell J)
- Inconsistent dot sizes creating the impression that dot area encodes a second variable
- Overloading with many colour groups making the chart a rainbow

## Implementation Notes

### matplotlib
```python
ax.vlines(categories, 0, values, color='grey', linewidth=1.5)
ax.scatter(categories, values, s=60, color='steelblue', zorder=5)
ax.axhline(0, color='black', linewidth=0.8)
```

### plotly
`go.Scatter(x=categories, y=values, mode='markers') + go.Bar(x=categories, y=values, width=0.02)` or use `error_y` with zero errors as a workaround for stems.

### altair
`mark_rule(strokeWidth=1.5)` with `y='value:Q'` and `y2=alt.value(0)` layered with `mark_circle(size=60)`.

### excel / tableau
**Tableau**: Dual-axis with Bar (thin width) + Circle. **Excel**: Line chart with markers, set line colour to grey and markers to filled circles.

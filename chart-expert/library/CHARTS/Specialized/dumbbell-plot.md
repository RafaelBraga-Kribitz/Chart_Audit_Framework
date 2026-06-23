---
name: Dumbbell Plot
category: Specialized
input_type: [cat-multi-value, interval-range]
it_variants: []
analytical_function: Comparison
visual_family: Plot
shape_primitive: [Line, Circle]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive]
complexity: Basic
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [J]
alternatives: [lollipop-chart, slope-chart, bar-chart]
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
# Dumbbell Plot

## Description
Also known as a DNA Chart, Connected Dot Plot, or Gap Chart. A Dumbbell Plot shows the range or difference between two values for each category. Each category has two dots (one for each value) connected by a horizontal or vertical line. The line's length encodes the magnitude of the gap or change, while the dots are positioned on the value axis. It is excellent for showing before/after comparisons, disparities between two groups, or confidence intervals.

## When to Use
- Before-and-after comparisons (e.g., performance before/after an intervention)
- Showing disparity or gap between two groups across many categories
- Communicating change direction and magnitude simultaneously for a list of items
- Replacing paired bar charts where the gap size is more important than the absolute values

## When NOT to Use
- More than 2 comparison points per category (use a slope chart or line chart instead)
- When absolute values matter as much as the gap (a grouped bar chart is clearer)
- Very large numbers of categories without sorting by gap size

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | One dumbbell per row |
| value_a | numeric | Left/lower dot value |
| value_b | numeric | Right/upper dot value |
| label_a | string | Legend label for group A |
| label_b | string | Legend label for group B |

## Best Practices
- Sort rows by the size of the gap (largest to smallest) for ranking insight
- Use contrasting colours for the two dots; the connecting line should be neutral
- Annotate the gap magnitude on or near the connecting line for the most important items
- Include a legend clearly identifying which dot is which group

## Common Mistakes
- Unordered rows making it impossible to see which categories have the largest gaps
- Silently dropping categories where one value is missing (smell J)
- Using dumbbells for more than 2 comparison points (visual clutter)
- Equal dot sizes when one group is more uncertain or approximate

## Implementation Notes

### matplotlib
```python
for i, row in df.iterrows():
    ax.plot([row.value_a, row.value_b], [i, i], 'grey', linewidth=1.5)
    ax.scatter(row.value_a, i, color='steelblue', s=80, zorder=5)
    ax.scatter(row.value_b, i, color='coral', s=80, zorder=5)
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df.category)
```

### plotly
`go.Scatter(x=[val_a, val_b], y=[cat, cat], mode='lines+markers')` per row.

### altair
`mark_rule()` with `x='value_a:Q'`, `x2='value_b:Q'` layered with `mark_circle()` for each endpoint.

### excel / tableau
**Tableau**: Dual-axis with two circle marks and a line mark connecting them. **Excel**: Line chart with markers, limited control.

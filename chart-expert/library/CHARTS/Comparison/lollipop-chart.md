---
name: Lollipop Chart
category: Comparison
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
failure_modes: [D, J]
alternatives: [bar-chart, dot-plot, dumbbell-plot]
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
A lollipop chart is a minimalist alternative to a bar chart that replaces each bar with a thin line (stem) topped by a circle (the "lollipop" head). The head position encodes the value, and the stem connects the value to the baseline. This reduces visual ink, avoids bar clutter when many categories are present, and shifts focus to the data points rather than the bar fills.

## When to Use
- As a cleaner alternative to a bar chart when many categories need to be shown
- When reducing visual ink is a priority and bar width adds no information
- Communicating ranked values where the relative position matters more than bar area
- When two series need to be overlaid (use a dumbbell lollipop variant)

## When NOT to Use
- The audience expects conventional bars and may not immediately recognize lollipops
- Very precise value reading is needed and the small dot is harder to read than a bar edge
- Part-to-whole relationships are the message (use a stacked bar)
- Very short values where the stem is nearly invisible and only the dot appears

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | The groups being compared |
| value | numeric | The measured quantity; must be non-negative for upward stems |

## Best Practices
- Sort categories by value (descending) for ranking readability — see Smell D
- Use a y-axis starting at zero to make stem lengths meaningful
- Keep the dot size consistent and large enough to be clearly visible
- Use a thin, low-contrast stem color and a high-contrast dot color for visual hierarchy
- Add value labels near the dots when precise reading is needed

## Common Mistakes
- Leaving categories in arbitrary order — see Smell D
- Using lollipops without a zero baseline, making stem lengths meaningless
- Silently dropping zero-value categories — see Smell J
- Using lollipops for very small values where the stem is nearly invisible

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.vlines(df['category'], 0, df['value'], color='gray', linewidth=1)
ax.plot(df['category'], df['value'], 'o', color='steelblue', markersize=8)
ax.set_ylim(0)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
```

### plotly
Combine `go.Scatter(mode='markers')` with `go.Bar(width=0.02)` as thin bars, or use the error bar trick for stems.

### altair
Layer a `mark_rule` (from y=0 to y=value) with a `mark_point` at each value position.

### excel / tableau
Tableau: Dual-axis combining a thin bar (for stem) and a circle mark (for head). Excel: Scatter chart overlaid with a line chart using zero-value baseline.

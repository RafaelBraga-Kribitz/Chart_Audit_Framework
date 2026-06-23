---
name: 100% Stacked Bar Chart
category: Composition
input_type: [cat-multi-value, composition]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics]
complexity: Basic
encoding_channels: [length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [I, J]
alternatives: [pie-chart, stacked-area-100pct, marimekko-chart]
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
# 100% Stacked Bar Chart

## Description
A 100% Stacked Bar Chart normalises each bar to 100%, showing the proportional composition of each category group as coloured segments. Unlike a regular stacked bar, it sacrifices absolute magnitude information to emphasise relative shares. It is the rectangular equivalent of a Pie Chart, allowing side-by-side composition comparison across multiple groups — a task at which the pie chart fails.

## When to Use
- Comparing the proportional composition of multiple groups side-by-side
- When absolute totals are unimportant and only the relative mix matters
- Survey data showing response distribution (Strongly Agree/Agree/Neutral/Disagree/Strongly Disagree) across groups

## When NOT to Use
- When absolute values matter alongside proportions (use a regular stacked bar)
- More than 6–7 segments per bar (inner segments become unreadable without a common baseline)
- Showing change in composition over time with a continuous axis (use 100% Stacked Area instead)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| group | categorical | Identifies each bar (x-axis) |
| segment | categorical | Sub-category within each bar |
| value | numeric (≥0) | Raw count or value; library normalises to 100% |

## Best Practices
- Place the most important or most variable segment adjacent to a baseline (first or last)
- Annotate the percentage inside each segment when segments are wide enough
- Use a consistent colour palette across all bars — the same segment always the same colour
- Consider diverging layout for Likert scales (neutral at centre)

## Common Mistakes
- Segments that are not mutually exclusive, inflating totals (smell I)
- Silently dropping a small segment that rounds to 0% (smell J)
- Comparing inner segment sizes across bars — only the first and last segments share a common baseline
- Using too many colours making the legend unreadable

## Implementation Notes

### matplotlib
```python
bottom = np.zeros(n_groups)
for seg, color in zip(segments, colors):
    vals = data[seg] / data[segments].sum(axis=1) * 100
    ax.bar(groups, vals, bottom=bottom, color=color, label=seg)
    bottom += vals
```

### plotly
`go.Bar` with `barmode='relative'` and `barnorm='percent'`.

### altair
`mark_bar()` with `stack='normalize'` on the y encoding and `color=alt.Color('segment:N')`.

### excel / tableau
**Excel**: Select data → Insert → Bar Chart → 100% Stacked Bar. **Tableau**: Drag dimension to Color, select "Stack Marks" → 100%.

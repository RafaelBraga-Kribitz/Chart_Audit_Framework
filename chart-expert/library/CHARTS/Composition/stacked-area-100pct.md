---
name: 100% Stacked Area Chart
category: Composition
input_type: [time-series, cat-multi-value]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Area]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive]
complexity: Basic
encoding_channels: [position, area, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [I, J]
alternatives: [stacked-bar-100pct, stream-graph]
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
# 100% Stacked Area Chart

## Description
A 100% Stacked Area Chart normalises all values at each time point to 100%, showing the proportional composition of a total as it evolves over time. Each coloured band represents one category's share, and all bands together always fill the full chart height. It is the temporal equivalent of a 100% Stacked Bar Chart, trading the ability to read absolute magnitudes for a clear view of compositional shift over time.

## When to Use
- Showing how the proportional mix of categories changes over time
- Market share evolution, budget allocation shifts, demographic composition over years
- When the absolute total is less important than the relative share trends

## When NOT to Use
- When absolute values matter — the normalisation hides growth or decline in totals
- Categories with many crossing trends (a line chart per category is clearer)
- More than 6–7 categories (inner bands lack common baselines for comparison)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| time | temporal / numeric | X-axis time dimension |
| category | categorical | One area band per category |
| value | numeric (≥0) | Raw value; normalised to % of total at each time point |

## Best Practices
- Place the most stable or largest category at the bottom for a reliable baseline reference
- Annotate the first and last data points with percentage labels
- Use a consistent colour palette — the same category always the same colour
- Consider a small-multiple approach if individual category trends need inspection

## Common Mistakes
- Segments not mutually exclusive, inflating totals at each time point (smell I)
- Silently dropping a category that temporarily reaches zero (smell J)
- Audiences misreading rising bands as growth (the total is always 100%)
- Too many categories creating a rainbow of thin unreadable bands

## Implementation Notes

### matplotlib
```python
ax.stackplot(time, *[data[cat] for cat in categories],
             labels=categories, colors=palette)
# Normalise first: data_pct = data.div(data.sum(axis=1), axis=0) * 100
```

### plotly
`go.Scatter` traces with `stackgroup='one'` and `groupnorm='percent'`.

### altair
`mark_area()` with `stack='normalize'` on y encoding and `color=alt.Color('category:N')`.

### excel / tableau
**Excel**: Insert → Area Chart → 100% Stacked Area. **Tableau**: Area chart with "Stack Marks" set to 100%.

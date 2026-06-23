---
name: Bump Chart
category: Specialized
input_type: [time-series, cat-multi-value]
it_variants: []
analytical_function: Ranking
visual_family: Chart
shape_primitive: [Line, Circle]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [J]
alternatives: [slope-chart, line-chart]
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
# Bump Chart

## Description
A Bump Chart shows how rankings change over time across multiple categories. The y-axis is the rank (1 = top), the x-axis is time (discrete periods), and each category is a coloured line connecting its rank positions. Lines cross when rankings change, making it immediately clear which entities are rising, falling, or stable. It focuses purely on ordinal position rather than the underlying metric values.

## When to Use
- Tracking how entities move up or down in a ranking over several time periods
- Sports league standings, music chart rankings, product sales rank, market share rank over time
- When the competitive dynamics (overtaking events) are the primary story

## When NOT to Use
- When the absolute metric values matter as much as the rank (use a line chart)
- Continuous time series (ranks measured at more than 10–15 discrete intervals become cluttered)
- Only 2 time periods (use a Slope Chart instead)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| entity | categorical | Each line is one entity |
| period | categorical / temporal | Discrete time periods on x-axis |
| rank | integer (≥1) | Ranking at this period; 1 = highest |

## Best Practices
- Invert the y-axis (rank 1 at the top)
- Use a sigmoid/spline interpolation between periods rather than straight line segments
- Label entities at start and end of chart; avoid mid-chart labels
- Colour-code entities with a distinct, accessible palette (limit to ≤10 entities)
- Highlight specific entities of interest with prominent colours; grey the rest

## Common Mistakes
- Too many lines (>10 entities) creating an indistinguishable tangle
- Not inverting the y-axis, making "higher rank number = better" confusing
- Including entities with many missing periods, creating broken lines (smell J)
- Using a line chart (with metric values) when only rank is meaningful

## Implementation Notes

### matplotlib
```python
for entity, group in df.groupby('entity'):
    ax.plot(group.period, group.rank, 'o-', label=entity, linewidth=2)
ax.invert_yaxis()
ax.set_xlabel('Period')
ax.set_ylabel('Rank')
```

### plotly
`go.Scatter(x=periods, y=ranks, mode='lines+markers', name=entity)` per entity; `yaxis=dict(autorange='reversed')`.

### altair
`mark_line()` + `mark_point()` with `y=alt.Y('rank:O', scale=alt.Scale(reverse=True))`.

### excel / tableau
**Tableau**: Line chart with rank on a reversed y-axis. **Excel**: Line chart with y-axis manually reversed.

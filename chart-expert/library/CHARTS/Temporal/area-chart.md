---
name: Area Chart
category: Temporal
input_type: [time-series, xy-simple]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Area, Line]
cardinality_fit: [medium, large]
audience: [Executive, Analytics, Public]
complexity: Basic
encoding_channels: [position, color-hue, color-value]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [L, B, I]
alternatives: [line-chart, stacked-area-chart, sparkline]
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

# Area Chart

## Description
An area chart is a line chart where the region between the line and the x-axis is filled with color. This fill emphasizes the magnitude of the quantity and the cumulative volume of change over time. It is most appropriate for a single series or a small number of transparent overlapping series.

## When to Use
- Emphasizing the total volume of a single metric over time
- Showing accumulated quantity (e.g., cumulative downloads, running totals)
- Comparing two overlapping series where the overlap region is meaningful
- When fill area provides meaningful visual weight to the trend

## When NOT to Use
- More than 3 overlapping series (fills obscure each other — use small multiples or a line chart)
- When precise individual values matter more than overall shape
- For part-to-whole breakdowns (use stacked area chart instead)
- Nominal or unordered x-axis categories

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date or ordered numeric | Must be sorted ascending |
| value | numeric | Should be non-negative for fill to read correctly |
| series (optional) | categorical | Limit to 2-3 for overlay; use transparency |

## Best Practices
- Fill color should have reduced opacity (0.3–0.6) when overlapping series are shown
- Always baseline at zero; a non-zero baseline makes fill area misleading
- Use a solid stroke line on top of the fill to make exact values readable
- For two series, place the larger one behind the smaller to avoid occlusion

## Common Mistakes
- Stacking series that are not additive components of a whole — see Smell I
- Filling above a non-zero baseline, making area proportions meaningless
- Using area fills so opaque that overlapping series disappear — see Smell L
- Treating the visual volume as proportional when the y-axis is truncated

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.fill_between(df['date'], df['value'], alpha=0.4, color='steelblue')
ax.plot(df['date'], df['value'], color='steelblue', linewidth=1.5)
ax.set_ylim(0)
plt.tight_layout()
```

### plotly
`px.area(df, x='date', y='value')` or `go.Scatter(fill='tozeroy', mode='lines')`.

### altair
`alt.Chart(df).mark_area(opacity=0.4).encode(x='date:T', y='value:Q')`

### excel / tableau
Excel: Insert > Area Chart. Tableau: Marks card set to Area; drag measure to Rows and date to Columns.

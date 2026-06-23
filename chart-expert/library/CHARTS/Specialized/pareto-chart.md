---
name: Pareto Chart
category: Specialized
input_type: [cat-value]
it_variants: []
analytical_function: Ranking
visual_family: Chart
shape_primitive: [Bar, Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive]
complexity: Basic
encoding_channels: [length, position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [J]
alternatives: [bar-chart, lollipop-chart, funnel-chart]
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
# Pareto Chart

## Description
A Pareto Chart combines a sorted bar chart (categories ordered from highest to lowest frequency or impact) with a cumulative percentage line overlaid on a secondary y-axis. It is used to identify the "vital few" from the "trivial many" in accordance with the Pareto Principle (80/20 rule). The cumulative line makes it easy to identify the point at which, say, 80% of the total effect is explained by the first N categories. It is a core tool in quality control (Six Sigma, ISO standards).

## When to Use
- Identifying which causes, defects, or issues account for the majority of a problem
- Quality improvement: fault types, customer complaints, error categories
- Prioritising interventions where effort should target highest-impact categories

## When NOT to Use
- Data without a natural count or frequency structure
- All categories contribute roughly equally (the Pareto insight doesn't apply)
- When temporal trend matters more than the ranking

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | Defect type, cause, or issue |
| count | numeric (≥0) | Frequency or impact score |

Cumulative percentage is computed: `cumsum(sorted_count) / total * 100`.

## Best Practices
- Sort bars strictly descending by count
- Draw the cumulative line from the top-right corner of the first bar
- Mark the 80% threshold on the cumulative line axis
- Label the number of categories at the 80% cutoff directly on the chart

## Common Mistakes
- Not sorting bars in descending order (defeats the Pareto analysis)
- Silently dropping low-frequency categories without aggregating into "Other" (smell J)
- Dual y-axis scaling that misaligns bars and cumulative line at the 100% endpoint
- Treating the 80/20 threshold as a strict rule rather than a guide

## Implementation Notes

### matplotlib
```python
df = df.sort_values('count', ascending=False)
df['cumulative'] = df['count'].cumsum() / df['count'].sum() * 100
ax1.bar(df.category, df['count'], color='steelblue')
ax2 = ax1.twinx()
ax2.plot(df.category, df.cumulative, 'ro-', linewidth=2)
ax2.axhline(80, color='grey', linestyle='--')
ax2.set_ylim(0, 110)
```

### plotly
`go.Bar` for sorted counts + `go.Scatter` for cumulative line on secondary y-axis via `secondary_y=True`.

### altair
Dual-layer: `mark_bar()` for counts + `mark_line()` for cumulative percentage, with secondary y-axis via `resolve_scale`.

### excel / tableau
**Excel**: Insert → Pareto Chart (Excel 2016+, built-in). **Tableau**: Dual-axis with bar and line; compute cumulative % as a table calculation.

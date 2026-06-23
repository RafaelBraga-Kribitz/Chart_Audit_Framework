---
name: Funnel Chart
category: Composition
input_type: [cat-value]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Polygon, Bar]
cardinality_fit: [small-N]
audience: [Executive, Analytics]
complexity: Basic
encoding_channels: [length, area, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [I, J]
alternatives: [pyramid-chart, stacked-bar-100pct, pareto-chart]
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
# Funnel Chart

## Description
A Funnel Chart represents a sequential process where a quantity decreases from one stage to the next, visualised as a series of progressively narrowing horizontal bars or trapezoids. The classic use case is a sales or conversion funnel (Awareness → Interest → Consideration → Purchase). Each stage's width or area is proportional to the number of items remaining in the process, making drop-off rates visually apparent.

## When to Use
- Showing attrition across a linear process pipeline (sales, marketing, onboarding)
- Highlighting which stages have the highest drop-off rates
- Communicating conversion rates to executive or business audiences

## When NOT to Use
- Stages are not sequential or have feedback loops
- Data does not decrease monotonically (use a bar chart instead)
- Precise stage-to-stage comparison is more important than overall funnel shape

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| stage | categorical (ordered) | Each stage in the process, top to bottom |
| value | numeric (≥0) | Count or volume at each stage; must be non-increasing ideally |
| conversion_rate | numeric (optional) | Stage-to-stage rate for annotation |

## Best Practices
- Annotate each stage with absolute value and conversion rate from the previous stage
- Use a single colour with varying opacity, or a gradient, rather than many colours
- Sort stages in process order — do not re-sort by value
- Keep stages to 4–8 for readability

## Common Mistakes
- Values that increase between stages (breaks the funnel metaphor) — use a bar chart
- Stages that are not mutually exclusive (items counted in multiple stages) (smell I)
- Omitting stages with low volume rather than showing them explicitly (smell J)
- Using 3D perspective which distorts width comparisons

## Implementation Notes

### matplotlib
```python
# Centre-align bars of decreasing width
for i, (label, val) in enumerate(zip(stages, values)):
    ax.barh(i, val, left=(max_val - val) / 2, color=color)
    ax.text(max_val/2, i, label, ha='center', va='center')
ax.axis('off')
```

### plotly
```python
go.Funnel(y=stages, x=values, textposition='inside', textinfo='value+percent initial')
```

### altair
Use `mark_bar()` with centred horizontal bars; compute offsets manually.

### excel / tableau
**Excel**: Insert → Funnel Chart (Excel 2019+). **Tableau**: Use a Gantt Bar chart with centred offset calculation, or built-in Funnel chart in newer versions.

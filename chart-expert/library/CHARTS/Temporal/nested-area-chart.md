---
name: Nested Area Chart
category: Temporal
input_type: [time-series, interval-range]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Area, Line]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-value, color-hue]
tool_support: [matplotlib, plotly, altair, d3]
failure_modes: [C, L]
alternatives: [range-area-chart, area-chart, line-chart]
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

# Nested Area Chart

## Description
A nested area chart overlays multiple area bands concentrically, where each inner band represents a tighter interval or a specific sub-series nested within a wider one. It is most commonly used to show progressively narrower confidence or percentile bands around a central estimate — for example, 90%, 75%, and 50% credible intervals stacked inward from widest to narrowest.

## When to Use
- Displaying hierarchical uncertainty bands (e.g., forecast confidence intervals)
- Showing nested percentile ranges (p10/p90, p25/p75, median)
- Comparing a central line to multiple enclosing uncertainty bounds
- Communicating model output uncertainty to a technical or analytics audience

## When NOT to Use
- Series represent independent, non-hierarchical quantities (use overlapping area chart)
- More than 4–5 nesting levels (bands become too narrow to read)
- Audience expects precise values at each band boundary (use a table or error bars)
- Bands do not have a natural nesting/containment relationship

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date or ordered numeric | Sorted ascending |
| lower_outer / upper_outer | numeric | Widest band boundaries |
| lower_inner / upper_inner | numeric | Progressively tighter bounds |
| central | numeric | Median or mean line (optional but recommended) |

## Best Practices
- Use a single hue with progressively lighter shades for outer bands
- Always draw the widest band first (bottom layer) so inner bands are visible
- Label each band with its interval level (e.g., "90% CI") in a legend
- Overlay the central estimate as a distinct solid line
- Do not mislabel percentile bands as HDI unless they are — see Smell C

## Common Mistakes
- Labeling equal-tailed percentile intervals as "Highest Density Intervals" — see Smell C
- Over-smoothing bands to hide actual jagged uncertainty — see Smell L
- Using too many bands such that the innermost is visually imperceptible
- Implying the outer band is a hard boundary rather than a probability envelope

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.fill_between(t, lower90, upper90, alpha=0.15, color='steelblue', label='90% CI')
ax.fill_between(t, lower50, upper50, alpha=0.35, color='steelblue', label='50% CI')
ax.plot(t, median, color='steelblue', linewidth=2, label='Median')
ax.legend()
plt.tight_layout()
```

### plotly
Use multiple `go.Scatter(fill='tonexty')` traces in order from widest to narrowest.

### altair
Layer multiple `mark_area()` with increasing opacity and decreasing y-span using `y` and `y2` encodings.

### excel / tableau
Not natively supported. In Tableau, use dual-axis band charts with computed band boundaries as separate measures.

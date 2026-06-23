---
name: Circular Bar Chart
category: Comparison
input_type: [cat-value]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Bar, Circle]
cardinality_fit: [medium]
audience: [Public, Executive]
complexity: Intermediate
encoding_channels: [position, length, angle, color-hue]
tool_support: [d3, matplotlib, plotly, tableau]
failure_modes: [D, F]
alternatives: [bar-chart, horizontal-bar-chart, radar-chart, lollipop-chart]
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

# Circular Bar Chart

## Description
A circular bar chart (radial bar chart) arranges bars radially around a central point, with each bar radiating outward from the center. Bar length (radius) encodes the quantitative value. Categories are distributed around the circumference at equal angular intervals. It is a visually striking alternative to a standard bar chart but sacrifices precision for aesthetic appeal.

## When to Use
- Infographic or magazine-style contexts where visual impact is prioritized over precision
- When a large number of categories (10–30) benefit from a compact radial layout
- Cyclical data (months of the year, hours of the day) where the circular layout reinforces the cycle
- Public-facing dashboards where the aesthetic differentiates the presentation

## When NOT to Use
- Precise value comparison is required (radial length is harder to compare than linear bar length)
- Audience needs to read exact values (use a horizontal bar chart)
- Fewer than 8–10 categories (a standard bar chart is cleaner and more readable)
- Categories are not cyclical and the circular layout implies a false periodicity

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | The groups arranged around the circle |
| value | numeric | Encodes bar length (radius); must be non-negative |

## Best Practices
- Sort categories by value within the circular layout for readable ranking — see Smell D
- For cyclical data (months, weekdays), maintain natural order rather than value-sorting
- Start bars from a minimum baseline > 0 to prevent inner bars from disappearing
- Use a legend or direct labels since angular position is a less precise reference
- Include a scale annotation (reference radius lines) so lengths can be compared

## Common Mistakes
- Not sorting categories by value in non-cyclical contexts — see Smell D
- Encoding the value as the bar's outer bounding box area rather than its radial length — see Smell F
- Using circular bars when a horizontal bar chart would communicate the same information more clearly
- Overcrowding with too many categories so bars become too thin to distinguish

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np
N = len(categories)
angles = np.linspace(0, 2*np.pi, N, endpoint=False)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.bar(angles, values, width=2*np.pi/N * 0.8,
       bottom=0.2, color='steelblue', alpha=0.7, edgecolor='white')
ax.set_xticks(angles)
ax.set_xticklabels(categories, fontsize=8)
ax.set_yticklabels([])
```

### plotly
`go.Barpolar(r=values, theta=categories, width=[360/len(categories)]*len(categories))`

### altair
Requires polar coordinate transformation; not natively supported as a radial bar chart.

### excel / tableau
Tableau: Polar coordinate calculation using computed sin/cos fields; render as bars on a scatter plot base. Excel: Not supported natively — requires significant workaround.

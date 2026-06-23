---
name: Spline Graph
category: Temporal
input_type: [time-series, xy-simple]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Line]
cardinality_fit: [medium, large]
audience: [Executive, Public, Analytics]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [L, K]
alternatives: [line-chart, area-chart, stepped-line-graph]
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

# Spline Graph

## Description
A spline graph is a line chart where data points are connected by smooth cubic spline curves rather than straight line segments. The interpolated curve passes through all actual data points while using smooth Bezier or cubic spline mathematics to create a visually flowing shape. It is aesthetically appealing and can suggest underlying continuity in the data.

## When to Use
- The underlying phenomenon is genuinely continuous and smooth (e.g., physical sensor data, physiological measurements)
- Communicating general trend shape to a broad or executive audience where smoothness aids readability
- When you have enough data points that the smooth curve is a reasonable approximation
- Dashboard and reporting contexts where visual polish matters

## When NOT to Use
- Sparse data with few points — splines can wildly overshoot between points, creating false peaks and valleys — see Smell L
- Data has true sharp discontinuities or step changes (use a stepped line chart)
- The exact values between data points are meaningful and the interpolation would misrepresent them
- Scientific or analytical contexts where smoothing artifacts could be mistaken for real signal — see Smell L

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date or ordered numeric | Must be sorted ascending |
| value | numeric | Sufficient density for smooth interpolation |
| series (optional) | categorical | Multiple series with color differentiation |

## Best Practices
- Use only when data density is high enough to justify smooth interpolation
- Mark actual data points explicitly with dots to distinguish real values from interpolated curve
- Avoid monotone cubic splines if overshooting is a concern (use `monotone` interpolation)
- Be transparent in annotations if smoothing has been applied

## Common Mistakes
- Applying cubic spline to very sparse data, creating fictitious intermediate peaks — see Smell L
- Presenting a spline as if each point on the curve is a real data observation
- Using splines to make a noisy, unconvincing trend look smoother and more certain than it is
- Correlation artifact: a self-correlated time-smoothed series being misread as evidence of pattern — see Smell K

## Implementation Notes

### matplotlib
```python
from scipy.interpolate import make_interp_spline
import numpy as np
x_new = np.linspace(x.min(), x.max(), 300)
spline = make_interp_spline(x, y, k=3)
ax.plot(x_new, spline(x_new), color='steelblue')
ax.scatter(x, y, color='steelblue', zorder=5)  # show actual points
```

### plotly
`go.Scatter(x=..., y=..., line=dict(shape='spline', smoothing=1.3))`

### altair
`alt.Chart(df).mark_line(interpolate='monotone').encode(x='date:T', y='value:Q')`

### excel / tableau
Excel: Insert > Line chart > right-click series > Format Data Series > Smoothed Line. Tableau: Edit Line mark > Curve style.

---
name: Radial Heatmap
category: Distribution
input_type: [time-series, matrix-grid]
it_variants: []
analytical_function: Distribution
visual_family: Chart
shape_primitive: [Area, Polygon]
cardinality_fit: [medium, large]
audience: [Analytics, Technical, Public]
complexity: Intermediate
encoding_channels: [angle, color-value, position]
tool_support: [matplotlib, plotly, d3, tableau]
failure_modes: [E, J]
alternatives: [heat-map, spiral-histogram, calendar-heatmap, line-chart]
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

# Radial Heatmap

## Description
A Radial Heatmap (also called a circular heatmap or polar heatmap) arranges a heat map's rows in a circular arc rather than a linear grid — typically wrapping a periodic time axis (hours of the day, days of the week, months of the year) around the circumference. Each ring represents one unit of a longer cycle (e.g., a year or a week), and each segment of the ring represents a sub-unit (e.g., a month or a day). Cell colour encodes the data value as in a standard heat map. The circular layout leverages pre-attentive perception of periodicity and is visually engaging for cyclical patterns.

## When to Use
- Displaying periodic or cyclical data where the cycle wraps naturally (hours × days, months × years)
- Making temporal patterns visually striking for public-facing or presentation contexts
- When a linear heatmap would require very wide aspect ratios for many time periods

## When NOT to Use
- When the data is not cyclical — a radial layout imposes false periodicity on linear data
- When precise value comparison across rings is required — the inner rings are physically smaller and harder to compare
- When the number of rings (cycles) is large (> ~5) — outer rings dominate and inner rings become tiny
- For analytical audiences who need to read values precisely (use linear heat map instead)

## Data Requirements
- One cyclical time dimension (the angle axis — e.g., hour, day, month)
- One additional time or categorical dimension (the ring axis — e.g., year, week number)
- One numeric value per cell

## Best Practices
- Label ring levels clearly (e.g., year labels at the start of each ring)
- Use a perceptually uniform colour scale; avoid rainbow
- Start the angular axis at 12 o'clock (top) for clock-like time axes
- Include a colour legend with labelled tick marks
- Keep the number of rings small (3–5) for legibility

## Common Mistakes
- E (MC-noise-as-difference): inner ring segments appear smaller than outer ring segments even for the same value — colour must be the sole value encoding, and cell area differences can confuse perception
- J (silently-dropped-categories): missing periods render as gaps or zeros — document explicitly
- Choosing an overly fine angular granularity that makes individual segments too thin to distinguish colour
- Using radial heatmap for non-cyclical data, implying periodicity that does not exist

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
theta = np.linspace(0, 2 * np.pi, n_angular, endpoint=False)
r = np.arange(n_rings)
# Use pcolormesh in polar coordinates
ax.pcolormesh(theta, r, values_matrix, cmap='viridis')
ax.set_theta_zero_location('N')  # 12 o'clock start
ax.set_theta_direction(-1)       # clockwise
plt.colorbar(ax.pcolormesh(theta, r, values_matrix, cmap='viridis'),
             label='Value')
plt.tight_layout()
```

### plotly
Use `go.Barpolar` or a polar heatmap with `go.Heatmap` in polar coordinates. Plotly Express does not have a direct radial heatmap shortcut; use graph_objects.

### altair
Altair does not natively support polar coordinates. Pre-compute Cartesian coordinates for each segment and use `mark_arc` or custom polygon marks.

### excel / tableau
- **Excel**: No native radial heatmap. Approximate with Doughnut charts layered per ring.
- **Tableau**: No native support. Requires significant calculated field work to map angular and radial coordinates manually.

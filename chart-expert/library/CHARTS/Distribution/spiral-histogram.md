---
name: Spiral Histogram
category: Distribution
input_type: [time-series, xy-simple]
it_variants: []
analytical_function: Distribution
visual_family: Chart
shape_primitive: [Bar, Area]
cardinality_fit: [large, very-large]
audience: [Analytics, Public]
complexity: Advanced
encoding_channels: [angle, length, color-value]
tool_support: [matplotlib, d3, plotly]
failure_modes: [E]
alternatives: [histogram, radial-heatmap, density-plot, spiral-plot]
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

# Spiral Histogram

## Description
A Spiral Histogram arranges histogram bars along a spiral (Archimedean or logarithmic) rather than along a linear axis. The angle encodes the periodic component of a time or cyclical dimension (e.g., day of year, month), and the outward radial position represents progression through successive cycles (e.g., years). Each bar's length radiates outward from the spiral track, encoding frequency or value. The spiral form is primarily used for long time-series data where cyclic patterns repeat over many periods and a linear chart would become extremely wide.

## When to Use
- Long periodic time series (multiple years of monthly/daily data) where cyclical patterns are the focus
- When a linear histogram would require an impractically wide display
- Presentation and public-facing contexts where the spiral form creates visual interest
- Displaying seasonality trends that repeat over many annual cycles

## When NOT to Use
- When precise bar-length comparison is required — radial bars at different distances from centre are not directly comparable
- When the data is not cyclical or periodic — the spiral implies periodicity
- For analytical audiences performing exact value extraction — linear charts are more readable
- When only a few cycles exist — a radial chart or calendar heatmap is cleaner

## Data Requirements
- A time or cyclical index column (angle dimension)
- A numeric value or count column (bar length)
- Sufficient data to fill multiple cycles (typically 3+ years of monthly or daily data)

## Best Practices
- Label each cycle's start point clearly (e.g., year markers at January positions)
- Use consistent bar width and angular spacing
- Add a reference ring for scale (e.g., a dotted circle at a specific bar-length value)
- Include a colour scale if colour encodes a second variable
- Annotate anomalous spikes directly on the chart

## Common Mistakes
- E (MC-noise-as-difference): bars at outer rings appear larger in absolute terms even for the same radial length — perceptual distortion is inherent in the spiral form
- Using a spiral histogram when a simple line chart would communicate trends more clearly
- Insufficient labelling of the angular and radial dimensions — readers cannot orient themselves
- Overlapping bars when the spiral pitch is too tight

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

n = len(values)
theta = np.linspace(0, 2 * np.pi * n_cycles, n)
r_base = np.linspace(1, 3, n)  # spiral baseline radius
r_bar = r_base + values / values.max() * 0.4  # bar extends outward

fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
for i in range(n):
    ax.plot([theta[i], theta[i]], [r_base[i], r_bar[i]],
            color='steelblue', linewidth=2)
ax.set_rticks([])
ax.set_title('Spiral Histogram')
plt.tight_layout()
```

### plotly
No native spiral histogram. Construct using `go.Scatterpolar` with individual bar segments as line traces from baseline radius to bar-tip radius.

### altair
No native spiral support. Pre-convert spiral coordinates to Cartesian and use `mark_rule` or `mark_bar` with custom x/y/x2/y2 encodings.

### excel / tableau
Not natively supported. Requires heavy calculated field engineering or external pre-processing.

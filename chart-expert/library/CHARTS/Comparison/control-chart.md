---
name: Control Chart
category: Comparison
input_type: [time-series, xy-simple]
it_variants: []
analytical_function: Deviation
visual_family: Chart
shape_primitive: [Line, Dot]
cardinality_fit: [medium, large]
audience: [Technical, Analytics]
complexity: Advanced
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, d3, tableau, powerbi]
failure_modes: [B, E, L]
alternatives: [line-chart, run-chart, error-bars]
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

# Control Chart

## Description
A control chart (Shewhart chart) plots a time series of a process metric with three reference lines: the centerline (process mean), the Upper Control Limit (UCL), and the Lower Control Limit (LCL), typically set at ±3 sigma from the mean. Points outside the control limits or exhibiting non-random patterns signal that the process may be out of statistical control. It is the foundational tool of statistical process control (SPC).

## When to Use
- Monitoring manufacturing, service, or business processes for statistical stability over time
- Distinguishing common-cause variation (normal) from special-cause variation (assignable)
- Process improvement contexts (Six Sigma, Lean, quality control)
- Determining whether a process change had a statistically meaningful effect

## When NOT to Use
- Sample sizes are too small to estimate meaningful control limits
- The process is not stable enough to establish a baseline (too early in measurement)
- Zero-variance data where all points are identical — see Smell B
- Smoothing the line in a way that hides out-of-control signals — see Smell L

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| sample / time | ordered or date | Sequential sample identifier |
| value | numeric | The quality characteristic being measured |
| subgroup_size | integer (optional) | For X-bar charts; the size of each sample subgroup |

Control limits are computed from the data: UCL = mean + 3σ, LCL = mean - 3σ (for individuals chart).

## Best Practices
- Compute control limits from a stable baseline period; do not use specification limits as substitutes
- Highlight out-of-control points in a distinct color (typically red) for immediate identification
- Apply Western Electric rules (or Nelson rules) to identify non-random patterns beyond just ±3σ breaches
- Annotate the chart with process change events (new supplier, new machine, process improvement)
- Never smooth or interpolate the line — each individual data point must be visible

## Common Mistakes
- Confusing control limits (statistical) with specification limits (engineering tolerances)
- Zero-variance data creating flat lines with meaningless, collapsed control limits — see Smell B
- Applying smoothing that obscures out-of-control signals — see Smell L
- Using Monte Carlo simulated variation to pad control limits — see Smell E

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np
mean = df['value'].mean()
sigma = df['value'].std()
ucl, lcl = mean + 3*sigma, mean - 3*sigma

fig, ax = plt.subplots()
ax.plot(df['sample'], df['value'], 'b-o', markersize=4)
ax.axhline(mean, color='green', linewidth=1, label='Mean')
ax.axhline(ucl, color='red', linestyle='--', linewidth=1, label='UCL')
ax.axhline(lcl, color='red', linestyle='--', linewidth=1, label='LCL')
out_of_control = df[df['value'] > ucl] if df[df['value'] > ucl].any else df[df['value'] < lcl]
ax.legend()
plt.tight_layout()
```

### plotly
`go.Scatter` for the data line plus three `go.Scatter` traces with `mode='lines'` for mean, UCL, and LCL reference lines.

### altair
Layer `mark_line(point=True)` with three `mark_rule` references for mean, UCL, and LCL.

### excel / tableau
Tableau: Line chart with three reference lines added via the Analytics pane (constant value). Excel: Add three reference series to a line chart.

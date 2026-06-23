---
name: Density Plot
category: Distribution
input_type: [xy-simple, cat-value]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Area, Line]
cardinality_fit: [large, very-large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, area, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [G, E]
alternatives: [histogram, violin-plot, ecdf-plot, ridge-plot]
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

# Density Plot

## Description
A Density Plot (also known as a Kernel Density Estimate plot, KDE plot, or Density Trace Graph) visualises the distribution of a continuous variable as a smooth curve by applying kernel smoothing to the raw data. Unlike a histogram, a density plot is not affected by arbitrary bin boundaries — it represents the estimated probability density function across the variable's range. Peaks in the curve indicate where values are most concentrated, and the area under the curve integrates to 1 (when normalised to density).

## When to Use
- Showing the overall shape and modality of a continuous distribution
- Comparing the distributional shapes of multiple groups on the same axes (overlaid KDEs)
- When bin-edge sensitivity in histograms is problematic
- Communicating whether data is roughly normal, skewed, bimodal, or heavy-tailed
- Overlaying on a normalised histogram as a smooth reference

## When NOT to Use
- When n is very small (< ~30) — KDE creates a misleadingly smooth curve (smell G)
- When the variable is discrete or has sparse unique values — KDE implies false continuity
- When exact counts per bin matter (use histogram)
- When the audience needs to read off precise probabilities at specific values (use ECDF)
- When data has hard boundaries (e.g., 0 to 1) and the KDE bleeds past them without boundary correction

## Data Requirements
- One continuous numeric column
- n >= 50 recommended for stable KDE shape; n >= 100 preferred
- Optional: grouping column for overlaid multi-group densities

## Best Practices
- Document the kernel type (Gaussian is default) and bandwidth selection method (Scott's rule, Silverman's rule, or manual)
- Use `bw_adjust` or equivalent to fine-tune bandwidth — too narrow is spiky, too wide obscures structure
- Apply boundary correction when data is bounded (e.g., ages, proportions, non-negative measurements)
- Use transparency (alpha 0.3–0.5) when overlaying multiple group densities
- If comparing groups with very different sample sizes, note that KDE heights are not directly comparable without normalisation

## Common Mistakes
- G (KDE-over-atoms): applying KDE to data with fewer than ~30 points creates a false sense of smooth distribution
- Extending the KDE far beyond the data range without clipping to actual support
- E (MC-noise-as-difference): interpreting minor bumps in the density curve as meaningful distributional features rather than bandwidth artefacts
- Overlaying multiple group KDEs with different n per group and comparing curve heights as density magnitude
- Forgetting that the y-axis is "density", not "probability" or "count" — probability requires integrating over an interval

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np

kde = gaussian_kde(data, bw_method='scott')
x = np.linspace(data.min(), data.max(), 200)
plt.plot(x, kde(x), linewidth=2)
plt.fill_between(x, kde(x), alpha=0.3)
plt.xlabel('Value')
plt.ylabel('Density')
plt.tight_layout()
```
Or with seaborn: `sns.kdeplot(data=df, x='value', fill=True, bw_adjust=1.0)`

### plotly
```python
import plotly.figure_factory as ff
fig = ff.create_distplot([data], ['Group'], show_hist=False)
fig.show()
```
Or: `px.histogram(df, x='value', histnorm='probability density', marginal='rug')`

### altair
```python
import altair as alt
alt.Chart(df).transform_density('value', as_=['value', 'density']).mark_area(opacity=0.5).encode(
    x='value:Q',
    y='density:Q',
    color='group:N'
)
```

### excel / tableau
- **Excel**: No native KDE. Use NORM.DIST or manually computed kernel values in a helper table, then plot as a smooth line chart.
- **Tableau**: Analytics pane > Distribution Band or use a density mark type (Tableau 2020.1+). For custom KDE, pre-compute values externally.

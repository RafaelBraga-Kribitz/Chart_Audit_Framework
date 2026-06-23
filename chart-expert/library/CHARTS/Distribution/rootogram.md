---
name: Rootogram
category: Distribution
input_type: [xy-simple]
it_variants: []
analytical_function: Distribution
visual_family: Chart
shape_primitive: [Bar, Line]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [position, length]
tool_support: [matplotlib, d3]
failure_modes: [G, E]
alternatives: [histogram, density-plot, ecdf-plot, qq-plot]
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

# Rootogram

## Description
A Rootogram is a diagnostic chart for assessing the fit of a count distribution model to observed data. It plots the square root of observed frequencies as hanging bars from a smooth fitted curve (the square root of expected frequencies), so that the bars hang down from the fitted curve to a baseline. If the model fits well, bars nearly reach the zero line; bars above zero indicate over-prediction and bars below indicate under-prediction. Taking square roots stabilises the variance (Poisson-like counts have variance proportional to mean), making deviations visually uniform across the count range.

## When to Use
- Assessing goodness-of-fit of count distribution models (Poisson, negative binomial, zero-inflated models)
- Diagnosing specific failure modes: zero-inflation, overdispersion, or fat tails
- Communicating model fit to a technical/statistical audience
- After fitting GLMs or count regression models

## When NOT to Use
- When the audience is non-technical — the hanging-bar convention is not intuitive
- For continuous distributions (use a QQ plot or density residual plot instead)
- When a simple chi-squared test result is sufficient without visual diagnosis
- When n per bin is very small, making fitted curve estimates unstable

## Data Requirements
- One integer count column (observed frequencies per bin or category)
- A fitted model that provides expected count per bin
- Bins must cover the full support of the distribution (including zero)

## Best Practices
- Use "hanging" rootogram (bars hang from fitted curve) rather than "standing" — hanging highlights deviations from zero baseline
- Label the zero baseline clearly as the "perfect fit" reference
- Annotate regions of systematic over/under-prediction
- Report the fitted model parameters (e.g., lambda for Poisson, mu and theta for NegBin) in the caption
- Use a "suspended" variant (bars centred on fitted curve) to highlight symmetry of deviations

## Common Mistakes
- G (KDE-over-atoms): fitting a continuous density to discrete count data without noting discreteness
- E (MC-noise-as-difference): treating small deviations from zero baseline as model failure without computing a formal goodness-of-fit test
- Omitting the fitted curve — the chart is meaningless without the reference model overlay
- Not labelling the y-axis correctly (it shows √count, not count)

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

obs_counts = np.array([...])      # observed frequencies per bin
exp_counts = np.array([...])      # model-predicted expected frequencies
bins = np.arange(len(obs_counts))

sqrt_obs = np.sqrt(obs_counts)
sqrt_exp = np.sqrt(exp_counts)

fig, ax = plt.subplots()
# Hanging bars: bottom at sqrt_exp - sqrt_obs, top at sqrt_exp
ax.bar(bins, sqrt_obs, bottom=sqrt_exp - sqrt_obs,
       color='steelblue', edgecolor='white', label='Observed (hanging)')
ax.step(bins, sqrt_exp, where='mid', color='red', label='Fitted')
ax.axhline(0, color='black', linewidth=0.8)
ax.set_xlabel('Count value')
ax.set_ylabel('√Frequency')
ax.legend()
plt.tight_layout()
```

### plotly
Construct with `go.Bar` for hanging bars and `go.Scatter` for the fitted curve. Set `base` parameter to `sqrt_exp - sqrt_obs`.

### altair
Pre-compute sqrt values and use `mark_bar` with explicit `y` and `y2` encodings for the hanging bar.

### excel / tableau
Not natively supported. Requires pre-computed hanging bar heights imported as data columns.

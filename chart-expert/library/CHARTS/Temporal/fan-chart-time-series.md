---
name: Fan Chart (Time Series)
category: Temporal
input_type: [time-series, interval-range]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Area, Line]
cardinality_fit: [medium, large]
audience: [Analytics, Technical, Executive]
complexity: Intermediate
encoding_channels: [position, color-value, color-hue]
tool_support: [matplotlib, plotly, d3, r-ggplot2]
failure_modes: [A, C, L]
alternatives: [range-area-chart, nested-area-chart, line-chart]
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

# Fan Chart (Time Series)

## Description
A fan chart is a time series chart that shows a historical line followed by a set of progressively widening uncertainty bands extending into the future forecast horizon. The bands fan out from the last known data point, with the fan width representing the increasing uncertainty of projections over time. Each nested band typically represents a different probability interval (e.g., 50%, 75%, 90%).

## When to Use
- Communicating probabilistic forecasts with uncertainty that grows over the forecast horizon
- Economic and financial forecasting (central bank inflation forecasts are a canonical use case)
- Model output visualization where uncertainty bounds are explicitly computed
- When the audience needs to understand not just the point forecast but the range of likely outcomes

## When NOT to Use
- Historical data only with no forecast component (use a line chart or range area chart)
- Uncertainty bounds are constant or non-probabilistic (use error bars instead)
- Audience cannot interpret probabilistic intervals and needs a simpler communication (use point forecast only)
- Bands are symmetric by assumption but the true uncertainty distribution is highly skewed

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date | Includes both historical and forecast horizon |
| central | numeric | Point estimate / most likely path |
| lower_90 / upper_90 | numeric | Outer fan boundary (widest) |
| lower_50 / upper_50 | numeric | Inner fan boundary |
| is_forecast | boolean | Flag to distinguish historical from forecast portion |

## Best Practices
- Plot historical data as a solid line; use a dashed or lighter line for the forecast central path — see Smell A
- Use a single hue with progressively lighter fills for wider bands
- Label each band with its probability level directly or in a legend
- Explicitly mark the "as-of" date where history ends and forecast begins
- Do not anchor the fan at a point that implies certainty — the central estimate is also probabilistic

## Common Mistakes
- Anchoring the fan from the final historical point as if that point is certain, ignoring its own uncertainty — see Smell A
- Mislabeling forecast percentile bands as HDIs without verifying the distributional properties — see Smell C
- Over-smoothing fan boundaries to look cleaner than the underlying model warrants — see Smell L
- Failing to document the model or assumptions generating the uncertainty bounds

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.fill_between(forecast_dates, lower90, upper90, alpha=0.15, color='steelblue', label='90% CI')
ax.fill_between(forecast_dates, lower50, upper50, alpha=0.35, color='steelblue', label='50% CI')
ax.plot(historical_dates, historical, color='steelblue', linewidth=2)
ax.plot(forecast_dates, central, color='steelblue', linewidth=2, linestyle='--')
ax.axvline(transition_date, color='gray', linestyle=':', linewidth=1)
ax.legend()
```

### plotly
Layer multiple `go.Scatter(fill='tonexty')` traces for each band level, with the historical line as a separate solid trace.

### altair
Layer multiple `mark_area` transforms for each interval level plus a `mark_line` for the historical and forecast central paths.

### excel / tableau
Tableau: Dual-axis approach with computed band fields. Requires separate data model with lower/upper columns per band. Excel: Not practical without significant data preparation.

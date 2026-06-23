---
name: Renko Chart
category: Temporal
input_type: [time-series, xy-simple]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Square]
cardinality_fit: [large, very-large]
audience: [Technical]
complexity: Advanced
encoding_channels: [position, color-hue]
tool_support: [d3, matplotlib]
failure_modes: [L]
alternatives: [candlestick-chart, kagi-chart, line-chart]
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

# Renko Chart

## Description
A Renko chart is a Japanese price chart that filters out time and minor price fluctuations by plotting fixed-size bricks (boxes) only when price moves by a predetermined amount (the "brick size"). A new brick is added only when the price moves the full brick size in either direction. Up bricks are typically white or green; down bricks are black or red. Time is not uniformly represented on the x-axis, making Renko charts purely price-movement focused.

## When to Use
- Technical analysis contexts where filtering out noise is desired to reveal trend direction
- Identifying support and resistance levels in financial price data
- Trend following strategies where small price fluctuations should not trigger signals
- When the trader wants to focus on price movement size rather than time elapsed

## When NOT to Use
- Time-series analysis where the timing of price moves matters (use a candlestick chart)
- Audiences unfamiliar with Renko encoding — the non-linear x-axis confuses most viewers
- Non-financial data without a clear "brick size" concept
- When precise timestamps are required for each data point

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| price (close) | numeric | Sequential price series; usually daily close prices |
| brick_size | numeric (parameter) | Fixed price increment per brick; chosen by analyst |

The chart requires pre-processing: compute bricks from raw price data before rendering.

## Best Practices
- Choose brick size thoughtfully: too small = noisy, too large = misses important moves
- Use ATR (Average True Range) as a guide for setting brick size dynamically
- Note that the x-axis is not uniform time — label this clearly for any audience
- Combine with volume or other indicators only if they can be mapped to the brick count axis

## Common Mistakes
- Applying Renko smoothing to hide genuine price volatility, implying artificial smoothness — see Smell L
- Choosing a brick size that fits historical data perfectly but overfits to noise
- Presenting a Renko chart to a non-technical audience without explaining the x-axis
- Comparing Renko charts across different brick sizes as if they are equivalent

## Implementation Notes

### matplotlib
Requires manual brick computation:
```python
# Pseudocode for Renko brick construction
bricks = []
for price in prices:
    while price >= current_price + brick_size:
        bricks.append(('up', current_price))
        current_price += brick_size
    while price <= current_price - brick_size:
        bricks.append(('down', current_price))
        current_price -= brick_size
# Then render bricks as colored rectangles
```

### plotly
Not natively supported; requires pre-computed brick data and custom `go.Scatter` or rectangle drawing.

### altair
Not supported natively; requires pre-computed brick data.

### excel / tableau
Not supported in either tool without significant custom calculation.

---
name: Candlestick Chart
category: Temporal
input_type: [interval-range, time-series]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Bar, Line]
cardinality_fit: [medium, large]
audience: [Technical, Analytics]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [plotly, d3, matplotlib, tableau, powerbi]
failure_modes: []
alternatives: [range-area-chart, line-chart, renko-chart, kagi-chart]
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

# Candlestick Chart

## Description
A candlestick chart displays four values per time period (open, high, low, close — OHLC) using a rectangular body (open-to-close range) and thin wicks (high and low extremes). The body is colored to indicate whether the close was higher (bullish, typically green or white) or lower (bearish, typically red or black) than the open. It is the standard visualization for financial price data.

## When to Use
- Displaying OHLC financial price data (stocks, commodities, currencies, crypto)
- Analyzing price action patterns and trends over time periods
- When all four OHLC values are available and the open-to-close direction is meaningful
- Technical analysis contexts where candlestick patterns (doji, hammer, engulfing) are being identified

## When NOT to Use
- Only closing prices are available (use a line chart)
- The audience is unfamiliar with OHLC encoding (use a simplified chart or add a legend)
- Data is not financial price data with open/close semantics
- Very long time horizons where individual candles become too narrow to read

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date | The time period for each candle |
| open | numeric | Price at the start of the period |
| high | numeric | Highest price during the period; >= open, close |
| low | numeric | Lowest price during the period; <= open, close |
| close | numeric | Price at the end of the period |
| volume (optional) | numeric | Often displayed as a sub-chart below |

## Best Practices
- Use green/white for bullish candles (close > open) and red/black for bearish
- Display volume as a bar sub-chart below the main panel for context
- Include moving average overlays (SMA, EMA) when trend analysis is the goal
- Use appropriate time granularity: daily candles for weeks-to-months, weekly for months-to-years
- Ensure high >= max(open, close) and low <= min(open, close) in data validation

## Common Mistakes
- Rendering candles so densely packed that bodies and wicks are indistinguishable
- Using inconsistent color encoding (e.g., red for up in some tools, down in others)
- Displaying candlesticks for non-OHLC data just because the format looks technical
- Ignoring the volume dimension when interpreting price moves

## Implementation Notes

### matplotlib
```python
import mplfinance as mpf
mpf.plot(df, type='candle', volume=True,
         style='charles', title='AAPL Price')
# df must have DatetimeIndex with Open, High, Low, Close columns
```

### plotly
`go.Candlestick(x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])`

### altair
Not natively supported; requires manual rule and bar marks layered together with color encoding.

### excel / tableau
Excel: Insert > Stock Chart > Open-High-Low-Close. Tableau: Use Gantt bar marks with computed fields for body and wick segments.

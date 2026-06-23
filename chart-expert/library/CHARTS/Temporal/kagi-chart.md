---
name: Kagi Chart
category: Temporal
input_type: [time-series, xy-simple]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Line]
cardinality_fit: [large, very-large]
audience: [Technical]
complexity: Advanced
encoding_channels: [position, color-hue, color-value]
tool_support: [d3, matplotlib]
failure_modes: [L]
alternatives: [candlestick-chart, renko-chart, line-chart]
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

# Kagi Chart

## Description
A Kagi chart is a Japanese price chart that shows price movements using a series of vertical lines connected by horizontal links. The line changes direction only when price reverses by a set reversal amount. Lines become thick (Yang) when price breaks above the previous high and thin (Yin) when price falls below the previous low. Like Renko, time is not uniform on the x-axis — the chart only advances when a reversal occurs.

## When to Use
- Technical financial analysis focused on identifying supply and demand levels
- Filtering intraday or day-to-day noise to see the dominant price trend
- Identifying when a trend reverses by watching for Yang (thick) to Yin (thin) transitions
- When the analyst wants a view that is independent of time elapsed

## When NOT to Use
- The audience needs to correlate price moves with specific dates/events (use candlestick)
- The reversal amount parameter is not clearly defined or defensible
- Non-financial data that does not have a natural "reversal amount" interpretation
- General audiences who are unfamiliar with Kagi line conventions

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| price (close) | numeric | Sequential price series |
| reversal_amount | numeric (parameter) | Minimum move to trigger a direction change; often 4% or ATR-based |

The chart requires pre-processing: compute the Kagi lines from raw price data.

## Best Practices
- Use a percentage-based reversal (e.g., 4% of price) for long time series; fixed dollar amounts skew at different price levels
- Clearly indicate whether line weight changes (Yin/Yang) or color changes are used to signal trend direction
- Add price scale on the y-axis; x-axis is ordinal (reversal count), not calendar time
- Pair with other indicators sparingly — the chart is already abstract

## Common Mistakes
- Using too small a reversal amount, recreating the noise the chart is meant to filter — see Smell L
- Choosing a reversal amount that is data-mined for historical pattern-fitting
- Presenting to audiences who interpret the x-axis as calendar time
- Confusing Kagi with Renko — both suppress time but use different geometric primitives (lines vs. bricks)

## Implementation Notes

### matplotlib
Requires manual pre-computation of Kagi line vertices:
```python
# Pseudocode
direction = 'up'
vertices = [(0, prices[0])]
for price in prices[1:]:
    if direction == 'up' and price < vertices[-1][1] - reversal:
        direction = 'down'
        vertices.append((next_x, price))
    elif direction == 'down' and price > vertices[-1][1] + reversal:
        direction = 'up'
        vertices.append((next_x, price))
    else:
        vertices[-1] = (vertices[-1][0], price)  # extend current line
# Then render as thick/thin alternating line segments
```

### plotly
Not natively supported; requires custom rendering of pre-computed line segments.

### altair
Not supported natively.

### excel / tableau
Not supported.

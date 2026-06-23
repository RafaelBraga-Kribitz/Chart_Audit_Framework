---
name: Bubble Timeline
category: Temporal
input_type: [event-time, xyz-trivariate]
it_variants: []
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Circle]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive, Public]
complexity: Intermediate
encoding_channels: [position, area, color-hue, color-value]
tool_support: [d3, plotly, altair, matplotlib, tableau]
failure_modes: [F]
alternatives: [timeline, gantt-chart, scatter-plot]
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

# Bubble Timeline

## Description
A bubble timeline extends a standard timeline by encoding an additional quantitative variable as the size (area) of a circle placed at each event's position on the time axis. The x-axis encodes time, bubble position on y may represent a category or lane, and bubble size represents magnitude (e.g., revenue, impact, event scale). This provides three dimensions of information in a compact temporal layout.

## When to Use
- Placing events in time while simultaneously communicating their relative magnitude or scale
- Product launch timelines where bubble size = revenue impact or number of users affected
- Historical event visualization where bubble size = casualty count, economic value, or significance
- When a simple timeline lacks quantitative context for each event's importance

## When NOT to Use
- The quantitative variable encoded as size is not meaningful or reliable
- Many events cluster at similar times, causing bubble overlap that obscures information
- The audience cannot reliably decode area differences (use a bar chart alongside the timeline instead)
- More than ~20–30 events — too many bubbles become visually cluttered

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| event_date | date | Timestamp for each event |
| label | string | Event name |
| magnitude | numeric | The quantity encoded as bubble area (not radius) |
| category (optional) | categorical | For y-axis lanes or bubble color |

## Best Practices
- Encode magnitude as bubble area (not radius or diameter) to avoid area perception errors — see Smell F
- Use a size legend with 2–3 reference circles showing exact values
- Separate simultaneous events into lanes (y-axis) to prevent overlap
- Keep bubble count low enough that individual events are identifiable
- Annotate the most significant events directly

## Common Mistakes
- Encoding magnitude as radius rather than area, making large events appear disproportionately large — see Smell F
- Placing too many events without lane separation, creating an unreadable blob
- Using bubble color redundantly with size when color could encode a distinct dimension
- Omitting a size legend, leaving viewers unable to interpret bubble magnitudes

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(figsize=(12, 4))
# Scale area proportionally: size parameter = area in points^2
sizes = (df['magnitude'] / df['magnitude'].max()) * 2000
ax.scatter(df['event_date'], df['category'], s=sizes,
           c=df['color_val'], alpha=0.6, edgecolors='white')
for _, row in df.iterrows():
    ax.annotate(row['label'], (row['event_date'], row['category']),
                 ha='center', va='bottom', fontsize=7)
plt.tight_layout()
```

### plotly
`px.scatter(df, x='event_date', y='category', size='magnitude', color='category', hover_name='label', size_max=60)`

### altair
`alt.Chart(df).mark_circle().encode(x='event_date:T', y='category:N', size='magnitude:Q', color='category:N', tooltip='label:N')`

### excel / tableau
Tableau: Scatter plot with date on x-axis, category on y-axis, size by magnitude, and label text overlay. Excel: Bubble chart with date on x-axis, requiring numeric date formatting.

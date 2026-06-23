---
name: Dot Density Plot
category: Distribution
input_type: [xy-simple, cat-value]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Dot]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical, Public]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [E, J]
alternatives: [beeswarm-plot, strip-plot, histogram, counts-plot]
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

# Dot Density Plot

## Description
A Dot Density Plot (also called a Wilkinson dot plot) represents each individual observation as a dot, stacking dots vertically in columns above their value on the x-axis. Unlike a histogram that uses bar height to show counts, a dot density plot makes the count tangible — you can literally count the dots. Dots are stacked directly above their data value, with no binning: each dot sits at its exact value position. The visual output resembles a histogram in overall shape but preserves the "one mark per datum" philosophy and shows the actual distribution of individual values.

## When to Use
- Small to moderate datasets (n < ~200) where individual observations carry interpretive weight
- Educational contexts where readers should understand that each mark = one data point
- Showing the exact distribution of discrete or limited-precision continuous values
- Comparing the distribution of several small groups side-by-side

## When NOT to Use
- Large n (> ~300) — stacked columns become too tall and dots too small
- When the variable is truly continuous with many unique values — every column has at most one dot, degrading to a strip plot
- When approximate density shape is sufficient and individual points are not accountable

## Data Requirements
- One continuous or discrete numeric column (the value being stacked)
- Optional: one categorical grouping column for side-by-side comparison
- Best with n between 20 and 200

## Best Practices
- Use fixed dot size so each dot represents exactly one observation
- Use consistent y-axis increments based on actual stacking (not normalised)
- Colour-code by group if showing multiple distributions on the same axis
- Label the x-axis with the variable name and units
- Annotate summary statistics (mean, median) with reference lines

## Common Mistakes
- E (MC-noise-as-difference): interpreting slight differences in column heights as meaningful without statistical testing
- J (silently-dropped-categories): omitting zero-count positions can misrepresent the support of the distribution
- Using unequal dot sizes — destroys the "one dot per observation" visual equality
- Allowing dots from different groups to overlap without colour distinction

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

def dot_density(ax, data, color='steelblue', size=100):
    from collections import Counter
    counts = Counter(np.round(data, 1))  # round to bin precision
    for val, cnt in sorted(counts.items()):
        ax.scatter([val] * cnt,
                   [(i + 0.5) for i in range(cnt)],
                   s=size, color=color, alpha=0.8)

fig, ax = plt.subplots()
dot_density(ax, data)
ax.set_xlabel('Value')
ax.set_ylabel('Count')
plt.tight_layout()
```
Or use `plotnine` (ggplot2-style): `geom_dotplot(binwidth=...)`.

### plotly
No native dot density plot. Pre-compute stacking positions in Python and use `go.Scatter` with individual point coordinates.

### altair
```python
import altair as alt
alt.Chart(df).mark_circle(size=50).encode(
    x='value:Q',
    y=alt.Y('stack_index:Q', title='Count')
).transform_window(
    stack_index='rank()',
    groupby=['value_bin']
).transform_calculate(value_bin='round(datum.value * 5) / 5')
```

### excel / tableau
- **Excel**: Scatter chart with pre-computed stack y-positions in a helper column.
- **Tableau**: Use `INDEX()` within a partition by bin as the y-axis; set mark to Circle.

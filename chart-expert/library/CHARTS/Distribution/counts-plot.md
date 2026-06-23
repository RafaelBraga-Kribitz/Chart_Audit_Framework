---
name: Counts Plot
category: Distribution
input_type: [cat-value, xy-simple]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Dot, Circle]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Basic
encoding_channels: [position, area]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [E, J]
alternatives: [strip-plot, jitter-plot, histogram, dot-density-plot]
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

# Counts Plot

## Description
A Counts Plot (also called a count chart or dot frequency plot) displays the frequency of observations at each value of a variable as a stack of dots or circles, where each dot represents one observation. It is essentially a discrete histogram that preserves the "one mark per observation" philosophy. Counts plots are especially useful for small datasets with discrete or semi-discrete values, allowing viewers to read off exact counts while seeing the distributional shape simultaneously.

## When to Use
- Displaying the frequency distribution of a small, discrete or ordinal variable
- Showing exact counts while also communicating distributional shape
- Audit and QA contexts where each observation carries individual weight
- Categorical or low-cardinality continuous data where binning would be lossy

## When NOT to Use
- When n is large (> ~200) — stacked dots become too small to see
- When the variable is truly continuous with many unique values (use histogram or density plot)
- When the audience needs smooth trend reading rather than exact counts

## Data Requirements
- One discrete or low-cardinality continuous column (the value being counted)
- Optional: one categorical grouping column for faceted or coloured counts
- Best with n < ~150 total observations

## Best Practices
- Use consistent dot size so each dot visually equals exactly one observation
- Add count labels at the top of each stack for direct reading
- Keep axes clean — the y-axis is implicit (stack height = count)
- Sort categories by frequency for comparison purposes
- Use colour to encode a secondary variable if needed, with a clear legend

## Common Mistakes
- J (silently-dropped-categories): omitting zero-count categories breaks the visual continuity
- E (MC-noise-as-difference): interpreting a one-dot difference as meaningful without context of total n
- Using counts plot on large n — the chart breaks down visually
- Varying dot size — it destroys the "one dot = one observation" convention

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
from collections import Counter

counts = Counter(data)
for val, cnt in counts.items():
    for i in range(cnt):
        plt.scatter(val, i + 0.5, s=100, color='steelblue')
plt.xlabel('Value')
plt.ylabel('Count')
```

### plotly
No direct counts plot. Approximate with `px.histogram` set to `histfunc='count'` and using a scatter trace for individual dots.

### altair
```python
import altair as alt
alt.Chart(df).mark_circle(size=60).encode(
    x='value:O',
    y=alt.Y('cumcount():Q', title='Count'),
    color=alt.value('steelblue')
).transform_window(
    cumcount='count()',
    groupby=['value']
)
```

### excel / tableau
- **Excel**: Manual construction using a helper column for stack position.
- **Tableau**: Use `INDEX()` as row number within a partition to stack dots along y-axis.

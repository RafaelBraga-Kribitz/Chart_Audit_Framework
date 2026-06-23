---
name: Violin Plot
category: Distribution
input_type: [cat-value, demo-grouped]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Area, Line]
cardinality_fit: [medium, large, very-large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, area, length]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [G, E]
alternatives: [box-plot, density-plot, beeswarm-plot, strip-plot]
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

# Violin Plot

## Description
A Violin Plot combines a Box Plot with a mirrored Kernel Density Estimate (KDE) to show both summary statistics and the full distribution shape of a continuous variable across groups. The width of the "violin" at each value represents the estimated probability density at that point, making multimodal or skewed distributions immediately visible. A box-plot summary (median, IQR, whiskers) is often embedded inside the violin.

## When to Use
- Comparing distribution shapes across groups, especially when multimodality or skewness is expected
- When a box plot is too reductive and would hide important distributional features
- Communicating distributional differences to a technical or analytics audience
- Exploratory analysis of measurement data across experimental conditions

## When NOT to Use
- When n per group is very small (< 30–50) — the KDE will be misleading (smell G)
- When the audience is non-technical and unfamiliar with density estimation
- When too many groups exist (> ~8) — violins become too narrow to read
- When exact quartile values matter more than shape (use box plot)
- When data has discrete or semi-discrete support — KDE creates false continuity

## Data Requirements
- One continuous numeric column (the value being distributed)
- One categorical grouping column
- Recommended minimum n per group: ~50 for KDE to be meaningful
- Optional: secondary grouping for split violins

## Best Practices
- Embed a box plot or dot for median inside each violin for a summary anchor
- Use split violins (half-half) to compare two sub-groups within each category
- Set KDE bandwidth deliberately (too narrow = spiky; too wide = oversmoothed)
- Label the y-axis with the variable name and units; label groups on the x-axis
- Normalise violin widths to the same maximum width across groups (default in most tools)
- Supplement with a strip or beeswarm overlay when n is moderate (30–200) to show actual data

## Common Mistakes
- G (KDE-over-atoms): applying violin plot to groups with n < 30 creates a smooth shape that does not reflect the data
- Leaving the default bandwidth without checking — auto-bandwidth may undersmooth or oversmooth
- E (MC-noise-as-difference): treating wider violins in a region as definitively "more data there" without accounting for sample size differences
- Forgetting to state the KDE kernel and bandwidth in methods or chart footnotes for reproducibility
- Clipping violins at data bounds vs. letting them extend beyond — document the choice

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.violinplot([group_a, group_b], positions=[1, 2],
              showmedians=True, showextrema=True)
ax.set_xticks([1, 2])
ax.set_xticklabels(['A', 'B'])
ax.set_ylabel('Value')
plt.tight_layout()
```
`bw_method` controls KDE bandwidth. For full flexibility, use seaborn's `violinplot`.

### plotly
```python
import plotly.express as px
fig = px.violin(df, x='group', y='value', box=True, points='outliers')
fig.show()
```
`violinmode='overlay'` or `'group'` controls multi-group layout. `side='positive'` for half-violins.

### altair
Altair does not have a native violin mark; combine a density transform with an area mark:
```python
alt.Chart(df).transform_density('value', groupby=['group'], as_=['value','density']).mark_area(orient='horizontal').encode(
    y='value:Q', x=alt.X('density:Q', stack='center', impute=None), color='group:N'
)
```

### excel / tableau
- **Excel**: No native violin plot. Use third-party add-ins or build manually with helper columns.
- **Tableau**: Not natively supported. Approximate via density marks + dual axis or use a custom Shape palette with KDE computed externally.

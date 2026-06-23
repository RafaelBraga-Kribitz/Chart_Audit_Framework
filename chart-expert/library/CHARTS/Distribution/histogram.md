---
name: Histogram
category: Distribution
input_type: [xy-simple]
it_variants: []
analytical_function: Distribution
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [large, very-large]
audience: [Analytics, Technical]
complexity: Basic
encoding_channels: [position, length]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [G, E]
alternatives: [density-plot, bar-chart, frequency-polygon]
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

# Histogram

## Description
A Histogram visualises the distribution of data over a continuous interval by grouping values into bins and displaying the count (or frequency) of observations in each bin as a bar. Each bar's height encodes how many data points fall within that interval. Histograms help reveal where values are concentrated, the shape of the distribution (normal, skewed, bimodal), and the presence of outliers or gaps.

## When to Use
- Exploring the distribution shape of a single continuous variable
- Identifying modality (unimodal, bimodal, multimodal) in a dataset
- Detecting skewness, outliers, or gaps in continuous data
- Giving a rough view of the probability distribution before formal modeling
- QA checks on sensor readings, scores, measurements, and other numeric columns

## When NOT to Use
- When comparing distributions across many groups simultaneously (use box plots or violin plots instead)
- When the variable is categorical or ordinal (use bar chart instead)
- When exact data points matter more than aggregate shape (use dot plot or ECDF)
- When n < ~30, bin choice dominates the picture and individual point plots are clearer
- When communicating to an executive audience that needs a precise single number

## Data Requirements
- One continuous numeric column (the variable being distributed)
- Sample size >= 30 recommended; >= 100 for reliable shape estimation
- Optional: a grouping/facet column for small-multiple histograms

## Best Practices
- Choose bin count deliberately: Sturges' rule (k = 1 + log2 n) or Freedman-Diaconis as starting points; then inspect
- Always label axes with units; label y-axis as "Count", "Frequency", or "Density" explicitly
- Use consistent bin widths unless there is a domain reason for variable width
- Annotate the mean or median with a vertical reference line when the audience needs a summary statistic
- Normalise to density (area = 1) before overlaying a KDE curve, otherwise y-axes conflict
- For comparing two distributions, prefer overlapping semi-transparent histograms or faceted panels over stacking

## Common Mistakes
- G (KDE-over-atoms): overlaying a smooth KDE curve on a discrete or very small dataset implies false continuity
- E (MC-noise-as-difference): declaring two distributions "different" from visual inspection alone without a statistical test
- Choosing bin count to confirm a hypothesis (too few bins hide multimodality; too many create noise peaks)
- Mislabeling y-axis as "Probability" when it actually shows raw counts
- Starting y-axis above zero, which exaggerates relative differences between bars

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.hist(data, bins='fd', edgecolor='white', color='steelblue')
ax.set_xlabel('Value')
ax.set_ylabel('Count')
ax.set_title('Histogram')
plt.tight_layout()
```
Key params: `bins` (int, sequence, or string rule like `'auto'`, `'fd'`, `'sturges'`), `density=True` to normalise, `alpha` for transparency when overlaying.

### plotly
```python
import plotly.express as px
fig = px.histogram(df, x='value', nbins=30, title='Histogram')
fig.show()
```
Use `histnorm='probability density'` to normalise. `color` parameter splits by group.

### altair
```python
import altair as alt
alt.Chart(df).mark_bar().encode(
    alt.X('value:Q', bin=alt.Bin(maxbins=30)),
    y='count()'
)
```
Use `alt.Bin(step=...)` for fixed bin width. Add `color` for grouped histograms.

### excel / tableau
- **Excel**: Insert > Chart > Histogram (Analysis ToolPak or native in Excel 2016+). Set bin width in Format Axis.
- **Tableau**: Drop continuous measure onto Columns; change mark type to Bar; show "Number of Records" on Rows. Right-click axis > Edit > Fixed bin size.

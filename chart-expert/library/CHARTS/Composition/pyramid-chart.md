---
name: Pyramid Chart
category: Composition
input_type: [cat-value, demo-grouped]
it_variants: [IT026, IT011]
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Pyramid, Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Public]
complexity: Basic
encoding_channels: [length, area, color-hue]
tool_support: [matplotlib, plotly, d3, tableau, powerbi, excel]
failure_modes: [I, J]
alternatives: [funnel-chart, stacked-bar-100pct]
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: part-to-whole
ibcs_status: preferred
questions: ["How is the whole split on Pyramid Chart?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
---
# Pyramid Chart

## Description
A Pyramid Chart (also called a Population Pyramid when showing age/gender demographics) represents data as a series of stacked horizontal bars forming a triangular or trapezoidal shape. Values are typically largest at the base and decrease toward the apex. In its demographic form, it shows age cohorts split by two groups (male/female) on opposing sides. In its generic form it ranks hierarchical or sequential categories from largest to smallest.

## When to Use
- Population demographics showing age distribution by gender
- Hierarchical data with an inherent ordering from base to peak (e.g., organisational tiers)
- Illustrating priority or importance levels (e.g., Maslow's hierarchy, sales tiers)

## When NOT to Use
- Data without a natural ordering from largest to smallest
- When precise comparison between individual bars matters more than overall shape
- More than ~15 rows (bars become too thin)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical (ordered) | Age group, tier, or hierarchy level — bottom to top |
| left_value | numeric (≥0) | Left side value (e.g., female count) |
| right_value | numeric (≥0) | Right side value (e.g., male count); omit for single-sided |

## Best Practices
- For population pyramids: ensure both axes use the same scale for fair comparison
- Annotate tick labels with age group names on the vertical axis
- Use two contrasting colours for the two sides in a population pyramid
- Sort from largest (bottom) to smallest (top) for non-demographic use

## Common Mistakes
- Different x-axis scales on left and right sides of a population pyramid (distorts comparison)
- Using 3D perspective that makes bar lengths ambiguous
- Omitting axis labels so viewers cannot read actual values
- Treating non-exclusive categories as exclusive by stacking them (smell I)


## Dashboard and other surfaces

status: placeholder

`Pyramid Chart` can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with funnel-chart, stacked-bar-100pct.

Suggested communication placement: **breakdown** zone. Vault coarse type, when a scraped template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
# Population pyramid
ax.barh(ages, -female_vals, color='pink', label='Female')
ax.barh(ages, male_vals, color='steelblue', label='Male')
ax.set_xticks([-max_val, 0, max_val])
ax.set_xticklabels([str(abs(int(x))) for x in ax.get_xticks()])
```

### plotly
Use `go.Bar` with two horizontal bar traces; negate one side's values and apply `abs()` to tick labels.

### altair
Two `mark_bar()` layers with one using negated x values; shared y encoding for age groups.

### excel / tableau
**Excel**: Population pyramid via bar chart with one series negated. **Tableau**: Dual-axis bar chart with mirrored axes.

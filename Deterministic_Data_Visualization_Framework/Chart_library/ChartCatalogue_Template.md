# Chart Catalogue Template

Use this structure for each chart you document in your Obsidian vault.

---

## Example 1: Sales Trend Line Chart

```markdown
---
title: Sales Trend Over Time
chart_type: Line Chart
data_input_type: time-series
tags: [time-series, line-chart, business, sales]
use_cases: [trend-analysis, performance-monitoring]
created: 2026-06-23
---

# Sales Trend Over Time

## Data Structure
**Input Type:** [[time-series]]  
**Shorthand:** `#time-series`  
**Format:**
```
| Date    | Sales_USD |
|---------|-----------|
| 1-1-2025| 50,000    |
| 2-1-2025| 45,000    |
| 3-1-2025| 62,000    |
```

## Why This Chart Type
- Shows **change over time** (temporal data required)
- Good for identifying trends, seasonality, anomalies
- Excellent for executive dashboards
- Continuous time axis ensures proper sequencing

## Configuration
- **X-axis:** Date (temporal, ordered)
- **Y-axis:** Sales amount (numeric, continuous)
- **Encoding:** Position on Y-axis represents value
- **Best practice:** Include baseline or target line for comparison

## Variations
- **Area chart:** For emphasis on magnitude
- **Multi-line:** If comparing multiple product lines
- **Candlestick:** If including OHLC (Open/High/Low/Close)

## Tools
- Excel: Insert > Line Chart
- Tableau: Drag date to Columns, metric to Rows
- Power BI: Line chart visual + date slicer
- D3.js: `d3.line()` with time scale

## Related Charts
- [[xy-simple|Scatter Plot]] (if showing individual points)
- [[xy-dual-series|Multi-Line Chart]] (if comparing trends)
- [[composition|Stacked Area]] (if showing parts over time)

---
```

## Example 2: Product Mix Bar Chart

```markdown
---
title: Product Mix by Category
chart_type: Bar Chart
data_input_type: cat-multi-value
tags: [cat-multi-value, bar-chart, composition, products]
use_cases: [comparison, market-share, portfolio-analysis]
created: 2026-06-23
---

# Product Mix by Category

## Data Structure
**Input Type:** [[cat-multi-value]]  
**Shorthand:** `#cat-multi-value`  
**Format:**
```
| Product    | Q1_Sales | Q2_Sales | Q3_Sales |
|------------|----------|----------|----------|
| Product A  | 100,000  | 120,000  | 110,000  |
| Product B  | 85,000   | 90,000   | 105,000  |
| Product C  | 60,000   | 55,000   | 70,000   |
```

## Why This Chart Type
- **Compares categories across multiple measures**
- Good for ranking and side-by-side comparison
- Works well when comparing performance metrics across periods
- Easy to identify leaders and laggards

## Configuration
- **X-axis (Rows):** Product categories (nominal, unordered)
- **Y-axis (Values):** Sales amounts (numeric)
- **Grouping:** By quarter (multiple series)
- **Color encoding:** One color per quarter/series
- **Ordering:** Sort by total or latest period descending

## Variations
- **Horizontal bar:** Better for long category labels
- **Stacked bar:** If showing parts-of-whole (e.g., revenue breakdown)
- **100% stacked bar:** If showing proportional mix
- **Lollipop chart:** Modern alternative, better for sparse data

## Tools
- Excel: Insert > Clustered Column/Bar
- Tableau: Drag category to Rows, metric to Columns, quarter to Color
- Power BI: Clustered Bar visual with legend
- Matplotlib: `plt.bar()` with grouped positioning

## Related Charts
- [[cat-value|Simple Bar Chart]] (single metric)
- [[composition|Stacked Bar 100%]] (if showing proportion of whole)
- [[demo-grouped|Demographic/Grouped]] (if comparing subcategories)

---
```

## Example 3: Customer Age Distribution Heatmap

```markdown
---
title: Customer Demographics Heatmap
chart_type: Heatmap
data_input_type: demo-grouped
tags: [demo-grouped, heatmap, demographics, customer-segmentation]
use_cases: [segmentation, market-analysis, audience-profiling]
created: 2026-06-23
---

# Customer Demographics Heatmap

## Data Structure
**Input Type:** [[demo-grouped]]  
**Shorthand:** `#demo-grouped`  
**Format:**
```
| Age Group | Female | Male  |
|-----------|--------|-------|
| 18-25     | 340    | 450   |
| 25-35     | 580    | 620   |
| 35-50     | 720    | 650   |
| 50+       | 420    | 380   |
```

## Why This Chart Type
- **Shows intersections of two categorical dimensions**
- Color intensity reveals patterns across groups
- Good for density/concentration analysis
- Excellent for identifying clusters or outliers

## Configuration
- **Rows:** Primary category (Age Group)
- **Columns:** Subcategory (Gender)
- **Cell values:** Numeric (customer count)
- **Color scale:** Sequential or diverging depending on context
- **Annotations:** Show actual values in cells

## Variations
- **Annotation heatmap:** With percentages or ratios
- **Normalized heatmap:** If comparing across different scales
- **Diverging heatmap:** If showing positive/negative variance
- **Treemap:** Alternative for hierarchical categories

## Tools
- Excel: Conditional formatting on pivot table
- Tableau: Heatmap mark type with dimensions on Rows/Columns
- Power BI: Matrix visual with conditional formatting
- Seaborn: `sns.heatmap()` with Pandas DataFrame

## Insights Enabled
- Which demographic segments have highest/lowest counts
- Patterns of concentration (e.g., gender skew by age)
- Underrepresented or overrepresented groups

## Related Charts
- [[cat-multi-value|Grouped Bar Chart]] (alternative layout)
- [[hierarchical-cat|Treemap]] (for 3+ hierarchical levels)
- [[matrix|Confusion Matrix]] (if categorical outputs)

---
```

## Example 4: Portfolio Risk-Return Bubble Chart

```markdown
---
title: Investment Portfolio Risk-Return
chart_type: Bubble Chart
data_input_type: xyz-trivariate
tags: [xyz-trivariate, bubble-chart, financial, risk-analysis]
use_cases: [portfolio-optimization, investment-analysis, asset-allocation]
created: 2026-06-23
---

# Investment Portfolio Risk-Return

## Data Structure
**Input Type:** [[xyz-trivariate]]  
**Shorthand:** `#xyz-trivariate`  
**Format:**
```
| Asset        | Risk (Std Dev) | Return (%) | Allocation ($M) |
|--------------|----------------|------------|-----------------|
| US Stocks    | 12             | 8.5        | 150             |
| Bonds        | 4              | 3.2        | 200             |
| Real Estate  | 15             | 10         | 100             |
| Commodities  | 18             | 6          | 50              |
```

## Why This Chart Type
- **Displays three dimensions simultaneously:**
  - X-axis: Risk (horizontal position)
  - Y-axis: Return (vertical position)
  - Bubble size: Portfolio allocation amount
- Reveals trade-offs between risk and return
- Bubble size adds third metric efficiently
- Better than separate scatter plots for multidimensional comparison

## Configuration
- **X-axis:** Risk metric (standard deviation, volatility)
- **Y-axis:** Return metric (percentage, absolute)
- **Bubble size:** Portfolio weight, allocation, or importance
- **Color:** Asset class or region
- **Labels:** Asset names or ticker symbols

## Variations
- **Sized scatter plot:** If only showing relative sizes, no bubble style
- **3D scatter:** If literal 3D representation needed (rarely better)
- **Small multiples:** If comparing multiple portfolios

## Tools
- Excel: XY Scatter + add bubble size series
- Tableau: Bubble mark type with X, Y, Size, and Color encodings
- Power BI: Scatter chart with custom size field
- D3.js: `d3-force` for positioning or `d3.pack()` for packing

## Key Insights
- Identify efficient frontier (highest return for risk level)
- Spot outliers (high risk with low return)
- Assess diversification (bubble spread)
- Evaluate concentration (dominant bubble sizes)

## Related Charts
- [[bivariate-simple|Scatter Plot]] (without third dimension)
- [[bivariate-dual|Dual-Axis Chart]] (if comparing two metrics)
- [[hierarchical-cat|Treemap]] (if showing nested allocations)

---
```

## Example 5: Website Traffic Heatmap by Day/Hour

```markdown
---
title: Site Traffic Patterns (Day × Hour)
chart_type: Calendar Heatmap / Matrix Heatmap
data_input_type: matrix-grid
tags: [matrix-grid, heatmap, time-patterns, web-analytics]
use_cases: [traffic-analysis, anomaly-detection, scheduling]
created: 2026-06-23
---

# Website Traffic Patterns

## Data Structure
**Input Type:** [[matrix-grid]]  
**Shorthand:** `#matrix-grid`  
**Format (2D Grid):**
```
|      | 00:00 | 06:00 | 12:00 | 18:00 |
|------|-------|-------|-------|-------|
| Mon  | 320   | 450   | 2100  | 1850  |
| Tue  | 340   | 520   | 2250  | 1920  |
| Wed  | 380   | 610   | 2480  | 2150  |
| Thu  | 420   | 650   | 2680  | 2280  |
```

## Why This Chart Type
- **Reveals patterns in two categorical dimensions**
- Day of week + hour of day creates matrix structure
- Color intensity immediately shows traffic peaks
- Enables "at a glance" pattern recognition

## Configuration
- **Rows:** Days of week (Mon-Sun)
- **Columns:** Hours of day (0-23)
- **Cell values:** Traffic count / pageviews
- **Color scale:** Sequential (low=light, high=dark)
- **Cell annotations:** Show actual values

## Variations
- **Calendar heatmap:** If using actual dates (2D calendar view)
- **Interactive tooltip:** On hover show details
- **Normalized heatmap:** If comparing across different scales
- **Diverging heatmap:** If comparing to baseline/average

## Insights Enabled
- **Peak hours:** When traffic surges (lunch hours, evenings)
- **Low-traffic zones:** When to schedule maintenance
- **Day patterns:** Weekday vs. weekend behavior
- **Anomalies:** Unexpected traffic spikes

## Tools
- Excel: Pivot table + conditional formatting
- Tableau: Heatmap mark type with Day/Hour dimensions
- Power BI: Matrix visual with conditional formatting
- Plotly: `heatmap()` with custom colorscale
- Matplotlib: `imshow()` with Pandas crosstab

## Related Charts
- [[time-series|Line Chart]] (if emphasizing continuous time trend)
- [[demo-grouped|Grouped Bar]] (if showing day or hour separately)
- [[event-time|Calendar Heatmap]] (if tracking specific events)

---
```

---

## File Organization in Obsidian

```
CHARTS/
├── Temporal/
│   ├── 01 - Sales Trend Line Chart.md
│   ├── 02 - Traffic Over Time.md
│   └── 03 - Historical Comparison.md
│
├── Comparison/
│   ├── 01 - Product Mix Bar Chart.md
│   ├── 02 - Regional Performance.md
│   └── 03 - Competitor Benchmark.md
│
├── Distribution/
│   ├── 01 - Customer Demographics Heatmap.md
│   ├── 02 - Demographic Segments.md
│   └── 03 - Market Penetration.md
│
├── Relationship/
│   ├── 01 - Portfolio Risk-Return Bubble.md
│   ├── 02 - Correlation Scatter.md
│   └── 03 - Feature Importance.md
│
├── Composition/
│   ├── 01 - Budget Breakdown Pie.md
│   ├── 02 - Revenue Mix Stack.md
│   └── 03 - Market Share.md
│
└── _INDICES/
    ├── By Data Input Type.md (linked index)
    ├── By Chart Type.md (linked index)
    └── By Use Case.md (linked index)
```

## Obsidian Queries to Build Index Files

**By Data Input Type:**
```
LIST WHERE contains(tags, "#time-series") OR contains(tags, "#xy-simple")
GROUP BY data_input_type
SORT BY data_input_type
```

**By Chart Type:**
```
LIST WHERE file.frontmatter.chart_type
GROUP BY chart_type
SORT BY chart_type ASC
```

**By Use Case:**
```
LIST WHERE contains(use_cases, "comparison")
GROUP BY use_cases
```

---

## Front Matter Fields to Use

```yaml
---
title: [Chart Name]
chart_type: [Line, Bar, Pie, Heatmap, Bubble, etc.]
data_input_type: [xy-simple, time-series, cat-multi-value, etc.]
tags: [input-type-tag, chart-type-tag, domain-tag, use-case-tag]
use_cases: [use-case-1, use-case-2, use-case-3]
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
tools: [Excel, Tableau, Power BI, D3.js, etc.]
complexity: [Basic, Intermediate, Advanced]
audience: [Executive, Analytics, Technical]
---
```

---

**Template Version:** 1.0  
**Last Updated:** 2026-06-23  
**Purpose:** Standardized chart documentation for Obsidian vault

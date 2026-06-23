# Index: Charts by Tool (Verified Implementations)

Status: all entries are `stub` until library-curator marks them `verified` after a successful render.

---

## matplotlib

All common chart types supported natively or via seaborn/scipy.

**Native matplotlib:**
- Bar, Horizontal Bar, Grouped Bar, Stacked Bar → `barh`, `bar` + `bottom`
- Line, Area, Stacked Area → `plot`, `fill_between`, `stackplot`
- Scatter → `scatter`
- Histogram → `hist`
- Box Plot → `boxplot`
- Pie, Donut → `pie` + `wedgeprops={'width': ...}`
- Error Bars → `errorbar`
- Candlestick → via `mplfinance`
- Waterfall → manual bar + bottom calculation
- Heatmap → `imshow` or `pcolormesh`
- Violin → `violinplot`

**Via seaborn:**
- Violin → `sns.violinplot`
- Box → `sns.boxplot`
- Strip/Jitter → `sns.stripplot`
- Beeswarm → `sns.swarmplot`
- Regression Scatter → `sns.regplot`

## plotly

Excellent for interactive charts. Use `plotly.graph_objects` or `plotly.express`.

**plotly.express shortcuts:**
- Bar → `px.bar`
- Line → `px.line`
- Scatter → `px.scatter`
- Area → `px.area`
- Box → `px.box`
- Violin → `px.violin`
- Histogram → `px.histogram`
- Pie, Donut → `px.pie`
- Treemap → `px.treemap`
- Sunburst → `px.sunburst`
- Choropleth → `px.choropleth`
- Bubble Map → `px.scatter_geo`
- Parallel Coordinates → `px.parallel_coordinates`
- Sankey → `go.Sankey`
- Funnel → `px.funnel`

## altair / vega-lite

Declarative grammar. Mark + encoding channels.

- Bar → `mark_bar()` + `x=alt.X('cat'), y=alt.Y('val')`
- Line → `mark_line()`
- Area → `mark_area()`
- Scatter → `mark_point()`
- Histogram → `mark_bar()` + `x=alt.X(bin=True)`
- Box → `mark_boxplot()`
- Heatmap → `mark_rect()` + `color=`
- Geospatial → `mark_geoshape()` + topojson

## d3

Full custom control. Use for: network, custom Sankey, interactive dashboards, geographic projections.

## tableau

All standard charts via Show Me panel or manual drag-and-drop.

## powerbi

Standard charts in Visualizations pane. Custom visuals via AppSource for: Sankey, Chord, Radar, etc.

## excel

Most common charts via Insert → Charts. Treemap, Sunburst, Funnel, Waterfall via Insert → Hierarchy/Waterfall.

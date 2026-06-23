# Index: Charts by Data Input Type

Auto-maintained by library-curator. Add entries as library grows.

---

## xy-simple — [numeric, numeric]
Simple bivariate: two numeric columns, no explicit time.
- Scatter Plot → `Relationship/scatter-plot.md`
- Connected Scatter Plot → `Relationship/connected-scatter-plot.md`
- Line Chart (no time axis) → `Temporal/line-chart.md`

## xy-dual-series — [num/cat, num, num]
Two numeric series against a shared axis.
- Multi-Line Chart → `Temporal/line-chart.md`
- Grouped Bar Chart → `Comparison/grouped-bar-chart.md`
- Dumbbell Plot → `Comparison/dumbbell-plot.md`

## xyz-trivariate — [num, num, num]
Three numeric columns.
- Bubble Chart → `Relationship/bubble-chart.md`
- 3D Scatter Plot → `Relationship/3d-scatter-plot.md`
- Contour Plot → `Distribution/contour-plot.md`

## cat-value — [categorical, numeric]
One category column, one numeric value.
- Bar Chart → `Comparison/bar-chart.md`
- Horizontal Bar Chart → `Comparison/horizontal-bar-chart.md`
- Pie Chart → `Composition/pie-chart.md`
- Donut Chart → `Composition/donut-chart.md`
- Lollipop Chart → `Comparison/lollipop-chart.md`
- Dot Plot → `Comparison/dot-plot.md`
- Waffle Chart → `Composition/waffle-chart.md`
- Circular Bar Chart → `Comparison/circular-bar-chart.md`

## cat-multi-value — [categorical, num, num...]
One category, multiple numeric values.
- Grouped Bar Chart → `Comparison/grouped-bar-chart.md`
- Stacked Bar Chart → `Composition/stacked-bar-chart.md`
- Stacked Bar 100% → `Composition/stacked-bar-100pct.md`
- Radar Chart → `Specialized/radar-chart.md`
- Parallel Coordinates → `Relationship/parallel-coordinates.md`
- Heat Map → `Distribution/heat-map.md`

## time-series — [datetime, num...]
Date/time column + one or more numeric values.
- Line Chart → `Temporal/line-chart.md`
- Area Chart → `Temporal/area-chart.md`
- Stacked Area Chart → `Temporal/stacked-area-chart.md`
- Stream Graph → `Temporal/stream-graph.md`
- Sparkline → `Temporal/sparkline.md`
- Bump Chart → `Temporal/bump-chart.md`
- Slope Chart → `Temporal/slope-chart.md`
- Fan Chart → `Temporal/fan-chart-time-series.md`
- Candlestick Chart → `Temporal/candlestick-chart.md`
- Gantt Chart → `Specialized/gantt-chart.md`

## interval-range — [cat, num, num] to [cat, num×4]
Min/max or OHLC ranges.
- Box Plot → `Distribution/box-plot.md`
- Candlestick Chart → `Temporal/candlestick-chart.md`
- Column Range → `Comparison/column-range.md`
- Error Bars → `Comparison/error-bars.md`
- Span Chart → `Comparison/span-chart.md`
- Bullet Graph → `Comparison/bullet-graph.md`

## demo-grouped — [cat, cat, num...]
Two categorical dimensions + numeric value.
- Grouped Bar Chart → `Comparison/grouped-bar-chart.md`
- Stacked Bar Chart → `Composition/stacked-bar-chart.md`
- Heat Map → `Distribution/heat-map.md`
- Population Pyramid → `Comparison/population-pyramid.md`
- Butterfly Chart → `Comparison/butterfly-chart.md`
- Marimekko Chart → `Composition/marimekko-chart.md`

## composition — [cat, num...] summing to 100%
Parts that add to a whole.
- Pie Chart → `Composition/pie-chart.md`
- Donut Chart → `Composition/donut-chart.md`
- Stacked Bar 100% → `Composition/stacked-bar-100pct.md`
- Treemap → `Composition/treemap.md`
- Sunburst Diagram → `Composition/sunburst-diagram.md`
- Waffle Chart → `Composition/waffle-chart.md`
- Marimekko Chart → `Composition/marimekko-chart.md`

## hierarchical-cat — [num/ordered, cat, cat, cat...]
Nested categorical hierarchy with values.
- Treemap → `Composition/treemap.md`
- Sunburst Diagram → `Composition/sunburst-diagram.md`
- Packed Circle Chart → `Composition/packed-circle-chart.md`
- Dendrogram → `Specialized/dendrogram.md`
- Partition Chart → `Composition/partition-chart.md`

## matrix-grid — 2D grid: row-cat × col-cat → value
Two categorical axes, one value per cell.
- Heat Map → `Distribution/heat-map.md`
- Correlation Matrix → `Relationship/correlation-matrix.md`
- Mosaic Plot → `Composition/marimekko-chart.md`
- Chord Diagram → `Composition/chord-diagram.md`
- Matrix Diagram → `Relationship/matrix-diagram.md`

## event-time — [categorical, datetime]
Events with timestamps.
- Timeline → `Temporal/timeline.md`
- Gantt Chart → `Specialized/gantt-chart.md`
- Bubble Timeline → `Temporal/bubble-timeline.md`

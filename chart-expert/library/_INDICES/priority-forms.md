# Verification priority — chart forms used by decision-analytics-reconstruction

This list drives the order in which library entries are verified per the
protocol in `chart-expert/references/verification-protocol.md`. Matplotlib
first for every form (the target repo's canonical pipeline is matplotlib),
then plotly (its dashboard/explorer surfaces).

1. bar chart (vertical)
2. horizontal bar chart
3. grouped bar chart
4. histogram
5. density / KDE plot
6. violin plot
7. box plot
8. scatter plot
9. line chart
10. area / band chart (fill_between interval bands)
11. heatmap (matrix)
12. choropleth map
13. PCA biplot / annotated scatter
14. small multiples (faceted panels)
15. table (as an exhibit form)

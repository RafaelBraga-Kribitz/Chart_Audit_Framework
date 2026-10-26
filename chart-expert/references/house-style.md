# House style — the Braga design system v2.1

Load this whenever the target repository belongs to Rafael Braga-Kribitz (any
`github.com/RafaelBraga-Kribitz/*` checkout) or declares `bk-viz` as a dependency.
The library's chart specs say *which* chart and *how to build it*; this file
says how every chart in the owner's portfolio *looks*. Where a library snippet
hard-codes a colour (`#4477AA`, `#d3d3d3`, …), this file wins.

Source of truth: braga-portfolio-v2
[`design-system/DECISIONS.md`](https://github.com/RafaelBraga-Kribitz/braga-portfolio-v2/blob/main/design-system/DECISIONS.md)
(D-015–D-018, D-033, D-036, D-053) and its `tokens.json`. The implementation is
[`bk-viz`](https://github.com/RafaelBraga-Kribitz/bk-viz) ≥ 2.0.0; never copy a
hex value from either into chart code.

## Implement (chart-expert)

1. Declare `bk-viz` (`bk-viz @ git+https://github.com/RafaelBraga-Kribitz/bk-viz@fe8125a3043f49a798ef24740b23f81c46863562`, the 2.0.0 merge commit; `@v2.0.0` once that tag is pushed)
   and call `bk.apply("light")` (or `"dark"`) before plotting.
2. Colours only through roles: `bk.c("sc-ac")` actual, `bk.c("sc-py")` previous
   year, `bk.c("sc-pl")` plan (outline), `bk.variance_color(delta)` for
   variances, `bk.palette("categorical", n)` for unordered series (six or more:
   the rest are `bk.c("cat-other")`), `bk.palette("seq" | "div" | "two" | …)`
   for scales, `bk.highlight_palette(labels, highlight=…)` for the one mark that
   earned the accent.
3. One highlight per chart (`hl`, the ultramarine accent). Two highlights read
   as none.
4. Colour lives in marks, never in type: labels in `ink` / `ink-2`
   (`bk.direct_label`, `bk.value_labels`). A bad variance label carries ▲
   (`bk.variance_label`). The only coloured text is the one earned KPI figure.
5. Finding as the title (`bk.finding_title`), provenance under the chart
   (`bk.footer`), direct labels instead of a legend where possible.
6. Save with `bk.save(fig, path)` (PNG + SVG); no text below 12px.

## Audit (chart-audit, Layer 9 — Visual Integrity)

For a chart in the owner's portfolio, each item below is a finding when it fails.
They are presentation findings: they never outrank Layers 1–8 (upstream first).

| Check | Fails when |
|---|---|
| Theme applied | the generator does not import `bk_theme` / call `bk.apply()`; the surface is white or `#E6E6E6` (v1) |
| No v1 palette | orange `#FA6400`, moment blue `#5B7FFF`, or a Söhne font name appears in the generator or the figure |
| One highlight | more than one mark in the accent; the accent used for anything but the earned mark |
| IBCS roles | variance coloured by anything but `var-pos` / `var-neg`; a bad variance without ▲; plan drawn solid |
| Colour in type | a label, tick or title in a hue (other than the one earned KPI figure); `mid` grey used for text |
| Categorical order | hues out of slot order, or six-plus series without `cat-other` |
| Type | not BKribitz / BKribitz Mono; any text below 12px |
| Provenance | no `bk.footer` (source, run, epistemic tag) on a published figure |

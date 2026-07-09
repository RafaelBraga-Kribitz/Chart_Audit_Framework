"""Verified matplotlib implementation — bar chart (vertical).

Proof-case snippet for chart-expert/library/CHARTS/Comparison/bar-chart.md
per chart-expert/references/verification-protocol.md: inline fixture,
generalized column names, self-contained, saves a PNG whose non-emptiness is
the render proof. Output path is taken from argv[1] (defaults to a temp
file) so the snippet never writes into the repository.
"""

import sys
import tempfile

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Inline fixture: one categorical column, one value column.
categories = ["North", "South", "East", "West", "Central"]
values = [42, 31, 55, 24, 38]

out_path = sys.argv[1] if len(sys.argv) > 1 else tempfile.mktemp(suffix=".png")

fig, ax = plt.subplots(figsize=(6, 4))
# Sort by value (library best practice: rank categories by magnitude).
order = sorted(range(len(values)), key=lambda i: values[i], reverse=True)
cats_sorted = [categories[i] for i in order]
vals_sorted = [values[i] for i in order]

bars = ax.bar(cats_sorted, vals_sorted, color="#4477AA")
ax.bar_label(bars, padding=2)  # direct labels beat a legend for one series
ax.set_ylim(0, max(vals_sorted) * 1.15)  # zero baseline, headroom for labels
ax.set_ylabel("Value")
ax.set_title("Bar chart — verification fixture")
ax.spines[["top", "right"]].set_visible(False)

fig.tight_layout()
fig.savefig(out_path, dpi=100)
print(out_path)

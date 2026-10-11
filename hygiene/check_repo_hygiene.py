#!/usr/bin/env python3
"""Re-runnable IMP-F04 hygiene check over the tracked tree.

Invariants (spec: improvement_plan/IMP-F04_repo-hygiene.md):
  1. No byte-identical duplicate files, except groups that lie entirely inside
     the scraped site mirrors (third-party archives whose pages link to their
     own copies; exempted by the 2026-10-11 spec amendment).
  2. The superseded trees OLD-chart-audit/ and _legacy/ are gone, and the two
     design-history documents live under docs/design-history/.
  3. The single-sourced references exist exactly once.
  4. No binary alias files and no scraped WordPress plugin/theme assets.

Exit 0 when every invariant holds, 1 otherwise. Stdlib only.
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIRROR_ROOT = "Deterministic_Data_Visualization_Framework/references/"
SITE_MIRRORS = (
    "chartmaker.visualisingdata.com",
    "datavizcatalogue.com",
    "datavizproject.com",
    "depictdatastudio.com",
    "www.data-to-viz.com",
)
REMOVED_TREES = ("OLD-chart-audit/", "_legacy/")
DESIGN_HISTORY = ("docs/design-history/GPT Chart Audit Mode.md", "docs/design-history/Reverse_order.md")
SINGLE_SOURCED = ("input-type-schema.md", "input-type-inventory.md")
BANNED_FRAGMENTS = ("wp-content/plugins/", "wp-content/themes/")


def tracked_files() -> list[str]:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
    return [f for f in out.decode().split("\0") if f and (ROOT / f).is_file()]


def in_site_mirror(path: str) -> bool:
    return any(path.startswith(f"{MIRROR_ROOT}{site}/") for site in SITE_MIRRORS)


def duplicate_problems(files: list[str]) -> list[str]:
    groups: dict[str, list[str]] = defaultdict(list)
    for f in files:
        groups[hashlib.sha256((ROOT / f).read_bytes()).hexdigest()].append(f)
    return [
        "duplicate: " + ", ".join(paths)
        for paths in groups.values()
        if len(paths) > 1 and not all(in_site_mirror(p) for p in paths)
    ]


def tree_problems(files: list[str]) -> list[str]:
    problems = [f"superseded tree still tracked: {t}" for t in REMOVED_TREES if any(f.startswith(t) for f in files)]
    problems += [f"design-history document missing: {d}" for d in DESIGN_HISTORY if d not in files]
    for name in SINGLE_SOURCED:
        copies = [f for f in files if Path(f).name == name]
        if copies != [f"chart-expert/references/{name}"]:
            problems.append(f"{name} must exist once under chart-expert/references/, found: {copies}")
    problems += [f"binary alias file: {f}" for f in files if Path(f).name.endswith(" alias")]
    problems += [f"scraped plugin/theme asset: {f}" for f in files if any(b in f for b in BANNED_FRAGMENTS)]
    return problems


def main() -> int:
    files = tracked_files()
    problems = duplicate_problems(files) + tree_problems(files)
    for p in problems:
        print(f"[FAIL] {p}")
    if problems:
        print(f"[FAIL] repo hygiene: {len(problems)} problem(s)")
        return 1
    print(f"[PASS] repo hygiene: {len(files)} tracked files, no duplicates outside the site mirrors")
    return 0


if __name__ == "__main__":
    sys.exit(main())

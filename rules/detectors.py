# -*- coding: utf-8 -*-
"""Deterministic detectors for the mechanically checkable code smells (IMP-F01).

Implements the signatures in ``rules/detectors_spec.md``. Every detector
returns a ``Finding``; an input problem raises ``DetectorInputError`` (exit 2
at the CLI) and is never reported as "no smell". Stdlib only.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import asdict, dataclass
from statistics import pstdev
from typing import Iterable, Mapping, Sequence


class DetectorInputError(ValueError):
    """The detector could not run on these inputs (exit code 2)."""


@dataclass(frozen=True)
class Finding:
    smell: str
    fired: bool
    evidence: str
    inputs_digest: str

    def as_dict(self) -> dict:
        return asdict(self)


def _digest(payload: object) -> str:
    blob = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:16]


# ── Smell B ──────────────────────────────────────────────────────────────────


def detect_flat_distribution(
    rows: Sequence[Mapping[str, object]],
    group_col: str,
    metric_col: str,
    std_threshold: float = 1e-9,
) -> Finding:
    """Fire when every group (of >= 2 groups) has metric std below the threshold.

    ``rows`` is a table as a sequence of mappings (e.g. ``csv.DictReader``).
    Single-row groups are listed in the evidence but cannot fire the smell.
    """
    if not rows:
        raise DetectorInputError("empty frame")
    missing = [c for c in (group_col, metric_col) if c not in rows[0]]
    if missing:
        raise DetectorInputError(f"missing column(s): {missing}")
    groups: dict[str, list[float]] = {}
    for i, row in enumerate(rows):
        try:
            value = float(row[metric_col])  # type: ignore[arg-type]
        except (TypeError, ValueError) as exc:
            raise DetectorInputError(f"non-numeric {metric_col!r} at row {i}: {row[metric_col]!r}") from exc
        if math.isnan(value):
            raise DetectorInputError(f"NaN {metric_col!r} at row {i}")
        groups.setdefault(str(row[group_col]), []).append(value)
    stds = {g: pstdev(v) if len(v) > 1 else None for g, v in sorted(groups.items())}
    multi = {g: s for g, s in stds.items() if s is not None}
    singletons = sorted(g for g, s in stds.items() if s is None)
    fired = len(groups) >= 2 and bool(multi) and all(s < std_threshold for s in multi.values())
    shown = ", ".join(f"{g}={s:.3g}" for g, s in multi.items())
    evidence = f"std per group: {shown or 'none'}"
    if singletons:
        evidence += f"; single-row groups (not counted): {singletons}"
    if fired:
        evidence = f"all {len(multi)} multi-row groups have std < {std_threshold:g}; " + evidence
    return Finding("B", fired, evidence, _digest([group_col, metric_col, std_threshold, groups]))


# ── Smell C ──────────────────────────────────────────────────────────────────

_LEVEL = re.compile(r"(\d+(?:\.\d+)?)\s*%")
_HDI = re.compile(r"\b(HDI|HPDI|highest[- ]density)\b", re.IGNORECASE)


def detect_interval_mislabel(
    declared_label: str,
    computed_low: float,
    computed_high: float,
    quantile_low: float,
    quantile_high: float,
    level_tolerance: float = 0.005,
) -> Finding:
    """Fire when the label's interval type or level disagrees with the computation.

    Symmetric quantiles (``quantile_low + quantile_high == 1``) are an
    equal-tailed interval, so an "HDI" label fires; and the implied level
    ``quantile_high - quantile_low`` must match the labelled percentage.
    """
    match = _LEVEL.search(declared_label or "")
    if match is None:
        raise DetectorInputError(f"no percentage in label {declared_label!r}")
    if not (0.0 < quantile_low < 1.0 and 0.0 < quantile_high < 1.0) or quantile_low >= quantile_high:
        raise DetectorInputError(f"quantiles must satisfy 0 < low < high < 1, got {quantile_low}, {quantile_high}")
    if computed_low > computed_high:
        raise DetectorInputError(f"computed_low {computed_low} > computed_high {computed_high}")
    labelled = float(match.group(1)) / 100.0
    implied = quantile_high - quantile_low
    problems = []
    if _HDI.search(declared_label) and abs(quantile_low + quantile_high - 1.0) <= level_tolerance:
        problems.append(f"labelled HDI but computed as equal-tailed quantiles {quantile_low:g}/{quantile_high:g}")
    if abs(implied - labelled) > level_tolerance:
        problems.append(f"labelled {labelled:.1%} but quantiles imply {implied:.1%}")
    evidence = "; ".join(problems) if problems else (
        f"label {declared_label!r} matches {quantile_low:g}/{quantile_high:g} ({implied:.1%})"
    )
    digest = _digest([declared_label, computed_low, computed_high, quantile_low, quantile_high, level_tolerance])
    return Finding("C", bool(problems), evidence, digest)


# ── Smell J ──────────────────────────────────────────────────────────────────


def detect_dropped_categories(
    expected_categories: Iterable[str], plotted_categories: Iterable[str]
) -> Finding:
    """Fire when any expected category is absent from the plotted categories."""
    expected, plotted = set(expected_categories), set(plotted_categories)
    if not expected:
        raise DetectorInputError("empty expected_categories: no contract to check against")
    missing, extra = sorted(expected - plotted), sorted(plotted - expected)
    evidence = f"dropped: {missing}" if missing else f"all {len(expected)} expected categories plotted"
    if extra:
        evidence += f"; warning, unexpected plotted categories: {extra}"
    return Finding("J", bool(missing), evidence, _digest([sorted(expected), sorted(plotted)]))


DETECTORS = {
    "detect_flat_distribution": detect_flat_distribution,
    "detect_interval_mislabel": detect_interval_mislabel,
    "detect_dropped_categories": detect_dropped_categories,
}

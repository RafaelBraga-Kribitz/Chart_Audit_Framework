# -*- coding: utf-8 -*-
"""Tests for the deterministic rule layer (IMP-F01): python -m unittest discover rules"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import chart_audit_rules as cli  # noqa: E402
from detectors import (  # noqa: E402
    DetectorInputError,
    detect_dropped_categories,
    detect_flat_distribution,
    detect_interval_mislabel,
)


class FlatDistribution(unittest.TestCase):
    def test_fires_when_every_group_is_constant(self) -> None:
        rows = [{"g": "a", "m": "1"}, {"g": "a", "m": "1"}, {"g": "b", "m": "2"}, {"g": "b", "m": "2"}]
        self.assertTrue(detect_flat_distribution(rows, "g", "m").fired)

    def test_clean_when_any_group_varies(self) -> None:
        rows = [{"g": "a", "m": "1"}, {"g": "a", "m": "1"}, {"g": "b", "m": "2"}, {"g": "b", "m": "5"}]
        self.assertFalse(detect_flat_distribution(rows, "g", "m").fired)

    def test_single_row_groups_do_not_fire(self) -> None:
        rows = [{"g": "a", "m": "1"}, {"g": "b", "m": "2"}]
        f = detect_flat_distribution(rows, "g", "m")
        self.assertFalse(f.fired)
        self.assertIn("single-row groups", f.evidence)

    def test_one_group_cannot_fire(self) -> None:
        self.assertFalse(detect_flat_distribution([{"g": "a", "m": "1"}] * 3, "g", "m").fired)

    def test_input_errors(self) -> None:
        for rows, g, m in (([], "g", "m"), ([{"g": "a", "m": "1"}], "x", "m"), ([{"g": "a", "m": "z"}], "g", "m")):
            with self.assertRaises(DetectorInputError):
                detect_flat_distribution(rows, g, m)

    def test_deterministic_digest(self) -> None:
        rows = [{"g": "a", "m": "1"}, {"g": "a", "m": "2"}]
        self.assertEqual(
            detect_flat_distribution(rows, "g", "m").inputs_digest,
            detect_flat_distribution(list(rows), "g", "m").inputs_digest,
        )


class IntervalMislabel(unittest.TestCase):
    def test_equal_tailed_labelled_hdi_fires(self) -> None:
        f = detect_interval_mislabel("94% HDI", -1.0, 1.0, 0.03, 0.97)
        self.assertTrue(f.fired)
        self.assertIn("equal-tailed", f.evidence)

    def test_level_mismatch_fires(self) -> None:
        f = detect_interval_mislabel("95% interval", -1.0, 1.0, 0.03, 0.97)
        self.assertTrue(f.fired)
        self.assertIn("94.0%", f.evidence)

    def test_consistent_percentile_label_is_clean(self) -> None:
        self.assertFalse(detect_interval_mislabel("90% equal-tailed interval", -1.0, 1.0, 0.05, 0.95).fired)

    def test_input_errors(self) -> None:
        bad = (
            ("HDI", -1, 1, 0.05, 0.95),  # no percentage
            ("90%", 1, -1, 0.05, 0.95),  # low > high
            ("90%", -1, 1, 0.0, 0.95),  # quantile outside (0, 1)
            ("90%", -1, 1, 0.9, 0.1),  # quantiles reversed
        )
        for args in bad:
            with self.assertRaises(DetectorInputError):
                detect_interval_mislabel(*args)


class DroppedCategories(unittest.TestCase):
    def test_fires_and_names_missing(self) -> None:
        f = detect_dropped_categories({"A", "B", "C"}, {"A", "B"})
        self.assertTrue(f.fired)
        self.assertIn("'C'", f.evidence)

    def test_extra_categories_warn_without_firing(self) -> None:
        f = detect_dropped_categories({"A"}, {"A", "Z"})
        self.assertFalse(f.fired)
        self.assertIn("warning", f.evidence)

    def test_empty_expectation_is_an_error(self) -> None:
        with self.assertRaises(DetectorInputError):
            detect_dropped_categories(set(), {"A"})


class Cli(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.chart = self.tmp / "chart.png"
        self.chart.write_bytes(b"")

    def _write(self, name: str, text: str) -> str:
        path = self.tmp / name
        path.write_text(text, encoding="utf-8")
        return str(path)

    def _run(self, *extra: str) -> int:
        return cli.main([str(self.chart), str(self.chart), *extra])

    def test_manifest_and_matrix_are_consistent(self) -> None:
        self.assertEqual(cli.main(["--check-manifest"]), 0)

    def test_all_skipped_is_exit_zero(self) -> None:
        self.assertEqual(self._run(), 0)

    def test_fired_detector_is_exit_one(self) -> None:
        exp, plot = self._write("e.txt", "A\nB\n"), self._write("p.txt", "A\n")
        self.assertEqual(self._run("--expected-categories", exp, "--plotted-categories", plot), 1)

    def test_clean_detector_is_exit_zero(self) -> None:
        exp, plot = self._write("e.txt", "A\nB\n"), self._write("p.txt", "A\nB\n")
        self.assertEqual(self._run("--expected-categories", exp, "--plotted-categories", plot), 0)

    def test_input_error_is_exit_two(self) -> None:
        data = self._write("d.csv", "g,m\na,1\n")
        self.assertEqual(self._run("--data", data, "--group-col", "nope", "--metric-col", "m"), 2)
        self.assertEqual(cli.main([str(self.tmp / "missing.png"), str(self.chart)]), 2)

    def test_unimplemented_detector_in_manifest_is_exit_two(self) -> None:
        manifest = self._write(
            "m.yaml",
            "rules:\n  - id: SMELL-X\n    enforcement: detector-backed\n"
            "    detector: {function: detect_nothing, spec: rules/detectors_spec.md}\n",
        )
        with self.assertRaises(cli.ManifestError):
            cli.load_manifest(Path(manifest))

    def test_matrix_drift_is_detected(self) -> None:
        rules = cli.load_manifest(cli.RULES / "manifest.yaml")
        drifted = self._write("matrix.md", "| SMELL-B | x | llm-judged-only | ref |\n")
        with self.assertRaises(cli.ManifestError):
            cli.check_coverage_matrix(rules, Path(drifted))


if __name__ == "__main__":
    unittest.main()

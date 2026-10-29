"""Independent witnesses and controls for the declared ideal helix model."""
import json
import math
from pathlib import Path
import unittest
from probes.dna_kakeya_calibrated_probe import (
    build_report, exact_covering_report, tangent_latitude_degrees,
    sample_helix_directions, line_angle,
)


class DNAGeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_committed_receipt_matches_regeneration(self):
        path = Path(__file__).resolve().parents[1] / "probes/dna_kakeya_calibrated_probe_out.json"
        def compare(expected, actual):
            if isinstance(expected, float):
                self.assertTrue(math.isclose(expected, actual, rel_tol=0., abs_tol=1e-11))
            elif isinstance(expected, dict):
                self.assertEqual(expected.keys(), actual.keys())
                for key in expected:
                    compare(expected[key], actual[key])
            elif isinstance(expected, list):
                self.assertEqual(len(expected), len(actual))
                for left, right in zip(expected, actual):
                    compare(left, right)
            else:
                self.assertEqual(expected, actual)
        compare(json.loads(path.read_text()), self.report)
        self.assertTrue(self.report["pass"])

    def test_axis_witness_matches_calibrated_radius(self):
        # For this A/B/Z model, Z has the closest tangent direction to the axis.
        directions = sample_helix_directions(radius=9., pitch=45.6, handedness=-1, sample_count=17)
        axial_gap = math.degrees(min(line_angle((0., 0., 1.), d) for d in directions))
        self.assertAlmostEqual(axial_gap, 51.11781468284084, places=11)
        self.assertGreater(axial_gap, self.report["reconciliation"]["sampled_grid_maximum_degrees"])

    def test_interior_gap_and_endpoint_controls(self):
        self.assertEqual(exact_covering_report([0., 90.])["covering_radius_degrees"], 45.)
        self.assertEqual(exact_covering_report([0.])["covering_radius_degrees"], 90.)
        self.assertEqual(exact_covering_report([90.])["covering_radius_degrees"], 90.)

    def test_invalid_calibration_cannot_produce_a_receipt(self):
        for values in ([], [math.nan], [math.inf], [91.]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                exact_covering_report(values)
        for radius, pitch in ((0., 1.), (1., math.nan), (math.inf, 1.)):
            with self.subTest(radius=radius, pitch=pitch), self.assertRaises(ValueError):
                tangent_latitude_degrees(radius, pitch)


if __name__ == "__main__":
    unittest.main()

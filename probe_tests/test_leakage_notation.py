"""Finite numeric migration checks; requires numpy/scipy, no safety claim."""
import unittest
import numpy as np
from l2c_probe import L2CProbe

class Hamiltonian:
    def matrix_restricted(self):
        return np.array([[0., 2.], [2., 3.]])

class LeakageNotationTest(unittest.TestCase):
    def test_noncommuting_projector_retains_numeric_behavior(self):
        probe = L2CProbe(Hamiltonian(), projector=np.diag([1., 0.]))
        report = probe.report()
        self.assertAlmostEqual(report.leakage_ell_H, 2.)
        self.assertEqual(report.leakage_h, report.leakage_ell_H)
        payload = report.as_dict()
        self.assertEqual(payload["leakage_ell_H"], 2.)
        self.assertNotIn("leakage_h", payload)
        expected = report.spectral_gap_delta / (report.spectral_gap_delta + 2. + probe.eps)
        self.assertAlmostEqual(report.beta_c, expected)

    def test_spectral_projector_zero_is_only_finite_leakage(self):
        report = L2CProbe(Hamiltonian(), max_rank=1).report()
        self.assertAlmostEqual(report.leakage_ell_H, 0.)
        self.assertNotIn("h_eval", report.as_dict())

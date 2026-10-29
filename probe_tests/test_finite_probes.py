"""Behavioral regressions for finite diagnostics; no evaluator calibration."""
import unittest
import numpy as np
from l2c_probe import L2CProbe
from examples.ipiano_probe import ipiano


class Hamiltonian:
    def __init__(self, matrix):
        self.matrix = matrix

    def matrix_restricted(self):
        return self.matrix


class FiniteProbeTests(unittest.TestCase):
    def test_equal_distance_rank_tie_prefers_positive_eigenvalue(self):
        p = L2CProbe(Hamiltonian(np.diag([-0.001, 0.001])), max_rank=1)
        np.testing.assert_allclose(p.protected_projector(), np.diag([0., 1.]))

    def test_normalized_protected_and_bulk_retention(self):
        p = L2CProbe(Hamiltonian(np.diag([0., 2.])), max_rank=1)
        self.assertAlmostEqual(p.love_squared([2., 0.], 1.), 1.)
        self.assertAlmostEqual(p.love_squared([0., 2.], 1.), 0.)

    def test_noncommuting_projector_has_time_dependent_retention(self):
        p = L2CProbe(Hamiltonian([[0., 1.], [1., 0.]]), projector=np.diag([1., 0.]))
        np.testing.assert_allclose(p.love_squared_curve([1., 0.], [0., np.pi/2]), [1., 0.], atol=1e-12)
        self.assertAlmostEqual(p.leakage_norm(), 1.)

    def test_invalid_hamiltonian_is_not_silently_replaced(self):
        for matrix in ([], [1., 2.], [[1., 2.]], [[0., 1.], [0., 0.]], [[np.nan]]):
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                L2CProbe(Hamiltonian(matrix))

    def test_invalid_projector_cannot_create_superunit_retention(self):
        for projector in (np.diag([2., 0.]), [[0., 1.], [0., 0.]], np.diag([np.nan, 0.])):
            with self.subTest(projector=projector), self.assertRaises(ValueError):
                L2CProbe(Hamiltonian(np.eye(2)), projector=projector)

    def test_invalid_rank_rejected(self):
        for rank in (-1, 1.5, 3, True):
            with self.subTest(rank=rank), self.assertRaises(ValueError):
                L2CProbe(Hamiltonian(np.eye(2)), max_rank=rank)

    def test_invalid_state_and_time_rejected(self):
        p = L2CProbe(Hamiltonian(np.eye(2)))
        for state, time in (([0., 0.], 0.), ([np.nan, 1.], 0.), ([1.], 0.), ([1., 0.], np.inf)):
            with self.subTest(state=state, time=time), self.assertRaises(ValueError):
                p.love_squared(state, time)

    def test_ipiano_reduces_to_known_quadratic_gradient_step(self):
        x, trace = ipiano(np.array([2.]), lambda x: x, lambda y, a: y,
                          lambda x: float(np.sum(x*x)/2), alpha=0.25,
                          beta_ipiano=0., iterations=2)
        np.testing.assert_allclose(x, [1.125])
        self.assertAlmostEqual(trace[-1].residual_norm, 1.125)

    def test_ipiano_rejects_invalid_parameters(self):
        cases = ({"alpha": np.nan}, {"alpha": np.inf}, {"iterations": -1},
                 {"iterations": 1.5}, {"beta_ipiano": np.nan})
        for kwargs in cases:
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                ipiano(np.ones(1), lambda x: x, lambda y, a: y, lambda x: 0., **kwargs)

    def test_ipiano_rejects_nonfinite_result(self):
        with self.assertRaises(FloatingPointError):
            ipiano(np.ones(1), lambda x: x, lambda y, a: y*np.nan, lambda x: 0.)


if __name__ == "__main__":
    unittest.main()

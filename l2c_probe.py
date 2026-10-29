"""L2C protected-sector Hamiltonian probe.

This module formalizes L²_C as protected-sector retention under Hamiltonian
flow. It is designed to operate on the Hamiltonian objects used in the HOT
lattice / DDTL probe lane, especially objects exposing matrix_restricted(),
unitary_restricted(), occupancy_statevector_restricted(), and
occupancy_fidelity().

Canonical definitions:

    L²_C(psi,t) = || P_C exp(-i t H_T) psi ||²
    ell_H           = || (I - P_C) H_T P_C ||
    beta_C      = Delta / (Delta + ell_H + eps)

This file is a finite-dimensional analytic probe. It does not assert a final
infinite-dimensional spectral identification with zeta zeros.
"""

from __future__ import annotations

from dataclasses import dataclass
from numbers import Integral
from typing import Any, Dict, Iterable, Optional, Tuple

import numpy as np
import scipy.linalg as la
import scipy.sparse as sparse


ArrayLike = Any


@dataclass(frozen=True)
class L2CReport:
    """Structured status output for an L²_C probe run."""

    dimension: int
    protected_rank: int
    leakage_ell_H: float
    spectral_gap_delta: float
    beta_c: float
    target_energy: float
    tolerance_delta: float

    @property
    def leakage_h(self) -> float:
        """Deprecated read alias for leakage_ell_H; never evaluator h_eval."""
        return self.leakage_ell_H

    def as_dict(self) -> Dict[str, float]:
        return {
            "dimension": float(self.dimension),
            "protected_rank": float(self.protected_rank),
            "leakage_ell_H": self.leakage_ell_H,
            "spectral_gap_delta": self.spectral_gap_delta,
            "beta_c": self.beta_c,
            "target_energy": self.target_energy,
            "tolerance_delta": self.tolerance_delta,
        }


class L2CProbe:
    """Compute finite L²_C metrics from a restricted Hamiltonian.

    Parameters
    ----------
    ham:
        Hamiltonian-like object. Must expose matrix_restricted(). Optional
        methods occupancy_statevector_restricted() and occupancy_fidelity()
        enable occupancy-native coherence metrics.
    target_energy:
        Energy around which the protected sector is chosen. HOT midgap modes
        typically use target_energy=0.
    delta:
        Spectral tolerance for selecting protected eigenvectors.
    eps:
        Numerical stabilizer in beta_C.
    projector:
        Optional user-supplied protected-sector projector. If supplied, it
        overrides target_energy/delta selection for P_C but the spectrum is
        still computed for diagnostics.
    max_rank:
        Optional cap on the number of protected eigenvectors, selected by
        closeness to target_energy. Useful when finite-size effects blur exact
        midgap modes.
    """

    def __init__(
        self,
        ham: Any,
        target_energy: float = 0.0,
        delta: float = 1e-6,
        eps: float = 1e-12,
        projector: Optional[ArrayLike] = None,
        max_rank: Optional[int] = None,
    ) -> None:
        self.ham = ham
        self.target_energy = float(target_energy)
        self.delta = float(delta)
        self.eps = float(eps)
        self.max_rank = max_rank
        if not np.isfinite(self.target_energy) or not np.isfinite(self.delta) or self.delta < 0:
            raise ValueError("target_energy must be finite and delta finite and nonnegative.")
        if not np.isfinite(self.eps) or self.eps <= 0:
            raise ValueError("eps must be finite and positive.")

        H = ham.matrix_restricted()
        self.H = H.toarray() if sparse.issparse(H) else np.asarray(H, dtype=complex)
        if self.H.ndim != 2 or self.H.shape[0] != self.H.shape[1] or not self.H.size:
            raise ValueError("Restricted Hamiltonian must be a nonempty square matrix.")
        if not np.all(np.isfinite(self.H)):
            raise ValueError("Restricted Hamiltonian must be finite.")
        self.dimension = int(self.H.shape[0])
        if max_rank is not None and (
            isinstance(max_rank, bool) or not isinstance(max_rank, Integral)
            or not 0 <= max_rank <= self.dimension
        ):
            raise ValueError("max_rank must be an integer between zero and dimension.")

        if not np.allclose(self.H, self.H.conj().T, rtol=0.0, atol=1e-10):
            raise ValueError("Restricted Hamiltonian must be Hermitian.")
        # Remove numerical roundoff only after checking the model assumption.
        self.H = 0.5 * (self.H + self.H.conj().T)

        self.evals, self.evecs = la.eigh(self.H)
        self._projector = self._coerce_projector(projector) if projector is not None else None

    def _coerce_projector(self, projector: ArrayLike) -> np.ndarray:
        P = projector.toarray() if sparse.issparse(projector) else np.asarray(projector, dtype=complex)
        if P.shape != self.H.shape:
            raise ValueError("Projector shape must match restricted Hamiltonian shape.")
        if not np.all(np.isfinite(P)) or not np.allclose(P, P.conj().T, rtol=0.0, atol=1e-10):
            raise ValueError("Projector must be finite and Hermitian.")
        P = 0.5 * (P + P.conj().T)
        if not np.allclose(P @ P, P, rtol=0.0, atol=1e-10):
            raise ValueError("Projector must be idempotent.")
        return P

    def protected_indices(self) -> np.ndarray:
        """Return eigenvector indices selected as protected."""
        distances = np.abs(self.evals - self.target_energy)
        if self.max_rank is not None:
            order = np.lexsort((-self.evals, distances))
            return order[: int(self.max_rank)]
        return np.flatnonzero(distances <= self.delta)

    def protected_projector(self) -> np.ndarray:
        """Return P_C, the protected-sector projector."""
        if self._projector is not None:
            return self._projector
        idx = self.protected_indices()
        if idx.size == 0:
            return np.zeros_like(self.H, dtype=complex)
        V = self.evecs[:, idx]
        return V @ V.conj().T

    def protected_rank(self) -> int:
        """Return rank of the protected-sector projector."""
        P = self.protected_projector()
        return int(round(float(np.real(np.trace(P)))))

    def leakage_operator(self) -> np.ndarray:
        """Return L_off = (I-P_C) H P_C."""
        P = self.protected_projector()
        I = np.eye(self.dimension, dtype=complex)
        return (I - P) @ self.H @ P

    def leakage_norm(self, ord: Optional[int] = 2) -> float:
        """Return ell_H = ||(I-P_C) H P_C||."""
        return float(la.norm(self.leakage_operator(), ord=ord))

    def spectral_gap(self) -> float:
        """Return Delta, distance between protected and bulk eigenvalues."""
        idx = set(map(int, self.protected_indices()))
        if self._projector is not None:
            # User projectors need not be spectral. Fall back to distance from
            # target to nearest outside eigenvalue as a diagnostic.
            distances = np.abs(self.evals - self.target_energy)
            return float(np.min(distances)) if distances.size else 0.0
        if not idx or len(idx) == len(self.evals):
            return 0.0
        protected = np.array([self.evals[i] for i in idx])
        bulk = np.array([v for i, v in enumerate(self.evals) if i not in idx])
        distances = np.abs(protected[:, None] - bulk[None, :])
        return float(np.min(distances)) if distances.size else 0.0

    def beta_coherence(self) -> float:
        """Return beta_C = Delta / (Delta + ell_H + eps)."""
        gap = self.spectral_gap()
        ell_H = self.leakage_norm()
        return float(gap / (gap + ell_H + self.eps))

    def evolve(self, psi: ArrayLike, t: float) -> np.ndarray:
        """Return exp(-itH) psi in the restricted sector."""
        vec = self._column(psi)
        if vec.shape[0] != self.dimension:
            raise ValueError("State dimension must match the Hamiltonian.")
        if not np.isfinite(t):
            raise ValueError("Evolution time must be finite.")
        U = la.expm(-1j * self.H * float(t))
        return U @ vec

    def love_squared(self, psi: ArrayLike, t: float) -> float:
        """Return L²_C(psi,t)=||P_C exp(-itH) psi||²."""
        P = self.protected_projector()
        evolved = self.evolve(psi, t)
        retained = P @ evolved
        return float(np.real(retained.conj().T @ retained).item())

    def love_squared_curve(self, psi: ArrayLike, times: Iterable[float]) -> np.ndarray:
        """Return L²_C over a sequence of times."""
        return np.array([self.love_squared(psi, t) for t in times], dtype=float)

    def occupancy_l2c(self, psi0: ArrayLike, psit: ArrayLike) -> float:
        """Return occupancy-native L²_C using the Hamiltonian occupancy metric.

        Requires the source Hamiltonian object to expose:
            occupancy_statevector_restricted
            occupancy_fidelity
        """
        if not hasattr(self.ham, "occupancy_statevector_restricted"):
            raise AttributeError("ham lacks occupancy_statevector_restricted().")
        if not hasattr(self.ham, "occupancy_fidelity"):
            raise AttributeError("ham lacks occupancy_fidelity().")
        rho0 = self.ham.occupancy_statevector_restricted(self._as_sparse_col(psi0))
        rhot = self.ham.occupancy_statevector_restricted(self._as_sparse_col(psit))
        return float(self.ham.occupancy_fidelity(rho0, rhot))

    def report(self) -> L2CReport:
        """Return a structured finite-probe report."""
        return L2CReport(
            dimension=self.dimension,
            protected_rank=self.protected_rank(),
            leakage_ell_H=self.leakage_norm(),
            spectral_gap_delta=self.spectral_gap(),
            beta_c=self.beta_coherence(),
            target_energy=self.target_energy,
            tolerance_delta=self.delta,
        )

    @staticmethod
    def _column(psi: ArrayLike) -> np.ndarray:
        arr = psi.toarray() if sparse.issparse(psi) else np.asarray(psi, dtype=complex)
        arr = arr.reshape((-1, 1))
        if not arr.size or not np.all(np.isfinite(arr)):
            raise ValueError("State vector must be finite and nonempty.")
        norm = la.norm(arr)
        if not np.isfinite(norm) or norm == 0:
            raise ValueError("State vector must have finite nonzero norm.")
        return arr / norm

    @staticmethod
    def _as_sparse_col(psi: ArrayLike) -> sparse.csc_matrix:
        return sparse.csc_matrix(L2CProbe._column(psi))

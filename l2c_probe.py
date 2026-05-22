"""L2C protected-sector Hamiltonian probe.

This module formalizes L²_C as protected-sector retention under Hamiltonian
flow. It is designed to operate on the Hamiltonian objects used in the HOT
lattice / DDTL probe lane, especially objects exposing matrix_restricted(),
unitary_restricted(), occupancy_statevector_restricted(), and
occupancy_fidelity().

Canonical definitions:

    L²_C(psi,t) = || P_C exp(-i t H_T) psi ||²
    h           = || (I - P_C) H_T P_C ||
    beta_C      = Delta / (Delta + h + eps)

This file is a finite-dimensional analytic probe. It does not assert a final
infinite-dimensional spectral identification with zeta zeros.
"""

from __future__ import annotations

from dataclasses import dataclass
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
    leakage_h: float
    spectral_gap_delta: float
    beta_c: float
    target_energy: float
    tolerance_delta: float

    def as_dict(self) -> Dict[str, float]:
        return {
            "dimension": float(self.dimension),
            "protected_rank": float(self.protected_rank),
            "leakage_h": self.leakage_h,
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

        H = ham.matrix_restricted()
        self.H = H.toarray() if sparse.issparse(H) else np.asarray(H, dtype=complex)
        self.dimension = int(self.H.shape[0])
        if self.H.shape[0] != self.H.shape[1]:
            raise ValueError("Restricted Hamiltonian must be square.")

        # Symmetrize at numerical precision. The source Hamiltonians are
        # constructed as mat + mat.conj().T, but this keeps the probe robust.
        self.H = 0.5 * (self.H + self.H.conj().T)

        self.evals, self.evecs = la.eigh(self.H)
        self._projector = self._coerce_projector(projector) if projector is not None else None

    def _coerce_projector(self, projector: ArrayLike) -> np.ndarray:
        P = projector.toarray() if sparse.issparse(projector) else np.asarray(projector, dtype=complex)
        if P.shape != self.H.shape:
            raise ValueError("Projector shape must match restricted Hamiltonian shape.")
        return 0.5 * (P + P.conj().T)

    def protected_indices(self) -> np.ndarray:
        """Return eigenvector indices selected as protected."""
        distances = np.abs(self.evals - self.target_energy)
        if self.max_rank is not None:
            order = np.argsort(distances)
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
        """Return h = ||(I-P_C) H P_C||."""
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
        """Return beta_C = Delta / (Delta + h + eps)."""
        gap = self.spectral_gap()
        h = self.leakage_norm()
        return float(gap / (gap + h + self.eps))

    def evolve(self, psi: ArrayLike, t: float) -> np.ndarray:
        """Return exp(-itH) psi in the restricted sector."""
        vec = self._column(psi)
        U = la.expm(-1j * self.H * float(t))
        return U @ vec

    def love_squared(self, psi: ArrayLike, t: float) -> float:
        """Return L²_C(psi,t)=||P_C exp(-itH) psi||²."""
        P = self.protected_projector()
        evolved = self.evolve(psi, t)
        retained = P @ evolved
        return float(np.real(retained.conj().T @ retained))

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
            leakage_h=self.leakage_norm(),
            spectral_gap_delta=self.spectral_gap(),
            beta_c=self.beta_coherence(),
            target_energy=self.target_energy,
            tolerance_delta=self.delta,
        )

    @staticmethod
    def _column(psi: ArrayLike) -> np.ndarray:
        arr = psi.toarray() if sparse.issparse(psi) else np.asarray(psi, dtype=complex)
        arr = arr.reshape((-1, 1))
        norm = np.sqrt(np.real(arr.conj().T @ arr))[0, 0]
        if norm == 0:
            raise ValueError("State vector must be nonzero.")
        return arr / norm

    @staticmethod
    def _as_sparse_col(psi: ArrayLike) -> sparse.csc_matrix:
        return sparse.csc_matrix(L2CProbe._column(psi))

"""Example: finite L²_C / DDTL Hamiltonian probe.

This example assumes the OSF HOT lattice source file `hamiltonian.py` is present
on the Python path and exposes Tesseract1P. The example intentionally uses a
small L because the restricted tesseract Hamiltonian has size L^4 x L^4.

Source provenance:
- OSF file: https://osf.io/p2v7y/files/34fnt
- Paper: Realization of Higher-Order Topological Lattices on a Quantum Computer
- PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC11237062/
"""

from __future__ import annotations

import numpy as np

from hamiltonian import Tesseract1P
from l2c_probe import L2CProbe


def alternating_hot_params(ncoeff: int = 32):
    """Return a simple nontrivial alternating-hopping parameter set.

    These are not a reproduction of the paper's Supplementary Table values.
    They are a lightweight smoke-test configuration for the probe API.
    """
    vs = np.full(ncoeff, 0.3, dtype=float)
    vps = np.full(ncoeff, 1.0, dtype=float)
    return vs, vps


def main() -> None:
    L = 2
    vs, vps = alternating_hot_params()
    ham = Tesseract1P(vs=vs, vps=vps, L=L)

    probe = L2CProbe(ham, target_energy=0.0, delta=1e-8, max_rank=2)
    report = probe.report()

    # Localized corner state in restricted coordinates.
    psi0 = ham.statevector_restricted(1, 1, 1, 1)
    times = np.linspace(0.0, 1.0, 6)
    curve = probe.love_squared_curve(psi0, times)

    print("L²_C / DDTL report")
    print(report)
    print("times:", times)
    print("L²_C curve:", curve)


if __name__ == "__main__":
    main()

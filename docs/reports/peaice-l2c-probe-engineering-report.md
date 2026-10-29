# PeAIce L²_C finite probe engineering report

**Revision:** 29 October 2026 · KakeyaLogic · Love Labs LCA
**Status:** finite numerical diagnostics; operational validity OPEN

## Current implementation

`l2c_probe.py` accepts a finite Hermitian Hamiltonian and selects a spectral
protected sector or accepts a finite orthogonal projector. Its public classes
are `L2CProbe` and `L2CReport`. The implemented measurements are:

```text
L²_C(ψ,t) = ‖P_C exp(-itH_T) ψ‖², with ψ normalized
ℓ_H = ‖(I-P_C)H_TP_C‖
β_C = Δ/(Δ+ℓ_H+ε)
```

For custom non-spectral projectors, `spectral_gap()` returns a target-distance
diagnostic, not a proved protected-to-bulk gap. A spectral projector commutes
with H_T: its retention is constant and its leakage vanishes. Studying transfer
requires a noncommuting projector. A bulk state has zero protected mass; unitary
flow does not itself dissipate the state.

| Surface | Public API |
|---|---|
| Selection | `protected_indices()`, `protected_projector()`, `protected_rank()` |
| Coupling | `leakage_operator()`, `leakage_norm()` |
| Separation diagnostic | `spectral_gap()`, `beta_coherence()` |
| Normalized evolution and retention | `evolve()`, `love_squared()`, `love_squared_curve()` |
| Receipt | `report()`, `L2CReport.as_dict()` |

The rank selector uses `np.lexsort((-self.evals, distances))`: equal distances
prefer the larger eigenvalue, so +0.001 wins over -0.001 at target zero.
Malformed Hamiltonians, non-projectors, invalid ranks, and nonfinite inputs are
rejected. Retention extracts a scalar explicitly for modern NumPy compatibility.
`leakage_h` remains a deprecated read alias; serialized output uses
`leakage_ell_H`. Evaluator h_eval is a separate, uncalibrated governance concept.

## Reproducible verification

```bash
python -m pip install numpy scipy
python -m unittest discover -s probe_tests -v
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python examples/typed_directional_state/run_saver_reference.py
python examples/ipiano_probe.py
```

The committed regressions exercise the tie convention, analytic two-state
retention, noncommuting transfer, leakage serialization, invalid models and
states, and an iPiano quadratic control. CI runs both unittest suites and the
SAVER calibration, including an installed-wheel check.

## Historical receipt and owed implementation

The earlier CoWork report described a correction from 48 passes / 1 failure to
49 passes in a separate environment. That historical suite is not tracked as
`tests/test_l2c_probe.py`; its count must not be substituted for a current result.
The newer finite regression suite has its own test inventory.

`BetaDynamicReport`, `beta_T`, `coercive_gap`, `coercive_threshold`,
`coercive_energy`, and `beta_dynamic_report` are unimplemented research targets
in this checkout. Downstream code must not import them as existing APIs. The
optional tesseract example requires the separately obtained OSF `hamiltonian.py`
source documented in its header. The iPiano example is a fixed-step numerical
diagnostic; backtracking and Lyapunov telemetry remain owed.

## Claim ledger and rejection conditions

| Claim | Status | Evidence and limit |
|---|---|---|
| Deterministic sector convention | implemented finite behavior | Equal-distance regression; positive-side convention is explicit |
| Protected mass and leakage | NUMERICS / finite linear algebra | Analytic two-state controls; no operational AI effectiveness claim |
| Historical 49 passes | historical receipt | Original suite unavailable; current tests are separate |
| β-dynamic APIs | PROPOSED / OWED | No executable implementation in this revision |
| Infinite spectral identification | OPEN | Finite diagnostics do not discharge the prime-carrying bridge |

Reject a finite implementation if it selects the wrong tie, admits a
non-projector as P_C, produces invalid normalized retention, hides nonfinite
telemetry, or reports unimplemented APIs as verified. Preserve failed controls
and their revisions. `h_eval < 1`; RH and Coleman remain OPEN.

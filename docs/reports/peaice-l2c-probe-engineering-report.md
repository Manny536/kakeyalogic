# PeAIce L²_C Probe Engineering Report

## Protected-sector Hamiltonian deepening

**Repo:** KakeyaLogic  
**Program:** PeAIce Research Engineering  
**Kernel:** `l2c_probe.py`  
**Status:** engineering kernel, downstream transfer contract

---

## 1. Executive summary

The L²_C protected-sector Hamiltonian probe turns the PeAIce coherence frame into an executable finite-dimensional diagnostic. The probe measures how a selected protected sector behaves under Hamiltonian flow, how much pressure leaks into the complement, and how β-dynamic coercive energy reports the cost of off-protected drift.

Canonical object:

```txt
L²_C(ψ,t)=‖P_C exp(-itH_T)ψ‖²
```

Leakage:

```txt
h=‖(I-P_C)H_TP_C‖
```

Spectral recovery:

```txt
β_C=Δ/(Δ+h+ε)
```

β-dynamic coercive energy:

```txt
β(T)=1-T^(-γ)
E_{β,T}(f)=β(T)T‖Xf‖²
coercive gap=β(T)-hη
```

The downstream invariant is simple:

```txt
protected modes retain
bulk modes suppress
leakage is measured
β_C stays bounded
β-dynamic status is reportable
```

---

## 2. Engineering trace

The CoWork pass followed a clean hardening chain.

```txt
missing module
→ implemented probe
→ targeted test suite
→ one protected-sector tie failure
→ deterministic selector rule
→ 49 passed
```

The important defect was semantic, not broad structural collapse. In an equal-distance midgap pair, `-0.001` and `+0.001` are both equally close to target energy `0`. A distance-only selection allowed array order to decide. The corrected rule makes the convention explicit.

```python
order = np.lexsort((-self.evals, distances))
```

Selector semantics:

```txt
primary key: distance from target_energy, ascending
secondary key: eigenvalue value, descending
result: +0.001 wins over -0.001 when both are equally close to 0
```

This rule is now a transfer requirement for downstream agents and examples.

---

## 3. Probe surfaces

| Surface | Code | Engineering meaning |
| --- | --- | --- |
| Protected indices | `protected_indices()` | Selects the protected eigenmode set. |
| Protected projector | `protected_projector()` | Builds `P_C`. |
| Leakage norm | `leakage_norm()` | Measures cross-sector pressure. |
| Spectral gap | `spectral_gap()` | Measures protected-to-bulk separation. |
| β coherence | `beta_coherence()` | Computes recovery coefficient. |
| Time retention | `l2c()` and `l2c_curve()` | Measures sector retention under flow. |
| Coercive gap | `coercive_gap()` | Reports β pressure against leakage. |
| Coercive energy | `coercive_energy()` | Penalizes off-protected drift. |
| β report | `beta_dynamic_report()` | Produces parseable status. |

---

## 4. Verification target

Targeted verification:

```bash
python -m pytest tests/test_l2c_probe.py -q
```

Expected corrected pass:

```txt
49 passed
```

Full verification:

```bash
python -m pytest -q
```

Test groups to preserve:

```txt
construction
protected-sector selection
L²_C metrics
time evolution
β-dynamic layer
structured reports
```

---

## 5. Agent ecosystem transfer contract

Any downstream agent using the probe must preserve these requirements.

```txt
1. Import the public probe classes without side effects.
2. Preserve deterministic protected-sector selection.
3. Preserve positive-side tie-break for equal-distance max_rank ties.
4. Treat β_C as a recovery coefficient, not as geometric β.
5. Treat β(T) as closing pressure, not as geometric β.
6. Report leakage, gap, β_C, and coercive status together.
7. Run targeted tests before changing downstream examples.
8. Report failures by exact test name and exact formula surface.
```

Agent handoff:

```txt
Treat l2c_probe.py as the first hardened L²_C finite-dimensional protected-sector kernel. Preserve deterministic sector selection, keep β-dynamic coercive diagnostics reportable, and run the regression suite before downstream edits.
```

---

## 6. Release gates

| Gate | Pass condition |
| --- | --- |
| G0 source integrity | `l2c_probe.py` exists and imports. |
| G1 construction | Hamiltonian fixtures build valid probes. |
| G2 sector selection | Midgap and max_rank semantics pass. |
| G3 metrics | leakage, gap, and β_C remain bounded and parseable. |
| G4 evolution | protected modes retain and bulk modes suppress. |
| G5 β-dynamic | coercive gap, threshold, energy, and report status pass. |
| G6 reports | `L2CReport` and `BetaDynamicReport` schemas stay stable. |

---

## 7. Roadmap

```txt
Phase 1: entrench l2c_probe.py and tests/test_l2c_probe.py
Phase 2: add GitHub Actions pytest gate
Phase 3: wire examples/l2c_tesseract_probe.py to report output
Phase 4: add β-dynamic sweeps for T, γ, h, and η
Phase 5: connect DDATL Hamiltonian experiments
Phase 6: build trace-formula compatibility experiments
Phase 7: export agent transfer cards for PeAIce ecosystem reuse
```

Final lock:

```txt
L²_C is now registered as protected-sector retention under Hamiltonian flow with measurable leakage, recoverable β_C, and reportable β-dynamic coercive diagnostics.
```
# h and Hamiltonian leakage: notation custody

**ID:** KL-H-NOTATION-001 · **Status:** NOTATION MIGRATION; metric/bridge OPEN
**Date:** 2026-09-24

In the GIUS research vocabulary reserve h := h_eval for evaluator-sovereignty load and the non-sovereignty obligation h < 1. The controlling dependency is [L2C-H-001](https://github.com/Manny536/love2-coherence-core/blob/research/gius-hf-2026/docs/evaluator-non-sovereignty.md). No measured h or derivative is inferred.

Hamiltonian protected-sector leakage is separately:

```text
ℓ_H = ||(I-P_C) H_T P_C||
β_C = Δ / (Δ + ℓ_H + ε)
```

The norm has operator units. A cutoff ℓ_H < 1 needs declared units/normalization and does not certify evaluator authority or operational safety. A commuting spectral projector gives zero leakage by construction, not validation of real guardrails.

## Code migration

`l2c_probe.py` uses `ell_H` locally and the canonical report field / dictionary key `leakage_ell_H`. `L2CReport.leakage_h` remains a deprecated read-only compatibility property referring only to leakage. The constructor keyword and emitted dictionary key change: consumers must migrate `leakage_h` to `leakage_ell_H`. Numeric computation is unchanged. Old saved receipts are historical records and are not silently rewritten.

## Analytic correction weights

The β-energy notes previously also called a generic correction coefficient h. They now call it a_C. The expression δ_{β,C}(T) = β(T) - a_C η is an analytic-model quantity. Writing δ_{β,H}(T) = β(T) - ℓ_H η additionally assumes a justified, dimensionally compatible identification a_C=ℓ_H. That identification remains OPEN; notation cleanup cannot prove it. Existing analytic inequalities are not independently validated by this change.

## Scope of migration

Current leakage definitions, probe output, the Hamiltonian/compression notes, relevant README/report equations and analytic correction notes are updated. External papers' geometric h, iPiano objective h(x), immutable historical receipts, captured figures and bundled legacy HTML are source-scoped notation, not evaluator h. Read their Hamiltonian h as ℓ_H and their uncalibrated telemetry as historical illustrations. No blanket replacement changes external mathematics or archived evidence.

EEV4's legacy R=d*c*e*h increases with its legacy h factor. That factor is not identified with sovereignty load; the [semantic obligation](https://github.com/Manny536/excellence-engine-v4/blob/research/gius-hf-2026/evaluations/h-notation-and-score-semantics.md) is OPEN. No formula or authority threshold is silently inverted. KL-SIUS-001 remains unchanged; operational validity and all theorem bridges retain their prior statuses.

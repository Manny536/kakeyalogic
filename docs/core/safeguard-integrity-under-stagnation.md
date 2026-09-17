# Safeguard Integrity Under Stagnation (SIUS)

**Program:** `PEAICE-SIUS-001`
**Local ID:** `KL-SIUS-001`
**Status:** DOCUMENTED DEFINITION; operational validity OPEN
**Registered:** 2026-09-16

Standalone basis: [SIUS Integrity.docx](https://github.com/Manny536/researchengineeringreports/blob/main/reports/sources/sius-integrity-provenance.md), supplied by the user in “Explain sticky sets.” [Source provenance and limits](https://github.com/Manny536/researchengineeringreports/blob/main/reports/sources/sius-integrity-provenance.md).

## Definition and scope

**Static Safeguard ≠ Operative Safeguard.** A declared control can remain unchanged while its operative force degrades as its environment changes. This is a preservation problem and a documented definition, not a proved universal theorem or a claim that every static safeguard necessarily fails.

SIUT (Safeguard Integrity Under Transformation) asks whether safeguards survive $X_0 \xrightarrow{T} X_1$. SIUS is its sibling condition: fix the declared system/control projection $X_t=X_0$ (so $T=I$ on that projection) while $E_0\rightarrow E_t$. Environmental change can include capability baselines, integrations, adversary tactics, vocabulary, or authority context. Declare exactly what is frozen and what belongs to $E$ before evaluating.

If the protected control itself changes, label the episode SIUT or mixed SIUT/SIUS; do not silently call the whole changing system static. Little coarse progress or internal circulation alone is not the standalone SIUS definition.

## Operative state and margin

The ordered grain vector is $\Gamma_G=(s,a,v,e,r)^T$: semantic preservation, authority preservation, visibility, enforceability/containment, and retention through time. Under fixed $X_0$, evaluate these obligations against the current environment: $\Gamma_G(X_0;E_t)$. This explicit environmental argument explains how operative grain outcomes can change while the control remains fixed.

The source's operative margin is

$$\Delta_G(t)=\operatorname{ContainmentBoundary}(X_0)-E_{\mathrm{cap}}(t).$$

A **Stagnation Boundary Error** is $\Delta_G(t)<0$. Numeric subtraction requires a declared common scale, units, measurement procedure, and uncertainty treatment; arbitrary capability scores and sets cannot be subtracted. If those are unavailable, retain an unresolved margin and evaluate the separately specified reachability/containment relation. A modeled nonnegative margin is not universal containment evidence.

For a declared environment, observation window, and required direction set, preservation requires a supported nonnegative margin, every required grain operative, and evaluator non-sovereignty `h < 1`. No weighted average can compensate for a failed grain. Missing evidence remains unresolved; it cannot authorize routing. Equality at zero passes only the modeled margin inequality, with no robustness buffer implied.

| Coordinate | Failure mechanism | Operational obligation |
|---|---|---|
| s | Semantic decay under changed vocabulary/context | Test current meaning, including drifted and stable examples |
| a | Stale authority or credentials | Recheck scope, expiry, revocation and write authorization |
| v | Telemetry blind spots | Demonstrate coverage of newly reachable activity; missing logs are not a pass |
| e | Containment decoupling | Test a conservative reachability envelope, including egress outside planned routes |
| r | Longitudinal correction/patch decay | Replay retained corrections and red lines at later checkpoints |

## Response and custody

Use the existing SAVER sequence: **Observe → Grain → Gate → Overlap → Refine → Route → Receipt → Retain**. Only admitted transitions enter planning; unresolved and failed transitions remain available as evidence. Route existence does not establish containment.

HELD correction custody must distinguish instructions, evidence, authority, and constraints. A correction requires applicable authority and evidence; instruction-shaped text supplies neither. Retain the correction's scope, lineage, applicability and replay evidence. HELD does not itself mean true, active, approved, or executable. EEV4 owns its evaluation predicate. `h < 1` is the evaluator non-sovereignty obligation here, not an inferred physical leakage norm or a measured certificate.

## Operator firewall

SIUS defines the preservation obligation and failure condition. The [finite-grain operator note](../operators/finite-grain-del.md), `KL-SIUS-OP-001`, is a separate **PROPOSED** diagnostic. SIUS does not depend on establishing a differentiable field or curl. Operator success does not establish SIUS validity; SIUS evidence does not establish the operator. Kakeya geometry supplies at most a structural analogy unless a transfer is proved.

## Registration and open obligations

| Repository | Local ID | Ownership | Status |
|---|---|---|---|
| `kakeyalogic` | [KL-SIUS-001](https://github.com/Manny536/kakeyalogic/blob/main/docs/core/safeguard-integrity-under-stagnation.md) | Controlling SIUS definition | DOCUMENTED DEFINITION; operational validity OPEN |
| `excellence-engine-v4` | [EEV4-SIUS-EVAL-001](https://github.com/Manny536/excellence-engine-v4/blob/main/evaluations/sius-held-correction.md) | HELD/SIUS evaluation | EVALUATION CONTRACT |
| `LoveLabs-LCA` | [LCA-SIUS-CAL-001](https://github.com/Manny536/LoveLabs-LCA/blob/main/docs/sius-operational-outcomes.md) | Operational benchmark protocol and synthetic calibration | REGISTERED BENCHMARK; operational validation OPEN |
| `researchengineeringreports` | [RER-SIUS-001](https://github.com/Manny536/researchengineeringreports/blob/main/reports/sius-safeguard-integrity-under-stagnation.md) | Academic report and source custody | WORKING RESEARCH REPORT |
| `peaice-index` | [INDEX-SIUS-001](https://github.com/Manny536/peaice-index/blob/main/docs/sius.md) | Compressed public route | ROUTE ONLY |
| `love2-coherence-core` | [L2C-SIUS-DEP-001](https://github.com/Manny536/love2-coherence-core/blob/main/docs/sius-dependency.md) | h < 1 and correction-retention dependency | DEPENDENCY POINTER |

All child IDs belong to `PEAICE-SIUS-001`; none supplies independent corroboration merely by repeating another repository. The report holds the source provenance record; this file controls the repository definition.

Operational SIUS validity remains **OPEN**, alongside operational SIUT validity. Required next evidence: calibrated observables and thresholds, explicit environment coverage, longitudinal traces, independent evaluation, and counterexample search. Falsify a scoped preservation claim with any required grain failure, negative operative margin, uncontained reachable state, unauthorized authority promotion, or lost applicable correction. Reject any proposed diagnostic that reports preservation despite such a witnessed violation. RH and Coleman remain OPEN; no theorem bridge is promoted.

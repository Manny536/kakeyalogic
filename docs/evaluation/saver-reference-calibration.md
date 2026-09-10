# SAVER reference calibration

**Date:** 2026-09-10

**Fixture:** `SAVER-CAL-001`

**Specification:** [Five-grain routing 1.0](../core/five-grain-routing.md)

**State:** SYNTHETIC CALIBRATION AND REFERENCE-ROUTER BEHAVIORAL RECEIPT. Operational SIUT validity remains OPEN.

## What calibration means here

Calibration binds a frozen synthetic graph to:

- a declared required-direction set;
- required SAVER grains `S, A, V, E, R`;
- declared grain evidence and interior samples;
- an explicitly chosen positive operational edge-cost model;
- expected admitted, unresolved, and failed sets;
- expected Geodecis distances and a separate containment verdict.

It does **not** fit a safety, ethics, truth, or Love-Squared Coherence score. No weighted grain average is used for admission.

Cost model:

```text
name: synthetic_operational_hops
unit: declared_positive_cost
not:  safety, ethics, truth, L²_C
```

On `SAVER-CAL-001` the unresolved shortcut costs 1, the shortest admitted route costs 8, and the longer admitted direct route costs 12. Those numbers are chosen so the evidence-sensitivity diagnostic is strictly positive:

```text
Δ_evid(start, goal) = d^A − d^◇ = 8 − 1 = 7
```

`Δ_evid` reports how much the preferred route could change if unresolved evidence later resolved favorably. It is not permission to traverse the unresolved shortcut.

## Graph

```text
start --e_via1(4, admitted)--> via --e_via2(4, admitted)--> goal
start --e_long(12, admitted)--> goal
start --e_shortcut(1, V UNRESOLVED)--> goal
start --e_failed_authority(2, A FAIL)--> leak
start --e_boundary(2, interior S FAIL)--> smooth --e_smooth_goal(1, admitted)--> goal
start --e_not_evaluated(5, NOT_EVALUATED)--> shadow
```

Allowed boundary: `{start, via, smooth, goal, shadow}`.  
Confirmed reachable `R⁻` also includes `leak`. Containment therefore FAILs even though the admitted planner path `start → via → goal` exists.

## Six specification cases

| Case | Expected on `SAVER-CAL-001` |
|---|---|
| Shortest admitted route | `start → via → goal` via `e_via1`, `e_via2`, cost 8 |
| Unresolved shortcut visible, not traversed | `e_shortcut` in `E^U`, absent from the selected path; `d^◇ = 1` |
| Failed transition retained | `e_failed_authority` in `E^F` and in the retention ledger |
| Endpoint-pass / interior-fail | `e_boundary` flagged as a Semantic boundary-error falsifier |
| Retention regression | later compression drops `obj_redline`; Retention FAILs for `d_safeguard` |
| Planning is not containment | admitted route exists; containment verdict FAIL because `leak ∈ R⁻` |

`NOT_EVALUATED` on `e_not_evaluated` remains distinct from `UNRESOLVED` on `e_shortcut`. Both block admission.

## How to run

```text
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python examples/typed_directional_state/run_saver_reference.py
```

The runner prints a routing receipt and a calibration receipt that includes the fixture SHA-256. Re-running against a mutated fixture must change the hash.

## Honesty

- Grain predicates in this fixture are declared, not inferred from natural language.
- The reference router does not block a live control plane.
- `PASS_MODEL` is not issued on this fixture; the containment receipt is FAIL, and even a later `PASS_MODEL` would be conditional on the reachability model.
- Operational SIUT validity remains OPEN until deployment evidence exists.

# Change log

## 2026-09-08 — Five-grain routing, specification 1.0

### Added

- Defined the five KakeyaLogic grains: **Semantic, Authority, Visibility, Enforceability, Retention**.
- Added `docs/core/five-grain-routing.md` as the controlling routing specification.
- Defined the finite evaluation field as required directions × required SAVER grains.
- Added non-compensatory grain gating: a failed, unresolved, or not-evaluated required grain cannot be offset by stronger results elsewhere.
- Added explicit admitted, unresolved, and failed transition sets.
- Added **Geodecis** as a proposed route-selection layer operating only on KakeyaLogic-admitted transitions under an explicitly chosen operational cost.
- Added uncertainty-visible distance as an evidence-sensitivity diagnostic; unresolved shortcuts remain visible but non-traversable.
- Added the endpoint-pass / interior-fail boundary-error falsifier.
- Added a formal separation between planner admissibility and modeled reachability/containment.

### Preserved

- The 0.1 typed-directional object, transformation, identity, provenance, recovery, and history obligations remain antecedent contracts beneath the five-grain layer.
- Compression, overlap, and refinement retain their existing transformation meanings.
- HELD remains **relevant and retained**, not automatically active, verified, approved, true, or executable.
- Existing geometric, spectral, operator, optimization, and numerical research retains its native theorem and evidence status.

### Open

- Reference implementation of the SAVER grain evaluator and KakeyaLogic router.
- Geodecis runtime and route-cost calibration.
- Synthetic regression suite, including unresolved shortcut and endpoint-pass/interior-fail cases.
- Longitudinal Retention evaluation.
- Operational SIUT validation and reachability/containment coverage.

No behavioral pass, deployment change, theorem promotion, provider-policy exception, or new authority is claimed by specification 1.0.

---

## 2026-08-28 — Typed-directional foundation, specification 0.1

### Added

- Core definition, glossary, object contract, transformation contracts, and directional-completeness specification.
- Explicit separation of kind, type, and independent status dimensions.
- Relevant scope and basis for HELD objects; active remains a separate operational selection.
- Proposed geometry-to-state mapping and a field contract for the separately owned custody engine.
- Repository map separating existing components, new documentation, and planned implementation paths.

### Clarified

- **HELD means relevant and retained**, not merely stored. It does not automatically mean active, verified, approved, or executable.
- Preservation permits justified corrections with versioned history; it does not freeze outdated state.
- Completeness is relative to a predeclared required-direction set and is checked per direction. Equal counts or aggregate scores do not establish preservation.
- Compression costs must identify the resource measured. Refinement does not reconstruct discarded information without a retained or retrieved source.
- The corrected **49 passed** result is a historical receipt, not a current-tree result or evidence for the new contract. The original engineering report remains unchanged.

### Unchanged and pending

- No executable code, deployment workflow, public-page behavior, published research artifact, or theorem status is changed.
- Machine-readable schemas, reference implementation, new behavioral tests, longitudinal performance measurements, and downstream custody-engine adoption remain pending.
- No private data is introduced and no new authority or provider-policy exception is created.

Baseline inspected: `6f12f0fd58e147d04eb2c5feefa4797a9fa0a852`. See the [repository map](docs/repository-map.md) and [core overview](docs/core/README.md) for scope and source links.

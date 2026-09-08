# KakeyaLogic repository map

**Map date:** 2026-09-08

**Baseline for specification 1.0:** `main` at `98c655c7cd5023acaaeee30d5abcd124bdc05ec1`.

**Update scope:** five-grain routing specification and documentation integration. Existing numerical kernels, public page behavior, deployment workflow, and theorem-status artifacts are preserved.

## Reader path

Start with the [root overview](../README.md), then the [core foundations](core/README.md), [glossary](core/glossary.md), [object contract](core/typed-directional-object.md), [transformation contract](core/compression-overlap-refinement.md), [directional completeness](core/directional-completeness.md), and [five-grain routing](core/five-grain-routing.md). Use the [documentation index](README.md) for the wider research program.

## Current computational-core documents

| Path | Responsibility | Specification 1.0 treatment |
|---|---|---|
| [docs/core/README.md](core/README.md) | Core definition, scope, reading order, and delivery state | Promoted to 1.0; introduces SAVER grain field and routing split. |
| [docs/core/glossary.md](core/glossary.md) | Object, direction, grain, status, and routing vocabulary | Adds Semantic, Authority, Visibility, Enforceability, Retention, Geodecis, admission, and reachability terms. |
| [docs/core/typed-directional-object.md](core/typed-directional-object.md) | Identity, relevance, state dimensions, authority, relationships, and transitions | Preserved; remains the lower-level typed object contract. |
| [docs/core/compression-overlap-refinement.md](core/compression-overlap-refinement.md) | Transformation contracts and receipts | Preserved; five-grain routing applies a preservation view over these contracts. |
| [docs/core/directional-completeness.md](core/directional-completeness.md) | Required directions and evaluation | Promoted to 1.0; adds the directions × grains evaluation field and strict `KComplete`. |
| [docs/core/five-grain-routing.md](core/five-grain-routing.md) | SAVER grain gate, admitted/unresolved/failed transitions, Geodecis, interior tests, containment split | **NEW in 1.0.** |
| [docs/interfaces/geometry-to-relational-state.md](interfaces/geometry-to-relational-state.md) | Proposed geometry-to-state mapping | Preserved; no automatic theorem transfer. |
| [docs/interfaces/excellence-engine-v4.md](interfaces/excellence-engine-v4.md) | HELD relevance and field-to-custody interface | Preserved; separate engine ownership remains intact. |

## Existing components

| Location | Responsibility | Treatment in specification 1.0 |
|---|---|---|
| [README.md](../README.md) | Repository entry point, program state, existing kernel descriptions | Existing typed-directional foundation preserved; five-grain core is reachable through the core docs. |
| [docs/README.md](README.md) | Research documentation index | Existing research links preserved. |
| [Geometric probe](guth-wang-bateman-zahl-probe.md), [Light Basic](kns-light-basic.md), [restriction note](wang-wu-restriction-decoupling.md) | Directional geometry, incidence, scale, and separation research | Preserve originals; no theorem claim is promoted by SAVER routing. |
| [l2c_probe.py](../l2c_probe.py) | Existing protected-sector numerical kernel | No code or behavior change. |
| [probes/](../probes) | Existing deterministic numerical probes | Preserve; not the new five-grain routing implementation. |
| [examples/](../examples) | Existing numerical and learning examples | Preserve; file presence is not a fresh execution receipt. |
| [docs/data/](data), [docs/reports/](reports) | Existing numerical data and engineering reports | Preserve historical evidence without re-certifying it. |
| [Custody field mirror](excellence-engine-v4.md), [lab pointer](excellence-engine-v4-lab.md) | Separate-engine context and ownership | Preserve. |
| [Inspectable Intelligence](inspectable-intelligence.md), [authority detection](l2c-authority-detection.md) | Existing governance and source/authority discipline | Preserve and treat as evidence surfaces, not automatic grain passes. |
| [Prime-carrying architecture](prime-carrying-trace-architecture.md), [operator program](step4-operator-program.md), [spectral determinism](spectral-determinism.md) | Spectral and operator research | No theorem-status changes. |
| [Dynamics](dpsa-inertial-grounding.md), [optimization](ipiano-inertial-proximal-probe.md), [beta-dynamic layer](beta-dynamic.md) | Existing dynamics and optimization research | Preserve native notation and assumptions. |
| [docs/outcomes/](outcomes), [docs/whitepapers/](whitepapers), [docs/transfers/](transfers), [docs/archive/](archive) | Publication artifacts, transfers, and prior source state | No silent rewrite or relocation. |
| [arxiv/](../arxiv), [papers/](../papers) | Manuscripts, bibliography, exports, templates, and publication routing | Preserve existing topology. |
| [index.html](../index.html) | Current public page | Unchanged; public-navigation work is a later phase. |
| [.github/workflows/static.yml](../.github/workflows/static.yml) | Deploy repository content to GitHub Pages | Unchanged; not a test workflow. |
| [kakeyalogic-reconcile.sh](../kakeyalogic-reconcile.sh), [LICENSE](../LICENSE) | Existing maintenance script and license | Unchanged. |

## Specification 1.0 architecture

The computational routing stack is now documented as:

```text
Typed objects and relationships
        ↓
Required directions
        ↓
SAVER grains: Semantic · Authority · Visibility · Enforceability · Retention
        ↓
KakeyaLogic grain gate
        ↓
Admitted / Unresolved / Failed transition sets
        ↓
Geodecis operational route selection over admitted transitions
        ↓
Transformation receipt + longitudinal Retention re-check
```

Planning and containment remain separate. A shortest or otherwise preferred admitted route does not prove that every actually reachable alternative is contained.

## Planned implementation paths — not yet implemented

| Proposed path | Future responsibility |
|---|---|
| `schemas/` | Machine-readable field-object, grain-state, transformation-receipt, routing-receipt, and evaluation-receipt contracts. |
| `src/kakeyalogic/` | Reference typed field, SAVER grain evaluation, admission gate, Geodecis routing, lineage, and completeness evaluation. |
| `tests/` | Contract and regression tests, including endpoint-pass/interior-fail and planning-vs-containment cases. |
| `examples/typed_directional_state/` | Synthetic grain-routing, recovery, uncertainty, and failure examples. |
| `docs/evaluation/longitudinal-retention.md` | Matched longitudinal evaluations and response-timing protocol. |
| `.github/workflows/verify.yml` | Automated verification, separate from deployment. |

No private operational records, participant data, or new data access are introduced by specification 1.0.

## Cross-repository ownership

| Owner | Responsibility |
|---|---|
| KakeyaLogic | Geometric field, typed-directional contracts, SAVER grain routing specification, and proposed field-side checks. |
| [Excellence Engine Version 4](https://github.com/Manny536/excellence-engine-v4) | Custody engine, HELD predicates, engine schema, pipeline, and engine evaluations. |
| [Claude V6 research repository](https://github.com/Manny536/claude-v6) | Its theorem ledger and spectral claim status. |
| [LoveLabs-LCA](https://github.com/Manny536/LoveLabs-LCA) | Love-Squared Coherence relational research and application studies. |

The other repositories are linked, not modified or declared synchronized by this update.

## Historical receipt boundary

The [engineering report](reports/peaice-l2c-probe-engineering-report.md) and earlier pull-request record retain the corrected **49 passed** historical result. That result is not evidence that the five-grain routing contract has been implemented or behaviorally validated.

Specification 1.0 claims documentation-level closure only. Reference implementation, synthetic routing tests, operational SIUT validation, and containment coverage remain OPEN.

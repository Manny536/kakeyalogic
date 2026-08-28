# KakeyaLogic repository map

**Map date:** 2026-08-28

**Inspected baseline:** [`main` at `6f12f0fd58e147d04eb2c5feefa4797a9fa0a852`](https://github.com/Manny536/kakeyalogic/tree/6f12f0fd58e147d04eb2c5feefa4797a9fa0a852).

**Update scope:** documentation foundations only. Existing code, public page, deployment workflow, and published research artifacts are preserved.

## Reader path

Start with the [root overview](../README.md), then the [core foundations](core/README.md), [glossary](core/glossary.md), [object contract](core/typed-directional-object.md), [transformation contract](core/compression-overlap-refinement.md), and [completeness contract](core/directional-completeness.md). Use the [documentation index](README.md) for the wider research program.

## Existing components

| Location | Responsibility | Treatment in this update |
|---|---|---|
| [README.md](../README.md) | Repository entry point, program state, existing kernel descriptions | Add typed-directional definition and navigation; label historical test receipt. |
| [docs/README.md](README.md) | Research documentation index | Add core and interface sections; retain existing research links. |
| [Geometric probe](guth-wang-bateman-zahl-probe.md), [Light Basic](kns-light-basic.md), [restriction note](wang-wu-restriction-decoupling.md) | Directional geometry, incidence, scale, and separation research | Preserve originals; relate them through a separately scoped interface. |
| [l2c_probe.py](../l2c_probe.py) | Existing protected-sector numerical kernel | No code or behavior change. |
| [probes/](../probes) | Existing deterministic Light Basic numerical probe | Preserve; not the new typed-directional checker. |
| [examples/](../examples) | Existing numerical and learning examples | Preserve; file presence is not a fresh execution receipt. |
| [docs/data/](data), [docs/reports/](reports) | Existing numerical data and engineering reports | Preserve historical evidence without re-certifying it. |
| [Custody field mirror](excellence-engine-v4.md), [lab pointer](excellence-engine-v4-lab.md) | Separate-engine context and ownership | Preserve; new field contract lives under `docs/interfaces/`. |
| [Inspectable Intelligence](inspectable-intelligence.md), [authority detection](l2c-authority-detection.md) | Existing governance and source/authority discipline | Preserve; link from the new specification. |
| [Prime-carrying architecture](prime-carrying-trace-architecture.md), [operator program](step4-operator-program.md), [spectral determinism](spectral-determinism.md) | Spectral and operator research | No theorem-status changes. |
| [Dynamics](dpsa-inertial-grounding.md), [optimization](ipiano-inertial-proximal-probe.md), [beta-dynamic layer](beta-dynamic.md) | Existing dynamics and optimization research | Preserve native notation and assumptions. |
| [docs/outcomes/](outcomes), [docs/whitepapers/](whitepapers), [docs/transfers/](transfers), [docs/archive/](archive) | Publication artifacts, transfers, and prior source state | No silent rewrite or relocation. |
| [arxiv/](../arxiv), [papers/](../papers) | Manuscripts, bibliography, exports, templates, and publication routing | Preserve existing topology. |
| [index.html](../index.html) | Current Grain Zero and Outcomes public page | Unchanged; public-navigation work is a later phase. |
| [.github/workflows/static.yml](../.github/workflows/static.yml) | Deploy repository content to GitHub Pages | Unchanged; not a test workflow. |
| [kakeyalogic-reconcile.sh](../kakeyalogic-reconcile.sh), [LICENSE](../LICENSE) | Existing maintenance script and license | Unchanged. |

## Documentation added in this update

| Path | Responsibility |
|---|---|
| [docs/core/README.md](core/README.md) | Core definition, reading order, scope, and delivery state. |
| [docs/core/glossary.md](core/glossary.md) | Term definitions and kind/type/status distinctions. |
| [docs/core/typed-directional-object.md](core/typed-directional-object.md) | Identity, relevance, state dimensions, authority, relationships, and transitions. |
| [docs/core/compression-overlap-refinement.md](core/compression-overlap-refinement.md) | Operation contracts, resource accounting, recovery boundaries, and receipts. |
| [docs/core/directional-completeness.md](core/directional-completeness.md) | Predeclared requirements, per-direction predicates, and prospective regression cases. |
| [docs/interfaces/geometry-to-relational-state.md](interfaces/geometry-to-relational-state.md) | Explicit proposed mapping and transfer obligations. |
| [docs/interfaces/excellence-engine-v4.md](interfaces/excellence-engine-v4.md) | HELD relevance and the field-to-custody contract. |
| [docs/repository-map.md](repository-map.md) | This map. |
| [CHANGELOG.md](../CHANGELOG.md) | Documentation changes and evidence boundaries. |

## Planned paths — not implemented

These are planning labels, not links to existing components.

| Proposed path | Future responsibility |
|---|---|
| `schemas/` | Machine-readable field-object, transformation-receipt, and evaluation-receipt contracts. |
| `src/kakeyalogic/` | Reference field representation, transformations, lineage checks, and completeness evaluation. |
| `tests/` | Contract and regression tests; historical kernel-suite restoration is separate work. |
| `examples/typed_directional_state/` | Synthetic recovery and failure examples. |
| `docs/evaluation/longitudinal-retention.md` | Matched longitudinal evaluations and response-timing protocol. |
| `.github/workflows/verify.yml` | Automated verification, separate from deployment. |

Mount Olympus Fitness and authorized Computacenter workflows are possible later evaluation environments. No private operational records, participant data, or new data access are introduced by this documentation update.

## Cross-repository ownership

| Owner | Responsibility |
|---|---|
| KakeyaLogic | Geometric field, new field contracts, existing public artifacts, and proposed field-side checks. |
| [Excellence Engine Version 4](https://github.com/Manny536/excellence-engine-v4) | Custody engine, HELD predicates, engine schema, pipeline, and engine evaluations. |
| [Claude V6 research repository](https://github.com/Manny536/claude-v6) | Its theorem ledger and spectral claim status. |
| [LoveLabs-LCA](https://github.com/Manny536/LoveLabs-LCA) | Its relational research and application studies. |

The other repositories are linked, not modified or declared synchronized by this update.

## Historical receipt boundary

The [engineering report](reports/peaice-l2c-probe-engineering-report.md) and [earlier pull-request record](https://github.com/Manny536/kakeyalogic/pull/2) record the corrected **49 passed** result. That result is historical.

The inspected main tree contains no `tests/` directory or `tests/test_l2c_probe.py`. The only existing workflow is static deployment. The new documentation neither restores the suite nor supplies a current test pass. The report and historical artifacts remain intact; the root overview now makes their scope explicit.

When adding later components, update this map, the documentation index, and their implementation status together.

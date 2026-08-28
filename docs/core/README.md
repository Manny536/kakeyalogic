# KakeyaLogic core foundations

**Specification version:** 0.1

**Date:** 2026-08-28

**State:** DOCUMENTED DEFINITIONS AND CONTRACTS; implementation and behavioral validation planned.

## Definition

KakeyaLogic is a research architecture for typed directional completeness within artificial intelligence systems: preserving required directions and their identities, classifications, provenance, authority, status, and relationships through compression, overlap, and refinement.

A direction is a distinguishable route of relevance through system state, such as a claim connected to its evidence, correction, constraints, and consequences. A task declares which directions it requires. Completeness is assessed against that declared set, not against all possible knowledge.

## The core question

Can a system reduce a complex representation, allow directions to share structure, and recover finer distinctions without losing a required direction or silently changing what it means, supports, or authorizes?

The three operations are:

- **Compression:** reduce a declared representation cost while retaining required distinctions and recovery support.
- **Overlap:** share representational space while keeping distinct identities and roles recoverable.
- **Refinement:** resolve finer distinctions using retained information or explicitly retrieved sources, with lineage intact.

They may recur or interleave. Overlap is a representational condition, not a mandatory second processing step. Refinement is not automatically the inverse of compression.

## HELD and active

**HELD means relevant and retained.** Relevance is recorded against a research or task scope, with a reason for retaining the object. An active object is a HELD object selected for the current operation.

HELD does not automatically imply active, true, verified, approved, or executable. A disputed claim or disproved hypothesis can remain relevant and HELD as part of a correction history. Relevance is not evidence that the claim is true.

Custody, epistemic standing, activation, and approval are separate state dimensions. The [custody interface](../interfaces/excellence-engine-v4.md) preserves the separate engine's ownership of custody implementation.

## Reading order

| Document | Question answered |
|---|---|
| [Glossary](glossary.md) | What do the terms mean? |
| [Typed directional object](typed-directional-object.md) | What must an object and its relationships record? |
| [Transformation contracts](compression-overlap-refinement.md) | What can change, and what must survive? |
| [Directional completeness](directional-completeness.md) | How will preservation be assessed? |
| [Geometry-to-state interface](../interfaces/geometry-to-relational-state.md) | What connects the geometric and computational layers? |
| [Custody interface](../interfaces/excellence-engine-v4.md) | How does the field exchange relevant retained objects with the engine? |
| [Repository map](../repository-map.md) | Where do the existing and planned components live? |

## Scope and ownership

This core supplies computational definitions and proposed evaluation contracts. It preserves the existing geometric research, finite numerical probes, operator research, and historical artifacts. It does not claim that those artifacts already implement the new contracts.

KakeyaLogic owns the field representation, transformation requirements, and completeness checks. Excellence Engine Version 4 owns its custody predicates and runtime. The separate theorem ledger retains ownership of its mathematical claim status.

The word **kind** here is a broad schema category, not a claim that the project has implemented a formal programming-language kind system. The word **typed** requires enforceable rules; prose definitions alone do not demonstrate enforcement.

## Delivery state

| Component | State in this update |
|---|---|
| Definitions, glossary, object contract, and transformation contract | Documented |
| Required-direction and completeness specification | Documented; evaluation implementation pending |
| Geometric-to-computational mapping | Proposed; transfer obligations explicit |
| Machine-readable schemas and reference implementation | Planned; not supplied here |
| Contract tests and new performance measurements | Planned; no behavioral pass claimed |
| Custody-engine adoption of this interface | Pending coordination; not performed here |
| Existing geometric and spectral research | Preserved; no theorem-status changes |

The historical **49 passed** receipt concerns the earlier protected-sector probe work, not this foundation. See the [verification notes](../../README.md#8-verification-protocol).

Riemann Hypothesis OPEN; Coleman Conjecture OPEN; `h < 1` retained in its existing evaluator-boundary role. No provider policy, permission, or human-approval boundary is changed by this specification.

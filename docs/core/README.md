# KakeyaLogic core foundations

**Specification version:** 1.0

**Date:** 2026-09-08

**State:** DOCUMENTED DEFINITIONS, TRANSFORMATION CONTRACTS, AND FIVE-GRAIN ROUTING SPECIFICATION; reference implementation and behavioral validation remain planned.

## Definition

KakeyaLogic is a research architecture and proposed routing procedure for **typed directional completeness under transformation**. Every required direction is evaluated through five non-compensatory grains:

$$
\mathcal G=\{S,A,V,E,R\},
$$

where **S = Semantic, A = Authority, V = Visibility, E = Enforceability, R = Retention**.

A direction is a distinguishable route of relevance through system state, such as a claim connected to its evidence, correction, constraints, and consequences. A grain is a preservation dimension evaluated along that direction. A task declares which directions and grain obligations it requires. Completeness is assessed against that declared set, not against all possible knowledge.

The finite KakeyaLogic evaluation field is

$$
\mathcal D_{\mathrm{required}}\times\mathcal G.
$$

The five grains are not interchangeable weights and are not a scalar safety score. A strong Semantic result cannot compensate for failed Authority; route efficiency cannot compensate for failed Enforceability; missing Visibility cannot be treated as evidence of preservation.

## The five grains

| Grain | Requirement |
|---|---|
| **Semantic (S)** | Required meaning, distinctions, prohibitions, qualifications, and relation roles survive transformation. |
| **Authority (A)** | Source, scope, custody, approval, and write authority remain correctly distinguished and are never inferred from wording or proximity. |
| **Visibility (V)** | Evidence needed to inspect preservation, loss, uncertainty, or boundary erosion remains observable or explicitly unresolved. |
| **Enforceability (E)** | The system or surrounding control layer can block, contain, reverse, or refuse a transition when the declared obligation requires it. |
| **Retention (R)** | Required state, corrections, revocations, evidence, red lines, and relationships remain live and recoverable through time and later transformation. |

See [Five-grain routing](five-grain-routing.md) for the routing gate, unresolved-state treatment, Geodecis interface, interior preservation test, and containment separation.

## The core question

Can a system reduce a complex representation, allow directions to share structure, recover finer distinctions, and select a continuation **without losing a required direction or any required Semantic, Authority, Visibility, Enforceability, or Retention obligation**?

The three established representation operations remain:

- **Compression:** reduce a declared representation cost while retaining required distinctions and recovery support.
- **Overlap:** share representational space while keeping distinct identities, roles, and grain states recoverable.
- **Refinement:** resolve finer distinctions using retained information or explicitly retrieved sources, with lineage intact.

They may recur or interleave. Overlap is a representational condition, not a mandatory second processing step. Refinement is not automatically the inverse of compression.

## KakeyaLogic routing

Candidate transitions are partitioned by their required grain outcomes:

```text
PASS
UNRESOLVED
FAIL
NOT_EVALUATED
```

A candidate transition is **admitted for planning** only when every required grain passes. Unresolved and failed transitions remain represented with evidence and obligations but do not enter the admitted planner graph.

The routing sequence is:

```text
Observe → Grain → Gate → Overlap → Refine → Route → Receipt → Retain
```

KakeyaLogic constructs the admitted transition geometry. **Geodecis** is the proposed downstream route-selection layer: given an explicitly declared operational edge cost, it chooses among admitted continuations. The cost is not a Love-Squared Coherence, truth, ethics, or safety score.

A valid planned route does not establish containment of all states the deployed system may be able to reach. Planning and reachability/containment require separate receipts.

## HELD and active

**HELD means relevant and retained.** Relevance is recorded against a research or task scope, with a reason for retaining the object. An active object is a HELD object selected for the current operation.

HELD does not automatically imply active, true, verified, approved, or executable. A disputed claim, failed grain, unresolved transition, or disproved hypothesis can remain relevant and HELD because its evidence and correction history matter.

Custody, epistemic standing, activation, approval, and lifecycle remain separate state dimensions. The [custody interface](../interfaces/excellence-engine-v4.md) preserves the separate engine's ownership of custody implementation.

## Reading order

| Document | Question answered |
|---|---|
| [Glossary](glossary.md) | What do the terms, directions, grains, and statuses mean? |
| [Typed directional object](typed-directional-object.md) | What must an object and its relationships record? |
| [Transformation contracts](compression-overlap-refinement.md) | What can change, and what must survive? |
| [Directional completeness](directional-completeness.md) | How are required directions and per-direction checks assessed? |
| [Five-grain routing](five-grain-routing.md) | How do SAVER grains gate transitions and expose Geodecis routing? |
| [Geometry-to-state interface](../interfaces/geometry-to-relational-state.md) | What connects the geometric and computational layers? |
| [Custody interface](../interfaces/excellence-engine-v4.md) | How does the field exchange relevant retained objects with the engine? |
| [Repository map](../repository-map.md) | Where do the existing and planned components live? |

## Scope and ownership

This core supplies computational definitions and proposed evaluation/routing contracts. It preserves the existing geometric research, finite numerical probes, operator research, and historical artifacts. It does not claim that those artifacts already implement the 1.0 contracts.

KakeyaLogic owns the field representation, transformation requirements, five-grain admission logic, and completeness checks. Excellence Engine Version 4 owns its custody predicates and runtime. The separate theorem ledger retains ownership of its mathematical claim status.

The word **kind** here is a broad schema category, not a claim that the project has implemented a formal programming-language kind system. The word **typed** requires enforceable rules; prose definitions alone do not demonstrate enforcement.

## Delivery state

| Component | State in specification 1.0 |
|---|---|
| Definitions, glossary, object contract, and transformation contract | Documented |
| Required-direction and completeness specification | Documented; evaluation implementation pending |
| Five-grain SAVER routing contract | Documented; runtime implementation pending |
| Geodecis admitted-distance interface | Proposed and defined; implementation pending |
| Interior boundary-loss test | Specified; not yet executed |
| Reachability / containment separation | Specified; operational coverage remains OPEN |
| Geometric-to-computational mapping | Proposed; transfer obligations explicit |
| Machine-readable schemas and reference implementation | Planned; not supplied here |
| Contract tests and new performance measurements | Planned; no behavioral pass claimed |
| Custody-engine adoption of this interface | Pending coordination; not performed here |
| Existing geometric and spectral research | Preserved; no theorem-status changes |

The historical **49 passed** receipt concerns the earlier protected-sector probe work, not this foundation or five-grain routing specification.

Riemann Hypothesis OPEN; Coleman Conjecture OPEN; operational SIUT validity OPEN; `h < 1` retained in its existing evaluator-boundary role. No provider policy, permission, or human-approval boundary is changed by this specification.

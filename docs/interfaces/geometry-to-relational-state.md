# Geometry-to-relational-state interface

**Specification version:** 1.0

**State:** MAPPING PROPOSAL; no automatic theorem transfer.

## Purpose

The existing repository develops directional geometry, scale persistence, incidence, overlap, and separation rules. The computational core uses these as a research starting point while defining its own observable objects and checks.

Primary in-repository references:

- [Directional geometry and multiscale probe](../guth-wang-bateman-zahl-probe.md).
- [Kakeya Needle Set, Light Basic: typed observability and separation](../kns-light-basic.md).
- [Inspectable Intelligence: existing claim discipline](../inspectable-intelligence.md).
- [Five-grain routing specification](../core/five-grain-routing.md).

The cited documents retain their own status statements. This interface does not re-prove their mathematical claims or upgrade their proposed bridges.

## Explicit mapping

| Geometric layer | Proposed computational counterpart | Required boundary |
|---|---|---|
| Required direction family | Declared set of task-relevant routes through typed state | A semantic route is not automatically a vector or a unit segment. |
| Tube representing a direction | Identifiable representation of a required route and its source objects | The encoding and recovery procedure must be specified. |
| Incidence relationships | Typed edges between objects, sources, corrections, and constraints | Edge meanings and orientation must survive; adjacency alone is insufficient. |
| Shading or selected support | A selected active view of retained objects | An active view is not the entire HELD state. |
| Overlap and multiplicity | Shared clusters, summary units, or representation regions | High multiplicity alone does not establish conflation or failure. |
| Coarse/fine scale hierarchy | Project, lane, cluster, claim, source-detail, and transformation-interior levels | The aggregation and refinement rules must be declared. |
| Union footprint | A specified representation-cost measure | Prompt tokens, storage, retrieval costs, and route costs are different measurements. |
| Geometric separation rule | Tests against inferring authority or hidden structure from shared representation | The computational rule needs its own contract and evaluation. |
| Directional preservation field | Required directions × Semantic, Authority, Visibility, Enforceability, Retention grains | The five grains are computational preservation dimensions, not imported geometric coordinates. |
| Admitted path | Sequence of transitions whose declared required grains all PASS | Admission is an evidence/control rule, not a Kakeya theorem consequence. |
| Geodecis distance | Least declared operational cost among admitted paths | This is an explicit graph-distance construction; it is not inferred from $L^2_C$ notation or geometric tube length. |

## What may be carried forward

The geometric program motivates three inspectable questions:

1. Is every required direction represented?
2. Can overlapping directions be distinguished?
3. Do supporting relationships survive scale changes?

Specification 1.0 adds two operational questions:

4. Do the required **Semantic, Authority, Visibility, Enforceability, and Retention** grains survive along each required direction?
5. Which transitions are therefore admitted, unresolved, or failed before route selection?

The computational core answers these through [object records](../core/typed-directional-object.md), [transformation receipts](../core/compression-overlap-refinement.md), [per-direction tests](../core/directional-completeness.md), and the [five-grain routing gate](../core/five-grain-routing.md).

## Routing geometry

KakeyaLogic 1.0 constructs a finite, time-indexed admitted transition structure after grain evaluation. Given an explicitly chosen positive edge-cost function $\ell_t$, the Geodecis layer may define an admitted path distance

$$
d_{C,t}^{A}(x,g)
=
\inf_{\gamma:x\rightsquigarrow g,\;\gamma\subseteq E_t^A}
\sum_{e\in\gamma}\ell_t(e).
$$

For one-way transformations this distance may be asymmetric. Symmetry, geodesic completeness, hyperbolicity, or other metric-geometric properties must be established separately for the chosen realization.

The subscript $C$ records the Love-Squared Coherence research context; it does not claim that this graph distance is mathematically implied by the notation $L^2_C$.

## Unknowns and interior structure

An unresolved transition remains represented even when it is excluded from the admitted planner graph. Non-admission does not establish non-reachability.

Likewise, endpoint preservation does not establish preservation through a transformation interior. If a claimed transition passes at $x$ and $y$ but a required grain fails at an inspectable intermediate state, the transition fails admission at that claimed scale.

This creates a direct role for multiscale refinement: coarse edges may need to be resolved into finer states before Semantic, Authority, Visibility, Enforceability, or Retention can be evaluated honestly.

## What remains to be established

Before importing a quantitative geometric estimate into a system claim, specify the encoding, spaces, measures, scale parameters, admissibility hypotheses, observable quantities, and any distortion introduced by the mapping. Show that the hypotheses hold for the actual system representation.

Neither an attractive visualization nor a successful finite recovery or routing test supplies those obligations. A semantic embedding is not assumed to satisfy Kakeya hypotheses. No claim about hidden neural attention follows from an observable retrieval or output trace.

Keep existing symbols scoped: geometric scale ratio, numerical leakage, evaluator authority boundaries, SAVER grain states, and operational route costs are not interchangeable because they share notation or analogy. In particular, `h < 1` retains its declared evaluator-boundary role here; it is not a measured probability of correctness.

Hyperbolicity remains a separate geometric hypothesis. It may later characterize the structure or predictability of a realized routing graph, but it does not establish safeguard preservation or containment.

Riemann Hypothesis OPEN; Coleman Conjecture OPEN. Existing closed-negative spectral routes are not reopened by specification 1.0.

## Practical boundary

KakeyaLogic's computational target is faithful, task-scoped recovery and routing of typed state under non-compensatory five-grain preservation requirements. This interface provides the proposed bridge from geometric vocabulary to observable system objects; it does not claim that directional geometry alone proves artificial-intelligence reliability.

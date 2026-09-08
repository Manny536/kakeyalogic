# KakeyaLogic five-grain routing contract

**Specification version:** 1.0

**Date:** 2026-09-08

**State:** DOCUMENTED ROUTING SPECIFICATION; reference implementation, calibration, and behavioral validation remain pending.

## Definition

KakeyaLogic extends typed directional completeness with a five-grain preservation field carried by every required direction:

$$
\mathcal G = \{S,A,V,E,R\},
$$

where:

- **Semantic (S):** the required meaning, distinction, prohibition, relation, or qualification remains the same through transformation.
- **Authority (A):** source, scope, custody, approval, and write authority remain correctly distinguished; authority is never created by wording, proximity, or type labels.
- **Visibility (V):** the evidence required to inspect preservation, loss, uncertainty, or boundary erosion remains observable or explicitly unresolved.
- **Enforceability (E):** the system or surrounding control layer can actually block, contain, reverse, or refuse a transition when the declared obligation requires it.
- **Retention (R):** the required state, correction, red line, evidence, and relationships remain live and recoverable through time, update, and later transformation.

These are **grains**, not interchangeable weights and not a scalar safety score. A strong grain cannot compensate for a failed required grain.

## Direction versus grain

A **direction** remains a distinguishable route of relevance through typed state. A **grain** is one preservation dimension evaluated along that direction.

For each required direction $d$, define its grain bundle

$$
K_t(d)=\bigl(S_t(d),A_t(d),V_t(d),E_t(d),R_t(d)\bigr).
$$

The finite evaluation field is therefore

$$
\mathcal D_{\mathrm{required}}\times\mathcal G.
$$

The five-grain layer does not replace the existing identity, content, classification, status, provenance, relationship, recovery, and history checks. Those checks supply evidence to one or more grain predicates.

## Grain outcomes

Each required direction-grain pair receives an explicit outcome:

```text
PASS
UNRESOLVED
FAIL
NOT_EVALUATED
```

- **PASS:** the declared grain obligation is supported by the specified evidence and check.
- **UNRESOLVED:** the transition or state remains relevant and visible, but evidence is insufficient to establish preservation or failure.
- **FAIL:** an observable condition contradicts the declared grain obligation.
- **NOT_EVALUATED:** the required check has not been performed. It is not a pass and must not be silently collapsed into UNRESOLVED.

Unknowns remain first-class. Excluding an unresolved transition from routing does not establish that the deployed system cannot execute it.

## Candidate transformations

Let a candidate transformation be

$$
e:x\rightarrow y.
$$

Examples include deployment, delegation, scaling, compression, configuration change, tool use, customer transfer, context shift, and organizational transfer. These transformations are environments through which grains are tested; they are not themselves KakeyaLogic grains.

For each candidate edge $e$, evaluate the required grain predicates

$$
P_{d,q}(e),\qquad q\in\mathcal G.
$$

A transition is **admitted for planning** only when every grain required by its declared contract passes:

$$
e\in E_t^{A}
\iff
\bigwedge_{q\in Q_e}P_q(e)=\mathrm{PASS}.
$$

No weighted sum may override this gate. Semantic quality cannot compensate for missing authority, route efficiency cannot compensate for failed enforceability, and apparent endpoint correctness cannot compensate for unresolved visibility.

## Three transition sets

KakeyaLogic routing distinguishes three sets:

$$
E_t^{A}=\{e:\text{all required grains PASS}\},
$$

$$
E_t^{U}=\{e:\text{no required grain FAILS and at least one is UNRESOLVED or NOT\_EVALUATED}\},
$$

$$
E_t^{F}=\{e:\text{at least one required grain FAILS}\}.
$$

The sets have different roles:

- **Admitted** transitions may enter the planner.
- **Unresolved** transitions remain represented with their missing evidence and obligations but are not admitted.
- **Failed** transitions remain represented as falsification evidence and are not admitted.

Deleting unresolved or failed edges from the research state would erase evidence and weaken later refinement.

## KakeyaLogic routing loop

At state $x_t$:

1. **Observe** candidate continuations and their typed source objects.
2. **Grain** each continuation across Semantic, Authority, Visibility, Enforceability, and Retention.
3. **Gate** candidates into admitted, unresolved, and failed sets.
4. **Overlap** shared representation without merging independently recoverable direction identity or grain state.
5. **Refine** coarse or unresolved representations when retained or permitted sources can expose finer evidence.
6. **Route** only through admitted transitions.
7. **Receipt** the selected transformation, evidence, outcomes, and unresolved alternatives.
8. **Retain** and re-evaluate longitudinally after later updates or transformations.

Compactly:

```text
Observe → Grain → Gate → Overlap → Refine → Route → Receipt → Retain
```

## Geodecis interface

KakeyaLogic constructs the admitted transition geometry. **Geodecis** is a proposed route-selection layer inside that geometry.

Given positive operational edge costs $\ell_t(e)$ and destination $g$, define

$$
d_{C,t}^{A}(x,g)
=
\inf_{\gamma:x\rightsquigarrow g,\;\gamma\subseteq E_t^A}
\sum_{e\in\gamma}\ell_t(e).
$$

For directed transformations this distance may be asymmetric; no symmetry is assumed.

A Geodecis next-step policy may select

$$
y^*\in
\arg\min_{(x,y)\in E_t^A}
\left[\ell_t(x,y)+d_{C,t}^{A}(y,g)\right].
$$

The cost is explicitly operational. It is **not** a safety, ethics, truth, or Love-Squared Coherence score. KakeyaLogic determines admissibility; Geodecis chooses among admitted continuations under the declared cost model.

## Uncertainty-visible distance

To keep known unknowns visible, define

$$
E_t^{\Diamond}=E_t^A\cup E_t^U
$$

and

$$
d_{C,t}^{\Diamond}(x,g)
=
\inf_{\gamma:x\rightsquigarrow g,\;\gamma\subseteq E_t^{\Diamond}}
\sum_{e\in\gamma}\ell_t(e).
$$

When both distances are finite, define

$$
\Delta_t^{\mathrm{evid}}(x,g)
=
d_{C,t}^{A}(x,g)-d_{C,t}^{\Diamond}(x,g)\ge 0.
$$

This is an **evidence-sensitivity diagnostic**, not permission to traverse unresolved edges. It reports how much the preferred route could change if unresolved evidence were later resolved favorably.

## Interior preservation test

Endpoint agreement is insufficient. A transformation may begin and end in apparently acceptable states while losing a required grain internally.

Represent the realized transformation as

$$
\rho_e:[0,1]\rightarrow\mathcal X,
\qquad
\rho_e(0)=x,
\qquad
\rho_e(1)=y.
$$

For every required grain $q$, admission requires the declared obligation to hold across the inspectable realization at the scale claimed by the test:

$$
\forall u\in[0,1],\qquad P_q(\rho_e(u))=\mathrm{PASS},
$$

or an equivalent declared discrete refinement.

A boundary-error falsifier is

$$
P_q(x)=\mathrm{PASS},
\quad
P_q(y)=\mathrm{PASS},
\quad
\exists u\in(0,1):P_q(\rho_e(u))=\mathrm{FAIL}.
$$

If the interior cannot be observed at the resolution needed to establish the claim, the relevant Visibility grain remains UNRESOLVED and the edge is not admitted at that claimed level.

## Planning is not containment

A selected admitted route does not establish that every executable alternative is contained.

Maintain a separate reachability model with

$$
\mathcal R_t^{-}(x)
\subseteq
\mathcal R_t(x)
\subseteq
\mathcal R_t^{+}(x),
$$

where $\mathcal R_t^{-}$ contains confirmed-reachable states and $\mathcal R_t^{+}$ is a conservative modeled envelope of possibly reachable states.

A containment evaluation may report:

```text
FAIL       confirmed reachable state violates the allowed boundary
PASS_MODEL conservative modeled envelope remains inside the allowed boundary
OPEN       coverage is insufficient to establish either result
```

`PASS_MODEL` is conditional on the reachability model. An admitted planner path and a containment result are separate receipts.

## Compression, overlap, refinement, and grains

The existing transformation contracts remain controlling. The five-grain layer adds a preservation view over them:

- **Compression:** reducing representation cost must not silently drop a required grain obligation or the evidence needed to evaluate it.
- **Overlap:** shared representation must preserve independently recoverable direction identity and independently inspectable grain state.
- **Refinement:** finer recovery must restore grain evidence and lineage without inventing missing content or authority.
- **Retention:** later state must preserve justified corrections, revocations, evidence, and unresolved gaps rather than merely reproducing old wording.

A compact representation is valid only when the required typed distinctions and required grain states remain recoverable under the declared budget and permissions.

## Strict grain completeness

For a fixed required-direction set, define strict KakeyaLogic grain completeness as

$$
\operatorname{KComplete}(X)
\iff
\bigwedge_{d\in\mathcal D_{\mathrm{required}}}
\bigwedge_{q\in Q_d}
P_{d,q}(X)=\mathrm{PASS}.
$$

A failed, unresolved, or not-evaluated required grain blocks a strict completeness claim. Diagnostic summaries may be reported, but no aggregate score overrides a failing required grain.

## Relationship to Love-Squared Coherence and SIUT

This document does not infer a metric from the notation $L^2_C$. Love-Squared Coherence remains the surrounding relational and custody research framework. The operational distance above is an explicitly chosen construction on the admitted graph.

Safeguard Integrity Under Transformation (SIUT) supplies the preservation problem: beneficial constraints must remain semantically intact, correctly authorized, observable, enforceable, and retained under transformation. KakeyaLogic supplies the typed directional and five-grain routing representation used to inspect that problem.

## Implementation status

This specification adds no current runtime enforcement and claims no behavioral pass. A reference implementation should begin with a synthetic graph and test:

1. a shortest admitted route;
2. an unresolved shortcut that remains visible but is not traversed;
3. a failed transition that remains retained as evidence;
4. an endpoint-pass / interior-fail transformation;
5. a retention regression after a later state update;
6. a separate containment verdict showing that a valid planned route does not establish containment of all reachable alternatives.

The operational SIUT validity of this realization remains **OPEN** until those tests and later deployment evidence exist.

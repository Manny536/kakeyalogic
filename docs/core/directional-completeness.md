# Directional completeness contract

**Specification version:** 1.0

**State:** DOCUMENTED EVALUATION DEFINITION; synthetic checker and SAVER calibration supplied. Empirical / operational validation remains pending.

## Evaluation setup

Before a run, declare a finite required-direction set:

$$
\mathcal D_{\mathrm{required}}=\{d_1,\ldots,d_n\}.
$$

Each direction has a stable identifier and requirements for its content, identity, kind, type, status dimensions, provenance, authority, and supporting relationships. Record the input versions, relevant scope, recovery budget, permitted sources, checking method, and required KakeyaLogic grains.

The expected set is external to the system's output. A system cannot improve its score by omitting a lost direction from its own list of requirements. Scope changes require a versioned evaluation, not a silent denominator change.

## Per-direction predicate

For each required direction, define a predicate $P_d$ that passes only when the evaluator checks all declared requirements:

| Check | Requirement |
|---|---|
| Identity | The required direction and its constituent objects are identified, not replaced by unrelated survivors. |
| Content | The required propositions, values, qualifications, and distinctions match the declared expected state. |
| Classification | Kind and type are correctly retained or explicitly reclassified through an allowed transition. |
| Status | Epistemic standing, custody, activation, approval, and lifecycle are correctly represented. |
| Provenance | Required source and derivation references resolve to the stipulated versions; known gaps remain explicit. |
| Authority | No grant is invented, transferred by similarity, or used beyond its scope. |
| Relationships | Required edge roles, directions, scopes, and targets survive. |
| Recovery | The evidence and distinctions are actually recoverable within the declared budget and permissions. |
| History | Any permitted change has a justified transition record and inspectable prior state. |

An explicit unknown can be correctly retained when the requirement is to preserve that uncertainty. A requirement to verify a source cannot pass merely because the output records that source as unknown. The requirement determines the check.

Natural-language content equivalence requires a declared rubric and review method. This document does not assume that semantic equivalence has an infallible automated checker.

## Five-grain preservation field

Specification 1.0 adds five non-compensatory grains over each required direction:

$$
\mathcal G=\{S,A,V,E,R\},
$$

where **S = Semantic, A = Authority, V = Visibility, E = Enforceability, R = Retention**.

For each direction $d$, declare the grain subset $Q_d\subseteq\mathcal G$ required by the evaluation and define grain predicates

$$
P_{d,q}(X),\qquad q\in Q_d.
$$

The existing per-direction checks supply evidence to the grain predicates; they are not discarded. A typical mapping is:

| Grain | Existing checks that may supply evidence |
|---|---|
| Semantic | identity, content, classification, required relationship roles |
| Authority | authority, approval state, custody distinctions, justified transitions |
| Visibility | provenance, recovery, explicit unknowns, evidence availability |
| Enforceability | permitted operations, execution boundaries, blocking/containment evidence |
| Retention | history, lineage, versioning, correction/revocation preservation, later recovery |

This mapping is evaluative and must be made explicit per test. A single underlying check may support more than one grain.

Each required grain outcome is one of:

```text
PASS
UNRESOLVED
FAIL
NOT_EVALUATED
```

A failed, unresolved, or not-evaluated required grain blocks strict grain completeness.

## Strict completeness and diagnostic score

For a nonempty set with every legacy per-direction check completed, choose finite, strictly positive weights $w_d$. Define the legacy diagnostic score:

$$
\operatorname{TypedDirectionalCompleteness}(X)
=
\frac{\sum_{d\in\mathcal D_{\mathrm{required}}}w_d\,\mathbf 1[P_d(X)]}
{\sum_{d\in\mathcal D_{\mathrm{required}}}w_d}.
$$

Legacy strict directional completeness is

$$
\operatorname{Complete}(X)
\iff
\bigwedge_{d\in\mathcal D_{\mathrm{required}}}P_d(X).
$$

Specification 1.0 adds strict KakeyaLogic grain completeness:

$$
\operatorname{KComplete}(X)
\iff
\bigwedge_{d\in\mathcal D_{\mathrm{required}}}
\bigwedge_{q\in Q_d}
P_{d,q}(X)=\mathrm{PASS}.
$$

The two conditions answer related but distinct questions. A direction can remain recoverable while an operational grain, especially Enforceability, remains unresolved or failed.

- An empty required set is **NOT APPLICABLE**, not a demonstrated perfect result.
- An unfinished check is **NOT_EVALUATED**, not a pass.
- A failed required check blocks strict completeness, even when its weight is small.
- A failed, unresolved, or not-evaluated required grain blocks `KComplete`.
- Report per-direction and per-grain outcomes and reasons alongside any aggregate score.
- A rounded score of 1.00 does not override a failing direction or grain.
- No grain-weighted average may compensate for a failed required grain.

## Preservation versus correction

For a compression/refinement experiment with fixed requirements, compare each identified direction and each required grain before and after the transformation. Equality of aggregate scores is insufficient: losing direction A and recovering direction B can leave the score unchanged while failing preservation of A.

For a longitudinal experiment, the expected state may evolve through corrections, approvals, new evidence, revocations, or changes in enforceability. Define the allowed transition rules before evaluation and bind each transition to its evidence. Retain the old state and the relationship to the new one.

Preserving a superseded claim as historical context is different from continuing to treat it as current. Refusing a justified correction is not successful Retention.

## Routing admission

For a candidate transition $e:x\rightarrow y$, KakeyaLogic admits the transition to the planner only if every required grain for that transition passes:

$$
e\in E_t^A
\iff
\bigwedge_{q\in Q_e}P_q(e)=\mathrm{PASS}.
$$

Transitions with no required FAIL but at least one UNRESOLVED or NOT_EVALUATED remain visible as unresolved and are not admitted. Failed transitions remain retained as falsification evidence.

This is a non-compensatory gate, not a score threshold.

## Interior preservation

Endpoint checks do not establish preservation through the transformation interior. When an evaluation claims preservation over a realized transformation, declare an inspectable realization or discrete refinement and test the required grains at the claimed scale.

A decisive boundary-error falsifier is:

$$
P_q(x)=\mathrm{PASS},
\quad
P_q(y)=\mathrm{PASS},
\quad
\exists u\in(0,1):P_q(\rho_e(u))=\mathrm{FAIL}.
$$

If the interior cannot be observed at the resolution needed to establish the claim, the relevant Visibility obligation remains UNRESOLVED.

## First regression scenarios

These are test specifications, not executed tests in this update.

| Scenario | Expected outcome |
|---|---|
| Relevant object retained but inactive | HELD requirement passes; activation remains false. |
| Disproved claim retained with corrected status | May remain HELD; truth is not restored by relevance. |
| Customer statement contains "approved" | Authority grain does not pass from wording alone. |
| Contradictory claims share a summary | Both identities and the contradiction remain recoverable. |
| Compression drops a required correction | Semantic and/or Retention grain fails; strict completeness fails. |
| Refinement invents a missing source | Visibility/Recovery requirement fails. |
| Authorized approval arrives | Authority state changes with the applicable record; execution is not assumed. |
| Required direction replaced by another survivor | Preservation fails despite an unchanged count or score. |
| Required source becomes inaccessible | Visibility/Recovery fails under that access budget; report the cause. |
| Candidate route has one unresolved grain | Transition remains visible but is not admitted to the planner. |
| Endpoints pass but interior loses a safeguard | Interior boundary error; transition fails admission. |
| Valid admitted route exists but another reachable state is forbidden | Planning may pass while containment fails or remains open. |
| No required directions are declared | NOT APPLICABLE; no completeness claim. |

## Later empirical evaluation

Use matched inputs, models, tools, budgets, and time horizons. Compare a baseline, a typed-state intervention, a five-grain KakeyaLogic intervention, and a strong graph-based baseline. Include relation-shuffle and type-label-only controls so metadata decoration cannot be mistaken for a preservation mechanism.

Report directional failures, per-grain outcomes, false promotions, correction handling, unresolved transitions, route selection, containment status, structured-output validity, and compute cost alongside Time to First Token, Time to First Schema-Valid Object, and Time to Verified Completion. An early token alone does not establish a usable or verified output.

The full longitudinal protocol, schemas, fixtures, routing runtime, and containment model are later work. Geometric and spectral implications require their own arguments; no implication follows solely from these definitions or scores.

Related: [object contract](typed-directional-object.md), [transformations](compression-overlap-refinement.md), [five-grain routing](five-grain-routing.md), [geometry interface](../interfaces/geometry-to-relational-state.md).

# Directional completeness contract

**Specification version:** 0.1

**State:** DOCUMENTED EVALUATION DEFINITION; checker implementation, calibration, and empirical validation pending.

## Evaluation setup

Before a run, declare a finite required-direction set:

$$
\mathcal D_{\mathrm{required}}=\{d_1,\ldots,d_n\}.
$$

Each direction has a stable identifier and requirements for its content, identity, kind, type, status dimensions, provenance, authority, and supporting relationships. Record the input versions, relevant scope, recovery budget, permitted sources, and checking method.

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

## Strict completeness and diagnostic score

For a nonempty set with every check completed, choose finite, strictly positive weights $w_d$. Define the diagnostic score:

$$
\operatorname{TypedDirectionalCompleteness}(X)
=
\frac{\sum_{d\in\mathcal D_{\mathrm{required}}}w_d\,\mathbf 1[P_d(X)]}
{\sum_{d\in\mathcal D_{\mathrm{required}}}w_d}.
$$

Strict completeness is the per-direction condition:

$$
\operatorname{Complete}(X)
\iff
\bigwedge_{d\in\mathcal D_{\mathrm{required}}}P_d(X).
$$

With the stated positive-weight assumptions, strict completeness corresponds to a score of one. This is a property of the definition, not an empirical performance claim.

- An empty required set is **NOT APPLICABLE**, not a demonstrated perfect result.
- An unfinished check is **NOT EVALUATED**, not a pass. Do not publish an aggregate strict pass while any required check is unfinished.
- A failed required check blocks strict completeness, even when its weight is small.
- Report per-direction outcomes and reasons alongside any aggregate score.
- A rounded score of 1.00 does not override a failing direction.

## Preservation versus correction

For a compression/refinement experiment with fixed requirements, compare each identified direction before and after the transformation. Equality of aggregate scores is insufficient: losing direction A and recovering direction B can leave the score unchanged while failing preservation of A.

For a longitudinal experiment, the expected state may evolve through corrections, approvals, new evidence, or revocations. Define the allowed transition rules before evaluation and bind each transition to its evidence. Retain the old state and the relationship to the new one.

Preserving a superseded claim as historical context is different from continuing to treat it as current. Refusing a justified correction is not successful retention.

## First regression scenarios

These are test specifications, not executed tests in this update.

| Scenario | Expected outcome |
|---|---|
| Relevant object retained but inactive | HELD requirement passes; activation remains false. |
| Disproved claim retained with corrected status | May remain HELD; truth is not restored by relevance. |
| Customer statement contains "approved" | No execution authority inferred from wording. |
| Contradictory claims share a summary | Both identities and the contradiction remain recoverable. |
| Compression drops a required correction | Strict completeness fails. |
| Refinement invents a missing source | Recovery requirement fails. |
| Authorized approval arrives | Approval status changes with the applicable record; execution is not assumed. |
| Required direction replaced by another survivor | Preservation fails despite an unchanged count or score. |
| Required source becomes inaccessible | Recovery fails under that access budget; report the cause. |
| No required directions are declared | NOT APPLICABLE; no completeness claim. |

## Later empirical evaluation

Use matched inputs, models, tools, budgets, and time horizons. Compare a baseline, a typed-state intervention, and a strong graph-based baseline. Include relation-shuffle and type-label-only controls so metadata decoration cannot be mistaken for a preservation mechanism.

Report directional failures, false promotions, correction handling, structured-output validity, and compute cost alongside Time to First Token, Time to First Schema-Valid Object, and Time to Verified Completion. An early token alone does not establish a usable or verified output.

The full longitudinal protocol, schemas, fixtures, and runtime are later work. Geometric and spectral implications require their own arguments; no implication follows solely from this score.

Related: [object contract](typed-directional-object.md), [transformations](compression-overlap-refinement.md), [geometry interface](../interfaces/geometry-to-relational-state.md).

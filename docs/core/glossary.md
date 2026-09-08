# KakeyaLogic glossary

**Specification version:** 1.0

**State:** DOCUMENTED DEFINITIONS; enforcement remains an implementation obligation.

These definitions govern the computational core. Existing mathematical notation retains its stated native meaning; shared words or symbols do not establish a mathematical transfer.

## Object vocabulary

| Term | Definition |
|---|---|
| Object | An identifiable unit the system can store, inspect, relate, and process. |
| Content | The text, values, or other information carried by an object. |
| Identity | A stable reference distinguishing an object from other objects, including objects with identical text. |
| Version | A recorded revision of an object; changes remain linked to earlier versions. |
| Kind | A broad family used by the declared schema, such as research-related or action-related. |
| Type | The object's specific operational role, such as hypothesis, observation, correction, deployment request, or approval record. |
| Typed | Classified under explicit rules governing permitted interpretation, relationships, and operations. A decorative tag alone is insufficient. |
| Status | The object's current condition, represented through separate dimensions where necessary: epistemic standing, custody, activation, approval, and lifecycle. |
| Provenance | The object's source, source version, and derivation history, including known gaps. |
| Authority | Externally established, scoped permission governing what may be authorized, for whom, on which targets, and under which conditions. It is not created by an object's wording or type label. |
| Relationship | A typed connection such as supports, contradicts, corrects, requires approval from, derives from, or supersedes. |
| Lineage | The traceable history linking an object to sources, parents, versions, and transformations. |

## Relevance and custody vocabulary

| Term | Definition |
|---|---|
| Relevance | A recorded relationship between an object and a declared research or task scope. Relevance does not establish truth. |
| Relevance scope | The project, research question, task, or operation to which the relevance judgment applies. |
| Relevance basis | The reason and supporting context for retaining an object in that scope. |
| HELD | Relevant and retained within a declared scope, with its classification and available provenance, authority, status, and relationships preserved for recovery and use. Unknown fields remain explicit. |
| Active | A HELD object selected for use in the current operation. Selection for analysis does not imply permission to execute its content. |
| Approved | Supported by an applicable authorization record for a specified action and scope. |
| Verified | A specified claim or condition has passed a declared check with a traceable receipt. It is not blanket certification of the whole object. |
| Superseded | Replaced for a specified current use by a later object or version, while retaining the replacement relationship and history. |

**HELD implies relevance.** It does not automatically imply active, verified, approved, or executable. A counterexample, failed grain, unresolved transition, rejected proposal, or disproved hypothesis may remain HELD because its history matters.

## Directional and transformation vocabulary

| Term | Definition |
|---|---|
| Direction | A distinguishable route of relevance through state, such as a claim linked to evidence and correction. It is not automatically a geometric vector. |
| Required direction set | The finite set of directions a task or evaluation declares must survive, together with the requirements for each. |
| Scale | A declared level of detail or aggregation, such as project, lane, cluster, claim, or source passage. |
| Representation | The carrier used to make information available, such as a graph, structured summary, object store, or selected context. |
| Compression | Reducing declared representation size or cost while retaining required distinctions and recovery support. |
| Overlap | Multiple directions sharing representational space without losing independently recoverable identities, roles, or required grain states. |
| Refinement | Resolving finer distinctions using retained information or explicitly retrieved sources while preserving lineage. |
| Retention | Keeping required information, relationships, corrections, evidence, and grain state available through time and transformation. |
| Recovery | Actually retrieving or reconstructing required distinctions within declared resources and permissions. |
| Directional completeness | Every direction in the declared required set remains represented. |
| Typed directional completeness | Every required direction can be recovered with its required content, identity, classification, provenance, authority, status, and relationships correctly accounted for. |

## Five-grain vocabulary

The five KakeyaLogic grains are the non-compensatory preservation dimensions carried by each required direction:

| Grain | Definition |
|---|---|
| Semantic (S) | Preservation of the required meaning, distinction, prohibition, qualification, or relationship role under transformation. |
| Authority (A) | Preservation of correct source, scope, custody, approval, and write-authority distinctions under transformation. |
| Visibility (V) | Preservation of enough observable evidence to inspect preservation, loss, uncertainty, or boundary erosion; unresolved observability remains explicit. |
| Enforceability (E) | Preservation of the actual ability of the system or surrounding control layer to block, contain, reverse, or refuse a transition when required. |
| Retention (R) | Preservation through time of the required state, correction, red line, evidence, lineage, and relationships. |
| Grain bundle | The ordered five-grain state $K_t(d)=(S_t(d),A_t(d),V_t(d),E_t(d),R_t(d))$ attached to a required direction. |
| Grain field | The finite evaluation surface $\mathcal D_{\mathrm{required}}\times\{S,A,V,E,R\}$. |
| Grain gate | The non-compensatory admission rule requiring every declared grain obligation for a candidate transition to pass before the transition enters the admitted planner graph. |
| Strict grain completeness | The condition that every required direction and every required grain predicate passes. |

The grains are not weights. No aggregate score may convert a failed required grain into a pass.

## Routing vocabulary

| Term | Definition |
|---|---|
| Candidate transition | A possible state transformation $e:x\rightarrow y$ considered by the routing layer. |
| Admitted transition | A candidate transition whose declared required grain predicates all PASS. |
| Unresolved transition | A candidate with no required grain FAIL and at least one required grain UNRESOLVED or NOT_EVALUATED. It remains represented but is not admitted for planning. |
| Failed transition | A candidate with at least one required grain FAIL. It remains represented as evidence but is not admitted for planning. |
| Operational edge cost | An explicitly chosen positive cost used for route planning. It is not a safety, truth, ethics, or Love-Squared Coherence score. |
| Admitted distance | The least declared operational cost among paths composed only of admitted transitions. For directed transformations it may be asymmetric. |
| Geodecis | The proposed route-selection layer that chooses among KakeyaLogic-admitted continuations using the declared operational distance field. KakeyaLogic determines admissibility; Geodecis does not create authority or safety. |
| Reachability model | A separate model of states the deployed system may actually be capable of reaching. A planned admitted route does not establish containment of this set. |
| PASS_MODEL | A containment result stating that a conservative modeled reachability envelope remains inside the allowed boundary; it is conditional on the model and is not an unconditional safety proof. |

## Evaluation vocabulary

| Term | Definition |
|---|---|
| PASS | A declared requirement is supported by the specified check and evidence. |
| UNRESOLVED | The object or transition remains relevant and visible, but evidence is insufficient to establish preservation or failure. |
| FAIL | An observable condition contradicts a declared preservation or admission requirement. |
| NOT_EVALUATED | A required check has not been performed. It is not a pass and is distinct from an evaluated uncertainty. |
| Drift | An unaccounted-for change in meaning, classification, relationships, grain state, or use. |
| False promotion | Assigning stronger evidential or operational standing without the necessary justification. |
| Verification | Checking a specified claim or condition against declared tests or evidence. |
| Receipt | A record identifying the checked object and version, method, scope, result, evidence, and limitations. |
| Historical receipt | A record of a prior evaluation. Its result does not automatically apply to a different version, environment, or new contract. |
| Falsifier | An explicit observable condition that contradicts a stated claim or preservation requirement. |
| Interior boundary error | A transformation whose required grain passes at its endpoints but fails at an inspectable intermediate state or refinement. |

## Kind, type, and status: one example

| Field | Example value |
|---|---|
| Content | "Deploy the patch tonight." |
| Kind | Action-related |
| Type | Deployment request |
| Custody status | HELD, relevant to the patch-planning task |
| Activation status | Active for review |
| Approval status | Pending |
| Provenance | A specified customer email and version |
| Authority | Request only; no execution grant established |
| Relationship | Requires an authorized approval record |

If approval arrives, the request's type need not change. Its approval status changes with a linked approval record. Execution requires its own authorization checks and event record; the request's text is not evidence that execution occurred.

Earlier wording such as "proposed action" and "completed action" must be normalized to the underlying role plus lifecycle status when that is what the phrase means. Reclassification is possible, but it requires a recorded reason and version history rather than silent relabeling.

Related: [object contract](typed-directional-object.md), [five-grain routing](five-grain-routing.md), [custody interface](../interfaces/excellence-engine-v4.md), [completeness checks](directional-completeness.md).

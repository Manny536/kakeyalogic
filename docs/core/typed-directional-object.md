# Typed directional object contract

**Specification version:** 0.1

**State:** DOCUMENTED CONTRACT; machine-readable schema and runtime enforcement planned.

## Semantic object

The semantic tuple is:

$$
d=(x,k,\tau,s,p,a,\mathcal R).
$$

| Field | Meaning | Required distinction |
|---|---|---|
| $x$ | Content | What is said is separate from whether it is established. |
| $k$ | Kind | Broad family; not lifecycle status. |
| $\tau$ | Type | Specific operational role; not automatic authority. |
| $s$ | Structured status | Custody, activation, epistemic standing, approval, and lifecycle are independent dimensions. |
| $p$ | Provenance | Source and derivation history, including explicit unknowns. |
| $a$ | Authority | Externally grounded scope, conditions, and grant references; not merely a numerical rank. |
| $\mathcal R$ | Relationships | Typed edges with targets, versions, scopes, and supporting evidence. |

One direction may depend on several objects and edges. Its identifier must resolve the whole required route, not just one matching sentence. The tuple describes the state to preserve; it does not require every direction to be encoded as a single graph node.

## Identity and relevance envelope

An implementation must additionally record:

| Field | Requirement |
|---|---|
| `object_id` | Stable identity; duplicate text from different sources remains distinguishable. |
| `version` | Revision identifier linked to previous versions. |
| `direction_id` | Reference to the direction or directions this object supports. |
| `relevance_scope` | Declared task or research scope. |
| `relevance_basis` | Reason for relevance, with supporting context. |
| `relevance_assessed_at` | Time or event at which that relevance judgment was recorded. |
| `lineage` | Source, parent, derivation, correction, and supersession references. |
| `specification_version` | Contract version under which the record is interpreted. |

These are proposed schema fields, not a serialized schema supplied by this update. Unknown source or authority details must be recorded as unknown; neither a model nor a schema label may manufacture them.

## Independent state dimensions

| Dimension | Illustrative values | Meaning |
|---|---|---|
| Custody | HELD; archived | Relevant retained state versus historical storage outside the currently declared held scope. |
| Activation | Inactive; active | Whether selected for the present operation. |
| Epistemic standing | Unassessed; disputed; contradicted; verified for a named check | What evidence currently supports. |
| Approval | Not applicable; pending; granted; denied; revoked | Whether an applicable action authorization exists. |
| Lifecycle | Current; superseded | Whether this version controls the specified current use. |

The table is explanatory, not an exhaustive enumeration. A HELD object can be disputed, inactive, and unapproved at the same time. A superseded object may remain HELD for historical relevance.

Approval records must identify the grantor, applicable authority, target, action, scope, conditions, and expiry or revocation information when relevant. A request can be active for review without being executable.

## Relationship contract

Every required edge records its source object, relation type, target object, applicable versions, and scope. Direction matters: `corrects` is not interchangeable with `supports`, and `requires_approval_from` is not `approved_by`.

An unresolved target remains unresolved. A shared cluster must preserve member identities and edge roles rather than replacing them with an unsupported common assertion.

Compression and refinement must preserve required edges or declare their loss. A derived child may have a different type from its parent, but the derivation rule and supporting sources must justify it. A summary of an approval record is not a new grant of authority.

## Correction and transition contract

Preservation does not freeze state. A valid transition records:

1. The object identity and before/after versions.
2. The changed fields and before/after values.
3. The correction, new evidence, or authorization supporting the change.
4. The applicable transition rule and authority, where authority is required.
5. The event time, responsible actor or process, and affected relationships.
6. The prior state or a retained reference sufficient to inspect it.

Retyping requires explicit justification. Ordinary compression must not turn a hypothesis into an established result. New evidence may instead support a new result object linked to the hypothesis and its evaluation history.

If an object ceases to be relevant to a particular scope, record a relevance transition and retain the historical receipt. Do not keep calling it HELD in that scope while declaring it irrelevant. Do not silently shrink an evaluation's required-direction set to hide the transition.

## Minimum failure conditions

- Identity or source distinctions disappear under deduplication.
- A correction edge becomes support for the superseded claim.
- An object is marked HELD with no recorded relevant scope or basis.
- The word "approved" is treated as a grant without applicable authority.
- A status change lacks its supporting event or reason.
- An unknown provenance field becomes known without a source.
- A child receives authority solely because it shares a parent or cluster.

The [transformation contract](compression-overlap-refinement.md) supplies operation-level receipts. The [completeness contract](directional-completeness.md) determines whether each required direction survived.

# Compression, overlap, and refinement

**Specification version:** 0.1

**State:** DOCUMENTED TRANSFORMATION CONTRACTS; implementations and measured guarantees pending.

These contracts apply to the [typed directional object](typed-directional-object.md) and a predeclared [required-direction set](directional-completeness.md). A transformation can be honestly recorded while failing to preserve that set. Reporting loss is necessary; it does not make the loss a completeness pass.

## Compression

Compression reduces a declared representation cost while retaining the distinctions required for later reasoning or action.

**Input:** versioned objects and relationships, required directions, resource budget, permitted sources, and a declared cost measure.

**Output:** a smaller representation, mappings to retained objects or recovery sources, and a transformation receipt.

Required behavior:

- Declare whether the measured cost is prompt tokens, stored bytes, retrieval operations, or another specified resource.
- Compare input and output under the same cost definition.
- Preserve required identities, classifications, source references, corrections, and relationship roles.
- Identify any retained external store needed for recovery and include its access assumptions.
- Declare exclusions, approximations, and losses individually.
- Keep type, authority, and status unchanged unless a separately justified transition is recorded.

A shorter prompt backed by an unchanged document store is prompt-context compression, not necessarily a reduction in total storage. Deduplicating two sentences must not erase their independent sources.

**Failure example:** a summary combines an unverified claim and a correction into one confident statement, dropping the correction's scope and the original source references.

## Overlap

Overlap is shared representational occupancy by distinct directions. It is not automatically agreement, duplication, or failure.

**Input:** two or more directions sharing a cluster, summary, graph region, context segment, or other declared representation unit.

**Output:** shared structure with independently recoverable member identities, types, sources, authority scopes, statuses, and required relationships.

Required behavior:

- Define the representation unit and record which directions occupy it.
- Preserve a member-to-source mapping and distinguish repeated copies from independent evidence.
- Retain contradiction, correction, and approval relationships separately from support relationships.
- Never infer shared authority or truth from proximity or common membership.
- Report multiplicity and conflation separately; increased overlap alone does not establish damage.

**Failure example:** a customer statement and an internal approval record share a topic cluster, and the customer's statement silently inherits the approval record's authority.

## Refinement

Refinement resolves a representation into finer distinctions while preserving lineage to its supporting objects and sources.

**Input:** a coarse or overlapping representation, requested detail level, required directions, recovery sources, and access budget.

**Output:** finer objects and relationships, parent/member mappings, recovery evidence, and unresolved gaps.

Required behavior:

- Identify which coarse objects and source versions support each recovered distinction.
- Restore required member identity, type, status, and relation roles, not merely similar wording.
- Distinguish recovery from new inference or newly acquired information.
- Record retrieval from external sources, including unavailable or changed source versions.
- Justify newly derived child objects and their types rather than inheriting a parent's conclusions automatically.
- Report irrecoverable gaps; do not generate plausible missing content and label it recovered.

Refinement cannot reconstruct information actually discarded unless another retained source supplies it. It is not assumed to be an inverse of compression.

**Failure example:** a system reconstructs a source quotation that was never retained and has not been retrieved, then assigns it the original source's identity.

## Common transformation receipt

The future receipt schema must carry at least:

| Field group | Required record |
|---|---|
| Identity | Transformation identifier, operation, and contract version. |
| Inputs and outputs | Exact object identifiers and versions. |
| Evaluation scope | Required-direction-set identifier and version. |
| Resources | Declared cost metric, before/after costs, recovery budget, and permitted sources. |
| Membership and lineage | Parent/child, cluster/member, and source mappings. |
| Outcomes by direction | Preserved, lost, changed with justification, or not evaluated. |
| Transitions | Before/after state, rule, evidence, and applicable authorization. |
| Uncertainty | Unknown fields, failed retrievals, unresolved conflicts, and incomplete checks. |
| Verification | Checker or reviewer, method, evidence references, and limitations. |

The receipt describes observable records and recovery attempts. It does not claim access to hidden model attention or private reasoning traces.

## One round trip

Synthetic input: a patch request, a stated maintenance window, a correction to that window, and an approval requirement. All are HELD because they are relevant to planning; the request is active for review but not approved for execution.

1. Compress the objects into a planning summary while retaining identifiers and source references.
2. Let the old and corrected windows share a topic cluster while retaining the `supersedes` relationship.
3. Refine the summary into the current window, correction history, request, and unresolved approval requirement.
4. Check each required direction against its declared expected state.

The round trip fails if the old window becomes current again, the approval requirement disappears, or the request becomes executable without authorization. It can pass without recovering every original word if all declared content and relationship requirements are satisfied.

The sequence is illustrative. Real transformations may interleave, and overlap can exist before compression. See [directional completeness](directional-completeness.md) for the actual pass condition.

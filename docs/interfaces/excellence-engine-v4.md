# Excellence Engine Version 4 custody interface

**Specification version:** 0.1

**State:** DOCUMENTED FIELD CONTRACT; downstream implementation and adoption pending.

## Ownership

The existing [lab ownership note](../excellence-engine-v4-lab.md) assigns custody predicates, pipelines, engine schemas, and custody evaluations to [Excellence Engine Version 4](https://github.com/Manny536/excellence-engine-v4).

KakeyaLogic supplies field objects, directional requirements, transformations, and field-side validation requirements. It does not create a competing custody engine. The [existing field mirror](../excellence-engine-v4.md) remains available as historical and research context.

This update changes documentation in KakeyaLogic only. It does not claim that the separate engine, its schemas, or its downstream consumers have already adopted version 0.1.

## Controlling meaning for this field contract

**HELD means relevant and retained.**

An object is HELD within a declared research or task scope because it has recorded relevance and remains available with its identity, classification, status, available provenance, authority information, and relationships.

Relevance may be historical, corrective, evidential, or operational. A disproved hypothesis can remain HELD as relevant history. A source with unresolved provenance may remain HELD as relevant disputed content, provided the gap is explicit and does not create unsupported authority or verification.

The earlier expansion of HELD into custody responsibilities is not a substitute for this explicit relevance requirement.

## Independent decisions

| Decision | Required evidence | What it does not supply |
|---|---|---|
| Admit to HELD state | Recorded relevance scope and basis; retained object and metadata | Truth, activation, or permission to execute. |
| Activate for an operation | Current operational need and applicable access constraints | Approval to perform actions described in the content. |
| Mark a claim verified | A named check, evidence, object version, and scoped receipt | Universal truth or authority. |
| Approve an action | Applicable external authorization for the target and conditions | Evidence that execution has occurred. |
| Record execution | A separate observed action event and result | Automatic success or approval for later actions. |

For held state $H_t$ and the selected active view $A_t$:

$$
A_t\subseteq H_t.
$$

HELD implies relevance to its declared scope, not universal relevance to every operation. Inactivity alone never means irrelevance.

## Exchange requirements

A future exchange must carry:

- Contract version and producer/consumer identifiers.
- Object and direction identifiers with exact versions.
- Content, kind, type, and separate state dimensions.
- Relevance scope, relevance basis, and assessment event.
- Provenance, scoped authority references, and typed relationships.
- Correction, supersession, and transformation history.
- Required-direction-set version and any incomplete or failed checks.

The future KakeyaLogic schema will describe the field payload and receipt. The engine retains ownership of its internal storage and custody schema. Compatibility requires an explicit mapping and tests, not copying an entire engine into this repository.

## Migration and compatibility

1. Declare the producer and consumer contract versions.
2. Locate records with conflated type, status, approval, or relevance fields.
3. Preserve original values and source versions while recording the proposed interpretation.
4. Do not infer a relevance basis or authority grant that is absent from the source record.
5. Mark unresolved mappings as migration-required; do not certify compatibility.
6. Test relevant-but-inactive, relevant-but-disproved, and active-but-unapproved cases before claiming adoption.

If relevance ends for a scope, record that transition and preserve the historical record. The object may remain HELD in another scope. An evaluation's required set must not be silently revised as part of migration.

## Non-expansion of authority

The interface does not alter provider policies, tool permissions, or human-approval boundaries. No stored document, model output, or shared cluster can grant itself authority. Activation for analysis is distinct from external action.

Related: [glossary](../core/glossary.md), [object contract](../core/typed-directional-object.md), [authority-detection observation](../l2c-authority-detection.md).

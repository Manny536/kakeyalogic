"""Strict grain completeness and the legacy diagnostic score.

No aggregate score may override a failing required grain.
"""

from __future__ import annotations

from dataclasses import dataclass

from kakeyalogic.grains import Grain, GrainBundle, Outcome, SAVER, required_pairs
from kakeyalogic.state import FieldState, TypedObject


@dataclass(frozen=True)
class CompletenessReport:
    status: str
    kcomplete: bool
    missing: tuple[dict, ...]
    diagnostic_score: float | None
    note: str

    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "kcomplete": self.kcomplete,
            "missing": list(self.missing),
            "diagnostic_score": self.diagnostic_score,
            "note": self.note,
        }


def kcomplete(
    bundle: GrainBundle,
    direction_ids: tuple[str, ...],
    grains: tuple[Grain, ...] = SAVER,
    *,
    weights: dict[str, float] | None = None,
) -> CompletenessReport:
    if not direction_ids:
        return CompletenessReport(
            status="NOT_APPLICABLE",
            kcomplete=False,
            missing=(),
            diagnostic_score=None,
            note="empty required-direction set is NOT APPLICABLE, not a perfect result",
        )
    pairs = required_pairs(direction_ids, grains)
    missing: list[dict] = []
    passed_dirs = 0
    for direction_id in direction_ids:
        dir_ok = True
        for grain in grains:
            cell = bundle.cell(direction_id, grain)
            outcome = cell.outcome if cell else Outcome.NOT_EVALUATED
            if outcome is not Outcome.PASS:
                dir_ok = False
                missing.append(
                    {
                        "direction_id": direction_id,
                        "grain": grain.value,
                        "outcome": outcome.value,
                    }
                )
        if dir_ok:
            passed_dirs += 1
    score = None
    if weights is None:
        score = passed_dirs / len(direction_ids)
    else:
        num = sum(weights.get(d, 1.0) for d in direction_ids if not any(
            m["direction_id"] == d for m in missing
        ))
        den = sum(weights.get(d, 1.0) for d in direction_ids)
        score = num / den if den else None
    complete = not missing
    return CompletenessReport(
        status="PASS" if complete else "FAIL",
        kcomplete=complete,
        missing=tuple(missing),
        diagnostic_score=score,
        note=(
            "diagnostic_score is a legacy per-direction summary; it does not "
            "override a failing required grain"
        ),
    )


def retention_bundle_from_objects(
    state: FieldState,
    *,
    prior_objects: dict[str, TypedObject] | None = None,
) -> GrainBundle:
    """Re-evaluate Retention after a later update.

    A required held correction, red line, or evidence object that is no longer
    recoverable fails Retention. Prior failed/unresolved edges are not scored
    here; they are retained separately in the ledger.
    """
    from kakeyalogic.grains import GrainCell

    cells = []
    prior = prior_objects or {}
    for direction in state.directions.values():
        required_objs = [
            obj
            for obj in prior.values()
            if obj.direction_id == direction.direction_id and obj.held
        ]
        lost = [
            obj
            for obj in required_objs
            if obj.object_id not in state.objects
            or not state.objects[obj.object_id].recoverable
        ]
        if lost and any(obj.role in {"correction", "red_line", "evidence"} or obj.type in {"correction", "red_line"} for obj in lost):
            outcome = Outcome.FAIL
            reason = (
                "required correction/red-line/evidence is no longer recoverable: "
                + ", ".join(o.object_id for o in lost)
            )
        elif lost:
            outcome = Outcome.FAIL
            reason = "required held object is no longer recoverable: " + ", ".join(
                o.object_id for o in lost
            )
        elif not any(
            obj.direction_id == direction.direction_id and obj.held and obj.recoverable
            for obj in state.objects.values()
        ):
            outcome = Outcome.UNRESOLVED
            reason = "no recoverable held object remains for this direction"
        else:
            outcome = Outcome.PASS
            reason = "required held objects remain recoverable"
        cells.append(
            GrainCell(
                direction_id=direction.direction_id,
                grain=Grain.R,
                outcome=outcome,
                check="longitudinal_retention",
                reason=reason,
                evidence_refs=tuple(
                    o.object_id
                    for o in state.objects.values()
                    if o.direction_id == direction.direction_id
                ),
            )
        )
    from kakeyalogic.grains import GrainBundle as Bundle

    return Bundle(cells=tuple(cells))

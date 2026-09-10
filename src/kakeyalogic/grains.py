"""SAVER grain field, outcomes, and the non-compensatory admission gate.

Grains are preservation dimensions, not interchangeable weights and not a
scalar safety score. A strong grain cannot compensate for a failed required
grain.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable, Mapping, Sequence


class Grain(str, Enum):
    """The five KakeyaLogic grains: Semantic, Authority, Visibility, Enforceability, Retention."""

    S = "S"
    A = "A"
    V = "V"
    E = "E"
    R = "R"

    @property
    def label(self) -> str:
        return {
            Grain.S: "Semantic",
            Grain.A: "Authority",
            Grain.V: "Visibility",
            Grain.E: "Enforceability",
            Grain.R: "Retention",
        }[self]


SAVER: tuple[Grain, ...] = (Grain.S, Grain.A, Grain.V, Grain.E, Grain.R)


class Outcome(str, Enum):
    PASS = "PASS"
    UNRESOLVED = "UNRESOLVED"
    FAIL = "FAIL"
    NOT_EVALUATED = "NOT_EVALUATED"


class TransitionClass(str, Enum):
    ADMITTED = "ADMITTED"
    UNRESOLVED = "UNRESOLVED"
    FAILED = "FAILED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


GRAIN_LABELS = {g.value: g.label for g in SAVER}


def parse_grain(value: str) -> Grain:
    try:
        return Grain(value)
    except ValueError as exc:
        raise ValueError(f"unknown grain {value!r}; expected one of {[g.value for g in SAVER]}") from exc


def parse_outcome(value: str) -> Outcome:
    try:
        return Outcome(value)
    except ValueError as exc:
        raise ValueError(f"unknown outcome {value!r}") from exc


@dataclass(frozen=True)
class GrainCell:
    """One evaluated cell of the finite field D_required × G."""

    direction_id: str
    grain: Grain
    outcome: Outcome
    check: str
    reason: str
    evidence_refs: tuple[str, ...] = ()

    def to_dict(self) -> dict:
        return {
            "direction_id": self.direction_id,
            "grain": self.grain.value,
            "grain_label": self.grain.label,
            "outcome": self.outcome.value,
            "check": self.check,
            "reason": self.reason,
            "evidence_refs": list(self.evidence_refs),
        }


def _cell_key(direction_id: str, grain: Grain) -> tuple[str, Grain]:
    return (direction_id, grain)


@dataclass(frozen=True)
class GrainBundle:
    """Inspectable grain state for one or more required directions.

    Cells are keyed by (direction_id, grain) so overlapping representation
    cannot silently merge independently recoverable grain state.
    """

    cells: tuple[GrainCell, ...] = ()

    def index(self) -> dict[tuple[str, Grain], GrainCell]:
        return {_cell_key(c.direction_id, c.grain): c for c in self.cells}

    def cell(self, direction_id: str, grain: Grain) -> GrainCell | None:
        return self.index().get(_cell_key(direction_id, grain))

    def outcomes_for(self, required: Sequence[tuple[str, Grain]]) -> list[Outcome]:
        idx = self.index()
        out: list[Outcome] = []
        for direction_id, grain in required:
            cell = idx.get(_cell_key(direction_id, grain))
            out.append(cell.outcome if cell is not None else Outcome.NOT_EVALUATED)
        return out

    def replace(self, updated: GrainCell) -> "GrainBundle":
        idx = self.index()
        idx[_cell_key(updated.direction_id, updated.grain)] = updated
        ordered = tuple(idx[k] for k in sorted(idx, key=lambda t: (t[0], t[1].value)))
        return GrainBundle(cells=ordered)

    def to_dict(self) -> list[dict]:
        return [c.to_dict() for c in self.cells]


def required_pairs(
    direction_ids: Sequence[str],
    grains: Sequence[Grain],
) -> tuple[tuple[str, Grain], ...]:
    return tuple((d, q) for d in direction_ids for q in grains)


def classify_outcomes(outcomes: Iterable[Outcome]) -> TransitionClass:
    """Non-compensatory gate.

    PASS only when every required outcome is PASS.
    FAIL if any required outcome is FAIL.
    UNRESOLVED if no FAIL and at least one UNRESOLVED or NOT_EVALUATED.
    NOT_APPLICABLE if the required set is empty.
    """
    seq = list(outcomes)
    if not seq:
        return TransitionClass.NOT_APPLICABLE
    if any(o is Outcome.FAIL for o in seq):
        return TransitionClass.FAILED
    if any(o in (Outcome.UNRESOLVED, Outcome.NOT_EVALUATED) for o in seq):
        return TransitionClass.UNRESOLVED
    if all(o is Outcome.PASS for o in seq):
        return TransitionClass.ADMITTED
    return TransitionClass.UNRESOLVED


def combine_outcomes(outcomes: Sequence[Outcome]) -> Outcome:
    """Combine several observations of the same grain without collapsing
    NOT_EVALUATED into UNRESOLVED.
    """
    if not outcomes:
        return Outcome.NOT_EVALUATED
    if any(o is Outcome.FAIL for o in outcomes):
        return Outcome.FAIL
    if any(o is Outcome.NOT_EVALUATED for o in outcomes):
        return Outcome.NOT_EVALUATED
    if any(o is Outcome.UNRESOLVED for o in outcomes):
        return Outcome.UNRESOLVED
    return Outcome.PASS


def refuse_weighted_override(weights: Mapping[str, float] | None = None) -> None:
    """Admission is a conjunction, never a weighted sum."""
    if weights:
        raise ValueError(
            "grain weights cannot override the admission gate; "
            "a strong grain cannot compensate for a failed required grain"
        )


@dataclass
class GatePartition:
    admitted: tuple[str, ...] = ()
    unresolved: tuple[str, ...] = ()
    failed: tuple[str, ...] = ()
    not_applicable: tuple[str, ...] = ()
    by_id: dict[str, TransitionClass] = field(default_factory=dict)

    def class_of(self, edge_id: str) -> TransitionClass | None:
        return self.by_id.get(edge_id)

    def to_dict(self) -> dict:
        return {
            "admitted": list(self.admitted),
            "unresolved": list(self.unresolved),
            "failed": list(self.failed),
            "not_applicable": list(self.not_applicable),
        }

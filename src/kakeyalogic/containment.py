"""Planning is not containment.

A selected admitted route does not establish that every executable alternative
is contained. Reachability uses a separate model R- ⊆ R ⊆ R+.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ContainmentVerdict(str, Enum):
    FAIL = "FAIL"
    PASS_MODEL = "PASS_MODEL"
    OPEN = "OPEN"


@dataclass(frozen=True)
class ContainmentReport:
    verdict: ContainmentVerdict
    allowed_boundary: tuple[str, ...]
    confirmed_reachable: tuple[str, ...]
    modeled_envelope: tuple[str, ...]
    violators: tuple[str, ...]
    coverage_gaps: tuple[str, ...]
    note: str

    def to_dict(self) -> dict:
        return {
            "verdict": self.verdict.value,
            "allowed_boundary": list(self.allowed_boundary),
            "confirmed_reachable": list(self.confirmed_reachable),
            "modeled_envelope": list(self.modeled_envelope),
            "violators": list(self.violators),
            "coverage_gaps": list(self.coverage_gaps),
            "note": self.note,
        }


def evaluate_containment(
    *,
    allowed_boundary: tuple[str, ...],
    confirmed_reachable: tuple[str, ...],
    modeled_envelope: tuple[str, ...],
    coverage_declared: bool = True,
) -> ContainmentReport:
    allowed = set(allowed_boundary)
    confirmed = set(confirmed_reachable)
    envelope = set(modeled_envelope)

    if not confirmed.issubset(envelope) and coverage_declared:
        # Model is internally inconsistent; treat as OPEN rather than silently repairing.
        gaps = tuple(sorted(confirmed - envelope))
        return ContainmentReport(
            verdict=ContainmentVerdict.OPEN,
            allowed_boundary=tuple(allowed_boundary),
            confirmed_reachable=tuple(confirmed_reachable),
            modeled_envelope=tuple(modeled_envelope),
            violators=(),
            coverage_gaps=gaps,
            note="confirmed-reachable set is not inside the modeled envelope; coverage OPEN",
        )

    violators = tuple(sorted(node for node in confirmed if node not in allowed))
    if violators:
        return ContainmentReport(
            verdict=ContainmentVerdict.FAIL,
            allowed_boundary=tuple(allowed_boundary),
            confirmed_reachable=tuple(confirmed_reachable),
            modeled_envelope=tuple(modeled_envelope),
            violators=violators,
            coverage_gaps=(),
            note=(
                "confirmed reachable state violates the allowed boundary; "
                "an admitted planner path does not establish containment"
            ),
        )

    if not coverage_declared:
        return ContainmentReport(
            verdict=ContainmentVerdict.OPEN,
            allowed_boundary=tuple(allowed_boundary),
            confirmed_reachable=tuple(confirmed_reachable),
            modeled_envelope=tuple(modeled_envelope),
            violators=(),
            coverage_gaps=(),
            note="coverage is insufficient to establish PASS_MODEL or FAIL",
        )

    envelope_violators = tuple(sorted(node for node in envelope if node not in allowed))
    if envelope_violators:
        return ContainmentReport(
            verdict=ContainmentVerdict.OPEN,
            allowed_boundary=tuple(allowed_boundary),
            confirmed_reachable=tuple(confirmed_reachable),
            modeled_envelope=tuple(modeled_envelope),
            violators=(),
            coverage_gaps=envelope_violators,
            note=(
                "conservative envelope is not inside the allowed boundary and no "
                "confirmed violator was recorded; containment remains OPEN"
            ),
        )

    return ContainmentReport(
        verdict=ContainmentVerdict.PASS_MODEL,
        allowed_boundary=tuple(allowed_boundary),
        confirmed_reachable=tuple(confirmed_reachable),
        modeled_envelope=tuple(modeled_envelope),
        violators=(),
        coverage_gaps=(),
        note="PASS_MODEL is conditional on the reachability model, not an unconditional safety proof",
    )

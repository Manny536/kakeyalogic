"""Interior preservation: endpoint agreement is not enough."""

from __future__ import annotations

from dataclasses import dataclass

from kakeyalogic.grains import Grain, GrainBundle, GrainCell, Outcome, combine_outcomes
from kakeyalogic.state import CandidateEdge


@dataclass(frozen=True)
class InteriorReport:
    edge_id: str
    bundle: GrainBundle
    boundary_error: bool
    unobserved_claimed_interior: bool
    notes: tuple[str, ...] = ()

    def to_dict(self) -> dict:
        return {
            "edge_id": self.edge_id,
            "bundle": self.bundle.to_dict(),
            "boundary_error": self.boundary_error,
            "unobserved_claimed_interior": self.unobserved_claimed_interior,
            "notes": list(self.notes),
        }


def evaluate_interior(edge: CandidateEdge) -> InteriorReport:
    """Apply the spec interior test to declared edge grain evidence.

    Boundary-error falsifier:
        P_q(src)=PASS, P_q(dst)=PASS, exists u in (0,1) with P_q(rho(u))=FAIL.

    If a transformation claims interior preservation but the interior cannot
    be observed at the claimed scale, Visibility remains UNRESOLVED.
    """
    notes: list[str] = []
    bundle = edge.declared
    boundary_error = False
    unobserved = False

    interior_open = tuple(s for s in edge.interior if 0.0 < s.u < 1.0)
    endpoints = tuple(s for s in edge.interior if s.u == 0.0 or s.u == 1.0)

    if edge.claimed_interior_scale and not interior_open:
        unobserved = True
        notes.append(
            "claimed interior scale has no inspectable sample in (0, 1); "
            "Visibility remains UNRESOLVED"
        )
        for direction_id in edge.direction_ids:
            existing = bundle.cell(direction_id, Grain.V)
            bundle = bundle.replace(
                GrainCell(
                    direction_id=direction_id,
                    grain=Grain.V,
                    outcome=Outcome.UNRESOLVED,
                    check="interior_visibility",
                    reason=(
                        existing.reason + " | " if existing else ""
                    )
                    + "interior unobserved at claimed scale",
                    evidence_refs=existing.evidence_refs if existing else (),
                )
            )

    if interior_open:
        for direction_id, grain in edge.required_pairs():
            declared_cell = bundle.cell(direction_id, grain)
            declared_outcome = declared_cell.outcome if declared_cell else Outcome.NOT_EVALUATED
            interior_outcomes = [
                sample.outcomes_for(direction_id).get(grain, Outcome.NOT_EVALUATED)
                for sample in interior_open
            ]
            endpoint_outcomes = [
                sample.outcomes_for(direction_id).get(grain, declared_outcome)
                for sample in endpoints
            ] or [declared_outcome]
            if (
                all(o is Outcome.PASS for o in endpoint_outcomes)
                and any(o is Outcome.FAIL for o in interior_outcomes)
            ):
                boundary_error = True
                bundle = bundle.replace(
                    GrainCell(
                        direction_id=direction_id,
                        grain=grain,
                        outcome=Outcome.FAIL,
                        check="interior_boundary_error",
                        reason=(
                            f"endpoints PASS for {grain.label} but interior sample "
                            f"FAILS along {edge.edge_id}"
                        ),
                        evidence_refs=declared_cell.evidence_refs if declared_cell else (),
                    )
                )
                notes.append(
                    f"boundary-error falsifier on {direction_id}/{grain.value}"
                )
                continue
            combined = combine_outcomes([declared_outcome, *interior_outcomes])
            if declared_cell is None or combined is not declared_outcome:
                bundle = bundle.replace(
                    GrainCell(
                        direction_id=direction_id,
                        grain=grain,
                        outcome=combined,
                        check="interior_combined",
                        reason=(
                            declared_cell.reason
                            if declared_cell
                            else "combined declared and interior outcomes"
                        ),
                        evidence_refs=declared_cell.evidence_refs if declared_cell else (),
                    )
                )

    return InteriorReport(
        edge_id=edge.edge_id,
        bundle=bundle,
        boundary_error=boundary_error,
        unobserved_claimed_interior=unobserved,
        notes=tuple(notes),
    )

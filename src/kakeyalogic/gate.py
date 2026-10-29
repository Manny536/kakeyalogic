"""Partition candidate transitions into admitted, unresolved, and failed sets."""

from __future__ import annotations

from dataclasses import dataclass

from kakeyalogic.grains import (
    GatePartition,
    GrainBundle,
    TransitionClass,
    classify_outcomes,
    refuse_weighted_override,
)
from kakeyalogic.interior import InteriorReport, evaluate_interior
from kakeyalogic.state import CandidateEdge


@dataclass(frozen=True)
class EvaluatedEdge:
    edge: CandidateEdge
    bundle: GrainBundle
    classification: TransitionClass
    interior: InteriorReport
    admission_issues: tuple[str, ...] = ()

    @property
    def edge_id(self) -> str:
        return self.edge.edge_id

    def to_dict(self) -> dict:
        return {
            "edge_id": self.edge.edge_id,
            "src": self.edge.src,
            "dst": self.edge.dst,
            "cost": self.edge.cost,
            "classification": self.classification.value,
            "bundle": self.bundle.to_dict(),
            "interior": self.interior.to_dict(),
            "boundary_error": self.interior.boundary_error,
            "admission_issues": list(self.admission_issues),
        }


def evaluate_edge(edge: CandidateEdge) -> EvaluatedEdge:
    interior = evaluate_interior(edge)
    classification = classify_outcomes(interior.bundle.outcomes_for(edge.required_pairs()))
    return EvaluatedEdge(
        edge=edge,
        bundle=interior.bundle,
        classification=classification,
        interior=interior,
    )


def grain_and_gate(
    edges: dict[str, CandidateEdge],
    *,
    weights: dict[str, float] | None = None,
) -> tuple[dict[str, EvaluatedEdge], GatePartition]:
    refuse_weighted_override(weights)
    evaluated = {edge_id: evaluate_edge(edge) for edge_id, edge in edges.items()}
    return evaluated, partition_evaluated(evaluated)


def partition_evaluated(evaluated: dict[str, EvaluatedEdge]) -> GatePartition:
    """Build the routing sets from the final, including overlap, evaluation."""
    admitted: list[str] = []
    unresolved: list[str] = []
    failed: list[str] = []
    not_applicable: list[str] = []
    by_id: dict[str, TransitionClass] = {}
    for edge_id, item in sorted(evaluated.items()):
        by_id[edge_id] = item.classification
        if item.classification is TransitionClass.ADMITTED:
            admitted.append(edge_id)
        elif item.classification is TransitionClass.UNRESOLVED:
            unresolved.append(edge_id)
        elif item.classification is TransitionClass.FAILED:
            failed.append(edge_id)
        else:
            not_applicable.append(edge_id)
    partition = GatePartition(
        admitted=tuple(admitted),
        unresolved=tuple(unresolved),
        failed=tuple(failed),
        not_applicable=tuple(not_applicable),
        by_id=by_id,
    )
    return partition

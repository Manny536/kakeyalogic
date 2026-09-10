"""Overlap: shared representation without merging direction identity or grain state."""

from __future__ import annotations

from dataclasses import dataclass, replace

from kakeyalogic.gate import EvaluatedEdge
from kakeyalogic.grains import SAVER, TransitionClass
from kakeyalogic.state import FieldState


@dataclass(frozen=True)
class OverlapIssue:
    cluster_id: str
    code: str
    detail: str
    edge_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class OverlapReport:
    ok: bool
    issues: tuple[OverlapIssue, ...] = ()

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "issues": [
                {"cluster_id": i.cluster_id, "code": i.code, "detail": i.detail,
                 "edge_ids": list(i.edge_ids)}
                for i in self.issues
            ],
        }


def check_overlap(state: FieldState, evaluated: dict[str, EvaluatedEdge]) -> OverlapReport:
    """Shared clusters must keep independently recoverable grain bundles.

    Authority is never created by wording, proximity, or type labels.
    """
    issues: list[OverlapIssue] = []
    for cluster in state.clusters.values():
        cluster_edges = tuple(sorted(
            edge_id for edge_id, item in evaluated.items()
            if item.edge.cluster_id == cluster.cluster_id
        ))
        if len(set(cluster.member_direction_ids)) != len(cluster.member_direction_ids):
            issues.append(
                OverlapIssue(
                    cluster.cluster_id,
                    "merged_direction_identity",
                    "cluster member list collapsed distinct direction identities",
                    cluster_edges,
                )
            )
        for direction_id in cluster.member_direction_ids:
            direction = state.directions.get(direction_id)
            grains = direction.required_grains if direction else SAVER
            missing = [q.value for q in grains if not any(
                direction_id in item.edge.direction_ids
                and item.bundle.cell(direction_id, q) is not None
                for item in evaluated.values()
            )]
            if missing:
                issues.append(
                    OverlapIssue(
                        cluster.cluster_id,
                        "missing_independent_grain_state",
                        f"direction {direction_id} lacks independently inspectable grains: {', '.join(missing)}",
                        cluster_edges,
                    )
                )
    for item in evaluated.values():
        if item.edge.authority_inherited_from_cluster:
            issues.append(
                OverlapIssue(
                    item.edge.cluster_id,
                    "authority_from_proximity",
                    f"{item.edge.edge_id} inherited authority from cluster membership; "
                    "authority is never created by proximity",
                    (item.edge_id,),
                )
            )
    return OverlapReport(ok=not issues, issues=tuple(issues))


def enforce_overlap(
    evaluated: dict[str, EvaluatedEdge], report: OverlapReport
) -> dict[str, EvaluatedEdge]:
    """Retain declared grain evidence, but reject structurally invalid edges.

    The receipt names the independent admission failures rather than changing
    a declared grain observation into an invented measurement.
    """
    result = dict(evaluated)
    for issue in report.issues:
        for edge_id in issue.edge_ids:
            item = result[edge_id]
            result[edge_id] = replace(
                item,
                classification=TransitionClass.FAILED,
                admission_issues=item.admission_issues + (issue.code + ": " + issue.detail,),
            )
    return result

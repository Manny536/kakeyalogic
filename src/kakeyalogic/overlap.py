"""Overlap: shared representation without merging direction identity or grain state."""

from __future__ import annotations

from dataclasses import dataclass

from kakeyalogic.gate import EvaluatedEdge
from kakeyalogic.grains import Grain
from kakeyalogic.state import FieldState


@dataclass(frozen=True)
class OverlapIssue:
    cluster_id: str
    code: str
    detail: str


@dataclass(frozen=True)
class OverlapReport:
    ok: bool
    issues: tuple[OverlapIssue, ...] = ()

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "issues": [
                {"cluster_id": i.cluster_id, "code": i.code, "detail": i.detail}
                for i in self.issues
            ],
        }


def check_overlap(state: FieldState, evaluated: dict[str, EvaluatedEdge]) -> OverlapReport:
    """Shared clusters must keep independently recoverable grain bundles.

    Authority is never created by wording, proximity, or type labels.
    """
    issues: list[OverlapIssue] = []
    for cluster in state.clusters.values():
        if len(set(cluster.member_direction_ids)) != len(cluster.member_direction_ids):
            issues.append(
                OverlapIssue(
                    cluster.cluster_id,
                    "merged_direction_identity",
                    "cluster member list collapsed distinct direction identities",
                )
            )
        for direction_id in cluster.member_direction_ids:
            found = False
            for item in evaluated.values():
                if direction_id in item.edge.direction_ids and item.bundle.cell(
                    direction_id, Grain.A
                ):
                    found = True
                    break
            if not found:
                # Direction grain state may also live on held objects; require at least
                # one inspectable Authority cell somewhere on an incident edge.
                issues.append(
                    OverlapIssue(
                        cluster.cluster_id,
                        "missing_independent_grain_state",
                        f"direction {direction_id} has no independently inspectable Authority cell",
                    )
                )
        for item in evaluated.values():
            if item.edge.cluster_id != cluster.cluster_id:
                continue
            if item.edge.authority_inherited_from_cluster:
                issues.append(
                    OverlapIssue(
                        cluster.cluster_id,
                        "authority_from_proximity",
                        (
                            f"{item.edge.edge_id} inherited authority from cluster membership; "
                            "authority is never created by proximity"
                        ),
                    )
                )
    return OverlapReport(ok=not issues, issues=tuple(issues))

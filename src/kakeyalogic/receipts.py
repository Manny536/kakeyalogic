"""Transformation and routing receipts.

A receipt records observable evaluation, not hidden model traces. Unresolved
alternatives remain listed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from kakeyalogic.completeness import CompletenessReport
from kakeyalogic.containment import ContainmentReport
from kakeyalogic.gate import EvaluatedEdge, GatePartition
from kakeyalogic.geodecis import DistanceReport
from kakeyalogic.overlap import OverlapReport
from kakeyalogic.refine import RefineReport


def _utcnow() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


@dataclass
class RetentionLedger:
    """Longitudinal store for receipts, failed edges, and unresolved gaps."""

    receipts: list[dict] = field(default_factory=list)
    failed_edge_ids: list[str] = field(default_factory=list)
    unresolved_edge_ids: list[str] = field(default_factory=list)
    dropped_objects: list[dict] = field(default_factory=list)

    def record_partition(self, partition: GatePartition) -> None:
        for edge_id in partition.failed:
            if edge_id not in self.failed_edge_ids:
                self.failed_edge_ids.append(edge_id)
        for edge_id in partition.unresolved:
            if edge_id not in self.unresolved_edge_ids:
                self.unresolved_edge_ids.append(edge_id)

    def record_drop(self, object_id: str, reason: str, epoch: int) -> None:
        self.dropped_objects.append(
            {"object_id": object_id, "reason": reason, "epoch": epoch}
        )

    def to_dict(self) -> dict:
        return {
            "receipts": list(self.receipts),
            "failed_edge_ids": list(self.failed_edge_ids),
            "unresolved_edge_ids": list(self.unresolved_edge_ids),
            "dropped_objects": list(self.dropped_objects),
        }


@dataclass
class RoutingReceipt:
    specification_version: str
    fixture_id: str
    source: str
    goal: str
    partition: GatePartition
    evaluated: dict[str, EvaluatedEdge]
    overlap: OverlapReport
    refine: RefineReport | None
    geodecis: DistanceReport
    containment: ContainmentReport
    completeness: CompletenessReport
    retention: dict[str, Any]
    selected_edge_ids: tuple[str, ...]
    selected_nodes: tuple[str, ...]
    unresolved_alternatives: tuple[str, ...]
    failed_evidence: tuple[str, ...]
    limitations: tuple[str, ...]
    recorded_at: str = field(default_factory=_utcnow)

    def to_dict(self) -> dict:
        return {
            "specification_version": self.specification_version,
            "fixture_id": self.fixture_id,
            "recorded_at": self.recorded_at,
            "source": self.source,
            "goal": self.goal,
            "loop": [
                "Observe",
                "Grain",
                "Gate",
                "Overlap",
                "Refine",
                "Route",
                "Receipt",
                "Retain",
            ],
            "partition": self.partition.to_dict(),
            "evaluated": {k: v.to_dict() for k, v in self.evaluated.items()},
            "overlap": self.overlap.to_dict(),
            "refine": None if self.refine is None else self.refine.to_dict(),
            "geodecis": self.geodecis.to_dict(),
            "containment": self.containment.to_dict(),
            "completeness": self.completeness.to_dict(),
            "retention": self.retention,
            "selected_edge_ids": list(self.selected_edge_ids),
            "selected_nodes": list(self.selected_nodes),
            "unresolved_alternatives": list(self.unresolved_alternatives),
            "failed_evidence": list(self.failed_evidence),
            "limitations": list(self.limitations),
        }

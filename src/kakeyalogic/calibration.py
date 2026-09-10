"""Load the synthetic SAVER calibration fixture.

Calibration here means: declare operational costs, required directions,
required grains, grain evidence, interior samples, and expected behavioral
outcomes on a frozen synthetic graph. It is not a fitted safety score.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from kakeyalogic.grains import Grain, SAVER, parse_grain
from kakeyalogic.state import (
    CandidateEdge,
    Direction,
    FieldState,
    OverlapCluster,
    TypedObject,
    bundle_from_declared,
    parse_interior,
)


DEFAULT_FIXTURE = (
    Path(__file__).resolve().parent / "data" / "saver_calibration_graph.json"
)


@dataclass(frozen=True)
class CalibrationFixture:
    path: Path
    raw: dict[str, Any]
    state: FieldState
    expected: dict[str, Any]
    cost_model: dict[str, Any]
    sha256: str

    @property
    def fixture_id(self) -> str:
        return str(self.raw["fixture_id"])

    @property
    def specification_version(self) -> str:
        return str(self.raw.get("specification_version", "1.0"))


def fixture_hash(raw: dict[str, Any] | str | bytes) -> str:
    if isinstance(raw, (bytes, bytearray)):
        payload = bytes(raw)
    elif isinstance(raw, str):
        payload = raw.encode("utf-8")
    else:
        payload = json.dumps(raw, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _grains(raw: list[str] | None, default: tuple[Grain, ...] = SAVER) -> tuple[Grain, ...]:
    if raw is None:
        return default
    return tuple(parse_grain(g) for g in raw)


def load_fixture(path: str | Path | None = None) -> CalibrationFixture:
    fixture_path = Path(path) if path else DEFAULT_FIXTURE
    text = fixture_path.read_text(encoding="utf-8")
    raw = json.loads(text)
    sha = fixture_hash(text.encode("utf-8"))

    direction_ids = tuple(d["direction_id"] for d in raw["directions"])
    default_grains = _grains(raw.get("required_grains"))

    directions = {
        item["direction_id"]: Direction(
            direction_id=item["direction_id"],
            required_grains=_grains(item.get("required_grains"), default_grains),
            description=item.get("description", ""),
        )
        for item in raw["directions"]
    }
    objects = {
        item["object_id"]: TypedObject(
            object_id=item["object_id"],
            direction_id=item["direction_id"],
            type=item["type"],
            content=item.get("content", ""),
            held=item.get("held", True),
            recoverable=item.get("recoverable", True),
            role=item.get("role", item.get("type", "")),
            version=str(item.get("version", "1")),
            provenance=item.get("provenance", ""),
            authority=item.get("authority", ""),
            cluster_id=item.get("cluster_id", ""),
            notes=item.get("notes", ""),
        )
        for item in raw.get("objects", [])
    }
    clusters = {
        item["cluster_id"]: OverlapCluster(
            cluster_id=item["cluster_id"],
            member_direction_ids=tuple(item["member_direction_ids"]),
            representation_unit=item.get("representation_unit", ""),
            notes=item.get("notes", ""),
        )
        for item in raw.get("clusters", [])
    }

    edges: dict[str, CandidateEdge] = {}
    for item in raw["edges"]:
        grains = _grains(item.get("required_grains"), default_grains)
        dirs = tuple(item.get("direction_ids") or direction_ids)
        declared = bundle_from_declared(
            dirs,
            grains,
            item.get("grains", {}),
            check=item.get("check", "declared_fixture"),
            reason=item.get("reason", "calibration fixture declaration"),
            evidence_refs=item.get("evidence_refs", []),
            per_direction=item.get("per_direction"),
        )
        edges[item["edge_id"]] = CandidateEdge(
            edge_id=item["edge_id"],
            src=item["src"],
            dst=item["dst"],
            cost=float(item["cost"]),
            direction_ids=dirs,
            required_grains=grains,
            declared=declared,
            interior=parse_interior(item.get("interior", []), grains),
            claimed_interior_scale=bool(item.get("claimed_interior_scale", False)),
            cluster_id=item.get("cluster_id", ""),
            notes=item.get("notes", ""),
            authority_inherited_from_cluster=bool(
                item.get("authority_inherited_from_cluster", False)
            ),
        )

    reach = raw.get("reachability", {})
    state = FieldState(
        state_id=raw.get("fixture_id", fixture_path.stem),
        nodes=tuple(raw["nodes"]),
        directions=directions,
        objects=objects,
        edges=edges,
        clusters=clusters,
        allowed_boundary=tuple(raw.get("allowed_boundary", raw["nodes"])),
        confirmed_reachable=tuple(reach.get("confirmed_minus", ())),
        modeled_envelope=tuple(reach.get("modeled_plus", ())),
        current=raw.get("source", raw["nodes"][0]),
        goal=raw.get("goal", raw["nodes"][-1]),
        notes=raw.get("notes", ""),
    )
    return CalibrationFixture(
        path=fixture_path,
        raw=raw,
        state=state,
        expected=raw.get("expected", {}),
        cost_model=raw.get("cost_model", {}),
        sha256=sha,
    )


def calibration_receipt(fixture: CalibrationFixture, routing: dict) -> dict:
    return {
        "kind": "SAVER_CALIBRATION_RECEIPT",
        "specification_version": fixture.specification_version,
        "fixture_id": fixture.fixture_id,
        "fixture_sha256": fixture.sha256,
        "cost_model": fixture.cost_model,
        "required_directions": list(fixture.state.required_direction_ids()),
        "required_grains": [g.value for g in _grains(fixture.raw.get("required_grains"))],
        "expected": fixture.expected,
        "routing": {
            "selected_nodes": routing.get("selected_nodes"),
            "selected_edge_ids": routing.get("selected_edge_ids"),
            "admitted_cost": routing.get("geodecis", {}).get("admitted", {}).get("cost"),
            "diamond_cost": routing.get("geodecis", {}).get("diamond", {}).get("cost"),
            "evidence_sensitivity": routing.get("geodecis", {}).get("evidence_sensitivity"),
            "partition": routing.get("partition"),
            "containment": routing.get("containment", {}).get("verdict"),
        },
        "honesty": [
            "Calibration binds declared operational costs and grain evidence on a synthetic graph.",
            "This is not a fitted safety, ethics, truth, or L²_C score.",
            "Passing synthetic tests is a reference-router behavioral receipt.",
            "Operational SIUT validity remains OPEN.",
        ],
    }

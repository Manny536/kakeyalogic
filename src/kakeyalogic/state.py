"""Typed field state: objects, directions, candidate transformations, interior samples."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Mapping, Sequence

from kakeyalogic.grains import (
    Grain,
    GrainBundle,
    GrainCell,
    Outcome,
    SAVER,
    parse_grain,
    parse_outcome,
)


@dataclass(frozen=True)
class TypedObject:
    object_id: str
    direction_id: str
    type: str
    content: str
    held: bool = True
    recoverable: bool = True
    role: str = ""
    version: str = "1"
    provenance: str = ""
    authority: str = ""
    cluster_id: str = ""
    notes: str = ""

    def to_dict(self) -> dict:
        return {
            "object_id": self.object_id,
            "direction_id": self.direction_id,
            "type": self.type,
            "content": self.content,
            "held": self.held,
            "recoverable": self.recoverable,
            "role": self.role,
            "version": self.version,
            "provenance": self.provenance,
            "authority": self.authority,
            "cluster_id": self.cluster_id,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Direction:
    direction_id: str
    required_grains: tuple[Grain, ...] = SAVER
    description: str = ""

    def to_dict(self) -> dict:
        return {
            "direction_id": self.direction_id,
            "required_grains": [g.value for g in self.required_grains],
            "description": self.description,
        }


@dataclass(frozen=True)
class InteriorSample:
    u: float
    outcomes: Mapping[Grain, Outcome]
    note: str = ""
    per_direction: Mapping[str, Mapping[Grain, Outcome]] | None = None

    def __post_init__(self) -> None:
        if not 0.0 <= self.u <= 1.0:
            raise ValueError(f"interior sample u={self.u} is outside [0, 1]")

    def outcomes_for(self, direction_id: str) -> Mapping[Grain, Outcome]:
        if self.per_direction and direction_id in self.per_direction:
            return self.per_direction[direction_id]
        return self.outcomes

    def to_dict(self) -> dict:
        payload = {
            "u": self.u,
            "outcomes": {g.value: o.value for g, o in self.outcomes.items()},
            "note": self.note,
        }
        if self.per_direction:
            payload["per_direction"] = {
                d: {g.value: o.value for g, o in grains.items()}
                for d, grains in self.per_direction.items()
            }
        return payload


@dataclass(frozen=True)
class CandidateEdge:
    """A candidate transformation e: src → dst with declared grain evidence."""

    edge_id: str
    src: str
    dst: str
    cost: float
    direction_ids: tuple[str, ...]
    required_grains: tuple[Grain, ...]
    declared: GrainBundle
    interior: tuple[InteriorSample, ...] = ()
    claimed_interior_scale: bool = False
    cluster_id: str = ""
    notes: str = ""
    authority_inherited_from_cluster: bool = False

    def __post_init__(self) -> None:
        if self.cost <= 0:
            raise ValueError(
                f"operational edge cost must be positive; {self.edge_id} has cost={self.cost}"
            )

    def required_pairs(self) -> tuple[tuple[str, Grain], ...]:
        return tuple((d, q) for d in self.direction_ids for q in self.required_grains)

    def to_dict(self) -> dict:
        return {
            "edge_id": self.edge_id,
            "src": self.src,
            "dst": self.dst,
            "cost": self.cost,
            "direction_ids": list(self.direction_ids),
            "required_grains": [g.value for g in self.required_grains],
            "declared": self.declared.to_dict(),
            "interior": [s.to_dict() for s in self.interior],
            "claimed_interior_scale": self.claimed_interior_scale,
            "cluster_id": self.cluster_id,
            "notes": self.notes,
            "authority_inherited_from_cluster": self.authority_inherited_from_cluster,
        }


@dataclass(frozen=True)
class OverlapCluster:
    cluster_id: str
    member_direction_ids: tuple[str, ...]
    representation_unit: str
    notes: str = ""


@dataclass
class FieldState:
    """Research state at one evaluation epoch.

    Unresolved and failed edges remain in `edges`. Deleting them would erase
    evidence and weaken later refinement.
    """

    state_id: str
    nodes: tuple[str, ...]
    directions: dict[str, Direction]
    objects: dict[str, TypedObject]
    edges: dict[str, CandidateEdge]
    clusters: dict[str, OverlapCluster] = field(default_factory=dict)
    allowed_boundary: tuple[str, ...] = ()
    confirmed_reachable: tuple[str, ...] = ()
    modeled_envelope: tuple[str, ...] = ()
    current: str = ""
    goal: str = ""
    epoch: int = 0
    notes: str = ""

    def copy(self) -> "FieldState":
        return FieldState(
            state_id=self.state_id,
            nodes=self.nodes,
            directions=dict(self.directions),
            objects={k: v for k, v in self.objects.items()},
            edges={k: v for k, v in self.edges.items()},
            clusters=dict(self.clusters),
            allowed_boundary=self.allowed_boundary,
            confirmed_reachable=self.confirmed_reachable,
            modeled_envelope=self.modeled_envelope,
            current=self.current,
            goal=self.goal,
            epoch=self.epoch,
            notes=self.notes,
        )

    def required_direction_ids(self) -> tuple[str, ...]:
        return tuple(sorted(self.directions))

    def objects_for(self, direction_id: str) -> list[TypedObject]:
        return [o for o in self.objects.values() if o.direction_id == direction_id]


def bundle_from_declared(
    direction_ids: Sequence[str],
    grains: Sequence[Grain],
    declared: Mapping[str, str],
    *,
    check: str,
    reason: str,
    evidence_refs: Sequence[str] = (),
    per_direction: Mapping[str, Mapping[str, str]] | None = None,
) -> GrainBundle:
    cells: list[GrainCell] = []
    for direction_id in direction_ids:
        local = per_direction.get(direction_id, {}) if per_direction else {}
        for grain in grains:
            raw = local.get(grain.value, declared.get(grain.value, Outcome.NOT_EVALUATED.value))
            cells.append(
                GrainCell(
                    direction_id=direction_id,
                    grain=grain,
                    outcome=parse_outcome(raw) if isinstance(raw, str) else raw,
                    check=check,
                    reason=reason,
                    evidence_refs=tuple(evidence_refs),
                )
            )
    return GrainBundle(cells=tuple(cells))


def parse_interior(raw_samples: Sequence[Mapping], grains: Sequence[Grain]) -> tuple[InteriorSample, ...]:
    samples: list[InteriorSample] = []
    for item in raw_samples:
        outcomes = {
            parse_grain(k): parse_outcome(v) for k, v in item.get("outcomes", {}).items()
        }
        per_dir = None
        if "per_direction" in item:
            per_dir = {
                d: {parse_grain(k): parse_outcome(v) for k, v in mapping.items()}
                for d, mapping in item["per_direction"].items()
            }
        samples.append(
            InteriorSample(
                u=float(item["u"]),
                outcomes=outcomes,
                note=item.get("note", ""),
                per_direction=per_dir,
            )
        )
        missing = [g for g in grains if g not in samples[-1].outcomes]
        if missing and per_dir is None:
            # Interior samples may omit grains; omitted grains stay NOT_EVALUATED at that u.
            filled = dict(samples[-1].outcomes)
            for g in missing:
                filled[g] = Outcome.NOT_EVALUATED
            samples[-1] = InteriorSample(
                u=samples[-1].u,
                outcomes=filled,
                note=samples[-1].note,
                per_direction=samples[-1].per_direction,
            )
    return tuple(samples)


def replace_object(state: FieldState, obj: TypedObject) -> FieldState:
    new_state = state.copy()
    new_state.objects[obj.object_id] = obj
    return new_state


def drop_object(state: FieldState, object_id: str, *, reason: str) -> FieldState:
    new_state = state.copy()
    obj = new_state.objects[object_id]
    new_state.objects[object_id] = replace(
        obj,
        held=False,
        recoverable=False,
        notes=(obj.notes + f" | dropped: {reason}").strip(" |"),
    )
    new_state.epoch = state.epoch + 1
    return new_state

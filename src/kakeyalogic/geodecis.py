"""Geodecis: operational route selection on KakeyaLogic-admitted transitions.

The cost is explicitly operational. It is not a safety, ethics, truth, or
Love-Squared Coherence score. KakeyaLogic determines admissibility; Geodecis
chooses among admitted continuations.
"""

from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from math import inf

from kakeyalogic.gate import EvaluatedEdge
from kakeyalogic.grains import TransitionClass


@dataclass(frozen=True)
class Path:
    nodes: tuple[str, ...]
    edge_ids: tuple[str, ...]
    cost: float

    def to_dict(self) -> dict:
        return {
            "nodes": list(self.nodes),
            "edge_ids": list(self.edge_ids),
            "cost": None if self.cost == inf else self.cost,
        }


@dataclass(frozen=True)
class DistanceReport:
    source: str
    goal: str
    admitted: Path
    diamond: Path
    evidence_sensitivity: float | None
    next_step: str | None
    next_edge_id: str | None

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "goal": self.goal,
            "admitted": self.admitted.to_dict(),
            "diamond": self.diamond.to_dict(),
            "evidence_sensitivity": self.evidence_sensitivity,
            "next_step": self.next_step,
            "next_edge_id": self.next_edge_id,
            "note": (
                "evidence_sensitivity is a diagnostic, not permission to traverse "
                "unresolved edges"
            ),
        }


def _usable(item: EvaluatedEdge, *, include_unresolved: bool) -> bool:
    if item.classification is TransitionClass.ADMITTED:
        return True
    if include_unresolved and item.classification is TransitionClass.UNRESOLVED:
        return True
    return False


def shortest_path(
    evaluated: dict[str, EvaluatedEdge],
    source: str,
    goal: str,
    *,
    include_unresolved: bool = False,
) -> Path:
    """Directed Dijkstra on positive operational costs. No symmetry assumed."""
    if source == goal:
        return Path(nodes=(source,), edge_ids=(), cost=0.0)

    adj: dict[str, list[tuple[float, str, str]]] = {}
    for item in evaluated.values():
        if not _usable(item, include_unresolved=include_unresolved):
            continue
        adj.setdefault(item.edge.src, []).append(
            (item.edge.cost, item.edge.dst, item.edge.edge_id)
        )

    dist: dict[str, float] = {source: 0.0}
    prev: dict[str, tuple[str, str]] = {}
    heap: list[tuple[float, str]] = [(0.0, source)]
    seen: set[str] = set()

    while heap:
        cost, node = heappop(heap)
        if node in seen:
            continue
        seen.add(node)
        if node == goal:
            break
        for edge_cost, dst, edge_id in adj.get(node, []):
            cand = cost + edge_cost
            if cand < dist.get(dst, inf):
                dist[dst] = cand
                prev[dst] = (node, edge_id)
                heappush(heap, (cand, dst))

    if goal not in dist:
        return Path(nodes=(), edge_ids=(), cost=inf)

    nodes = [goal]
    edge_ids: list[str] = []
    cursor = goal
    while cursor != source:
        parent, edge_id = prev[cursor]
        edge_ids.append(edge_id)
        nodes.append(parent)
        cursor = parent
    nodes.reverse()
    edge_ids.reverse()
    return Path(nodes=tuple(nodes), edge_ids=tuple(edge_ids), cost=dist[goal])


def admitted_distance(evaluated: dict[str, EvaluatedEdge], source: str, goal: str) -> Path:
    return shortest_path(evaluated, source, goal, include_unresolved=False)


def diamond_distance(evaluated: dict[str, EvaluatedEdge], source: str, goal: str) -> Path:
    """Distance on E^A ∪ E^U. Diagnostic only; unresolved edges are not traversable."""
    return shortest_path(evaluated, source, goal, include_unresolved=True)


def evidence_sensitivity(admitted: Path, diamond: Path) -> float | None:
    if admitted.cost is inf or diamond.cost is inf:
        return None
    delta = admitted.cost - diamond.cost
    if delta < 0:
        # Numerical guard: diamond is a relaxation of admitted, so delta >= 0.
        return 0.0
    return delta


def next_step(
    evaluated: dict[str, EvaluatedEdge],
    source: str,
    goal: str,
) -> tuple[str | None, str | None]:
    """Geodecis one-step policy: argmin_y [ℓ(x,y) + d^A(y,g)] over admitted edges."""
    outgoing = [
        item
        for item in evaluated.values()
        if item.edge.src == source and item.classification is TransitionClass.ADMITTED
    ]
    if not outgoing:
        return None, None
    best: tuple[float, str, str] | None = None
    for item in outgoing:
        rest = admitted_distance(evaluated, item.edge.dst, goal)
        if rest.cost is inf:
            continue
        total = item.edge.cost + rest.cost
        candidate = (total, item.edge.dst, item.edge.edge_id)
        if best is None or candidate < best:
            best = candidate
    if best is None:
        return None, None
    return best[1], best[2]


def geodecis_report(
    evaluated: dict[str, EvaluatedEdge],
    source: str,
    goal: str,
) -> DistanceReport:
    admitted = admitted_distance(evaluated, source, goal)
    diamond = diamond_distance(evaluated, source, goal)
    nxt, nxt_edge = next_step(evaluated, source, goal)
    return DistanceReport(
        source=source,
        goal=goal,
        admitted=admitted,
        diamond=diamond,
        evidence_sensitivity=evidence_sensitivity(admitted, diamond),
        next_step=nxt,
        next_edge_id=nxt_edge,
    )

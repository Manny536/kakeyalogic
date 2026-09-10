"""Refinement restores finer grain evidence without inventing content or authority."""

from __future__ import annotations

from dataclasses import dataclass, replace

from kakeyalogic.gate import EvaluatedEdge, evaluate_edge
from kakeyalogic.grains import Grain, GrainCell, Outcome, parse_grain, parse_outcome
from kakeyalogic.state import CandidateEdge, InteriorSample


@dataclass(frozen=True)
class RefinementSource:
    """Permitted finer evidence for an unresolved or coarse edge."""

    edge_id: str
    grain_updates: dict[str, dict[str, str]]
    interior: tuple[InteriorSample, ...] = ()
    grant_refs: tuple[str, ...] = ()
    source_refs: tuple[str, ...] = ()
    invent_authority: bool = False
    invent_content: bool = False
    note: str = ""


@dataclass(frozen=True)
class RefineReport:
    applied: tuple[str, ...]
    refused: tuple[tuple[str, str], ...]
    evaluated: dict[str, EvaluatedEdge]

    def to_dict(self) -> dict:
        return {
            "applied": list(self.applied),
            "refused": [{"edge_id": e, "reason": r} for e, r in self.refused],
            "evaluated": {k: v.to_dict() for k, v in self.evaluated.items()},
        }


def refine_edges(
    edges: dict[str, CandidateEdge],
    sources: dict[str, RefinementSource],
) -> tuple[dict[str, CandidateEdge], RefineReport]:
    updated = dict(edges)
    applied: list[str] = []
    refused: list[tuple[str, str]] = []
    evaluated: dict[str, EvaluatedEdge] = {}

    for edge_id, source in sources.items():
        edge = updated.get(edge_id)
        if edge is None:
            refused.append((edge_id, "unknown edge"))
            continue
        if source.invent_authority:
            refused.append((edge_id, "refinement cannot invent missing authority"))
            continue
        if source.invent_content:
            refused.append((edge_id, "refinement cannot invent missing content"))
            continue

        bundle = edge.declared
        for direction_id, mapping in source.grain_updates.items():
            for grain_key, outcome_key in mapping.items():
                grain = parse_grain(grain_key)
                outcome = parse_outcome(outcome_key)
                existing = bundle.cell(direction_id, grain)
                if grain is Grain.A and outcome is Outcome.PASS and not source.grant_refs:
                    refused.append((edge_id, "Authority PASS requires a grant reference"))
                    bundle = edge.declared
                    break
                if grain is Grain.S and outcome is Outcome.PASS and not source.source_refs:
                    if existing and existing.outcome is not Outcome.PASS:
                        refused.append((edge_id, "Semantic PASS from unresolved/fail requires a source reference"))
                        bundle = edge.declared
                        break
                bundle = bundle.replace(
                    GrainCell(
                        direction_id=direction_id,
                        grain=grain,
                        outcome=outcome,
                        check="refinement",
                        reason=source.note or "finer retained or permitted source",
                        evidence_refs=tuple(source.grant_refs or source.source_refs),
                    )
                )
            else:
                continue
            break
        else:
            new_interior = edge.interior + source.interior
            new_edge = replace(
                edge,
                declared=bundle,
                interior=new_interior,
                notes=(edge.notes + " | refined").strip(" |"),
            )
            updated[edge_id] = new_edge
            evaluated[edge_id] = evaluate_edge(new_edge)
            applied.append(edge_id)
            continue
        # refused mid-update: keep original
        evaluated[edge_id] = evaluate_edge(edge)

    return updated, RefineReport(
        applied=tuple(applied),
        refused=tuple(refused),
        evaluated=evaluated,
    )

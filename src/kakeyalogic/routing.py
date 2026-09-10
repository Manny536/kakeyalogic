"""KakeyaLogic routing loop.

Observe → Grain → Gate → Overlap → Refine → Route → Receipt → Retain
"""

from __future__ import annotations

from kakeyalogic.completeness import kcomplete, retention_bundle_from_objects
from kakeyalogic.containment import evaluate_containment
from kakeyalogic.gate import grain_and_gate, partition_evaluated
from kakeyalogic.geodecis import geodecis_report
from kakeyalogic.grains import GrainBundle
from kakeyalogic.overlap import check_overlap, enforce_overlap
from kakeyalogic.receipts import RetentionLedger, RoutingReceipt
from kakeyalogic.refine import RefinementSource, refine_edges
from kakeyalogic.state import FieldState, drop_object


LIMITATIONS = (
    "Synthetic reference router. Grain predicates are declared in the fixture, "
    "not inferred from natural language.",
    "Operational SIUT validity remains OPEN until later deployment evidence exists.",
    "Geodecis cost is an explicitly chosen operational cost, not a safety or L²_C score.",
    "An admitted route is not a containment proof.",
    "This runtime does not enforce production control-plane blocking.",
)


class KakeyaRouter:
    def __init__(
        self,
        state: FieldState,
        *,
        specification_version: str = "1.0",
        fixture_id: str = "",
    ) -> None:
        self.state = state
        self.specification_version = specification_version
        self.fixture_id = fixture_id
        self.ledger = RetentionLedger()
        self._prior_objects = dict(state.objects)

    def run(
        self,
        *,
        source: str | None = None,
        goal: str | None = None,
        refinements: dict[str, RefinementSource] | None = None,
        later_update: dict | None = None,
    ) -> RoutingReceipt:
        source = source or self.state.current
        goal = goal or self.state.goal
        if not source or not goal:
            raise ValueError("source and goal are required")

        # Observe: candidate continuations already live on FieldState.edges.
        observed = dict(self.state.edges)

        # Grain + Gate.
        evaluated, partition = grain_and_gate(observed)
        self.ledger.record_partition(partition)

        # Overlap.
        overlap = check_overlap(self.state, evaluated)
        evaluated = enforce_overlap(evaluated, overlap)
        partition = partition_evaluated(evaluated)
        self.ledger.record_partition(partition)

        # Refine (optional; default run does not auto-resolve unknowns).
        refine_report = None
        if refinements:
            new_edges, refine_report = refine_edges(observed, refinements)
            self.state.edges = new_edges
            evaluated, partition = grain_and_gate(self.state.edges)
            self.ledger.record_partition(partition)
            overlap = check_overlap(self.state, evaluated)
            evaluated = enforce_overlap(evaluated, overlap)
            partition = partition_evaluated(evaluated)
            self.ledger.record_partition(partition)

        # Route only through admitted transitions.
        geo = geodecis_report(evaluated, source, goal)

        # Containment is a separate receipt.
        containment = evaluate_containment(
            allowed_boundary=self.state.allowed_boundary,
            confirmed_reachable=self.state.confirmed_reachable,
            modeled_envelope=self.state.modeled_envelope,
        )

        # Completeness over the selected admitted path's grain cells, if any.
        selected_cells = []
        for edge_id in geo.admitted.edge_ids:
            selected_cells.extend(evaluated[edge_id].bundle.cells)
        completeness = kcomplete(
            GrainBundle(cells=tuple(selected_cells)),
            self.state.required_direction_ids(),
            required_grains_by_direction={
                d.direction_id: d.required_grains
                for d in self.state.directions.values()
            },
        )

        retention = self._retain(later_update)

        receipt = RoutingReceipt(
            specification_version=self.specification_version,
            fixture_id=self.fixture_id,
            source=source,
            goal=goal,
            partition=partition,
            evaluated=evaluated,
            overlap=overlap,
            refine=refine_report,
            geodecis=geo,
            containment=containment,
            completeness=completeness,
            retention=retention,
            selected_edge_ids=geo.admitted.edge_ids,
            selected_nodes=geo.admitted.nodes,
            unresolved_alternatives=partition.unresolved,
            failed_evidence=partition.failed,
            limitations=LIMITATIONS,
        )
        self.ledger.receipts.append(receipt.to_dict())
        return receipt

    def _retain(self, later_update: dict | None) -> dict:
        report: dict = {
            "epoch": self.state.epoch,
            "held_failed_edges": list(self.ledger.failed_edge_ids),
            "held_unresolved_edges": list(self.ledger.unresolved_edge_ids),
            "later_update": None,
            "retention_after_update": None,
        }
        if not later_update:
            return report
        dropped = list(later_update.get("drop_objects", []))
        reason = later_update.get("reason", "later state update")
        for object_id in dropped:
            if object_id in self.state.objects:
                self.state = drop_object(self.state, object_id, reason=reason)
                self.ledger.record_drop(object_id, reason, self.state.epoch)
        r_bundle = retention_bundle_from_objects(
            self.state, prior_objects=self._prior_objects
        )
        report["later_update"] = {
            "drop_objects": dropped,
            "reason": reason,
            "epoch": self.state.epoch,
        }
        report["retention_after_update"] = r_bundle.to_dict()
        report["held_failed_edges"] = list(self.ledger.failed_edge_ids)
        report["held_unresolved_edges"] = list(self.ledger.unresolved_edge_ids)
        return report

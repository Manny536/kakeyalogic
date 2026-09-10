"""Contract tests: gate, overlap, refine, completeness, cost, and score non-override."""

from __future__ import annotations

import sys
import unittest
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kakeyalogic.calibration import load_fixture
from kakeyalogic.completeness import kcomplete
from kakeyalogic.containment import ContainmentVerdict, evaluate_containment
from kakeyalogic.gate import evaluate_edge, grain_and_gate
from kakeyalogic.geodecis import admitted_distance, diamond_distance
from kakeyalogic.grains import (
    Grain,
    GrainBundle,
    GrainCell,
    Outcome,
    TransitionClass,
    classify_outcomes,
)
from kakeyalogic.overlap import check_overlap
from kakeyalogic.refine import RefinementSource, refine_edges
from kakeyalogic.state import InteriorSample


class GateContracts(unittest.TestCase):
    def test_not_evaluated_is_not_unresolved(self) -> None:
        self.assertEqual(
            classify_outcomes([Outcome.PASS, Outcome.UNRESOLVED]),
            TransitionClass.UNRESOLVED,
        )
        self.assertEqual(
            classify_outcomes([Outcome.PASS, Outcome.NOT_EVALUATED]),
            TransitionClass.UNRESOLVED,
        )
        fixture = load_fixture()
        evaluated, partition = grain_and_gate(fixture.state.edges)
        shortcut = evaluated["e_shortcut"]
        uneval = evaluated["e_not_evaluated"]
        self.assertEqual(shortcut.classification, TransitionClass.UNRESOLVED)
        self.assertEqual(uneval.classification, TransitionClass.UNRESOLVED)
        vis = {c.direction_id: c.outcome for c in shortcut.bundle.cells if c.grain is Grain.V}
        self.assertTrue(all(o is Outcome.UNRESOLVED for o in vis.values()))
        raw = {c.outcome for c in uneval.bundle.cells}
        self.assertEqual(raw, {Outcome.NOT_EVALUATED})
        self.assertIn("e_shortcut", partition.unresolved)
        self.assertIn("e_not_evaluated", partition.unresolved)

    def test_fail_dominates_unresolved(self) -> None:
        self.assertEqual(
            classify_outcomes([Outcome.FAIL, Outcome.UNRESOLVED, Outcome.PASS]),
            TransitionClass.FAILED,
        )

    def test_empty_required_set_is_not_applicable(self) -> None:
        self.assertEqual(classify_outcomes([]), TransitionClass.NOT_APPLICABLE)
        report = kcomplete(GrainBundle(), ())
        self.assertEqual(report.status, "NOT_APPLICABLE")
        self.assertFalse(report.kcomplete)

    def test_weights_cannot_override_gate(self) -> None:
        fixture = load_fixture()
        with self.assertRaises(ValueError):
            grain_and_gate(fixture.state.edges, weights={"S": 99.0, "A": 0.01})

    def test_four_pass_one_fail_is_not_admitted(self) -> None:
        item = evaluate_edge(load_fixture().state.edges["e_failed_authority"])
        outcomes = item.bundle.outcomes_for(item.edge.required_pairs())
        self.assertIn(Outcome.FAIL, outcomes)
        self.assertGreater(outcomes.count(Outcome.PASS), 0)
        self.assertEqual(item.classification, TransitionClass.FAILED)


class OverlapRefineContracts(unittest.TestCase):
    def test_overlap_keeps_independent_grain_state(self) -> None:
        fixture = load_fixture()
        evaluated, _ = grain_and_gate(fixture.state.edges)
        report = check_overlap(fixture.state, evaluated)
        self.assertTrue(report.ok)

    def test_authority_from_cluster_proximity_fails_overlap(self) -> None:
        fixture = load_fixture()
        poisoned = dict(fixture.state.edges)
        poisoned["e_via1"] = replace(
            poisoned["e_via1"], authority_inherited_from_cluster=True
        )
        evaluated, _ = grain_and_gate(poisoned)
        state = fixture.state.copy()
        state.edges = poisoned
        report = check_overlap(state, evaluated)
        self.assertFalse(report.ok)
        self.assertTrue(any(i.code == "authority_from_proximity" for i in report.issues))

    def test_refine_cannot_invent_authority(self) -> None:
        fixture = load_fixture()
        _, report = refine_edges(
            fixture.state.edges,
            {
                "e_shortcut": RefinementSource(
                    edge_id="e_shortcut",
                    grain_updates={"d_approval": {"A": "PASS"}},
                    invent_authority=True,
                    note="forged grant",
                )
            },
        )
        self.assertIn("e_shortcut", [e for e, _ in report.refused])

    def test_refine_can_resolve_visibility_with_interior(self) -> None:
        fixture = load_fixture()
        pass_map = {g: Outcome.PASS for g in (Grain.S, Grain.A, Grain.V, Grain.E, Grain.R)}
        samples = (
            InteriorSample(u=0.0, outcomes=pass_map),
            InteriorSample(u=0.5, outcomes=pass_map, note="recovered interior"),
            InteriorSample(u=1.0, outcomes=pass_map),
        )
        updated, report = refine_edges(
            fixture.state.edges,
            {
                "e_shortcut": RefinementSource(
                    edge_id="e_shortcut",
                    grain_updates={
                        "d_safeguard": {"V": "PASS"},
                        "d_approval": {"V": "PASS"},
                    },
                    interior=samples,
                    source_refs=("obj_redline",),
                    grant_refs=("grant:ops-1",),
                    note="interior recovered from retained source",
                )
            },
        )
        self.assertIn("e_shortcut", report.applied)
        item = evaluate_edge(updated["e_shortcut"])
        self.assertEqual(item.classification, TransitionClass.ADMITTED)
        self.assertFalse(item.interior.unobserved_claimed_interior)


class CompletenessAndContainment(unittest.TestCase):
    def test_kcomplete_blocked_by_unresolved_grain(self) -> None:
        cells = [
            GrainCell("d", Grain.S, Outcome.PASS, "t", "ok"),
            GrainCell("d", Grain.A, Outcome.PASS, "t", "ok"),
            GrainCell("d", Grain.V, Outcome.UNRESOLVED, "t", "gap"),
            GrainCell("d", Grain.E, Outcome.PASS, "t", "ok"),
            GrainCell("d", Grain.R, Outcome.PASS, "t", "ok"),
        ]
        report = kcomplete(GrainBundle(tuple(cells)), ("d",))
        self.assertFalse(report.kcomplete)
        self.assertAlmostEqual(report.diagnostic_score or 0.0, 0.0)

    def test_pass_model_is_conditional(self) -> None:
        report = evaluate_containment(
            allowed_boundary=("a", "b"),
            confirmed_reachable=("a", "b"),
            modeled_envelope=("a", "b"),
        )
        self.assertEqual(report.verdict, ContainmentVerdict.PASS_MODEL)
        self.assertIn("conditional", report.note)

    def test_open_when_coverage_insufficient(self) -> None:
        report = evaluate_containment(
            allowed_boundary=("a", "b"),
            confirmed_reachable=("a",),
            modeled_envelope=("a", "b"),
            coverage_declared=False,
        )
        self.assertEqual(report.verdict, ContainmentVerdict.OPEN)


class GeodecisContracts(unittest.TestCase):
    def test_failed_edges_never_enter_admitted_or_diamond(self) -> None:
        fixture = load_fixture()
        evaluated, _ = grain_and_gate(fixture.state.edges)
        admitted = admitted_distance(evaluated, "start", "goal")
        diamond = diamond_distance(evaluated, "start", "goal")
        self.assertNotIn("e_failed_authority", admitted.edge_ids)
        self.assertNotIn("e_boundary", admitted.edge_ids)
        self.assertNotIn("e_failed_authority", diamond.edge_ids)
        self.assertNotIn("e_boundary", diamond.edge_ids)
        self.assertIn("e_shortcut", diamond.edge_ids)
        self.assertNotIn("e_shortcut", admitted.edge_ids)

    def test_positive_cost_enforced(self) -> None:
        fixture = load_fixture()
        edge = fixture.state.edges["e_via1"]
        with self.assertRaises(ValueError):
            replace(edge, cost=0.0)


if __name__ == "__main__":
    unittest.main()

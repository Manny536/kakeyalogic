"""Behavioral validation of the six specification-1.0 synthetic cases."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kakeyalogic.calibration import load_fixture
from kakeyalogic.grains import Grain, Outcome, TransitionClass
from kakeyalogic.routing import KakeyaRouter


class SaverBehavioralTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = load_fixture()
        cls.expected = cls.fixture.expected
        router = KakeyaRouter(
            cls.fixture.state.copy(),
            specification_version=cls.fixture.specification_version,
            fixture_id=cls.fixture.fixture_id,
        )
        cls.receipt = router.run(later_update=cls.fixture.raw.get("later_update"))
        cls.payload = cls.receipt.to_dict()

    def test_1_shortest_admitted_route(self) -> None:
        self.assertEqual(self.receipt.selected_nodes, tuple(self.expected["admitted_path_nodes"]))
        self.assertEqual(self.receipt.selected_edge_ids, tuple(self.expected["admitted_path_edges"]))
        self.assertEqual(self.receipt.geodecis.admitted.cost, self.expected["admitted_cost"])
        self.assertNotIn("e_long", self.receipt.selected_edge_ids)
        self.assertNotIn("e_smooth_goal", self.receipt.selected_edge_ids)

    def test_2_unresolved_shortcut_visible_not_traversed(self) -> None:
        shortcut = self.expected["shortcut_edge"]
        self.assertIn(shortcut, self.receipt.partition.unresolved)
        self.assertNotIn(shortcut, self.receipt.selected_edge_ids)
        self.assertEqual(self.receipt.geodecis.diamond.cost, self.expected["diamond_cost"])
        self.assertEqual(
            self.receipt.geodecis.evidence_sensitivity,
            self.expected["evidence_sensitivity"],
        )
        for cell in self.receipt.evaluated[shortcut].bundle.cells:
            if cell.grain is Grain.V:
                self.assertEqual(cell.outcome, Outcome.UNRESOLVED)
        self.assertIn(shortcut, self.receipt.unresolved_alternatives)
        self.assertIn(shortcut, self.receipt.retention["held_unresolved_edges"])

    def test_3_failed_transition_retained_as_evidence(self) -> None:
        failed = self.expected["failed_authority_edge"]
        self.assertIn(failed, self.receipt.partition.failed)
        self.assertIn(failed, self.receipt.failed_evidence)
        self.assertIn(failed, self.receipt.retention["held_failed_edges"])
        self.assertIn(failed, self.fixture.state.edges)
        cell = self.receipt.evaluated[failed].bundle.cell("d_approval", Grain.A)
        self.assertIsNotNone(cell)
        self.assertEqual(cell.outcome, Outcome.FAIL)

    def test_4_endpoint_pass_interior_fail(self) -> None:
        edge_id = self.expected["boundary_error_edge"]
        item = self.receipt.evaluated[edge_id]
        self.assertTrue(item.interior.boundary_error)
        self.assertEqual(item.classification, TransitionClass.FAILED)
        self.assertIn(edge_id, self.receipt.partition.failed)
        for direction_id in ("d_safeguard", "d_approval"):
            cell = item.bundle.cell(direction_id, Grain.S)
            self.assertEqual(cell.outcome, Outcome.FAIL)
        self.assertNotIn("smooth", self.receipt.selected_nodes)

    def test_5_retention_regression_after_later_update(self) -> None:
        cells = self.receipt.retention["retention_after_update"]
        by_dir = {c["direction_id"]: c for c in cells if c["grain"] == Grain.R.value}
        self.assertEqual(
            by_dir[self.expected["retention_after_update_direction"]]["outcome"],
            self.expected["retention_after_update"],
        )
        self.assertIn("obj_redline", [d["object_id"] for d in self.receipt.retention["later_update"] and [
            {"object_id": x} for x in self.receipt.retention["later_update"]["drop_objects"]
        ]])
        self.assertIn(
            self.expected["failed_authority_edge"],
            self.receipt.retention["held_failed_edges"],
        )
        self.assertIn(
            self.expected["shortcut_edge"],
            self.receipt.retention["held_unresolved_edges"],
        )

    def test_6_planning_is_not_containment(self) -> None:
        self.assertEqual(self.receipt.selected_nodes, tuple(self.expected["admitted_path_nodes"]))
        self.assertEqual(self.receipt.containment.verdict.value, self.expected["containment_verdict"])
        self.assertEqual(
            list(self.receipt.containment.violators),
            self.expected["containment_violators"],
        )
        self.assertIn("leak", self.receipt.containment.confirmed_reachable)
        self.assertNotIn("leak", self.receipt.containment.allowed_boundary)


if __name__ == "__main__":
    unittest.main()

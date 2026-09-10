"""Regression cases from the reference implementation review."""

import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

import kakeyalogic
from kakeyalogic.calibration import load_fixture
from kakeyalogic.grains import Grain
from kakeyalogic.refine import RefinementSource
from kakeyalogic.routing import KakeyaRouter


class ReviewRegressions(unittest.TestCase):
    def test_default_fixture_is_packaged_and_matches_example(self):
        fixture = load_fixture()
        package = Path(kakeyalogic.__file__).resolve().parent
        self.assertTrue(fixture.path.is_relative_to(package))
        example = Path(__file__).resolve().parents[1] / "examples/typed_directional_state/saver_calibration_graph.json"
        self.assertEqual(fixture.path.read_bytes(), example.read_bytes())

    def test_invalid_authority_cannot_route_even_after_refinement(self):
        for refine in (False, True):
            with self.subTest(refine=refine):
                state = load_fixture().state.copy()
                state.edges["e_via1"] = replace(
                    state.edges["e_via1"], authority_inherited_from_cluster=True
                )
                refinements = {"e_via1": RefinementSource("e_via1", {})} if refine else None
                receipt = KakeyaRouter(state).run(refinements=refinements)
                self.assertFalse(receipt.overlap.ok)
                self.assertNotIn("e_via1", receipt.selected_edge_ids)
                self.assertNotIn("e_via1", receipt.partition.admitted)
                self.assertIn("e_via1", receipt.partition.failed)
                self.assertIn("e_via1", receipt.retention["held_failed_edges"])
                self.assertEqual(receipt.selected_edge_ids, ("e_long",))
                self.assertEqual(receipt.geodecis.admitted.cost, 12)

    def test_cluster_identity_failure_blocks_affected_edges(self):
        state = load_fixture().state.copy()
        cluster_id = state.edges["e_via1"].cluster_id
        cluster = state.clusters[cluster_id]
        state.clusters[cluster_id] = replace(
            cluster, member_direction_ids=cluster.member_direction_ids * 2
        )
        receipt = KakeyaRouter(state).run()
        affected = {e.edge_id for e in state.edges.values() if e.cluster_id == cluster_id}
        self.assertFalse(affected.intersection(receipt.selected_edge_ids))
        self.assertTrue(affected.issubset(receipt.partition.failed))

    def _load_subset(self, *, explicit=False):
        raw = {
            "fixture_id": "subset", "required_grains": ["S"],
            "nodes": ["start", "goal"], "source": "start", "goal": "goal",
            "directions": [{"direction_id": "d"}],
            "clusters": [{"cluster_id": "c", "member_direction_ids": ["d"]}],
            "edges": [{"edge_id": "e", "src": "start", "dst": "goal",
                       "cost": 1, "grains": {"S": "PASS"}, "cluster_id": "c"}],
        }
        if explicit:
            raw["directions"][0]["required_grains"] = ["S"]
            raw["edges"][0]["required_grains"] = ["S"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.json"
            path.write_text(json.dumps(raw), encoding="utf-8")
            return load_fixture(path)

    def test_missing_grain_declarations_inherit_fixture_default(self):
        fixture = self._load_subset()
        self.assertEqual(fixture.state.directions["d"].required_grains, (Grain.S,))
        self.assertEqual(fixture.state.edges["e"].required_grains, (Grain.S,))
        receipt = KakeyaRouter(fixture.state).run()
        self.assertEqual(receipt.selected_edge_ids, ("e",))

    def test_direction_subset_controls_completeness_and_overlap(self):
        receipt = KakeyaRouter(self._load_subset(explicit=True).state).run()
        self.assertTrue(receipt.overlap.ok)
        self.assertEqual(receipt.selected_edge_ids, ("e",))
        self.assertTrue(receipt.completeness.kcomplete)
        self.assertEqual(receipt.completeness.missing, ())


if __name__ == "__main__":
    unittest.main()

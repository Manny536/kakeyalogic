#!/usr/bin/env python3
"""Run the SAVER reference router on the synthetic calibration graph.

Deterministic, stdlib only. Prints a routing receipt and a calibration receipt.
Exit 0 if the six specification cases match the fixture's expected block.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from kakeyalogic.calibration import calibration_receipt, load_fixture  # noqa: E402
from kakeyalogic.grains import Grain, Outcome  # noqa: E402
from kakeyalogic.routing import KakeyaRouter  # noqa: E402


def _match(receipt: dict, expected: dict) -> list[str]:
    failures: list[str] = []
    geo = receipt["geodecis"]
    part = receipt["partition"]
    if receipt["selected_nodes"] != expected["admitted_path_nodes"]:
        failures.append(
            f"admitted path {receipt['selected_nodes']} != {expected['admitted_path_nodes']}"
        )
    if receipt["selected_edge_ids"] != expected["admitted_path_edges"]:
        failures.append(
            f"admitted edges {receipt['selected_edge_ids']} != {expected['admitted_path_edges']}"
        )
    if geo["admitted"]["cost"] != expected["admitted_cost"]:
        failures.append(f"admitted cost {geo['admitted']['cost']} != {expected['admitted_cost']}")
    if geo["diamond"]["cost"] != expected["diamond_cost"]:
        failures.append(f"diamond cost {geo['diamond']['cost']} != {expected['diamond_cost']}")
    if geo["evidence_sensitivity"] != expected["evidence_sensitivity"]:
        failures.append(
            f"evidence sensitivity {geo['evidence_sensitivity']} != {expected['evidence_sensitivity']}"
        )
    if expected["shortcut_edge"] in receipt["selected_edge_ids"]:
        failures.append("unresolved shortcut was traversed")
    if expected["shortcut_edge"] not in part["unresolved"]:
        failures.append("unresolved shortcut is not visible in E^U")
    if expected["failed_authority_edge"] not in part["failed"]:
        failures.append("failed authority edge missing from E^F")
    if expected["failed_authority_edge"] not in receipt["retention"]["held_failed_edges"]:
        failures.append("failed edge was not retained")
    if expected["boundary_error_edge"] not in part["failed"]:
        failures.append("interior boundary-error edge was not failed")
    if receipt["evaluated"][expected["boundary_error_edge"]]["boundary_error"] is not True:
        failures.append("boundary-error flag missing")
    if sorted(part["admitted"]) != sorted(expected["admitted_edges"]):
        failures.append(f"admitted set {part['admitted']} != {expected['admitted_edges']}")
    if sorted(part["unresolved"]) != sorted(expected["unresolved_edges"]):
        failures.append(f"unresolved set {part['unresolved']} != {expected['unresolved_edges']}")
    if sorted(part["failed"]) != sorted(expected["failed_edges"]):
        failures.append(f"failed set {part['failed']} != {expected['failed_edges']}")
    if receipt["containment"]["verdict"] != expected["containment_verdict"]:
        failures.append(
            f"containment {receipt['containment']['verdict']} != {expected['containment_verdict']}"
        )
    if receipt["containment"]["violators"] != expected["containment_violators"]:
        failures.append(
            f"violators {receipt['containment']['violators']} != {expected['containment_violators']}"
        )
    r_cells = receipt["retention"]["retention_after_update"] or []
    r_map = {(c["direction_id"], c["grain"]): c["outcome"] for c in r_cells}
    key = (expected["retention_after_update_direction"], Grain.R.value)
    if r_map.get(key) != expected["retention_after_update"]:
        failures.append(f"retention after update {r_map.get(key)} != {expected['retention_after_update']}")
    shortcut_v = [
        c
        for c in receipt["evaluated"][expected["shortcut_edge"]]["bundle"]
        if c["grain"] == Grain.V.value
    ]
    if not shortcut_v or any(c["outcome"] != Outcome.UNRESOLVED.value for c in shortcut_v):
        failures.append("shortcut Visibility was not UNRESOLVED")
    uneval = [
        c["outcome"]
        for c in receipt["evaluated"]["e_not_evaluated"]["bundle"]
    ]
    if any(o != Outcome.NOT_EVALUATED.value for o in uneval):
        failures.append("NOT_EVALUATED was collapsed into another outcome")
    return failures


def main() -> int:
    fixture = load_fixture()
    router = KakeyaRouter(
        fixture.state.copy(),
        specification_version=fixture.specification_version,
        fixture_id=fixture.fixture_id,
    )
    receipt = router.run(later_update=fixture.raw.get("later_update"))
    payload = receipt.to_dict()
    calib = calibration_receipt(fixture, payload)
    failures = _match(payload, fixture.expected)

    print("=== SAVER REFERENCE ROUTING RECEIPT ===")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    print("=== SAVER CALIBRATION RECEIPT ===")
    print(json.dumps(calib, indent=2, ensure_ascii=False))
    print("fixture_sha256:", fixture.sha256)
    print("script_sha256:", hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    print("python:", sys.version.split()[0])
    print("spec_cases_met:", not failures)
    for item in failures:
        print("FAIL:", item)
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())

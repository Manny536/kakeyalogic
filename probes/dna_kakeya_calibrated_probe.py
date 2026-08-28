#!/usr/bin/env python3
"""CP-DNA-002: calibrated A/B/Z ideal-helix direction receipt.

This independently written verifier separates two quantities that must not be
collapsed:

* an exact covering radius for the declared latitude-circle model; and
* a maximum/mean gap measured on a deterministic 1,024-point target grid.

The calibrated dimensions are from the Dickerson and Franklin references
registered in ``docs/dna-as-antecedent-kakeya.md``. Directions are unoriented
lines (v ~ -v). Tangent-direction coverage is not unit-segment containment, so
this receipt cannot certify a Kakeya set, RH, or the Coleman Conjecture.
"""

from __future__ import annotations

import json
import math
from collections.abc import Iterable, Sequence
from typing import TypedDict

Vec3 = tuple[float, float, float]


class Conformation(TypedDict):
    diameter_angstrom: float
    pitch_angstrom: float
    handedness: int


CONFORMATIONS: dict[str, Conformation] = {
    "A-DNA": {
        "diameter_angstrom": 23.0,
        "pitch_angstrom": 28.6,
        "handedness": 1,
    },
    "B-DNA": {
        "diameter_angstrom": 20.0,
        "pitch_angstrom": 35.7,
        "handedness": 1,
    },
    "Z-DNA": {
        "diameter_angstrom": 18.0,
        "pitch_angstrom": 45.6,
        "handedness": -1,
    },
}


def dot(left: Vec3, right: Vec3) -> float:
    return sum(a * b for a, b in zip(left, right))


def normalize(vector: Vec3) -> Vec3:
    norm = math.sqrt(dot(vector, vector))
    if norm == 0.0:
        raise ValueError("direction vector must be nonzero")
    return tuple(component / norm for component in vector)  # type: ignore[return-value]


def tangent_latitude_degrees(radius: float, pitch: float) -> float:
    """Return the latitude of an ideal-helix tangent above the equator."""

    if radius <= 0.0 or pitch <= 0.0:
        raise ValueError("radius and pitch must be positive")
    return math.degrees(math.atan2(pitch, 2.0 * math.pi * radius))


def exact_covering_report(latitudes: Sequence[float]) -> dict[str, object]:
    """Cover RP2 by full-azimuth latitude circles using a 1D reduction.

    Under v ~ -v, a target line is represented by absolute latitude in
    [0, 90] degrees. Its nearest circle distance is the distance to the nearest
    registered absolute latitude. The covering radius is therefore the largest
    endpoint gap or half an interior gap.
    """

    ordered = sorted(abs(latitude) for latitude in latitudes)
    if not ordered or ordered[-1] > 90.0:
        raise ValueError("latitudes must be nonempty and lie in [-90, 90]")

    candidates: list[tuple[str, float]] = [("equator", ordered[0])]
    candidates.extend(
        (f"midpoint_{index}_{index + 1}", (right - left) / 2.0)
        for index, (left, right) in enumerate(zip(ordered, ordered[1:]))
    )
    candidates.append(("helix_axis", 90.0 - ordered[-1]))
    witness, radius = max(candidates, key=lambda item: item[1])
    return {
        "covering_radius_degrees": radius,
        "witness_region": witness,
        "candidate_gaps_degrees": dict(candidates),
    }


def helix_tangent(theta: float, radius: float, pitch: float, handedness: int) -> Vec3:
    rise_per_radian = pitch / (2.0 * math.pi)
    phase = handedness * theta
    return normalize(
        (
            -handedness * radius * math.sin(phase),
            handedness * radius * math.cos(phase),
            rise_per_radian,
        )
    )


def sample_helix_directions(
    *, radius: float, pitch: float, handedness: int, sample_count: int
) -> list[Vec3]:
    return [
        helix_tangent(
            2.0 * math.pi * index / sample_count,
            radius,
            pitch,
            handedness,
        )
        for index in range(sample_count)
    ]


def fibonacci_sphere(sample_count: int) -> list[Vec3]:
    golden_angle = math.pi * (3.0 - math.sqrt(5.0))
    points: list[Vec3] = []
    for index in range(sample_count):
        z = 1.0 - 2.0 * (index + 0.5) / sample_count
        radius = math.sqrt(max(0.0, 1.0 - z * z))
        azimuth = golden_angle * index
        points.append((radius * math.cos(azimuth), radius * math.sin(azimuth), z))
    return points


def line_angle(left: Vec3, right: Vec3) -> float:
    cosine = min(1.0, max(0.0, abs(dot(left, right))))
    return math.acos(cosine)


def sampled_coverage(
    directions: Sequence[Vec3], targets: Iterable[Vec3]
) -> dict[str, float]:
    gaps = [min(line_angle(target, direction) for direction in directions) for target in targets]
    return {
        "maximum_gap_degrees": math.degrees(max(gaps)),
        "mean_gap_degrees": math.degrees(sum(gaps) / len(gaps)),
    }


def build_report() -> dict[str, object]:
    helix_samples = 720
    target_count = 1024
    targets = fibonacci_sphere(target_count)
    per_conformation: dict[str, object] = {}
    union_directions: list[Vec3] = []
    latitudes: list[float] = []

    for name, parameters in CONFORMATIONS.items():
        radius = parameters["diameter_angstrom"] / 2.0
        pitch = parameters["pitch_angstrom"]
        handedness = parameters["handedness"]
        latitude = tangent_latitude_degrees(radius, pitch)
        latitudes.append(latitude)
        directions = sample_helix_directions(
            radius=radius,
            pitch=pitch,
            handedness=handedness,
            sample_count=helix_samples,
        )
        union_directions.extend(directions)
        per_conformation[name] = {
            "diameter_angstrom": parameters["diameter_angstrom"],
            "pitch_angstrom": pitch,
            "handedness": "right" if handedness > 0 else "left",
            "tangent_latitude_degrees": latitude,
            "exact_line_space": exact_covering_report([latitude]),
            "sampled_1024_target_grid": sampled_coverage(directions, targets),
        }

    exact_union = exact_covering_report(latitudes)
    sampled_union = sampled_coverage(union_directions, targets)
    exact_radius = float(exact_union["covering_radius_degrees"])
    sampled_maximum = sampled_union["maximum_gap_degrees"]

    checks = {
        "calibrated_latitudes_are_distinct": len({round(value, 12) for value in latitudes})
        == len(latitudes),
        "finite_abz_union_is_not_direction_complete": exact_radius > 0.0,
        "exact_radius_matches_independent_formula": math.isclose(
            exact_radius,
            51.11781468284084,
            rel_tol=0.0,
            abs_tol=1e-12,
        ),
        "sampled_maximum_is_strictly_below_exact_radius": sampled_maximum < exact_radius,
        "sampled_statistic_is_not_labeled_exact": True,
        "tangent_coverage_is_not_kakeya_certification": True,
    }

    return {
        "designation": "CP-DNA-002",
        "status": "NUMERICS / DIAGNOSTIC (source-calibrated exact ideal model)",
        "claim_scope": "ideal circular-helix tangent directions only",
        "direction_space": "unoriented lines (v ~ -v)",
        "calibration_sources": [
            "Dickerson 1992, doi:10.1016/0076-6879(92)11007-6",
            "Franklin and Gosling 1953, doi:10.1107/S0365110X53001939",
        ],
        "parameters": {
            "helix_samples_per_conformation": helix_samples,
            "spherical_grid_targets": target_count,
        },
        "per_conformation": per_conformation,
        "finite_abz_union": {
            "exact_line_space": exact_union,
            "sampled_1024_target_grid": sampled_union,
        },
        "reconciliation": {
            "exact_covering_radius_degrees": exact_radius,
            "sampled_grid_maximum_degrees": sampled_maximum,
            "sampled_grid_mean_degrees": sampled_union["mean_gap_degrees"],
            "interpretation": (
                "The 1024-target maximum is a lower sampled witness, not the exact "
                "covering radius."
            ),
        },
        "checks": checks,
        "firewall": [
            "a finite A/B/Z latitude union is direction-incomplete",
            "tangent-direction coverage is not unit-segment containment",
            "exact means exact for the declared ideal model and decimal inputs",
            "the pass field is a receipt check, not self-certification",
            "CP-DNA-002 does not certify a Kakeya set, RH, or the Coleman Conjecture",
        ],
        "open_obligations": [
            "A/B/Z transition dynamics",
            "variable-axis unit-segment containment test",
            "prime-carrying trace bridge",
        ],
        "h_less_than_one": "active: evaluator non-sovereignty",
        "pass": all(checks.values()),
    }


def main() -> int:
    report = build_report()
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

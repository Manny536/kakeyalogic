#!/usr/bin/env python3
"""Deterministic direction-coverage diagnostic for the DNA/Kakeya posit.

This probe studies tangent line directions, with v and -v identified. It does
not test containment of unit line segments and therefore cannot certify a
Kakeya set.
"""

from __future__ import annotations

import json
import math
from typing import Iterable, Sequence

Vec3 = tuple[float, float, float]


def dot(left: Vec3, right: Vec3) -> float:
    return sum(a * b for a, b in zip(left, right))


def normalize(vector: Vec3) -> Vec3:
    norm = math.sqrt(dot(vector, vector))
    if norm == 0.0:
        raise ValueError("direction vector must be nonzero")
    return tuple(component / norm for component in vector)  # type: ignore[return-value]


def helix_tangent(theta: float, radius: float, rise_per_radian: float) -> Vec3:
    """Unit tangent of H(t)=(a cos t, a sin t, bt)."""

    return normalize(
        (
            -radius * math.sin(theta),
            radius * math.cos(theta),
            rise_per_radian,
        )
    )


def sample_helix_directions(
    *, radius: float, rise_per_radian: float, sample_count: int
) -> list[Vec3]:
    return [
        helix_tangent(2.0 * math.pi * index / sample_count, radius, rise_per_radian)
        for index in range(sample_count)
    ]


def fibonacci_sphere(sample_count: int) -> list[Vec3]:
    """Deterministic approximately uniform target directions on S^2."""

    golden_angle = math.pi * (3.0 - math.sqrt(5.0))
    points: list[Vec3] = []
    for index in range(sample_count):
        z = 1.0 - 2.0 * (index + 0.5) / sample_count
        radius = math.sqrt(max(0.0, 1.0 - z * z))
        theta = golden_angle * index
        points.append((radius * math.cos(theta), radius * math.sin(theta), z))
    return points


def line_angle(left: Vec3, right: Vec3) -> float:
    """Angular distance for unoriented lines, identifying v with -v."""

    cosine = min(1.0, max(0.0, abs(dot(left, right))))
    return math.acos(cosine)


def coverage_report(directions: Sequence[Vec3], targets: Iterable[Vec3]) -> dict[str, float]:
    gaps = [min(line_angle(target, direction) for direction in directions) for target in targets]
    return {
        "worst_gap_degrees": math.degrees(max(gaps)),
        "mean_gap_degrees": math.degrees(sum(gaps) / len(gaps)),
    }


def build_report() -> dict[str, object]:
    radius = 1.0
    sample_count = 720
    target_count = 512
    reference_rise = 0.35
    pitch_ratios = (0.0, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 10.0, 50.0)

    targets = fibonacci_sphere(target_count)
    single = sample_helix_directions(
        radius=radius,
        rise_per_radian=reference_rise,
        sample_count=sample_count,
    )
    ensemble = [
        direction
        for ratio in pitch_ratios
        for direction in sample_helix_directions(
            radius=radius,
            rise_per_radian=ratio * radius,
            sample_count=sample_count,
        )
    ]

    single_coverage = coverage_report(single, targets)
    ensemble_coverage = coverage_report(ensemble, targets)
    axial_components = [direction[2] for direction in single]
    axial_spread = max(axial_components) - min(axial_components)

    checks = {
        "single_helix_is_restricted_latitude": axial_spread < 1e-12,
        "single_helix_is_not_direction_complete": single_coverage["worst_gap_degrees"] > 20.0,
        "pitch_ensemble_reduces_coverage_gap": (
            ensemble_coverage["worst_gap_degrees"]
            < 0.5 * single_coverage["worst_gap_degrees"]
        ),
        "tangent_coverage_is_not_kakeya_certification": True,
    }

    return {
        "designation": "CP-DNA-001",
        "status": "NUMERICS / DIAGNOSTIC",
        "direction_space": "unoriented lines (v ~ -v)",
        "parameters": {
            "radius": radius,
            "reference_rise_per_radian": reference_rise,
            "helix_samples_per_pitch": sample_count,
            "spherical_targets": target_count,
            "pitch_ratios": pitch_ratios,
        },
        "single_ideal_helix": {
            "axis_component": reference_rise
            / math.sqrt(radius * radius + reference_rise * reference_rise),
            "axis_component_spread": axial_spread,
            **single_coverage,
        },
        "fixed_axis_pitch_ensemble": ensemble_coverage,
        "checks": checks,
        "firewall": [
            "directional tangent sampling is not unit-segment containment",
            "the pitch ensemble is a parameter diagnostic, not a biological universality claim",
            "CP-DNA-001 does not certify a Kakeya set, RH, or the Coleman Conjecture",
        ],
        "pass": all(checks.values()),
    }


def main() -> int:
    report = build_report()
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

"""KakeyaLogic reference field: typed directional completeness and SAVER routing."""

from kakeyalogic.calibration import CalibrationFixture, load_fixture
from kakeyalogic.completeness import kcomplete
from kakeyalogic.containment import ContainmentVerdict, evaluate_containment
from kakeyalogic.gate import evaluate_edge, grain_and_gate
from kakeyalogic.geodecis import geodecis_report
from kakeyalogic.grains import (
    SAVER,
    Grain,
    GrainBundle,
    Outcome,
    TransitionClass,
    classify_outcomes,
)
from kakeyalogic.routing import KakeyaRouter

__all__ = [
    "SAVER",
    "CalibrationFixture",
    "ContainmentVerdict",
    "Grain",
    "GrainBundle",
    "KakeyaRouter",
    "Outcome",
    "TransitionClass",
    "classify_outcomes",
    "evaluate_containment",
    "evaluate_edge",
    "geodecis_report",
    "grain_and_gate",
    "kcomplete",
    "load_fixture",
]

__version__ = "1.0.0"

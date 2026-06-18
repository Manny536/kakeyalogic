"""Minimal iPiano inertial proximal probe for KakeyaLogic / PeAIce.

This example registers iPiano as a finite optimization probe:

    forward motion + inertial memory + proximal correction

It uses a toy nonconvex composite objective

    h(x) = f(x) + g(x)

where f is smooth and nonconvex and g is convex nonsmooth L1 pressure.

Run:
    python examples/ipiano_probe.py

This file is intentionally dependency-light: numpy only.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List

import numpy as np

Array = np.ndarray


@dataclass(frozen=True)
class IPianoState:
    iteration: int
    objective: float
    step_norm: float
    residual_norm: float
    alpha: float
    beta_ipiano: float

    def as_dict(self) -> dict:
        return {
            "iteration": self.iteration,
            "objective": self.objective,
            "step_norm": self.step_norm,
            "residual_norm": self.residual_norm,
            "alpha": self.alpha,
            "beta_ipiano": self.beta_ipiano,
        }


def soft_threshold(x: Array, lam: float) -> Array:
    """Proximal map for lam * ||x||_1."""
    return np.sign(x) * np.maximum(np.abs(x) - lam, 0.0)


def toy_f(x: Array) -> float:
    """Smooth nonconvex double-well objective."""
    return float(np.sum(0.25 * (x * x - 1.0) ** 2))


def toy_grad_f(x: Array) -> Array:
    """Gradient of toy_f."""
    return x * (x * x - 1.0)


def toy_g(x: Array, l1_weight: float) -> float:
    """Convex nonsmooth L1 pressure."""
    return float(l1_weight * np.sum(np.abs(x)))


def objective(x: Array, l1_weight: float) -> float:
    return toy_f(x) + toy_g(x, l1_weight)


def prox_g_l1(y: Array, alpha: float, l1_weight: float) -> Array:
    return soft_threshold(y, alpha * l1_weight)


def proximal_residual(
    x: Array,
    grad_f: Callable[[Array], Array],
    prox_g: Callable[[Array, float], Array],
) -> Array:
    """Residual r(x)=x-(I+partial g)^(-1)(x-grad f(x)).

    The residual is evaluated at unit step size to match the iPiano paper's
    proximal-residual convention.
    """
    return x - prox_g(x - grad_f(x), 1.0)


def ipiano(
    x0: Array,
    grad_f: Callable[[Array], Array],
    prox_g: Callable[[Array, float], Array],
    objective_fn: Callable[[Array], float],
    *,
    alpha: float = 0.05,
    beta_ipiano: float = 0.8,
    iterations: int = 250,
) -> tuple[Array, List[IPianoState]]:
    """Run the constant-parameter iPiano update.

    Update:
        x_{n+1} = prox_{alpha g}(x_n - alpha grad f(x_n)
                                 + beta(x_n - x_{n-1}))

    beta_ipiano is the optimizer inertia parameter. It is not the Kakeya scale
    ratio beta = rho/delta and not the closing pressure beta_close(T).
    """
    if not (0.0 <= beta_ipiano < 1.0):
        raise ValueError("beta_ipiano must be in [0, 1).")
    if alpha <= 0:
        raise ValueError("alpha must be positive.")

    x_prev = np.asarray(x0, dtype=float).copy()
    x = x_prev.copy()
    telemetry: List[IPianoState] = []

    for n in range(iterations):
        y = x - alpha * grad_f(x) + beta_ipiano * (x - x_prev)
        x_next = prox_g(y, alpha)

        step_norm = float(np.linalg.norm(x_next - x))
        residual = proximal_residual(x_next, grad_f, prox_g)
        residual_norm = float(np.linalg.norm(residual))

        telemetry.append(
            IPianoState(
                iteration=n + 1,
                objective=objective_fn(x_next),
                step_norm=step_norm,
                residual_norm=residual_norm,
                alpha=alpha,
                beta_ipiano=beta_ipiano,
            )
        )

        x_prev, x = x, x_next

    return x, telemetry


def main() -> None:
    rng = np.random.default_rng(42)
    l1_weight = 0.05
    x0 = rng.normal(size=16)

    prox = lambda y, alpha: prox_g_l1(y, alpha, l1_weight)
    obj = lambda x: objective(x, l1_weight)

    x_star, trace = ipiano(
        x0,
        toy_grad_f,
        prox,
        obj,
        alpha=0.05,
        beta_ipiano=0.8,
        iterations=250,
    )

    first = trace[0]
    last = trace[-1]

    print("iPiano probe complete")
    print(f"dimension: {x_star.size}")
    print(f"first objective: {first.objective:.8f}")
    print(f"last objective:  {last.objective:.8f}")
    print(f"last step norm: {last.step_norm:.8e}")
    print(f"last residual:  {last.residual_norm:.8e}")
    print(f"beta_iPiano:    {last.beta_ipiano:.3f}")


if __name__ == "__main__":
    main()

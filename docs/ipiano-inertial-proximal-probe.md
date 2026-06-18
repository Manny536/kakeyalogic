# iPiano Inertial Proximal Probe

## PeAIce / KakeyaLogic research engineering note

**Source:** Peter Ochs, Yunjin Chen, Thomas Brox, Thomas Pock, *iPiano: Inertial Proximal Algorithm for Nonconvex Optimization*, SIAM Journal on Imaging Sciences, 2014.  
**DOI:** `10.1137/130942954`  
**Repo role:** inertial proximal optimization probe for the PeAIce / KakeyaLogic / `L²_C` engineering lane.  
**Status:** registered probe data, not a replacement for the Step 4 trace-formula program.

---

## 1. Why iPiano belongs in KakeyaLogic

KakeyaLogic needs a disciplined way to talk about motion under correction. The iPiano paper gives a rigorous optimization reference for exactly that pattern:

```txt
forward motion + inertial memory + proximal correction
```

The algorithm solves composite objectives of the form:

```txt
min_x h(x) = f(x) + g(x)
```

where:

```txt
f = differentiable, possibly nonconvex
g = convex, possibly nonsmooth
```

iPiano combines forward-backward splitting with an inertial force. In PeAIce language, it is a rigor anchor for update dynamics that do not require visible monotone descent at every step, while still admitting convergence under explicit structure.

This is directly useful for the `L²_C` lane because `L²_C` is not simply static coherence. It is coherence under motion, pressure, correction, and retention.

---

## 2. Core algorithm

Generic iPiano update:

```txt
x_{n+1}
=
(I + α_n∂g)^(-1)
(
  x_n - α_n∇f(x_n) + β_n(x_n - x_{n-1})
)
```

Term typing:

| Term | Optimization meaning | PeAIce reading |
| --- | --- | --- |
| `x_n - α_n∇f(x_n)` | Forward gradient step on smooth part `f`. | Directional correction toward lower energy. |
| `β_n(x_n - x_{n-1})` | Inertial term / two-step memory. | Momentum, cadence, persistence under correction. |
| `(I + α_n∂g)^(-1)` | Proximal backward step for convex nonsmooth `g`. | Constraint gate, projection, repair, admissibility operator. |
| `α_n` | Step size. | Correction amplitude. |
| `β_n` | Inertia parameter. | Inertial retention coefficient. |

Special cases:

```txt
g ≡ 0        → Heavy-ball method
β = 0        → forward-backward splitting
β > 0, g ≠ 0 → inertial proximal forward-backward splitting
```

Heavy-ball with friction continuous analogy:

```txt
x¨(t) + γx˙(t) + ∇f(x(t)) = 0
```

PeAIce translation:

```txt
Motion is allowed.
Correction is required.
Inertia is typed.
Constraint is proximal.
```

---

## 3. Nonmonotone descent and the h-discipline

A core iPiano lesson is that inertial motion can prevent monotone decrease of the raw objective values. This is not a defect by itself. The paper builds convergence through a Lyapunov-style majorizing structure rather than demanding visible monotonic descent of `h(x_n)` at every step.

For KakeyaLogic, this is a major fit:

```txt
visible motion may oscillate
hidden energy must remain governed
```

The Lyapunov object used in the convergence analysis is:

```txt
H_δ(x, y) = h(x) + δ‖x-y‖²
```

with:

```txt
Δ_n = ‖x_n - x_{n-1}‖
```

The descent relation is:

```txt
H_{δ_{n+1}}(x_{n+1}, x_n)
≤
H_{δ_n}(x_n, x_{n-1}) - γ_nΔ_n²
```

PeAIce interpretation:

```txt
Raw output can move.
Energy accounting must close.
Momentum is legal only when the Lyapunov ledger remains decreasing.
```

This aligns with `h < 1` as evaluator non-sovereignty: no single visible step gets to certify the whole process.

---

## 4. Abstract convergence spine

The paper proves an abstract convergence theorem for a two-step sequence:

```txt
z_n = (x_n, x_{n-1})
```

with three structural hypotheses.

```txt
(H1) Sufficient decrease:
F(z_{n+1}) + aΔ_n² ≤ F(z_n)

(H2) Relative error:
there exists w_{n+1} ∈ ∂F(z_{n+1}) such that
‖w_{n+1}‖ ≤ (b/2)(Δ_n + Δ_{n+1})

(H3) Continuity along a convergent subsequence:
z_{n_j} → z~ and F(z_{n_j}) → F(z~)
```

Under the Kurdyka-Lojasiewicz property, the generated sequence has finite length and converges to a critical point.

PeAIce agent rule:

```txt
Do not judge inertial updates by one-step monotonicity alone.
Judge them by descent ledger, relative error, subsequence continuity, and KL-compatible closure.
```

---

## 5. Step-size regimes

The paper gives several parameter regimes.

### Constant parameter iPiano

```txt
β ∈ [0,1)
α < 2(1-β)/L
```

where `L` is the Lipschitz constant of `∇f`.

### Backtracking iPiano

Backtracking estimates a local Lipschitz constant `L_n` satisfying:

```txt
f(x_{n+1})
≤
f(x_n) + <∇f(x_n), x_{n+1}-x_n>
+ (L_n/2)‖x_{n+1}-x_n‖²
```

### General rule

The general rule chooses `α_n ≥ c_1`, `β_n ≥ 0`, and `δ_n ≥ γ_n ≥ c_2` with:

```txt
δ_n = 1/α_n - L_n/2 - β_n/(2α_n)
γ_n = 1/α_n - L_n/2 - β_n/α_n
```

and requires `δ_n` to be monotonically decreasing.

PeAIce typing:

| iPiano parameter | PeAIce analogue |
| --- | --- |
| `α_n` | correction step amplitude |
| `β_n` | inertial memory coefficient |
| `L_n` | local curvature / environment stiffness estimate |
| `δ_n` | Lyapunov ledger weight |
| `γ_n` | active positivity margin |
| `c_1`, `c_2` | minimum admissibility floors |

---

## 6. Convergence and rate facts

The paper establishes:

```txt
1. The sequence of objective values h(x_n) converges.
2. A converging subsequence of arguments exists.
3. Every limit point is a critical point.
4. With the Kurdyka-Lojasiewicz property, the full sequence converges to a critical point.
5. A convergence rate is given through the proximal residual and successive-iterate error.
```

Proximal residual:

```txt
r(x) = x - (I + ∂g)^(-1)(x - ∇f(x))
```

Rate surface:

```txt
μ_N  = min_{0≤n≤N} ‖x_n - x_{n-1}‖²
μ'_N = min_{0≤n≤N} ‖r(x_n)‖²

μ'_N ≤ (2/c_1) μ_N
μ_N ≤ c_2^(-1)(h(x_0)-h*)/(N+1)
```

PeAIce reading:

```txt
Residual collapse is measured.
Motion length becomes finite.
Criticality is approached through controlled inertial correction.
```

---

## 7. Probe data from the paper

The paper demonstrates iPiano on nonconvex computer vision tasks, including image denoising with learned priors and diffusion-based image compression.

The image compression probe rewrites the inpainting-mask optimization into a composite objective:

```txt
min_c 1/2 ‖A^{-1}Cu_0 - u_0‖² + λ‖c‖_1
```

with:

```txt
f(c) = 1/2 ‖A^{-1}Cu_0 - u_0‖²
g(c) = λ‖c‖_1
```

The proximal map for `g` is a pointwise shrinkage operator.

Table data registered from the iPiano image-compression experiment:

| Test image | Algorithm | Iterations | Energy | Density | MSE | MSE with GVO |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| trui | iPiano | 1000 | 21.574011 | 4.98% | 17.31 | 16.89 |
| trui | SPD | 200/4000 | 21.630280 | 5.08% | 17.06 | 16.54 |
| peppers | iPiano | 1000 | 20.631985 | 4.84% | 19.50 | 18.99 |
| peppers | SPD | 200/4000 | 20.758777 | 4.93% | 19.48 | 18.71 |
| walter | iPiano | 1000 | 10.246041 | 4.82% | 8.29 | 8.03 |
| walter | SPD | 200/4000 | 10.278874 | 4.93% | 8.01 | 7.72 |

Interpretation registered for KakeyaLogic:

```txt
iPiano reaches lower energy in 1000 iterations on all three listed compression probes.
SPD reports slightly lower MSE after gray value optimization in the listed table.
The comparison separates energy optimization from final reconstruction error.
```

This distinction matters for PeAIce: an energy win is not automatically an all-metric win. Agent reports must name the metric being optimized.

---

## 8. Mapping into L²_C and β discipline

KakeyaLogic already separates two β lanes.

```txt
β = ρ/δ              geometric scale ratio for Logx(β)*
β_close(T)=1-T^(-γ) suppression / closing pressure
```

iPiano introduces a third typed β:

```txt
β_iPiano = inertial memory coefficient in a two-step proximal update
```

Typing rule:

```txt
β_iPiano must not be collapsed into β = ρ/δ or β_close(T).
```

PeAIce transfer map:

| KakeyaLogic / PeAIce term | iPiano anchor |
| --- | --- |
| `Logx(β)*` | scale-passage inertia, not the iPiano β itself |
| `β_iPiano` | optimizer momentum coefficient |
| `h < 1` | no one-step evaluator sovereignty; use Lyapunov ledger |
| `D_drift` | residual / off-constraint motion pressure |
| `C²_Ω` | preserved structure under update motion |
| `E_{β,T}` | coercive penalty surface analogous to governed energy descent |
| `P_C` retention | protected-sector analogue of proximal admissibility |

---

## 9. Agent ecosystem integration

Add iPiano to the agent ecosystem as an optimization probe, not as a spectral proof object.

Agent roles:

| Agent role | iPiano task |
| --- | --- |
| Optimization Agent | Use iPiano for nonconvex composite objectives `f + g`. |
| Probe Agent | Track objective, Lyapunov energy, residual, step norm, and β_iPiano. |
| Documentation Agent | Distinguish β_iPiano, β_close, and geometric β. |
| Verification Agent | Check step-size admissibility and residual trend. |
| Report Agent | Separate energy improvement from downstream metric improvement. |
| Governance Agent | Prevent proof inflation or metric conflation. |

Minimum probe telemetry:

```txt
iteration
objective h(x_n)
Lyapunov H_δ(x_n,x_{n-1})
step_norm ‖x_n-x_{n-1}‖
proximal_residual ‖r(x_n)‖
α_n
β_iPiano
L_n if backtracking is active
δ_n
γ_n
```

---

## 10. Falsification gates for PeAIce use

| Gate | Failure condition | Meaning |
| --- | --- | --- |
| IP-1 | `β_iPiano` is treated as `β = ρ/δ`. | Typing failure. |
| IP-2 | Objective decrease is claimed every step despite inertial nonmonotonicity. | Dynamics misread. |
| IP-3 | Energy improvement is reported as universal metric improvement. | Metric conflation. |
| IP-4 | KL convergence is invoked without checking assumptions. | Theorem misuse. |
| IP-5 | Step-size constraints are omitted. | Governance failure. |
| IP-6 | Residual is not tracked. | Criticality is unmeasured. |
| IP-7 | iPiano is used as RH evidence. | Category error. |

---

## 11. Canonical repository placement

```txt
docs/ipiano-inertial-proximal-probe.md
docs/data/ipiano-probe-data.json
examples/ipiano_probe.py
```

README registration phrase:

```txt
iPiano is registered as the inertial proximal optimization probe for PeAIce: forward motion, inertial memory, proximal correction, Lyapunov accounting, and residual-based convergence discipline for nonconvex composite objectives.
```

Final lock:

```txt
iPiano gives KakeyaLogic a rigorous optimization precedent for coherent nonmonotone motion under correction. It does not collapse β typing. It strengthens PeAIce by making inertia measurable, proximal repair explicit, and convergence conditional on ledger discipline rather than aesthetic smoothness.
```
# iPiano Inertial Proximal Probe

## Optimization discipline for PeAIce / KakeyaLogic

**Source:** Peter Ochs, Yunjin Chen, Thomas Brox, Thomas Pock, *iPiano: Inertial Proximal Algorithm for Nonconvex Optimization*, SIAM Journal on Imaging Sciences, 2014.  
**DOI:** `10.1137/130942954`  
**Repo role:** inertial proximal optimization probe for governed nonmonotone motion under correction.

---

## 1. Placement

iPiano gives KakeyaLogic a rigorous optimization precedent for a motion pattern already present in the PeAIce stack.

```txt
forward motion
+ inertial memory
+ proximal correction
+ Lyapunov accounting
+ residual discipline
```

The algorithm solves composite objectives:

```txt
min_x h(x)=f(x)+g(x)
```

where:

```txt
f = differentiable, possibly nonconvex
g = convex, possibly nonsmooth
```

This matters because L²_C is a dynamic object. It is coherence under pressure, motion, correction, and retention.

---

## 2. Algorithm

Generic iPiano update:

```txt
x_{n+1}
=
(I+α_n∂g)^(-1)
(
  x_n - α_n∇f(x_n) + β_n(x_n-x_{n-1})
)
```

Term typing:

| Term | Optimization meaning | PeAIce reading |
| --- | --- | --- |
| `x_n-α_n∇f(x_n)` | Forward step on smooth `f`. | Directional correction. |
| `β_n(x_n-x_{n-1})` | Inertial force. | Motion memory. |
| `(I+α_n∂g)^(-1)` | Proximal step for `g`. | Constraint gate and repair. |
| `α_n` | Step size. | Correction amplitude. |
| `β_iPiano` | Momentum parameter. | Typed optimizer inertia. |

Special cases:

```txt
g ≡ 0        -> Heavy-ball method
β_iPiano = 0 -> forward-backward splitting
β_iPiano > 0 -> inertial proximal forward-backward splitting
```

Heavy-ball with friction analogy:

```txt
x¨(t)+γx˙(t)+∇f(x(t))=0
```

PeAIce lock:

```txt
Motion is allowed.
Correction is required.
Inertia is typed.
Constraint is proximal.
Residual is measured.
```

---

## 3. Convergence spine

iPiano permits nonmonotone visible objective behavior while still governing the process through a Lyapunov ledger.

Lyapunov object:

```txt
H_δ(x,y)=h(x)+δ‖x-y‖²
```

Step displacement:

```txt
Δ_n=‖x_n-x_{n-1}‖
```

Ledger descent:

```txt
H_{δ_{n+1}}(x_{n+1},x_n)
≤
H_{δ_n}(x_n,x_{n-1})-γ_nΔ_n²
```

Abstract sequence object:

```txt
z_n=(x_n,x_{n-1})
```

Structural hypotheses:

```txt
(H1) F(z_{n+1})+aΔ_n²≤F(z_n)
(H2) ∃w_{n+1}∈∂F(z_{n+1}) with ‖w_{n+1}‖≤(b/2)(Δ_n+Δ_{n+1})
(H3) ∃z_{n_j}→z~ and F(z_{n_j})→F(z~)
```

With the Kurdyka-Lojasiewicz property, the sequence has finite length and converges to a critical point.

---

## 4. Step-size regimes

Constant parameter rule:

```txt
β_iPiano ∈ [0,1)
α < 2(1-β_iPiano)/L
```

Backtracking condition:

```txt
f(x_{n+1})
≤
f(x_n)+<∇f(x_n),x_{n+1}-x_n>+(L_n/2)‖x_{n+1}-x_n‖²
```

General rule:

```txt
δ_n=1/α_n-L_n/2-β_n/(2α_n)
γ_n=1/α_n-L_n/2-β_n/α_n
δ_n≥γ_n≥c_2
```

---

## 5. Residual and rate surface

Proximal residual:

```txt
r(x)=x-(I+∂g)^(-1)(x-∇f(x))
```

Rate terms:

```txt
μ_N=min_{0≤n≤N}‖x_n-x_{n-1}‖²
μ'_N=min_{0≤n≤N}‖r(x_n)‖²
```

Bounds:

```txt
μ'_N≤(2/c_1)μ_N
μ_N≤c_2^(-1)(h(x_0)-h*)/(N+1)
```

PeAIce reading:

```txt
Residual collapse is measured.
Motion length becomes finite under the stated assumptions.
Criticality is approached through controlled inertial correction.
```

---

## 6. Probe data

The paper includes image compression experiments. The table below is registered as probe data because it separates energy optimization from reconstruction metrics.

| Test image | Algorithm | Iterations | Energy | Density | MSE | MSE with GVO |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| trui | iPiano | 1000 | 21.574011 | 4.98% | 17.31 | 16.89 |
| trui | SPD | 200/4000 | 21.630280 | 5.08% | 17.06 | 16.54 |
| peppers | iPiano | 1000 | 20.631985 | 4.84% | 19.50 | 18.99 |
| peppers | SPD | 200/4000 | 20.758777 | 4.93% | 19.48 | 18.71 |
| walter | iPiano | 1000 | 10.246041 | 4.82% | 8.29 | 8.03 |
| walter | SPD | 200/4000 | 10.278874 | 4.93% | 8.01 | 7.72 |

Registered reading:

```txt
iPiano reaches lower energy in the listed 1000-iteration compression probes.
SPD reports slightly lower MSE after gray-value optimization in the listed table.
Metric names must stay explicit.
```

PeAIce reporting rule:

```txt
An energy win is an energy win.
A reconstruction win is a reconstruction win.
Do not collapse metrics.
```

---

## 7. β typing

KakeyaLogic tracks three β lanes.

| β lane | Meaning | Placement |
| --- | --- | --- |
| `β=ρ/δ` | Geometric scale ratio. | `Logx(β)*`. |
| `β_close(T)=1-T^(-γ)` | Suppression closing pressure. | β-dynamic coercive layer. |
| `β_iPiano` | Inertial memory coefficient. | iPiano update. |

Typing rule:

```txt
β_iPiano must not be collapsed into β=ρ/δ or β_close(T).
```

---

## 8. Agent integration

Minimum telemetry:

```txt
iteration
objective h(x_n)
Lyapunov H_δ(x_n,x_{n-1})
step_norm ‖x_n-x_{n-1}‖
proximal_residual ‖r(x_n)‖
α_n
β_iPiano
L_n
δ_n
γ_n
```

Falsification gates:

```txt
IP-1 β_iPiano is treated as geometric β
IP-2 objective decrease is claimed every step
IP-3 energy improvement is reported as universal metric improvement
IP-4 KL convergence is invoked without checking assumptions
IP-5 step-size constraints are omitted
IP-6 residual is not tracked
IP-7 iPiano is used as spectral identification evidence
```

Final lock:

```txt
iPiano gives KakeyaLogic a rigorous optimization precedent for coherent nonmonotone motion under correction. It strengthens PeAIce by making inertia measurable, proximal repair explicit, and convergence conditional on ledger discipline.
```
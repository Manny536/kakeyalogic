# L² Spectral Operator — Φ Quadratic Lattice

**Repo:** KakeyaLogic — Excellence Engine v3  
**Companion:** `docs/step4-operator-program.md`, `docs/spectral-equivalence-target.md`, `docs/thermal-coupling-correction.md`  
**Status:** 🟡 formal candidate operator · 🟢 L2-1 coupling gate corrected · 🔴 spectral identification open · ⛔ K_σ determinant realization CLOSED (V6.4.3 — order/genus/density)  
**Core:** L² extracted from Φ's `n²` arithmetic, then coupled to the Kakeya/Fourier spectral program through a thermal-measure-aware kernel

---

> **V6.4.3 DOWNSTREAM CLOSURE NOTE — propagated 25 June 2026.**
> The `|m^2 - n^2|^{-sigma}` `K_sigma` realization of the Step-4 determinant target is **`CLOSED-NEGATIVE`**.
> `det_zeta(L^2_{Phi,K} - (z^2 + 1/4)) = C * Xi(z)` cannot hold for the `D_1^2 + gamma_K K_sigma` operator:
> `gamma_K K_sigma` is relatively compact w.r.t. `D_1^2` (`K_sigma in S_2` for `sigma > 1/2`), so by
> Weyl-class invariance the counting stays `N(Lambda) ~ Lambda^{1/4}` and never reaches Riemann-von Mangoldt
> `sqrt(Lambda) log Lambda` (**counting**); below `sigma*` the `det_2` order exceeds 1 (**order**); above `sigma*`
> the determinant is genus 0 vs genus-1 Xi (**genus**); at `sigma*` the power-law spectrum gives linear
> zero-density, not `T log T` (**density**).
> The finite-window crossing `sigma*_N ~ 0.83-0.92` is demoted; the analytic Weyl boundary is `sigma_c = 1`
> (`s_n(K_sigma) ~ n^{-sigma}` to leading order).
> **Canonical:** `docs/peaice-ddatl-001.md` Section 7.1 and `docs/ddatl-v6-4-3-grounding-citations.md`.
> **Any determinant-identity, eigenvalue-bijection, or "load-bearing OPEN" claim below that reads as live for
> the square-difference kernel is superseded by this note.** The DDATL host object stays `FORMAL`; the gap is
> relocated to a prime-carrying length/weight operator (`docs/prime-carrying-trace-architecture.md`) and the
> Nyman-Beurling / Baez-Duarte distance program.
> RH `OPEN` · Coleman Conjecture `OPEN` · no proof claimed.

---


## 0. Purpose

This document gives an explicit spectral definition of the L² operator matching the quadratic lattice inside the Riemann Φ-kernel.

The goal is to move Step 4 from a general spectral-equivalence target into a concrete theorem-bearing object:

```txt
Φ arithmetic → L² operator → regulated coupling → spectral determinant → Ξ(z) → zeta-zero ordinates
```

The load-bearing target remains spectral identification with the nontrivial zeta zeros.

This revision incorporates the L2-1 correction from `docs/thermal-coupling-correction.md`: the naive coupling `K_σ(m,n)=|m²-n²|^{-σ}` is not symmetric or bounded on the weighted thermal space `H_Φ(u)`. The corrected coupling is `K_σ^{reg}`, which respects the native thermal measure.

---

## 1. Φ Data and the Quadratic Lattice

Use the standard Φ-kernel structure:

```txt
Φ(u) = Σ_{n≥1} (2π² n⁴ e^{9u} - 3π n² e^{5u}) e^{-π n² e^{4u}}
```

The active arithmetic lattice is:

```txt
Λ_{n²} = { n² : n ∈ N, n ≥ 1 }
```

The exponential factor supplies the natural heat weight:

```txt
w_n(u) = exp(-π n² e^{4u})
```

Define the Φ-induced Hilbert space:

```txt
H_Φ(u) = ℓ²(N, w_u)
```

with inner product:

```txt
<a,b>_u = Σ_{n≥1} a_n overline(b_n) w_n(u)
```

The finite-support vectors form the dense test domain:

```txt
D_0 = c_{00}(N) ⊂ H_Φ(u)
```

Interpretation:

```txt
H_Φ(u) is not external to Φ.
It is the Hilbert space induced by Φ's own n²-localized Gaussian lattice.
```

Native-measure rule:

```txt
Every operator coupling must respect its native measure.
```

For `H_Φ(u)`, the native measure is the thermal weight `w_u`.

---

## 2. First Dynamic: Quadratic Lattice Operator

Let `{e_n}` be the canonical basis of `H_Φ(u)`.

Define:

```txt
D₁ e_n = n² e_n
```

with maximal domain:

```txt
D(D₁) = { a ∈ H_Φ(u) : Σ n⁴ |a_n|² w_n(u) < ∞ }
```

Then:

```txt
Spec(D₁) = { 1, 4, 9, 16, ... }
```

This is the first dynamic:

```txt
D₁ = multiplication by the quadratic lattice Λ_{n²}
```

---

## 3. Uncoupled L² Operator

The Φ coefficient contains two arithmetic terms:

```txt
n⁴ = (n²)²
n²
```

Define the uncoupled L² operator:

```txt
L²_0(u) = D₁² - a(u)D₁
```

where:

```txt
a(u) = (3 / 2π)e^{-4u}
```

Its domain is:

```txt
D(L²_0) = { a ∈ H_Φ(u) : Σ n⁸ |a_n|² w_n(u) < ∞ }
```

Acting on basis vectors:

```txt
L²_0(u)e_n = λ_n^(0)(u)e_n
```

with eigenvalues:

```txt
λ_n^(0)(u) = n⁴ - (3 / 2π)e^{-4u}n²
```

The Φ coefficient is recovered by scaling this operator:

```txt
2π²e^{9u} L²_0(u)e_n
= (2π²n⁴e^{9u} - 3πn²e^{5u})e_n
```

Therefore:

```txt
Φ(u) = 2π²e^{9u} Σ_{n≥1} λ_n^(0)(u) w_n(u)
```

or, in weighted diagonal trace notation:

```txt
Φ(u) = Tr_{w_u}(2π²e^{9u}L²_0(u))
```

This is the key extraction:

```txt
L² is read out of Φ.
It is not appended from outside the arithmetic.
```

---

## 4. Regulated Kakeya/Fourier Coupling Kernel

The diagonal operator captures Φ's local arithmetic, but Step 4 also needs directional interaction.

The prior naive kernel:

```txt
K_σ(m,n) = |m²-n²|^{-σ}
```

is symmetric as an unweighted matrix but is not symmetric or bounded on the weighted space `H_Φ(u)=ℓ²(N,w_u)`. The corrected coupling must include the thermal Jacobian of the space.

Define the thermally regulated coupling:

```txt
K_σ^{reg}(m,n) = 0                                    if m=n
K_σ^{reg}(m,n) = |m²-n²|^{-σ} (w_m(u)/w_n(u))^{1/2}  if m≠n
```

Equivalently:

```txt
K_σ^{reg}(m,n)
=
|m²-n²|^{-σ} exp(-π(m²-n²)e^{4u}/2)
```

with working threshold:

```txt
σ > 1/2
```

Formal status:

```txt
K_σ^{reg} is symmetric on H_Φ(u).
K_σ^{reg} is Hilbert-Schmidt on H_Φ(u) for σ > 1/2.
Hilbert-Schmidt implies bounded.
```

For real coupling strength `γ_K`, define the corrected operator:

```txt
L²_{Φ,K}^{reg}(u)
=
D₁² - (3 / 2π)e^{-4u}D₁ + γ_K K_σ^{reg}
```

on domain:

```txt
D(L²_{Φ,K}^{reg}) = D(L²_0)
```

Because `K_σ^{reg}` is bounded and symmetric on `H_Φ(u)`, `L²_{Φ,K}^{reg}` is the corrected Step 4 operator candidate by bounded symmetric perturbation of the self-adjoint multiplication operator `L²_0`, with the final Kato-Rellich domain estimate tracked in `docs/thermal-coupling-correction.md`.

This gives the explicit corrected Step 4 candidate:

```txt
L²_{Φ,K}^{reg}(u) = L²_0(u) + γ_K K_σ^{reg}
```

Interpretation:

```txt
L²_0 = exact Φ arithmetic
K_σ^{reg} = thermal-measure-aware Kakeya/Fourier directional interaction
γ_K = coupling pressure between arithmetic lattice and directional geometry
```

The unweighted power-law kernel is still the natural kernel in the canonical `ℓ²(N)` picture. The thermal factor appears when translating that kernel back into `H_Φ(u)`.

---

## 5. Eigenvalue Problem

The corrected spectral equation is:

```txt
L²_{Φ,K}^{reg}(u)ψ_j = λ_jψ_j
```

Expanded in coordinates:

```txt
(n⁴ - (3 / 2π)e^{-4u}n²)ψ_j(n)
+
γ_K Σ_{m≠n}
|m²-n²|^{-σ}(w_m(u)/w_n(u))^{1/2} ψ_j(m)
=
λ_jψ_j(n)
```

The uncoupled spectrum is:

```txt
λ_n^(0)(u) = n⁴ - (3 / 2π)e^{-4u}n²
```

The coupled spectrum is the Step 4 object:

```txt
Spec(L²_{Φ,K}^{reg}) = { λ_j }
```

Under the canonical isometry:

```txt
V : H_Φ(u) → ℓ²(N),   (Va)_n = a_n √w_n(u),
```

`L²_{Φ,K}^{reg}` becomes:

```txt
Ã(u) = diag(n⁴ - (3/2π)e^{-4u}n²) + γ_K |m²-n²|^{-σ}
```

in the unweighted `ℓ²(N)` picture.

---

## 6. Spectral Identification Target

Let the completed Xi function be written as an even function of `z`:

```txt
Ξ(z) = ξ(1/2 + iz)
```

The desired spectral identification is:

```txt
λ_j ↔ γ_j² + 1/4
```

where:

```txt
ξ(1/2+iγ_j)=0
```

Thus the Step 4 theorem target becomes:

```txt
Spec(L²_{Φ,K}^{reg}) = { γ_j² + 1/4 }
```

with multiplicity.

Equivalent determinant form:

```txt
det_ζ(L²_{Φ,K}^{reg} - (z² + 1/4)) = C · Ξ(z)
```

for some nonzero constant `C`, after the determinant is rigorously defined.

This determinant identity is the load-bearing bridge.

The thermal correction does not prove this identity. It only repairs the operator so the spectral question becomes well-posed.

---

## 7. Step 4 Closure Sequence

### 7.1 Domain and self-adjointness

Prove:

```txt
D(L²_0) is dense in H_Φ(u)
L²_0 is self-adjoint
K_σ^{reg} is symmetric on H_Φ(u)
K_σ^{reg} is Hilbert-Schmidt for σ > 1/2
L²_{Φ,K}^{reg} is self-adjoint on D(L²_0)
```

Current status:

```txt
D(L²_0) dense: FORMAL
L²_0 self-adjoint: FORMAL
K_σ^{reg} symmetric: FORMAL
K_σ^{reg} Hilbert-Schmidt: FORMAL for σ > 1/2
K_σ^{reg} bounded: FORMAL
L²_{Φ,K}^{reg} self-adjoint: PROPOSED by Kato-Rellich, final domain estimate pending
```

### 7.2 Trace-class regularization

Show that the resolvent difference is trace class:

```txt
(L²_{Φ,K}^{reg}+I)^{-1} - (L²_0+I)^{-1} ∈ S₁
```

This permits a regularized determinant.

### 7.3 Determinant construction

Define:

```txt
Z_L(z) = det_ζ(L²_{Φ,K}^{reg} - (z² + 1/4))
```

and prove that `Z_L(z)` is entire or has the exact meromorphic structure required to match `Ξ(z)`.

### 7.4 Heat/Φ kernel equivalence

Prove that the heat trace or weighted trace generated by `L²_{Φ,K}^{reg}` recovers the Φ-kernel contribution:

```txt
Tr_{reg}(e^{-tL²_{Φ,K}^{reg}}) ↔ ∫ e^{tu²}Φ(u)e^{izu}du
```

This is the analytic continuation bridge.

### 7.5 Counting law

Show that the spectral counting function:

```txt
N_L(T) = #{ λ_j : 0 < sqrt(λ_j - 1/4) ≤ T }
```

matches the Riemann-von Mangoldt asymptotic:

```txt
N_ξ(T) = T/(2π)log(T/(2π)) - T/(2π) + O(log T)
```

Counting is necessary but not sufficient.

### 7.6 Explicit formula compatibility

Prove the trace relation:

```txt
Tr φ(L²_{Φ,K}^{reg}) ↔ Σ_ρ φ(Im ρ) ↔ prime-side explicit formula
```

This is where the operator must pass from geometric/lattice structure into arithmetic equivalence.

### 7.7 β/h suppression compatibility

After spectral identification, the β/h layer acts on the off-critical complement:

```txt
ρ_off(T,σ) ≤ exp(-(β(T)-hη)T|σ-1/2|²)
```

with active positivity condition:

```txt
β(T)-hη > 0
```

The required compatibility is:

```txt
ker(X) = Ran(Π_sym) = critical-line spectral sector
```

---

## 8. Formal Theorem Statement

### Theorem Target L2-SI

Construct `H_Φ(u)`, `D(L²_{Φ,K}^{reg})`, and:

```txt
L²_{Φ,K}^{reg}(u)
=
D₁² - (3 / 2π)e^{-4u}D₁ + γ_K K_σ^{reg}
```

such that:

```txt
L²_{Φ,K}^{reg} = (L²_{Φ,K}^{reg})^*
```

and:

```txt
det_ζ(L²_{Φ,K}^{reg} - (z² + 1/4)) = C · Ξ(z)
```

Then:

```txt
Spec(L²_{Φ,K}^{reg}) = { γ_j² + 1/4 : ξ(1/2+iγ_j)=0 }
```

and the Step 4 spectral ID is closed.

---

## 9. Falsification Conditions

This L² spectral route fails if any load-bearing condition breaks:

```txt
L2-1. [RESOLVED] The naive K_σ fails on H_Φ(u), but K_σ^{reg} is symmetric and Hilbert-Schmidt for σ > 1/2.
L2-1a. The corrected coupling K_σ^{reg} does not preserve or enable the spectral identification property.
L2-2. L²_{Φ,K}^{reg} has the wrong spectral type.
L2-3. The determinant cannot be defined in a compatible way.
L2-4. The heat/Φ trace relation fails.
L2-5. Counting does not match Riemann-von Mangoldt.
L2-6. The explicit formula cannot be recovered.
L2-7. The spectrum cannot be identified with ξ-zero ordinates.
L2-8. β/h suppression acts on a sector different from the spectral-equivalence sector.
```

L2-1 is now a correction record, not the active blocker. L2-1a becomes the active spectral compatibility gate.

---

## 10. Downstream L²_C Interpretation

The thermal correction matches the saturated direction update in `docs/step4-operator-program.md`.

```txt
saturated direction → scale aware tube
spectral coupling → weight aware kernel
Logx(β)* → inertia term preserving admissibility across scale
```

The native-measure rule is common to both lanes:

```txt
A raw object becomes valid only after it is expressed in the geometry of its own space.
```

For Kakeya direction geometry, the native measure is directional saturation across rays, tubes, shadings, non clustering, and scale.

For `L²_{Φ,K}^{reg}`, the native measure is the thermal weight:

```txt
w_n(u)=exp(-πn²e^{4u}).
```

Canonical downstream chain:

```txt
Bateman direction tree
→ saturated direction
→ δ-tube packet
→ Sparse^Grain
→ Logx(β)*
→ L²_C
→ K_σ^{reg}
→ L²_{Φ,K}^{reg}
```

---

## 11. Status Return

```txt
Object: L²_{Φ,K}^{reg}
Ground space: H_Φ(u)=ℓ²(N, e^{-πn²e^{4u}})
Base lattice: Λ_{n²}
First dynamic: D₁e_n=n²e_n
Uncoupled L²: D₁²-(3/2π)e^{-4u}D₁
Kakeya coupling: γ_KK_σ^{reg}
Correction: K_σ → K_σ^{reg}=|m²-n²|^{-σ}(w_m/w_n)^{1/2}
Working threshold: σ > 1/2
Symmetry: FORMAL
Hilbert-Schmidt: FORMAL
Boundedness: FORMAL
Self-adjointness: PROPOSED
Eigenvalue target: λ_j=γ_j²+1/4
Load-bearing theorem: det_ζ(L²_{Φ,K}^{reg}-(z²+1/4)) = CΞ(z)
L2-1 gate: RESOLVED by thermal correction
L2-1a gate: OPEN spectral identification compatibility
Step 4: spectral ID target sharpened
State: active:🟢 / developing:🟡 / spectral ID:🔴
```

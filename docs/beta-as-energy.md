# β as Energy — EEV3 Step 4

**Notation correction (2026-09-24):** a_C is an analytic correction weight, distinct from evaluator h_eval and Hamiltonian leakage ℓ_H. Identifying a_C with ℓ_H requires an additional normalized model; it is not established here. Existing analytic claims are not re-proved by this notation migration. See [notation custody](h-notation.md).

**Repo:** KakeyaLogic — Excellence Engine v3  
**Companion:** `docs/beta-dynamic.md`, `docs/operator-domain.md`  
**Status:** 🟡 theorem target · 🟢 energy formalization active  
**Core:** E = L² · β > 0 · h_eval < 1

## 0. Purpose

This document gives the β-dynamic a precise mathematical role:

```txt
β is an energy coefficient on off-critical defect.
```

It is not merely a scalar rescaling of an operator. It is not a rhetorical momentum term. In the Step 4 program, β is the coefficient that makes off-axis leakage energetically expensive.

---

## 1. Defect Energy

Let `X = X*` be the critical-line defect observable.

The defect energy is:

```txt
E_def(f) = ||Xf||²
```

At height scale `T`, define:

```txt
E_def,T(f) = T||Xf||²
```

Then β-energy is:

```txt
E_β,T(f) = β(T)T||Xf||²
```

where:

```txt
β(T) = 1 - T^(-γ)
```

---

## 2. a_C-Corrected Energy

Let `C` be a_C-correction with relative form bound:

```txt
|⟨Cf,f⟩| ≤ η||Xf||² + b||f||²
```

The a_C-corrected β energy is:

```txt
E_β,a_C,T(f)
= β(T)T||Xf||² + a_C⟨Cf,f⟩
```

Lower bound:

```txt
E_β,a_C,T(f)
≥ (β(T)-a_C η)T||Xf||² - a_C b||f||²
```

The gap is:

```txt
δ_{β,C}(T) = β(T)-a_C η
```

This is the active energy gap of EEV3 Step 4.

---

## 3. Off-Axis Projection Bound

For off-axis sector `P_σ`, assume:

```txt
P_σX²P_σ ≥ |σ - 1/2|²P_σ
```

Then for `f ∈ Ran(P_σ)`:

```txt
E_β,a_C,T(f)
≥ δ_{β,C}(T)T|σ - 1/2|²||f||² - a_C b||f||²
```

After floor renormalization:

```txt
E_β,a_C,T(f)
≥ δ_{β,C}(T)T|σ - 1/2|²||f||²
```

provided:

```txt
δ_{β,C}(T) > 0
```

---

## 4. Suppression Estimate

If `A_{β,a_C,T}` is the self-adjoint operator associated to the closed lower-semibounded form, then the off-axis semigroup obeys:

```txt
||P_σ exp(-A_{β,a_C,T})P_σ||
≤ exp(-δ_{β,C}(T)T|σ - 1/2|²)
```

This gives the refined EEV3 suppression target:

```txt
ρ_off(T,σ)
≤ exp(-(β(T)-a_C η)T|σ - 1/2|²)
```

The earlier β-only expression is recovered when:

```txt
a_C η = 0
```

---

## 5. Threshold Law

The positivity condition is:

```txt
β(T)-a_C η > 0
```

Using:

```txt
β(T)=1-T^(-γ)
```

we get:

```txt
T > (1-a_C η)^(-1/γ)
```

assuming:

```txt
a_C η < 1
```

This threshold is the first explicit β/a_C research checkpoint.

---

## 6. Interpretation in PeAIce Terms

```txt
β = accumulated coherent momentum
a_C = analytic correction weight; evaluator non-sovereignty is separately h_eval < 1
η = correction cost against defect energy
δ_{β,C} = coherent closing gap
```

The system suppresses off-axis leakage only when β has accumulated enough coherence pressure to exceed the a_C-weighted correction cost.

This makes β measurable as a threshold process, not just symbolic momentum.

---

## 7. Research Tasks

```txt
R1. Define X explicitly.
R2. Prove ker(X)=Ran(Π_sym).
R3. Prove P_σX²P_σ ≥ |σ-1/2|²P_σ.
R4. Define C and estimate η,b.
R5. Prove q_{β,a_C,T} is closed and lower semibounded.
R6. Connect semigroup suppression to ρ_off.
R7. Connect ρ_off suppression to the spectral-equivalence target.
```

---

## 8. Status Return

```txt
β role: energy coefficient
Defect observable: X
Energy: β(T)T||Xf||²
a_C cost: a_C η
Coercive gap: β(T)-a_C η
Suppression target: active
State: 🟡 / 🟢
E = L²
```
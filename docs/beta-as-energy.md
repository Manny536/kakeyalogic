# β as Energy — EEV3 Step 4

**Repo:** KakeyaLogic — Excellence Engine v3  
**Companion:** `docs/beta-dynamic.md`, `docs/operator-domain.md`  
**Status:** 🟡 theorem target · 🟢 energy formalization active  
**Core:** E = L² · β > 0 · h < 1

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

## 2. h-Corrected Energy

Let `C` be h-correction with relative form bound:

```txt
|⟨Cf,f⟩| ≤ η||Xf||² + b||f||²
```

The h-corrected β energy is:

```txt
E_β,h,T(f)
= β(T)T||Xf||² + h⟨Cf,f⟩
```

Lower bound:

```txt
E_β,h,T(f)
≥ (β(T)-hη)T||Xf||² - hb||f||²
```

The gap is:

```txt
δ_β,h(T) = β(T)-hη
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
E_β,h,T(f)
≥ δ_β,h(T)T|σ - 1/2|²||f||² - hb||f||²
```

After floor renormalization:

```txt
E_β,h,T(f)
≥ δ_β,h(T)T|σ - 1/2|²||f||²
```

provided:

```txt
δ_β,h(T) > 0
```

---

## 4. Suppression Estimate

If `A_{β,h,T}` is the self-adjoint operator associated to the closed lower-semibounded form, then the off-axis semigroup obeys:

```txt
||P_σ exp(-A_{β,h,T})P_σ||
≤ exp(-δ_β,h(T)T|σ - 1/2|²)
```

This gives the refined EEV3 suppression target:

```txt
ρ_off(T,σ)
≤ exp(-(β(T)-hη)T|σ - 1/2|²)
```

The earlier β-only expression is recovered when:

```txt
hη = 0
```

---

## 5. Threshold Law

The positivity condition is:

```txt
β(T)-hη > 0
```

Using:

```txt
β(T)=1-T^(-γ)
```

we get:

```txt
T > (1-hη)^(-1/γ)
```

assuming:

```txt
hη < 1
```

This threshold is the first explicit β/h research checkpoint.

---

## 6. Interpretation in PeAIce Terms

```txt
β = accumulated coherent momentum
h = evaluator non-sovereignty / correction gate
η = correction cost against defect energy
δ_β,h = coherent closing gap
```

The system suppresses off-axis leakage only when β has accumulated enough coherence pressure to exceed the h-weighted correction cost.

This makes β measurable as a threshold process, not just symbolic momentum.

---

## 7. Research Tasks

```txt
R1. Define X explicitly.
R2. Prove ker(X)=Ran(Π_sym).
R3. Prove P_σX²P_σ ≥ |σ-1/2|²P_σ.
R4. Define C and estimate η,b.
R5. Prove q_{β,h,T} is closed and lower semibounded.
R6. Connect semigroup suppression to ρ_off.
R7. Connect ρ_off suppression to the spectral-equivalence target.
```

---

## 8. Status Return

```txt
β role: energy coefficient
Defect observable: X
Energy: β(T)T||Xf||²
h cost: hη
Coercive gap: β(T)-hη
Suppression target: active
State: 🟡 / 🟢
E = L²
```
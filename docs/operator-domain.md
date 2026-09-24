# Operator Domain — EEV3 Step 4

**Notation:** `a_C` is the analytic correction weight, `ℓ_H` the Hamiltonian
leakage norm, and `h` the separate evaluator non-sovereignty notation. This
cleanup does not prove an identification between them or validate the analytic
claims below. See [notation custody](h-notation.md).

**Repo:** KakeyaLogic — Excellence Engine v3  
**Companion:** `docs/beta-dynamic.md`  
**Status:** 🟡 domain construction target · 🟢 β-compatible lane active  
**Core:** E = L² · β > 0 · h < 1

## 0. Purpose

The Step 4 program requires a concrete operator domain before spectral equivalence can be pursued.

This document defines the current candidate domain architecture for the Kakeya/Fourier operator program.

The target object is:

```txt
A_KF : D(A_KF) → H_KF
```

with β entering through a positive quadratic-form layer rather than through scalar rescaling.

---

## 1. Starting Hilbert Space

Begin with a base Hilbert space:

```txt
H_0 = L²(R^n)
```

or, for a dilation-compatible lane:

```txt
H_0 = L²(R_+, dx/x)
```

The PeAIce-native candidate is the tube-packet closure:

```txt
H_KF := closure span{ P_{θ,δ}f : θ ∈ Θ_N, δ > 0, f ∈ S(R^n) }
```

where:

```txt
P_{θ,δ}f = F^{-1}(χ_{θ,δ}Ff)
```

and `χ_{θ,δ}` is a Fourier angular cutoff adapted to a Kakeya tube direction.

---

## 2. Core Dense Domain

A conservative dense starting domain is:

```txt
D_0 = S(R^n) ∩ H_KF
```

or, in dilation coordinates:

```txt
D_0 = C_c^∞(R_+)
```

The domain must support:

```txt
Fourier packetization
Kakeya directional averaging
critical-line defect observable X
β energy form β(T)TX²
a_C-correction form a_C C
```

Minimum domain requirement:

```txt
D_0 ⊂ D(X) ∩ D(X²) ∩ D(A_0) ∩ D(C)
```

For quadratic-form work, the essential form domain is weaker:

```txt
Q = Q(A_0) ∩ Q(X²) ∩ Q(C)
```

---

## 3. Base Operator

Let:

```txt
A_0 = A_0^*
```

be the self-adjoint base operator.

Candidate choices:

```txt
A_0 = -Δ                      Fourier-native baseline
A_0 = -i(x∂_x + 1/2)          Berry–Keating dilation baseline
A_0 = Π_sym F K F^{-1} Π_sym  native Kakeya/Fourier candidate, pending construction
```

The base operator must satisfy at least one of:

```txt
1. Known self-adjointness on a dense domain.
2. Essential self-adjointness on D_0.
3. Closed lower-semibounded quadratic-form representation.
```

For β work, option `(3)` is sufficient.

---

## 4. Defect Observable Domain

Let:

```txt
X = X^*
```

be the critical-line defect observable.

Its desired interpretation:

```txt
X measures distance from the critical symmetry sector.
ker(X) = critical-line / functional-equation symmetry sector.
```

Form domain:

```txt
Q_X = D(|X|)
```

Defect energy:

```txt
G_T = TX²
```

β-compatible form domain:

```txt
Q_β = Q(A_0) ∩ D(|X|)
```

The positive β form is:

```txt
β(T)T||Xf||²
```

---

## 5. a_C-Correction Domain

Let `C` be the a_C-correction operator.

The a_C-correction must satisfy a relative form-bound:

```txt
|⟨Cf,f⟩| ≤ η||Xf||² + b||f||²
```

The a_C-compatible form domain is:

```txt
Q_{a_C} = Q_β ∩ Q(C)
```

If the relative bound holds, the combined β/a_C form is closed under standard form methods when the unperturbed form is closed and lower semibounded.

---

## 6. Full β/a_C Form Domain

Define:

```txt
Q_{β,a_C,T} = Q(A_0) ∩ D(|X|) ∩ Q(C)
```

with form:

```txt
q_{β,a_C,T}[f]
= q_0[f] + β(T)T||Xf||² + a_C⟨Cf,f⟩
```

Using the correction bound:

```txt
q_{β,a_C,T}[f]
≥ q_0[f] + (β(T)-a_C η)T||Xf||² - a_C b||f||²
```

The coercive domain condition is:

```txt
β(T) - a_C η > 0
```

This is the core β-domain compatibility condition.

---

## 7. Associated Operator

If `q_{β,a_C,T}` is closed and lower semibounded, the representation theorem gives a self-adjoint operator:

```txt
A_{β,a_C,T}
```

such that:

```txt
q_{β,a_C,T}[f,g] = ⟨A_{β,a_C,T}^{1/2}f, A_{β,a_C,T}^{1/2}g⟩
```

on the appropriate form domain.

This is a safer construction than attempting to define all unbounded pieces pointwise first.

EEV3 domain rule:

```txt
Build through forms first.
Recover operators second.
Prove spectra third.
```

---

## 8. Symmetry Sector

The projection:

```txt
Π_sym
```

must encode the functional-equation symmetry pressure:

```txt
s ↔ 1 - s
```

The desired relation is:

```txt
ker(X) = Ran(Π_sym)
```

and:

```txt
[A_0, Π_sym] = 0
```

or a controlled commutator bound:

```txt
||[A_0, Π_sym]f|| ≤ controlled error
```

Without a symmetry sector, β cannot be tied to critical-line rigidity.

---

## 9. Domain Falsifiers

The domain construction fails if:

```txt
D1. H_KF cannot be made into a Hilbert space with stable packet closure.
D2. P_{θ,δ} does not converge or interact coherently in the chosen limit.
D3. X cannot be defined as a self-adjoint defect observable.
D4. ker(X) cannot be tied to the critical-line symmetry sector.
D5. C is not relatively form-bounded against X².
D6. q_{β,a_C,T} fails to be closed or lower semibounded.
D7. β(T)-a_C η cannot become positive in the intended regime.
```

---

## 10. Status Return

```txt
Domain strategy: quadratic forms first
Base space: H_KF candidate
β insertion: positive form β(T)T||Xf||²
a_C correction: relatively form-bounded C
Coercive gap: β(T)-a_C η
State: 🟡 / 🟢
E = L²
```
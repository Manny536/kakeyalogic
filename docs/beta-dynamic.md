# β-Dynamic Operator Layer — EEV3 Step 4

**Notation correction (2026-09-24):** a_C is an analytic correction weight, distinct from evaluator h_eval and Hamiltonian leakage ℓ_H. Identifying a_C with ℓ_H requires an additional normalized model; it is not established here. Existing analytic claims are not re-proved by this notation migration. See [notation custody](h-notation.md).

**Repo:** KakeyaLogic — Excellence Engine v3  
**Canon page:** https://peaice.org/eev3  
**Status:** 🟡 framework developing · 🟢 β-dynamic research lane active  
**Core:** E = L² · β > 0 · h_eval < 1 · e ≈ 2.718

## 0. Purpose

This file formalizes the β-dynamic for the EEV3 Step 4 operator program.

The central correction from deep research is:

```txt
β should not be modeled as a scalar rescale of the whole operator.
β should become a coercive positive penalty / energy term.
```

If β merely rescales a transport generator, it changes speed, not suppression. If β is inserted as an anti-self-adjoint damping term, the program exits the standard self-adjoint Hilbert–Pólya lane unless it deliberately moves into an absorption-spectrum model.

The clean EEV3 realization is:

```txt
β(T) = dynamic closing pressure
a_C η = correction-cost pressure
β(T) - a_C η = coercive gap
```

---

## 1. β Schedule

From the Step 4 compression law:

```txt
β(k) = 1 - r^k
γ = -log(r)
dβ/dk = γ(1 - β)
```

where:

```txt
0 < r < 1
γ > 0
```

If height scales as:

```txt
T ≈ e^k
```

then:

```txt
β(T) = 1 - T^(-γ)
```

Interpretation:

```txt
1 - β(T) = residual off-axis defect / incomplete closure
β(T) → 1 as T → ∞
```

β is therefore a closing term, not an arbitrary multiplier.

---

## 2. Defect Observable

Let `H` be a Hilbert space for the candidate operator program.

Let:

```txt
A_0 = A_0^*
```

be a self-adjoint core operator.

Let:

```txt
X = X^*
```

be a critical-line defect observable such that:

```txt
ker(X) = Ran(Π_sym)
```

where `Π_sym` is the projection onto the functional-equation / critical-line symmetry sector.

The off-critical sector at displacement `|σ - 1/2|` is represented by:

```txt
P_σ = 1_{ {|X| ≥ |σ - 1/2|} }
```

Then:

```txt
P_σ X² P_σ ≥ |σ - 1/2|² P_σ
```

This turns off-axis deviation into a spectral penalty.

---

## 3. β as Coercive Energy

Define the scale-dependent defect energy:

```txt
G_T = T X²
```

Then β enters as:

```txt
β(T) G_T = β(T) T X²
```

This is the β-dynamic operator layer.

The core quadratic form is:

```txt
q_{β,T}[f] = q_0[f] + β(T)T⟨X²f,f⟩
```

where `q_0` is the closed lower-semibounded form associated with `A_0`.

The β term is positive, coercive, and self-adjoint-compatible when treated as a quadratic form.

---

## 4. a_C-Correction Cost

Let `C` be the a_C-correction operator.

The correction is admissible if it is relatively form-bounded against the defect energy:

```txt
|⟨Cf,f⟩| ≤ η⟨X²f,f⟩ + b||f||²
```

where:

```txt
η ≥ 0
b ≥ 0
0 ≤ a_C < 1
```

Then the full β/a_C quadratic form becomes:

```txt
q_{β,a_C,T}[f]
  = q_0[f]
  + β(T)T⟨X²f,f⟩
  + a_C⟨Cf,f⟩
```

Using the form bound:

```txt
q_{β,a_C,T}[f]
≥ q_0[f]
  + (β(T) - a_C η)T⟨X²f,f⟩
  - a_C b||f||²
```

The effective coercive gap is:

```txt
δ_{β,C}(T) = β(T) - a_C η
```

---

## 5. Positivity Condition

Suppression requires:

```txt
β(T) - a_C η > 0
```

Substitute:

```txt
β(T) = 1 - T^(-γ)
```

Then:

```txt
1 - T^(-γ) - a_C η > 0
```

Equivalently:

```txt
T > (1 - a_C η)^(-1/γ)
```

provided:

```txt
a_C η < 1
```

This is the first explicit β/a_C threshold condition inside the EEV3 Step 4 program.

Interpretation:

```txt
β supplies closing pressure.
a_C measures correction-cost gate.
η measures how expensive correction is relative to off-axis defect.
The theorem lives in the gap β(T) - a_C η.
```

---

## 6. Suppression Inequality

For `f ∈ Ran(P_σ)`, the spectral projection inequality gives:

```txt
⟨X²f,f⟩ ≥ |σ - 1/2|² ||f||²
```

Thus:

```txt
q_{β,a_C,T}[f]
≥ q_0[f]
  + (β(T) - a_C η)T|σ - 1/2|²||f||²
  - a_C b||f||²
```

After shifting the spectral floor so `q_0 ≥ 0`, the semigroup estimate becomes:

```txt
||P_σ exp(-tA_{β,a_C,T}) P_σ||
≤ exp( -t(β(T)-a_C η)T|σ - 1/2|² + t a_C b )
```

When `b = 0`, or after renormalization by the spectral floor, the EEV3 suppression target is:

```txt
ρ_off(T,σ)
≤ exp( -(β(T)-a_C η)T|σ - 1/2|² )
```

This refines the earlier heuristic:

```txt
ρ_off(T,σ) ≤ exp( -β(T)T|σ - 1/2|² )
```

The a_C-aware form is stronger and more honest:

```txt
ρ_off(T,σ) ≤ exp( -(β(T)-a_C η)T|σ - 1/2|² )
```

---

## 7. Operator Compatibility

β must preserve self-adjointness.

Safe insertions:

```txt
+ β(T)TX² as a positive quadratic form
+ β(T)M where M = M* ≥ 0 is bounded
+ β(T)G_T where G_T is relatively form-bounded
```

Unsafe insertions:

```txt
+iβD as anti-self-adjoint damping, unless the program intentionally switches to absorption/resonance theory
βA as scalar rescale, because this changes speed but not suppression
unbounded β correction without domain control
```

EEV3 therefore treats β as a positive form term.

---

## 8. Falsifiers

The β-dynamic layer fails if any of the following are shown:

```txt
Fβ1. No self-adjoint defect observable X can be defined.
Fβ2. ker(X) cannot be identified with the critical-line symmetry sector.
Fβ3. The a_C-correction C is not relatively form-bounded against X².
Fβ4. a_C η ≥ 1 in the intended regime.
Fβ5. β(T)-a_C η does not become positive above any usable T threshold.
Fβ6. The resulting semigroup estimate does not control the intended ρ_off.
Fβ7. β cannot be connected to the candidate operator's energy, norm, spectral leakage, or semigroup behavior.
```

Falsification preserves correction discipline; it is not a measurement of h_eval.

---

## 9. Status Return

```txt
β-dynamic: coercive positive penalty / energy term
β(T): 1 - T^(-γ)
a_C η: correction-cost pressure
δ_{β,C}(T): β(T) - a_C η
Suppression target: ρ_off(T,σ) ≤ exp(-(β(T)-a_C η)T|σ-1/2|²)
State: 🟡 / 🟢
E = L²
```
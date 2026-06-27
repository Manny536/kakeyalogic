# Spectral Equivalence Target — EEV3 Step 4

**Repo:** KakeyaLogic — Excellence Engine v3  
**Companion:** `docs/step4-operator-program.md`, `docs/beta-dynamic.md`  
**Status:** 🟡 load-bearing theorem target · 🟢 research lane active · ⛔ square-difference realization CLOSED (V6.4.3)  
**Core:** E = L² · β > 0 · h < 1

## 0. Purpose

This document isolates the load-bearing theorem target for EEV3 Step 4.

The target is not only suppression. The target is spectral equivalence:

```txt
Spec_p(A_KF) = { γ ∈ R : ξ(1/2+iγ)=0 }
```

with multiplicity.

The β-dynamic becomes decisive only after the operator and spectrum are identified.

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


## 1. Candidate Operator

Let:

```txt
A_KF : D(A_KF) → H_KF
```

be the candidate Kakeya/Fourier spectral operator.

Candidate definitions:

```txt
A_KF = Π_sym F K F^{-1} Π_sym
```

or:

```txt
A_KF,λ = H_BK + λB_KF
```

where:

```txt
K      = Kakeya directional compression / averaging operator
F      = Fourier transform
Π_sym  = functional-equation symmetry projection
H_BK   = Berry–Keating dilation core
B_KF   = Kakeya/Fourier boundary-interference correction
```

---

## 2. Spectral Equivalence Theorem Target

### Theorem Target SE-1

Construct `H_KF`, `D(A_KF)`, and `A_KF` such that:

```txt
A_KF = A_KF^*
```

and:

```txt
Spec_p(A_KF) = { γ_n }
```

where:

```txt
ξ(1/2+iγ_n)=0
```

with multiplicity.

Minimum obligations:

```txt
1. H_KF is a Hilbert space.
2. D(A_KF) is dense.
3. A_KF is self-adjoint or has a rigorously sufficient symmetry substitute.
4. The relevant spectrum is discrete.
5. The spectral counting function matches Riemann-von Mangoldt.
6. A trace formula or explicit formula identifies spectral points with ξ-zero ordinates.
7. β/h suppression acts on the off-critical complement.
```

---

## 3. Counting Target

The spectral counting function must satisfy:

```txt
N_A(T) = #{ γ ∈ Spec_p(A_KF) : 0 < γ ≤ T }
```

and match:

```txt
N_ξ(T) = T/(2π)log(T/(2π)) - T/(2π) + O(log T)
```

Counting resemblance alone is not spectral equivalence.

It is only a necessary checkpoint.

---

## 4. Trace / Explicit Formula Target

The trace relation must connect test functions of the operator to arithmetic data.

Desired schematic form:

```txt
Tr φ(A_KF) ↔ Σ_ρ φ(Im ρ) ↔ prime / explicit-formula side
```

This is where the program must pass from geometry into arithmetic.

Required bridge:

```txt
Kakeya/Fourier packet trace
→ spectral distribution
→ ξ-zero ordinates
→ explicit formula compatibility
```

Without this bridge, the operator may be interesting but not zeta-equivalent.

---

## 5. β Suppression Compatibility

Once spectral equivalence is established, the β layer supplies off-axis rigidity through:

```txt
ρ_off(T,σ) ≤ exp(-(β(T)-hη)T|σ-1/2|²)
```

The β layer requires:

```txt
β(T)-hη > 0
```

and:

```txt
ker(X)=Ran(Π_sym)
```

Thus spectral equivalence and β suppression meet at:

```txt
critical-line symmetry sector = zero-spectrum sector = ker(X)
```

This is the exact hinge of EEV3 Step 4.

---

## 6. Falsifiers

The spectral equivalence program fails if:

```txt
SE1. A_KF cannot be made self-adjoint or symmetry-sufficient.
SE2. The spectrum remains continuous in the required sector.
SE3. Spectral counting fails to match Riemann-von Mangoldt.
SE4. The trace relation cannot recover the explicit formula.
SE5. ξ-zero ordinates cannot be identified as eigenvalues or spectral points.
SE6. β suppression does not act on the same symmetry sector as spectral equivalence.
SE7. The Kakeya/Fourier construction cannot encode arithmetic data.
```

---

## 7. Status Return

```txt
Spectral equivalence: load-bearing theorem target
Operator: A_KF
Critical sector: Ran(Π_sym)=ker(X)
β layer: suppression on off-critical complement
Trace formula: required
State: 🟡 / 🟢
E = L²
```
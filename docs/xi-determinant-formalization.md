# Xi Determinant Formalization — Step 1 / Step 2

**Repo:** KakeyaLogic — Excellence Engine v3
**Companion:** `docs/spectral-determinism.md`, `docs/spectral-equivalence-target.md`, `docs/l2-spectral-operator.md`
**Status:** CONDITIONAL CRITERION · operator construction OPEN · historical square-difference realization CLOSED-NEGATIVE
**Core objects:** ζ, ξ, Ξ, D_A, μ_off, self-adjointness, determinant identity
**Canon flag:** Gödel → h

> **Current scope, reviewed 29 October 2026.** This note states a conditional
> determinant criterion, not a reopened construction lane. The square-difference
> realization is CLOSED-NEGATIVE under V6.4.3, and the bounded WP5b lane is
> CLOSED-NEGATIVE under V6.5. The controlling relocation is
> [prime-carrying trace architecture](prime-carrying-trace-architecture.md), with
> [spectral-equivalence closure](spectral-equivalence-target.md). A new Dirac lift
> must independently meet those counting, domain, and arithmetic obligations.

## 0. Purpose

This document sharpens the first formal bridge in the KakeyaLogic spectral program:

```txt
ζ(s) → ξ(s) → Ξ(z) → determinant target → real spectrum → μ_off = 0
```

The goal is to prevent the phrase “substitute ζ by Ξ” from reading as an informal replacement. The move is instead a zero-preserving completion followed by a coordinate change that converts RH into a real-zero / real-spectrum problem.

The determinant step is then stated as a theorem target rather than as an assumed result.

---

## 1. Xi reduction is not a heuristic substitution

Define the completed zeta function:

```math
ξ(s)=\frac12s(s-1)π^{-s/2}Γ(s/2)ζ(s).
```

Define the critical-line coordinate function:

```math
Ξ(z)=ξ\left(\frac12+iz\right).
```

Inside the critical strip

```math
0<\operatorname{Re}(s)<1,
```

the completion factors introduce no new nontrivial zeros. More precisely, away from the endpoint regularization factors, the multiplier

```math
\frac12s(s-1)π^{-s/2}Γ(s/2)
```

is nonzero in the open critical strip. Therefore, for nontrivial zeros,

```math
ζ(ρ)=0 \Longleftrightarrow ξ(ρ)=0.
```

Under the coordinate transform

```math
ρ=\frac12+iz,
```

the critical line becomes

```math
\operatorname{Re}(ρ)=\frac12 \Longleftrightarrow z\in\mathbb R.
```

Therefore RH is equivalent to:

```math
Ξ(z)=0 \Rightarrow z\in\mathbb R.
```

**Formal reading:** Ξ is viable because it preserves the nontrivial zero set while translating the line condition into a real-axis condition.

---

## 2. Determinant target: first conservative formulation

Let

```math
A_{Φ,K}:\operatorname{Dom}(A)\subset H_{Φ,K}\to H_{Φ,K}
```

be a candidate KakeyaLogic operator on a Hilbert space `H_{Φ,K}`.

Define a regularized spectral determinant:

```math
D_A(z):=\det_ζ(A_{Φ,K}-zI).
```

The determinant target is:

```math
D_A(z)=CΞ(z),\qquad C\ne0.
```

This should be read as an equality of entire functions after regularization, or at minimum as an equality of zero divisors:

```math
\mathcal Z(D_A)=\mathcal Z(Ξ)
```

with multiplicity.

The finite-dimensional determinant principle motivates this target. In infinite
dimensions, compact resolvent alone does not define a zeta determinant: a spectral
cut, meromorphic continuation, regularity at the determinant parameter, and the
zero-divisor property must be established for the chosen realization. A signed
self-adjoint spectrum needs explicit branch conventions. No regularization is
supplied by this note.

---

## 3. Correction: avoid premature squaring

A tempting form in the repo is:

```math
\det_ζ(L^2_{Φ,K}-(z^2+1/4))=CΞ(z).
```

This is suggestive, but it must be handled carefully.

Because Ξ is even,

```math
Ξ(z)=Ξ(-z),
```

a squared spectral coordinate can be natural. However, a squared operator target risks losing sign and multiplicity data unless the spectral lift is specified.

The safer formulation is a two-level target:

### Level A — Dirac-style spectral lift

Construct a self-adjoint operator `B_{Φ,K}` such that

```math
\det_ζ(B_{Φ,K}-zI)=CΞ(z).
```

Then zeros of Ξ are directly spectral values of `B_{Φ,K}`.

### Level B — squared Hamiltonian shadow

Define

```math
L^2_{Φ,K}=B_{Φ,K}^{2}+\frac14I
```

or, depending on normalization,

```math
L^2_{Φ,K}-\frac14I=B_{Φ,K}^{2}.
```

Squaring is not automatically a determinant identity. For a symmetric signed
spectrum, the pair +γ and -γ gives B² an eigenvalue γ² of twice the individual
multiplicity. Even in finite dimensions det(B²-z²I) is proportional to
det(B-zI)det(B+zI), so an even Dirac determinant gives a squared zero divisor.
Regularized products can require further normalization. A positive-spectrum
restriction or another justified multiplicity prescription is owed before any
squared determinant can be derived.

**Rule:** prove the linear `z` determinant before relying on the `z²+1/4` determinant.

---

## 4. Spectral criterion for μ_off = 0

Define the zero-counting measure of Ξ:

```math
μ_Ξ:=\sum_{Ξ(z)=0}m_zδ_z.
```

Define off-axis mass:

```math
μ_{off}:=μ_Ξ(\mathbb C\setminus\mathbb R).
```

Then RH is equivalent to:

```math
μ_{off}=0.
```

If `B_{Φ,K}` is self-adjoint and

```math
\det_ζ(B_{Φ,K}-zI)=CΞ(z),
```

then:

```math
Ξ(z)=0
\Rightarrow
z\in\operatorname{Spec}(B_{Φ,K})
\Rightarrow
z\in\mathbb R.
```

Therefore:

```math
μ_{off}=0.
```

This is the precise mathematical hinge.

---

## 5. Theorem target: Xi determinant criterion

### Theorem Target XD-1

Let `H_{Φ,K}` be a Hilbert space and let

```math
B_{Φ,K}:\operatorname{Dom}(B)\subset H_{Φ,K}\to H_{Φ,K}
```

be densely defined and self-adjoint.

Assume:

1. `B_{Φ,K}` has the spectral discreteness required for a ζ-regularized determinant.
2. The determinant

```math
D_B(z)=\det_ζ(B_{Φ,K}-zI)
```

is well-defined as an entire function up to a nowhere-zero entire factor, and
its zeros are exactly the discrete eigenvalues with their spectral multiplicities.
This zero-divisor property is an explicit hypothesis, not a consequence of
self-adjointness alone.

3. There exists `C≠0` such that

```math
D_B(z)=CΞ(z).
```

Then all zeros of Ξ are real. Consequently all nontrivial zeros of ζ satisfy

```math
\operatorname{Re}(ρ)=\frac12.
```

### Proof skeleton

Since `B_{Φ,K}` is self-adjoint, its spectrum is real. The zeros of the ζ-regularized determinant occur exactly at spectral values of `B_{Φ,K}` with multiplicity. By the determinant identity, the zeros of `D_B` are exactly the zeros of Ξ. Therefore every zero of Ξ is real. Since `Ξ(z)=ξ(1/2+iz)`, every corresponding nontrivial zero `ρ=1/2+iz` of ζ has real part `1/2`.

---

## 6. What remains open

The abstract criterion remains conditional. Any new realization owes:

```txt
XD-1. Define H_{Φ,K} rigorously.
XD-2. Construct B_{Φ,K} explicitly.
XD-3. Prove Dom(B) is dense.
XD-4. Prove B_{Φ,K}=B_{Φ,K}^*.
XD-5. Prove the required spectral discreteness / trace-class resolvent condition.
XD-6. Define det_ζ(B_{Φ,K}-zI) without ambiguity.
XD-7. Prove D_B(z)=CΞ(z), not merely that the zeros resemble Ξ zeros.
XD-8. Recover Riemann-von Mangoldt counting from the spectral side.
XD-9. Recover the explicit formula / prime side from the trace side.
XD-10. Derive β/h off-axis suppression as a consequence of the operator structure.
```

---

## 7. β/h compatibility layer

The existing β/h suppression form

```math
ρ_{off}(T,σ)\le \exp\left(-(β(T)-hη)T|σ-1/2|^2\right)
```

should not be treated as a substitute for spectral equivalence.

It belongs after the determinant identity:

```txt
operator identity → real spectrum → μ_off=0 → β/h explains stability of the critical sector
```

Rather than:

```txt
β/h suppression → assume μ_off=0
```

The rigorous ordering is:

```txt
self-adjointness first
spectral determinant identity second
μ_off=0 third
β/h stability interpretation fourth
```

---

## 8. Status return

```txt
ζ → ξ completion justified:        YES
ξ → Ξ coordinate transform:        YES
Ξ as spectral target:              YES
Linear determinant target:         FORMALIZED
Squared determinant target:        SECONDARY / MULTIPLICITY DERIVATION OWED
Self-adjoint operator built:        OPEN
D_B(z)=CΞ(z) proved:                OPEN
μ_off=0 derived:                   TARGET
β/h suppression role:              COMPATIBILITY LAYER
```

KakeyaLogic should now treat the determinant program as a Dirac-first spectral construction:

```txt
B_{Φ,K} self-adjoint
→ det_ζ(B_{Φ,K}-zI)=CΞ(z)
→ zeros of Ξ are real
→ μ_off=0
→ Re(ρ)=1/2
```

## Sources and rejection conditions

The completion and reflection formulas are standard background:
[NIST DLMF §25.4](https://dlmf.nist.gov/25.4), with the zero-location question in
[§25.10](https://dlmf.nist.gov/25.10). The determinant identity is a proposed
construction obligation. Reject a candidate if it has a mismatched zero divisor,
uncontrolled spectral cut, incorrect multiplicities, incompatible counting, or
requires insertion of the desired zero ordinates. RH and Coleman remain OPEN;
`h_eval < 1` remains active.

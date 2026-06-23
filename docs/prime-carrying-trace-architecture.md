# Prime-Carrying Trace Architecture after the Square-Difference No-Go

**Canon designation:** `PEAICE-CLAUDEV6-NOTE-003`  
**Program:** PeAIce Research Program · KakeyaLogic · L²_C Framework  
**Status:** Riemann Hypothesis OPEN · Coleman Conjecture OPEN · no proof claimed  
**Purpose:** repo-facing rigor gate after the `|m²−n²|^{-σ}` determinant no-go

## 0. Executive status

The square-difference kernel family is closed as a determinant bridge to the completed zeta function. It remains useful only as a compact-geometry test object.

The live branch is not another hand-built compact kernel on `ℓ²(ℕ)`. The live branch is **prime-carrying trace architecture**: a construction where the prime powers, von Mangoldt weights, archimedean density, and functional-equation symmetry are present from the start.

This note records the transition from a closed operator family to a rigor-gated research direction.

```text
Closed:
  |m²−n²|^{-σ} kernel family as a determinant bridge to Ξ.

Open:
  prime-carrying trace architecture.

Computable next work package:
  Nyman–Beurling / Báez-Duarte Hilbert-space distance problem.

Rule:
  No future PeAIce RH-side object enters the repo as a bridge unless it explicitly carries
  Λ(n), log(p^k), archimedean T log T density, and functional-equation symmetry.
```

---

## 1. Closed branch: what is actually proved

Let

\[
K_\sigma(m,n)=
\begin{cases}
|m^2-n^2|^{-\sigma}, & m\ne n,\\
0, & m=n.
\end{cases}
\]

After resolving the weighted inner product, the thermal weight cancels. The corrected operator is the weight-free symmetric kernel above, written in the orthonormal basis. The verified result is

\[
K_\sigma\in S_2 \quad\Longleftrightarrow\quad \sigma>\frac12.
\]

Thus, for `σ > 1/2`, `K_σ` is Hilbert–Schmidt, compact, and self-adjoint, with real discrete spectrum tending to zero. This is the verified brick.

The determinant route to `Ξ` closes for this family by three gates.

### 1.1 Parity wall

The completed critical-line function

\[
\Xi(z)=\xi\!\left(\frac12+iz\right)
\]

is even. Hence any determinant representation directly matching `Ξ(z)` must have vanishing odd spectral moments.

But for the square-difference kernel,

\[
\operatorname{Tr}(K_\sigma^3)
=
\sum_{i,j,k\text{ distinct}}
|i^2-j^2|^{-\sigma}|j^2-k^2|^{-\sigma}|k^2-i^2|^{-\sigma}
>0.
\]

So the naive determinant target `det(I − zK_σ)` fails at the cubic trace. The regularized determinant `det₂` does not remove this obstruction; the cubic term remains in the logarithmic expansion.

### 1.2 Counting mismatch for the `z² + 1/4` target

Encoding the spectral variable as `z²` builds evenness by hand, but then eigenvalue counting closes the route. If the free part has eigenvalues comparable to `n⁴`, then

\[
N_L(\Lambda)\sim \Lambda^{1/4}.
\]

The zeta-zero target requires Riemann–von Mangoldt density,

\[
N_\zeta(T)\sim \frac{T}{2\pi}\log\frac{T}{2\pi},
\]

and after `Λ = T² + 1/4`, this becomes

\[
N_\zeta(\Lambda)\sim \sqrt{\Lambda}\log\Lambda.
\]

The operator is polynomially too sparse. Relatively compact perturbations cannot repair this Weyl class mismatch.

### 1.3 Prime-support obstruction

The explicit formula requires a trace side supported on prime powers:

\[
\sum_\gamma h(\gamma)
=
\text{archimedean/Gamma terms}
-
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\widehat h(\log n)
+\cdots.
\]

The square-difference kernel factors as

\[
|m^2-n^2|^{-\sigma}=|m-n|^{-\sigma}|m+n|^{-\sigma}.
\]

It carries integer-square geometry. It does not carry prime powers, von Mangoldt weights, or Euler-product structure. There is nowhere for the first non-archimedean contribution

\[
\frac{\log 2}{\sqrt2}\widehat h(\log2)
\]

to originate.

This is the decisive no-go. The operator has compact geometry, not arithmetic dynamics.

---

## 2. Necessary specification for a prime-carrying operator

This section is a necessary-condition spec, not a construction.

A candidate RH-side trace object must be compatible with the Weil explicit formula. It must have a trace identity of the form

\[
\operatorname{Tr} h(H)
=
\text{archimedean term}
-
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\widehat h(\log n)
+\text{endpoint / symmetry terms}.
\]

Therefore, any proposed operator, transfer system, or determinant bridge must carry the following data structurally.

### 2.1 Length spectrum

\[
\text{lengths} = \{\log(p^k):p\text{ prime},\ k\ge1\}.
\]

Generic integer distances, square differences, or hand-built decay kernels do not satisfy this condition.

### 2.2 Weights

\[
\frac{\Lambda(p^k)}{\sqrt{p^k}}
=\frac{\log p}{p^{k/2}}.
\]

This is where the load-bearing `1/2` lives. It is the critical-line mass in the explicit formula.

It must not be confused with the Hilbert–Schmidt threshold

\[
\sigma>\frac12,
\]

which is only analytic square-summability.

```text
The Hilbert–Schmidt 1/2 is analytic summability.
The explicit-formula 1/2 is arithmetic critical-line mass.
They are not the same invariant.
```

### 2.3 Archimedean term

The smooth term must reproduce the Gamma-factor side and the Riemann–von Mangoldt density

\[
N(T)\sim \frac{T}{2\pi}\log\frac{T}{2\pi}.
\]

The counting obstruction and the prime-support obstruction are therefore linked. The correct archimedean place forces the correct asymptotic density.

### 2.4 Reality mechanism

The spectrum must be real through a self-adjoint operator, a Frobenius-like mechanism, or an equivalent positivity structure. This is the actual Hilbert–Pólya burden.

### 2.5 Trace formula delivery

The route must be a trace formula, relative determinant, Lefschetz formula, Selberg/Gutzwiller-type identity, or an established equivalent Hilbert-space criterion. Eigenvalue-by-eigenvalue matching is not an acceptable construction principle.

---

## 3. Known branches and exact status

### 3.1 Berry–Keating `xp`

The Berry–Keating direction points at the archimedean counting term through the dilation Hamiltonian

\[
H=\frac12(xp+px).
\]

It gets the smooth counting behavior strikingly close to the Riemann–von Mangoldt term. The open gap is rigorous discreteness and a forced prime-periodic-orbit mechanism. The bare `xp` operator has continuous-spectrum issues; the prime sum remains heuristic unless the dynamics forces orbit lengths `log p`.

### 3.2 Connes adèles / noncommutative geometry

The Connes approach genuinely carries primes because it works over all places of `ℚ`: the real place and every `p`-adic place. The explicit formula becomes a global trace formula. The RH difficulty is relocated into positivity / spectral interpretation, not removed. Zeros appear through an absorption or missing-spectrum picture rather than as ordinary eigenvalues of a simple compact self-adjoint operator.

### 3.3 Selberg trace formula

For Selberg zeta functions, the Hilbert–Pólya dream is realized: a self-adjoint Laplacian, a trace formula, and closed geodesics whose lengths feed the zeta object. This is a genuine model of the right architecture. It is not the Riemann zeta problem because the length spectrum is not the rational-prime spectrum of `ζ(s)`.

### 3.4 Function fields

For curves over finite fields, the analogue is realized through Frobenius acting on cohomology. The zeros are eigenvalues of a geometric operator, and the prime objects enter through Lefschetz. This success does not currently transfer to `Spec ℤ`, because the required cohomological geometry over the integers is not known.

---

## 4. Computable pivot: Nyman–Beurling / Báez-Duarte

The next PeAIce computation should not attempt to invent another bespoke zeta operator. It should implement an established RH-equivalent Hilbert-space formulation.

The Nyman–Beurling criterion reformulates RH as a closure problem in a Hilbert space. Báez-Duarte strengthens the formulation into a discrete form. This gives a healthier computational target: finite distances whose decay is equivalent to RH.

One computational form uses Dirichlet polynomials

\[
A_N(s)=\sum_{n=1}^{N}\frac{a_n}{n^s}
\]

and the distance

\[
d_N^2
=
\inf_{A_N}
\frac{1}{2\pi}
\int_{-\infty}^{\infty}
\left|
1-\zeta\!\left(\frac12+it\right)
A_N\!\left(\frac12+it\right)
\right|^2
\frac{dt}{\frac14+t^2}.
\]

The finite problem can be written as a least-squares projection. Define

\[
f_n(t)=\zeta\!\left(\frac12+it\right)n^{-1/2-it}
\]

inside the weighted Hilbert space

\[
\langle f,g\rangle
=
\frac{1}{2\pi}\int_{-\infty}^{\infty}f(t)\overline{g(t)}\frac{dt}{\frac14+t^2}.
\]

Then

\[
d_N^2=\inf_{a_1,\dots,a_N}\left\|1-\sum_{n=1}^{N}a_n f_n\right\|^2.
\]

Let

\[
G_{mn}=\langle f_m,f_n\rangle,
\qquad
b_m=\langle 1,f_m\rangle.
\]

If `G_N` is invertible, the finite distance is

\[
d_N^2=1-b^*G_N^{-1}b.
\]

Equivalently, the computation is a Gram-matrix projection problem. This is the preferred next work package because it is already tied to a known RH-equivalent Hilbert-space criterion.

```text
Next compute target:
  Build finite Gram matrices G_N.
  Stabilize numerical integration on the critical line.
  Track d_N² = 1 − b* G_N^{-1} b.
  Compare decay against known Nyman–Beurling / Báez-Duarte expectations.
  Make no proof claim from numerics.
```

---

## 5. PeAIce rigor gate

A proposed RH-side operator, approximation, determinant, or spectral bridge must pass this checklist before it enters the repo as a bridge.

```text
[ ] Prime support: log(p^k), not generic integer distances.
[ ] Von Mangoldt weights: Λ(n)/sqrt(n).
[ ] Archimedean density: T log T.
[ ] Evenness / functional-equation symmetry.
[ ] Trace formula route, not eigenvalue guessing.
[ ] Known-equivalent formulation or clearly marked conjectural bridge.
[ ] No proof language unless every equivalence step is proven.
```

### Canon status block

```text
PEAICE RIGOR GATE

Closed:
The |m²−n²|^{-σ} kernel family is closed as a determinant bridge to Ξ.
It verifies a compact Hilbert–Schmidt threshold, but it does not carry prime arithmetic.

Open:
Prime-carrying trace architecture remains open.

Computable:
The Nyman–Beurling / Báez-Duarte distance problem is the preferred next work package.

Rule:
No future PeAIce RH object enters the repo as a bridge unless it explicitly carries
Λ(n), log(p^k), archimedean density, and functional-equation symmetry.
```

---

## 6. References to anchor before further expansion

- B. Nyman, *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*, 1950.
- A. Beurling, unpublished seminar criterion, 1955; later known through the Nyman–Beurling criterion.
- L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, Rendiconti di Matematica, 2003.
- M. V. Berry and J. P. Keating, `H = xp` and the Riemann zeros, 1999.
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Mathematica, 1999.
- A. Selberg, trace formula and Selberg zeta literature.
- A. Weil and P. Deligne, function-field RH and cohomological trace-formula framework.

---

## 7. Final canon line

The square kernel taught us what a wall looks like. Báez-Duarte gives us a real Hilbert-space door with RH still fully intact.

**RH remains OPEN. Coleman Conjecture remains OPEN. No proof is claimed.**

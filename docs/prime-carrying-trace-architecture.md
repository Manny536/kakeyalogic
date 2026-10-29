# Prime-Carrying Trace Architecture after the Square-Difference Audit

**Canon designation:** `PEAICE-CLAUDEV6-NOTE-003 / V6.5 relocation target`  
**Program:** PeAIce Research Program · KakeyaLogic · L²_C Framework  
**Status:** Riemann Hypothesis OPEN · Coleman Conjecture OPEN · no proof claimed  
**Purpose:** repo-facing rigor gate after the `|m²−n²|^{-σ}` no-go, scope-corrected by the Copilot prime-support audit

> **V6.5 DOWNSTREAM NOTE — propagated 1 July 2026.** WP5b bounded lane is
> **CLOSED-NEGATIVE** (`WP5-OBS-2`): Krein SSF `ξ(λ)` uniformly bounded under operator-bounded
> coupling (Theorem H, claude-v6 canon). Prime-carrying relocation is **forced** — R1 requires
> unbounded `ξ` at `√λ log λ` scale. Live: L1 unbounded mods · WP5c u-flow · L3 ladder.
> Source: Fable 5 WP5b scaffold · Grok TERMINAL-004. RH `OPEN`.

> **V6.4.3 RELOCATION TARGET — live frontier.** GAP-001 moved *here* from the closed
> `|m^2 - n^2|^{-sigma}` square-difference lane (see `docs/peaice-ddatl-001.md` Section 7.1).
> This is the only open operator route: lengths `log(p^k)`, weights `Lambda(p^k) p^{-k/2}`,
> archimedean `Gamma`-density giving `T log T`, reality via self-adjointness. RH `OPEN`.

## 0. Executive status

The square-difference kernel family remains under no-go pressure, but the rigorous closure is now sharper and narrower than the first V6.4 statement.

The prior sentence "the kernel has no primes, therefore it cannot manufacture zeta arithmetic" is downgraded to a heuristic. Entrywise square structure does not by itself prove global spectral invariants are prime-free. The Jacobi theta function is the warning: it is built from integer-square data and still participates directly in the analytic continuation and functional equation of `ζ`.

The corrected canon is:

```text
Rigorous:
  Corridor I: naive determinant det(I − zK) is closed by parity.
  Corridor II: z² + 1/4 eigenvalue route is closed by counting mismatch.
  Trace-class determinant corridor is closed by genus mismatch.

Scope-corrected:
  The prime-support obstruction is a strong heuristic / trace-level pressure,
  not an all-orders determinant proof by itself.

Open computation:
  Hilbert–Schmidt determinant corridor is reduced to the singular-value exponent
  ρ(K_σ) versus 1.

Live frontier:
  compute s_n(K_σ) asymptotics;
  keep prime-carrying trace architecture as the structural open branch;
  keep Nyman–Beurling / Báez-Duarte as the preferred RH-equivalent compute pivot.
```

This note supersedes the earlier wording that closed the full determinant corridor solely by "missing prime support." The conclusion that the `|m²−n²|` family is unlikely to reach `Ξ` is preserved; the proof status is corrected.

---

## 1. Corrected kernel brick

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

Thus, for `σ > 1/2`, `K_σ` is Hilbert–Schmidt, compact, and self-adjoint, with real discrete spectrum tending to zero. This brick remains valid.

What changes in V6.4.3 is not Theorem B. What changes is the determinant-level no-go language.

---

## 2. The three corridors and their corrected status

### 2.1 Corridor I — naive determinant `det(I − zK_σ)`

This route is rigorously closed.

The completed critical-line function

\[
\Xi(z)=\xi\!\left(\frac12+iz\right)
\]

is even. Hence any direct determinant representation matching `Ξ(z)` must have vanishing odd spectral moments.

But for the square-difference kernel,

\[
\operatorname{Tr}(K_\sigma^3)
=
\sum_{i,j,k\text{ distinct}}
|i^2-j^2|^{-\sigma}|j^2-k^2|^{-\sigma}|k^2-i^2|^{-\sigma}
>0.
\]

So the naive determinant target fails at the cubic trace. Carleman regularization does not save the direct `z`-determinant: the cubic term remains in the logarithmic expansion.

### 2.2 Corridor II — `z² + 1/4` eigenvalue target

This route is rigorously closed.

Encoding the spectral variable as `z²` builds evenness in by hand and evades the parity wall. But eigenvalue counting closes the route. If the free part has eigenvalues comparable to `n⁴`, then

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

The operator is polynomially too sparse. Relatively compact perturbations cannot repair this Weyl class mismatch. This is the repository's L2-5 obstruction.

### 2.3 Corridor III — relative / regularized determinant corridor

This route is scope-corrected.

A holistic relative determinant identity could, in principle, yield `Ξ` without matching eigenvalues one by one. Corridor III is not automatically closed by Corridor I or Corridor II:

- the `z²` encoding can neutralize evenness objections;
- the operator spectrum need not equal the zero ordinates directly;
- first-order trace neutrality does not control every higher cumulant.

The previous prime-support argument remains useful as guidance, but it is not a complete determinant-level proof.

---

## 3. Prime-support argument: downgraded but preserved as a gate

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

It has no local von Mangoldt weight in any entry. That remains an important warning.

However, the implication

```text
entries built from integer squares ⇒ global determinant invariants are prime-free
```

is invalid as a general principle.

The Jacobi theta function is the counterexample. It is assembled from integer-square data, yet through Riemann's theta representation it participates in the analytic continuation and functional equation of `ζ`. Therefore, "integer-square form" alone cannot be used as a determinant-level no-go proof.

Corrected reading:

```text
What K_σ lacks locally:
  explicit Λ(n), log(p^k), and Euler-product weights in its entries.

What remains unproved from entry inspection alone:
  that every global invariant of K_σ is prime-free.

Required next step:
  compute global invariants: traces, cumulants, singular values, determinant order, and functional-equation content.
```

---

## 4. Trace-neutrality: first-order only

Theorems C and E remain valid as trace-level results, but their scope must be respected.

For `K ∈ S₂`, the Carleman determinant has the logarithmic expansion

\[
\log \det{}_2(I-zK)
=-\sum_{p\ge2}\frac{z^p}{p}\operatorname{Tr}(K^p).
\]

Theorems C and E constrain the first-order trace channel. They do not, by themselves, rule out every higher cumulant

\[
\operatorname{Tr}(K^p),\qquad p\ge2.
\]

So the correct statement is:

```text
Trace-neutrality closes the first-order trace route.
It does not alone close every all-orders determinant route.
```

The corridor lives precisely in the gap between first order and all orders.

---

## 5. Rigorous positivity invariant

The rigorous invariant behind the parity wall is positivity, not prime absence.

For `σ > 1/2`, `K_σ ∈ S₂`, and for every `p ≥ 2`, `K_σ^p ∈ S₁`. Since `K_σ` has nonnegative off-diagonal entries and zero diagonal,

\[
\operatorname{Tr}(K_\sigma^p)
=
\sum_{i_1,\dots,i_p}\prod_j (K_\sigma)_{i_j i_{j+1}}
\ge0,
\]

with strict positivity for every `p ≥ 2`, because closed walks on distinct indices exist.

In particular,

\[
\operatorname{Tr}(K_\sigma^{2r+1})>0,
\]

while the odd power sums associated with the even function `Ξ(z)` vanish. This is the rigorous engine for Corridor I.

---

## 6. Genus obstruction: trace-class corridor closed

The trace-class determinant corridor is rigorously closed by entire-function genus.

`Ξ` is entire of order `1` and genus `1`: its zeros have logarithmic density, and the canonical product requires genus-one Weierstrass factors.

If `A ∈ S₁`, then

\[
\det(I-zA)=\prod_n(1-z\lambda_n(A)),
\qquad
\sum_n |\lambda_n(A)|<\infty,
\]

is a genus-zero product. A genus-zero Fredholm determinant cannot equal `C·Ξ(z)`.

Therefore:

```text
No trace-class operator A can satisfy det(I − zA) = C·Ξ(z).
```

This sharpens the parity obstruction. It closes the trace-class corridor without appealing to prime support.

---

## 7. Hilbert–Schmidt corridor: reduced to singular-value exponent

The genuine square-difference object is Hilbert–Schmidt, not necessarily trace class. For `A ∈ S₂`, `det₂(I − zA)` is an entire function of genus at most `1` and order at most `2`.

The necessary order condition for

\[
\det{}_2(I-zA)=C\,\Xi(z)
\]

is that the convergence exponent of the singular values equals `1`:

\[
\rho(A)=
\inf\left\{p\ge1:\sum_n s_n(A)^p<\infty\right\}=1.
\]

For the kernel family, the live analytic question is therefore

\[
\rho(K_\sigma)\stackrel{?}{=}1.
\]

If `ρ(K_σ) ≠ 1`, the Hilbert–Schmidt determinant corridor closes rigorously by order mismatch. If `ρ(K_σ)=1`, the program must descend to genus, zero-density, cumulant, and functional-equation tests.

This is now the correct next probe:

```text
Compute singular-value asymptotics s_n(K_σ).
Extract ρ(K_σ).
Compare ρ(K_σ) against 1.
```

---

## 8. Cumulant and coefficient tests

Independent of global order, the determinant can be tested coefficient by coefficient.

The even coefficients of

\[
\log\frac{\Xi(z)}{\Xi(0)}
\]

are governed by secular sums over zero ordinates,

\[
\sum_\gamma \gamma^{-2k},
\qquad k=1,2,3,\dots.
\]

The operator side is governed by the regularized traces

\[
\operatorname{Tr}(K_\sigma^p).
\]

A single mismatch at a required coefficient falsifies the identity at that order. A match would be meaningful only if it survives the full cumulant sequence and the growth/genus tests.

This replaces broad prime-support rhetoric with finite, checkable invariants.

---

## 9. Functional-equation content

The substitution `z²` imitates evenness, but `Ξ(z)=Ξ(-z)` is not merely parity. It encodes the `s ↔ 1−s` functional equation and the archimedean Gamma factor.

Any determinant construction must reproduce the content of this symmetry, not just its even visual form.

Therefore, a future candidate must be checked for:

```text
[ ] parity / evenness;
[ ] order and genus;
[ ] Riemann–von Mangoldt density;
[ ] archimedean Gamma-factor content;
[ ] prime-power side of the explicit formula;
[ ] all-orders cumulant compatibility.
```

---

## 10. Prime-carrying trace architecture: necessary specification

This remains the structural open branch.

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

### 10.1 Length spectrum

\[
\text{lengths} = \{\log(p^k):p\text{ prime},\ k\ge1\}.
\]

Generic integer distances, square differences, or hand-built decay kernels do not satisfy this condition directly.

### 10.2 Weights

\[
\frac{\Lambda(p^k)}{\sqrt{p^k}}
=\frac{\log p}{p^{k/2}}.
\]

This is where the load-bearing `1/2` lives. It is the critical-line mass in the explicit formula. It must not be confused with the Hilbert–Schmidt threshold

\[
\sigma>\frac12,
\]

which is analytic square-summability.

```text
The Hilbert–Schmidt 1/2 is analytic summability.
The explicit-formula 1/2 is arithmetic critical-line mass.
They are not the same invariant.
```

### 10.3 Archimedean term

The smooth term must reproduce the Gamma-factor side and the Riemann–von Mangoldt density

\[
N(T)\sim \frac{T}{2\pi}\log\frac{T}{2\pi}.
\]

### 10.4 Reality mechanism

The spectrum must be real through a self-adjoint operator, a Frobenius-like mechanism, or an equivalent positivity structure. This is the actual Hilbert–Pólya burden.

### 10.5 Trace formula delivery

The route must be a trace formula, relative determinant, Lefschetz formula, Selberg/Gutzwiller-type identity, or an established equivalent Hilbert-space criterion. Eigenvalue-by-eigenvalue matching is not an acceptable construction principle.

---

## 11. Known branches and exact status

### 11.1 Berry–Keating `xp`

The Berry–Keating direction points at the archimedean counting term through the dilation Hamiltonian

\[
H=\frac12(xp+px).
\]

It gets the smooth counting behavior strikingly close to the Riemann–von Mangoldt term. The open gap is rigorous discreteness and a forced prime-periodic-orbit mechanism. The bare `xp` operator has continuous-spectrum issues; the prime sum remains heuristic unless the dynamics forces orbit lengths `log p`.

### 11.2 Connes adèles / noncommutative geometry

The Connes approach carries primes through all places of `ℚ`: the real place and every `p`-adic place. The explicit formula becomes a global trace formula. The RH difficulty is relocated into positivity / spectral interpretation, not removed. Zeros appear through an absorption or missing-spectrum picture rather than as ordinary eigenvalues of a simple compact self-adjoint operator.

### 11.3 Selberg trace formula

For Selberg zeta functions, the Hilbert–Pólya dream is realized: a self-adjoint Laplacian, a trace formula, and closed geodesics whose lengths feed the zeta object. This is a genuine model of the right architecture. It is not the Riemann zeta problem because the length spectrum is not the rational-prime spectrum of `ζ(s)`.

### 11.4 Function fields

For curves over finite fields, the analogue is realized through Frobenius acting on cohomology. The zeros are eigenvalues of a geometric operator, and the prime objects enter through Lefschetz. This success does not currently transfer to `Spec ℤ`, because the required cohomological geometry over the integers is not known.

---

## 12. Computable pivot: Nyman–Beurling / Báez-Duarte

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
1-
\zeta\!\left(\frac12+it\right)
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

## 13. Updated PeAIce rigor gate

A proposed RH-side operator, approximation, determinant, or spectral bridge must pass this checklist before it enters the repo as a bridge.

```text
[ ] Parity / functional-equation symmetry is handled structurally, not cosmetically.
[ ] Order and genus match Ξ.
[ ] Counting matches Riemann–von Mangoldt T log T growth where eigenvalues are claimed.
[ ] Prime support is demonstrated through global invariants, not entry inspection alone.
[ ] Von Mangoldt weights Λ(n)/sqrt(n) appear in a trace formula or established equivalent.
[ ] Trace formula route is used; eigenvalue guessing is rejected.
[ ] Known-equivalent formulation or clearly marked conjectural bridge.
[ ] No proof language unless every equivalence step is proven.
```

### Canon status block

```text
PEAICE RIGOR GATE — V6.4.3 AUDIT PATCH

Preserved:
The corrected |m²−n²|^{-σ} kernel verifies a compact Hilbert–Schmidt threshold:
K_σ ∈ S₂ iff σ > 1/2.

Closed rigorously:
Corridor I: naive determinant closed by parity / positive odd traces.
Corridor II: z² eigenvalue route closed by counting mismatch.
Trace-class corridor: closed by genus mismatch.

Scope corrected:
Prime-support obstruction is heuristic / trace-level pressure,
not an all-orders determinant proof by itself.
Theorems C and E are first-order and do not control all p ≥ 2 cumulants.

Open computation:
Hilbert–Schmidt determinant corridor reduces to singular-value exponent:
ρ(K_σ) versus 1.

Open structural frontier:
Prime-carrying trace architecture remains open.

Computable:
Nyman–Beurling / Báez-Duarte distance problem remains the preferred RH-equivalent work package.
```

---

## 14. References to anchor before further expansion

- B. Nyman, *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*, 1950.
- A. Beurling, unpublished seminar criterion, 1955; later known through the Nyman–Beurling criterion.
- L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, Rendiconti di Matematica, 2003.
- M. V. Berry and J. P. Keating, `H = xp` and the Riemann zeros, 1999.
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Mathematica, 1999.
- A. Selberg, trace formula and Selberg zeta literature.
- A. Weil and P. Deligne, function-field RH and cohomological trace-formula framework.
- Jacobi theta / Riemann theta representation of `ζ`, used here as the audit counterexample to entrywise prime-free reasoning.

---

## 15. Final canon line

The square kernel taught us what a wall looks like, and the audit taught us how narrow the word "wall" must be. Parity closes the naive determinant, counting closes the eigenvalue route, genus closes trace-class determinants, and the Hilbert–Schmidt corridor now lives or dies by `s_n(K_σ)`.

**RH remains OPEN. Coleman Conjecture remains OPEN. No proof is claimed.**

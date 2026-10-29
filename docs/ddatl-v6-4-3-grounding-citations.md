# DDATL V6.4.3 Grounding and Citation Ledger

**Document:** `PEAICE-KAKEYALOGIC-DDATL-001`  
**Patch:** V6.4.3 Hilbert-Schmidt corridor calibration  
**Purpose:** Ground the path from the finite crossing `sigma*_N ≈ 0.83-0.92` to the analytic boundary `sigma_c = 1`, and cite the mathematical sources behind each finding.

---

## 1. Executive grounding

The V6.4.3 finding is:

```txt
0.83-0.92 = sigma*_N, a finite-window singular-value crossing
1.00      = sigma_c, the analytic Weyl / order-one boundary
```

The square-difference coupling

```txt
K_sigma(m,n) = |m^2 - n^2|^{-sigma},  m != n
```

is Hilbert-Schmidt exactly for `sigma > 1/2`. That result is a direct summability calculation on the matrix entries. The later `0.83-0.92` values come from finite truncation fits of the singular-value exponent. The analytic boundary `sigma_c = 1` comes from the leading singular-value law

```txt
s_n(K_sigma) ~ c_sigma n^{-sigma}
rho(K_sigma) = 1/sigma
```

so the order-one condition `rho(K_sigma)=1` occurs at `sigma=1`. Even at `sigma=1`, the determinant lane closes because `s_n ~ n^{-1}` produces linear determinant-zero counting, while the Riemann-von Mangoldt law requires `T log T` density.

---

## 2. Finding-by-finding provenance

### Finding A — Hilbert-Schmidt membership threshold

Claim:

```txt
||K_sigma||_HS^2 = sum_{m != n} |m^2 - n^2|^{-2 sigma}
converges <=> sigma > 1/2
```

Derivation sketch:

```txt
m^2 - n^2 = (m-n)(m+n)
```

Near the diagonal, write `m = n + d`:

```txt
|m^2 - n^2|^{-2sigma}
≈ |d|^{-2sigma}(2n)^{-2sigma}
```

The dominant comparison is therefore a product-like near-diagonal sum:

```txt
sum_n n^{-2sigma} sum_{d >= 1} d^{-2sigma}
```

which converges exactly when both factors converge, i.e. `2sigma > 1`.

Status:

```txt
FORMAL
```

Grounding source category:

```txt
Direct comparison test / Schatten S_2 definition.
```

Reference:

```txt
Barry Simon, Trace Ideals and Their Applications, 2nd ed., AMS, 2005.
Use for Schatten classes, Hilbert-Schmidt class S_2, trace-class S_1, and regularized determinants.
```

---

### Finding B — finite crossing `sigma*_N ≈ 0.83-0.92`

Claim:

```txt
sigma*_N ≈ 0.83-0.92 is a finite-window crossing, not the analytic boundary.
```

Derivation sketch:

Finite truncations fit an effective singular-value exponent:

```txt
s_n(K_sigma; N-window) ~ n^{-alpha_N(sigma)}
```

with observed structure:

```txt
alpha_N(sigma) = sigma + delta_N(sigma)
delta_N(sigma) > 0
```

Thus the finite condition

```txt
alpha_N(sigma) = 1
```

can occur before the analytic boundary:

```txt
sigma*_N = 1 - delta_N(sigma*_N)
```

This explains the observed path:

```txt
older finite window : sigma*_N ~ 0.83
later finite window : sigma*_N ~ 0.92
analytic boundary   : sigma_c = 1
```

Status:

```txt
NUMERICS / CALIBRATION
```

Grounding source category:

```txt
Internal finite-matrix diagonalization evidence; not a published theorem.
```

Citation protocol:

```txt
Cite as internal PeAIce / KakeyaLogic numerical evidence, not external mathematics.
Do not cite sigma*_N as a theorem.
```

---

### Finding C — analytic leading law `s_n(K_sigma) ~ c_sigma n^{-sigma}`

Claim:

```txt
s_n(K_sigma) ~ c_sigma n^{-sigma}
rho(K_sigma) = 1/sigma
```

Derivation sketch:

Near the diagonal:

```txt
|m^2-n^2|^{-sigma}
= |m-n|^{-sigma}(m+n)^{-sigma}
≈ |d|^{-sigma}(2n)^{-sigma}
```

Weighted Toeplitz reduction:

```txt
K_sigma ~ 2^{-sigma} D T D
D = diag(k^{-sigma/2})
T = Toeplitz convolution |m-n|^{-sigma}
```

Symbol:

```txt
a(x,xi) ~ x^{-sigma}|xi|^{sigma-1}
```

Weyl volume:

```txt
N(t) = #{s_n > t}
     ~ (1/2pi) vol{a(x,xi)>t}
     ~ C_sigma t^{-1/sigma}
```

Invert the count:

```txt
s_n ~ c_sigma n^{-sigma}
```

The same volume calculation reproduces the exact Hilbert-Schmidt threshold `sigma > 1/2`, which is the consistency check for the leading symbol.

Status:

```txt
PROPOSED -> FORMAL after Birman-Solomyak / weighted Toeplitz singular-value proof.
```

Grounding source category:

```txt
Weyl asymptotics / singular-value asymptotics for compact operators, weighted integral or pseudodifferential operators, and Birman-Solomyak-style spectral estimates.
```

References:

```txt
M. Sh. Birman and M. Z. Solomyak, spectral asymptotics / estimates of singular numbers for weakly polar integral and pseudodifferential-type operators.
Barry Simon, Trace Ideals and Their Applications, for singular values and Schatten-class language.
```

---

### Finding D — order-one boundary is `sigma_c = 1`

Claim:

```txt
rho(K_sigma)=1 <=> sigma=1
```

Derivation:

From the leading law:

```txt
s_n ~ n^{-sigma}
```

Schatten summability gives:

```txt
sum_n s_n^p ~ sum_n n^{-sigma p}
```

which converges exactly when:

```txt
sigma p > 1
```

Therefore:

```txt
rho(K_sigma) = inf{p >= 1 : sigma p > 1} = 1/sigma
```

The condition `rho(K_sigma)=1` is therefore:

```txt
1/sigma = 1  =>  sigma = 1
```

Status:

```txt
PROPOSED conditional on Finding C; algebraic after the singular-value asymptotic.
```

Reference:

```txt
Barry Simon, Trace Ideals and Their Applications, for Schatten p-summability and determinant class language.
```

---

### Finding E — determinant pincer closes the K_sigma lane

Claim:

```txt
1/2 < sigma < 1 : CLOSED by order
sigma = 1       : CLOSED by zero-density
sigma > 1       : CLOSED by genus / density
```

Reasoning:

For `sigma < 1`, the leading law gives `rho(K_sigma)>1`, so the determinant order exceeds the order-one target of `Xi`.

For `sigma = 1`, the order gate survives, but `s_n ~ n^{-1}` places determinant zeros at reciprocal singular values:

```txt
z_n ~ 1/s_n ~ n
```

so:

```txt
N_det(R) ~ R
```

The Riemann-von Mangoldt zero-counting law requires:

```txt
N_zeta(T) = T/(2pi) log(T/(2pi)) - T/(2pi) + O(log T)
```

so the density is `T log T`, not linear.

For `sigma > 1`, the leading law gives trace-class behavior and an ordinary Fredholm determinant / genus-zero lane, while `Xi` carries the Riemann-von Mangoldt density.

Status:

```txt
CLOSED-NEGATIVE for the one-parameter K_sigma determinant family.
```

References:

```txt
Riemann-von Mangoldt zero-counting formula for the T log T target.
Barry Simon, Trace Ideals and Their Applications, for determinant / trace ideal background.
```

---

### Finding F — full DDATL square-difference realization closes by Weyl class

Claim:

```txt
L^2_{Phi,K} = D_1^2 - (3/(2pi))e^{-4u}D_1 + gamma_K K_sigma
```

with `K_sigma in S_2` is a relatively compact perturbation of the `D_1^2` lane and cannot change the leading counting class:

```txt
N(Lambda) ~ Lambda^{1/4}
```

Reasoning:

`D_1 e_n = n^2 e_n`, so `D_1^2 e_n = n^4 e_n`. Therefore the unperturbed counting law is:

```txt
n^4 <= Lambda  <=>  n <= Lambda^{1/4}
```

so:

```txt
N_0(Lambda) ~ Lambda^{1/4}
```

For `sigma > 1/2`, `K_sigma in S_2`, hence compact. The perturbation does not introduce the `sqrt(Lambda) log Lambda` density required after squaring the Riemann-von Mangoldt variable.

Status:

```txt
CLOSED-NEGATIVE for D_1^2 + gamma_K K_sigma.
```

Reference category:

```txt
Compact perturbation / Weyl-class stability; direct eigenvalue-counting comparison.
```

---

### Finding G — relocation to prime-carrying trace architecture

Claim:

The live frontier requires prime-carrying data:

```txt
lengths : log(p^k)
weights : Lambda(p^k)/p^{k/2} = (log p) p^{-k/2}
density : archimedean Gamma-factor side producing T log T
reality : self-adjoint / trace-formula-compatible structure
```

Reasoning:

The square-difference kernel carries generic integer/square difference spacing. The Riemann explicit formula carries prime-power data through the von Mangoldt function. The explicit formula / trace-formula pressure is therefore prime-carrying, not square-difference-carrying.

Status:

```txt
LIVE FRONTIER / NEXT ARCHITECTURE
```

References:

```txt
Von Mangoldt function and explicit-formula role in zeta / prime-power data.
Berry-Keating / xp program for the semiclassical counting pressure.
Nyman-Beurling / Baez-Duarte criterion for an established Hilbert-space RH-equivalent pivot.
```

---

### Finding H — Slater arXiv:1007.4805 is downstream, not the Schatten input

Claim:

The phrase `Hilbert-Schmidt` appears in two different categories:

```txt
Schatten S_2 Hilbert-Schmidt class : operator singular values
Slater Hilbert-Schmidt measure     : flat Euclidean measure on density matrices
```

Slater is relevant to downstream moment and coefficient discipline, not to `rho(K_sigma)`.

Grounding:

Slater's paper explicitly uses Hilbert-Schmidt as Euclidean / flat measure on the convex body of two-rebit density matrices and studies determinant moments such as `det(rho)`, `det(rho^PT)`, and their product. The paper also develops moment computations, intermediate polynomial coefficients, root/pole structure, and asymptotic coefficient behavior that are useful as a methodological analogue for cumulant and zero-density bookkeeping.

Status:

```txt
STRUCTURAL ANALOGY / DOWNSTREAM METHODS ONLY
```

Reference:

```txt
Paul B. Slater, Hilbert-Schmidt Orthogonality of det(rho) and det(rho^PT) over the Two-Rebit Systems rho and Further Determinantal Moment Analyses, arXiv:1007.4805.
```

---

## 3. Citation table

| DDATL claim | Grounding type | Citation / source |
|---|---:|---|
| `K_sigma in S_2 iff sigma > 1/2` | Direct summability / Schatten definition | Simon, *Trace Ideals and Their Applications* |
| `sigma*_N ≈ 0.83-0.92` | Internal numerical finite-window finding | PeAIce / KakeyaLogic V6.4.2-V6.4.3 truncation runs |
| `s_n(K_sigma) ~ c_sigma n^{-sigma}` | Weyl-symbol asymptotic, proposed proof route | Birman-Solomyak-style singular-value asymptotics; Simon trace-ideal background |
| `rho(K_sigma)=1/sigma` | Algebra from singular-value law | Simon trace-ideal / Schatten p-summability framework |
| `sigma_c = 1` | Consequence of `rho=1/sigma` | Internal derivation from cited Schatten framework |
| `sigma=1 fails density` | Riemann-von Mangoldt mismatch | Riemann-von Mangoldt zero-counting formula |
| prime-carrying relocation | Explicit formula / von Mangoldt data | von Mangoldt function / explicit formula references; Berry-Keating; Nyman-Beurling / Baez-Duarte |
| Slater quarantine | Category hygiene | Slater arXiv:1007.4805 |

---

## 4. Reference list

### Trace ideals / determinant class / Schatten language

```txt
Barry Simon.
Trace Ideals and Their Applications.
2nd edition, Mathematical Surveys and Monographs, American Mathematical Society, 2005.
Use: S_p classes, Hilbert-Schmidt S_2, trace class S_1, regularized determinants.
```

### Singular-value asymptotics / Weyl-symbol route

```txt
M. Sh. Birman and M. Z. Solomyak.
Spectral asymptotics / estimates of singular numbers for weakly polar integral operators and pseudodifferential-type operators.
Use: rigorous upgrade route for the weighted Toeplitz / symbol asymptotic s_n(K_sigma) ~ c_sigma n^{-sigma}.
```

### Riemann-von Mangoldt density

```txt
Riemann-von Mangoldt formula:
N(T) = T/(2pi) log(T/(2pi)) - T/(2pi) + O(log T).
Use: zero-density obstruction; Xi requires T log T, while K_sigma power-law spectra produce pure-power or linear counts.
```

### Prime-power / explicit formula data

```txt
Von Mangoldt function:
Lambda(n) = log p if n=p^k, otherwise 0.
Use: prime-power weights Lambda(p^k)/p^{k/2}; trace architecture must carry log(p^k) lengths and von Mangoldt weights.
```

### Berry-Keating / Hilbert-Polya lane

```txt
M. V. Berry and J. P. Keating.
H = xp and the Riemann zeros / semiclassical counting program.
Use: operator-theoretic pressure point and average zero-counting connection.
```

### Nyman-Beurling / Baez-Duarte pivot

```txt
Luis Baez-Duarte.
A strengthening of the Nyman-Beurling criterion for the Riemann Hypothesis.
arXiv:math/0202141.
Use: established RH-equivalent Hilbert-space pivot; supports relocation from bespoke spectral invention to distance / Gram-matrix decay.
```

### Slater Hilbert-Schmidt measure discipline

```txt
Paul B. Slater.
Hilbert-Schmidt Orthogonality of det(rho) and det(rho^PT) over the Two-Rebit Systems rho and Further Determinantal Moment Analyses.
arXiv:1007.4805.
Use: downstream moment / coefficient / root-pole methodology; category distinction between Hilbert-Schmidt measure and Schatten S_2.
```

---

## 5. Canonical language to reuse

```txt
We did not erase 0.83. We demoted it.

0.83-0.92 is the finite-window numerical crossing sigma*_N.
1 is the analytic Weyl boundary sigma_c.
The bridge is delta_N(sigma), the finite-window correction in alpha_N(sigma)=sigma+delta_N(sigma).
As the leading asymptotic law takes over, delta_N -> 0, and the canonical crossing moves to sigma=1.

The square-difference lane closes either way:
below 1 by order,
at 1 by zero-density,
above 1 by genus / density.

The live route is prime-carrying trace architecture.
```

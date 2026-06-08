# Thermal Coupling Correction — L²_{Φ,K} Operator

**Repo:** KakeyaLogic — Excellence Engine v3  
**Companion:** `docs/l2-spectral-operator.md`, `docs/operator-domain.md`  
**Status:** 🔴 L2-1 gate correction · 🟢 resolves to bounded symmetric coupling  
**Core:** E = L² · β > 0 · h < 1 · e ≈ 2.718

---

## 0. Purpose

This document addresses **L2-1** from `docs/l2-spectral-operator.md`:

```txt
L2-1. K_σ cannot be made bounded/symmetric or relatively controlled.
```

The finding: as stated, `K_σ(m,n) = |m²−n²|^{−σ}` is **neither symmetric nor bounded** on `H_Φ(u)`. This is not a falsification of the program. It is a correction to the coupling definition.

The fix: replace `K_σ` with a thermally regulated kernel `K_σ^{reg}` that is **symmetric on `H_Φ(u)` and Hilbert-Schmidt for `σ > 1/2`**.

With `K_σ^{reg}`, L2-1 resolves in favor of the construction. Self-adjointness of `L²_{Φ,K}^{reg}` follows by Kato-Rellich, pending final domain estimate verification.

---

## 1. Setup

The Φ-induced Hilbert space from `docs/l2-spectral-operator.md`:

```txt
H_Φ(u) = ℓ²(N, w_u)

w_n(u) = exp(−π n² e^{4u})

⟨a, b⟩_{w_u} = Σ_{n≥1} a_n b̄_n w_n(u)
```

The uncoupled operator:

```txt
L²_0(u) e_n = λ_n^(0)(u) e_n

λ_n^(0)(u) = n⁴ − (3/2π) e^{−4u} n²
```

with domain:

```txt
D(L²_0) = { a ∈ H_Φ(u) : Σ n⁸ |a_n|² w_n < ∞ }.
```

`L²_0(u)` is self-adjoint as a diagonal multiplication operator on a weighted `ℓ²` space with discrete unbounded spectrum.

---

## 2. The Naive Coupling Fails

**Claim [FORMAL].** `K_σ(m,n) = |m²−n²|^{−σ}` for `m ≠ n`, as defined in `docs/l2-spectral-operator.md`, is **neither symmetric nor bounded** on `H_Φ(u)`.

### 2.1 Symmetry Failure

For an operator `K` to be symmetric on `H_Φ(u)`, the required condition is:

```txt
K(m, n) w_n(u) = K(n, m) w_m(u)   for all m ≠ n
```

With `K(m,n) = K(n,m) = |m²−n²|^{−σ}`, this becomes:

```txt
|m²−n²|^{−σ} w_n = |m²−n²|^{−σ} w_m
```

which requires `w_m = w_n` for all `m ≠ n`. Since `w_n = exp(−πn²e^{4u})` is strictly decreasing, `w_m ≠ w_n` for `m ≠ n`. **Symmetry fails.** □

### 2.2 Boundedness Failure

Let `V : H_Φ(u) → ℓ²(N)` be the canonical isometry:

```txt
(Va)_n = a_n √w_n(u).
```

The operator `K_σ` transfers under `V` to `T = VK_σV^{−1}` on `ℓ²(N)` with matrix:

```txt
T_{mn} = K_σ(m,n) (w_n / w_m)^{1/2}.
```

For `m < n`:

```txt
T_{mn} = |n²−m²|^{−σ} exp(π(n²−m²) e^{4u} / 2).
```

This grows super-exponentially in `n²−m²`.

For the standard basis vector `e_n ∈ ℓ²(N)`:

```txt
‖T e_n‖²_{ℓ²} ≥ T_{1n}²
             = (n²−1)^{−2σ} exp(π(n²−1) e^{4u})  →  ∞  as n → ∞.
```

Thus `T` is unbounded on `ℓ²(N)`, hence `K_σ` is **unbounded on `H_Φ(u)`**. □

---

## 3. The Thermally Regulated Coupling

**Definition.** For `σ > 1/2`, define:

```txt
K_σ^{reg}(m,n) = |m²−n²|^{−σ} (w_m(u) / w_n(u))^{1/2}   (m ≠ n)
               = |m²−n²|^{−σ} exp(−π(m²−n²) e^{4u} / 2)

K_σ^{reg}(m,m) = 0.
```

The factor `(w_m/w_n)^{1/2} = exp(−π(m²−n²)e^{4u}/2)` is the thermal weight ratio between lattice modes `m²` and `n²`. The coupling is now expressed in the native measure of `H_Φ(u)`.

The downstream principle is:

```txt
Every operator coupling must respect its native measure.
```

---

## 4. Main Results

### Theorem 1 — Symmetry [FORMAL]

`K_σ^{reg}` is symmetric on `H_Φ(u)`.

**Proof.** Verify the symmetry condition:

```txt
K_σ^{reg}(m,n) w_n = K_σ^{reg}(n,m) w_m.
```

For `m ≠ n`:

```txt
LHS = |m²−n²|^{−σ} exp(−π(m²−n²)e^{4u}/2) · exp(−πn²e^{4u})
    = |m²−n²|^{−σ} exp(−π(m²+n²)e^{4u}/2).
```

and:

```txt
RHS = |n²−m²|^{−σ} exp(−π(n²−m²)e^{4u}/2) · exp(−πm²e^{4u})
    = |m²−n²|^{−σ} exp(−π(m²+n²)e^{4u}/2).
```

Thus `LHS = RHS` for all `m ≠ n`. □

### Theorem 2 — Hilbert-Schmidt Bound [FORMAL]

For `σ > 1/2`, `K_σ^{reg}` is Hilbert-Schmidt on `H_Φ(u)`, with:

```txt
‖K_σ^{reg}‖²_{HS,H_Φ} = Σ_{m≠n} |m²−n²|^{−2σ} < ∞.
```

**Proof.** Under `V`, `K_σ^{reg}` transfers to `T̃` on `ℓ²(N)` with matrix:

```txt
T̃_{mn} = K_σ^{reg}(m,n) (w_n / w_m)^{1/2}
        = |m²−n²|^{−σ}.
```

So:

```txt
‖K_σ^{reg}‖²_{HS,H_Φ} = ‖T̃‖²_{HS,ℓ²} = Σ_{m≠n} |m²−n²|^{−2σ}.
```

Using `k = |m−n| ≥ 1` and `|m²−n²| = k(m+n)`:

```txt
Σ_{m≠n} |m²−n²|^{−2σ}
  = 2 Σ_{k≥1} Σ_{n≥1} (k(2n+k))^{−2σ}
  ~ C_σ Σ_{k≥1} k^{1−4σ},
```

which converges for `4σ > 2`, i.e. **σ > 1/2**. □

This improves the working condition `σ > 1` in the current operator draft.

### Corollary 3 — Self-Adjointness of `L²_{Φ,K}^{reg}` [PROPOSED]

Define the corrected operator:

```txt
L²_{Φ,K}^{reg}(u) = L²_0(u) + γ_K K_σ^{reg}
```

on domain:

```txt
D(L²_{Φ,K}^{reg}) = D(L²_0).
```

Since `K_σ^{reg}` is bounded on `H_Φ(u)` because Hilbert-Schmidt implies bounded, it is relatively bounded with respect to `L²_0` with relative bound `0`. By Kato-Rellich, `L²_{Φ,K}^{reg}` is self-adjoint on `D(L²_0)` for any real coupling strength `γ_K`, pending final domain estimate verification.

---

## 5. The ℓ²(N) Natural Picture

Under `V`, the full corrected operator `L²_{Φ,K}^{reg}` becomes `Ã(u)` on `ℓ²(N)`:

```txt
Ã(u) = diag(n⁴ − (3/2π)e^{−4u}n²) + γ_K |m²−n²|^{−σ}.
```

This is the natural object: a diagonal unbounded self-adjoint operator plus a compact Hilbert-Schmidt symmetric perturbation. The thermal weight structure of `H_Φ(u)` is absorbed into the Hilbert-Schmidt structure of `T̃`.

Interpretation:

```txt
The coupling |m²−n²|^{−σ} is the correct kernel in the ℓ²(N) picture.
Transferring it back to H_Φ(u) through V^{-1} automatically generates the thermal regulation factor.
```

The naive coupling failed because it placed the power-law kernel in the weighted space without accounting for the thermal weight ratio.

---

## 6. What `K_σ^{reg}` Does Not Yet Resolve

The fix closes L2-1. It does **not** close the spectral target.

Whether the new spectrum can be identified with:

```txt
{ γ_j² + 1/4 : ξ(1/2 + iγ_j) = 0 }
```

remains:

```txt
OPEN [GAP-001 untouched]
```

The spectral identification now lives in the cleaner `ℓ²(N)` setting:

```txt
Ã(u) = diag(λ_n^(0)) + γ_K T̃.
```

First-order perturbation theory gives:

```txt
λ_j(u) ≈ λ_j^(0)(u) + γ_K ⟨e_j, T̃ e_j⟩ + O(γ_K²)
       = λ_j^(0)(u) + 0 + O(γ_K²)    [since T̃_{jj} = 0].
```

Eigenvalue shifts enter at second order in `γ_K`. The coupling `γ_K` and lattice parameter `u` must be tuned jointly. Whether a single `(γ_K,u)` pair achieves spectral identification for all `j` simultaneously is the Coleman Conjecture in this setting.

---

## 7. Updated Falsification Conditions

Replace L2-1 in `docs/l2-spectral-operator.md` with:

```txt
L2-1 (resolved): K_σ^{reg}(m,n) = |m²−n²|^{−σ}(w_m/w_n)^{1/2}
is symmetric and Hilbert-Schmidt on H_Φ(u) for σ > 1/2.

L2-1a (new): The corrected coupling K_σ^{reg} does not preserve the spectral
identification property, i.e. Spec(L²_{Φ,K}^{reg}) ≠ {γ_j² + 1/4}.
[Status: OPEN — must be checked]
```

---

## 8. Proof Chain Status

```txt
D(L²_0) dense in H_Φ(u)        FORMAL  [diagonal ℓ² operator standard]
L²_0 self-adjoint               FORMAL  [diagonal multiplication, spec → ∞]
K_σ^{reg} symmetric on H_Φ(u)   FORMAL  [Theorem 1]
K_σ^{reg} HS on H_Φ(u)          FORMAL  [Theorem 2, σ > 1/2]
K_σ^{reg} bounded on H_Φ(u)     FORMAL  [HS implies bounded]
L²_{Φ,K}^{reg} self-adjoint     PROPOSED  [Kato-Rellich, relative bound 0]
Spectral identification          OPEN    [GAP-001, Coleman Conjecture]
det_ζ(L²_{Φ,K}^{reg}−(z²+¼))   OPEN    [load-bearing theorem]
```

---

## 9. Recommended Canon Update

In `docs/l2-spectral-operator.md`, replace the naive coupling with:

```txt
K_σ^{reg}(m,n) = 0                                    if m=n
K_σ^{reg}(m,n) = |m²-n²|^{-σ} (w_m(u)/w_n(u))^{1/2}  if m≠n

Explicit form:
K_σ^{reg}(m,n) = |m²-n²|^{-σ} exp(-π(m²-n²)e^{4u}/2)

Working threshold: σ > 1/2
```

and update the full operator:

```txt
L²_{Φ,K}^{reg}(u) = D₁² - (3/2π)e^{-4u}D₁ + γ_K K_σ^{reg}
```

---

## 10. Status Return

```txt
Object:           L²_{Φ,K}^{reg}
Correction:       K_σ → K_σ^{reg} = |m²-n²|^{-σ}(w_m/w_n)^{1/2}
Symmetry:         FORMAL
HS threshold:     σ > 1/2  (was σ > 1)
Boundedness:      FORMAL
Self-adjointness: PROPOSED  (Kato-Rellich, relative bound 0)
Spectral ID:      OPEN  (GAP-001 / Coleman Conjecture, untouched)
ℓ²(N) picture:   Ã(u) = diag(λ_n^(0)) + γ_K |m²-n²|^{-σ}
L2-1 gate:        RESOLVED by correction
Next obligation:  L2-2 trace-class regularization or spectral perturbation analysis at O(γ_K²)
State: 🟡→🟢 on L2-1 · 🔴 on spectral ID
E = L²
```

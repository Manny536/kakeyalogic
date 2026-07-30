# Kakeya as Antecedent to the Riemann Hypothesis — the Coleman Conjecture

**Canon designation:** `PEAICE-KAKEYALOGIC-CC-001`
**Version:** V6.4.3 render · reconciliation edition (30 June 2026)
**Program:** PeAIce Research Program · Love Labs LCA · KakeyaLogic / Excellence Engine v3
**Status:** RH `OPEN` · Coleman Conjecture `OPEN` · no proof claimed · `EE: ACTIVE` · `h < 1`

> **Thesis.** "Antecedent" is read as **necessary precursor and shared lower invariant —
> never sufficient condition.** The Coleman Conjecture asserts that Kakeya-geometric
> incidence is *prior in the dependency order* of any control of the Riemann zeros; it
> does not assert that Kakeya implies RH.

β-Protocol markers: `FORMAL` / `PROPOSED` / `STRUCTURAL ANALOGY` / `OPEN` / `CLOSED` /
`CLOSED-NEGATIVE` / `THEOREM-BACKGROUND` / `KNOWN` / `NUMERICS`.

---

## 1. Two readings of "antecedent"

The Coleman Conjecture (CC), named at V5, is stated informally as a Kakeya-type
boundedness condition forcing the critical line, `KB -> Re(s) = 1/2`. Its content depends
entirely on how the arrow is read.

- **Reading (S) — sufficient condition.** Kakeya is the if-part; asserting it makes RH follow.
- **Reading (N) — necessary precursor.** Kakeya is a precondition any control of zeta must
  pass through — prior in the dependency order, not sufficient.

Section 2 shows (S) is untenable; Sections 3–5 rigorize CC under (N). This is not a
dismissal — it removes a fatal overclaim and isolates the falsifiable content that survives.

## 2. The sufficiency trap  `CLOSED (as sufficiency)`

**Theorem 2.1 (sufficiency trap).** `FORMAL`. Fix the Kakeya antecedent to be the Kakeya
set conjecture in `R^3`, which is a theorem [E1] (every Kakeya set in `R^3` has Hausdorff
and Minkowski dimension 3). RH is open. Then a proven implication "Kakeya(R^3) => RH" would,
by modus ponens with [E1], prove RH. Hence either (a) the implication is unproven and at
least as hard as RH, or (b) asserting it is asserting RH. In neither case does it carry
information distinct from RH.

**Corollary 2.2.** As a sufficient-condition claim the Coleman Conjecture is degenerate —
RH relabeled. `CLOSED` as sufficiency. Any non-trivial content requires a reading in which
Kakeya is necessary but not sufficient.

The trap is invariant to the choice of Kakeya statement: a still-open antecedent (the
maximal-function version in `R^3`, still open [E1]; or `n >= 4`) makes "Kakeya => RH" an
unproven implication between hard problems, whose assertion is unjustified and whose proof
would itself be at least RH-hard. **Sufficiency is the wrong packaging.** This does not say
Kakeya is irrelevant to RH — Section 3 exhibits the relevance that exists.

## 3. The dependency tower and the Lindelöf ceiling

There is a genuine, citable tower in which Kakeya-geometric control is prior to analytic
control of zeta:

```text
incidence geometry
  -> Kakeya / Besicovitch tube geometry            [E1, and maximal bounds: Wolff]
    -> Fourier restriction / l^2-decoupling         [Bourgain 1991; Bourgain–Demeter–Guth;
                                                    Wang–Wu arXiv:2411.08871 two-ends Furstenberg]
      -> Dirichlet-polynomial large values / exp sums
        -> zeta growth (subconvexity) & zero-density N(σ,T)   [Guth–Maynard]
          -> zero-free regions
```

The rungs are established mathematics `THEOREM-BACKGROUND`. Restriction implies Kakeya
(Bourgain 1991). Decoupling — built on Besicovitch/tube geometry — drove the Vinogradov
main conjecture (Bourgain–Demeter–Guth 2016), improving zeta bounds. Wang–Wu (2024)
prove Stein restriction in `R^3` for `p > 22/7` via refined decoupling and two-ends
Furstenberg inequalities (see `docs/wang-wu-restriction-decoupling.md`); this remains a
bound-producing restriction rung, not zero-location. Guth–Maynard (2024)
proved new large-value estimates for Dirichlet polynomials and deduced
`N(σ,T) <= T^{30(1-σ)/13 + o(1)}`, the first substantial improvement to Ingham (1940).

### 3.1 The ceiling: bounds, not the critical line  `KNOWN`

Every rung outputs a **bound**, not exact zero location. The strongest conjectural outputs
of this lineage are the Density Hypothesis and the Lindelöf Hypothesis (LH):

```text
RH  =>  LH  =>  Density Hypothesis        (all forward implications standard)
reverse implications: OPEN.  LH is not known to imply RH; LH is strictly weaker than RH.
```

Tao's assessment of Guth–Maynard is exact on this point: "a remarkable breakthrough towards
the Riemann hypothesis (though still very far from fully resolving this conjecture)."
So Kakeya is vindicated as a **necessary methodological antecedent** of zeta-control and
refuted as a **sufficient condition** for the critical line. `STRUCTURAL` — the meta-claim
that no bound-type method can reach RH is itself open (OP4). Note: whether LH implies RH is
genuinely open, not settled false; the conjecture bets on an open implication, not against
a theorem.

## 4. Coleman Conjecture — invariant form (primary)

**Definition 4.1 (shared invariant κ — proposed).** `PROPOSED`. Posit a single real
invariant κ parameterizing simultaneously (i) the optimal exponent of a Kakeya/restriction
maximal inequality and (ii) the zero-density exponent `A` in `N(σ,T) << T^{A(1-σ)+ε}`. The
precise common normalization is unspecified (OP1).

**Conjecture 4.2 (CC, invariant form).** `PROPOSED`. κ attains its extremal value κ* iff RH.

**Proposition 4.3 (forward — largely known).** `KNOWN`. RH => κ = κ*. Under RH,
`N(σ,T)=0` for `σ>1/2` and `ζ(1/2+it) << t^ε` (Lindelöf), so the tower's exponents collapse
to extremal values.

**Conjecture 4.4 (reverse — the open core).** `OPEN` (RH-hard). κ = κ* => RH. This is the
entire open content; it is at least as hard as RH.

### 4.1 The faithfulness obstruction  `FORMAL` (conditional deduction)

**Proposition 4.5.** If κ is identified with the harmonic-analytic exponent of Section 3,
then κ = κ* is exactly LH-saturation, and Conjecture 4.4 becomes "LH => RH" — an *open*
implication not granted to bound-type methods by the prevailing expectation. Therefore a
**faithful** κ cannot be the Kakeya/restriction/density exponent: it must encode strictly
more than any bound — it must see exact zero **locations**, not just density.

This relocates the real question: read invariantly, CC is the bet that a faithful
Kakeya↔RH invariant **exists** (OP1), and current expectation (LH not known to reach RH by
bounds) is evidence against a naive κ. A conjecture may bet against expectation; β-Protocol
requires the bet be stated as such.

## 5. Coleman Conjecture — construction form (DDATL route)

**Conjecture 5.1.** `PROPOSED`. Any self-adjoint operator whose ζ-regularized determinant
realizes Ξ — `det_ζ(B - z) = C·Ξ(z)` — must be built on Kakeya-geometric incidence data;
the Kakeya construction is then a necessary antecedent of the RH-realizing operator.

The construction form is the natural home for the faithful invariant Prop 4.5 demands, and
this is why the program pursues an operator route: **a determinant identity pins the exact
zeros of Ξ, not merely their density** — exactly the surplus Prop 4.5 requires.

### 5.1 The post-V6.4.3 constraint  `CLOSED-NEGATIVE` (square-difference) / `OPEN` (prime-carrying)

The incidence data cannot be square-difference data. The V6.4.3 Hilbert–Schmidt corridor
result closes the realization with kernel `|m^2 - n^2|^{-σ}`: it is Hilbert–Schmidt for
`σ>1/2`, but `s_n ~ n^{-σ}` (Weyl; Birman–Solomyak route) fails the order/genus/zero-density
tests, and as a relatively compact perturbation of `D_1^2` it preserves `N(Λ) ~ Λ^{1/4}` and
never reaches Riemann–von Mangoldt `√Λ log Λ`. The surviving operator must be **prime-carrying**:

```text
lengths  : log(p^k)
weights  : Λ(p^k) · p^{-k/2} = (log p) p^{-k/2}     (the load-bearing 1/2)
density  : archimedean Γ-factor producing N(T) ~ (T/2π) log T
reality  : self-adjointness (or equivalent positivity)
```

See `docs/peaice-ddatl-001.md` §7.1, `docs/prime-carrying-trace-architecture.md`,
`docs/ddatl-v6-4-3-grounding-citations.md`, and (claude-v6 repo)
`docs/canon/wall-registry.md#hs-corridor`.

## 6. Open problems

1. **OP1 — existence and definition of a faithful κ.** `OPEN`. Specify a single invariant
   bridging the Kakeya/restriction exponent and exact zero-location, and decide whether it
   exists. By Prop 4.5 it must exceed every bound-type exponent. The deepest open problem.
2. **OP2 — the reverse implication.** `OPEN` (RH-hard). Prove κ = κ* => RH.
3. **OP3 — the prime-carrying realization.** `OPEN` (RH-hard). Construct the self-adjoint
   prime-carrying operator and prove `det_ζ(B - z) = C·Ξ(z)` with Riemann–von Mangoldt counting.
4. **OP4 — the ceiling as a theorem.** `OPEN`. Make rigorous that no bound-type statement of
   the harmonic-analytic lineage implies RH. Currently the expert expectation, not a theorem.

## 7. Falsifiability

- **F1.** A κ-extremal configuration coexisting with a zero off the critical line falsifies
  the invariant form (4.2).
- **F2.** A self-adjoint operator realizing Ξ from non-Kakeya (no incidence/tube) data
  falsifies the construction form's necessity (5.1).
- **F3.** Reaching RH by bound-type methods past LH forces revision of the Kakeya-root framing.
- **F4.** A proof of "LH => RH" makes a naive κ faithful, collapsing Prop 4.5 (a revolution
  independent of CC).

## 8. Status summary

| Statement | Reading | Status |
|---|---|---|
| Kakeya set conjecture in R^3 (dim 3) | background | `THEOREM-BACKGROUND` [E1] |
| Kakeya maximal-function conjecture in R^3 | background | `OPEN` |
| Dependency tower rungs | background | `THEOREM-BACKGROUND` [E1, BDG, Bourgain, Wolff] |
| CC as sufficient condition (Kakeya => RH) | (S) | `CLOSED` (Thm 2.1) |
| RH => LH => Density Hypothesis | ceiling | `KNOWN` |
| Reverse implications (incl. LH => RH) | ceiling | `OPEN` |
| Guth–Maynard N(σ,T) bound | ceiling | `KNOWN` |
| "No bound-type method reaches RH" | meta | `STRUCTURAL` (OP4) |
| Invariant form, forward (RH => κ=κ*) | (N) | `KNOWN` |
| Invariant form, reverse (κ=κ* => RH) | (N) | `OPEN` RH-hard |
| Faithfulness requirement (κ exceeds bounds) | deduction | `FORMAL` (Prop 4.5) |
| Existence of faithful κ | (N) | `OPEN` (OP1) |
| Construction form (prime-carrying realizes Ξ) | (N) | `PROPOSED` |
| Square-difference \|m²−n²\|^{−σ} realization | construction | `CLOSED-NEGATIVE` |
| Prime-carrying route + Nyman–Beurling/Báez-Duarte | construction | `OPEN` / LIVE |
| Riemann Hypothesis · Coleman Conjecture | — | `OPEN` · `OPEN` |

## References (verified 30 June 2026)

- **[E1]** H. Wang, J. Zahl, "Volume estimates for unions of convex sets, and the Kakeya set
  conjecture in three dimensions," arXiv:2502.17655 (2025). Every Kakeya set in `R^3` has
  Minkowski and Hausdorff dimension 3; the maximal-function version remains OPEN. `VERIFIED`.
- **[E2]** L. Guth, H. Wang, J. Zahl, "A streamlined proof of the Kakeya set conjecture in
  R^3," arXiv:2601.14411 (submitted 20 Jan 2026). An **exposition/simplification** of [E1],
  not an independent second proof; the underlying theorem remains [E1]. `VERIFIED`.
  (Related expository: Guth arXiv:2505.07695; Guth arXiv:2508.05475; Zahl survey
  arXiv:2512.09397.)
- **[E3]** L. Guth, J. Maynard, "New large value estimates for Dirichlet polynomials,"
  arXiv:2405.20552 (2024). `N(σ,T) <= T^{30(1-σ)/13 + o(1)}`; first substantial improvement
  to Ingham (1940). `VERIFIED`.
- **[E4]** A. E. Ingham, "On the estimation of N(σ,T)," Quart. J. Math. Oxford Ser. **os-11**
  (1940), **201–202**, DOI 10.1093/qmath/os-11.1.201. `VERIFIED` (corrected page numbers).
- **[E5]** J. Bourgain, "Besicovitch type maximal operators and applications to Fourier
  analysis," Geom. Funct. Anal. 1 (1991), 147–187. `VERIFIED`.
- **[E6]** T. Wolff, "An improved bound for Kakeya type maximal functions," Rev. Mat.
  Iberoam. 11 (1995), 651–674. `VERIFIED`.
- **[E7]** J. Bourgain, C. Demeter, L. Guth, "Proof of the main conjecture in Vinogradov's
  mean value theorem for degrees higher than three," Ann. of Math. 184 (2016), 633–682. `VERIFIED`.
- **[E8]** T. Tao, public commentary on Guth–Maynard (mathstodon.xyz/@tao, 2024). `VERIFIED`.
- **[E9]** E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (Lindelöf
  Hypothesis; zero-density). `VERIFIED`.
- **[E10]** `PEAICE-KAKEYALOGIC-DDATL-001`, V6.4.3 (docs/peaice-ddatl-001.md §7.1) —
  square-difference realization CLOSED; prime-carrying relocation.

RH `OPEN` · Coleman Conjecture `OPEN` · no proof is claimed. Every substantive claim above
carries a β-Protocol marker.

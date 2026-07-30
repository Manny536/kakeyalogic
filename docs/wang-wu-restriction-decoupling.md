# Wang–Wu Restriction / Two-Ends Furstenberg

**Repo:** KakeyaLogic — Excellence Engine v3  
**Status:** 🟢 KNOWN external grounding · 🔴 RH / spectral identification open  
**Designation:** `PEAICE-KAKEYALOGIC-REF-WW-001`  
**Claim discipline:** `h < 1` · RH OPEN · Coleman OPEN · citation does not upgrade program bridges to FORMAL

## Bibliographic identity

| Field | Value |
|---|---|
| Title | Restriction Estimates Using Decoupling Theorems and Two-Ends Furstenberg Inequalities |
| Authors | Hong Wang, Shukun Wu |
| arXiv | [2411.08871v3](https://arxiv.org/abs/2411.08871) · math.CA · 19 Dec 2024 |
| BibTeX key | `WangWu2024Restriction` · `arxiv/bibliography/peaice-arxiv.bib` |
| Grounding table | Block E · `arxiv/bibliography/grounding-register.md` |
| Local PDF (not in git) | `Downloads/Research/Math-References/restrictionestimatesusingdecoulpingtheorems.pdf` |
| Downstream twin | `Manny536/claude-v6` · `docs/research/wang-wu-restriction-decoupling.md` |

## Summary

Wang–Wu attack Stein’s Fourier restriction / extension conjecture by combining:

1. **Oscillation tools** — refined decoupling (Bourgain–Demeter line; GIOW / Du–Zhang refinement) and induction on scales.  
2. **Incidence tools** — two-ends Furstenberg inequalities for tube–ball incidences under two-ends shadings.

Headline KNOWN facts:

```txt
n = 3: restriction for p > 22/7
plane: two-ends Furstenberg ⇒ typical multiplicity M(Q) ≲ m λ^{−1/2}
Conjecture 0.9 (higher-d two-ends Furstenberg) ⇒ full restriction
high d: restriction for p > (154n+6)/(77n−95)
n = 3 numerology: p > 22/7  ↔  Kakeya Hausdorff dim ≥ 5/2 (Wolff hairbrush)
```

## Imported vocabulary

```txt
E_S                  Fourier extension operator on hypersurface S
R-tubes              R^{1/2} × ⋯ × R wave-packet supports
Y(T), λ              shading of a tube and its density
two-ends             shading mass on both ends of each tube
M(Q)                 tube multiplicity on an R^{1/2}-ball
refined decoupling   control of ‖E_S f‖_{L^p(X)} by M and m
hairbrush            Wolff structure used for the n=3 lift
```

## Role in KakeyaLogic / L²_C

```txt
GBZ probe (Kakeya set geometry in R³)
  + Wang–Wu (restriction incidence + decoupling)
  = geometric / harmonic-analysis pressure language

Does NOT supply:
  prime-carrying lengths/weights
  T log T density carrier
  μ(placement) → ζ-zero location operator
  RH or Coleman closure
```

Companion anchors:

- [`guth-wang-bateman-zahl-probe.md`](guth-wang-bateman-zahl-probe.md) — Kakeya R³ spine  
- [`coleman-conjecture-antecedent.md`](coleman-conjecture-antecedent.md) — dependency tower honesty  
- [`kns-light-basic.md`](kns-light-basic.md) — typed incidence (program side)  

## Firewall

```txt
KNOWN: restriction exponents, two-ends Furstenberg plane theorem, Kakeya dim numerology
PROPOSED / OPEN (program): any map from placement grammar to zero location
CLOSED-NEGATIVE (literature): peer-reviewed Kakeya/restriction → ζ zero-counting bridge
```

Register date: 2026-07-30 · twin registration with `Manny536/claude-v6`.

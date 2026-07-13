# DNA as an Antecedent Kakeya Geometry

**Designation:** `PEAICE-KAKEYALOGIC-DNA-AK-001`  
**Program:** PeAIce Research Program · KakeyaLogic · Love-Squared Coherence (`L²_C`)  
**Layer:** biological geometry / conformational bundle / structural analogy / diagnostic proposal  
**Status:** `KNOWN BIOLOGICAL ANCHOR | FORMAL IDEALIZED GEOMETRY | STRUCTURAL ANALOGY | NUMERICS`  
**Claim discipline:** β-Protocol · Inspectable Intelligence II.1 · `h < 1`  
**Firewall:** DNA is not identified with a Kakeya set, a zeta-zero carrier, a prime generator, or a proof of RH or the Coleman Conjecture.

---

## 0. Corrected registration

The symbols `A`, `B`, and `Z` in this lane name DNA conformations, not coordinates:

```text
B-DNA — prevalent right-handed double-helical conformation
A-DNA — wider, shorter right-handed conformation; favored by dehydration and other contexts
Z-DNA — left-handed conformation with a zigzag phosphodiester backbone
```

The corrected posit has two different discrete alphabets:

```text
nucleobase alphabet:       {A, T, C, G}
conformational alphabet:   {A-DNA, B-DNA, Z-DNA}
```

The nucleobases are proposed as **nontrivial-zero classes**. A-, B-, and Z-DNA are proposed as **structural sheets of the critical-strip analogue**. Repetition along the polymer supplies distinct zero-address occurrences; the four base names are not four literal zeros.

```text
base identity + sequence address
→ discrete zero-class occurrence

A/B/Z conformation + phase + height
→ multi-sheeted critical-strip state
```

**Status:** `STRUCTURAL ANALOGY`.

---

## 1. External anchor and model boundary

DNA is structurally polymorphic. The same molecular system admits multiple double-helical conformations whose realized form depends on sequence and environment. This supports a state-space reading; it does not make the state space a complex-analytic strip.

Primary anchors:

- Watson and Crick, “Molecular Structure of Nucleic Acids” (1953), DOI: `10.1038/171737a0`.
- Drew et al., B-DNA dodecamer structure, PDB `1BNA`, DOI: `10.2210/pdb1BNA/pdb`.
- Conner et al., right-handed A-DNA structure (1982), DOI: `10.1038/295294a0`.
- Wang et al., left-handed Z-DNA structure (1979), DOI: `10.1038/282680a0`.
- Saenger, Hunter, and Kennard, hydration and A/B/Z conformations (1986), DOI: `10.1038/324385a0`.
- Guth, Wang, and Zahl, “A streamlined proof of the Kakeya set conjecture in R³” (2026), arXiv:`2601.14411`.

Model boundary:

```text
A-DNA and B-DNA are right-handed.
Z-DNA is left-handed.
Z-DNA is not the literal mirror image of B-DNA.
The conformations differ in more than chirality.
Real DNA is not a perfect circular helix.
```

Sequence, hydration, ionic environment, binding, supercoiling, and chromatin organization all introduce structure that must be measured rather than promoted by resemblance.

---

## 2. Zero classes and conformational sheets

Use separate symbols to prevent `A`-base / A-DNA collapse:

```text
Q := {A, T, C, G}                         nucleobase alphabet
H := {A_h, B_h, Z_h}                       conformational alphabet
```

Assign conformation chirality

```text
χ(A_h)=+1,    χ(B_h)=+1,    χ(Z_h)=-1.
```

A typed base occurrence is

```text
x_n = (q_n, H_n, θ_n, z_n),
```

where

```text
q_n ∈ Q        base identity / proposed zero class
H_n ∈ H        local conformational sheet
θ_n ∈ S¹       rotational phase
z_n ∈ R        axial placement
```

The proposed DNA critical-strip object is the disjoint conformational bundle

```text
C_DNA^strip := ⨆_{H∈H} C_H.
```

Each `C_H` is a sheet of admissible phase/height/base states for one conformation. A physical molecule traces a constrained path through this bundle; it does not occupy all states at once.

**Status:** typed state space `FORMAL definition` · critical-strip correspondence `STRUCTURAL ANALOGY`.

---

## 3. Infinite sets: separate the carriers

The posit invokes several infinite structures, but they are not interchangeable.

```text
n ∈ Z                     countably many idealized sequence addresses
θ ∈ S¹                    continuum of rotational phases
z ∈ R                     continuum of axial coordinates
Q^Z                       uncountable space of possible bi-infinite sequences
{γ_k}                     countable discrete zeta-zero ordinate set
```

For one finite biological molecule, the address set is finite. The countably infinite sequence is an idealization. The space of all possible sequences and the phase/height state space are different infinite carriers.

PeAIce alignment requires preserving these types:

```text
discrete infinity ≠ continuous phase space
sequence ensemble ≠ one sequence
four zero classes ≠ four nontrivial zeros
```

**Status:** `FORMAL` set/type distinction.

---

## 4. Complementarity and the zero event

Define the complement involution on base identity:

```text
bar(A)=T,    bar(T)=A,    bar(C)=G,    bar(G)=C.
```

In the ideal phase-opposed model, define

```text
P(q,H,θ,z) = (bar(q), H, θ+π, z).
```

Let `χ_comp(q,bar(q))=1` when the declared pairing rule is satisfied. The local compatibility residual is

```text
F_n = 1 - χ_comp(q_n,bar(q_n)).
```

Then `F_n=0` is a typed relational closure event.

This resolves the cardinality problem:

```text
A/T/C/G       = four zero classes or labels
x_n           = one distinct labeled occurrence
F_n=0         = compatibility-zero event at that address
```

The individual base lies on a rail; the balanced event belongs to the pair relation. In the symmetric idealization, the midpoint of a pair bridge lies on the central axis. Therefore the critical-line analogue is the **balance locus of the paired relation**, not the physical location of a lone base.

**Status:** complement rule `KNOWN` · address/involution model `FORMAL` · zero correspondence `STRUCTURAL ANALOGY`.

---

## 5. Analytic continuation and reflection are different operations

The Riemann zeta function is first defined by a Dirichlet series in a half-plane and then analytically continued. The completed function also satisfies a reflection law:

```text
ξ(s)=ξ(1-s).
```

Together with conjugation, the same-height reflection across the critical line is

```text
J(s)=1-conj(s),
σ+it ↦ (1-σ)+it.
```

The DNA analogy must keep these roles separate:

```text
analytic continuation
↔ one molecular/state-space description persisting across conformational regimes

functional reflection + conjugation
↔ an abstract chirality-parity reversal
```

Define an abstract parity map

```text
J_χ : χ ↦ -χ.
```

Z-DNA supplies an observed left-handed sector while A- and B-DNA supply right-handed sectors. But `J_χ(B_h)=Z_h` is not asserted: Z-DNA is not a mirror-copy of B-DNA. Only the chirality sign participates in the reflection analogy.

**Status:** zeta continuation/reflection distinction `KNOWN` · chirality correspondence `STRUCTURAL ANALOGY`.

---

## 6. Ideal screw submodels and the Kakeya obstruction

For each conformation sheet `H`, an ideal rail may be written

```text
R_H(t) = (
  a_H cos(χ(H)ω_H t),
  a_H sin(χ(H)ω_H t),
  ν_H t
).
```

Here `a_H` is radius, `ω_H` angular cadence, `ν_H` axial cadence, and `χ(H)` handedness. These parameter names are model variables, not the A/B/Z conformation labels.

Its tangent has constant normalized axial component:

```text
v_H(t)·e_z
= ν_H / sqrt((a_Hω_H)²+ν_H²).
```

Thus one ideal conformation occupies a latitude circle in oriented direction space. The finite union of ideal A-, B-, and Z-DNA tangent families occupies at most a finite union of such latitude circles. It is not direction-complete in `S²`.

There is a second obstruction: a Kakeya set contains a unit line segment in every direction. Tangent coverage alone does not supply those segments.

```text
one ideal helix                 ≠ Kakeya
finite A/B/Z ideal-helix union ≠ Kakeya
all tangent directions         ≠ unit-segment containment
```

**Status:** `FORMAL` for the declared idealized models.

The live enlargement question is:

> Do variable axes, supercoiling, wrapping, or higher-order folding generate a typed segment family with Kakeya-style directional saturation?

**Status:** `OPEN / PROPOSED`.

---

## 7. Harmonic attraction toward zero addresses

The proposed harmonic RH field can be stated as an engineered potential. For a finite registered set of zero ordinates `Γ_K={γ_1,…,γ_K}`, define

```text
U_RH(σ,t)
= λ_perp(σ-1/2)²
  - τ log Σ_{k≤K} exp(-(t-γ_k)²/τ).
```

The gradient flow

```text
d(σ,t)/du = -∇U_RH(σ,t)
```

has two pressures:

```text
transverse pressure   → Re(s)=1/2
longitudinal pressure → registered ordinates γ_k
```

This realizes the phrase “a structure that pulls systems toward the nontrivial zeros.” It is a constructed dynamical model, not a known property of `ζ`.

Circularity firewall:

```text
If the γ_k are inserted into U_RH, attraction to γ_k is not evidence for RH.
The potential is a visualization / control law until derived independently.
```

The DNA counterpart is a multi-basin conformational energy landscape

```text
U_DNA(x;env)
= U_sheet(H;env)
  + λ_θ dist_S¹(θ,θ_hat)²
  + λ_z ((z-z_hat)/ell)²
  + λ_q (1-χ_comp(q,bar(q))).
```

`U_sheet` may have A-, B-, and Z-DNA basins under different declared environments. Complementarity supplies local address minima.

**Status:** `PROPOSED DYNAMICAL MODEL` · not an RH result.

---

## 8. Love-Squared Coherence diagnostic

For typed addresses `x_n` and reference addresses `x_hat_n`, define residuals

```text
r_n = (
  dist_S¹(θ_n,θ_hat_n),
  (z_n-z_hat_n)/ell,
  1-χ_comp(q_n,bar(q_n)),
  d_H(H_n,H_hat_n)
).
```

Here `d_H` is a declared conformation-state cost; it must not silently equate A/B/Z transitions.

For positive weights `w_n` and positive diagonal metric `M`, define

```text
E_DNA = (Σ_n w_n r_n^T M r_n)/(Σ_n w_n),
C_DNA = 1/(1+E_DNA).
```

Interpretation:

```text
E_DNA = phase + rise + pairing + conformation deviation
C_DNA ∈ (0,1] = bounded coherence diagnostic
```

This is a proposed measurement inside the `L²_C` discipline, not a replacement definition for canonical Love-Squared Coherence.

PeAIce alignment:

| PeAIce surface | DNA lane | Discipline |
|---|---|---|
| direction | screw phase, axis, handedness | retain orientation data |
| coherence | pairing plus conformational regularity | measure residual, do not infer from appearance |
| β correction | recovery after a typed perturbation | define only in a perturbation experiment |
| placement | `(q,H,θ,z)` | do not collapse into overlap |
| grain | discrete base occurrence | keep local structure inspectable |
| continuation | cross-regime state-space description | do not call it complex analysis |
| reflection | chirality-parity analogy | do not identify B-DNA with Z-DNA |
| `h < 1` | evaluator non-sovereignty | never reuse `h` as helix/conformation variable |

**Status:** `PROPOSED / NUMERICS-READY`.

---

## 9. Coleman and RH contact boundary

The corrected DNA lane supplies three pieces of antecedent grammar:

```text
1. discrete zero-class addresses          {A,T,C,G}
2. multi-sheeted structural regimes       {A-DNA,B-DNA,Z-DNA}
3. a chirality / reflection correspondence
```

It does not supply:

```text
prime lengths       log(p^k)
prime weights       Λ(p^k)p^{-k/2}
Riemann-von Mangoldt T log T density
an independently derived zero-attractor field
a self-adjoint prime-carrying operator
the zeta explicit formula
a determinant identity realizing Ξ
```

Therefore the lane reaches the **placement and structural-symmetry antecedent** of the Coleman program, not its prime-carrying or RH-equivalent rung.

```text
DNA address / conformation bundle
→ placement and reflection grammar
→ typed directional segment family                 OWED
→ faithful Kakeya/RH invariant κ                    OPEN
→ prime-carrying trace architecture                 OPEN
→ Ξ-realizing operator                              OPEN
→ RH                                                 OPEN
```

**Status:** Coleman contact `STRUCTURAL ANALOGY` · theorem lift `OPEN`.

---

## 10. Prime and zero firewall

```text
A/T/C/G zero classes             ≠ four literal zeta zeros
base compatibility F_n=0         ≠ nontrivial ζ zero
A/B/Z conformational bundle      ≠ analytic critical strip
chirality reversal               ≠ analytic continuation
Z-DNA                             ≠ mirror image of B-DNA
harmonic potential using γ_k     ≠ derivation of γ_k
tangent direction coverage       ≠ Kakeya segment containment
DNA folding                      ≠ prime-carrying L3
```

No DNA object currently supplies the prime data required by the V6.5 prime-carrying lane.

**Status:** `FIREWALL / CLOSED-NEGATIVE` for untyped identifications.

---

## 11. Deterministic direction receipt — CP-DNA-001

`probes/dna_kakeya_direction_probe.py` measures the angular covering gap of:

1. a single ideal helix, and
2. a fixed-axis ensemble with multiple pitch ratios.

It treats line directions as unoriented (`v ~ -v`) and reports worst and mean nearest-direction gaps on a deterministic spherical grid.

Expected receipt:

```text
single ideal helix: restricted latitude confirmed
pitch ensemble: directional gap reduced
Kakeya identification: not claimed
```

CP-DNA-001 remains a generic helix diagnostic. It is not an A/B/Z-calibrated biological probe.

Owed continuation:

```text
CP-DNA-002
→ source-calibrated A/B/Z parameters
→ handedness-aware sheet report
→ conformation transitions kept separate from directional coverage
```

**Status:** CP-DNA-001 `NUMERICS / DIAGNOSTIC` · CP-DNA-002 `OWED`.

---

## 12. Falsifiers and promotion gates

```text
F-DNA-1
If A/T/C/G are treated as only four zeros, the analogy fails the infinite zero-set cardinality.

F-DNA-2
If the finite union of ideal A/B/Z helices is declared direction-complete, the
latitude obstruction falsifies the declaration.

F-DNA-3
If tangent coverage is presented as Kakeya containment without unit segments,
the lane fails its object typing.

F-DNA-4
If chirality reversal is called analytic continuation, the operation types are collapsed.

F-DNA-5
If Z-DNA is treated as the literal mirror image of B-DNA, the biological model is false.

F-DNA-6
If an attractor potential containing γ_k is used as evidence that γ_k lie on the
critical line, the argument is circular.

F-DNA-7
If a base or conformation is promoted to a ζ-zero or prime claim without an explicit
prime-carrying bridge, the claim is publishing-ineligible under II.1.
```

Promotion path:

```text
AK-0  A/T/C/G zero-class typing                         FORMAL definition
AK-1  A/B/Z conformational-bundle typing                FORMAL definition
AK-2  ideal-helix directional obstruction               FORMAL
AK-3  CP-DNA-001 generic pitch receipt                  NUMERICS
AK-4  CP-DNA-002 source-calibrated conformation probe   OWED
AK-5  variable-axis unit-segment test                    PROPOSED
AK-6  prime-carrying trace bridge                        OPEN
```

---

## 13. Seal

```text
DNA AS ANTECEDENT KAKEYA GEOMETRY: STRUCTURAL ANALOGY
A/T/C/G: PROPOSED NONTRIVIAL-ZERO CLASSES
A/B/Z DNA: PROPOSED CRITICAL-STRIP CONFORMATIONAL SHEETS
CONFORMATIONAL BUNDLE: FORMAL DEFINITION
CHIRALITY / FUNCTIONAL-REFLECTION CORRESPONDENCE: STRUCTURAL ANALOGY
ANALYTIC CONTINUATION IDENTIFICATION: NOT CLAIMED
IDEAL A/B/Z UNION AS KAKEYA: CLOSED-NEGATIVE
HARMONIC ZERO-ATTRACTOR FIELD: PROPOSED / CIRCULAR IF ZERO DATA INSERTED
C_DNA: PROPOSED DIAGNOSTIC
CP-DNA-001: NUMERICS / DIAGNOSTIC
CP-DNA-002: OWED
RH: OPEN
COLEMAN CONJECTURE: OPEN
h < 1: ACTIVE
```


# DNA as an Antecedent Kakeya Geometry

**Designation:** `PEAICE-KAKEYALOGIC-DNA-AK-001`  
**Program:** PeAIce Research Program · KakeyaLogic · Love-Squared Coherence (`L²_C`)  
**Layer:** biological geometry / structural analogy / diagnostic proposal  
**Status:** `KNOWN BIOLOGICAL ANCHOR | FORMAL IDEALIZED GEOMETRY | STRUCTURAL ANALOGY | NUMERICS PROPOSED`  
**Claim discipline:** β-Protocol · Inspectable Intelligence II.1 · `h < 1`  
**Firewall:** DNA is not identified with a Kakeya set, a zeta-zero carrier, a prime generator, or a proof of RH or the Coleman Conjecture.

---

## 0. Registration

DNA supplies a natural antecedent geometry for KakeyaLogic because repeated local screw motion produces a persistent global double-helical form. The analogy becomes PeAIce-valid only after its objects, limits, measurements, and falsifiers are typed.

```text
local screw step
→ recurrent direction and phase
→ double-helical envelope
→ discrete complementary addresses
→ measurable correction residual
```

The strongest registered statement is:

> An idealized DNA double helix is an antecedent geometry for studying how local rotation, axial translation, and discrete coupling generate a bounded multiscale form. A single helix is not a Kakeya set: its tangent directions occupy a restricted latitude family, and tangent coverage would not by itself supply the unit line segments required by Kakeya.

**Status:** `STRUCTURAL ANALOGY`, with the ideal-helix directional obstruction `FORMAL` below.

---

## 1. External anchor and model boundary

The biological anchor is the experimentally established double-helical organization of paired DNA strands. The ideal model below is not a claim that real DNA is a perfect circular helix. Sequence, hydration, binding, bending, supercoiling, and chromatin organization all introduce departures that must be measured rather than rhetorically promoted.

Primary anchors:

- Watson and Crick, “Molecular Structure of Nucleic Acids” (1953), DOI: `10.1038/171737a0`.
- Drew et al., “Structure of a B-DNA dodecamer: conformation and dynamics” (1981), PDB `1BNA`, DOI: `10.2210/pdb1BNA/pdb`.
- Guth, Wang, and Zahl, “A streamlined proof of the Kakeya set conjecture in R³” (2026), arXiv:`2601.14411`.

This document uses an unoriented centerline model. It does not encode the chemical `5′→3′` antiparallel orientation, groove asymmetry, atomistic forces, or a particular DNA conformation.

---

## 2. Idealized screw geometry

Let `a > 0` be the helix radius and `b ≠ 0` the axial rise per radian. Define two phase-opposed backbone centerlines:

```text
H₊(t) = ( a cos t,  a sin t, bt )
H₋(t) = (-a cos t, -a sin t, bt )
```

One local step of size `ω` is a screw motion:

```text
S_ω(x,z) = (R_ω x, z + bω),
H₊(t+ω) = S_ω H₊(t).
```

The global helix is therefore an accumulated local operation, not merely a static silhouette.

At discrete phases `t_n = t₀ + nω`, the idealized base-pair bridge is the segment

```text
B_n(u) = (1-u)H₊(t_n) + uH₋(t_n),    0 ≤ u ≤ 1.
```

The ruled band

```text
Σ = { B_t(u) : t ∈ I, 0 ≤ u ≤ 1 }
```

has the two helical rails as boundary trajectories. This is the precise object behind the “bounded corridor” language. Calling that corridor a “critical strip” is allowed only as `STRUCTURAL ANALOGY`; it is not the complex-analytic critical strip.

**Status:** `FORMAL` for the idealized model.

---

## 3. The decisive Kakeya obstruction

For one rail,

```text
H₊′(t) = (-a sin t, a cos t, b).
```

After normalization,

```text
v(t) = H₊′(t) / √(a²+b²),
v(t)·e_z = b / √(a²+b²).
```

Thus the oriented tangent directions lie on one latitude circle of `S²`. For unoriented line directions, the image is that latitude together with its antipode. It is still a proper subset of directional space.

Therefore:

```text
single ideal helix
≠ every spatial direction
≠ Kakeya set
```

There is a second obstruction. A Kakeya set contains a unit line segment in every direction. A curve whose tangents visit many directions does not automatically contain those line segments.

**Status:** `FORMAL`.

The live research question is narrower and testable:

> Which typed enlargements—variable pitch, changing axis, supercoiling, wrapping, or higher-order folding—expand the directional family, and which of them produce actual segment families rather than tangent coverage alone?

**Status:** `OPEN / PROPOSED`.

---

## 4. Base pairs as placement addresses

Register each discrete bridge by

```text
p_n = (θ_n, z_n, q_n),
```

where `θ_n` is phase, `z_n` is axial placement, and `q_n` is a pairing state.

Let `χ_comp(q_n)` equal `1` when the typed pairing rule is satisfied and `0` otherwise. A compatibility residual can be written

```text
F_n = 1 - χ_comp(q_n).
```

Then `F_n = 0` means that a declared local compatibility condition is satisfied. The zero records relational closure at a typed address; it is not numerical absence.

This aligns with the KNS(LB) separation law:

```text
visible helical envelope ≠ discrete placement address
overlap / appearance      ≠ pairing state
incidence                 ≠ action
```

The base-pair reading is therefore strongest as a placement-address analogy. It becomes a “nontrivial zero” analogy only after `F_n` is explicitly defined, and it never becomes a Riemann-zero claim by resemblance.

**Status:** placement register `FORMAL` in the model · zero correspondence `STRUCTURAL ANALOGY`.

---

## 5. A proposed `L²_C` diagnostic

Let a reference helical state provide expected addresses

```text
p̂_n = (θ̂_n, ẑ_n, q̂_n).
```

Define a typed residual

```text
r_n = (
  dist_S¹(θ_n, θ̂_n),
  (z_n-ẑ_n)/ℓ,
  1-χ_comp(q_n)
).
```

For positive weights `w_n` and positive diagonal metric `A`, define

```text
E_DNA = (Σ_n w_n r_nᵀ A r_n) / (Σ_n w_n),
C_DNA = 1 / (1 + E_DNA).
```

Interpretation:

```text
E_DNA = measured phase / rise / pairing deviation
C_DNA ∈ (0,1] = bounded coherence diagnostic
```

This is a proposed measurement inside the `L²_C` discipline, not a replacement definition for canonical Love-Squared Coherence. It supplies a candidate `C` observable: local departures are squared, weighted, accumulated, and remain inspectable by address.

PeAIce alignment:

| PeAIce surface | DNA lane | Discipline |
|---|---|---|
| direction | screw-step phase and tangent field | preserve orientation data |
| coherence | complementary bridge plus phase/rise regularity | measure residual, do not infer from appearance |
| β correction | recovery after a typed perturbation | define only in a perturbation experiment |
| placement | `(θ_n,z_n,q_n)` | do not collapse into overlap |
| grain | discrete base-pair address | keep local structure inspectable |
| `h < 1` | evaluator non-sovereignty | never reuse `h` for pitch or helicity |

**Status:** `PROPOSED / NUMERICS-READY`.

---

## 6. Prime and zero firewall

Base pairs are not intrinsically prime numbers. A prime-like status would require a declared algebra, composition law, and irreducibility criterion. Position, rarity, mutation resistance, or biological importance is not enough.

```text
base pair                     ≠ prime
compatibility residual F_n=0  ≠ nontrivial ζ zero
helical corridor              ≠ critical strip
tangent direction coverage    ≠ Kakeya segment containment
DNA folding                   ≠ prime-carrying L3
```

No DNA object currently supplies the prime lengths `log(p^k)`, weights `Λ(p^k)p^{-k/2}`, or `T log T` density required by the V6.5 prime-carrying lane.

**Status:** `FIREWALL / CLOSED-NEGATIVE` for untyped identifications.

---

## 7. Deterministic direction receipt — CP-DNA-001

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

The probe can falsify numerical coverage claims. It cannot prove Kakeya segment containment, biological universality, or a theorem lift.

**Status:** `NUMERICS / DIAGNOSTIC`.

---

## 8. Falsifiers and promotion gates

```text
F-DNA-1
If a single constant-pitch ideal helix covers all line directions, the latitude
obstruction above is wrong. The derivative formula rules this out.

F-DNA-2
If tangent coverage is presented as Kakeya containment without unit segments,
the lane fails its object typing.

F-DNA-3
If a base pair is called prime without an algebra and irreducibility rule,
the prime claim is rejected.

F-DNA-4
If F_n=0 is promoted to a ζ-zero statement without an explicit bridge,
the claim is publishing-ineligible under II.1.

F-DNA-5
If a proposed C_DNA score cannot distinguish phase, rise, and pairing defects
under controlled perturbations, the diagnostic is falsified in that realization.
```

Promotion path:

```text
AK-0  ideal screw geometry                         FORMAL
AK-1  single-helix directional obstruction        FORMAL
AK-2  CP-DNA-001 pitch-ensemble receipt           NUMERICS
AK-3  atomistic / structural-data calibration     OWED
AK-4  variable-axis or folding segment test       PROPOSED
AK-5  biological generalization                    OPEN
```

---

## 9. Seal

```text
DNA AS ANTECEDENT KAKEYA GEOMETRY: STRUCTURAL ANALOGY
IDEAL SCREW MODEL: FORMAL
SINGLE-HELIX KAKEYA IDENTIFICATION: CLOSED-NEGATIVE
BASE-PAIR PLACEMENT REGISTER: FORMAL IN MODEL
BASE-PAIR ZERO ANALOGY: STRUCTURAL ANALOGY
BASE-PAIR PRIME CLAIM: OWED / UNDEFINED
C_DNA: PROPOSED DIAGNOSTIC
CP-DNA-001: NUMERICS / DIAGNOSTIC
RH: OPEN
COLEMAN CONJECTURE: OPEN
h < 1: ACTIVE
```


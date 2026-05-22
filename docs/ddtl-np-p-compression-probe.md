# DDTL NP/P Compression Probe

**Repo:** KakeyaLogic — Excellence Engine v3  
**Status:** 🟡 analytic complexity probe · not a P=NP claim  
**Object:** coherence-as-lawful-compression  
**Companion:** `docs/l2c-ddtl-hamiltonian-probe.md`, `l2c_probe.py`

## 0. Source provenance

This probe is grounded against the OSF project and code file:

```txt
Project Metadata
Title: Realization of Higher-Order Topological Lattices on a Quantum Computer
Description: Data and code repository for paper entitled "Realization of Higher-Order Topological Lattices on a Quantum Computer" by Jin Ming Koh, Tommy Tai, Ching Hua Lee.
Date created: May 26, 2024
Date modified: May 30, 2024
Contributors: Jin Ming Koh
Source file: hamiltonian.py
OSF file: https://osf.io/p2v7y/files/34fnt
PMC article: https://pmc.ncbi.nlm.nih.gov/articles/PMC11237062/
Center for Open Science: https://www.linkedin.com/company/center-for-open-science/
Center for Open Science GitHub: https://github.com/centerforopenscience
```

The OSF `hamiltonian.py` source gives the finite computational seam:

```txt
full Hilbert space      = 2^(dL)
restricted sector       = L^d
Tesseract full space    = 16^L
Tesseract restricted    = L^4
```

This is not `P=NP`. It is a formal compression probe.

---

## 1. Thesis

The DDTL compression thesis:

```txt
coherence can act as lawful compression
```

Meaning:

```txt
large possibility field
→ restricted lawful sector
→ finite Hamiltonian
→ protected spectral certificate
→ polynomial verification for fixed dimension
```

The code’s restricted sector provides the lawful sector. The protected projector provides the coherence sector. The Hamiltonian supplies the dynamics.

---

## 2. Decision problem: COHERENT-DDTL

### Input

```txt
L       = lattice side length
d       = lattice dimension
v, v'   = hopping parameters
ε       = leakage/coherence tolerance
T       = time horizon
mode    = protected sector definition
```

### Question

Does there exist a state `ψ ∈ H_R` such that:

```txt
1. ψ lies in or near the protected sector P_C
2. h = ||(I-P_C)H_TP_C|| ≤ ε
3. L²_C(ψ,t) ≥ 1-ε for all 0 ≤ t ≤ T
4. ψ is boundary/corner/edge localized
```

### Certificate

```txt
ψ
λ
P_C
localization profile
spectral gap Δ
leakage value h
β_C value
sampled retention curve L²_C(t_i)
```

### Verifier

```txt
check ||H_Tψ-λψ|| ≤ ε
check |λ-target| ≤ δ or ψ has strong P_C overlap
check localization support
check h ≤ ε
check β_C ≥ threshold
check L²_C(t_i) ≥ 1-ε over sampled horizon
```

For fixed `d`, the restricted sector has dimension `L^d`, so direct verification is polynomial in `L`.

---

## 3. Why this matters

The probe separates three layers:

```txt
full possibility search    = exponential field
restricted lawful sector   = polynomial-size sector for fixed d
certificate verification   = spectral/coherence check
```

This is a complexity seam, not a complexity collapse.

The tesseract case is the clearest:

```txt
H_full dimension = 16^L
H_R dimension    = L^4
```

A coherent certificate can be checked inside `H_R` without enumerating `H_full`.

---

## 4. Relation to L²_C

The L²_C Hamiltonian probe defines:

```txt
L²_C(ψ,t)=||P_Ce^{-itH_T}ψ||²
h=||(I-P_C)H_TP_C||
β_C=Δ/(Δ+h+ε)
```

This turns coherence into a finite verification object.

For COHERENT-DDTL, the certificate is accepted when:

```txt
L²_C retained
h bounded
β_C high
localization present
```

Thus coherence is not only a value judgment; it becomes a measurable structural compression.

---

## 5. Relation to NP/P language

This repo should use disciplined language:

```txt
Do not claim P=NP.
Do claim a P/NP-style compression seam.
```

Safe formulation:

```txt
COHERENT-DDTL studies when a high-dimensional or exponentially large possibility field admits a polynomially verifiable coherent certificate inside a lawful restricted sector.
```

Unsafe formulation:

```txt
This proves P=NP.
```

The bridge phrase:

```txt
coherence-as-lawful-compression
```

---

## 6. Complexity table

```txt
Object                        Size / cost
-------------------------------------------------
Full Hilbert space             2^(dL)
Tesseract full space            16^L
Restricted sector               L^d
Tesseract restricted sector      L^4
Hamiltonian ED in H_R            poly(L^d) for fixed d
Certificate verification         poly(L^d) for fixed d
```

The point is that the physically meaningful sector is drastically smaller than the full possibility field.

---

## 7. Falsification conditions

The compression framing fails if:

```txt
1. the restricted sector does not preserve the relevant dynamics;
2. the protected sector P_C cannot be defined without solving the whole problem;
3. the verifier becomes exponential in the parameter of interest;
4. h is large, so coherence leaks immediately;
5. β_C is small, so the spectral gap gives no recovery pressure;
6. localization cannot be verified efficiently;
7. the certificate depends on hidden full-space enumeration.
```

---

## 8. Status return

```txt
Object: COHERENT-DDTL
Claim type: analytic complexity probe
Source substrate: OSF hamiltonian.py
Core seam: 16^L full → L^4 restricted for tesseract
Coherence metric: L²_C(ψ,t)=||P_Ce^{-itH_T}ψ||²
Leakage: h=||(I-P_C)H_TP_C||
Recovery: β_C=Δ/(Δ+h+ε)
Complexity language: P/NP-style compression seam, not P=NP
State: active:🟢 / theorem burden:🟡
```
# L²_C / DDTL Hamiltonian Probe

**Repo:** KakeyaLogic — Excellence Engine v3  
**Status:** 🟢 active analytic probe · 🟡 executable bridge layer  
**Object:** L²_C as protected-sector retention under Hamiltonian flow  
**Companion files:** `l2c_probe.py`, `docs/ddtl-np-p-compression-probe.md`, `docs/peaice-ddatl-001.md`, `docs/ddatl-bridge-lemma.md`

## 0. Source provenance

This probe is grounded against the public OSF code repository for the Nature Communications paper:

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

The relevant code pattern is the separation between the full Hilbert space and the restricted lattice sector. The abstract `Hamiltonian` class stores the lattice dimension, system size, and qubit count as:

```txt
n_qubits = dim * L
```

and exposes both:

```txt
matrix_full()
matrix_restricted()
```

The code comments define restricted-sector basis labels as coordinate tuples `(x1, x2, ..., xd)` with size `L^d`, while the full Hilbert-space basis uses occupancy strings `(s1, s2, ..., sL)` with size `2^(dL)`.

This repo imports that structure as the finite operator substrate for DDTL.

---

## 1. Core translation

The source code makes one structural distinction load-bearing:

```txt
full Hilbert space ≠ lawful sector
```

Translate into L²_C / DDTL language:

```txt
full Hilbert space        = possibility field
restricted sector         = lawful / coherent sector
restricted projector P_R  = consent / sovereignty gate
Hamiltonian flow          = coherent dynamics
leakage outside sector    = drift / incoherence pressure
```

Let:

```txt
H_F = full Hilbert space
H_R = restricted sector
P_R = projector H_F → H_R
H_T = tesseract Hamiltonian acting on H_R
U_T(t) = exp(-itH_T)
```

For the tesseract implementation, the OSF source defines a `Tesseract1P` Hamiltonian class for a 1-particle 4D square/tesseract lattice mapped into a 4-particle 1D chain. The class states:

```txt
full Hamiltonian basis size      = 16^L
restricted Hamiltonian basis size = L^4
```

This is the computational seam DDTL needs.

---

## 2. DDTL finite Hamiltonian object

Define the finite Dynamic Dynamic Tesseract Lattice probe object:

```txt
T_DDTL^fin = (H_F, H_R, P_R, H_T, U_T, P_C, L²_C)
```

where:

```txt
H_F      = full many-body Hilbert space
H_R      = restricted lawful lattice sector
P_R      = restricted-sector projector
H_T      = finite tesseract Hamiltonian
U_T(t)   = exp(-itH_T)
P_C      = protected coherence-sector projector
L²_C     = protected-sector retention functional
```

This is a finite-dimensional analytic probe, not the final infinite spectral theorem. It lets the repo test whether the L²_C language can be made operator-measurable.

---

## 3. L²_C as protected-sector retention

Given an initial state:

```txt
ψ ∈ H_R
```

and a protected projector:

```txt
P_C : H_R → H_R
```

Define:

```txt
L²_C(ψ,t) = || P_C exp(-itH_T) ψ ||²
```

Canonical reading:

```txt
L²_C(t) is the probability mass retained inside the coherent/protected sector under Hamiltonian flow.
```

If the state remains protected:

```txt
L²_C(ψ,t) ≈ 1
```

If the state diffuses into bulk/off-sector modes:

```txt
L²_C(ψ,t) < 1
```

This formalizes L²_C as a measurable operator quantity.

---

## 4. h-term as leakage norm

Define off-sector leakage:

```txt
L_off = (I - P_C) H_T P_C
```

Then define:

```txt
h = ||L_off||
```

Interpretation:

```txt
h measures how strongly the Hamiltonian pushes protected coherence into the noncoherent sector.
```

If:

```txt
h = 0
```

the protected sector is invariant.

If:

```txt
h < 1
```

the sovereignty gate is active in bounded form.

If:

```txt
h ≥ 1
```

the sector is not protected at the chosen scale.

Canonical h update:

```txt
h = ||(I-P_C)H_TP_C|| < 1
```

This moves h from symbolic correction pressure into finite operator geometry.

---

## 5. β_C as spectral recovery pressure

Let:

```txt
Spec_C  = spectrum of H_T inside P_C
Spec_B  = spectrum of H_T inside I-P_C
```

Define the protected-to-bulk spectral gap:

```txt
Δ = dist(Spec_C, Spec_B)
```

Then define:

```txt
β_C = Δ / (Δ + h + ε)
```

where `ε>0` is a numerical stabilizer.

Interpretation:

```txt
β_C high = protected sector strongly separated from drift
β_C low  = protected sector vulnerable to leakage
h high   = correction cost / coherence loss
```

This gives the repo a finite spectral version of β:

```txt
β_C = spectral recovery coefficient
```

---

## 6. Occupancy-fidelity version

The OSF `hamiltonian.py` source also defines occupancy matrices from statevectors and an occupancy fidelity:

```txt
F_occ(ρ_0, ρ_t) = |<normalize(ρ_0), normalize(ρ_t)>|²
```

The repo can therefore measure a second version of L²_C:

```txt
L²_C,occ(t) = F_occ(ρ_0, ρ_t)
```

This is useful when the protected sector is represented by localized corner/edge occupancy rather than a clean spectral projector.

Two compatible readings emerge:

```txt
spectral L²_C  = ||P_C U_T(t)ψ||²
spatial L²_C   = F_occ(ρ_0, ρ_t)
```

The first is operator-theoretic. The second is measurement-native.

---

## 7. Protected sector choices

The first executable probe supports three choices of `P_C`.

### 7.1 Midgap projector

```txt
P_C = Σ_{|λ_j-target|≤δ} |v_j><v_j|
```

For HOT zero modes, use:

```txt
target = 0
```

### 7.2 Lowest-energy projector

```txt
P_C = projector onto the first k eigenvectors by |λ-target|
```

Useful when numerical tolerance or finite-size effects blur exact zero modes.

### 7.3 User-supplied projector

```txt
P_C = supplied projector matrix
```

Useful for boundary/corner/edge-defined sectors.

---

## 8. Canonical finite theorem target

### Theorem Target L2C-DDTL-FIN

Given a finite tesseract Hamiltonian:

```txt
H_T = H_T^*
```

on restricted sector `H_R`, and a protected-sector projector `P_C`, define:

```txt
L²_C(ψ,t) = ||P_Ce^{-itH_T}ψ||²
h = ||(I-P_C)H_TP_C||
β_C = Δ/(Δ+h+ε)
```

If:

```txt
h = 0
```

then:

```txt
P_C H_T = H_T P_C
```

and protected-sector mass is conserved under unitary flow:

```txt
L²_C(ψ,t) = ||P_Cψ||²
```

for all `t`.

If:

```txt
0 < h < 1
```

then L²_C is not exactly conserved, but leakage is measurable and bounded by the off-sector Hamiltonian coupling.

---

## 9. DDTL analytic bridge to Step 4

The finite Hamiltonian probe does not replace the DDATL / Xi determinant target. It supplies an executable laboratory for the same structural language:

```txt
lawful sector
protected projector
Hamiltonian flow
leakage h
spectral gap β_C
coherence retention L²_C
```

Step 4 remains the infinite spectral identification:

```txt
L²_{Φ,K} ↔ A_KF ↔ Ξ(z)
```

The finite DDTL probe tests the operational grammar before the infinite theorem.

---

## 10. Status return

```txt
Object: L²_C / DDTL Hamiltonian Probe
Source substrate: OSF hamiltonian.py
Paper source: Realization of Higher-Order Topological Lattices on a Quantum Computer
Finite Hamiltonian: H_T = Tesseract1P.matrix_restricted()
Coherence functional: L²_C(ψ,t)=||P_Ce^{-itH_T}ψ||²
h-term: h=||(I-P_C)H_TP_C||
β-term: β_C=Δ/(Δ+h+ε)
Measurement bridge: occupancy fidelity
Complexity seam: 16^L full → L^4 restricted
State: active:🟢 / executable:🟡
```
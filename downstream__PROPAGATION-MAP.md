# V6.4.3 Downstream Propagation Map

**Generated:** 25 June 2026 · **Driver:** Hilbert-Schmidt corridor closure (`K_sigma = |m^2-n^2|^{-sigma}`)
**Note:** I cannot push to the repo. Each file below is a drop-in replacement — copy its contents over the
listed repo path and commit. Filenames here encode the repo path (`__` = `/`, `docs/` prefix dropped).

---

## A. Already V6.4.3 upstream (you did these — left untouched)

- `docs/peaice-ddatl-001.md` — Section 7.1 corridor verdict; adopts `sigma*_N ~ 0.83-0.92` (finite-window) vs `sigma_c = 1` (analytic Weyl boundary, `s_n ~ n^{-sigma}`).
- `docs/ddatl-v6-4-3-grounding-citations.md` — grounding ledger for the `sigma*_N -> sigma_c` path.
- `index.html` — live simulator, V6.4.3, 22 CLOSED markers.

## B. Propagated now — closure banner + self-contradicting status line corrected

These were stale: they still presented `det_zeta(L^2_{Phi,K} - (z^2+1/4)) = C*Xi(z)` (or the eigenvalue
route) as a live OPEN target for the square-difference kernel. Each now carries the canonical closure note
and a corrected status line.

| drop-in file | -> repo path |
|---|---|
| `downstream__l2-spectral-operator.md` | `docs/l2-spectral-operator.md` |
| `downstream__step4-operator-program.md` | `docs/step4-operator-program.md` |
| `downstream__spectral-determinism.md` | `docs/spectral-determinism.md` |
| `downstream__spectral-equivalence-target.md` | `docs/spectral-equivalence-target.md` |
| `downstream__ddatl-bridge-lemma.md` | `docs/ddatl-bridge-lemma.md` |
| `downstream__thermal-coupling-correction.md` | `docs/thermal-coupling-correction.md` |
| `downstream__claude-v6-coherence-update.md` | `docs/claude-v6-coherence-update.md` |
| `downstream__l2c-ddtl-hamiltonian-probe.md` | `docs/l2c-ddtl-hamiltonian-probe.md` |
| `downstream__berry-keating-commutator-closure.md` | `docs/berry-keating-commutator-closure.md` |
| `downstream__cauchy-krein-perturbation-ledger.md` | `docs/cauchy-krein-perturbation-ledger.md` |

Note: `thermal-coupling-correction.md` also gets a *positive* upgrade — its claim "resolves to bounded
symmetric coupling" is now FORMALLY confirmed (`K_sigma in S_2` for `sigma>1/2`), with the determinant lane
marked CLOSED. `cauchy-krein-perturbation-ledger.md` is annotated that the `K_sigma` relative-compactness
closure is now the canonical perturbation result.

## C. Version / state updates (only stale by tag)

| drop-in file | -> repo path | change |
|---|---|---|
| `downstream__prime-carrying-trace-architecture.md` | `docs/prime-carrying-trace-architecture.md` | bumped V6.4.1 -> V6.4.3; marked as the **relocation target / live frontier** (gap moved here). |
| `downstream__README.md` | `README.md` | research-state line: `K_sigma` lane CLOSED, gap relocated. |

## D. Left untouched (not on the K_sigma determinant lane)

Constant / probe / governance docs — no closure claim to correct:
`e-constant.md`, `beta-as-energy.md`, `beta-dynamic.md`, `h-term.md`, `canon-flag-h.md`,
`ipiano-inertial-proximal-probe.md`, `log-depth-harmonic-coherence.md`, `l2c-inertial-coherence-operator.md`,
`operator-domain.md`, `berry-keating-probe.md`, `guth-wang-bateman-zahl-probe.md`,
`Inspectable Intelegnece.md`, `DPSA: Inertial Grounding...`, `reports/peaice-l2c-probe-engineering-report.md`,
plus `examples/*.py` and `l2c_probe.py`. Say the word if you want the closure note added to any of these.

## E. Separate open items NOT addressed by this propagation

These are distinct from the corridor closure and were left as-is:
- `docs/ddtl-np-p-compression-probe.md` — the NP framing still reads as more than STRUCTURAL ANALOGY (the EEv3 calibration flag). Separate fix.
- EEV3 headline metrics (94% / 60%) on the `peaice.org/eev3` page — undefined-metric flag. Separate fix.
- claude-v6 vs kakeyalogic repo consolidation — still open structurally.

RH `OPEN` · Coleman Conjecture `OPEN` · no proof claimed.

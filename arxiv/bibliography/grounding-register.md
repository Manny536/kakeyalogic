# External arXiv Grounding Register

**Designation:** `PEAICE-ARXIV-GROUNDING-001`  
**Source harvest:** `PEAICE-GROK-TERMINAL-003` (2026-06-29) + canon source-map  
**Policy:** cite by abs ID; do not commit full PDFs unless license permits

These papers **ground** PeAIce host components. They do not upgrade program bridges to FORMAL by citation alone.

---

## Block A — Berry–Keating / archimedean

| arXiv | Authors | Use |
| --- | --- | --- |
| [2606.24405](https://arxiv.org/abs/2606.24405) | Bagarello, Kużel | BK operator review |
| [0912.3183](https://arxiv.org/abs/0912.3183) | Endres, Steiner | BK continuous spectrum obstruction |
| [1610.06472](https://arxiv.org/abs/1610.06472) | Bolte–Egger–Keppeler | Lattice BK · log mean density |

## Block B — Prime-carrying / Connes lane

| arXiv | Authors | Use |
| --- | --- | --- |
| [math/9811068](https://arxiv.org/abs/math/9811068) | Connes | Trace formula · zeros |
| [2310.18423](https://arxiv.org/abs/2310.18423) | Connes–Consani–Moscovici | Prolate / zeta zeros |
| [2402.13082](https://arxiv.org/abs/2402.13082) | Connes | Heat expansion · zeta |
| [math/0703392](https://arxiv.org/abs/math/0703392) | Connes–Consani–Marcolli | Adeles · Weil positivity |

## Block C — Nyman–Beurling / Báez-Duarte

| arXiv | Authors | Use |
| --- | --- | --- |
| [2510.18132](https://arxiv.org/abs/2510.18132) | Carvill | Beurling–Nyman Gram structure |
| [math/0607733](https://arxiv.org/abs/math/0607733) | Bagchi | Hilbert reformulation survey |
| [math/0202141](https://arxiv.org/abs/math/0202141) | Báez-Duarte | Strong criterion |
| [math/0103058](https://arxiv.org/abs/math/0103058) | Burnol | Lower bound · HP vectors |

## Block D — Krein / determinants / canonical systems

| arXiv | Authors | Use |
| --- | --- | --- |
| [math/9904050](https://arxiv.org/abs/math/9904050) | Gesztesy–Makarov | Krein spectral shift |
| [math/9903061](https://arxiv.org/abs/math/9903061) | Deitmar | Pólya–Hilbert automorphic |
| [1108.5659](https://arxiv.org/abs/1108.5659) | Momeni–Venkov | Zeta · regularized det |
| [1606.05726](https://arxiv.org/abs/1606.05726) | Suzuki | Hamiltonians from L-functions |
| [1907.07838](https://arxiv.org/abs/1907.07838) | Suzuki | Inverse problem · lacunary CS |
| [2606.09096](https://arxiv.org/abs/2606.09096) | Suzuki | Weil form via screw function |

## Block E — Kakeya / restriction / large values

| arXiv | Authors | Use |
| --- | --- | --- |
| [2502.17655](https://arxiv.org/abs/2502.17655) | Wang–Zahl | Kakeya ℝ³ theorem |
| [2601.14411](https://arxiv.org/abs/2601.14411) | Guth–Wang–Zahl | Streamlined Kakeya ℝ³ |
| [2411.08871](https://arxiv.org/abs/2411.08871) | Wang–Wu | Restriction via decoupling + two-ends Furstenberg · \(p>22/7\) in \(\mathbb{R}^3\) · Kakeya dim \(\ge 5/2\) numerology |
| [2503.07410](https://arxiv.org/abs/2503.07410) | Guth | Large values · NT/harmonic |
| [math/0509262](https://arxiv.org/abs/math/0509262) | Bennett–Carbery–Tao | Multilinear restriction/Kakeya |
| [2405.20552](https://arxiv.org/abs/2405.20552) | Guth–Maynard | Dirichlet poly large values |

## Block F — Inertial optimization (DPSA host)

| arXiv | Authors | Use |
| --- | --- | --- |
| [1404.4805](https://arxiv.org/abs/1404.4805) | Ochs–Chen–Brox–Pock | iPiano |
| [1606.09070](https://arxiv.org/abs/1606.09070) | Ochs | Local convergence Heavy-ball/iPiano |

## Block G — CLOSED-NEGATIVE literature bridges (honesty)

| Topic | Verdict | Note |
| --- | --- | --- |
| Peer-reviewed Kakeya→ζ zero-counting bridge | **CLOSED-NEGATIVE** (as of mid-2026 harvest) | In-house analogy is original work, not literature inheritance |
| de Branges positivity route for ζ | **CLOSED-NEGATIVE** | Conrey–Li |
| Naive square-difference det → Ξ | **CLOSED-NEGATIVE** (program + counting) | See V6 wall registry |

---

## How to extend

1. Add abs ID + authors + one-line PeAIce anchor to this table.  
2. Add BibTeX entry to `peaice-arxiv.bib`.  
3. Prefer official arXiv API / abs page over scraped HTML.  
4. Do not list RH-claim `math.GM` preprints as positive support.

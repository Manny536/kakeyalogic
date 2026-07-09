# PeAIce arXiv Lane

**Designation:** `PEAICE-ARXIV-LANE-001`  
**Host repo:** `Manny536/kakeyalogic`  
**Program:** PeAIce / KakeyaLogic / L²_C / Excellence Engine v3  
**Principal:** Manuel Coleman  
**Governance:** β-Protocol · II.1 (`PEAICE-II-CANON-001`) · `h < 1`  
**Stance:** receipts over reach · no self-certifying closure · RH OPEN · Coleman OPEN

This directory is the **submit-facing build tree** for PeAIce mathematical notes intended for [arXiv.org](https://arxiv.org). It is separate from internal whitepapers, Fable terminals, and GitHub Pages landings.

```txt
Internal canon  →  arxiv/manuscripts/*  →  PDF + source  →  arXiv submission
     (docs/)           (this tree)           (tools/)        (human account)
```

---

## 0. What this lane is (and is not)

| Is | Is not |
| --- | --- |
| LaTeX/metadata shells for public math notes | A claim that RH or Coleman is proved |
| Bibliography + grounding register | A dump of copyrighted PDFs |
| Series map with claim tags | Automatic promotion of every PeAIce file to arXiv |
| Submission checklist under II discipline | Self-certification by a model or webpage |

**II rule:** a manuscript is arXiv-eligible only if every load-bearing claim is tagged (`FORMAL` / `PROPOSED` / `OPEN` / `CLOSED-NEGATIVE` / `STRUCTURAL ANALOGY` / `NUMERICS`) and no OPEN target is asserted closed.

---

## 1. Directory map

```txt
arxiv/
  README.md                          ← this file
  SUBMISSION-CHECKLIST.md            ← pre-flight for each upload
  series/
    00-series-map.md                 ← planned notes, priority, categories
  bibliography/
    peaice-arxiv.bib                 ← BibTeX (external + self)
    grounding-register.md            ← arXiv abs IDs mapped to PeAIce lanes
  templates/
    peaice-amsart.tex                ← article class shell
    claim-discipline.tex             ← macros for status tags / firewalls
  manuscripts/
    ddatl-002-grain-zero/            ← Note 001 · first build (priority)
    kns-lb/                          ← Note 002 · typed object paper
  tools/
    README.md                        ← install TeX / build commands
    build.sh                         ← local PDF build when TeX present
```

---

## 2. Recommended arXiv categories

Primary and cross-list choices are **proposal only** until endorsement/account setup is complete.

| Manuscript family | Primary | Cross-list (optional) |
| --- | --- | --- |
| Grain Zero / Kakeya residual | `math.CA` or `math.MG` | `math.CO` |
| KNS(LB) typed incidence object | `math.CA` / `math.MG` | — |
| Operator / spectral shift notes | `math.SP` / `math.NT` | `math-ph` |
| II / governance (if ever) | **not** pure-math first | cs.AI only if rewritten for that venue |

Use arXiv’s current category guide at submission time. Do **not** use `math.GM` for PeAIce load-bearing notes unless the note is explicitly recreational/unconventional and you accept that framing.

---

## 3. First-wave series (build order)

| ID | Working title | Status | Source corpus |
| --- | --- | --- | --- |
| **ARX-001** | Grain Zero residual after Kakeya factorization in ℝ³ | Scaffold | `docs/whitepapers/ddatl-002-grain-zero-whitepaper.md` |
| **ARX-002** | KakeyaNeedleSet(Light(Basic)): typed object and two-layer decomposition | Scaffold | `PEAICE-CLAUDEV6-KNS-LB-PAPER-001` |
| **ARX-003** | Trace-neutral Kakeya operator and closed square-difference lanes | Planned | claude-v6 Theorems A–H + wall registry |
| **ARX-004** | Prime-carrying trace architecture: carrier decision and missing rung | Planned | compass wall/corridor + prime-carrying L3 |
| **ARX-005** | Coleman Conjecture as geometric antecedent (N-reading only) | Later | CC papers · sufficiency CLOSED |

Full map: [`series/00-series-map.md`](./series/00-series-map.md).

---

## 4. Account and endorsement (human steps)

arXiv requires a registered author account and, for new submitters in many math categories, **endorsement**.

```txt
1. Create/login: https://arxiv.org/user
2. Affiliation / name: Manuel Coleman · Love Labs LCA / PeAIce (as you prefer public)
3. Request endorsement in math.CA or math.MG if prompted
4. Prefer institutional or stable email for correspondence
5. Never list an AI system as an arXiv author
```

AI assistance may be acknowledged in a footnote or acknowledgments **if** you choose; arXiv authorship remains human.

---

## 5. Build pipeline (when TeX is available)

```bash
# from repo root, after installing MacTeX or BasicTeX + latexmk
cd arxiv/manuscripts/ddatl-002-grain-zero
../../tools/build.sh
# or: latexmk -pdf -interaction=nonstopmode main.tex
```

Until TeX is installed, edit `main.tex` / `main.md` here and compile on [Overleaf](https://www.overleaf.com) by uploading the manuscript folder + `templates/` + `bibliography/peaice-arxiv.bib`.

See [`tools/README.md`](./tools/README.md).

---

## 6. Source policy

- External arXiv papers are cited by **abs ID** and BibTeX; do not commit full-text PDFs unless license allows.
- Local Math-References PDFs stay under `Downloads/Research/Math-References/` (offline only).
- Internal designations (`PEAICE-…`) appear in front matter as program IDs; arXiv title/abstract stay mathematical and firewall-clean.

---

## 7. Related surfaces

| Surface | Role |
| --- | --- |
| `docs/whitepapers/` | Dense internal whitepapers |
| `docs/inspectable-intelligence.md` | II.1 publishing discipline |
| `claude-v6/docs/canon/` | Theorem register A–H · walls |
| `Research/.../PEAICE-GROK-TERMINAL-003_…` | Prior 20-paper arXiv grounding harvest |
| GitHub Pages `index.html` | Public program landing — not a preprint substitute |

---

## 8. Seal

```txt
PEAICE-ARXIV-LANE-001
begin · do not claim crown
RH OPEN · Coleman OPEN · h < 1
first note: Grain Zero residual (ARX-001)
```

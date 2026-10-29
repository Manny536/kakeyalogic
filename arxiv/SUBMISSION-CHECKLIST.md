# arXiv Submission Checklist (PeAIce)

Use once per manuscript. Print or copy into the manuscript’s `STATUS.md`.

**Manuscript ID:** _______________  
**Working title:** _______________  
**Target categories:** _______________  
**Date:** _______________

---

## A. Claim discipline (II / β-Protocol)

- [ ] Abstract does **not** claim RH or Coleman Conjecture proved
- [ ] Every new definition is marked FORMAL (definition) vs PROPOSED (conjecture)
- [ ] Every theorem/lemma has explicit hypotheses and a proof or is labeled OPEN / PROPOSED
- [ ] CLOSED-NEGATIVE results from the program are not reopened without new structure
- [ ] `h < 1` / evaluator non-sovereignty is not sold as a math theorem of ζ
- [ ] Symbol-collapse firewall present if K_σ / Re(s)=1/2 / μ / ζ(0) appear together
- [ ] Zeta firewall present if Kakeya residual meets regularization (ζ(0) second-stage only)
- [ ] No self-certification language (“AI confirmed”, “we have proved RH”, badge-as-proof)

## B. Mathematical hygiene

- [ ] Notation table or inline first-use definitions for all nonstandard symbols
- [ ] External theorems cited with author–year or arXiv ID; statements quoted carefully
- [ ] Proofs checked for: domain, measurability, constants depending on δ,ρ, scale passage
- [ ] Numerics (if any) isolated as NUMERICS with method + seed + hardware note
- [ ] Related work section distinguishes KNOWN literature from program-original claims

## C. arXiv package

- [ ] Single main `.tex` or clear multi-file set with one master
- [ ] All `\input` / `\include` / graphics / `.bib` present
- [ ] Bibliography compiles; no broken citations
- [ ] PDF builds with `pdflatex` / `latexmk` (or Overleaf log clean of fatal errors)
- [ ] PDF uses embedded fonts (Type 1 / OpenType) — arXiv requirement
- [ ] No hyperlinks that require login; arXiv strips some packages — test if needed
- [ ] `00README` or comments only if multi-file needs build order
- [ ] Source line endings and encoding UTF-8 where used carefully (math mode preferred for symbols)

## D. Metadata

- [ ] Title ≤ ~200 chars; no PeAIce marketing slogans as sole title
- [ ] Authors: human names only; affiliations OK
- [ ] Abstract: self-contained, no “this paper proves RH”
- [ ] MSC codes considered (e.g. 42B25, 28A75, 11M26 as appropriate)
- [ ] Comments line: “RH and Coleman Conjecture remain open” if program-adjacent
- [ ] License chosen (arXiv default or CC) — principal decision

## E. Cross-repo sync

- [ ] Source corpus path recorded in manuscript `STATUS.md`
- [ ] Designation (`PEAICE-…`) matches series map
- [ ] Git tag or commit hash recorded for the submitted source snapshot
- [ ] Public GitHub note updated only **after** arXiv assigns ID (optional)

## F. Post-submit

- [ ] arXiv ID recorded in `series/00-series-map.md`
- [ ] BibTeX `@unpublished` → `@article`/`@online` updated in `peaice-arxiv.bib`
- [ ] Index / peaice-index / Fable Instance links updated if desired
- [ ] No press claim beyond what the abstract states

---

```txt
Pass checklist ⇒ eligible to upload.
Fail any A-item ⇒ do not submit.
```

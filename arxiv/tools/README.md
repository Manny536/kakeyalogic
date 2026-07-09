# arXiv build tools

## Install TeX (macOS)

Option A — full MacTeX (large):

```bash
brew install --cask mactex
```

Option B — BasicTeX + packages (smaller):

```bash
brew install --cask basictex
# then, in a new terminal:
sudo tlmgr update --self
sudo tlmgr install latexmk amsmath amscls mathtools hyperref microtype enumitem
```

Option C — no local TeX: use [Overleaf](https://www.overleaf.com). Upload:

```txt
manuscripts/<id>/main.tex
templates/claim-discipline.tex
bibliography/peaice-arxiv.bib
```

Adjust `\input` / `\bibliography` paths for a flat Overleaf project if needed.

## Build

```bash
cd arxiv/manuscripts/ddatl-002-grain-zero
../../tools/build.sh
```

Or:

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

## arXiv upload package

Prefer a zip of sources that arXiv can compile:

```txt
main.tex
claim-discipline.tex   # or inline the macros
peaice-arxiv.bib
any figures.pdf
```

Do not upload proprietary full-text PDFs of others’ papers.

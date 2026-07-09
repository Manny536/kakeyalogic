#!/usr/bin/env bash
# Build the manuscript in the current directory (expects main.tex).
set -euo pipefail

if [[ ! -f main.tex ]]; then
  echo "error: run from a manuscript directory containing main.tex" >&2
  exit 1
fi

if command -v latexmk >/dev/null 2>&1; then
  latexmk -pdf -interaction=nonstopmode main.tex
elif command -v pdflatex >/dev/null 2>&1; then
  pdflatex -interaction=nonstopmode main.tex
  if [[ -f main.aux ]] && command -v bibtex >/dev/null 2>&1; then
    bibtex main || true
    pdflatex -interaction=nonstopmode main.tex
    pdflatex -interaction=nonstopmode main.tex
  fi
else
  echo "error: no latexmk/pdflatex found. Install MacTeX/BasicTeX or use Overleaf." >&2
  echo "see arxiv/tools/README.md" >&2
  exit 127
fi

echo "ok: build finished (see main.pdf if successful)"

#!/usr/bin/env bash
# kakeyalogic-reconcile.sh — resolve the stranded-banner duplication (V6.4.3 reconciliation)
# Run from the root of a fresh clone of github.com/Manny536/kakeyalogic
# It promotes the bannered root `downstream__*.md` files into their canonical docs/ paths,
# then removes the now-redundant staging/superseded files. Review, then commit.
set -euo pipefail

echo ">> Promoting bannered downstream__ files into docs/ ..."
declare -a DOCS=(
  l2-spectral-operator step4-operator-program spectral-determinism
  spectral-equivalence-target ddatl-bridge-lemma thermal-coupling-correction
  claude-v6-coherence-update l2c-ddtl-hamiltonian-probe
  berry-keating-commutator-closure cauchy-krein-perturbation-ledger
  prime-carrying-trace-architecture
)
for d in "${DOCS[@]}"; do
  if [[ -f "downstream__${d}.md" ]]; then
    mv -f "downstream__${d}.md" "docs/${d}.md"
    echo "   docs/${d}.md  <= downstream__${d}.md"
  fi
done

# README: the bannered root README replaces the repo README
if [[ -f downstream__README.md ]]; then
  mv -f downstream__README.md README.md
  echo "   README.md  <= downstream__README.md"
fi

echo ">> Removing redundant / superseded root artifacts ..."
# Superseded V6.4.2 root DDATL render (docs/peaice-ddatl-001.md is the V6.4.3 canon)
[[ -f peaice-ddatl-001.md ]] && rm -f peaice-ddatl-001.md && echo "   removed root peaice-ddatl-001.md (V6.4.2, superseded)"
# The already-applied corridor patch
[[ -f downstream-v6.4.3-corridor.patch ]] && rm -f downstream-v6.4.3-corridor.patch && echo "   removed downstream-v6.4.3-corridor.patch (applied)"
# The old propagation map (superseded by RECONCILE-v2 map)
[[ -f downstream__PROPAGATION-MAP.md ]] && rm -f downstream__PROPAGATION-MAP.md && echo "   removed downstream__PROPAGATION-MAP.md (superseded)"
# 1-byte junk placeholder
[[ -f "docs/DDATL downstream state" ]] && rm -f "docs/DDATL downstream state" && echo "   removed docs/'DDATL downstream state' (1-byte placeholder)"

# version-stale note on prime-carrying (bump tag 6.4.1 -> 6.4.3 if still present)
if [[ -f docs/prime-carrying-trace-architecture.md ]]; then
  sed -i 's/V6\.4\.1 audit patch/V6.4.3 audit patch (relocation target)/g' docs/prime-carrying-trace-architecture.md || true
fi

echo ""
echo ">> Add the new CC canon doc (copy kakeyalogic__docs__coleman-conjecture-antecedent.md here):"
echo "   cp <downloads>/kakeyalogic__docs__coleman-conjecture-antecedent.md docs/coleman-conjecture-antecedent.md"
echo ""
echo ">> Then:"
echo "   git add -A && git status"
echo "   git commit -m 'V6.4.3 reconciliation: promote closure banners into docs/, add CC canon doc, prune staging'"
echo ">> Done. Review 'git status' before committing."

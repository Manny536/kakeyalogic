# Frontier Math Rework

An executable mathematics prover and solver with an independent Python
certificate checker, our own bounded proof language, search engine, exact
solver, and replay format. It runs locally with Python 3.9 or later and no
runtime dependencies.

## Implemented mathematics

| Command | Theory and input | Checked result |
|---|---|---|
| `prove` | Classical propositional logic: names, `true`, `false`, `~`, `&`, `\|`, `->`, `<->`; explicit hypotheses | A sequent derivation, or a Boolean countermodel |
| `identity` | Polynomial identities over the rational field, with explicit multiplication, nonnegative integer powers, and division by nonzero rational constants | Equal canonical polynomial forms, or an exact rational counterexample |
| `solve` | Affine equations over the rational field, separated by semicolons | Reversible row operations establishing a unique solution, a complete parametric family, or inconsistency |
| `check` | A saved versioned JSON receipt | Independent replay against its exact problem, assumptions, and declared variables |

The application provides a terminal interface and Python API. Its supported language
is finite propositional logic and rational polynomial/linear algebra. Predicate
quantifiers, induction, inequalities, transcendental functions, general nonlinear
equation solving, and analysis require further kernel rules and solvers.

## Run the application

From a checkout:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
frontier-math-rework prove '(P -> Q) -> (~Q -> ~P)' --out contraposition.json
frontier-math-rework check contraposition.json --expect '(P -> Q) -> (~Q -> ~P)' --kind logic
frontier-math-rework prove 'Q' --given 'P' --given 'P -> Q'
frontier-math-rework identity '(x+y)^2 = x^2 + 2*x*y + y^2'
frontier-math-rework identity '(x+y)^2 = x^2 + y^2'
frontier-math-rework solve '2*x+y=7; x-y=2'
frontier-math-rework solve 'x+2*y-z=3' --variables x y z
frontier-math-rework solve 'x=1; x=2'
```

`python -m kakeyalogic.prover` exposes the same commands. Before installation,
use `PYTHONPATH=src python -m kakeyalogic.prover` from the repository root.
`--json` prints the complete receipt; `--out PATH` saves it.
Quotes keep shell operators inside mathematical expressions.

For `2*x+y=7; x-y=2`, the checked result is `x = 3; y = 1`.
For `x+2*y-z=3`, in variable order `[x,y,z]`, the full solution is
`[3,0,0] + y*[-2,1,0] + z*[1,0,1]`, with `y,z` arbitrary rationals.
For `x=1; x=2`, the certificate reaches a contradiction row `0 = 1`.

Use `1/10`, rather than decimal or floating-point literals. Write `2*x`, rather
than implicit multiplication `2x`. Powers use `^` or `**`; `-x^2` means
`-(x^2)`. Powers are evaluated as formal polynomial powers, including `x^0=1`.
The logic parser also accepts `¬ ∧ ∨ → ↔ ⊤ ⊥`. Implication is right associative;
precedence from strongest to weakest is negation, conjunction, disjunction,
implication, equivalence. Equivalence expands to two implications.

## Certificate architecture

The trusted checker never calls the search or solver modules. It derives the
result from the exact source and certificate, then compares that result with the
saved status. Search proposals and producer statistics supply no inference rule.

| Component | Responsibility |
|---|---|
| `syntax.py` | Bounded tokenizer, logical syntax, explicit assumptions, countermodel evaluation |
| `algebra.py` | Exact rational polynomial normalizer, affine parsing, checked echelon interpretation |
| `kernel.py` | Sequent-rule replay, counterexample checking, reversible row-operation replay |
| `engine.py` | Versioned problem-bound receipts and public verification entry point |
| `search.py`, `solver.py` | Certificate production; replaceable without changing acceptance rules |

The trusted computing base includes the checker, its parsers and exact arithmetic,
the receipt binding code, and the Python runtime. The kernel implementation has
regression tests; machine-checked metatheoretic soundness remains future work.

### Logical derivations

A sequent `Gamma |- Delta` means: whenever every proposition in `Gamma` holds,
at least one proposition in `Delta` holds. The root contains every supplied
`--given` hypothesis and the original goal. A proof closes with identity,
false on the left, or true on the right, and otherwise applies the specified
classical left/right connective rules. Node references must point backward.
The checker reconstructs every premise from the root; certificates cannot
substitute a different goal or introduce a new axiom.

An unprovable sequent returns an assignment making every hypothesis true and
the goal false. A limited search returns `UNKNOWN` with no certificate.
This distinction is enforced at verification time.

### Algebraic certificates

Polynomial coefficients use Python `Fraction` and arbitrary precision integers.
Canonical monomials preserve variable multiplicity. A successful identity
certificate supplies the common normal form, which the checker recomputes from
both original expressions. A failed identity supplies a concrete assignment;
the checker evaluates both sides exactly under that assignment.

Linear-system certificates contain elementary row operations, the resulting
reduced row echelon form (RREF), and the solution. The checker starts with the
original equations, replays each reversible operation, validates all RREF
conditions, and derives the solution family. Row scaling by zero and adding a
row to itself are rejected. A contradictory augmented pivot establishes
inconsistency; free columns establish the parameter basis. Variables appearing
in the original source remain present even when terms cancel: `x-x=0` returns
all rational `x`.

### Receipt identity and handoffs

Receipts bind the exact statement text, kind/domain, hypotheses, and optional
declared variable order with SHA-256. Whitespace changes therefore change the
problem digest. A digest detects content changes; authentication of the author
or source requires its own mechanism. A receiving worker should supply its own
full expected problem when it replays a receipt:

```python
from kakeyalogic.prover import run, verify

problem = {"kind": "logic", "statement": "Q", "assumptions": ["P", "P -> Q"]}
receipt = run(problem)
assert verify(receipt, expected_problem=problem)["valid"]
```

The command-line equivalent is:

```bash
frontier-math-rework prove 'Q' --given 'P' --given 'P -> Q' --out modus-ponens.json
frontier-math-rework check modus-ponens.json --expect 'Q' --kind logic --given 'P' --given 'P -> Q'
```

`PROVED` and `DISPROVED` refer to the complete formal problem including its
hypotheses. `UNIQUE`, `PARAMETRIC`, and `INCONSISTENT` describe the rational
solution set. `INVALID` denotes unsupported/malformed input or fixed language
bounds. `UNKNOWN` denotes an exhausted proof-search budget. Receipts with no
certificate cannot pass `check`. A completed mathematical classification,
including disproof or inconsistency, exits with code 0; rejected certificates
exit 1; unsupported input and exhausted searches exit 2.

Research statements must first be expressed in the supported formal language.
A proposition named `Compactness` carries only that proposition's explicitly
declared hypotheses and inference structure. The existing compactness,
Kakeya-to-Riemann, and Coleman obligations retain their registered status.

## Bounds and validation

Fixed bounds include 16 proposition/variable names, 16 logical hypotheses,
32 linear equations, 120 logical tokens per formula, 256 algebra tokens per
expression, 1024 polynomial terms, exponent at most 16, monomial degree at most
64, and rational numerator/denominator at most 4096 bits. Search defaults to
5000 steps, configurable up to 20000; replay allows 20000 logical visits or
4096 row operations. File-based certificate loading is capped at 4 MB and
rejects duplicate JSON keys and nonfinite numbers. Fixed bounds define the
accepted application language and keep resource failures separate from proofs.

Run the demo and tests:

```bash
PYTHONPATH=src python examples/math_prover/run_demo.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

Tests compare 250 generated logical problems with a separately implemented
truth-table oracle and generated nonsingular rational systems with known exact
solutions. Regression cases cover changed goals/hypotheses, forged leaves,
cyclic proof references, invalid row operations, changed solution vectors,
zero denominators, altered counterexamples, and source-bound CLI replay.

The next kernel extension is explicit first-order terms and quantifier rules,
with inference-rule tests preceding automated search. Induction and analysis
then require their own declared foundations and certificate formats.

## Research references

Manuel Coleman supplied these links as the material he studied while working
in this Lean and mathematics-prover research lane. The linked starting points
preserve the timestamps he shared.

| Reference | Starting point |
|---|---|
| [How Mathematicians can Get Started with Lean](https://www.youtube.com/watch?v=I2zaPoj3G50&t=300s) | 5:00 |
| [Is This the End of Handwritten Math? Introducing Lean](https://www.youtube.com/watch?v=0QZI_m8WZ0Q) | Beginning |
| [I tried Lean and instantly got PhD in Math](https://www.youtube.com/watch?v=l9hUGoN6BLM&t=2116s) | 35:16 |

The second video's accompanying source repository is
[AnkYog/LeanTutorial1](https://github.com/AnkYog/LeanTutorial1). Its README links
to that video and identifies `LeanTutorial.lean` as the example source.

English auto-generated speech captions have now been reviewed directly from
YouTube. See the [timestamped quotations and engineering interpretation](research/frontier-math-rework-video-notes.md)
and the [source-provenance record](research/sources/frontier-math-rework-video-quotes.json).
The starting points above preserve the shared URL timestamps; the reviewed
quotations have their own independently selected cue locations.

Manuel’s stated motivation is to reduce setup difficulty while retaining the
power of mechanically checked mathematics. The research references do not
attribute a commentator’s views about Lean’s creators to Manuel.

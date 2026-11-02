"""Trusted syntax for finite classical propositional logic.

No Python evaluation, user-defined inference rules, or implicit assumptions.
Equivalence is an abbreviation for two implications.
"""

import re
from dataclasses import dataclass
from typing import Tuple


class InvalidProblem(ValueError):
    """The input is outside the declared language or its resource bounds."""


class BudgetExceeded(ValueError):
    """Search stopped without a mathematical conclusion."""


@dataclass(frozen=True)
class Formula:
    """A proposition in the trusted abstract syntax."""

    op: str
    args: Tuple["Formula", ...] = ()
    name: str = ""


_TOKEN = re.compile(r"<->|->|[~&|()]|[A-Za-z][A-Za-z0-9_]*")
_UNICODE = str.maketrans({"¬": "~", "∧": "&", "∨": "|", "→": "->",
                         "↔": "<->", "⊥": "false", "⊤": "true"})


def tokenize(source, pattern, limit=256):
    """Tokenize the entire source; never skip an unrecognized character."""
    if not isinstance(source, str) or not source.strip() or len(source) > 4096:
        raise InvalidProblem("Enter a nonempty expression of at most 4096 characters.")
    tokens, pos = [], 0
    while pos < len(source):
        if source[pos].isspace():
            pos += 1
            continue
        match = pattern.match(source, pos)
        if match is None:
            raise InvalidProblem("Unexpected character at position %d." % (pos + 1))
        tokens.append(match.group())
        pos = match.end()
        if len(tokens) > limit:
            raise InvalidProblem("Expression token limit exceeded.")
    return tokens


def parse_formula(source):
    """Parse ~, &, |, -> (right associative), and <-> in that precedence order."""
    if not isinstance(source, str):
        raise InvalidProblem("A proposition must be text.")
    tokens = tokenize(source.translate(_UNICODE), _TOKEN, 120)
    pos = 0

    def take(token):
        nonlocal pos
        if pos < len(tokens) and tokens[pos] == token:
            pos += 1
            return True
        return False

    def atom(depth):
        nonlocal pos
        if depth > 40:
            raise InvalidProblem("Proposition nesting limit exceeded.")
        if take("~"):
            return Formula("not", (atom(depth + 1),))
        if take("("):
            value = equiv(depth + 1)
            if not take(")"):
                raise InvalidProblem("Missing closing parenthesis.")
            return value
        if pos >= len(tokens) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", tokens[pos]):
            raise InvalidProblem("Expected a proposition name or parenthesis.")
        name = tokens[pos]
        pos += 1
        return Formula(name) if name in ("true", "false") else Formula("atom", name=name)

    def conjunction(depth):
        value = atom(depth)
        while take("&"):
            value = Formula("and", (value, atom(depth)))
        return value

    def disjunction(depth):
        value = conjunction(depth)
        while take("|"):
            value = Formula("or", (value, conjunction(depth)))
        return value

    def implication(depth):
        if depth > 40:
            raise InvalidProblem("Proposition nesting limit exceeded.")
        value = disjunction(depth)
        if take("->"):
            value = Formula("imp", (value, implication(depth + 1)))
        return value

    def equiv(depth):
        value = implication(depth)
        while take("<->"):
            other = implication(depth)
            value = Formula("and", (Formula("imp", (value, other)),
                                    Formula("imp", (other, value))))
        return value

    result = equiv(0)
    if pos != len(tokens):
        raise InvalidProblem("Unexpected token: %s." % tokens[pos])
    # Expanding nested equivalences can be exponential; bound the actual tree.
    todo, count = [result], 0
    while todo:
        current = todo.pop()
        count += 1
        if count > 512:
            raise InvalidProblem("Expanded proposition is too large.")
        todo.extend(current.args)
    return result


def atoms(formula):
    """Collect names without assigning them truth values."""
    if formula.op == "atom":
        return {formula.name}
    return set().union(*(atoms(arg) for arg in formula.args))


def evaluate(formula, assignment):
    """Classical Boolean semantics used only to check counterexamples."""
    op, args = formula.op, formula.args
    if op == "atom":
        return assignment[formula.name]
    if op in ("true", "false"):
        return op == "true"
    if op == "not":
        return not evaluate(args[0], assignment)
    left, right = (evaluate(arg, assignment) for arg in args)
    if op == "and":
        return left and right
    if op == "or":
        return left or right
    if op == "imp":
        return not left or right
    raise InvalidProblem("Unknown logical connective.")


def logic_problem(problem):
    """Preserve all explicitly supplied hypotheses in the checked sequent."""
    assumptions = problem.get("assumptions", [])
    if not isinstance(assumptions, list) or len(assumptions) > 16:
        raise InvalidProblem("Supply at most 16 explicit assumptions.")
    left = tuple(parse_formula(item) for item in assumptions)
    right = (parse_formula(problem["statement"]),)
    names = set().union(*(atoms(item) for item in left + right))
    if len(names) > 16:
        raise InvalidProblem("At most 16 proposition names are supported per problem.")
    return left, right, names

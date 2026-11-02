"""Trusted exact polynomial arithmetic over Q and affine-system parsing.

Sparse monomials are sorted tuples of variable names. All coefficients use
Fraction; division is permitted only by nonzero rational constants.
"""

import re
from fractions import Fraction

from .syntax import InvalidProblem, tokenize

MAX_TERMS = 1024
MAX_BITS = 4096
_TOKEN = re.compile(r"\*\*|[0-9]+|[A-Za-z][A-Za-z0-9_]*|[+*/^()\-]")
_NAME = re.compile(r"[A-Za-z][A-Za-z0-9_]*\Z")


def bounded(poly):
    """Canonicalize zero terms and keep exact arithmetic within fixed bounds."""
    poly = {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}
    if len(poly) > MAX_TERMS or any(len(monomial) > 64 for monomial in poly):
        raise InvalidProblem("Polynomial size limit exceeded.")
    if any(max(abs(q.numerator).bit_length(), q.denominator.bit_length()) > MAX_BITS
           for q in poly.values()):
        raise InvalidProblem("Exact coefficient size limit exceeded.")
    return poly


def add(left, right):
    result = left.copy()
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return bounded(result)


def scale(poly, scalar):
    return bounded({monomial: coefficient * scalar for monomial, coefficient in poly.items()})


def multiply(left, right):
    result = {}
    if len(left) * len(right) > 100_000:
        raise InvalidProblem("Polynomial multiplication budget exceeded.")
    for first, a in left.items():
        for second, b in right.items():
            monomial = tuple(sorted(first + second))
            result[monomial] = result.get(monomial, Fraction(0)) + a * b
    return bounded(result)


def parse_polynomial(source):
    """Parse explicit rational polynomial syntax; no calls or symbolic inverses."""
    tokens = tokenize(source, _TOKEN, 256)
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
            raise InvalidProblem("Algebra nesting limit exceeded.")
        if take("("):
            value = expression(depth + 1)
            if not take(")"):
                raise InvalidProblem("Missing closing parenthesis.")
            return value
        if pos >= len(tokens):
            raise InvalidProblem("Expected an integer, variable, or parenthesis.")
        token = tokens[pos]
        pos += 1
        if token.isdigit():
            return bounded({(): Fraction(int(token))})
        if _NAME.fullmatch(token):
            return {(token,): Fraction(1)}
        raise InvalidProblem("Expected an integer, variable, or parenthesis.")

    def power(depth):
        nonlocal pos
        value = atom(depth)
        if take("^") or take("**"):
            if pos >= len(tokens) or not tokens[pos].isdigit():
                raise InvalidProblem("An exponent must be an integer from 0 through 16.")
            exponent = int(tokens[pos])
            pos += 1
            if exponent > 16:
                raise InvalidProblem("An exponent must be an integer from 0 through 16.")
            base, value = value, {(): Fraction(1)}
            for _ in range(exponent):
                value = multiply(value, base)
        return value

    def signed(depth):
        if depth > 40:
            raise InvalidProblem("Algebra nesting limit exceeded.")
        if take("+"):
            return signed(depth + 1)
        if take("-"):
            return scale(signed(depth + 1), -1)
        return power(depth)

    def product(depth):
        value = signed(depth)
        while pos < len(tokens) and tokens[pos] in ("*", "/"):
            divide = take("/")
            if not divide:
                take("*")
            other = signed(depth)
            if divide:
                if any(monomial for monomial in other) or not other.get((), 0):
                    raise InvalidProblem("Divide only by a nonzero rational constant.")
                value = scale(value, 1 / other[()])
            else:
                value = multiply(value, other)
        return value

    def expression(depth):
        value = product(depth)
        while pos < len(tokens) and tokens[pos] in ("+", "-"):
            subtract = take("-")
            if not subtract:
                take("+")
            other = product(depth)
            value = add(value, scale(other, -1) if subtract else other)
        return value

    value = expression(0)
    if pos != len(tokens):
        raise InvalidProblem("Unexpected algebra token: %s." % tokens[pos])
    if len(variables(value)) > 16:
        raise InvalidProblem("At most 16 variables are supported.")
    return value


def variables(poly):
    return set().union(*(set(monomial) for monomial in poly))


def equation(source):
    if not isinstance(source, str) or source.count("=") != 1:
        raise InvalidProblem("An equation must contain exactly one '='.")
    left, right = source.split("=")
    return parse_polynomial(left), parse_polynomial(right)


def normal_form(poly):
    return [[list(monomial), str(coefficient)] for monomial, coefficient in sorted(poly.items())]


def evaluate(poly, assignment):
    result = Fraction(0)
    for monomial, coefficient in poly.items():
        for name in monomial:
            coefficient *= assignment[name]
        result += coefficient
    return result


def rational(text):
    """Read a bounded certificate scalar in canonical Fraction string form."""
    if not isinstance(text, str) or len(text) > 2500:
        raise InvalidProblem("A certificate scalar must be a bounded rational string.")
    try:
        value = Fraction(text)
    except (ValueError, ZeroDivisionError) as error:
        raise InvalidProblem("Invalid certificate rational.") from error
    bounded({(): value})
    if str(value) != text:
        raise InvalidProblem("Certificate rationals must use canonical form, e.g. '1/2'.")
    return value


def linear_problem(problem):
    equations = problem["statement"].split(";")
    if not 1 <= len(equations) <= 32:
        raise InvalidProblem("Supply between 1 and 32 equations, separated by semicolons.")
    polys = [add(left, scale(right, -1)) for left, right in map(equation, equations)]
    if any(len(monomial) > 1 for poly in polys for monomial in poly):
        raise InvalidProblem("The linear solver accepts affine equations over Q.")
    # Keep syntactically present variables even if normalization cancels them.
    # x - x = 0 describes every rational x, rather than a zero-variable solution.
    names = {token for source in equations for token in tokenize(source.replace("=", " "), _TOKEN)
             if _NAME.fullmatch(token)}
    declared = problem.get("variables")
    if declared is None:
        declared = sorted(names)
    if (not isinstance(declared, list) or len(declared) > 16
            or any(not isinstance(name, str) or not _NAME.fullmatch(name) for name in declared)
            or len(set(declared)) != len(declared) or not names.issubset(declared)):
        raise InvalidProblem("Declare distinct variable names covering every equation variable (max 16).")
    matrix = [[poly.get((name,), Fraction(0)) for name in declared]
              + [-poly.get((), Fraction(0))] for poly in polys]
    return declared, matrix


def matrix_json(matrix):
    return [[str(value) for value in row] for row in matrix]


def solution_from_rref(names, matrix):
    """Trusted interpretation of an already checked reduced row echelon form."""
    width = len(names)
    pivots, previous, zero_seen = {}, -1, False
    for index, row in enumerate(matrix):
        pivot = next((j for j, value in enumerate(row) if value), None)
        if pivot is None:
            zero_seen = True
            continue
        if zero_seen or pivot <= previous or row[pivot] != 1:
            raise InvalidProblem("Certificate matrix is not in reduced row echelon form.")
        if any(other[pivot] != 0 for k, other in enumerate(matrix) if k != index):
            raise InvalidProblem("A pivot column is not reduced.")
        previous = pivot
        pivots[pivot] = index
    if width in pivots:
        return {"classification": "INCONSISTENT", "contradiction_row": pivots[width]}
    free = [j for j in range(width) if j not in pivots]
    particular = [Fraction(0)] * width
    basis = []
    for column, index in pivots.items():
        particular[column] = matrix[index][-1]
    for column in free:
        vector = [Fraction(0)] * width
        vector[column] = Fraction(1)
        for pivot, index in pivots.items():
            vector[pivot] = -matrix[index][column]
        basis.append([str(value) for value in vector])
    return {"classification": "PARAMETRIC" if free else "UNIQUE", "variables": names,
            "particular": [str(value) for value in particular], "basis": basis,
            "parameters": [names[j] for j in free]}

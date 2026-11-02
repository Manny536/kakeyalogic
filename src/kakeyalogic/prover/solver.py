"""Untrusted exact-algebra certificate producers."""

from fractions import Fraction

from . import algebra


def identity(problem):
    left, right = algebra.equation(problem["statement"])
    if left == right:
        return {"method": "normalization", "normal_form": algebra.normal_form(left)}, {}
    difference = algebra.add(left, algebra.scale(right, -1))
    assignment = {}
    # Specialize one variable at a time while keeping the polynomial nonzero.
    # A nonzero degree-d polynomial has at most d roots over Q.
    for name in sorted(algebra.variables(left) | algebra.variables(right)):
        degree = max((monomial.count(name) for monomial in difference), default=0)
        for candidate in range(degree + 1):
            specialized = {}
            for monomial, coefficient in difference.items():
                reduced = tuple(variable for variable in monomial if variable != name)
                coefficient *= Fraction(candidate) ** monomial.count(name)
                specialized[reduced] = specialized.get(reduced, Fraction(0)) + coefficient
            specialized = algebra.bounded(specialized)
            if specialized:
                assignment[name] = str(candidate)
                difference = specialized
                break
        else:
            raise ValueError("Failed to construct a nonidentity witness.")
    return {"method": "evaluation", "assignment": assignment}, {}


def linear(problem):
    names, matrix = algebra.linear_problem(problem)
    operations, pivot_row = [], 0
    # Include the augmented column so inconsistent systems also reach full RREF.
    for column in range(len(names) + 1):
        selected = next((row for row in range(pivot_row, len(matrix)) if matrix[row][column]), None)
        if selected is None:
            continue
        if selected != pivot_row:
            matrix[selected], matrix[pivot_row] = matrix[pivot_row], matrix[selected]
            operations.append({"op": "swap", "a": selected, "b": pivot_row})
        factor = 1 / matrix[pivot_row][column]
        if factor != 1:
            matrix[pivot_row] = [factor * value for value in matrix[pivot_row]]
            operations.append({"op": "scale", "row": pivot_row, "factor": str(factor)})
        for row in range(len(matrix)):
            if row == pivot_row or not matrix[row][column]:
                continue
            factor = -matrix[row][column]
            matrix[row] = [a + factor * b for a, b in zip(matrix[row], matrix[pivot_row])]
            operations.append({"op": "add", "target": row, "source": pivot_row, "factor": str(factor)})
        for row in matrix:
            for value in row:
                algebra.bounded({(): value})
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return {"method": "row-reduction", "operations": operations,
            "rref": algebra.matrix_json(matrix), "solution": algebra.solution_from_rref(names, matrix)}, {
                "row_operations": len(operations)}

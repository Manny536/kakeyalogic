"""Certificate checker. This module never imports search or solver code.

The trusted base is this checker, syntax.py, algebra.py, Python's integers and
fractions. The supported logical theory is classical propositional logic;
algebra is over the rational field. No extra axioms can be loaded.
"""

from . import algebra
from .syntax import InvalidProblem, evaluate, logic_problem

MAX_NODES = 20_000
MAX_OPERATIONS = 4096


def fields(value, required):
    """Reject incomplete or differently shaped certificate objects."""
    if not isinstance(value, dict) or set(value) != set(required.split()):
        raise InvalidProblem("Malformed certificate object; expected fields: " + required)


def index(value, size):
    if type(value) is not int or not 0 <= value < size:
        raise InvalidProblem("Invalid certificate index.")
    return value


def validate_problem(problem):
    if not isinstance(problem, dict) or not isinstance(problem.get("statement"), str):
        raise InvalidProblem("A problem requires a text statement.")
    kind = problem.get("kind")
    allowed = {"logic": {"kind", "statement", "assumptions"},
               "identity": {"kind", "statement"},
               "linear": {"kind", "statement", "variables"}}
    if not isinstance(kind, str) or kind not in allowed or not set(problem).issubset(allowed[kind]):
        raise InvalidProblem("Problem kind must be logic, identity, or linear, with explicit fields.")
    if len(problem["statement"]) > 16_384:
        raise InvalidProblem("Problem statement is too large.")
    return kind


def check_logic(problem, certificate):
    left, right, names = logic_problem(problem)
    if certificate.get("method") == "countermodel":
        fields(certificate, "method assignment")
        assignment = certificate["assignment"]
        if (not isinstance(assignment, dict) or set(assignment) != names
                or any(type(value) is not bool for value in assignment.values())):
            raise InvalidProblem("Countermodel must assign a Boolean to every proposition.")
        if not all(evaluate(item, assignment) for item in left) or evaluate(right[0], assignment):
            raise InvalidProblem("Assignment does not refute the original sequent.")
        return "DISPROVED"
    fields(certificate, "method nodes root")
    if certificate["method"] != "sequent":
        raise InvalidProblem("Unknown logical certificate method.")
    nodes = certificate["nodes"]
    if not isinstance(nodes, list) or not 1 <= len(nodes) <= MAX_NODES:
        raise InvalidProblem("Proof node limit exceeded or empty proof.")
    root = index(certificate["root"], len(nodes))
    if root != len(nodes) - 1:
        raise InvalidProblem("The root must be the final proof node.")
    todo, seen, work = [(root, left, right)], set(), 0
    while todo:
        node_id, gamma, delta = todo.pop()
        work += 1
        if work > MAX_NODES:
            raise InvalidProblem("Certificate replay budget exceeded.")
        seen.add(node_id)
        node = nodes[node_id]
        if not isinstance(node, dict):
            raise InvalidProblem("A proof node must be an object.")
        rule = node.get("rule")
        if rule in ("id", "bottom_left", "top_right"):
            fields(node, "rule")
            valid = (rule == "id" and bool(set(gamma).intersection(delta))
                     or rule == "bottom_left" and any(f.op == "false" for f in gamma)
                     or rule == "top_right" and any(f.op == "true" for f in delta))
            if not valid:
                raise InvalidProblem("Unjustified proof leaf.")
            continue
        fields(node, "rule index children")
        if rule not in {"true_left", "false_right", "not_left", "not_right",
                        "and_left", "and_right", "or_left", "or_right", "imp_left", "imp_right"}:
            raise InvalidProblem("Unknown inference rule.")
        side = gamma if rule.endswith("_left") else delta
        selected = index(node["index"], len(side))
        principal = side[selected]
        if principal.op != rule.rsplit("_", 1)[0]:
            raise InvalidProblem("Inference rule does not match its principal formula.")
        rest = side[:selected] + side[selected + 1:]
        args = principal.args
        # Independently specified two-sided classical sequent rules.
        if rule == "true_left":
            premises = [(rest, delta)]
        elif rule == "false_right":
            premises = [(gamma, rest)]
        elif rule == "not_left":
            premises = [(rest, delta + (args[0],))]
        elif rule == "not_right":
            premises = [(gamma + (args[0],), rest)]
        elif rule == "and_left":
            premises = [(rest + args, delta)]
        elif rule == "and_right":
            premises = [(gamma, rest + (args[0],)), (gamma, rest + (args[1],))]
        elif rule == "or_left":
            premises = [(rest + (args[0],), delta), (rest + (args[1],), delta)]
        elif rule == "or_right":
            premises = [(gamma, rest + args)]
        elif rule == "imp_left":
            premises = [(rest, delta + (args[0],)), (rest + (args[1],), delta)]
        else:  # imp_right
            premises = [(gamma + (args[0],), rest + (args[1],))]
        children = node["children"]
        if not isinstance(children, list) or len(children) != len(premises):
            raise InvalidProblem("Incorrect premise count.")
        for child, (before, after) in zip(children, premises):
            # Backward-only references also rule out cyclic proof certificates.
            index(child, node_id)
            todo.append((child, before, after))
    if seen != set(range(len(nodes))):
        raise InvalidProblem("Certificate contains unreachable proof nodes.")
    return "PROVED"


def check_identity(problem, certificate):
    left, right = algebra.equation(problem["statement"])
    if certificate.get("method") == "normalization":
        fields(certificate, "method normal_form")
        if left != right or certificate["normal_form"] != algebra.normal_form(left):
            raise InvalidProblem("Polynomial normal forms do not establish this identity.")
        return "PROVED"
    fields(certificate, "method assignment")
    if certificate["method"] != "evaluation":
        raise InvalidProblem("Unknown algebraic certificate method.")
    assignment = certificate["assignment"]
    if not isinstance(assignment, dict) or set(assignment) != algebra.variables(left) | algebra.variables(right):
        raise InvalidProblem("A counterexample must assign every polynomial variable.")
    assignment = {name: algebra.rational(value) for name, value in assignment.items()}
    if algebra.evaluate(left, assignment) == algebra.evaluate(right, assignment):
        raise InvalidProblem("Assignment does not refute the polynomial identity.")
    return "DISPROVED"


def check_linear(problem, certificate):
    fields(certificate, "method operations rref solution")
    if certificate["method"] != "row-reduction":
        raise InvalidProblem("Unknown linear certificate method.")
    names, matrix = algebra.linear_problem(problem)
    operations = certificate["operations"]
    if not isinstance(operations, list) or len(operations) > MAX_OPERATIONS:
        raise InvalidProblem("Row operation limit exceeded.")
    for operation in operations:
        if not isinstance(operation, dict):
            raise InvalidProblem("A row operation must be an object.")
        op = operation.get("op")
        if op == "swap":
            fields(operation, "op a b")
            first, second = index(operation["a"], len(matrix)), index(operation["b"], len(matrix))
            matrix[first], matrix[second] = matrix[second], matrix[first]
        elif op == "scale":
            fields(operation, "op row factor")
            row = index(operation["row"], len(matrix))
            factor = algebra.rational(operation["factor"])
            if not factor:
                raise InvalidProblem("Scaling a row by zero is not reversible.")
            matrix[row] = [factor * value for value in matrix[row]]
        elif op == "add":
            fields(operation, "op target source factor")
            target = index(operation["target"], len(matrix))
            source = index(operation["source"], len(matrix))
            if target == source:
                raise InvalidProblem("Row addition must use distinct rows.")
            factor = algebra.rational(operation["factor"])
            matrix[target] = [a + factor * b for a, b in zip(matrix[target], matrix[source])]
        else:
            raise InvalidProblem("Unknown row operation.")
        for row in matrix:
            for value in row:
                algebra.bounded({(): value})
    if certificate["rref"] != algebra.matrix_json(matrix):
        raise InvalidProblem("Claimed matrix does not match the replayed row operations.")
    solution = algebra.solution_from_rref(names, matrix)
    if (certificate["solution"] != solution
            or (solution["classification"] == "INCONSISTENT"
                and type(certificate["solution"].get("contradiction_row")) is not int)):
        raise InvalidProblem("Claimed solution does not match the checked echelon form.")
    return solution["classification"]


def check(problem, certificate):
    """Check the actual problem and proof; return only the derived status."""
    kind = validate_problem(problem)
    if not isinstance(certificate, dict):
        raise InvalidProblem("Missing certificate object.")
    return {"logic": check_logic, "identity": check_identity, "linear": check_linear}[kind](problem, certificate)

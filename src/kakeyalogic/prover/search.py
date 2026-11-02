"""Untrusted deterministic sequent search. Only kernel replay admits a proof."""

from .syntax import BudgetExceeded, logic_problem


def prove(problem, max_steps=5000):
    left, right, names = logic_problem(problem)
    nodes, steps = [], 0

    def emit(rule, selected=None, children=None):
        node = {"rule": rule}
        if selected is not None:
            node.update(index=selected, children=children)
        nodes.append(node)
        return len(nodes) - 1

    def visit(gamma, delta):
        nonlocal steps
        steps += 1
        if steps > max_steps:
            raise BudgetExceeded("Logical search step budget exhausted.")
        if set(gamma).intersection(delta):
            return emit("id"), None
        if any(item.op == "false" for item in gamma):
            return emit("bottom_left"), None
        if any(item.op == "true" for item in delta):
            return emit("top_right"), None
        for side_name, side in (("left", gamma), ("right", delta)):
            for selected, formula in enumerate(side):
                if formula.op == "atom":
                    continue
                rest = side[:selected] + side[selected + 1:]
                op, args = formula.op, formula.args
                if side_name == "left":
                    if op == "true":
                        goals = [(rest, delta)]
                    elif op == "not":
                        goals = [(rest, delta + args)]
                    elif op == "and":
                        goals = [(rest + args, delta)]
                    elif op == "or":
                        goals = [(rest + (a,), delta) for a in args]
                    else:  # implication
                        goals = [(rest, delta + (args[0],)), (rest + (args[1],), delta)]
                else:
                    if op == "false":
                        goals = [(gamma, rest)]
                    elif op == "not":
                        goals = [(gamma + args, rest)]
                    elif op == "and":
                        goals = [(gamma, rest + (a,)) for a in args]
                    elif op == "or":
                        goals = [(gamma, rest + args)]
                    else:
                        goals = [(gamma + (args[0],), rest + (args[1],))]
                children = []
                for before, after in goals:
                    child, witness = visit(before, after)
                    if witness is not None:
                        return None, witness
                    children.append(child)
                return emit(op + "_" + side_name, selected, children), None
        assignment = {name: False for name in sorted(names)}
        assignment.update({formula.name: True for formula in gamma})
        return None, assignment

    root, countermodel = visit(left, right)
    certificate = ({"method": "countermodel", "assignment": countermodel}
                   if countermodel is not None else {"method": "sequent", "nodes": nodes, "root": root})
    return certificate, {"search_steps": steps}

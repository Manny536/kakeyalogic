"""Independent semantic checks, exact solving, and hostile-certificate regressions."""

# Successful cases below assert their checked status before using a certificate.
# Pylint infers only the null-certificate error variant of engine.run's dict.
# pylint: disable=unsubscriptable-object

import copy
import itertools
import json
import random
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

from kakeyalogic.prover import run, verify
from kakeyalogic.prover.engine import fingerprint, load_receipt
from kakeyalogic.prover.syntax import InvalidProblem


def logic(statement, assumptions=None):
    return {"kind": "logic", "statement": statement, "assumptions": assumptions or []}


def linear(statement, variables=None):
    problem = {"kind": "linear", "statement": statement}
    if variables is not None:
        problem["variables"] = variables
    return problem


def identity(statement):
    return {"kind": "identity", "statement": statement}


class LogicTests(unittest.TestCase):
    def checked(self, problem, status):
        receipt = run(problem)
        self.assertEqual(receipt["status"], status, receipt)
        self.assertTrue(verify(receipt, expected_problem=problem)["valid"])
        self.assertTrue(verify(load_receipt(json.dumps(receipt)))["valid"])
        return receipt

    def test_classical_rules_and_explicit_assumptions(self):
        proved = ["P -> P", "P | ~P", "~~P -> P", "false -> P", "P -> true",
                  "true -> (P -> P)", "(P | false) -> P", "~false",
                  "(P & Q) -> P", "P -> (Q -> (P & Q))", "P -> (P | Q)",
                  "((P | Q) & ~P) -> Q", "((P -> Q) & P) -> Q",
                  "(P -> Q) -> (~Q -> ~P)", "(P <-> Q) -> (Q <-> P)",
                  "(P -> Q -> P)", "¬(P ∧ ¬P)"]
        for source in proved:
            with self.subTest(source=source):
                self.checked(logic(source), "PROVED")
        self.checked(logic("Q", ["P", "P -> Q"]), "PROVED")
        self.checked(logic("Q", ["P"]), "DISPROVED")

    def test_countermodels(self):
        for source in ("P", "false", "P & ~P", "P -> Q", "(P -> Q) -> P", "P <-> Q"):
            with self.subTest(source=source):
                self.checked(logic(source), "DISPROVED")

    def test_generated_formulas_against_separate_truth_table_oracle(self):
        # This oracle deliberately does not use the production parser/evaluator.
        rng = random.Random(1301)

        def formula(depth):
            if depth == 0 or rng.random() < 0.2:
                return rng.choice(("P", "Q", "R", "true", "false"))
            op = rng.choice(("~", "&", "|", "->", "<->"))
            if op == "~":
                return op, formula(depth - 1)
            return op, formula(depth - 1), formula(depth - 1)

        def text(tree):
            if isinstance(tree, str):
                return tree
            if tree[0] == "~":
                return "~(" + text(tree[1]) + ")"
            return "(" + text(tree[1]) + tree[0] + text(tree[2]) + ")"

        def truth(tree, values):
            if isinstance(tree, str):
                return {"true": True, "false": False, **values}[tree]
            op = tree[0]
            a = truth(tree[1], values)
            if op == "~":
                return not a
            b = truth(tree[2], values)
            return {"&": a and b, "|": a or b, "->": (not a) or b, "<->": a == b}[op]

        valuations = [dict(zip(("P", "Q", "R"), values))
                      for values in itertools.product((False, True), repeat=3)]
        for case in range(250):
            goal, hypothesis = formula(3), formula(2)
            assumptions = [hypothesis] if case % 2 else []
            valid = all(not all(truth(item, values) for item in assumptions) or truth(goal, values)
                        for values in valuations)
            self.checked(logic(text(goal), [text(item) for item in assumptions]),
                         "PROVED" if valid else "DISPROVED")

    def test_budget_exhaustion_never_means_disproof(self):
        receipt = run(logic("(P -> Q) -> (~Q -> ~P)"), max_steps=1)
        self.assertEqual(receipt["status"], "UNKNOWN")
        self.assertIsNone(receipt["certificate"])
        self.assertFalse(verify(receipt)["valid"])

    def test_malformed_logic_is_rejected(self):
        for source in ("", "P Q", "P;Q", "P ->", "P)", "((P)", "P ∀ Q", "~" * 50 + "P"):
            with self.subTest(source=source):
                self.assertEqual(run(logic(source))["status"], "INVALID")


class AlgebraTests(unittest.TestCase):
    def checked(self, problem, status):
        receipt = run(problem)
        self.assertEqual(receipt["status"], status, receipt)
        self.assertTrue(verify(receipt, expected_problem=problem)["valid"], receipt)
        return receipt

    def test_exact_polynomial_identities(self):
        for source in ("(x+y)^2=x^2+2*x*y+y^2", "(x-y)*(x+y)=x^2-y^2",
                       "(x+1)^3=x^3+3*x^2+3*x+1", "x/3+x/6=x/2",
                       "-x^2 = -(x*x)", "(x-x)^0=1", "0=0", "x/(1+1)=x/2"):
            with self.subTest(source=source):
                self.checked(identity(source), "PROVED")

    def test_polynomial_counterexamples(self):
        for source in ("(x+y)^2=x^2+y^2", "x=x+1", "1=2", "x-x=1", "x^2=x", "x*y=0"):
            with self.subTest(source=source):
                self.checked(identity(source), "DISPROVED")

    def test_unique_rational_solution_and_no_float_rounding(self):
        receipt = self.checked(linear("2*x+y=7;x-y=2"), "UNIQUE")
        self.assertEqual(receipt["certificate"]["solution"]["particular"], ["3", "1"])
        receipt = self.checked(linear("9007199254740993*x=9007199254740994"), "UNIQUE")
        self.assertEqual(receipt["certificate"]["solution"]["particular"],
                         ["9007199254740994/9007199254740993"])

    def test_parametric_solution_basis(self):
        receipt = self.checked(linear("x+2*y-z=3;2*x+4*y-2*z=6"), "PARAMETRIC")
        solution = receipt["certificate"]["solution"]
        self.assertEqual(solution["variables"], ["x", "y", "z"])
        particular = list(map(Fraction, solution["particular"]))
        self.assertEqual(particular[0] + 2 * particular[1] - particular[2], 3)
        self.assertEqual(len(solution["basis"]), 2)
        for raw in solution["basis"]:
            vector = list(map(Fraction, raw))
            self.assertEqual(vector[0] + 2 * vector[1] - vector[2], 0)

    def test_constant_and_inconsistent_systems(self):
        self.checked(linear("x=1;x=2"), "INCONSISTENT")
        self.checked(linear("0=1"), "INCONSISTENT")
        self.checked(linear("0=0"), "UNIQUE")
        self.checked(linear("0=0", ["x"]), "PARAMETRIC")
        receipt = self.checked(linear("x-x=0"), "PARAMETRIC")
        self.assertEqual(receipt["certificate"]["solution"]["variables"], ["x"])
        self.assertEqual(run(linear("x-x=0", []))["status"], "INVALID")

    def test_generated_full_rank_systems(self):
        rng = random.Random(73)
        for _ in range(60):
            a, b, c, d = [rng.randint(-9, 9) for _ in range(4)]
            if a * d == b * c:
                continue
            x, y = Fraction(rng.randint(-8, 8), 3), Fraction(rng.randint(-8, 8), 5)
            source = "%s*x+(%s)*y=%s;%s*x+(%s)*y=%s" % (a, b, a*x+b*y, c, d, c*x+d*y)
            receipt = self.checked(linear(source), "UNIQUE")
            self.assertEqual(receipt["certificate"]["solution"]["particular"], [str(x), str(y)])

    def test_declared_variable_order_is_preserved(self):
        receipt = self.checked(linear("x+y=4", ["y", "x", "z"]), "PARAMETRIC")
        self.assertEqual(receipt["certificate"]["solution"]["variables"], ["y", "x", "z"])
        for names in (["x", "x"], ["z"], ["x", "bad-name"]):
            self.assertEqual(run(linear("x=1", names))["status"], "INVALID")

    def test_unsupported_or_unsafe_algebra(self):
        for source in ("x/x=1", "1/0=0", "x^-1=1", "x^17=1", "x^2^2=1",
                       "sin(x)=0", "__import__('os')=0", "x.__class__=1", "2x=2",
                       "0.1+0.2=0.3", "x=1=2", "x<1", "x==1", "x=1;"):
            with self.subTest(source=source):
                self.assertEqual(run(identity(source))["status"], "INVALID")
        self.assertEqual(run(linear("x^2=4"))["status"], "INVALID")


class CertificateTests(unittest.TestCase):
    def test_verifier_does_not_call_producers(self):
        receipts = [run(logic("P|~P")), run(identity("(x+1)^2=x^2+2*x+1")), run(linear("2*x=3"))]
        with mock.patch("kakeyalogic.prover.search.prove", side_effect=AssertionError("search called")), \
                mock.patch("kakeyalogic.prover.solver.identity", side_effect=AssertionError("solver called")), \
                mock.patch("kakeyalogic.prover.solver.linear", side_effect=AssertionError("solver called")):
            for receipt in receipts:
                self.assertTrue(verify(receipt)["valid"])

    def test_saved_status_source_and_hypotheses_are_not_trusted(self):
        original = run(logic("Q", ["P", "P -> Q"]))
        changed = copy.deepcopy(original)
        changed["status"] = "DISPROVED"
        self.assertFalse(verify(changed)["valid"])
        changed = copy.deepcopy(original)
        changed["problem"]["statement"] = "R"
        self.assertFalse(verify(changed)["valid"])
        changed["problem_sha256"] = fingerprint(changed["problem"])
        self.assertFalse(verify(changed)["valid"])
        changed = copy.deepcopy(original)
        changed["problem"]["assumptions"] = []
        changed["problem_sha256"] = fingerprint(changed["problem"])
        self.assertFalse(verify(changed)["valid"])
        different_valid_problem = run(logic("Q", ["Q"]))
        self.assertFalse(verify(different_valid_problem, expected_problem=original["problem"])["valid"])

    def test_illegal_proof_leaves_rules_and_graphs(self):
        original = run(logic("P -> P"))
        mutations = [
            lambda cert: cert["nodes"][0].update(rule="made_up_axiom"),
            lambda cert: cert["nodes"][-1].update(children=[cert["root"]]),
            lambda cert: cert["nodes"][-1].update(children=[]),
            lambda cert: cert["nodes"][-1].update(index=True),
            lambda cert: cert["nodes"][-1].update(index=20),
            lambda cert: cert.update(root=False),
            lambda cert: cert["nodes"][-1].update(rule="or_right"),
        ]
        for mutation in mutations:
            changed = copy.deepcopy(original)
            mutation(changed["certificate"])
            self.assertFalse(verify(changed)["valid"])
        fabricated = run(logic("P"))
        fabricated.update(status="PROVED", certificate={"method": "sequent", "nodes": [{"rule": "id"}], "root": 0})
        self.assertFalse(verify(fabricated)["valid"])
        orphan = copy.deepcopy(original)
        orphan["certificate"]["nodes"].append({"rule": "imp_right", "index": 0, "children": [0]})
        orphan["certificate"]["root"] = 2
        self.assertFalse(verify(orphan)["valid"])

    def test_counterexample_is_rechecked(self):
        receipt = run(logic("P"))
        receipt["certificate"]["assignment"]["P"] = True
        self.assertFalse(verify(receipt)["valid"])
        receipt["certificate"]["assignment"]["P"] = 0
        self.assertFalse(verify(receipt)["valid"])
        receipt = run(identity("x=0"))
        receipt["certificate"]["assignment"]["x"] = "0"
        self.assertFalse(verify(receipt)["valid"])

    def test_row_operations_and_solution_are_replayed(self):
        original = run(linear("2*x=3"))
        for replacement in ("0", "1", "1/0", "NaN", 0.5, None, "2/4"):
            changed = copy.deepcopy(original)
            changed["certificate"]["operations"][0]["factor"] = replacement
            self.assertFalse(verify(changed)["valid"], replacement)
        changed = copy.deepcopy(original)
        changed["certificate"]["operations"] = []
        self.assertFalse(verify(changed)["valid"])
        changed = copy.deepcopy(original)
        changed["certificate"]["solution"]["particular"] = ["2"]
        self.assertFalse(verify(changed)["valid"])
        changed = copy.deepcopy(original)
        changed["certificate"]["operations"] = [{"op": "add", "target": 0, "source": 0, "factor": "-1"}]
        self.assertFalse(verify(changed)["valid"])
        changed = run(linear("x=1;x=2"))
        changed["certificate"]["solution"]["contradiction_row"] = True
        self.assertFalse(verify(changed)["valid"])

    def test_polynomial_normal_form_is_recomputed(self):
        receipt = run(identity("x+x=2*x"))
        receipt["certificate"]["normal_form"][0][1] = "3"
        self.assertFalse(verify(receipt)["valid"])

    def test_ambiguous_and_malformed_receipts(self):
        for source in ('{"status":"PROVED","status":"DISPROVED"}', '{"value":NaN}', '{"value":Infinity}'):
            with self.assertRaises(InvalidProblem):
                load_receipt(source)
        for value in (None, [], {}, {"problem": {}}, {"problem": "P"}):
            self.assertFalse(verify(value)["valid"])
        self.assertEqual(run({"kind": "logic", "statement": "P", "axioms": ["P"]})["status"], "INVALID")

    def test_cli_roundtrip_and_expected_problem(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "proof.json"
            prefix = [sys.executable, "-m", "kakeyalogic.prover"]
            produced = subprocess.run(prefix + ["prove", "P -> P", "--out", str(path), "--json"],
                                      text=True, capture_output=True, check=True)
            self.assertEqual(json.loads(produced.stdout)["status"], "PROVED")
            checked = subprocess.run(prefix + ["check", str(path), "--expect", "P -> P", "--kind", "logic", "--json"],
                                     text=True, capture_output=True, check=True)
            self.assertTrue(json.loads(checked.stdout)["valid"])
            rejected = subprocess.run(prefix + ["check", str(path), "--expect", "Q -> Q", "--kind", "logic"],
                                      text=True, capture_output=True, check=False)
            self.assertEqual(rejected.returncode, 1)


if __name__ == "__main__":
    unittest.main()

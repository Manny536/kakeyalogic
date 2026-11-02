"""Command-line mathematics application: python -m kakeyalogic.prover."""

import argparse
import json
import sys
from pathlib import Path

from .engine import load_receipt, run, verify


def _describe(receipt):
    print(receipt["status"])
    print(receipt["problem"]["statement"])
    for assumption in receipt["problem"].get("assumptions", []):
        print("  Given: " + assumption)
    if "reason" in receipt:
        print(receipt["reason"])
    certificate = receipt["certificate"]
    if not certificate:
        return
    if "assignment" in certificate:
        print("Counterexample: " + json.dumps(certificate["assignment"], sort_keys=True))
    if "solution" in certificate:
        solution = certificate["solution"]
        if solution["classification"] == "UNIQUE":
            print("; ".join(name + " = " + value for name, value in
                            zip(solution["variables"], solution["particular"])) or "Unique empty assignment.")
        elif solution["classification"] == "PARAMETRIC":
            print("Variable order: " + ", ".join(solution["variables"]))
            print("Particular vector: " + ", ".join(solution["particular"]))
            for parameter, vector in zip(solution["parameters"], solution["basis"]):
                print("  + " + parameter + " * (" + ", ".join(vector) + ")")
        else:
            print("Replayed row operations establish 0 = 1; no rational solution.")
    print("Certificate checked by Frontier Math Rework.")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Frontier Math Rework — independent exact proof checker and solver")
    commands = parser.add_subparsers(dest="command", required=True)
    for command, help_text in (("prove", "Classical propositional theorem proving"),
                               ("identity", "Polynomial identities over Q"),
                               ("solve", "Linear equations over Q, separated by semicolons")):
        child = commands.add_parser(command, help=help_text)
        child.add_argument("statement")
        child.add_argument("--json", action="store_true", help="Print the full replayable receipt")
        child.add_argument("--out", type=Path, help="Save a JSON proof receipt")
        if command == "prove":
            child.add_argument("--given", action="append", default=[], help="Explicit hypothesis; repeatable")
            child.add_argument("--max-steps", type=int, default=5000)
        if command == "solve":
            child.add_argument("--variables", nargs="+", help="Explicit variable order, including unused variables")
    check = commands.add_parser("check", help="Independently replay a saved certificate")
    check.add_argument("file", type=Path)
    check.add_argument("--expect", help="Require this exact statement, kind and hypotheses below")
    check.add_argument("--kind", choices=("logic", "identity", "linear"))
    check.add_argument("--given", action="append", default=[])
    check.add_argument("--variables", nargs="+")
    check.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "check":
            if (args.expect is None) != (args.kind is None):
                parser.error("Use --expect and --kind together to bind the full expected problem.")
            if args.expect is None and (args.given or args.variables):
                parser.error("--given and --variables require --expect and --kind.")
            if args.file.stat().st_size > 4_000_000:
                raise ValueError("Certificate file limit is 4 MB.")
            receipt = load_receipt(args.file.read_text(encoding="utf-8"))
            expected = None
            if args.expect is not None:
                expected = {"kind": args.kind, "statement": args.expect}
                if args.kind == "logic":
                    expected["assumptions"] = args.given
                elif args.given:
                    parser.error("--given is supported only for logic.")
                if args.variables is not None:
                    if args.kind != "linear":
                        parser.error("--variables is supported only for linear systems.")
                    expected["variables"] = args.variables
            result = verify(receipt, expected_problem=expected)
            if args.json:
                print(json.dumps(result, indent=2))
            elif result["valid"]:
                _describe(receipt)
            else:
                print("REJECTED: " + result["reason"])
            return 0 if result["valid"] else 1
        problem = {"kind": {"prove": "logic", "identity": "identity", "solve": "linear"}[args.command],
                   "statement": args.statement}
        if args.command == "prove":
            problem["assumptions"] = args.given
        if args.command == "solve" and args.variables is not None:
            problem["variables"] = args.variables
        receipt = run(problem, max_steps=getattr(args, "max_steps", 5000))
        encoded = json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
        if args.out:
            args.out.write_text(encoded, encoding="utf-8")
        if args.json:
            print(encoded, end="")
        else:
            _describe(receipt)
            if args.out:
                print("Saved: " + str(args.out))
        return 2 if receipt["certificate"] is None else 0
    except (OSError, ValueError, RecursionError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

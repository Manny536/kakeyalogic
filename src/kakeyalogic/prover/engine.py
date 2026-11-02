"""Problem-bound proof receipts and the public run/verify API."""

import hashlib
import json

from . import kernel
from .syntax import BudgetExceeded, InvalidProblem

SCHEMA = "frontier-math-rework/certificate-v1"
# Retain replay of previously saved records; new output uses the current name.
_PREVIOUS_SCHEMA = "love-labs-prover/0.1"


def fingerprint(problem):
    """Bind exact source, assumptions, domain/kind, and declared variable order."""
    source = json.dumps(problem, ensure_ascii=True, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def run(problem, *, max_steps=5000):
    """Produce a certificate and return success only after independent replay.

    UNKNOWN and INVALID always carry a null certificate. No conclusion is
    inferred from search exhaustion. Inputs must already be in the formal DSL.
    """
    receipt = {"schema": SCHEMA, "problem": problem, "problem_sha256": None,
               "status": "INVALID", "certificate": None, "statistics": {}}
    try:
        kind = kernel.validate_problem(problem)
        receipt["problem_sha256"] = fingerprint(problem)
        if type(max_steps) is not int or not 1 <= max_steps <= kernel.MAX_NODES:
            raise InvalidProblem("Search budget must be an integer from 1 through 20000.")
        # Lazy imports let certificate verification run without either producer.
        from . import search, solver  # pylint: disable=import-outside-toplevel
        if kind == "logic":
            certificate, statistics = search.prove(problem, max_steps)
        elif kind == "identity":
            certificate, statistics = solver.identity(problem)
        else:
            certificate, statistics = solver.linear(problem)
        status = kernel.check(problem, certificate)
        return dict(receipt, status=status, certificate=certificate, statistics=statistics)
    except (BudgetExceeded, RecursionError) as error:
        receipt.update(status="UNKNOWN", reason=str(error) or "Recursion budget exhausted.")
    except (InvalidProblem, ValueError, TypeError, KeyError, OverflowError) as error:
        receipt.update(reason=str(error))
    return receipt


def verify(receipt, *, expected_problem=None):
    """Re-derive the status; ignore producer statistics and trust no saved flag.

    expected_problem binds a received certificate to the caller's own complete
    problem. A digest alone is integrity metadata, not authentication.
    """
    try:
        if not isinstance(receipt, dict):
            raise InvalidProblem("A receipt must be a JSON object.")
        required = {"schema", "problem", "problem_sha256", "status", "certificate", "statistics"}
        if not required.issubset(receipt) or not set(receipt).issubset(required | {"reason"}):
            raise InvalidProblem("Malformed proof receipt.")
        if receipt["schema"] not in (SCHEMA, _PREVIOUS_SCHEMA):
            raise InvalidProblem("Unsupported proof receipt version.")
        problem = receipt["problem"]
        kernel.validate_problem(problem)
        if expected_problem is not None and fingerprint(problem) != fingerprint(expected_problem):
            raise InvalidProblem("Receipt does not match the expected problem and assumptions.")
        if receipt["problem_sha256"] != fingerprint(problem):
            raise InvalidProblem("Problem digest does not match its exact source.")
        if not isinstance(receipt["statistics"], dict):
            raise InvalidProblem("Malformed producer statistics.")
        status = kernel.check(problem, receipt["certificate"])
        if receipt["status"] != status:
            raise InvalidProblem("Saved status disagrees with the checked mathematical conclusion.")
        return {"valid": True, "status": status, "problem_sha256": receipt["problem_sha256"]}
    except (ValueError, TypeError, KeyError, IndexError, RecursionError, OverflowError) as error:
        return {"valid": False, "status": "REJECTED", "reason": str(error)}


def load_receipt(source):
    """Read bounded JSON and reject ambiguous duplicate fields and nonfinite values."""
    if not isinstance(source, str) or len(source.encode("utf-8")) > 4_000_000:
        raise InvalidProblem("Certificate file limit is 4 MB.")

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise InvalidProblem("Duplicate JSON field: " + key)
            result[key] = value
        return result

    def reject_constant(value):
        raise InvalidProblem("Nonfinite JSON value: " + value)

    try:
        return json.loads(source, object_pairs_hook=pairs, parse_constant=reject_constant)
    except RecursionError as error:
        raise InvalidProblem("Certificate JSON nesting limit exceeded.") from error

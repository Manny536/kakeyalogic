"""Execute and independently verify the first Frontier Math Rework examples."""

import json

from kakeyalogic.prover import run, verify

CASES = [
    ("Contraposition", {"kind": "logic", "statement": "(P -> Q) -> (~Q -> ~P)"}),
    ("Modus ponens", {"kind": "logic", "statement": "Q", "assumptions": ["P", "P -> Q"]}),
    ("Square expansion", {"kind": "identity", "statement": "(x+y)^2=x^2+2*x*y+y^2"}),
    ("False expansion", {"kind": "identity", "statement": "(x+y)^2=x^2+y^2"}),
    ("Unique solution", {"kind": "linear", "statement": "2*x+y=7;x-y=2"}),
    ("Solution family", {"kind": "linear", "statement": "x+2*y-z=3"}),
    ("Inconsistent system", {"kind": "linear", "statement": "x=1;x=2"}),
]


def main():
    results = []
    for label, problem in CASES:
        receipt = run(problem)
        checked = verify(receipt, expected_problem=problem)
        if not checked["valid"]:
            raise RuntimeError(label + ": " + str(checked))
        results.append({"example": label, "status": checked["status"], "receipt": receipt})
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

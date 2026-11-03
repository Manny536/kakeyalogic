"""Check source parity and standalone browser-bundle execution."""

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BrowserBundleTests(unittest.TestCase):
    """The published checker must match and run without repository imports."""

    def test_bundle_is_current(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/build_frontier_web.py"), "--check"],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_standalone_bundle_proves_solves_and_rejects_corruption(self):
        bundle = json.loads((ROOT / "frontier-math-rework/engine-sources.json").read_text())
        self.assertEqual(bundle["schema"], "frontier-math-rework/browser-sources-v1")
        with tempfile.TemporaryDirectory() as directory:
            unpacked = Path(directory)
            for item in bundle["files"]:
                self.assertEqual(hashlib.sha256(item["source"].encode()).hexdigest(), item["sha256"])
                target = unpacked / item["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(item["source"], encoding="utf-8")
            script = r'''
import copy,json,sys
sys.path.insert(0,sys.argv[1])
from kakeyalogic.prover import run,verify
cases=[
 ({"kind":"logic","statement":"(P & Q) -> (Q & P)"},"PROVED"),
 ({"kind":"logic","statement":"P -> Q"},"DISPROVED"),
 ({"kind":"identity","statement":"(x+y)^2=x^2+2*x*y+y^2"},"PROVED"),
 ({"kind":"linear","statement":"2*x+y=7;x-y=2"},"UNIQUE"),
 ({"kind":"linear","statement":"x+y=4"},"PARAMETRIC"),
 ({"kind":"linear","statement":"x=1;x=2"},"INCONSISTENT"),
]
for problem,status in cases:
 receipt=run(problem)
 assert receipt["status"]==status,receipt
 assert verify(receipt,expected_problem=problem)["valid"]
bad=copy.deepcopy(run(cases[0][0]))
bad["certificate"]["nodes"][0]["rule"]="untrusted_axiom"
assert not verify(bad)["valid"]
print("standalone browser package cases pass")
'''
            result = subprocess.run([sys.executable, "-I", "-c", script, str(unpacked)],
                                    cwd=directory, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_runtime_pin_matches_worker_and_rejects_changed_archive(self):
        spec = importlib.util.spec_from_file_location("frontier_pages", ROOT / "tools/build_frontier_pages.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        worker = (ROOT / "frontier-math-rework/worker.js").read_text()
        self.assertIn('const PYODIDE_VERSION = "' + module.RUNTIME_VERSION + '"', worker)
        self.assertNotIn("cdn.jsdelivr.net", worker)
        with tempfile.TemporaryDirectory() as directory:
            changed = Path(directory) / "changed.tar.bz2"
            changed.write_bytes(b"not the pinned runtime")
            with self.assertRaisesRegex(ValueError, "digest"):
                module.runtime_archive(changed)


if __name__ == "__main__":
    unittest.main()

"""Build the exact Python source bundle consumed by the static browser app."""

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "frontier-math-rework" / "engine-sources.json"


def build_bundle():
    """Bundle the installed package's source, without changing its checker."""
    source_root = ROOT / "src"
    package = source_root / "kakeyalogic"
    paths = sorted(list(package.rglob("*.py")) + list((package / "data").glob("*.json")))
    files = []
    for path in paths:
        source = path.read_text(encoding="utf-8")
        files.append({"path": path.relative_to(source_root).as_posix(), "source": source,
                      "sha256": hashlib.sha256(source.encode("utf-8")).hexdigest()})
    inventory = "\n".join(item["path"] + "\0" + item["sha256"] for item in files)
    return {"schema": "frontier-math-rework/browser-sources-v1", "files": files,
            "engine_fingerprint": hashlib.sha256(inventory.encode("utf-8")).hexdigest()}


def main():
    """Generate a deterministic asset or reject a stale committed bundle."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    encoded = json.dumps(build_bundle(), ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding="utf-8") != encoded:
            parser.exit(1, "Browser engine bundle is stale. Run python tools/build_frontier_web.py.\n")
        print("Browser engine bundle matches the Python source.")
    else:
        TARGET.parent.mkdir(parents=True, exist_ok=True)
        TARGET.write_text(encoded, encoding="utf-8")
        print("Built " + str(TARGET.relative_to(ROOT)))


if __name__ == "__main__":
    main()

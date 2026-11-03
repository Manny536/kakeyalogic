"""Stage GitHub Pages with a pinned, same-origin browser Python runtime."""

import argparse
import hashlib
import json
import shutil
import subprocess
import tarfile
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_VERSION = "314.0.7"
RUNTIME_URL = (
    "https://github.com/pyodide/pyodide/releases/download/" + RUNTIME_VERSION
    + "/pyodide-core-" + RUNTIME_VERSION + ".tar.bz2"
)
# The SHA-256 digest published on the official Pyodide GitHub release asset.
RUNTIME_SHA256 = "2abdcc2e35208af406e07724cffa85bc582ced97e9028383ecf5462541393f95"
RUNTIME_FILES = (
    "pyodide.js", "pyodide.mjs", "pyodide.asm.mjs", "pyodide.asm.wasm",
    "pyodide-lock.json", "python_stdlib.zip", "package.json",
)


def runtime_archive(provided=None):
    """Download once and verify the official archive before using any member."""
    path = provided or Path(tempfile.gettempdir()) / "frontier-math-runtime" / (
        "pyodide-core-" + RUNTIME_VERSION + ".tar.bz2"
    )
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(RUNTIME_URL, timeout=60) as response:
            data = response.read(20_000_001)
        if len(data) > 20_000_000:
            raise ValueError("Runtime archive exceeds the expected size bound.")
        if hashlib.sha256(data).hexdigest() != RUNTIME_SHA256:
            raise ValueError("Downloaded runtime digest differs from the pinned release.")
        path.write_bytes(data)
    if hashlib.sha256(path.read_bytes()).hexdigest() != RUNTIME_SHA256:
        raise ValueError("Runtime archive digest differs from the pinned release.")
    return path


def install_runtime(destination, archive_path=None):
    """Extract only named regular files, never archive paths or symbolic links."""
    path = runtime_archive(archive_path)
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(path, "r:bz2") as archive:
        for name in RUNTIME_FILES:
            member = archive.getmember("pyodide/" + name)
            if not member.isfile() or not 0 < member.size < 15_000_000:
                raise ValueError("Unexpected runtime archive member: " + name)
            source = archive.extractfile(member)
            if source is None:
                raise ValueError("Missing runtime archive member: " + name)
            with source:
                (destination / name).write_bytes(source.read())
    (destination / "runtime.json").write_text(json.dumps({
        "version": RUNTIME_VERSION, "source": RUNTIME_URL,
        "archive_sha256": RUNTIME_SHA256,
        "license": "https://github.com/pyodide/pyodide/blob/" + RUNTIME_VERSION + "/LICENSE",
    }, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def stage_site(destination, archive_path=None):
    """Copy tracked public content and supply the runtime only in the build output."""
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    destination.mkdir(parents=True, exist_ok=True)
    for name in tracked:
        if not name or name.startswith((".git", ".openai/")):
            continue
        source = ROOT / name
        if source.is_file():
            target = destination / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    install_runtime(destination / "frontier-math-rework" / "runtime", archive_path)
    (destination / ".nojekyll").touch()


def main():
    """Build a self-contained static Pages artifact."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    parser.add_argument("--runtime-archive", type=Path)
    args = parser.parse_args()
    destination = args.output.resolve()
    if destination == ROOT or destination in ROOT.parents:
        parser.error("Choose a dedicated build-output directory.")
    stage_site(destination, args.runtime_archive)
    print("Pages build ready: " + str(destination))


if __name__ == "__main__":
    main()

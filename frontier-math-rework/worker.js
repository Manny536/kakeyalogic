/* The browser executes the same Python package as the installed application. */
"use strict";

const PYODIDE_VERSION = "314.0.7";
const PYODIDE_URL = new URL("./runtime/", self.location.href).href;
let initialization;
let queue = Promise.resolve();

function progress(stage, message) {
  self.postMessage({ type: "progress", stage, message });
}

async function sha256(text, pyodide) {
  if (self.crypto?.subtle) {
    const digest = await self.crypto.subtle.digest("SHA-256", new TextEncoder().encode(text));
    return Array.from(new Uint8Array(digest), (byte) => byte.toString(16).padStart(2, "0")).join("");
  }
  // HTTP previews lack Web Crypto; retain the same check with Python's SHA-256.
  pyodide.globals.set("_bundle_hash_text", text);
  return pyodide.runPython("import hashlib; hashlib.sha256(_bundle_hash_text.encode('utf-8')).hexdigest()");
}

async function initialize() {
  if (!initialization) {
    initialization = (async () => {
      progress("runtime", "Preparing the local verification engine…");
      const { loadPyodide } = await import(`${PYODIDE_URL}pyodide.mjs`);
      const pyodide = await loadPyodide({ indexURL: PYODIDE_URL });
      if (pyodide.version !== PYODIDE_VERSION) throw new Error("Unexpected Python runtime version.");
      progress("source", "Loading the mathematics checker…");
      const response = await fetch(new URL("./engine-sources.json", self.location.href), { cache: "no-cache" });
      if (!response.ok) throw new Error("The checker source could not be loaded. Please retry.");
      const bundle = await response.json();
      if (bundle.schema !== "frontier-math-rework/browser-sources-v1" || !Array.isArray(bundle.files)) {
        throw new Error("Unsupported browser checker bundle.");
      }
      const paths = new Set();
      for (const file of bundle.files) {
        if (typeof file.path !== "string" || !/^kakeyalogic\/[A-Za-z0-9_./-]+$/.test(file.path)
            || file.path.includes("..") || paths.has(file.path) || typeof file.source !== "string") {
          throw new Error("Invalid browser source inventory.");
        }
        paths.add(file.path);
        if (await sha256(file.source, pyodide) !== file.sha256) throw new Error("Checker source integrity mismatch. Please reload.");
        const path = `/app/${file.path}`;
        pyodide.FS.mkdirTree(path.slice(0, path.lastIndexOf("/")));
        pyodide.FS.writeFile(path, file.source, { encoding: "utf8" });
      }
      const inventory = bundle.files.map((file) => `${file.path}\0${file.sha256}`).join("\n");
      if (await sha256(inventory, pyodide) !== bundle.engine_fingerprint) throw new Error("Checker inventory integrity mismatch.");
      pyodide.runPython(`
import sys, json
sys.path.insert(0, "/app")
from kakeyalogic.prover import run as _run_problem, verify as _verify_receipt
from kakeyalogic.prover.engine import load_receipt as _load_receipt
`);
      progress("ready", "Ready. Checks run in your browser.");
      return { pyodide, engineFingerprint: bundle.engine_fingerprint };
    })();
  }
  return initialization;
}

async function handle(request) {
  const { id, type } = request || {};
  try {
    if (typeof id !== "string" || !["initialize", "run", "verify"].includes(type)) {
      throw new Error("Unknown checker request.");
    }
    const { pyodide, engineFingerprint } = await initialize();
    if (type === "initialize") {
      self.postMessage({ id, type: "ready", engineFingerprint });
      return;
    }
    const started = performance.now();
    // Only data crosses this boundary. User input is never evaluated as Python.
    pyodide.globals.set("_browser_request_json", JSON.stringify(request));
    const output = pyodide.runPython(`
_browser_request = json.loads(_browser_request_json)
try:
    if _browser_request["type"] == "run":
        _browser_problem = _browser_request["problem"]
        _browser_receipt = _run_problem(_browser_problem, max_steps=_browser_request.get("maxSteps", 5000))
        _browser_verification = _verify_receipt(_browser_receipt, expected_problem=_browser_problem)
    else:
        _browser_receipt = _load_receipt(_browser_request["source"])
        _browser_verification = _verify_receipt(_browser_receipt, expected_problem=_browser_request.get("expectedProblem"))
    _browser_output = {"receipt": _browser_receipt, "verification": _browser_verification}
except (ValueError, TypeError, KeyError, IndexError, RecursionError, OverflowError) as _input_error:
    _browser_output = {"inputError": str(_input_error)}
json.dumps(_browser_output, ensure_ascii=False)
`);
    const payload = JSON.parse(output);
    if (payload.inputError) throw new Error(payload.inputError);
    self.postMessage({ id, type: "result", operation: type, ...payload,
      elapsedMs: Math.round(performance.now() - started), engineFingerprint });
  } catch (error) {
    self.postMessage({ id, type: "error", message: error instanceof Error ? error.message : String(error) });
  }
}

self.onmessage = (event) => {
  queue = queue.then(() => handle(event.data)).catch((error) => {
    self.postMessage({ id: event.data?.id, type: "error", message: String(error) });
  });
};

# Frontier Math Rework: browser application contract

Solance owns the Python bundle, worker, validation, and GitHub Pages pipeline.
Copilot owns the complete responsive interface in `frontier-math-rework/index.html`,
`app.js`, and `styles.css`. The existing repository-root `index.html` is retained;
the application is published at `/kakeyalogic/frontier-math-rework/`.

## Engine protocol

Create `new Worker('./worker.js', {type:'module'})`. Send unique string IDs; match responses to the
current request and ignore messages from cancelled/terminated workers.

```js
worker.postMessage({id:'boot', type:'initialize'});
worker.postMessage({id:'run-1', type:'run', problem, maxSteps:5000});
worker.postMessage({id:'check-1', type:'verify', source:rawJsonText, expectedProblem});
```

`expectedProblem` is optional; if omitted, replay checks the certificate's own
declared problem. A "match current problem" control must use the user's explicit
worksheet input. Do not silently derive that expectation from an imported file.
Always show the imported problem and hypotheses alongside its verification.

The engine sends:

- `{type:'progress', stage, message}` during initialization.
- `{id, type:'ready', engineFingerprint}` when initialized.
- `{id, type:'result', operation, receipt, verification, elapsedMs, engineFingerprint}`.
- `{id, type:'error', message}` on a failed operation.

`verification.valid` is the acceptance signal, derived by the independent checker.
Never display a saved certificate's self-reported status as accepted when replay
rejects it. An `INVALID` or `UNKNOWN` run has a null certificate and no mathematical
conclusion. `DISPROVED` and `INCONSISTENT` are legitimate checked results.

## Formal problem input

```json
{"kind":"logic","statement":"Q","assumptions":["P","P -> Q"]}
{"kind":"identity","statement":"(x+y)^2=x^2+2*x*y+y^2"}
{"kind":"linear","statement":"2*x+y=7;x-y=2"}
{"kind":"linear","statement":"x+y=4","variables":["x","y","z"]}
```

Omit `variables` to infer them. Split logic assumptions into nonempty lines.
For linear equations, translate input newlines to semicolons; preserve source
text thereafter so downloaded receipts can match the same explicit problem.
The supported arithmetic is rational; use `1/2`, explicit `*`, and powers `^`.

Logic receipts use `sequent` nodes or Boolean `countermodel` assignments.
Identity receipts contain a common polynomial normal form or rational witness.
Linear receipts contain row operations, RREF, and `solution` with classification,
ordered variables, particular vector, nullspace basis, and free parameters.
Use the existing Python documentation for these shapes; do not invent results.

## Required complete interface

- Calm academic workspace; cream paper, deep green/navy, clear typography, no
  product version labels or alternate application names. Responsive and accessible.
- Prove / polynomial identity / linear system modes; explicit hypotheses and
  optional variable order; syntax help and runnable examples for each.
- Initialize/loading/retry, busy, stop, empty, error, unknown and checked states.
  Stop must terminate the worker and create a fresh one for the next request.
- Human-readable exact solutions/counterexamples, proof-rule/row-operation trace,
  and an expandable JSON certificate inspector.
- Download/copy the actual receipt, import a bounded JSON file (4 MB), and replay
  it independently, with an optional explicit expected-problem match.
- Saved sessions on this device, with restore and delete. Bound history storage,
  catch quota/disabled-storage errors, and never claim a save that failed.
- Examples/research/help views with working navigation. Link the research notes
  without reproducing their video quotations. Provide the supported scope plainly.
- Ctrl/Cmd+Enter to run; labelled controls, visible keyboard focus, readable error
  feedback. User strings must use textContent, not unsanitized innerHTML.

The worker loads the pinned Pyodide runtime and the exact repository Python
package from this site's own assets. It sends no problem or certificate to a
remote computation service. The first load needs a network connection for those
static runtime assets. Runtime files are generated during the Pages build.

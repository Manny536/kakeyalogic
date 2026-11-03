"use strict";

const MAX_RECEIPT_BYTES = 4_000_000;
const MAX_SESSIONS = 20;
const MAX_SESSION_BYTES = 800_000;
const SESSION_KEY = "kakeyalogic.frontierMathRework.sessions.v1";
const examples = [
  {
    title: "Contraposition",
    mode: "logic",
    statement: "(P -> Q) -> (~Q -> ~P)",
    assumptions: "",
    variables: "",
    description: "A classical propositional theorem, checked with a sequent derivation.",
  },
  {
    title: "Modus ponens with hypotheses",
    mode: "logic",
    statement: "Q",
    assumptions: "P\nP -> Q",
    variables: "",
    description: "Make both hypotheses explicit and inspect how they support the goal.",
  },
  {
    title: "A countermodel",
    mode: "logic",
    statement: "P",
    assumptions: "",
    variables: "",
    description: "A valid disproof includes a Boolean assignment that falsifies the claim.",
  },
  {
    title: "Square of a sum",
    mode: "identity",
    statement: "(x+y)^2=x^2+2*x*y+y^2",
    assumptions: "",
    variables: "",
    description: "Compare exact polynomial normal forms over the rational field.",
  },
  {
    title: "An identity that fails",
    mode: "identity",
    statement: "(x+y)^2=x^2+y^2",
    assumptions: "",
    variables: "",
    description: "Inspect an exact rational witness when two polynomials differ.",
  },
  {
    title: "A unique linear solution",
    mode: "linear",
    statement: "2*x+y=7\nx-y=2",
    assumptions: "",
    variables: "",
    description: "Replay exact row operations to recover the unique rational solution.",
  },
  {
    title: "A parametric family",
    mode: "linear",
    statement: "x+y=4",
    assumptions: "",
    variables: "x, y, z",
    description: "Declare a variable order to include free variables in the solution family.",
  },
  {
    title: "An inconsistent system",
    mode: "linear",
    statement: "x=1\nx=2",
    assumptions: "",
    variables: "",
    description: "A checked contradiction row identifies an inconsistent system.",
  },
];

const modeDetails = {
  logic: {
    label: "Proposition",
    placeholder: "(P -> Q) -> (~Q -> ~P)",
    help: "Use ~, &, |, ->, <->, true, and false. Hypotheses go on separate lines; parentheses make grouping clear.",
  },
  identity: {
    label: "Polynomial equation",
    placeholder: "(x+y)^2=x^2+2*x*y+y^2",
    help: "Use explicit multiplication (2*x), exact rational constants (1/2), and nonnegative powers (^).",
  },
  linear: {
    label: "Linear equations",
    placeholder: "2*x+y=7\nx-y=2",
    help: "Enter one affine equation per line. Use exact fractions and explicit multiplication; lines become semicolon-separated equations.",
  },
};

const elements = {
  engineDot: document.getElementById("engine-dot"),
  engineStatus: document.getElementById("engine-status"),
  retryEngine: document.getElementById("retry-engine"),
  mode: document.getElementById("mode-select"),
  assumptionsField: document.getElementById("assumptions-field"),
  assumptions: document.getElementById("assumptions-input"),
  statementLabel: document.getElementById("statement-label"),
  statement: document.getElementById("statement-input"),
  syntaxHelp: document.getElementById("syntax-help"),
  variablesField: document.getElementById("variables-field"),
  variables: document.getElementById("variables-input"),
  runButton: document.getElementById("run-button"),
  stopButton: document.getElementById("stop-button"),
  clearButton: document.getElementById("clear-button"),
  shortcutHelp: document.getElementById("shortcut-help"),
  resultState: document.getElementById("result-state"),
  resultEmpty: document.getElementById("result-empty"),
  resultContent: document.getElementById("result-content"),
  resultSummary: document.getElementById("result-summary"),
  problemSummary: document.getElementById("problem-summary"),
  traceSection: document.getElementById("trace-section"),
  traceHeading: document.getElementById("trace-heading"),
  traceContent: document.getElementById("trace-content"),
  receiptJson: document.getElementById("receipt-json"),
  receiptDetails: document.getElementById("receipt-details"),
  copyReceipt: document.getElementById("copy-receipt"),
  downloadReceipt: document.getElementById("download-receipt"),
  saveSession: document.getElementById("save-session"),
  resultFeedback: document.getElementById("result-feedback"),
  receiptFile: document.getElementById("receipt-file"),
  fileName: document.getElementById("file-name"),
  receiptInput: document.getElementById("receipt-input"),
  matchProblem: document.getElementById("match-problem"),
  verifyButton: document.getElementById("verify-button"),
  importMessage: document.getElementById("import-message"),
  sessionCount: document.getElementById("session-count"),
  sessionList: document.getElementById("session-list"),
  sessionsEmpty: document.getElementById("sessions-empty"),
  sessionsMessage: document.getElementById("sessions-message"),
  importHeading: document.getElementById("import-heading"),
  examplesList: document.getElementById("examples-list"),
  tabs: Array.from(document.querySelectorAll('[role="tab"][data-view]')),
};

let worker = null;
let workerGeneration = 0;
let engineReady = false;
let pendingRequest = null;
let currentReceipt = null;
let currentVerification = null;
let currentOperation = null;
let savedSessions = [];
let storageAvailable = true;

function node(tag, className, text) {
  const result = document.createElement(tag);
  if (className) result.className = className;
  if (text !== undefined) result.textContent = text;
  return result;
}

function setEngineState(state, message) {
  elements.engineStatus.textContent = message;
  elements.engineDot.className = `engine-dot engine-${state}`;
  elements.retryEngine.hidden = state !== "error";
  engineReady = state === "ready";
  updateControls();
}

function setResultState(state, label, emptyMessage) {
  elements.resultState.className = `state-pill state-${state}`;
  elements.resultState.textContent = label;
  if (emptyMessage !== undefined) elements.resultEmpty.textContent = emptyMessage;
}

function clearResult() {
  currentReceipt = null;
  currentVerification = null;
  elements.resultContent.hidden = true;
  elements.resultEmpty.hidden = false;
  elements.resultSummary.replaceChildren();
  elements.problemSummary.replaceChildren();
  elements.problemSummary.hidden = true;
  elements.traceContent.replaceChildren();
  elements.traceSection.hidden = true;
  elements.receiptJson.textContent = "";
  elements.receiptDetails.open = false;
  elements.resultFeedback.textContent = "";
  updateControls();
}

function updateControls() {
  const isBusy = Boolean(pendingRequest && pendingRequest.type !== "initialize");
  elements.runButton.disabled = !engineReady || isBusy;
  elements.stopButton.hidden = !isBusy;
  elements.retryEngine.disabled = Boolean(pendingRequest);
  elements.verifyButton.disabled = !engineReady || isBusy || !elements.receiptInput.value.trim();
  const hasReceipt = Boolean(currentReceipt);
  elements.copyReceipt.disabled = !hasReceipt;
  elements.downloadReceipt.disabled = !hasReceipt;
  elements.saveSession.disabled = !hasReceipt || currentVerification?.valid !== true;
}

function makeWorker() {
  workerGeneration += 1;
  const generation = workerGeneration;
  worker = new Worker("./worker.js", { type: "module" });
  worker.onmessage = ({ data }) => {
    if (generation !== workerGeneration || !data || typeof data !== "object") return;
    if (data.type === "progress") {
      if (pendingRequest?.type === "initialize") {
        setEngineState("loading", typeof data.message === "string" ? data.message : "Preparing the checker…");
      }
      return;
    }
    if (!pendingRequest || data.id !== pendingRequest.id) return;
    if (data.type === "ready" && pendingRequest.type === "initialize") {
      pendingRequest = null;
      setEngineState("ready", "Ready · checks run in your browser");
      elements.shortcutHelp.textContent = "Press Ctrl/Cmd + Enter to run the current problem.";
      return;
    }
    if (data.type === "result" && pendingRequest.type !== "initialize") {
      const request = pendingRequest;
      pendingRequest = null;
      currentOperation = request.type;
      currentReceipt = data.receipt && typeof data.receipt === "object" ? data.receipt : null;
      currentVerification = data.verification && typeof data.verification === "object" ? data.verification : null;
      renderResult(data);
      setEngineState("ready", "Ready · checks run in your browser");
      return;
    }
    if (data.type === "error") {
      const request = pendingRequest;
      pendingRequest = null;
      if (request.type === "initialize") {
        setEngineState("error", typeof data.message === "string" ? data.message : "The checker could not start.");
        elements.shortcutHelp.textContent = "Check your connection, then retry the checker.";
      } else {
        setEngineState("ready", "Ready · checks run in your browser");
        showOperationError(typeof data.message === "string" ? data.message : "The checker could not complete this request.");
      }
    }
  };
  worker.onerror = (event) => {
    if (generation !== workerGeneration) return;
    event.preventDefault();
    const request = pendingRequest;
    pendingRequest = null;
    const message = "The checker stopped unexpectedly. Retry to start a fresh worker.";
    if (request?.type === "initialize") setEngineState("error", message);
    else {
      setEngineState("error", message);
      showOperationError(message);
    }
  };
}

function initializeEngine() {
  if (pendingRequest) return;
  try {
    if (!worker) makeWorker();
    const id = `initialize-${workerGeneration}-${crypto.randomUUID()}`;
    pendingRequest = { id, type: "initialize" };
    setEngineState("loading", "Starting the local checker…");
    elements.shortcutHelp.textContent = "Loading the browser mathematics engine. The first load needs a network connection.";
    worker.postMessage({ id, type: "initialize" });
  } catch (error) {
    pendingRequest = null;
    if (worker) worker.terminate();
    worker = null;
    const message = error instanceof Error ? error.message : "The checker could not start in this browser.";
    setEngineState("error", message);
    elements.shortcutHelp.textContent = "Check your browser settings, then retry the checker.";
  }
}

function ensureWorkerForNextRequest() {
  if (!engineReady && !pendingRequest) initializeEngine();
}

function modeProblem() {
  const mode = elements.mode.value;
  const statement = elements.statement.value;
  if (!statement.trim()) {
    elements.statement.focus();
    elements.statement.setCustomValidity("Enter a formal problem before running the checker.");
    elements.statement.reportValidity();
    elements.statement.setCustomValidity("");
    return null;
  }
  if (mode === "logic") {
    return {
      kind: "logic",
      statement,
      assumptions: elements.assumptions.value.split(/\r?\n/).map((line) => line.trim()).filter(Boolean),
    };
  }
  if (mode === "identity") return { kind: "identity", statement };
  const problem = { kind: "linear", statement: statement.replace(/\r\n?/g, "\n").replace(/\n/g, ";") };
  const variables = elements.variables.value.trim().split(/[\s,]+/).filter(Boolean);
  if (variables.length) problem.variables = variables;
  return problem;
}

function sendOperation(type, payload) {
  if (!engineReady || pendingRequest || !worker) return;
  const id = `${type}-${workerGeneration}-${crypto.randomUUID()}`;
  pendingRequest = { id, type };
  currentOperation = type;
  setResultState("busy", type === "run" ? "Checking" : "Replaying", type === "run" ? "The checker is working through your problem…" : "The checker is independently replaying this receipt…");
  elements.resultContent.hidden = true;
  elements.resultEmpty.hidden = false;
  elements.resultFeedback.textContent = "";
  updateControls();
  worker.postMessage({ id, type, ...payload });
}

function runProblem(event) {
  if (event) event.preventDefault();
  const problem = modeProblem();
  if (!problem) return;
  if (!engineReady) {
    ensureWorkerForNextRequest();
    setResultState("loading", "Preparing", "The browser checker is starting. Run again when it is ready.");
    return;
  }
  sendOperation("run", { problem, maxSteps: 5000 });
}

function verifyReceipt() {
  const source = elements.receiptInput.value;
  if (!source.trim()) {
    elements.importMessage.textContent = "Choose a receipt file or paste receipt JSON first.";
    return;
  }
  if (new TextEncoder().encode(source).length > MAX_RECEIPT_BYTES) {
    elements.importMessage.textContent = "This receipt exceeds the 4 MB file limit.";
    return;
  }
  let expectedProblem;
  if (elements.matchProblem.checked) {
    expectedProblem = modeProblem();
    if (!expectedProblem) return;
  }
  elements.importMessage.textContent = "Sending the receipt to the independent checker…";
  if (!engineReady) {
    ensureWorkerForNextRequest();
    elements.importMessage.textContent = "The checker is starting. Replay the receipt when it is ready.";
    return;
  }
  const payload = { source };
  if (expectedProblem !== undefined) payload.expectedProblem = expectedProblem;
  sendOperation("verify", payload);
}

function stopOperation() {
  if (!pendingRequest || pendingRequest.type === "initialize") return;
  const wasBusy = pendingRequest.type;
  pendingRequest = null;
  workerGeneration += 1;
  if (worker) worker.terminate();
  worker = null;
  engineReady = false;
  currentReceipt = null;
  currentVerification = null;
  clearResult();
  setResultState("stopped", "Stopped", "This request was stopped. A fresh checker is starting.");
  setEngineState("idle", "Stopped · a fresh checker will start on the next request");
  elements.importMessage.textContent = wasBusy === "verify" ? "Certificate replay stopped." : "Problem run stopped.";
  worker = null;
  initializeEngine();
}

function showOperationError(message) {
  currentReceipt = null;
  currentVerification = null;
  elements.resultContent.hidden = true;
  elements.resultEmpty.hidden = false;
  elements.resultEmpty.textContent = message;
  setResultState("error", "Error", message);
  elements.resultFeedback.textContent = message;
  updateControls();
}

function displayProblem(problem) {
  const section = node("section", "checked-problem");
  section.append(node("h3", "", "Problem declared in this receipt"));
  const kindLabels = { logic: "Propositional logic", identity: "Polynomial identity", linear: "Linear system" };
  const kind = typeof problem?.kind === "string" ? problem.kind : "";
  section.append(node("p", "problem-kind", kindLabels[kind] || "Declared problem"));
  if (typeof problem?.statement === "string") {
    const statement = node("pre", "problem-statement");
    statement.textContent = problem.statement;
    section.append(statement);
  }
  if (Array.isArray(problem?.assumptions)) {
    const assumptions = node("div", "problem-hypotheses");
    assumptions.append(node("h4", "", "Hypotheses"));
    if (problem.assumptions.length) {
      const list = node("ul", "compact-list");
      for (const assumption of problem.assumptions) list.append(node("li", "", displayUserValue(assumption)));
      assumptions.append(list);
    } else assumptions.append(node("p", "muted-copy", "None declared."));
    section.append(assumptions);
  }
  if (Array.isArray(problem?.variables)) {
    section.append(node("p", "problem-variables", `Variable order: ${problem.variables.map(displayUserValue).join(", ")}`));
  }
  return section;
}

function displayUserValue(value) {
  if (typeof value === "string") return value;
  try {
    return JSON.stringify(value) ?? "Unrenderable value";
  } catch {
    return "Unrenderable value";
  }
}

function renderResult(data) {
  elements.resultContent.hidden = false;
  elements.resultEmpty.hidden = true;
  elements.resultSummary.replaceChildren();
  elements.problemSummary.replaceChildren();
  elements.problemSummary.hidden = true;
  elements.traceContent.replaceChildren();
  elements.traceSection.hidden = true;
  elements.receiptJson.textContent = currentReceipt ? JSON.stringify(currentReceipt, null, 2) : "";
  elements.resultFeedback.textContent = "";

  if (currentReceipt?.problem) {
    elements.problemSummary.append(displayProblem(currentReceipt.problem));
    elements.problemSummary.hidden = false;
  } else if (currentOperation === "verify") {
    const preview = safeProblemPreview(elements.receiptInput.value);
    if (preview) {
      elements.problemSummary.append(displayProblem(preview));
      elements.problemSummary.hidden = false;
    }
  }

  if (currentVerification?.valid === true) {
    const status = typeof currentVerification.status === "string" ? currentVerification.status : "Checked";
    setResultState("checked", "Independently checked", `${status}: the independent checker accepted this certificate.`);
    const banner = node("div", "verification-banner");
    banner.append(node("span", "verification-mark", "✓"));
    const text = node("div");
    text.append(node("strong", "", statusLabel(status)));
    text.append(node("p", "", "The independent checker replayed the certificate successfully."));
    if (Number.isFinite(data.elapsedMs)) text.append(node("p", "muted-copy", `Checker time: ${data.elapsedMs} ms`));
    banner.append(text);
    elements.resultSummary.append(banner);
    renderCheckedTrace(currentReceipt, status);
  } else {
    const message = currentReceipt?.status === "UNKNOWN"
      ? "The search budget was exhausted. No certificate or mathematical conclusion is available."
      : typeof currentVerification?.reason === "string"
        ? currentVerification.reason
        : "The independent checker did not accept this receipt. No mathematical conclusion is shown.";
    setResultState("rejected", "Not accepted", message);
    const banner = node("div", "verification-banner verification-rejected");
    banner.append(node("span", "verification-mark", "!"));
    const text = node("div");
    text.append(node("strong", "", currentReceipt?.status === "UNKNOWN" ? "No checked conclusion" : "Certificate not accepted"));
    text.append(node("p", "", message));
    banner.append(text);
    elements.resultSummary.append(banner);
    if (currentOperation === "verify") {
      const note = node("p", "muted-copy", "The receipt’s saved status is not treated as an accepted result.");
      elements.resultSummary.append(note);
    }
  }
  updateControls();
}

function safeProblemPreview(source) {
  try {
    const parsed = JSON.parse(source);
    return parsed && typeof parsed === "object" && parsed.problem && typeof parsed.problem === "object"
      ? parsed.problem
      : null;
  } catch {
    return null;
  }
}

function statusLabel(status) {
  const labels = {
    PROVED: "Proved",
    DISPROVED: "Disproved · checked counterexample",
    UNIQUE: "Unique rational solution",
    PARAMETRIC: "Parametric rational solution",
    INCONSISTENT: "Inconsistent · checked contradiction",
  };
  return labels[status] || status;
}

function renderCheckedTrace(receipt, status) {
  const certificate = receipt?.certificate;
  if (!certificate || typeof certificate !== "object") return;
  elements.traceContent.replaceChildren();
  elements.traceSection.hidden = false;
  elements.traceHeading.textContent = "Checked evidence and exact result";
  if (receipt.problem?.kind === "logic") renderLogicTrace(certificate);
  else if (receipt.problem?.kind === "identity") renderIdentityTrace(certificate, status);
  else if (receipt.problem?.kind === "linear") renderLinearTrace(certificate, status);
}

function renderLogicTrace(certificate) {
  if (certificate.method === "countermodel" && certificate.assignment && typeof certificate.assignment === "object") {
    const panel = node("div", "trace-block");
    panel.append(node("h4", "", "Checked countermodel"));
    panel.append(node("p", "muted-copy", "This assignment satisfies the declared hypotheses and falsifies the proposition."));
    const list = node("dl", "assignment-list");
    for (const [name, value] of Object.entries(certificate.assignment)) {
      list.append(node("dt", "", name), node("dd", "", value === true ? "true" : value === false ? "false" : String(value)));
    }
    panel.append(list);
    elements.traceContent.append(panel);
    return;
  }
  if (certificate.method !== "sequent" || !Array.isArray(certificate.nodes)) return;
  const labels = {
    id: "Identity · matching proposition",
    false_left: "False on the left",
    true_right: "True on the right",
    not_left: "Negation on the left",
    not_right: "Negation on the right",
    and_left: "Conjunction on the left",
    and_right: "Conjunction on the right",
    or_left: "Disjunction on the left",
    or_right: "Disjunction on the right",
    imp_left: "Implication on the left",
    imp_right: "Implication on the right",
  };
  const panel = node("div", "trace-block");
  panel.append(node("h4", "", "Sequent derivation"));
  const list = node("ol", "proof-trace");
  certificate.nodes.forEach((item, index) => {
    const detail = item && typeof item === "object" ? item : {};
    let text = labels[detail.rule] || "Proof rule";
    if (Number.isInteger(detail.index)) text += ` · formula ${detail.index + 1}`;
    if (Array.isArray(detail.children)) text += ` · premises ${detail.children.map((child) => Number.isInteger(child) ? child + 1 : String(child)).join(", ")}`;
    if (index === certificate.root) text += " · root";
    list.append(node("li", "", text));
  });
  panel.append(list);
  elements.traceContent.append(panel);
}

function formatMonomial(variables) {
  return variables.length ? variables.map((name) => String(name)).join("·") : "1";
}

function renderIdentityTrace(certificate, status) {
  const panel = node("div", "trace-block");
  if (certificate.method === "normalization" && Array.isArray(certificate.normal_form)) {
    panel.append(node("h4", "", "Common exact polynomial normal form"));
    const terms = certificate.normal_form.map((term) => {
      if (!Array.isArray(term) || term.length < 2) return JSON.stringify(term);
      const variables = Array.isArray(term[0]) ? term[0] : [];
      return variables.length ? `${term[1]}·${formatMonomial(variables)}` : String(term[1]);
    });
    panel.append(node("p", "exact-result", terms.length ? terms.join("  +  ") : "0"));
    panel.append(node("p", "muted-copy", "Both sides reduce to this same exact form."));
  } else if ((certificate.method === "evaluation" || certificate.method === "countermodel")
      && certificate.assignment && typeof certificate.assignment === "object") {
    panel.append(node("h4", "", "Exact counterexample"));
    panel.append(node("p", "muted-copy", "The checked rational assignment makes the two sides unequal."));
    const list = node("dl", "assignment-list");
    for (const [name, value] of Object.entries(certificate.assignment)) {
      list.append(node("dt", "", name), node("dd", "", String(value)));
    }
    panel.append(list);
  }
  if (status === "PROVED" || status === "DISPROVED") elements.traceContent.append(panel);
}

function renderLinearTrace(certificate, status) {
  if (certificate.method !== "row-reduction") return;
  const panel = node("div", "trace-block");
  panel.append(node("h4", "", "Reversible row operations"));
  const operations = Array.isArray(certificate.operations) ? certificate.operations : [];
  if (!operations.length) panel.append(node("p", "muted-copy", "No row operations were needed."));
  else {
    const list = node("ol", "proof-trace");
    operations.forEach((operation) => {
      if (!operation || typeof operation !== "object") return;
      let text = "Row operation";
      if (operation.op === "swap") text = `Swap R${operation.a + 1} and R${operation.b + 1}`;
      if (operation.op === "scale") text = `R${operation.row + 1} ← (${operation.factor}) · R${operation.row + 1}`;
      if (operation.op === "add") text = `R${operation.target + 1} ← R${operation.target + 1} + (${operation.factor}) · R${operation.source + 1}`;
      list.append(node("li", "", text));
    });
    panel.append(list);
  }
  if (Array.isArray(certificate.rref)) {
    panel.append(node("h4", "subheading", "Reduced row-echelon form"));
    const table = node("table", "matrix-table");
    table.setAttribute("aria-label", "Reduced row-echelon matrix");
    const body = node("tbody");
    for (const row of certificate.rref) {
      if (!Array.isArray(row)) continue;
      const tr = node("tr");
      for (const value of row) tr.append(node("td", "", String(value)));
      body.append(tr);
    }
    table.append(body);
    panel.append(table);
  }
  const solution = certificate.solution;
  if (solution && typeof solution === "object") {
    panel.append(node("h4", "subheading", "Exact solution"));
    const classification = typeof solution.classification === "string" ? solution.classification : status;
    panel.append(node("p", "classification-note", statusLabel(classification)));
    if (classification === "INCONSISTENT") {
      if (Number.isInteger(solution.contradiction_row)) panel.append(node("p", "exact-result", `Contradiction in R${solution.contradiction_row + 1}.`));
      else panel.append(node("p", "exact-result", "The checked reduced system contains a contradiction."));
    } else if (Array.isArray(solution.variables) && Array.isArray(solution.particular)) {
      const variables = solution.variables.map(String);
      const particular = solution.particular.map(String);
      if (classification === "UNIQUE") {
        for (let index = 0; index < variables.length; index += 1) {
          panel.append(node("p", "solution-line", `${variables[index]} = ${particular[index] ?? "0"}`));
        }
      } else {
        const parameters = Array.isArray(solution.parameters) ? solution.parameters.map(String) : [];
        const basis = Array.isArray(solution.basis) ? solution.basis : [];
        for (let variableIndex = 0; variableIndex < variables.length; variableIndex += 1) {
          const terms = [particular[variableIndex] ?? "0"];
          for (let basisIndex = 0; basisIndex < basis.length; basisIndex += 1) {
            const coefficient = String(basis[basisIndex]?.[variableIndex] ?? "0");
            if (coefficient !== "0") terms.push(`${coefficient}·${parameters[basisIndex] ?? `t${basisIndex + 1}`}`);
          }
          panel.append(node("p", "solution-line", `${variables[variableIndex]} = ${terms.join(" + ")}`));
        }
        if (parameters.length) panel.append(node("p", "muted-copy", `Free parameters: ${parameters.join(", ")} ∈ ℚ.`));
      }
    }
  }
  elements.traceContent.append(panel);
}

function updateModeFields() {
  const details = modeDetails[elements.mode.value] || modeDetails.logic;
  elements.statementLabel.textContent = details.label;
  elements.statement.placeholder = details.placeholder;
  elements.syntaxHelp.textContent = details.help;
  elements.assumptionsField.hidden = elements.mode.value !== "logic";
  elements.variablesField.hidden = elements.mode.value !== "linear";
  elements.statement.setAttribute("aria-describedby", "syntax-help");
}

function setMode(mode) {
  if (!modeDetails[mode]) return;
  elements.mode.value = mode;
  updateModeFields();
}

function switchView(view) {
  for (const tab of elements.tabs) {
    const selected = tab.dataset.view === view;
    tab.setAttribute("aria-selected", String(selected));
    tab.tabIndex = selected ? 0 : -1;
    tab.classList.toggle("is-active", selected);
    const panel = document.getElementById(tab.getAttribute("aria-controls"));
    panel.hidden = !selected;
  }
}

function renderExamples() {
  elements.examplesList.replaceChildren();
  for (const example of examples) {
    const card = node("article", "work-card example-card");
    card.append(node("p", "eyebrow", modeDetails[example.mode].label));
    card.append(node("h2", "", example.title));
    card.append(node("p", "muted-copy", example.description));
    const code = node("pre", "example-code");
    code.textContent = [example.assumptions, example.statement].filter(Boolean).join("\n");
    card.append(code);
    const button = node("button", "button button-secondary", "Open in workspace");
    button.type = "button";
    button.addEventListener("click", () => {
      setMode(example.mode);
      elements.statement.value = example.statement;
      elements.assumptions.value = example.assumptions;
      elements.variables.value = example.variables;
      switchView("workspace");
      elements.statement.focus();
    });
    card.append(button);
    elements.examplesList.append(card);
  }
}

function storageBytes(sessions) {
  return new TextEncoder().encode(JSON.stringify(sessions)).length;
}

function readSessions() {
  try {
    const source = localStorage.getItem(SESSION_KEY);
    if (!source) return [];
    const parsed = JSON.parse(source);
    if (!Array.isArray(parsed)) return [];
    const sessions = parsed.filter((item) => item && typeof item.id === "string"
      && typeof item.receipt === "string" && item.problem && typeof item.savedAt === "string").slice(0, MAX_SESSIONS);
    while (sessions.length && storageBytes(sessions) > MAX_SESSION_BYTES) sessions.pop();
    return sessions;
  } catch {
    storageAvailable = false;
    elements.sessionsMessage.textContent = "Saved sessions are unavailable in this browser. You can still run and export receipts.";
    return [];
  }
}

function renderSessions() {
  elements.sessionList.replaceChildren();
  elements.sessionCount.textContent = String(savedSessions.length);
  elements.sessionsEmpty.hidden = savedSessions.length > 0;
  for (const session of savedSessions) {
    const item = node("li", "session-item");
    const detail = node("div", "session-detail");
    const problemText = typeof session.problem.statement === "string" ? session.problem.statement : "Saved certificate";
    detail.append(node("strong", "", problemText.slice(0, 100)));
    const savedStatus = typeof session.status === "string" ? session.status : "Saved";
    detail.append(node("span", "session-meta", `${statusLabel(savedStatus)} · ${formatDate(session.savedAt)}`));
    item.append(detail);
    const actions = node("div", "session-actions");
    const restore = node("button", "text-button", "Restore");
    restore.type = "button";
    restore.setAttribute("aria-label", `Restore ${problemText.slice(0, 60)}`);
    restore.addEventListener("click", () => restoreSession(session));
    const remove = node("button", "text-button text-danger", "Delete");
    remove.type = "button";
    remove.setAttribute("aria-label", `Delete saved session ${problemText.slice(0, 60)}`);
    remove.addEventListener("click", () => deleteSession(session.id));
    actions.append(restore, remove);
    item.append(actions);
    elements.sessionList.append(item);
  }
}

function formatDate(value) {
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? "Saved on this device" : `Saved ${date.toLocaleDateString()}`;
}

function persistSessions(nextSessions) {
  if (!storageAvailable) {
    elements.sessionsMessage.textContent = "Saved sessions are unavailable in this browser.";
    return false;
  }
  try {
    localStorage.setItem(SESSION_KEY, JSON.stringify(nextSessions));
    savedSessions = nextSessions;
    renderSessions();
    return true;
  } catch {
    elements.sessionsMessage.textContent = "Could not save changes to this browser’s storage. Existing sessions were left unchanged.";
    return false;
  }
}

function saveSession() {
  if (!currentReceipt || currentVerification?.valid !== true) return;
  const receipt = JSON.stringify(currentReceipt);
  if (!storageAvailable) {
    elements.sessionsMessage.textContent = "Could not save: browser storage is unavailable.";
    return;
  }
  const problem = currentReceipt.problem;
  const created = {
    id: crypto.randomUUID(),
    savedAt: new Date().toISOString(),
    status: currentVerification.status,
    problem,
    receipt,
  };
  let next = [created, ...savedSessions.filter((session) => session.id !== created.id)];
  let trimmed = false;
  while (next.length > MAX_SESSIONS || storageBytes(next) > MAX_SESSION_BYTES) {
    next.pop();
    trimmed = true;
  }
  if (!next.some((session) => session.id === created.id)) {
    elements.sessionsMessage.textContent = "This receipt is too large for the bounded saved-session history. Download it instead.";
    return;
  }
  if (persistSessions(next)) {
    elements.sessionsMessage.textContent = trimmed
      ? "Saved. The history limit removed the oldest session."
      : "Checked receipt saved on this device.";
  }
}

function restoreSession(session) {
  if (pendingRequest && pendingRequest.type !== "initialize") return;
  if (session.problem && typeof session.problem.kind === "string") {
    setMode(session.problem.kind);
    const statement = typeof session.problem.statement === "string" ? session.problem.statement : "";
    elements.statement.value = session.problem.kind === "linear" ? statement.replace(/;/g, "\n") : statement;
    elements.assumptions.value = Array.isArray(session.problem.assumptions) ? session.problem.assumptions.map(displayUserValue).join("\n") : "";
    elements.variables.value = Array.isArray(session.problem.variables) ? session.problem.variables.map(displayUserValue).join(", ") : "";
  }
  elements.receiptInput.value = session.receipt;
  elements.fileName.textContent = "Loaded from saved sessions";
  elements.importMessage.textContent = "Session loaded. Replay its certificate to verify it again.";
  switchView("workspace");
  updateControls();
  elements.importHeading.scrollIntoView({ block: "center", behavior: "smooth" });
  if (engineReady) verifyReceipt();
  else ensureWorkerForNextRequest();
}

function deleteSession(id) {
  const next = savedSessions.filter((session) => session.id !== id);
  if (persistSessions(next)) elements.sessionsMessage.textContent = "Saved session deleted.";
}

function saveReceiptFile() {
  if (!currentReceipt) return;
  const blob = new Blob([JSON.stringify(currentReceipt, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = node("a");
  link.href = url;
  link.download = "frontier-math-rework-receipt.json";
  document.body.append(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
  elements.resultFeedback.textContent = "Receipt JSON downloaded.";
}

async function copyReceipt() {
  if (!currentReceipt) return;
  try {
    await navigator.clipboard.writeText(JSON.stringify(currentReceipt, null, 2));
    elements.resultFeedback.textContent = "Receipt JSON copied to the clipboard.";
  } catch {
    elements.resultFeedback.textContent = "Clipboard access is unavailable. Use the certificate JSON inspector to copy it manually.";
    elements.receiptDetails.open = true;
  }
}

async function loadReceiptFile() {
  const file = elements.receiptFile.files?.[0];
  if (!file) return;
  if (file.size > MAX_RECEIPT_BYTES) {
    elements.receiptInput.value = "";
    elements.fileName.textContent = "File exceeds the 4 MB limit";
    elements.importMessage.textContent = "Certificate files must be 4 MB or smaller.";
    updateControls();
    return;
  }
  try {
    const source = await file.text();
    if (new TextEncoder().encode(source).length > MAX_RECEIPT_BYTES) throw new Error("Certificate files must be 4 MB or smaller.");
    elements.receiptInput.value = source;
    elements.fileName.textContent = file.name;
    elements.importMessage.textContent = "File loaded. Replay it to check the certificate.";
    updateControls();
  } catch (error) {
    elements.importMessage.textContent = error instanceof Error ? error.message : "Could not read this file.";
  }
}

function clearInputs() {
  elements.statement.value = "";
  elements.assumptions.value = "";
  elements.variables.value = "";
  elements.statement.focus();
  clearResult();
  setResultState("idle", "Waiting", "Choose a mode and enter a formal problem to begin.");
}

elements.mode.addEventListener("change", updateModeFields);
document.getElementById("problem-form").addEventListener("submit", runProblem);
elements.stopButton.addEventListener("click", stopOperation);
elements.retryEngine.addEventListener("click", () => {
  if (worker) worker.terminate();
  worker = null;
  pendingRequest = null;
  workerGeneration += 1;
  clearResult();
  initializeEngine();
});
elements.clearButton.addEventListener("click", clearInputs);
elements.receiptInput.addEventListener("input", updateControls);
elements.verifyButton.addEventListener("click", verifyReceipt);
elements.receiptFile.addEventListener("change", loadReceiptFile);
elements.copyReceipt.addEventListener("click", copyReceipt);
elements.downloadReceipt.addEventListener("click", saveReceiptFile);
elements.saveSession.addEventListener("click", saveSession);
elements.tabs.forEach((tab, index) => {
  tab.addEventListener("click", () => switchView(tab.dataset.view));
  tab.addEventListener("keydown", (event) => {
    if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
    event.preventDefault();
    const nextIndex = event.key === "Home" ? 0
      : event.key === "End" ? elements.tabs.length - 1
        : (index + (event.key === "ArrowRight" ? 1 : -1) + elements.tabs.length) % elements.tabs.length;
    elements.tabs[nextIndex].focus();
    switchView(elements.tabs[nextIndex].dataset.view);
  });
});
document.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key === "Enter"
      && !document.getElementById("panel-workspace").hidden) runProblem(event);
});

updateModeFields();
renderExamples();
savedSessions = readSessions();
renderSessions();
makeWorker();
initializeEngine();

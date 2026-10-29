# KL-GDR-001 — Grain-dependent deviation recognition and sticky directional custody

**Owner:** Love Labs LCA · KakeyaLogic (upstream directional definition)
**Status:** PROPOSED TESTABLE CONTRACT; conditional lemma below; operational effectiveness OPEN
**Registered:** 2026-10-12
**Related:** [typed directional object](typed-directional-object.md), [compression / overlap / refinement](compression-overlap-refinement.md), [directional completeness](directional-completeness.md), [SIUS](safeguard-integrity-under-stagnation.md).

## Claim boundary

**Correction = Direction** is an operational interpretation: a valid correction constrains the set of admissible future transitions. It is *not* a claim that every natural-language correction determines a unique geometric tangent, that every system trajectory is continuous, or that classical Kakeya geometry proves an AI property.

Represent a correction with stable identity, source, authority, applicability, supersession rules, and required relationships in the existing typed object contract. For a differentiable trajectory `gamma(t)` in a declared state space, an *optional* geometric realization associates it with a permitted velocity set `K_c(x)`. Discrete transitions instead use typed admission predicates. The geometry must not overwrite the typed authority model.

**Sticky custody** means that a governing correction remains effective on all *applicable* descendant directions under refinement, compression, rerouting, or delegation unless validly superseded. The descendant need not copy the exact words, and a summary is not itself a new grant of authority. Parent-to-child links must preserve identity, scope, evidence and version lineage. Relevance (HELD) never implies truth, approval or executability.

## Four separate observables

1. **Evidence availability (Visibility):** did an observation contain sufficient information to witness the relevant deviation?
2. **Recognition:** did the checker classify that observation against the *applicable retained correction*?
3. **Custody (Retention/Authority):** was the correction available, unaltered in governing meaning, and authoritative on this descendant route?
4. **Enforcement:** did an independently governed pre-commit gate block unauthorized effects?

Retrospective recognition is not prospective enforcement. Unknown coverage or a lost correction is `UNRESOLVED`, not a safety PASS. An observed unauthorized effect is FAIL regardless of subsequent repair. Detection latency, containment latency, notification latency, and false-positive rate are separate outcomes.

## Conditional finite-grain lemma

Let `P_k` be finite nested partitions of the *same realized trajectory* into
positive-duration intervals. On each parent interval, let the observed directional
average be the duration-weighted mean of its children's averages. Let `K` be a
**fixed convex** subset of the velocity space, and assume **exact, compatible
observations**. Duration weights avoid conflating time averages with arc-length averages.

Then

```text
v(parent) = sum_i weight_i * v(child_i),  weights >= 0, sum = 1
v(parent) outside K  =>  some v(child_i) outside K.
```

**Proof:** If all child averages were in convex `K`, their convex combination would belong to `K`, contradicting a violating parent average. Repeating the argument establishes nested inclusion of *detected violating cases* across refinements.

This proves monotonic **evidence-based flag persistence** for this narrow detector, *not* universal model recognition, improved precision under arbitrary noise, or monotonic behavior for nonconvex or state-dependent authorization predicates. The converse fails: fine-scale violations can cancel in coarse averages, leaving endpoints apparently safe.

## Falsifiers and counterexamples

- A coarse flag disappears at a finer **nested exact** partition with the same convex `K` and correctly computed averages: falsifies the implementation of the lemma.
- A finer analysis loses the governing correction during compaction/delegation: violates sticky custody, even if directional evidence remains visible.
- With bounded positional measurement error `epsilon`, a conservative slope detector needs an uncertainty allowance of at most `2 epsilon / delta` on a grain of duration `delta`. That allowance may increase as grains shrink; *per-resolution* recognition need not be monotonic.
- Replaying verified detection receipts can make the **recorded set** cumulative/monotone, but does not repair erroneous detections. False alarms must retain evidence, review state, and authorized supersession.
- Endpoint safety and recognition after commitment do not demonstrate pre-action containment.
- An authorized change to a protected control is SIUT or mixed SIUT/SIUS; do not misclassify refinement as a fixed-control SIUS evaluation.

## Registered experiment: KL-GDR-001 / GIUS-VRD-001

**Synthetic model only.** For `gamma(t)=(t,y(t))`, set the allowed vertical average velocity interval to `K=[-0.25,0.25]`. Construct 84 triangular excursions returning to the baseline (seven dyadic widths times twelve placements) plus 28 clean traces. Sample the same trajectories on nested dyadic grids of 4 through 2048 segments; half of each family crosses a simulated delegation point. Compare route-local custody against correction inheritance. Run a second monitor with *declared bounded measurement uncertainty* (not an invented claim of actual stochastic noise). Report:

- evidence-visible violating cases, recognized cases, custody-missing `UNRESOLVED` cases, false positives, and cumulative verified detections;
- exact versus uncertainty-aware detection by grain;
- earliest observable recognition time (when applicable), and separate pre-action enforcement status (`NOT_EVALUATED` unless implemented);
- scope, fixture generation, thresholds, and explicit synthetic provenance.

The downstream code belongs to **GIUS**. It must not change the existing `GIUS-BENCH-001` registered receipts or promote real-system effectiveness. See the downstream proposed `benchmarks/grain_recognition.py` and `docs/grain-dependent-recognition.md`.

### Reproduction receipt — 29 October 2026

Checked downstream [GIUS PR #3](https://github.com/Manny536/Guardrail-integrity-under-stagnation/pull/3)
at `6fdef9b340c57a0fd1a433119dc68c810fcbcc4e`: its GIUS calibration workflow
[run 38321697848](https://github.com/Manny536/Guardrail-integrity-under-stagnation/actions/runs/38321697848)
completed successfully. Independently rerunning the seven grain-recognition tests
and JSON experiment at that revision reproduced 112 cases (84 violations, 28 clean
controls). At 512 segments: exact inherited custody recognizes 84/84; route-local
custody recognizes 42/84 with 42 unresolved. At 2048: uncertainty-aware recognition
drops to 0/84 while exact recognition and cumulative verified detections remain 84/84.
This is reproduction of the declared synthetic fixture, not an independent dataset.
Pre-action enforcement remains NOT_EVALUATED; operational effectiveness remains OPEN.

## Open

Whether refinement improves *semantic* recognition in real agents, how to ensure scope-preserving correction inheritance under branching routes, whether better recognition predicts prevention, how to calibrate false alarms, and how to operationalize L²_C coherence/drift remain OPEN. The finite convex lemma does not imply a Kakeya dimension theorem, Hilbert–Pólya operator, or resolution of RH.

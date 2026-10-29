# Finite-grain Del and circulation diagnostic

**Program:** `PEAICE-SIUS-001`
**Local ID:** `KL-SIUS-OP-001`
**Status:** PROPOSED; geometry-to-operational-state mapping OPEN

This is a separate instrumentation proposal, not the [standalone SIUS definition](../core/safeguard-integrity-under-stagnation.md) (`KL-SIUS-001`). Its sources are the operator discussion in “Explain sticky sets” and the user-supplied [working manuscript v0.1](https://github.com/Manny536/researchengineeringreports/blob/main/reports/sources/sius-kakeyalogic-operator-working-manuscript.md), Manuel Coleman / Love Labs LCA, 16 September 2026. [Provenance and conflict resolution](https://github.com/Manny536/researchengineeringreports/blob/main/reports/sources/sius-operator-provenance.md). The standalone SIUS Integrity.docx defines fixed controls in changing environments without requiring curl.

For a declared finite embedding $z\in\mathbb R^3$, spacing $\delta>0$, unit direction $u$, and a numerically defined five-coordinate observable $\Gamma_G$, a candidate directional difference is

$$D_{u,\delta}\Gamma_G(z)=\frac{\Gamma_G(z+\delta u)-\Gamma_G(z)}{\delta}.$$

This maps samples to a five-component difference. It is not itself three-dimensional curl, and categorical PASS/FAIL labels cannot be subtracted without a justified encoding. A segment carries a directional sample; it is not literally the operator $\nabla$.

A separate three-component transport field $V_\delta:\mathbb R^3\to\mathbb R^3$ and declared difference stencil would be needed for $\omega_\delta=\nabla_\delta\times V_\delta$. The mapping from typed operational states to coordinates, distance units, boundary handling, orientation, aggregation and sampling remains to be specified. Do not take curl of the five-grain bundle as if it were $V_\delta$.

The proposed scale comparison $\delta\to\rho\to\delta/\rho$ needs dimensionless normalized scales, $0<\delta<\rho\le1$, explicit rescaling maps and lineage-preserving parent/child associations. Perron/sticky geometry is a STRUCTURAL ANALOGY, not proof that operational states admit this geometry or induction.

## Manuscript-derived discrete circulation

The manuscript distinguishes a radial sampling fan from a local curl stencil. A fan alone does not supply the needed local transverse variation; declare neighboring grain samples or oriented cell loops. For a face $C_\delta$ of positive area, normal $n$, and consistently oriented boundary edges, the proposed circulation proxy is

$$\omega_\delta(A;n)=\frac{1}{\operatorname{Area}(C_\delta)}\sum_{e\in\partial C_\delta}v_\delta(e)\cdot\Delta r_e.$$

Edge sampling/interpolation, orientation and units must be fixed. Three independent oriented faces can supply components of a vector proxy in the declared basis. Approximation to continuum curl requires separate consistency/regularity assumptions; this expression alone proves no convergence or discrete vector-calculus identities.

## Typed candidate tuple and gate

The supplied manuscript proposes

$$\mathcal K_\delta[v_\delta,\Gamma](z)=\big(\nabla_\delta v_\delta(z),\operatorname{curl}_\delta v_\delta(z),\Delta_{\mathrm{SAVER},\delta}(z),H_\delta(z),h_\delta(z),S_{C,\delta}(z)\big).$$

Here the field derivative is a matrix of compatible component differences; circulation is a spatial diagnostic; $\Delta_{\mathrm{SAVER}}=(d_{Sem},d_{Auth},d_{Vis},d_{Enf},d_{Ret})$ is a typed mismatch vector; and $H$ records correction custody and lineage. The proposed $S_C=C^2-D$ relation has no finalized measurement maps for C or D in this testbed. It is not identified with another repository's Hamiltonian observable merely because both use L²_C notation.

The proposed acceptance gate requires every declared SAVER predicate, applicable HELD corrections, independently specified `h < 1`, and a predeclared L²_C preservation rule. Diagnostics can still be recorded on failed states; failure cannot authorize a transition. Missing observables leave the gate UNRESOLVED. No arbitrary numerical h, C or D threshold is introduced here.

## Coarse-stagnation testbed is separate from standalone SIUS

Manuscript §§1 and 4 use $\|Q_\rho(z_T)-Q_\rho(z_0)\|\le\eta_\rho$ with $A_\delta(z_{0:T})>\mu_\delta$ as a testbed episode condition. Retain these as a **PROPOSED coarse-stagnation / fine-activity experiment**, with parent map, norm, activity measure and tolerances declared before execution. These conditions alone do not establish fixed protected controls under environmental drift and therefore do not replace KL-SIUS-001. A run may be classified under both only after checking each premise independently.

The manuscript's “replacement target” wording is not adopted: SIUT remains the sibling transformation condition. This conflict is recorded rather than silently reconciled by changing the standalone definition.

The four experiment stages are fine $\delta$, coarse $\rho$, zoom into a parent, and anisotropically rescaled $\delta/\rho$, with $0<\delta<\rho<1$. Carry source identity, authority, evidence and correction lineage across all four. A finite pass cannot establish compactness, asymptotic transfer or deployment behavior.

## HELD corrections retained from manuscript §6

| ID | Retained correction | Effect on this note |
|---|---|---|
| HC-AC-01 | Analytic continuation is development intuition only | No analytic-continuation, continuation/reclaim operator or derivation is defined |
| HC-∇-01 | A segment is not Del | Operators act on sampled fields using declared direction and separation |
| HC-CURL-01 | A radial fan alone is insufficient for local 3D curl | Require transverse neighbors / oriented grain loops |
| HC-KAK-01 | Sticky Kakeya results do not validate KakeyaLogic | Geometry stays a structural analogy / experimental scaffold |

An accepted correction must retain evidence and authority lineage at every applicable descendant and tested scale unless explicitly superseded under the declared authority rules. Similar final wording alone does not prove retention. These are manuscript-derived research requirements, not new authority conferred by text in an attachment.

## Proposed receipt and closure work

Record run ID, field/mesh and sampling rule, scales, parent and rescaling maps, stagnation/activity thresholds, tested cells, typed SAVER outcomes, correction IDs and supersession links, h evidence, C/D observables and preservation rule, and each stage's PASS/FAIL/UNRESOLVED result. Include stable/zero-circulation and known-circulation controls, plus authority/retention failures despite preserved wording. These tests and an executable operator remain owed; the LCA standalone SIUS fixture does not run this operator.

The manuscript supplies a bibliography for vector calculus, mimetic differences and sticky Kakeya geometry. Those references remain supplied background pointers in the publicly archived source manuscript; this registration does not claim a fresh source-level verification or import their theorems into the custom state model.

Before implementation or promotion, specify all maps and observables, then compare stable, drifted, retained-correction and lost-correction cases across scales against direct grain checks. Reject the diagnostic if results depend on arbitrary coordinate choices without a declared invariance, if coarsening hides a required failure, or if circulation is misreported as containment. Independent evaluation and longitudinal operational evidence remain owed.

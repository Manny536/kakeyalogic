# Frontier Math Rework: Lean video review

Reviewed 2 November 2026. This note uses the videos’ English auto-generated
speech captions, retrieved directly from YouTube. Excerpts reproduce caption
wording; linked times begin at the caption cue containing the excerpt.

## Research intent

Manuel Coleman values Lean’s mathematical power and the principle of mechanically
checked reasoning. His stated difficulty is getting a usable environment running.
The engineering aim is to reduce that friction while preserving explicit proof
obligations and rigorous checking. A commentator’s opinions about a developer or
vendor are recorded as that commentator’s views, separately from Manuel’s intent.

## Tsoding: setup, documentation, and the proof mechanism

[Tsoding Daily’s video](https://www.youtube.com/watch?v=l9hUGoN6BLM) moves from
installation and editor setup into programming, compilation, and C/Raylib
integration. Its final section turns to documentation, propositions, proof
construction, and tactics. These phases explain why the later mathematical
discussion is distinct from the earlier setup experience.

| ID | Time | Verbatim caption excerpt | Context |
|---|---|---|---|
| `TS-BUILD` | [35:16](https://www.youtube.com/watch?v=l9hUGoN6BLM&t=2116s) | “you can't build it on your machine” | His general source/binary commentary, qualified for Lean near 36:01. |
| `TS-DOC` | [3:02:06](https://www.youtube.com/watch?v=l9hUGoN6BLM&t=10926s) | “define everything up front” | After finding an example definition hidden in an expandable documentation block. |
| `TS-TYPE` | [3:10:00](https://www.youtube.com/watch?v=l9hUGoN6BLM&t=11400s) | “type that encodes some sort of a statement” | Relating a conjunction-swapping program to the proposition it establishes. |
| `TS-AUTO` | [3:14:46](https://www.youtube.com/watch?v=l9hUGoN6BLM&t=11686s) | “This is actual automation of programming.” | After demonstrating tactic-assisted proof construction and discussing remaining manual work. |

The originally shared [35:16 link](https://www.youtube.com/watch?v=l9hUGoN6BLM&t=2116s)
falls inside his build-cost and source/binary-reproducibility discussion
(34:21–36:11). At approximately 36:01 he qualifies the Lean-specific suspicion.
That location came from the shared URL; it was not a selected quotation. The
excerpts above were selected after reviewing the speech captions in context.

## Getting started: browser access and visible proof state

[The video on Alex Kontorovich’s channel](https://www.youtube.com/watch?v=I2zaPoj3G50)
opens through a browser-hosted Mathlib workspace and develops a squeeze-theorem
proof interactively. Its discussion distinguishes entered instructions from the
resulting goal state, then checks an AI-suggested theorem against the library.

| ID | Time | Verbatim caption excerpt | Context |
|---|---|---|---|
| `AK-GOAL` | [7:13](https://www.youtube.com/watch?v=I2zaPoj3G50&t=433s) | “the right hand side is lean talking back to me” | Explaining the interface’s display of assumptions and the current goal. |
| `AK-CHECK` | [22:30](https://www.youtube.com/watch?v=I2zaPoj3G50&t=1350s) | “let's check if it's real” | Checking whether a suggested theorem exists before using it. |

The supplied 5:00 URL remains the study starting point. These excerpt locations
were selected independently during this review.

## Ank Yog: propositions, proof terms, and tactics

[Ank Yog’s tutorial](https://www.youtube.com/watch?v=0QZI_m8WZ0Q) introduces
propositions as types, then builds proofs using introduction/elimination rules
and tactics before moving to larger mathematical examples.

| ID | Time | Verbatim caption excerpt | Context |
|---|---|---|---|
| `AY-TYPES` | [2:34](https://www.youtube.com/watch?v=0QZI_m8WZ0Q&t=154s) | “Propositions are types and their proofs are their terms.” | Explaining the connection between a proposition and a term proving it. |
| `AY-TACTIC` | [3:36](https://www.youtube.com/watch?v=0QZI_m8WZ0Q&t=216s) | “tactics allow us to give broad instructions on how to construct the proof.” | Introducing tactics as instructions for constructing a proof. |

The [accompanying example code](https://github.com/AnkYog/LeanTutorial1)
remains a separate primary reference for checking the mathematical syntax.

## Engineering interpretation for this repository

The following are Frontier Math Rework design decisions drawn from the review.

| Requirement | Present implementation | Next concrete extension |
|---|---|---|
| Reach a first checked example with clear setup instructions. | Virtual-environment instructions and an installed console-command smoke check. | A clean-environment bootstrap/diagnostic path with explicit expected output. |
| Show the mathematical state a user is working on. | Explicit input hypotheses, a goal, and replayable sequent certificates. | An inspection view showing each reconstructed premise and outstanding goal. |
| Keep suggested steps subject to mathematical checking. | Search and solving propose certificates; a separate checker replays them. | Any future suggestion provider submits through the same acceptance boundary. |
| Make example prerequisites visible and searchable. | Bounded syntax, explicit hypotheses, and documented kernel rules. | Self-contained examples with every local definition and dependency listed. |

Lean’s [own propositions-and-proofs exposition](https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/)
describes assertions and proof terms in dependent type theory. The current
Frontier Math Rework implementation checks classical sequent derivations and
exact algebraic certificates. A dependent proof-term language and quantifier
rules remain explicit kernel extensions. The video review supplies motivation
and interface requirements; the implemented mathematics is documented in the
[application guide](../frontier-math-rework.md).

## Source provenance

All three selected speech tracks are marked **English (auto-generated)** by
YouTube. Tsoding’s video also has an uploaded **English - Twitch Chat - Simple**
track. That chat track was excluded from this review and from every quotation.

The [quote-provenance record](sources/frontier-math-rework-video-quotes.json)
stores video IDs, track selection, caption snapshot hashes, precise cue ranges,
excerpt hashes, and timestamp links. Quotations appear once, in this note;
the record references them by ID. Whole caption tracks are temporary review
inputs and are not included in the repository.

Review coverage: complete caption tracks were retrieved for all three videos.
The Tsoding stream was mapped across its full duration, with close reading of
setup, the shared timestamp, documentation, and the final proof/tactic section.
The companion tutorials were reviewed for onboarding, proof-state feedback,
logical rules, and the relation between proof construction and checking.

# Day 2 Pedagogy Review: Train It

**Review date:** 2026-08-16  
**Status:** **PASS**  
**Delivery readiness:** **READY** with accepted nonblocking limitations  
**Rubric:** [standards/pedagogy-rubric.md](../../standards/pedagogy-rubric.md)  
**Authoritative scope:** [neural-networks-outline.md](../../neural-networks-outline.md)

## Executive Verdict

Day 2 has a coherent learning arc, strong evidence-driven labs, aligned assessments, purposeful visuals, and complete participant/solution validation. Learners retrieve the Day 1 forward trace, give error a scalar form, make update behavior visible, trace local sensitivities, batch the same mechanics, build a complete NumPy training loop, and only then reveal PyTorch automation and evidence-first diagnosis.

All required revisions from the initial review are closed. The D2-04 participant and solution notebooks now teach and execute the PyTorch 2.11 `zero_grad(set_to_none=True)` default accurately, both execution gates were restored with no leakage, slide 31 remains the evidence-only gate, slide 32 is withheld until submissions are accepted, and the 34-page PDF passed all eight asset checks.

## Final Revision Disposition

**Status: PASS. Final pedagogy score: 48/50.** The A/B/C launch-before-diagnosis sequence, post-acceptance slide-32 reveal, corrected `zero_grad()` semantics, and 34-page render are verified closed. Cognitive Load and Pacing remain 4/5 because no timed novice rehearsal has measured participant reasoning and transition time; all other dimensions are 5/5.

Accepted nonblocking notes are the absence of a hosted Colab run and exact PyTorch 2.11 runtime execution, visible rather than clickable PDF paths, untested PDF/UA reading order, and slide 32's intentional information density. None may be presented as validated beyond the evidence recorded here.

## Rubric Scores

| Dimension | Score | Judgment |
|---|---:|---|
| Learning progression | 5/5 | Loss and learning rate precede backprop; backprop precedes complete training; NumPy precedes PyTorch. |
| Cognitive load | 4/5 | Concepts are chunked well, but D2-03 and the final checks are demanding without novice timing evidence. |
| Active learning | 5/5 | Predictions, diagnosis, controlled changes, and explanations are consistently required. |
| Visual reasoning | 4/5 | Eight assets are purposeful; slide-32 reveal timing and unvalidated PDF rendering prevent full credit. |
| Retrieval and reinforcement | 5/5 | Submitted Day 1 evidence is retrieved at opening and diagnostic evidence is retrieved for Day 3. |
| Transfer | 5/5 | Checks require unfamiliar diagnosis and scientific-loop transfer rather than vocabulary recall. |
| Misconceptions | 4/5 | Coverage is extensive, but `zero_grad()` semantics are internally inconsistent. |
| Assessment alignment | 5/5 | All eight objectives map to mechanism, diagnosis, application, or transfer evidence. |
| Engagement | 5/5 | Mystery evidence, visible failures, gradient checks, and constrained repairs create meaningful decisions. |
| Pacing | 4/5 | The 450-minute plan and cut lines are credible on paper; no timed novice rehearsal exists. |

**Initial score:** **46/50** before revisions. The controlling final score is **48/50** above.

## Strengths

1. The opening retrieves the submitted Day 1 forward trace and consolidation before new instruction.
2. The day preserves the required loss -> learning rate -> backprop -> batching -> NumPy -> PyTorch sequence.
3. All four participant and solution pairs passed execution; remaining notes are limited to unrun environments.
4. `LESSON-D2-06` maps framework calls back to exposed mechanics rather than replacing explanation with syntax.
5. `CHECK-D2-04` retrieves actual diagnostic evidence for Day 3 readiness.

## Risks

1. D2-04's participant and solution notebooks incorrectly contrast plain `zero_grad()` with `set_to_none=True`.
2. Slide 32 displays plausible causes and checks that belong after the `ACT-D2-04` commitment.
3. The Day 2 PDF and render validation do not yet exist.
4. `CHECK-D2-03` and the live portion of `CHECK-D2-04` each require substantial evidence within five minutes.
5. Notebook compute times are excellent, but no novice rehearsal validates reasoning, writing, discussion, and transitions.

## Required Findings and Disposition Plan

| Action | Exact location | Concrete change | Rationale | Time impact | Priority / owner | Gate reset |
|---|---|---|---|---|---|---|
| KEEP | Student Guide opening retrieval; slides 01-03 | Preserve submitted-response sampling and second-color revision. | Retrieves Day 1 evidence rather than vocabulary. | None | P2 / Lesson Developer | None |
| KEEP | Course flow and all four lab launch/debrief sections | Preserve the current dependency order and immediate debriefs. | Every abstraction is introduced before dependent implementation. | None | P2 / Course Architect | None |
| CLARIFY | D2-04 participant semantics and solution API note | State that PyTorch 2.11 plain `zero_grad()` defaults to `set_to_none=True`; contrast it with explicit `set_to_none=False`. Remove claims that plain calls provide visible zero tensors. | Current wording contradicts the correctly sourced guide and can teach the wrong `.grad` state. | 0 live; 15-25 minutes production | **P0 / Lab Engineer and Lab Solution Engineer** | Reset D2-04 Student and Solution |
| CLARIFY | Slides 30-32, especially slide 32 | Keep slide 31 projected during diagnosis. Mark slide 32 explicitly post-gate and reveal it only after submissions are accepted. | The visual supplies hypotheses and checks that learners must produce first. | None | **P0 / Lesson Developer** | None |
| ADD VISUAL | Day 2 slide source and render validation | Render all 34 slides; verify eight SVGs, clipping, ordering, paths, legibility, notes, and alt-text limitations. | Strong source is not yet a validated delivery artifact. | 45-75 minutes production | **P0 / Lesson Developer** | None unless notebook code changes |
| SHORTEN | Final 15-minute check block | If delivery overruns, move evaluation-mode detail to the existing pre-Day-3 consolidation; preserve diagnosis and shape evidence live. | Protects collection and the final buffer without deleting objectives. | 0 net | P1 / Lesson Developer | None |
| ADD ACTIVITY | Instructor Guide exact schedule | Conduct one uninterrupted novice rehearsal and record block completion, help events, debriefs, and checks. | Execution time does not validate novice reasoning time. | 450 minutes staff time | P1 / Course Orchestrator | None unless artifacts change |
| KEEP | Participant and solution validation summaries | Retain hosted Colab and exact-2.11 limitations as environment notes only. | The reports accurately avoid unsupported runtime claims. | None | P2 / Course Orchestrator | None |

## Source-Grounded Correction

The official PyTorch 2.11 API documents the signature as `Optimizer.zero_grad(set_to_none=True)`. With the default, gradients are set to `None` rather than zero-filled tensors. The documentation notes that manual access behaves differently, parameters that receive no gradient remain `None` after backward, and optimizers distinguish a missing gradient from a zero gradient. The course may use plain `optimizer.zero_grad()` in the core loop, but its explanations and inspection code must account for `None`; explicit `set_to_none=False` is the appropriate contrast for zero-filled gradient buffers.

Source: [PyTorch 2.11 `Optimizer.zero_grad`](https://docs.pytorch.org/docs/2.11/generated/torch.optim.Optimizer.zero_grad.html)

## Pacing and Scope Disposition

The schedule totals exactly 450 minutes and protects lunch, both breaks, and the final 10-minute buffer. Cut negative-log-likelihood depth, extra graph branches, hardware detail, the D2-03 second experiment, and extra D2-04 failures first. Preserve predictions, gradient checking, the complete NumPy loop, one evidence-first PyTorch repair, debriefs, and checks.

No timed novice rehearsal currently exists. This is an operational recommendation and bars a novice-validated timing claim; it is not a substitute for the required notebook and slide corrections above.

## Revision Acceptance Checklist

- [x] D2-04 participant text correctly describes the plain PyTorch 2.11 `zero_grad()` default.
- [x] D2-04 solution text and inspection notes use the same semantics.
- [x] D2-04 Student gate was rerun and returned PASS WITH NOTES.
- [x] D2-04 Solution gate was rerun after Student PASS and returned PASS WITH NOTES.
- [x] Slide 32 is explicitly post-gate and withheld until diagnosis submissions are accepted.
- [x] `courseware/slides/day-2-train-it.pdf` exists with 34 pages.
- [x] All eight Day 2 SVG assets render and pass clipping, legibility, path, and ordering checks.
- [x] Render limitations for notes and alt text are recorded honestly.
- [x] Hosted Colab and exact PyTorch 2.11 execution remain unclaimed.
- [x] No Day 2 objective, primary lab, or required outline topic was removed.

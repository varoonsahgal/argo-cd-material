# Day 1 Pedagogy Review: See It

**Review date:** 2026-08-16  
**Status:** **PASS WITH NOTES**  
**Delivery readiness:** **READY** with accepted non-blocking limitations  
**Rubric:** [standards/pedagogy-rubric.md](../../standards/pedagogy-rubric.md)  
**Authoritative scope:** [neural-networks-outline.md](../../neural-networks-outline.md)

## 1. Executive Verdict

Day 1 has a strong instructional spine: learners move from one-neuron geometry to the linear limit, earn the need for nonlinear hidden transformations, trace shapes and semantic invariants, and finish by diagnosing a complete but incorrect forward prediction. The activities consistently require prediction, inspection, diagnosis, controlled modification, and explanation.

All required revisions from the initial review are closed. The afternoon prerequisite order is consistent, Leaky ReLU is independently optional across the activity, slide, participant notebook, and solution notebook, assessment follow-up has explicit timing and collection, all four lab pairs retain passing execution gates, and the 32-page slide PDF contains all five required teaching visuals.

No timed novice rehearsal or hosted Colab run has been conducted. Those facts remain accepted operational limitations and must not be presented as validated claims.

## Final Revision Disposition

**Status: PASS WITH NOTES.** The sole finding from the first re-review is closed. `ACT-D1-03` and slide 23 now define sigmoid, tanh, ReLU, and softmax as the four core activation cards and isolate Leaky ReLU as an optional extension. The current rendered PDF preserves this distinction and passed page-specific clipping, crowding, and legibility review. The D1-03 participant and solution validations confirm that the complete core path has no Leaky ReLU dependency and that the optional path remains independently executable. No new contradiction was introduced.

**Final pedagogy score: 48/50.** Transfer and Pacing remain 4/5; all other dimensions are 5/5. Accepted non-blocking notes are the absence of a timed novice rehearsal and hosted Colab run, readable localized label crowding, PDF accessibility limitations, and the previously accepted D1-01 threshold-count narrative discrepancy. No required pedagogy finding remains open.

## 2. Initial Rubric Scores (Historical, Before Revisions)

The table below records the package state at the initial review. The controlling post-remediation score is 48/50 in the Final Revision Disposition above.

| Dimension | Score | Evidence and judgment |
|---|---:|---|
| 1. Learning progression | **3/5** | The macro-sequence in [courseware/00-course-design/course-flow.md](../00-course-design/course-flow.md) is coherent: neuron geometry -> linear success/XOR failure -> layers -> activations -> forward mystery. However, `LAB-D1-03` declares `LESSON-D1-05` and `ACT-D1-03` as prerequisites while the schedule places both after the lab. [courseware/day-1/student-guide/day-1-student-guide.md](../day-1/student-guide/day-1-student-guide.md), "Activation Preview for the Observatory," explicitly acknowledges this inversion. |
| 2. Cognitive load | **4/5** | Intuition precedes most formalism, especially "Mental Model Before Math," boundary visualization, XOR evidence, and shape contracts. Dense computations are chunked into predictions, shapes, ranges, and invariants. The main load defect is that `LAB-D1-03` requires four scalar activation implementations, including Leaky ReLU, plus dense operations, stability, plotting, semantic-axis diagnosis, and debrief in 40 minutes. |
| 3. Active learning | **5/5** | [courseware/day-1/challenges/day-1-challenges.md](../day-1/challenges/day-1-challenges.md) repeatedly requires commitments before evidence. The four labs add constrained experimentation, deliberately wrong behavior, diagnosis, recovery, and explanation. Participants cannot complete the core path through passive execution alone. |
| 4. Visual reasoning | **3/5** | The source deck specifies purposeful boundary overlays, raw/hidden XOR views, activation small multiples, and a four-panel forward evidence board. Lab validations confirm useful plots. However, all five named slide PNG assets and the required PDF are absent, so the intended visual teaching surface is not deliverable. |
| 5. Retrieval and reinforcement | **4/5** | Slide 01 responses return on slide 31; `CHECK-D1-02` preserves a noon prediction and requires evidence-based revision after `LAB-D1-03`; `OBJ-D1-04` and `OBJ-D1-05` return in `LAB-D1-04`; the forward trace is explicitly carried into Day 2. Follow-up items in `CHECK-D1-01`, `CHECK-D1-03`, and `CHECK-D1-04` lack a concrete completion and retrieval schedule. |
| 6. Transfer | **4/5** | `CHECK-D1-01` asks for model choice from scenario constraints, `CHECK-D1-03` tests an unfamiliar "more identity layers" proposal, and `CHECK-D1-04` distinguishes model error from implementation failure. `LAB-D1-04` adds a controlled copied-parameter perturbation. A later retrieval task should require applying shape and invariant reasoning to a new architecture rather than the recurring `4 -> 8 -> 3` example. |
| 7. Misconceptions | **5/5** | [courseware/instructor-guide/day-1-instructor-guide.md](../instructor-guide/day-1-instructor-guide.md), "Misconception Routing Table," provides symptoms, discriminating questions, and routes for boundary motion, batch/parameter confusion, XOR, affine composition, wrong-axis softmax, anthropomorphism, and model-versus-code failure. Student-facing misconception clinics also appear near the relevant concepts. |
| 8. Assessment alignment | **4/5** | [courseware/00-course-design/learning-objectives.md](../00-course-design/learning-objectives.md) maps every Day 1 objective to instruction, practice, and a named check. The checks emphasize defense, diagnosis, application, and evidence rather than vocabulary recall. The score is reduced because three checks defer evidence items without a precise schedule or collection rule. |
| 9. Engagement | **4/5** | Boundary manipulation, XOR failure, activation diagnosis, mystery probes, and visible before/after evidence create meaningful curiosity. Scoring rewards prediction discipline and reasoning rather than speed. Missing rendered slide assets weaken the planned live reveals and prevent full delivery confidence. |
| 10. Pacing | **3/5** | The schedule totals exactly 450 elapsed minutes, protects breaks and the final buffer, and names cut lines. Compute runtimes are comfortably below limits. No timed novice rehearsal exists, D1-03 is dense for 40 minutes, and deferred assessment work is not assigned to a definite time. |

**Total:** **39/50**

## 3. Top Five Strengths

1. **The linear limitation earns the hidden layer.** `LAB-D1-02` lets a simple model succeed before showing why one boundary cannot represent XOR.
2. **Predictions are preserved as evidence.** `ACT-D1-01`, all four labs, and `CHECK-D1-02` require commitments before revealing results.
3. **Semantic correctness is taught beyond shape correctness.** D1-03's wrong-axis softmax is an unusually strong novice diagnostic because the code runs and preserves shape while violating a meaningful invariant.
4. **Misconceptions are routed to cheap tests.** The instructor guide offers concrete questions and evidence rather than generic warnings.
5. **The Day 2 bridge is conceptually clean.** D1-04 distinguishes fixed forward computation from learning and identifies error signal plus parameter change as the missing capabilities.

## 4. Top Five Risks

1. **Missing delivery visuals:** Five referenced PNG assets and the rendered Day 1 PDF do not exist.
2. **Impossible prerequisite order:** D1-03 declares `LESSON-D1-05` and `ACT-D1-03` as prerequisites but currently precedes them.
3. **Leaky-ReLU scope leak:** D1-03 requires Leaky-ReLU prediction, implementation, plotting, and tabular comparison even though the design labels its detail optional.
4. **Unscheduled assessment follow-up:** `CHECK-D1-01` Scenario B.4, `CHECK-D1-03` item 5, and `CHECK-D1-04` items 2 and 5 are deferred without a due time or retrieval event.
5. **Unverified human pacing:** Clean notebook runtimes do not establish that a novice can predict, implement, diagnose, explain, and debrief within the planned blocks.

## 5. Section-by-Section Recommendations

| Action | Exact location | Concrete change | Rationale | Time impact | Priority | Owner | Lab-gate reset impact |
|---|---|---|---|---|---|---|---|
| KEEP | [neural-networks-outline.md](../../neural-networks-outline.md), "Day 1 - How Neural Networks Actually Work"; [courseware/00-course-design/course-flow.md](../00-course-design/course-flow.md), "Day 1: See It" | Preserve the neuron -> linear limit -> hidden transformation -> complete forward trace arc and all seven Day 1 objectives. | The sequence gives each abstraction a visible problem to solve. | No change. | P2 | Course Architect and Lesson Developer | None. |
| ADD VISUAL | [courseware/slides/day-1-see-it.md](../slides/day-1-see-it.md), slides 08, 12, 14, 24, and 28; expected `courseware/slides/day-1-see-it.pdf` | Generate the five referenced assets: `boundary-motion-overlay.png`, `linear-success-boundary.png`, `xor-raw-hidden-linked.png`, `activation-small-multiples.png`, and `forward-evidence-board.png` under `courseware/shared/assets/day-1/`. Render all 32 slides to PDF and record clipping, links, readability, image presence, and notes/alt-text checks in `courseware/reviews/slide-render-validation.md`. | The deck is content-bearing and the architecture explicitly states that source-only slide directories are incomplete. The assets directory and PDF are currently absent. | Live time: 0. Production: approximately 60-90 minutes plus render QA. | **P0** | Lesson Developer; Course Orchestrator coordinates render | No lab reset. Generate assets only from already validated outputs; if notebook plotting code is changed to create them, reset the affected lab's gates. |
| MOVE | [courseware/00-course-design/course-flow.md](../00-course-design/course-flow.md), Day 1 afternoon; [courseware/instructor-guide/day-1-instructor-guide.md](../instructor-guide/day-1-instructor-guide.md), "Exact 450-Minute Schedule"; [courseware/day-1/student-guide/day-1-student-guide.md](../day-1/student-guide/day-1-student-guide.md), schedule and `LESSON-D1-05`; [courseware/slides/day-1-see-it.md](../slides/day-1-see-it.md), slides 21-25 | Reorder the afternoon to `13:45-14:02 LESSON-D1-05 + ACT-D1-03`, `14:02-14:42 LAB-D1-03`, `14:42-14:57 break`, and `14:57-15:05 LESSON-D1-06`. In the deck, move current slides 23-25 before current slides 21-22. Keep slides 18-20 before both. | This makes every declared D1-03 prerequisite occur before the lab while preserving D1-06 immediately before D1-04. It also reconciles the `OBJ-D1-05 -> OBJ-D1-06` dependency. | Net live change: 0 minutes. Break remains 15 minutes; all later blocks retain their duration. | **P1** | Course Architect owns timing contract; Lesson Developer updates guides and slides | Schedule-only edits do not reset lab execution gates. Run ID/link/prerequisite audits. |
| CLARIFY | [courseware/day-1/labs/LAB-D1-03-shapes-activations.ipynb](../day-1/labs/LAB-D1-03-shapes-activations.ipynb), activation prediction, activation TODO, core plot/table, and "Optional Extension" cells | Remove Leaky ReLU from required predictions, required TODOs, and core checkpoint dependencies. Move its implementation, plot/table comparison, and slope experiment into the optional extension. A learner who skips the optional section must complete every core assertion and debrief. | [courseware/00-course-design/course-flow.md](../00-course-design/course-flow.md), [courseware/00-course-design/course-architecture.md](../00-course-design/course-architecture.md), and the Student Guide all classify Leaky-ReLU detail as optional. The notebook currently makes it required. | Likely saves 3-5 novice minutes in the 40-minute block. | **P1** | Lab Engineer | Reset `LAB-D1-03` Student gate from **PASS WITH NOTES** to **RETEST REQUIRED**. Retest required path with optional cells skipped, then test the optional branch separately. |
| CLARIFY | [courseware/instructor-solutions/day-1/LAB-D1-03-shapes-activations-SOLUTION.ipynb](../instructor-solutions/day-1/LAB-D1-03-shapes-activations-SOLUTION.ipynb), activation implementation and "Optional Extension: Leaky-ReLU Slope" | Mirror the participant structure exactly: keep the core solution independent of Leaky ReLU and place all Leaky-ReLU answers, outputs, and instructor notes under an explicit optional heading. | The solution must not silently turn optional participant work into required instructor pacing or validation evidence. | No live time; approximately 10-15 minutes authoring plus execution. | **P1** | Lab Solution Engineer | Reset `LAB-D1-03` Solution gate from **PASS** to **RETEST REQUIRED**. Run a clean solution execution after the revised Student gate passes. |
| CLARIFY | [courseware/00-course-design/lab-map.md](../00-course-design/lab-map.md), `LAB-D1-03`; [courseware/day-1/student-guide/day-1-student-guide.md](../day-1/student-guide/day-1-student-guide.md), "Activation Preview for the Observatory" | Retain `LESSON-D1-05` and `ACT-D1-03` as prerequisites after moving them earlier. Revise the starter-state description so required TODOs list sigmoid, tanh, ReLU, and softmax; identify Leaky ReLU only as an optional comparison. Remove language saying the lab precedes formal nonlinearity instruction. | This reconciles architecture, schedule, guide, notebook, and gate contract without deleting an outline topic. | No live change. | **P1** | Course Architect and Lesson Developer | Contract change is covered by the D1-03 Student/Solution resets above. No reset for D1-01, D1-02, or D1-04. |
| ADD PRACTICE | [courseware/day-1/assessments/day-1-checks.md](../day-1/assessments/day-1-checks.md), `CHECK-D1-01`, `CHECK-D1-03`, and `CHECK-D1-04`; matching instructor and Student Guide sections | Schedule `CHECK-D1-01` Scenario B.4 inside the noon block: 8 minutes for D1-01 including evidence probes, 5 minutes for the D1-02 commitment, and 2 minutes for collection. Assign `CHECK-D1-03` item 5 and `CHECK-D1-04` items 2 and 5 as a five-minute consolidation task due before Day 2 at 09:00; sample one response in the existing Day 2 opening retrieval. State the due time and collection mechanism in all three artifacts. | "Follow-up" without a time or collection event is easily omitted and weakens retrieval evidence. | Day 1: 0 net minutes. Outside live session: 5 participant minutes. Day 2: use existing retrieval time. | **P1** | Lesson Developer | None. |
| ADD ACTIVITY | [courseware/instructor-guide/day-1-instructor-guide.md](../instructor-guide/day-1-instructor-guide.md), "Exact 450-Minute Schedule"; create a rehearsal record under `courseware/reviews/` | Conduct one uninterrupted 450-minute rehearsal with a participant who meets the stated Python/NumPy prerequisites but has not taken the neural-network course. Record actual block times, help events, unfinished tasks, debrief completion, and assessment completion. Require D1-03 core completion without optional Leaky ReLU in 40 minutes and preserve both breaks, lunch, and the final buffer. | Notebook execution time measures compute, not novice reasoning, writing, debugging, discussion, or transitions. | Staff time: 450 minutes plus approximately 30 minutes debrief. No production-course time change. | **P1** | Course Orchestrator coordinates; Lesson Developer facilitates; independent novice participant supplies evidence | No automatic reset. Any resulting notebook edit resets only the affected Student/Solution gates. |
| CLARIFY | [courseware/instructor-guide/day-1-instructor-guide.md](../instructor-guide/day-1-instructor-guide.md), "Scope Protection" and each block's cut line | Add explicit behind/ahead routes. Behind: cut application catalogue, extra output-head examples, Leaky-ReLU optional work, and extra probes; use precomputed arrays or static evidence when environment recovery consumes time; never cut predictions, core debriefs, breaks, or `CHECK-D1-04`. Ahead: add one unfamiliar shape/invariant transfer probe or require a disconfirming observation; do not begin Day 2 mathematics or promote optional activation taxonomy. | Current cut lines are strong, but an ahead-of-plan route is missing and behind-plan guidance is distributed rather than operationalized. | No planned time change; routes consume only recovered or surplus time. | **P1** | Lesson Developer | None unless a notebook is modified. |
| KEEP | [courseware/instructor-guide/day-1-instructor-guide.md](../instructor-guide/day-1-instructor-guide.md), "Misconception Routing Table"; [courseware/day-1/student-guide/day-1-student-guide.md](../day-1/student-guide/day-1-student-guide.md), misconception clinics | Preserve the symptom -> discriminating question -> evidence route structure and the prohibition on anthropomorphic explanations. | These are specific, economical, and tightly coupled to observable evidence. | No change. | P2 | Lesson Developer | None. |
| CLARIFY | [courseware/reviews/day-1-participant-lab-summary.md](day-1-participant-lab-summary.md) and [courseware/reviews/day-1-solution-summary.md](day-1-solution-summary.md) | Preserve the current non-blocker dispositions: plot-label overlap is optional polish; hosted Colab remains unvalidated; the D1-01 threshold-count discrepancy is incidental and outside the participant contract. Do not convert any of these into a release blocker unless the delivery environment or canonical contract changes. | These notes do not currently prevent interpretation, local CPU execution, or objective attainment. | No live change. | P2 | Course Orchestrator | None in their current state. Later canonical plot-code edits trigger lab-specific retesting. |

## 6. Missing Reinforcement Opportunities

1. **Softmax axis semantics:** Reuse D1-03's class-axis invariant when multiclass outputs next appear. Require participants to label the semantic axis before naming its numeric index.
2. **Batch size versus parameter count:** Retrieve `CHECK-D1-02` when Day 2 introduces batches. Ask which arrays change with batch size and which trainable arrays do not.
3. **Representation versus optimization:** Reuse `CHECK-D1-03` during the first Day 2 broken-model diagnosis. Ask whether more epochs can repair a representational limitation.
4. **Boundary versus confidence:** Ensure `CHECK-D1-01` Scenario B.4 is collected so positive common scaling is supported by both boundary and off-boundary probability evidence.
5. **Transfer to a new architecture:** Add one ahead-of-plan probe using an unfamiliar architecture such as `3 -> 5 -> 2`, requiring shapes, parameter count, and one semantic invariant without copying the recurring `4 -> 8 -> 3` table.

## 7. Missing Misconceptions

1. **Probability-shaped is not necessarily calibrated.** The Student Guide mentions this, but no retrieval or assessment asks participants to distinguish normalization from calibration.
2. **A 2D hidden projection is incomplete evidence.** Slide 28 notes the limitation, but the participant debrief should explicitly prevent treating a projection as the full six-dimensional representation.
3. **Positive common scaling is a special case.** Clarify that multiplying all affine parameters by a positive constant preserves the `0.5` boundary, while zero or negative scaling changes the interpretation.
4. **Equivalent outputs can have different parameterizations.** The course shows affine collapse but should explicitly state that more parameters do not guarantee a richer input-output function.
5. **A current all-zero ReLU region is not permanent unit death.** This misconception is already addressed well; preserve it when Leaky ReLU moves out of the required path.

## 8. Pacing Corrections

### Reconciled Afternoon Schedule

| Time | Minutes | Block |
|---|---:|---|
| 13:15-13:45 | 30 | `LESSON-D1-04` + `ACT-D1-04` |
| 13:45-14:02 | 17 | `LESSON-D1-05` + `ACT-D1-03` |
| 14:02-14:42 | 40 | `LAB-D1-03` |
| 14:42-14:57 | 15 | Protected break |
| 14:57-15:05 | 8 | `LESSON-D1-06` forward-trace consolidation |
| 15:05-16:05 | 60 | `LAB-D1-04` |
| 16:05-16:20 | 15 | `CHECK-D1-03`, `CHECK-D1-04`, Day 2 bridge |
| 16:20-16:30 | 10 | Protected recovery/questions/close |

The day remains exactly 450 elapsed minutes.

### If Behind

- Cut the application catalogue, extended output-head cases, and all optional Leaky-ReLU work first.
- Use precomputed activation arrays or static evidence if implementation blocks visual comparison.
- Preserve prediction commitments, D1-03 wrong-axis diagnosis, all core debriefs, `CHECK-D1-04`, breaks, lunch, and the final buffer.
- Do not use the final buffer for new activation or Day 2 content.

### If Ahead

- Give one unfamiliar architecture for shape and parameter transfer.
- Ask for an observation that would disconfirm a proposed diagnosis.
- Add one copied-parameter probe in D1-04, preserving canonical parameters.
- Do not start loss, gradients, backpropagation, or optional activation taxonomy.

### Rehearsal Acceptance Threshold

The schedule is accepted only when a qualified novice can:

- complete each required prediction before its reveal;
- complete D1-03 core work without Leaky-ReLU optional cells in 40 minutes;
- participate in each lab debrief rather than merely finish code;
- complete the noon assessment allocation in 15 minutes;
- complete the live portions of `CHECK-D1-03` and `CHECK-D1-04` in 13 minutes, leaving the two-minute bridge;
- retain both 15-minute breaks, the 60-minute lunch, and the 10-minute recovery buffer.

## 9. Highest-Priority Revisions Before Delivery

1. Reconcile the afternoon sequence and D1-03 prerequisite contract across the flow, guides, slides, and lab map.
2. Move Leaky-ReLU work out of the required D1-03 path in both participant and solution notebooks.
3. Reset and rerun the D1-03 Student and Solution gates, including a core run that skips the optional section.
4. Generate the five missing Day 1 visual assets, render the 32-slide PDF, and complete render validation.
5. Assign explicit times and collection rules to all deferred check items.
6. Run and document the timed novice rehearsal.
7. Re-review only the revised surfaces and close the required findings before delivery.

## Non-Blocker Dispositions

### Plot-Label Overlap

**Disposition:** Non-blocking presentation polish.

The participant validation summary reports readable but occasionally overlapping fixed-point or probe labels in D1-01, D1-02, and D1-04. The plots still expose the required evidence. Offset or collision-avoidance changes may be deferred. If canonical plotting code is changed, rerun the affected lab's visual and execution gates.

### No Real Colab Session

**Disposition:** Non-blocking for a local CPU delivery with accurate environment wording.

The readiness notebook and all Day 1 participant and solution paths passed independently on the documented local CPU environment. No report may claim hosted-Colab validation until readiness and the relevant notebook paths run in a fresh Colab CPU session. If hosted Colab is made a delivery requirement, this note becomes an environment gate rather than a pedagogy blocker.

### D1-01 Threshold-Count Note

**Disposition:** Non-blocking narrative discrepancy.

The solution summary records an incidental exact threshold-count difference between an earlier participant-validation narrative and the final selected solution path. The participant contract requires comparison and explanation, not a specific changed-decision count. The clean solution documents four changed decisions. No notebook or assessment gate reset is required unless the canonical threshold experiment or its assertions are changed.

## Final Revision Acceptance Checklist

- [x] Current status is **PASS WITH NOTES** with no required pedagogy finding open.
- [x] The Day 1 afternoon order is identical in the course flow, Student Guide, instructor guide, slide order, and lab prerequisites.
- [x] `LESSON-D1-05` and `ACT-D1-03` occur before `LAB-D1-03`.
- [x] `LESSON-D1-06` still occurs before `LAB-D1-04`.
- [x] D1-03's required path no longer asks learners to predict, implement, plot, or explain Leaky ReLU.
- [x] D1-03's optional Leaky-ReLU section is independently skippable without breaking later core cells.
- [x] The D1-03 solution mirrors the same core/optional boundary.
- [x] The D1-03 Student gate was rerun from a fresh kernel and restored to PASS WITH NOTES.
- [x] The D1-03 Solution gate was rerun after Student PASS and restored to PASS.
- [x] D1-04 received only an ID/link/prerequisite audit because its canonical notebook did not change.
- [x] All five named Day 1 PNG assets exist under `courseware/shared/assets/day-1/`.
- [x] `courseware/slides/day-1-see-it.pdf` exists and contains all 32 slides.
- [x] Slide-render validation confirms no missing images, clipping, broken paths, illegible labels, or absent visual notes/alt text.
- [x] `CHECK-D1-01` Scenario B.4 has an in-block time allocation.
- [x] `CHECK-D1-03` item 5 and `CHECK-D1-04` items 2 and 5 have an explicit due time, collection method, and retrieval event.
- [ ] A timed 450-minute novice rehearsal remains an accepted operational follow-up; no novice-validated timing claim is made.
- [x] Behind-plan and ahead-of-plan instructions are explicit in the instructor guide.
- [x] Plot-label overlap remains documented as optional because it does not obscure required evidence.
- [x] Colab wording continues to say "not yet validated" because no real hosted run has occurred.
- [x] The D1-01 threshold-count note remains non-blocking because the canonical experiment contract is unchanged.
- [x] No Day 1 objective, primary lab, or required course-outline topic was removed or moved to another day.

## Architecture-Owned Disposition

**Resolved in architecture on 2026-08-16:** The canonical blueprint and course flow now place `LESSON-D1-05` and `ACT-D1-03` before `LAB-D1-03`, retain `LESSON-D1-06` immediately before `LAB-D1-04`, preserve the protected break and final buffer, and keep Day 1 at exactly 450 elapsed minutes. The D1-03 planning contract now requires sigmoid, tanh, ReLU, and numerically stable softmax, with Leaky ReLU independently skippable and optional.

Downstream guide, slide, notebook, gate, asset, and assessment-follow-up items are closed by the Final Revision Disposition above. The novice rehearsal remains an accepted operational follow-up. No objective, ID, primary lab, or Day 2-4 architecture was changed.
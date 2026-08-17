# Capstone Instructor Guide: The Neural Network Investigation

**Instructor only. Exclude from participant release packages.**

**Canonical lab:** `LAB-D4-04`  
**Participant notebook:** `courseware/capstone/capstone-starter.ipynb`  
**Canonical solution:** `courseware/capstone/capstone-solution.ipynb`  
**Supplementary case key:** `courseware/instructor-solutions/day-4/capstone-case-key.md`  
**Participant support:** `courseware/capstone/capstone-student-guide.md`, `courseware/capstone/capstone-rubric.md`

All four Day 4 participant labs and all four solution counterparts report **PASS WITH NOTES** on the recorded local CPU stack. The capstone profiles `A`, `B`, and `C` passed both live and validation-only recovery paths, including the test lock. Do not improvise with or distribute the solution notebook or case key as participant recovery material. Hosted Colab, novice rehearsal, cross-device identity, and production latency remain unvalidated.

## Purpose and Boundaries

Participants investigate a compact neural network over scikit-learn digits framed as handwritten routing-code recognition. The task is intentionally small so teams can inspect curves, errors, slices, and resource evidence under a fixed budget. It does not simulate a production routing system or frontier-scale workflow.

The capstone product is a defensible evidence chain. More than one intervention can be acceptable; the profile key identifies intended primary limitations for calibration, not answers participants must guess.

## Canonical Profile Key

Use letters only in every participant-visible artifact, filename, display, and announcement.

| Profile | Instructor-only primary limitation | Expected baseline evidence | Strong first intervention families |
|---|---|---|---|
| `A` | training-data/class imbalance with weak worst-class recall | macro-F1 materially below accuracy; one or more weak classes/slices; aggregate can obscure harm | class weighting, balanced sampling, or targeted data composition change; require overall-regression bound |
| `B` | high capacity on constrained data/high variance | near-perfect training behavior; weaker validation; widening gap or validation peak | one regularizer, smaller width, early stopping, or more valid training data; one major change only |
| `C` | ineffective or unstable optimization configuration | stalled/oscillatory loss, weak train and validation behavior, no stable convergence | one learning-rate or optimizer correction; invariant check if instability could be implementation |

Do not name these diagnoses before defenses. Secondary issues may be real. Score the evidence chain, not agreement with this table.

## Before Class

1. Confirm the participant starter, solution, and case key still match their **PASS WITH NOTES** validation records.
2. Confirm the recorded clean-CPU evidence covers all three live cases and all three validation-only recovery paths.
3. Verify the fixed split hash, profile artifacts, case-letter display, and test lock.
4. Record package versions, device, thread settings, runtime, metric bands, and timing method.
5. Confirm no case filename, variable, color, or metadata reveals the intended diagnosis.
6. Prepare one cached baseline and one cached authorized intervention output per acceptable profile route.
7. Verify cached outputs contain no completed narrative answers.
8. Open the evidence-board and rubric visuals.
9. Prepare assignment cards with only `A`, `B`, or `C`.
10. Keep the canonical solution and case key out of shared/projected participant navigation.

## Team Assignment

Prefer teams of 3-4. Balance case counts across the cohort; do not assign based on presumed learner strength. Give only the letter and a launch token. Rotate evidence/experiment/validity/resource roles after Gate 3.

For small cohorts, use one team per profile. For large cohorts, duplicate profiles and compare different valid intervention choices during debrief without naming a winner by accuracy.

## Exact 95-Minute Run

| Time in block | Move | Gate/output |
|---:|---|---|
| 0-5 | Frame routing-code task, scope boundary, rubric | no diagnosis language |
| 5-10 | Assign A/B/C; confirm roles and test lock | case letter and split/hash |
| 10-20 | Baseline validity audit | Gate 1 facts |
| 20-30 | Curves, confusion, slice/error inspection | quantified evidence |
| 30-35 | Rank hypotheses and request one evidence card | Gate 2 commitment |
| 35-45 | Reveal approved evidence; design one run | Gate 3 contract |
| 45-65 | Execute or cached-output recovery | complete ledger |
| 65-75 | Aligned baseline/intervention comparison | quality/generalization/resource evidence |
| 75-80 | Accept/reject/narrow diagnosis | interpretation locked |
| 80-85 | Optional run decision; default is no | information-value justification |
| 85-90 | Lock checkpoint/claim; authorize test | Gate 4 record |
| 90-95 | One test access and defense preparation | Gate 5 report |

The shared `15:50-16:10` block supports four sequential five-minute defenses. With more than four teams, preassign parallel panels or timed recordings before the capstone begins. Every topology uses the same rubric, five-minute entitlement, skeptical-question rule, and post-defense individual `CHECK-D4-04`; do not substitute a team board or recording for the individual check.

## Evidence Reveal Policy

Each team may request one evidence reveal before the primary run. Provide only the requested card when it discriminates between stated hypotheses.

Possible cards:

- per-class support and recall;
- aligned unsmoothed train/validation loss;
- confusion pair counts;
- high-confidence error sample with label-review status;
- parameter count/model size;
- baseline seed/repeat snapshot;
- timing-method detail;
- preprocessing/split provenance.

Do not reveal a configuration label such as "imbalanced," "overfit," or "bad learning rate." Ask: "Which alternatives will this card separate?"

## Hint Ladder

Use the lowest sufficient hint. Record help events for scoring context.

### Level 1 - Orient to evidence

- "Which observation belongs in facts rather than hypotheses?"
- "Compare absolute train and validation behavior, not only the gap."
- "Which class or slice contributes disproportionately?"

### Level 2 - Force alternatives

- "Name a data explanation and an optimization explanation for the same symptom."
- "What result would make your leading diagnosis wrong?"
- "Which one missing card would separate the top two?"

### Level 3 - Constrain the experiment

- "Circle the single major factor that changes."
- "Write expected train, validation, slice, and resource directions."
- "Which field proves the split and checkpoint remained fixed?"

### Level 4 - Profile-specific nudge

- `A`: "Compare aggregate quality with per-class support and worst-class recall."
- `B`: "Find the epoch where validation stops following training."
- `C`: "Ask whether the training path is stable enough to diagnose capacity."

### Level 5 - Recovery direction

Offer two intervention families without selecting one. Require mechanism and rejection evidence before authorization.

## Acceptable Interventions

| Profile | Acceptable | Usually weak without more evidence |
|---|---|---|
| `A` | class weighting; balanced sampler; targeted training composition; bounded slice-specific collection plan | bigger model; threshold-only multiclass fix without consequence rationale |
| `B` | early stopping; one weight decay/dropout change; smaller architecture; more representative training data | longer training; simultaneous regularizer sweep |
| `C` | one learning-rate change; optimizer change under fixed settings; normalization/invariant repair when evidence supports it | more capacity before stable optimization; changing LR and optimizer together |

An off-key intervention can score strongly if the team has coherent evidence and rejection criteria. An intended intervention can score poorly if selected by guessing.

## Cached-Output Recovery

Use recovery after one bounded technical attempt or when a run would consume the defense window.

1. Preserve the team's pre-run record.
2. Capture the first failed invariant/error.
3. Attempt one repair that does not change the experiment.
4. Load the exact case/configuration cached output.
5. Display a visible **CACHED EVIDENCE** label.
6. Record source artifact, seed/config hash, and why live execution failed.
7. Continue comparison and defense.

Never use the solution notebook as recovery. Do not provide a cached output for a configuration the team did not authorize. A cached result preserves reasoning time but does not validate participant execution.

## Test-Lock Policy

The test set estimates the final locked decision; it is not an experiment dashboard.

- Hide test targets/metrics until Gate 4.
- Require hypothesis status, checkpoint, threshold/metric rule, and expected test range before access.
- Issue one authorization token per team.
- Log access time and selected record hash.
- Permit one test evaluation.
- If test conflicts with validation, narrow the claim and stop selection.
- Do not grant another test look after a model change.

A test-policy violation triggers the rubric caps. Preserve the event as teachable evidence; do not quietly reset the notebook.

## Scoring Anchors

Use the public 25/20/20/15/10/10 weights.

### Strong profile evidence

- `A`: compares macro/per-class behavior and support, improves or meaningfully tests worst-class behavior, and bounds overall regression.
- `B`: identifies strong training versus weaker held-out evidence, chooses one rescue, and evaluates absolute validation plus gap.
- `C`: distinguishes unstable/ineffective optimization from high bias, changes one optimization factor, and checks stability as well as final score.

### Strong negative result

Full design/diagnosis credit is possible when controls hold, prediction precedes compute, evidence rejects/narrows the mechanism, and the next experiment targets remaining uncertainty.

### Calibration rule

Do not award explanation credit for claims beyond the fixed digits case/environment. "This intervention improved profile A under the supplied split" is stronger than "this solves routing-code recognition."

## Defense Facilitation

Keep each defense to five minutes:

1. baseline/diagnosis: 60 seconds;
2. evidence/alternative: 60 seconds;
3. intervention/prediction: 60 seconds;
4. result/resources: 60 seconds;
5. decision/next step: 60 seconds.

The team evidence board and defense package contain no `individual_transfer` field. After the defense, each learner completes `CHECK-D4-04` separately. Score recorded and parallel-panel defenses with the same anchors as sequential live defenses.

Assign one peer team to submit a challenge question. Ask one of:

- "What evidence would make your diagnosis wrong?"
- "Why was this higher information than the next-best option?"
- "What did the negative result teach?"
- "Which claim changed after test access?"
- "Which resource number is least portable?"

Do not reveal profile diagnoses between defenses. After all boards are locked, debrief the distinct evidence patterns and acceptable alternatives.

## Common Failures and Interventions

| Failure | Instructor move |
|---|---|
| team hunts for profile key | restate that scoring follows evidence, not hidden-label accuracy |
| aggregate accuracy dominates | require worst-class/slice and consequence evidence |
| multiple changes proposed | ask which result can be attributed; return to Gate 3 |
| test requested early | ask which development decision is not yet locked |
| null result called failure | ask which hypothesis became less likely |
| gap-only diagnosis | ask for absolute train/validation levels and path |
| timing claim lacks method | require environment, warm-up, repeats, and batch/load |
| cached output treated as live | require visible cached label and source record |
| digits realism overclaimed | ask which production properties the dataset omits |
| defense narrates actions | point to evidence-board arrows and ask what changed the decision |

## Behind and Ahead

### Behind

- Use cached output after one bounded repair.
- Skip optional evidence cards.
- Forbid the second run.
- Preserve Gates 2-5 and the defense; do not trade interpretation for compute.

### Ahead

- Audit one competing diagnosis.
- Ask whether not spending the second run is defensible.
- Add one sensitivity or uncertainty statement without test reuse.
- Rehearse a skeptical defense question.

Do not introduce quantization, mixed precision, model parallelism, or deep interpretability implementation.

## Post-Capstone Record

Capture per profile:

- completion and help events;
- primary intervention family;
- hypothesis accepted/rejected/narrowed;
- test-lock compliance;
- cached-output use;
- rubric dimension scores;
- individual `CHECK-D4-04` transfer status;
- notebook/runtime defects for Lab Engineer or Lab Solution Engineer.

Current validation supports local CPU **PASS WITH NOTES** for the participant/solution pair and A/B/C live and recovery execution. Release claims must continue to exclude hosted Colab, novice rehearsal, cross-device identity, and production latency until those gates are separately exercised. Keep the team evidence board/defense and each learner's `CHECK-D4-04` as distinct records.

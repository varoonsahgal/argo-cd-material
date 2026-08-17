# Day 4 Instructor Guide: Think Like an ML Engineer

**Instructor only. Do not distribute with participant materials.**

**Canonical question:** The model trained successfully, but is it actually good, and what should improve next?  
**Day outcome:** Participants choose consequence-aware evidence, diagnose curves and slices, run one controlled/reproducible experiment, compare quality with resources, and defend an anonymous capstone investigation.  
**Must-land sentence:** **A defensible improvement is a chain of evidence, not a score delta.**

## Controlling Artifacts

- Participant guide: `courseware/day-4/student-guide/day-4-student-guide.md`
- Participant challenges: `courseware/day-4/challenges/day-4-challenges.md`
- Challenge key: `courseware/instructor-solutions/day-4/day-4-challenges-SOLUTION.md`
- Participant checks: `courseware/day-4/assessments/day-4-checks.md`
- Check key: `courseware/instructor-solutions/day-4/day-4-checks-SOLUTION.md`
- Capstone participant guide/rubric: `courseware/capstone/capstone-student-guide.md`, `courseware/capstone/capstone-rubric.md`
- Capstone instructor guide: `courseware/capstone/capstone-instructor-guide.md`
- Slide source: `courseware/slides/day-4-think-like-an-ml-engineer.md`
- Required assets: `courseware/shared/assets/day-4/`

## Objective and Evidence Map

| Objective | Must observe | Practice | Assessment |
|---|---|---|---|
| `OBJ-D4-01` | error consequence changes metric/threshold decision | `ACT-D4-01`, `LAB-D4-01` | `CHECK-D4-01` |
| `OBJ-D4-02` | train/validation levels, gap, and path separate hypotheses | `ACT-D4-02`, `LAB-D4-02` | `CHECK-D4-02` |
| `OBJ-D4-03` | quantified slices prioritize work beyond aggregate | `LAB-D4-02`, capstone | `CHECK-D4-02`, rubric |
| `OBJ-D4-04` | one change, predicted and rejecting evidence | `LAB-D4-03`, capstone | `CHECK-D4-03`, rubric |
| `OBJ-D4-05` | complete environment/data/config/result record | `LAB-D4-03`, capstone | `CHECK-D4-03`, rubric |
| `OBJ-D4-06` | quality/resource choice changes with constraint | `ACT-D4-03`, `LAB-D4-03` | `CHECK-D4-03`, rubric |
| `OBJ-D4-07` | same evidence loop transfers to seven categories | `ACT-D4-04` | `CHECK-D4-04` |
| `OBJ-D4-08` | team evidence-chain defense plus individual transfer | capstone/defense | rubric, `CHECK-D4-04` |

## Exact 450-Minute Schedule

| Time | Min | Mode and IDs | First cut if behind |
|---|---:|---|---|
| 09:00-09:15 | 15 | retrieval + `LESSON-D4-01` baseline | third sample chain discussion |
| 09:15-09:35 | 20 | `ACT-D4-01`, metrics/threshold visual | ROC mechanics, never consequence decision |
| 09:35-10:15 | 40 | `LAB-D4-01` | extra thresholds; preserve recommendation/debrief |
| 10:15-10:30 | 15 | protected break | never cut |
| 10:30-10:45 | 15 | `LESSON-D4-02`, `ACT-D4-02` | fourth curve reveal depth |
| 10:45-11:25 | 40 | `LESSON-D4-03`, `LAB-D4-02` | extra gallery examples |
| 11:25-11:35 | 10 | `CHECK-D4-01`, `CHECK-D4-02` | preserve both five-minute checks |
| 11:35-12:35 | 60 | protected lunch | never cut |
| 12:35-12:55 | 20 | `LESSON-D4-04`-`06`, `ACT-D4-03` | mixed-precision/quantization references |
| 12:55-13:45 | 50 | `LAB-D4-03` | optional second comparison; preserve rerun/record |
| 13:45-14:00 | 15 | protected break | never cut |
| 14:00-14:15 | 15 | `LESSON-D4-07`, `ACT-D4-04` | card detail; preserve evaluation design |
| 14:15-15:50 | 95 | `LESSON-D4-08`, `LAB-D4-04` | optional run; preserve interpretation/test lock |
| 15:50-16:10 | 20 | team five-minute defenses | use parallel panels, not shorter defenses |
| 16:10-16:20 | 10 | `CHECK-D4-03`, `CHECK-D4-04` | preserve individual evidence |
| 16:20-16:30 | 10 | protected buffer/close | no new content |

Total: `450` minutes.

## Current Production and Source Status

**Source-check date:** 2026-08-17.

| Claim | Status | Delivery implication |
|---|---|---|
| scikit-learn precision/recall/F1 expose `zero_division`; default warns | verified against current stable official API | examples set policy explicitly and explain no-positive cases |
| scikit-learn confusion matrix uses true-label rows, predicted-label columns | verified | label axes every time |
| ROC AUC is area under score-ranking ROC, not a threshold selector | verified/qualified | never say AUC chooses the operating point |
| `load_digits` has 1,797 8x8 examples, ten classes, 64 flattened features | verified | digits is a small classroom surface, not production realism |
| PyTorch does not guarantee exact reproduction across releases/platforms/CPU-GPU | verified/qualified against current 2.13 docs | state environment/tolerance; same seed is insufficient |
| deterministic operations may cost performance | verified/qualified | do not promise free determinism |
| reliable PyTorch timing needs representative threads/inputs, warm-up/repeats, and CUDA synchronization | verified/qualified | no hardware-free speed claims |

All four participant labs and all four solution counterparts report **PASS WITH NOTES** on the recorded local CPU stack. The capstone validation exercised profiles `A`, `B`, and `C` through both live and validation-only recovery paths, including the test lock. This evidence does not validate hosted Colab, novice rehearsal, cross-device identity, or production latency.

## Before Class

1. Confirm the four participant **PASS WITH NOTES** reports still match the canonical notebook hashes.
2. Confirm the four solution **PASS WITH NOTES** reports still match:
   - `courseware/instructor-solutions/day-4/LAB-D4-01-accuracy-is-not-enough-SOLUTION.ipynb`;
   - `courseware/instructor-solutions/day-4/LAB-D4-02-model-detective-SOLUTION.ipynb`;
   - `courseware/instructor-solutions/day-4/LAB-D4-03-one-experiment-SOLUTION.ipynb`;
   - `courseware/capstone/capstone-solution.ipynb`.
3. Confirm the supplementary `courseware/instructor-solutions/day-4/capstone-case-key.md` remains instructor-only and aligned to the validated A/B/C paths.
4. Record Python, scikit-learn, PyTorch, NumPy, device, threads, and asset versions.
5. Pre-run every required CPU path; verify fixed split/hash, metric orientation, threshold candidates, and `zero_division` handling.
6. Prepare cached participant-safe evidence; never use solution notebooks as fallback.
7. Select three anonymized Day 3 chains: strong, weak limitation, unfocused next experiment.
8. Confirm the cohort **Day 4 Checks** channel and team assignment cards.
9. Open all slide assets and verify paths against the render-validated 34-page PDF.
10. Review capstone test-lock tokens and evidence reveal cards.

## Recovery Contract

After one bounded repair:

- preserve prediction and experiment record;
- name the failed invariant;
- load matched participant-safe cached evidence;
- label it visibly;
- continue observation/debrief;
- log the failure for retest.

Fallback preserves learning time; it does not create lab validation.

## If Behind

Cut ROC derivation, extra curve cards, extra error images, hyperparameter catalogue, nondeterminism internals, frontier-card detail, and all optional second runs. Switch to cached evidence after one repair. Preserve every prediction gate, all four checks, capstone interpretation/test lock, defenses, breaks/lunch, and buffer.

## If Ahead

Request one stronger competing explanation, audit one bucket overlap, compare an alternative cost model, inspect a timing uncertainty, or rehearse a skeptical defense. Do not add mixed precision, quantization, model parallelism, deep interpretability, or safety-system implementation.

---

# Facilitation Runbook

## 09:00-09:15 - Retrieval + LESSON-D4-01

**Must land:** A claim is only as strong as its limitation and discriminating next experiment.

| Minute | Move |
|---:|---|
| 0-3 | Learners open original Day 3 live response and appended consolidation without editing. |
| 3-8 | Project strong chain; identify why its next experiment separates alternatives. |
| 8-12 | Project weak-limitation and unfocused-experiment chains; repair only the failed link. |
| 12-15 | Ask what equal accuracy omits; introduce consequence-first evaluation. |

**Questions/answers**

- Q: What makes a limitation real? A: It could plausibly weaken/reverse the claim and names missing evidence.
- Q: What makes a next experiment high-information? A: Competing explanations predict different observable outcomes.
- Q: Why retrieve originals? A: Revision quality is invisible if first states are overwritten.

Use the experiment-chain visual. If Day 3 consolidation is missing, supply a blank claim/evidence/limitation/experiment table; do not invent a learner response.

## 09:15-09:35 - ACT-D4-01 + Metrics

**Must land:** Metric and threshold follow consequences.

| Minute | Move |
|---:|---|
| 0-4 | State fraud stakeholders and collect costly-error vote before formulas. |
| 4-9 | Reveal confusion orientation and calculate precision/recall. |
| 9-14 | Move threshold through three states; synchronize counts and cost. |
| 14-17 | Reverse cost ratio; require revised recommendation. |
| 17-20 | Bound PR/ROC overview; state that AUC does not select threshold. |

**Questions/answers**

- Q: Lower threshold changes what? A: Decisions/counts; not learned parameters or score ranking.
- Q: Why not F1 alone? A: It weights precision/recall equally and omits this cost model.
- Q: Undefined precision? A: Expose no positive predictions; set `zero_division` intentionally rather than hiding behavior.

Use `threshold-confusion-cost.svg`. Cut ROC construction first.

## 09:35-10:15 - LAB-D4-01

**Participant path:** `courseware/day-4/labs/LAB-D4-01-accuracy-is-not-enough.ipynb`  
**Solution path:** `courseware/instructor-solutions/day-4/LAB-D4-01-accuracy-is-not-enough-SOLUTION.ipynb`

| Minute | Move |
|---:|---|
| 0-5 | prediction: baseline utility, costly error, threshold direction |
| 5-12 | majority baseline reveal; require minority recall |
| 12-25 | threshold sweep, confusion/PR/cost observation |
| 25-32 | scenario comparison and operating recommendation |
| 32-38 | limitation/alternative and stakeholder challenge |
| 38-40 | debrief sentence |

**Expected evidence:** majority baseline can have high accuracy and zero minority recall; lowering threshold usually raises recall/FP; cost-minimizing threshold differs by scenario. Use actual validated notebook bands when available, not planning values.

**Fallback:** matched threshold table/visual. **Debrief:** "Which evaluation rule failed, and what decision changed?"

## 10:30-10:45 - LESSON-D4-02 + ACT-D4-02

**Must land:** Levels, gap, and trajectory separate fit/generalization/optimization hypotheses.

Use `mystery-curves.svg`. Hide labels; require two observations and one alternative.

- Q: Both train/validation weak and smooth? A: underfit/high-bias family, but request duration/capacity/data evidence.
- Q: Train strong, validation worsens? A: overfit/high-variance family; split/data alternatives remain.
- Q: Oscillation? A: optimization/implementation family before capacity changes.
- Q: Small gap enough? A: no; both can be poor.

Cut the fourth configuration detail, not alternatives/rejection evidence.

## 10:45-11:25 - LESSON-D4-03 + LAB-D4-02

**Participant path:** `courseware/day-4/labs/LAB-D4-02-model-detective.ipynb`  
**Solution path:** `courseware/instructor-solutions/day-4/LAB-D4-02-model-detective-SOLUTION.ipynb`

| Minute | Move |
|---:|---|
| 0-5 | explain error funnel; predict largest versus highest-value bucket |
| 5-15 | hidden curve diagnosis and staged reveal |
| 15-25 | confusion pairs, confidence, selected errors |
| 25-33 | define/count slices and overlap policy |
| 33-38 | prioritize using prevalence, consequence, fixability |
| 38-40 | one experiment plus rejection evidence |

Use `error-funnel.svg`. Ask: "What would cherry-picked images hide?" Expected: prevalence/base rate and representativeness. Accept multiple bucket schemas when definitions/accounting are explicit.

**Fallback:** mystery-curve, confusion, error-gallery, and slice table matched to one baseline. **Cut:** extra images, never quantification/debrief.

## 11:25-11:35 - CHECK-D4-01 and CHECK-D4-02

Exactly five minutes each; collect the marked **live minimum** individually. Learners may answer in compact bullets. Any prompt marked **end-of-day consolidation** is appended without overwriting the live response and is due in **Day 4 Checks by 16:30**.

- D4-01 readiness: consequence -> metric/counts -> threshold direction -> AUC correction -> assumption.
- D4-02 readiness: two curve observations -> alternative -> quantified slice priority -> falsifiable action -> gap correction.

If metric reasoning is weak after collection, begin the afternoon with one two-minute error-cost reversal. If curve reasoning is weak, require absolute train/validation observations before labels during D4-03.

## 12:35-12:55 - LESSON-D4-04 to 06 + ACT-D4-03

**Must land:** One controlled run must be interpretable, reproducible within a boundary, and evaluated on a quality/resource frontier. One-major-change is this course's attribution discipline for a constrained run, not a universal ban on planned factorial or sequential experimental designs.

| Minute | Move |
|---:|---|
| 0-5 | compare confounded versus one-change experiment chain |
| 5-10 | audit reproducibility record and tolerance |
| 10-18 | run three deployment rounds on Pareto table |
| 18-20 | state timing qualification and moved topics |

Use `experiment-chain.svg`, `reproducibility-record.svg`, `quality-resource-pareto.svg`.

**Questions/answers**

- Q: Can a negative result succeed? A: yes, if it resolves/narrows a hypothesis under controls.
- Q: Same seed everywhere? A: no; record release/platform/device and tolerance.
- Q: Batch-1 latency versus throughput? A: distinct objectives; batching can improve throughput while latency worsens.
- Q: GPU means faster? A: no; profile representative end-to-end work and synchronize asynchronous timing.

Mixed precision implementation, quantization, and model parallelism are `MOVE`.

## 12:55-13:45 - LAB-D4-03

**Participant path:** `courseware/day-4/labs/LAB-D4-03-one-experiment.ipynb`  
**Solution path:** `courseware/instructor-solutions/day-4/LAB-D4-03-one-experiment-SOLUTION.ipynb`

| Minute | Move |
|---:|---|
| 0-8 | audit baseline and reject confounded draft |
| 8-15 | one hypothesis/change/prediction/rejection/stop rule |
| 15-30 | primary run |
| 30-38 | record quality, curves, bytes, timing method |
| 38-44 | seeded rerun/tolerance comparison |
| 44-48 | accept/reject/narrow and name next experiment |
| 48-50 | debrief information gained |

**Expected evidence:** complete record matters more than mandatory gain; one option may improve quality yet violate budget; repeatability is within a declared tolerance, not exact equality.

**Fallback:** baseline/intervention serialized records and aligned plots from the same case/config. Do not compare mismatched device timing.

## 14:00-14:15 - LESSON-D4-07 + ACT-D4-04

**Must land:** Seven representative public categories reuse the same scientific loop; none is reduced to one aggregate score.

Use `frontier-case-cards.svg`.

| Category | Ask |
|---|---|
| capability | what behavior and unacceptable regression? |
| evaluation | how can the grader be wrong? |
| regression | what changed and on which slice? |
| data | provenance/composition or model mechanics? |
| efficiency | what quality/resource frontier? |
| safety | which rare high-consequence failure disappears in average? |
| internals | descriptive pattern or causal evidence? |

For coding evaluation, expected components are held-out tasks/slices, executable grader limits, blinded human sample, contamination controls, and regression gates. Label categories representative; do not imply private organizational workflow.

## 14:15-15:50 - LESSON-D4-08 + LAB-D4-04 Capstone

**Participant path:** `courseware/capstone/capstone-starter.ipynb`  
**Solution path:** `courseware/capstone/capstone-solution.ipynb`  
**Case key:** `courseware/instructor-solutions/day-4/capstone-case-key.md`

Follow `courseware/capstone/capstone-instructor-guide.md`. Display `capstone-evidence-board.svg` and `capstone-rubric-defense.svg`.

**Nonnegotiable gates:** baseline validity; ranked diagnosis/alternative/disconfirmation; one primary experiment; interpretation before test; one authorized test access; calibrated claim.

Profile assignments A/B/C reveal no diagnosis. Use hint ladder, cached-output recovery, rubric anchors, and test token exactly as specified in the capstone instructor guide.

## 15:50-16:10 - Team Defenses

The 20-minute block supports **four sequential five-minute defenses**. For more than four teams, preassign parallel panels or timed recordings before the capstone begins; do not shorten defenses. Apply the same 25 performance / 20 generalization / 20 experiment design / 15 diagnosis / 10 efficiency / 10 explanation rubric in every topology. Every learner still completes `CHECK-D4-04` individually after the defense; the team evidence board and defense do not include `individual_transfer`.

Ask one skeptical question. Reward revised hypotheses, sound negative results, preserved test lock, and bounded claims. Do not rank by accuracy.

## 16:10-16:20 - CHECK-D4-03 and CHECK-D4-04

Exactly five minutes each, individual. Collect the marked live minimum in each window; close any marked end-of-day consolidation at 16:30 without replacing the original response.

- D4-03: experiment attribution, reproducibility, timing, calibrated quality claim.
- D4-04: unfamiliar coding-evaluation transfer and digits realism boundary.

Use the central solution for scoring. Keep team rubric and individual transfer evidence separate.

## 16:20-16:30 - Final Transition

Use only for recovery, one must-land correction, and close.

Ask:

1. What is the consequence?
2. What evidence distinguishes the hypotheses?
3. What one experiment should run next?
4. What did it cost?
5. What can we honestly claim?

Close:

> "You began with one neuron's forward path. You finish with a model claim that names its evidence, alternatives, resource cost, and next experiment. The scale can change; that discipline does not."

## Scope Protection

### Core

Consequence-aware metrics/thresholds; confusion/PR and bounded ROC overview; bias/variance/optimization; quantified slices; one experiment; reproducibility/tolerance; latency/throughput/memory/size; seven representative categories; anonymous capstone evidence chain and defense.

### SHORTEN first

ROC mechanics; extra curve cards; extended shift taxonomy; hyperparameter catalogue; nondeterminism internals; extra frontier examples.

### MOVE/reference only

Mixed-precision implementation; quantization; model parallelism/distributed implementation; deep interpretability; complete safety systems. Do not use buffer or capstone time to teach these.

## Final Collection Record

Capture:

- original/revised Day 3 chain quality;
- D4-01 consequence/threshold readiness;
- D4-02 curve/slice readiness;
- D4-03 controlled record/resource readiness;
- capstone profile, intervention, cached use, test compliance, rubric dimensions;
- D4-04 individual transfer;
- unresolved notebook, source, timing, or asset defects.

Current evidence supports local CPU **PASS WITH NOTES** for all four participant/solution counterparts, A/B/C live and recovery execution, and the 34-page slide render. Keep hosted Colab, novice rehearsal, cross-device identity, and production latency explicitly unvalidated.

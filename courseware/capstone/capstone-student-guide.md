# Capstone Student Guide: The Neural Network Investigation

**Canonical lab:** `LAB-D4-04`  
**Live time:** 95 minutes investigation + shared 20-minute defense block  
**Task framing:** handwritten routing-code digit recognition  
**Cases:** anonymous `A`, `B`, or `C` only

## Mission

A routing center uses a compact neural network to recognize one handwritten digit from a routing code. You inherit a fixed dataset split, an anonymous baseline case, existing evidence, and a limited experiment budget.

Your job is not to search until a score rises. Your job is to decide what is most likely limiting the baseline, run one primary experiment that can test that diagnosis, and defend what the evidence supports.

The dataset is the small scikit-learn handwritten-digits dataset. It provides 1,797 8×8 images across ten classes. This is a fast classroom investigation surface, not evidence that the resulting model is ready for a real routing system.

## Non-Negotiable Constraints

- Work only on the assigned anonymous case `A`, `B`, or `C`.
- Do not infer case meaning from its letter; letters are identifiers only.
- Keep the supplied training, validation, and test manifests unchanged.
- Use the supplied baseline and evidence before proposing a change.
- Run **one primary experiment**.
- Change one major factor in that experiment.
- Record the complete experiment contract before compute.
- Do not access test targets or test metrics until the authorized test gate.
- Do not optimize repeatedly against test evidence.
- A second run is available only when the notebook explicitly authorizes it. Not using it can be the stronger decision.
- Cached outputs preserve the reasoning task if training cannot complete; label them as cached evidence.

## Fixed Budget

| Resource | Budget |
|---|---|
| Primary interventions | 1 |
| Optional follow-up | only if authorized after interpretation |
| Team investigation | 95 minutes |
| Defense | 5 minutes per team within the shared block |
| Test access | once, after the decision record is locked |
| Claim scope | this fixed classroom split, case, environment, and measurement contract |

## Team Roles

Use three or four roles and rotate once after the experiment gate:

- **Evidence lead:** separates facts, hypotheses, and observations.
- **Experiment lead:** protects the one-major-change contract.
- **Validity lead:** checks split, metric, threshold, and test-lock rules.
- **Resource/defense lead:** records runtime/size evidence and builds the five-minute explanation.

Every participant must still complete `CHECK-D4-04` individually.

**Separation contract:** Do not add `individual_transfer` to the team evidence board, notebook defense fields, recording, or team package. After the defense, each learner submits `CHECK-D4-04` separately in **Day 4 Checks**.

## Investigation Timeline

| Minute | Phase | Required product |
|---:|---|---|
| 0-10 | Brief and validity audit | case letter, split/hash, baseline contract, unanswered questions |
| 10-25 | Inspect baseline | curves, metrics, confusion/slices, selected examples, resource evidence |
| 25-35 | Diagnose and rank | primary hypothesis, alternative, disconfirming evidence |
| 35-45 | Design | one intervention, prediction, rejection result, stop rule |
| 45-65 | Execute | serialized record and bounded primary run |
| 65-78 | Compare | aligned baseline/intervention evidence and resource comparison |
| 78-85 | Interpret | accept, reject, or narrow the diagnosis |
| 85-95 | Authorized test and defense | one test report, calibrated claim, evidence board |

Do not compress the interpretation phase to gain another run.

## Evidence Board

Keep four lanes visually separate.

### Lane 1 - Facts

Record only supplied or directly observed facts:

- case letter;
- dataset/split identity and hash;
- architecture/configuration;
- train/validation curves;
- aggregate, class, and slice metrics;
- selected error examples;
- runtime/model-size evidence and method.

### Lane 2 - Hypotheses

Rank candidate limitation families without treating the list as a hidden answer:

- data or label issue;
- high bias/underfitting;
- high variance/overfitting;
- optimization;
- architecture/representation;
- evaluation;
- compute/resource constraint.

For the top two, state supporting and threatening evidence.

### Lane 3 - Experiment Record

Complete before compute:

> **Hypothesis:**  
> **One major change:**  
> **Kept fixed:**  
> **Expected curve/metric/slice/resource effects:**  
> **Observation that rejects or narrows the hypothesis:**  
> **Stop rule:**  
> **Seed, data/split, environment, metric, threshold, checkpoint, timing method:**

### Lane 4 - Interpretation and Next Step

After the run:

> **Observed result:**  
> **Comparison with prediction:**  
> **Diagnosis status:** accepted / rejected / narrowed / unresolved  
> **Alternative still plausible:**  
> **Cost or resource effect:**  
> **Calibrated claim:**  
> **Next experiment with another hour:**

## Evidence Gates

### Gate 1 - Baseline validity

Before diagnosis, confirm:

- the split roles and manifest are clear;
- preprocessing ownership is valid;
- metric averaging and threshold are explicit;
- curves use aligned axes;
- resource measurements name an environment and method.

If a validity question remains, record it as a limitation. Do not silently repair the case.

### Gate 2 - Diagnosis commitment

Submit:

1. the leading hypothesis;
2. two supporting observations;
3. one competing explanation;
4. evidence that would make the leading hypothesis wrong;
5. one requested evidence reveal, if offered.

### Gate 3 - Primary experiment authorization

The run is ready only when:

- exactly one major factor changes;
- expected and rejection evidence are observable;
- the split and metric contract remain fixed;
- the run fits the budget;
- the team can explain why this experiment is more informative than its alternatives.

### Gate 4 - Interpretation before test

Lock the development decision before test access:

- accept, reject, narrow, or leave unresolved the hypothesis;
- select the checkpoint using validation evidence only;
- state the expected test behavior and tolerance;
- record the final claim before seeing test evidence.

### Gate 5 - Authorized test access

Access test evidence once. Report it without starting another selection loop. If test evidence conflicts with validation, narrow the claim and propose a future investigation; do not tune against the test set.

## Deliverables

Submit one team package:

1. completed evidence board;
2. baseline and intervention records;
3. one aligned quality/generalization comparison;
4. one class/slice or error-analysis comparison;
5. one resource comparison;
6. explicit test-authorization record;
7. calibrated conclusion, alternative, and next experiment;
8. five-minute defense.

The team package ends with the defense. It does not include any learner's `CHECK-D4-04` or an `individual_transfer` field.

A sound negative result is complete when it resolves or narrows the hypothesis, preserves controls, and supports a useful next action.

## Five-Minute Defense

The shared 20-minute block supports four sequential defenses. Larger cohorts use the preassigned parallel panel or timed-recording route. Every route receives the same five minutes, rubric, and skeptical question; every learner completes the same separate individual check afterward.

Use at most one minute per section.

1. **Baseline:** What was wrong or uncertain?
2. **Evidence:** What supports and threatens the diagnosis?
3. **Experiment:** What single factor changed, and what did you predict?
4. **Result:** What happened to quality, generalization, slices, and resources?
5. **Decision:** Why, what is the claim boundary, and what comes next?

Prepare for these questions:

- What evidence would make your diagnosis wrong?
- Why was this experiment more informative than another option?
- Did the result improve the model, improve the diagnosis, or both?
- Which test decision was fixed before test access?
- Which resource measurement is least transferable to another environment?
- What would you try next with one additional hour?

## Useful Failure and Recovery

If training fails technically:

1. preserve the prediction and record;
2. attempt one bounded repair using the first failed invariant;
3. stop when the recovery budget is reached;
4. use the supplied cached output for your exact case/configuration;
5. mark it as cached evidence;
6. continue comparison, interpretation, and defense.

Cached evidence does not erase the technical failure, but a technical failure does not need to erase the reasoning evidence.

## Final Integrity Check

Before submitting, verify:

- [ ] Case appears only as `A`, `B`, or `C`.
- [ ] No test evidence influenced the intervention or checkpoint decision.
- [ ] One major factor changed.
- [ ] A rejection observation was written before the run.
- [ ] Negative or null results were preserved.
- [ ] Metrics include definitions, averaging, and threshold where relevant.
- [ ] Runtime/size claims include the environment and method.
- [ ] The conclusion is bounded to the evidence.
- [ ] The next experiment tests remaining uncertainty rather than repeating random tuning.

Open [capstone-starter.ipynb](capstone-starter.ipynb) when the Day 4 briefing reaches `LESSON-D4-08`. Review [capstone-rubric.md](capstone-rubric.md) before spending the primary run.

# Day 4 Student Guide: Think Like an ML Engineer

**Big question:** The model trained successfully, but is it actually good, and what should improve next?  
**Outcome:** Complete and defend a constrained model investigation using consequences, slices, controlled experiments, reproducible records, and resource evidence.

> **Day 4 rule:** A score is not a decision. Name the consequence, evidence, alternative, and next discriminating check.

## Learning Outcomes

By the end of Day 4, you can:

- `OBJ-D4-01`: select metrics and thresholds from error consequences;
- `OBJ-D4-02`: distinguish high bias, high variance, healthy training, and optimization failure;
- `OBJ-D4-03`: turn errors into quantified slices and a prioritized work queue;
- `OBJ-D4-04`: design one falsifiable, high-information experiment;
- `OBJ-D4-05`: make an experiment record usable by another engineer;
- `OBJ-D4-06`: compare quality with latency, throughput, memory, and size;
- `OBJ-D4-07`: transfer the evidence loop to representative frontier problem categories;
- `OBJ-D4-08`: improve or meaningfully diagnose a model and defend the evidence chain.

## Exact Day Plan

| Time | Min | Mode and IDs |
|---|---:|---|
| 09:00-09:15 | 15 | Retrieve Day 3 evidence; `LESSON-D4-01` baseline |
| 09:15-09:35 | 20 | `ACT-D4-01`: cost, confusion matrix, thresholds, PR/ROC overview |
| 09:35-10:15 | 40 | `LAB-D4-01`: accuracy is not enough |
| 10:15-10:30 | 15 | Protected break |
| 10:30-10:45 | 15 | `LESSON-D4-02`, `ACT-D4-02`: mystery curves |
| 10:45-11:25 | 40 | `LESSON-D4-03`, `LAB-D4-02`: curves and error buckets |
| 11:25-11:35 | 10 | `CHECK-D4-01`, `CHECK-D4-02` |
| 11:35-12:35 | 60 | Protected lunch |
| 12:35-12:55 | 20 | `LESSON-D4-04` through `LESSON-D4-06`, `ACT-D4-03` |
| 12:55-13:45 | 50 | `LAB-D4-03`: one experiment, tracked and benchmarked |
| 13:45-14:00 | 15 | Protected break |
| 14:00-14:15 | 15 | `LESSON-D4-07`, `ACT-D4-04`: seven representative categories |
| 14:15-15:50 | 95 | `LESSON-D4-08`, `LAB-D4-04`: capstone investigation |
| 15:50-16:10 | 20 | Team five-minute defenses |
| 16:10-16:20 | 10 | `CHECK-D4-03`, `CHECK-D4-04`; individual transfer |
| 16:20-16:30 | 10 | Protected recovery and close |

Total: `450` elapsed minutes.

---

## Opening Retrieval: Do Not Improve the Story Yet

Open your original Day 3 live responses and appended consolidation in the cohort **Day 3 Checks** thread. Keep the original state visible.

Use this four-column chain from `CHECK-D3-04`:

| Claim | Evidence | Limitation or alternative | Highest-information next experiment |
|---|---|---|---|
|  |  |  |  |

Three anonymized consolidation chains will be shown:

1. a chain with a bounded claim and discriminating next experiment;
2. a chain whose limitation is too weak to threaten the claim;
3. a chain whose next experiment changes too many things.

### Retrieval decision

For each chain, mark the first link that fails. Then revise only the matching link in your own chain.

**Bridge question:** If two teams report the same validation accuracy, what evidence could still make one result much stronger?

---

# LESSON-D4-01 - Evaluation Begins with Consequences

**Objective:** `OBJ-D4-01`  
**Learning outcome:** Given an imbalanced binary task and asymmetric costs, choose a baseline, metric set, and threshold direction.

## Why this matters

A routing system can be 97% accurate by sending every rare urgent item down the ordinary route. The arithmetic is correct; the evaluation is useless for the decision.

Start with four questions:

1. What is the decision?
2. Which class is positive?
3. Who experiences each error?
4. What comparison or threshold would change the action?

Only then choose metrics.

## Confusion matrix as a consequence map

Under the course convention, rows are true labels and columns are predicted labels:

|  | Predicted negative | Predicted positive |
|---|---:|---:|
| Actual negative | true negative (`TN`) | false positive (`FP`) |
| Actual positive | false negative (`FN`) | true positive (`TP`) |

Accuracy answers "what fraction was classified correctly?"

$$
\text{accuracy}=\frac{TP+TN}{TP+TN+FP+FN}
$$

Precision asks how often a positive prediction is correct. Recall asks how many actual positives were found.

$$
\text{precision}=\frac{TP}{TP+FP},\qquad
\text{recall}=\frac{TP}{TP+FN}
$$

F1 balances precision and recall equally through their harmonic mean:

$$
F_1=2\frac{\text{precision}\cdot\text{recall}}{\text{precision}+\text{recall}}
$$

That equal balance is a mathematical choice, not a universal consequence model.

### Zero-division is evidence

A model that never predicts the positive class can make precision undefined. Current scikit-learn metric APIs expose `zero_division`; code should set the policy explicitly so warnings do not hide the model behavior. Report the zero-positive-prediction condition, not only the substituted number.

## Moving a threshold

For a binary score $s(x)$ and threshold $t$:

$$
\hat{y}=\mathbb{1}[s(x)\ge t]
$$

Lowering $t$ usually predicts more positives: recall can rise while false positives can also rise. Raising $t$ usually does the reverse. The score ordering and model parameters do not change.

A simple consequence model is:

$$
\text{cost}(t)=C_{FP}FP(t)+C_{FN}FN(t)
$$

This makes assumptions visible. Real consequences may be delayed, uncertain, or unevenly distributed, so do not mistake one classroom cost table for a complete policy.

## PR and ROC: overview, not an operating answer

A precision-recall curve shows how precision and recall move over thresholds and is often informative when positives are rare. An ROC curve compares true-positive rate with false-positive rate across thresholds. ROC AUC summarizes ranking over many thresholds. **AUC does not choose a deployment threshold**; consequences and constraints still determine the operating point.

### Prediction before the visual

A model currently misses too many costly positives. Predict the direction of threshold movement, one likely benefit, and one likely harm.

### Activity launch

Open [ACT-D4-01: Cost Council](../challenges/day-4-challenges.md#act-d4-01---cost-council). Commit before the threshold moves.

## LAB-D4-01 Launch - Accuracy Is Not Enough

**Objectives:** `OBJ-D4-01`  
**Prerequisites:** `LESSON-D4-01`, `ACT-D4-01`, Day 3 split validity  
**Time:** 40 minutes

Open [LAB-D4-01-accuracy-is-not-enough.ipynb](../labs/LAB-D4-01-accuracy-is-not-enough.ipynb).

Before running:

- name the positive class and costly error;
- predict the majority baseline's minority recall;
- predict how the preferred threshold changes when costs change.

Observe:

- accuracy beside minority recall and F1;
- the confusion matrix orientation;
- threshold, precision, recall, and cost moving together;
- whether the threshold `0.5` is supported by the scenario rather than habit.

## LAB-D4-01 Debrief - What Changed, and What Did Not?

1. Which evaluation rule made the majority baseline look acceptable?
2. When the threshold moved, which counts changed? Which model properties did not?
3. Which metric supports model comparison, and which decision still needs the cost model?
4. What assumption in the cost table would you challenge first?

**Misconception:** "F1 is the best metric for imbalance."  
**Correction:** Change the relative error cost while holding scores fixed. If the operational recommendation changes, no context-free metric was sufficient.

**Takeaway:** Evaluation begins with the consequence of errors, not a favorite metric.

**Transition:** Metrics show how often errors occur. They do not yet tell us whether the limitation is fit, optimization, data, or a concentrated slice.

---

# LESSON-D4-02 - Read Curves as Competing Hypotheses

**Objective:** `OBJ-D4-02`  
**Learning outcome:** Use train/validation relationships to distinguish fit, generalization, and optimization hypotheses.

## Mental model: practice, audition, and the path taken

- Training behavior shows what happened on examples used to fit parameters.
- Validation behavior estimates transfer to held-out development data.
- The gap matters, but absolute levels and the path through time matter too.

| Visible pattern | Leading hypothesis | Evidence still needed |
|---|---|---|
| train and validation both weak, smooth plateau | high bias/underfitting | capacity, features, longer training, baseline difficulty |
| train strong, validation weaker and gap widens | high variance/overfitting | split validity, data volume, slice behavior |
| loss oscillates/diverges or metrics jump | optimization failure | learning rate, gradients, normalization, implementation invariants |
| both improve and stabilize with modest gap | healthy relative to current evidence | slice, cost, shift, and test evidence |

These labels simplify interacting causes. A curve diagnosis should be written as "consistent with," not "proves."

### Predict before labels

For each mystery card, cite two visible observations, name one competing explanation, and request one evidence reveal.

Open [ACT-D4-02: Mystery Curves](../challenges/day-4-challenges.md#act-d4-02---mystery-curves).

**Misconception:** "High validation error means overfitting."  
**Correction:** First ask whether training error is low. Weak performance on both sets points elsewhere; unstable curves may point to optimization rather than capacity.

**Transition:** Curves narrow the family of explanations. Error examples and slices show where the model's work queue actually is.

---

# LESSON-D4-03 - Error Analysis Turns an Average into a Work Queue

**Objective:** `OBJ-D4-03`  
**Learning outcome:** Define quantified error buckets and choose an intervention from prevalence, consequence, and likely fixability.

## The error funnel

Move from broad to actionable evidence:

> all validation examples -> all errors -> confusion pairs -> confidence bands -> metadata slices -> inspected examples -> proposed intervention

A slice is a declared subset evaluated consistently, such as low-contrast images, one class pair, or examples from a collection source. A bucket is an error category used for accounting and diagnosis. Buckets may overlap, but the overlap policy must be explicit.

## Worked prioritization example

| Bucket | Error count | Cost per error | Estimated addressable share | Expected value proxy |
|---|---:|---:|---:|---:|
| faint routing digits | 24 | 3 | 0.50 | 36 |
| `3` confused with `8` | 31 | 1 | 0.60 | 18.6 |
| suspected label issue | 8 | 8 | 0.75 | 48 |

The largest bucket is not automatically first. The table is a prioritization hypothesis, not proof of causality.

## Error-analysis protocol

1. Freeze the evaluation set and baseline.
2. Quantify the aggregate and per-class behavior.
3. Inspect confusion pairs and high-confidence errors.
4. Define slices before comparing many interventions.
5. Count prevalence and consequence.
6. Name plausible causes and alternatives.
7. Choose an intervention and a rejection result.

### Discussion checkpoint

A model has many `3 -> 8` errors. Give one data hypothesis, one representation hypothesis, and one label-quality hypothesis that fit the same observation. What evidence separates them?

## LAB-D4-02 Launch - Model Detective

**Objectives:** `OBJ-D4-02`, `OBJ-D4-03`  
**Prerequisites:** `LESSON-D4-02`, `LESSON-D4-03`, `ACT-D4-02`  
**Time:** 40 minutes

Open [LAB-D4-02-model-detective.ipynb](../labs/LAB-D4-02-model-detective.ipynb).

Before revealing configurations:

- diagnose every curve from at least two observations;
- record one alternative and requested evidence;
- predict whether the largest confusion pair will also be the highest-value bucket.

During the investigation:

- preserve aggregate, per-class, confidence, and slice levels;
- do not let a gallery of selected images replace counts;
- distinguish suspected label ambiguity from model failure;
- propose one next experiment and one result that would reject its mechanism.

## LAB-D4-02 Debrief - From Symptom to Priority

1. Which local evidence changed the curve-only diagnosis?
2. Which bucket was frequent? Which was costly? Which appeared fixable?
3. What alternative remains after the inspection?
4. What single experiment best separates the leading explanations?

**Misconception:** "Fix the largest bucket first."  
**Correction:** Compare prevalence, consequence, addressable share, and spillover. Count alone does not establish expected value.

Complete [CHECK-D4-01 and CHECK-D4-02](../assessments/day-4-checks.md) before lunch.

Submit each marked five-minute live minimum in its scheduled window. Append any marked consolidation in the same **Day 4 Checks** thread by 16:30; do not overwrite the live response.

**Takeaway:** Aggregate metrics say how often; slices show where to investigate.

---

# LESSON-D4-04 - One Experiment Should Teach One Clear Thing

**Objective:** `OBJ-D4-04`  
**Learning outcome:** Write a falsifiable hypothesis, one major change, expected evidence, rejection evidence, and a stop rule.

A useful experiment record begins before compute:

> baseline evidence -> hypothesis -> one major change -> expected observation -> rejection observation -> stop rule

## Worked comparison

Weak:

> Make the network wider, switch optimizer, add weight decay, and train longer. See whether accuracy improves.

Stronger:

> Because train and validation scores are both low and stable, increasing hidden width from 32 to 64 should improve both by at least 0.01 without widening the gap beyond 0.02. If train behavior is unchanged, reject insufficient width as the leading limitation. Keep split, seed policy, optimizer, epochs, and evaluation fixed.

The stronger experiment can produce a useful negative result.

**Course attribution boundary:** The one-major-change rule is this course's discipline for making one constrained run interpretable. It is not a universal ban on factorial or sequential experimental design when interactions or staged decisions are the declared object of study.

### Prediction gate

Before every primary run, write:

- what should move;
- what should remain stable;
- what observation would make the hypothesis less likely;
- when you will stop.

**Misconception:** "An experiment succeeds only if the score improves."  
**Correction:** A controlled negative result can remove an explanation and prevent a larger wasted search.

---

# LESSON-D4-05 - Reproducibility Makes Evidence Shareable

**Objective:** `OBJ-D4-05`  
**Learning outcome:** Build a record another engineer can rerun and compare within a stated tolerance.

## Minimum reproducibility record

| Field | Why it matters |
|---|---|
| code/version identifier | identifies the procedure |
| architecture and trainable parameters | identifies model capacity |
| data source, split manifest/hash, transformations | identifies the evidence population |
| seed and every random generator used | supports repeatability |
| package versions and device | bounds environment-dependent behavior |
| optimizer, learning rate, batch, epochs, regularization | identifies training decisions |
| metric definitions, averaging, threshold | identifies evaluation semantics |
| timing method, warm-up, repeats | identifies resource measurement |
| best/final checkpoint rule | identifies which state was evaluated |
| raw results, uncertainty/tolerance, notes | preserves outcome and limitations |

A seed is not a universal replay button. Current PyTorch guidance explicitly does not guarantee complete reproducibility across releases, commits, platforms, or CPU/GPU execution. Deterministic operations can also reduce performance. Make the claim local: "repeatable within this environment and tolerance."

### Record audit

Two runs share a seed but not a split hash. Another pair shares a split hash but one reports only the best validation result after many tries. Which comparison is invalid, and which is biased? Explain separately.

**Takeaway:** Reproducibility is a claim with a boundary, not a checkbox.

---

# LESSON-D4-06 - Quality Lives on a Resource Frontier

**Objective:** `OBJ-D4-06`  
**Learning outcome:** Choose a model for a stated deployment constraint and identify the measurement that could reverse the choice.

## Keep the quantities distinct

- **Latency:** time for one request or batch, with percentile and conditions stated.
- **Throughput:** work completed per unit time under a stated load and batch policy.
- **Memory:** model storage and working memory are different quantities.
- **Model size:** serialized parameter/storage footprint under a stated format.
- **Quality:** task- and slice-specific evidence, not only an aggregate.

A Pareto-efficient option is not dominated on every relevant objective by another measured option. The chosen point still depends on the scenario.

## Timing discipline

Record hardware, software, input shape, batch, threads/device, warm-up, repeats, and summary statistic. Accelerator work can be asynchronous; CUDA timing must synchronize appropriately or use a timing tool that does. A GPU, mixed precision, or larger batch does not guarantee lower end-to-end latency.

Open [ACT-D4-03: Speed-Quality Trade-off](../challenges/day-4-challenges.md#act-d4-03---speed-quality-trade-off).

## LAB-D4-03 Launch - You Get One Experiment

**Objectives:** `OBJ-D4-04`, `OBJ-D4-05`, `OBJ-D4-06`  
**Prerequisites:** `LESSON-D4-04` through `LESSON-D4-06`, `ACT-D4-03`, `LAB-D4-02`  
**Time:** 50 minutes

Open [LAB-D4-03-one-experiment.ipynb](../labs/LAB-D4-03-one-experiment.ipynb).

Before compute:

- audit the baseline;
- choose exactly one major change;
- write expected quality, curve, and resource effects;
- write rejection evidence and a stop rule.

After compute:

- serialize the record;
- rerun under the supplied repeatability contract;
- compare aligned curves and quality/resource points;
- accept, reject, or narrow the hypothesis;
- name the next experiment without running it.

## LAB-D4-03 Debrief - What Did the Run Buy?

1. Did the intervention isolate the claimed mechanism?
2. Did the repeat fall inside the declared tolerance?
3. Did quality, latency, size, or memory move in a way you did not predict?
4. Was the run useful if the primary metric did not improve?
5. Which uncontrolled environmental factor most limits the resource comparison?

**Misconception:** "Twice as fast means half the cost."  
**Correction:** Cost also depends on utilization, concurrency, hardware, memory, reliability, and fixed overhead. Measure the actual objective.

**Scope boundary:** Mixed-precision implementation, quantization, model parallelism, and distributed optimization are `MOVE`/reference topics. They are not required Day 4 implementation outcomes.

---

# LESSON-D4-07 - Seven Representative Frontier Problem Categories

**Objective:** `OBJ-D4-07`  
**Learning outcome:** Map a new problem to a falsifiable claim, evidence object, regression risk, and next experiment.

These are representative categories described in public technical work. They are not a complete role description and make no claim about any organization's private workflow.

| Category | Better must mean | Evidence object | Common trap |
|---|---|---|---|
| capability improvement | a defined behavior improves | held-out tasks and slices | broad claim from one benchmark |
| evaluation/graders | measurement tracks intended behavior | grader audit and human sample | grader treated as ground truth |
| regression diagnosis | changed behavior is localized and reproduced | version/slice comparison | one symptom assigned one cause |
| training data | composition or quality change helps | provenance and controlled data comparison | contamination or confounding |
| efficiency | quality holds under a resource gain | latency/throughput/memory trace | hardware-free speed claim |
| safety evaluation | rare high-consequence failures are surfaced | category/slice severity evidence | average hides the critical tail |
| internal-behavior analysis | internal pattern supports a bounded description | activation/attribution plus intervention | descriptive pattern called cause |

The same loop applies:

> define better -> design evidence -> predict -> compare -> inspect regressions -> state the limit -> choose the next experiment

Open [ACT-D4-04: Design an Evaluation for Coding](../challenges/day-4-challenges.md#act-d4-04---design-an-evaluation-for-coding).

**Misconception:** "A higher benchmark score means a better model."  
**Correction:** Ask what was measured, whether the grader is valid, which slices regressed, whether contamination is plausible, and how far the claim transfers.

**Scope boundary:** Deep interpretability methods and end-to-end safety systems are `MOVE`/reference. Day 4 practices bounded evaluation and evidence, not complete safety or interpretability programs.

---

# LESSON-D4-08 - Capstone: Defend the Evidence Chain

**Objective:** `OBJ-D4-08` with evidence from `OBJ-D4-01` through `OBJ-D4-07`  
**Learning outcome:** Investigate one anonymous routing-code case and defend a controlled engineering decision.

The capstone uses scikit-learn's small handwritten-digits dataset as a classroom investigation surface. The framing is routing-code digit recognition. It supports fast, visible evidence practice; it does **not** establish production realism, deployment readiness, or frontier-scale validity.

## Your product is a decision trail

A strong evidence board distinguishes:

- facts supplied by the case;
- hypotheses and alternatives;
- predictions made before the run;
- observations from the run;
- interpretation and remaining uncertainty.

More than one diagnosis or intervention can be defensible. The score rewards evidence quality, calibrated claims, and useful negative results.

The team evidence board and defense do not contain `individual_transfer`. Each learner completes `CHECK-D4-04` separately after the defense.

## Capstone launch

1. Read the [Capstone Student Guide](../../capstone/capstone-student-guide.md).
2. Review the [Capstone Rubric](../../capstone/capstone-rubric.md).
3. Open [capstone-starter.ipynb](../../capstone/capstone-starter.ipynb).
4. Work only on your assigned anonymous case `A`, `B`, or `C`.
5. Do not access the test set until the notebook's authorization gate.

**Core budget:** one primary experiment. A second run occurs only if the capstone brief explicitly authorizes it; not spending it can be a strong decision.

## Evidence-board gates

- **Gate 1:** baseline facts and validity audit;
- **Gate 2:** ranked diagnosis, alternative, and disconfirming evidence;
- **Gate 3:** one intervention, prediction, rejection result, and resource budget;
- **Gate 4:** complete experiment record before test access;
- **Gate 5:** authorized test evidence and calibrated defense.

## Five-minute defense

The 20-minute block supports four sequential defenses. If the cohort has more than four teams, use the preassigned parallel panel or timed-recording route. Every route uses the same five-minute limit and rubric, and every learner still submits the individual check.

Answer:

1. What was wrong or uncertain about the baseline?
2. What evidence supports and threatens that diagnosis?
3. What did you change, and why was it the highest-information choice?
4. What happened to quality, generalization, slices, and resources?
5. Why is that result consistent or inconsistent with the mechanism?
6. What would you try next with another hour?

## Capstone debrief

Listen for a team that revised its hypothesis, defended a negative result, or chose not to spend another run. Identify why that can be stronger engineering than an unexplained score increase.

Complete the marked live minima for [CHECK-D4-03 and CHECK-D4-04](../assessments/day-4-checks.md) individually after the defenses. Append any marked consolidation by 16:30 without replacing the live response.

---

## Final Course Takeaways

1. A prediction is a model of what should happen.
2. A metric is useful only relative to a consequence or claim.
3. A curve is evidence for competing hypotheses, not a diagnosis by itself.
4. A slice turns an average into an actionable investigation.
5. A controlled negative result can be an excellent outcome.
6. A reproducible record states its environment and tolerance.
7. A production choice balances quality with resources and risk.
8. A defensible improvement is an evidence chain, not a score delta.

> **Four-day journey:** See it -> predict it -> build it -> train it -> break it -> measure it -> diagnose it -> improve it -> explain it.

## Reference Route: Moved Beyond the Live Path

Use these only after the core evidence loop is secure:

- ROC construction mechanics and derivation;
- mixed-precision implementation details;
- quantization workflows;
- model-parallel and distributed-training implementation;
- deep interpretability methods;
- complete safety engineering systems.

They are important topics, but compressing them into Day 4 would displace the controlled investigation and defense that the objectives require.

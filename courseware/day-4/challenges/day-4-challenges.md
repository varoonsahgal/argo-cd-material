# Day 4 Challenges: Think Like an ML Engineer

These four activities are completed during the timed Day 4 blocks. Commit to a decision before the evidence reveal. A strong response names the consequence or constraint, cites observable evidence, states an alternative, and identifies what would change the decision.

Do not optimize for agreement with another team. Optimize for a claim that can be tested.

---

## ACT-D4-01 - Cost Council

**Objective:** `OBJ-D4-01`  
**Time:** 10 minutes within 09:15-09:35  
**Team evidence:** one operating recommendation plus one revision after the cost change

A fraud-screening model scores 1,000 transactions. Fraud is the positive class.

| Outcome at threshold 0.50 | Count |
|---|---:|
| True negative | 930 |
| False positive | 30 |
| False negative | 12 |
| True positive | 28 |

### Commit before calculating

1. Name the two affected parties and one consequence of each error type.
2. Scenario A assigns a review cost of `$5` to each false positive and a loss of `$250` to each false negative. Which error should dominate the operating decision? Predict whether the threshold should move up, down, or remain unchanged.
3. Choose the minimum metric set needed to monitor the recommendation. Do not answer only "F1."

Use:

$$
\text{precision}=\frac{TP}{TP+FP},\qquad
\text{recall}=\frac{TP}{TP+FN}
$$

$$
\text{scenario cost}=C_{FP}FP+C_{FN}FN
$$

### Evidence reveal

The instructor will move the threshold over the same fixed scores and reveal synchronized confusion counts, precision, recall, and scenario cost.

Record:

- the threshold direction you recommended;
- what changed in the confusion matrix;
- what did **not** change about the underlying model scores;
- whether the evidence supported the recommendation.

### Cost reversal

Scenario B assigns `$80` to a false positive because every blocked legitimate payment triggers manual escalation, and `$100` to a false negative.

Revise or retain the recommendation. Explain why a ranking summary such as ROC AUC does not by itself choose the operating threshold.

### Council record

> **Decision:**  
> **Consequence that controls it:**  
> **Evidence:**  
> **Alternative considered:**  
> **Evidence that would change our decision:**

---

## ACT-D4-02 - Mystery Curves

**Objective:** `OBJ-D4-02`  
**Time:** 7 minutes within 10:30-10:45  
**Team evidence:** four diagnoses, each with two observations and one competing explanation

The instructor will display four unlabeled train/validation curve cards on identical axes. The candidate stories are:

- healthy training;
- underfitting/high bias;
- overfitting/high variance;
- optimization failure.

### Diagnose before the reveal

For every card, complete this table. A label without observations earns no evidence credit.

| Card | Primary diagnosis | Observation 1 | Observation 2 | Competing explanation | Next evidence to request |
|---|---|---|---|---|---|
| A |  |  |  |  |  |
| B |  |  |  |  |  |
| C |  |  |  |  |  |
| D |  |  |  |  |  |

Useful distinctions:

- poor train **and** validation behavior suggests a different limitation from a widening train/validation gap;
- an unstable path suggests a different next action from a smooth plateau;
- curves support hypotheses, but they rarely prove one unique cause.

### Staged reveal

After each configuration clue is revealed:

1. keep or revise the diagnosis;
2. state which observation gained or lost weight;
3. name one intervention that would test the revised hypothesis;
4. state a result that would reject that hypothesis.

### Detective debrief

> The most important distinction was ______ because ______. Curves alone still cannot eliminate ______. The highest-information next check is ______.

---

## ACT-D4-03 - Speed-Quality Trade-off

**Objective:** `OBJ-D4-06`  
**Time:** 8 minutes within 12:35-12:55  
**Team evidence:** one choice per deployment round and one measurement request

All measurements below were collected on the same declared CPU environment with the same input preparation. Quality differences smaller than `0.003` macro-F1 are within the current repeatability tolerance.

| Model | Macro-F1 | Batch-1 median latency | Throughput at batch 64 | Model size | Peak working memory |
|---|---:|---:|---:|---:|---:|
| P | 0.931 | 5.8 ms | 1,900/s | 3.2 MB | 42 MB |
| Q | 0.933 | 10.9 ms | 2,850/s | 8.7 MB | 76 MB |
| R | 0.925 | 3.7 ms | 1,720/s | 1.4 MB | 29 MB |
| S | 0.929 | 8.6 ms | 1,510/s | 6.5 MB | 71 MB |

### Round 1: interactive routing

The service has a strict batch-1 latency target of `6 ms`. Choose a model and identify any dominated option.

### Round 2: nightly processing

The service processes a large queue overnight; throughput matters more than single-request latency. Choose again.

### Round 3: constrained edge device

The model file must remain below `2 MB`, and macro-F1 must remain at least `0.920`. Choose again.

### Defend each choice

> **Constraint:**  
> **Choice:**  
> **Evidence:**  
> **Quality concession, if any:**  
> **Measurement still needed:**

Do not infer cost directly from speed. Do not compare latency and throughput as if they were the same quantity. The classroom table omits tail latency, concurrency, reliability, energy, and integration costs; name which omitted factor is most likely to overturn one choice.

---

## ACT-D4-04 - Design an Evaluation for Coding

**Objective:** `OBJ-D4-07`  
**Time:** 8 minutes within 14:00-14:15  
**Team evidence:** a falsifiable evaluation claim and a response to one adversarial reveal

A model team says:

> "Version N+1 is better at coding than Version N."

Your task is not to propose training. Design the minimum credible evaluation needed to decide whether the claim is supported.

### Define the claim

1. Rewrite "better at coding" as two or three observable behaviors.
2. Define at least three slices that could move differently. Include one slice outside the easiest benchmark cases.
3. State one unacceptable regression even if the aggregate score improves.

### Build the evidence chain

| Evidence component | Your design | Failure it helps detect |
|---|---|---|
| Task set and held-out policy |  |  |
| Executable or rule-based grader |  |  |
| Human review sample and rubric |  |  |
| Slices and uncertainty report |  |  |
| Contamination or memorization check |  |  |
| Regression gate |  |  |

For every automated grader, name one way it could reward the wrong behavior. For every human check, name one source of disagreement or bias.

### Commit

> We would support the claim if ______. We would reject or narrow it if ______. The strongest alternative explanation is ______.

### Adversarial reveal

The instructor will reveal one condition:

- aggregate benchmark score rises while a high-value slice regresses;
- the model learns to exploit the grader;
- examples resembling the test set appear in training data;
- human reviewers disagree systematically on task success.

Revise the claim, evaluation, or release decision. State what evidence would distinguish a real capability improvement from a measurement artifact.

---

## Activity Takeaway

Across all four activities, the transferable loop is:

> consequence or constraint -> claim -> evidence -> alternative -> decision -> next discriminating check

A metric, curve, benchmark, or runtime number becomes useful only when it changes a defensible decision.

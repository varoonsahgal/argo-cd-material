# Day 4 Challenge Solutions

**Instructor only. Do not distribute with participant materials.**

Use these as scoring anchors, not scripts learners must reproduce. Credit alternative decisions when the consequence, evidence, competing explanation, and decision boundary are explicit.

---

## ACT-D4-01 - Cost Council

### Baseline calculations

From `TN=930`, `FP=30`, `FN=12`, `TP=28`:

- accuracy: `(930+28)/1000 = 0.958`;
- precision: `28/(28+30) = 0.483`;
- recall: `28/(28+12) = 0.700`;
- F1: approximately `0.571`;
- Scenario A cost: `30($5)+12($250)=$3,150`;
- Scenario B cost at the current threshold: `30($80)+12($100)=$3,600`.

### Prompt-by-prompt anchor

1. **Parties/consequences:** a false positive can block or delay a legitimate customer and consume review work; a false negative can allow fraud and create financial/customer loss. Accept other bounded stakeholder consequences.
2. **Scenario A:** false negatives dominate because one costs 50 false-positive reviews. Test a lower threshold first, predicting higher recall/fewer false negatives and more false positives/lower precision. Do not promise lower total cost before the sweep.
3. **Metric set:** confusion counts plus minority recall and precision, scenario cost, and the threshold. F1 may supplement but cannot encode the 50:1 cost ratio.
4. **After reveal:** moving the threshold changes decisions/counts, not the trained parameters or score ordering. The recommendation is supported only if measured cost falls under the scenario.
5. **Scenario B:** a higher threshold or less aggressive lowering may now be defensible because false positives are nearly as costly as misses. The exact threshold requires the score sweep; no unique number follows from one confusion matrix.
6. **AUC correction:** ROC AUC summarizes ranking across thresholds. It does not incorporate this cost table or select an operating threshold.

### Acceptable alternatives

- Retaining the threshold is acceptable if the learner requests calibration/uncertainty evidence and refuses to move it from one point alone.
- A precision-recall curve, expected cost table, or constrained-recall formulation can all support the decision.
- Learners may reject the simple additive cost model if they state a replacement decision rule.

### Misconceptions to surface

- `0.958` accuracy means the model is operationally good.
- Lowering the threshold improves the model itself.
- F1 or AUC contains stakeholder costs.
- A single confusion matrix reveals the optimal threshold.

### Scoring: 10 points

| Evidence | Points |
|---|---:|
| Correct costly error and threshold-direction prediction | 3 |
| Benefit and harm named | 2 |
| Metric/count set tied to consequence | 2 |
| Revised recommendation under Scenario B | 2 |
| AUC/threshold distinction | 1 |

---

## ACT-D4-02 - Mystery Curves

The canonical visual maps:

- **A:** healthy training;
- **B:** underfitting/high bias;
- **C:** overfitting/high variance;
- **D:** optimization failure.

### Card anchors

| Card | Supporting observations | Competing explanation | Discriminating evidence/experiment |
|---|---|---|---|
| A | train/validation losses fall and stabilize; gap remains modest | both may still fail a costly slice or shifted data | inspect class/slice evidence and repeat on a valid fixed split |
| B | both train and validation performance remain weak; smooth plateaus | too few epochs, weak features, label noise, or implementation ceiling | increase one capacity/training-duration factor or compare a simple valid baseline |
| C | training continues improving while validation worsens after a best epoch; gap widens | split shift, leakage in train only, or label-quality differences | test one regularization/data intervention and inspect slices/provenance |
| D | loss oscillates or diverges; neither path stabilizes | logging error, corrupt batch, normalization, or implementation defect | reduce learning rate or run an invariant/gradient check while holding other factors fixed |

### Prompt completion

After each configuration reveal, a strong learner states which observation changed weight, revises rather than defends an obsolete guess, proposes one controlled intervention, and names a rejection result. Example for C: "If weight decay is the mechanism, validation should improve or the post-peak rise should weaken while train performance may fall slightly. If the aligned validation path and gap do not improve, reject inadequate regularization as the leading explanation."

### Acceptable alternatives

Curves rarely identify one unique cause. Credit a different primary label when two observations, a real competing explanation, and a discriminating next check cohere. Do not credit "get more data" without predicted evidence.

### Misconceptions

- Any validation error is overfitting.
- A small gap is healthy regardless of absolute performance.
- One curve shape proves one hyperparameter was wrong.
- Revision after new evidence is failure rather than good diagnosis.

### Scoring: 12 points

Award 3 per card: one for label, one for two observations, one for alternative plus discriminating evidence. A plausible noncanonical label can earn all 3.

---

## ACT-D4-03 - Speed-Quality Trade-off

### Dominance

Model P dominates S on every listed measurement: higher macro-F1 and throughput, lower latency, size, and memory. S should not be chosen from this table.

### Round anchors

1. **Interactive routing:** choose P. It meets the `<6 ms` target and has stronger quality than R. R is acceptable only if the learner introduces a tighter memory/size or latency margin requirement.
2. **Nightly processing:** choose Q for listed throughput (`2,850/s`) and near-equal quality. Batch-1 latency is not controlling.
3. **Edge device:** choose R because it is the only model below `2 MB` while macro-F1 remains above `0.920`.

### Missing measurements

Accept scenario-matched requests: p95/p99 latency and concurrency for interactive service; sustained throughput, queue behavior, and failures for nightly work; device-specific memory, energy, startup, and hardware compatibility for edge. Reliability can overturn any choice.

### Qualified claims

The `0.002` P/Q macro-F1 difference is inside the stated `0.003` tolerance, so call their measured quality near-equal. Do not infer that Q is truly better. Speed does not directly imply cost without utilization, hardware price, concurrency, and system overhead.

### Misconceptions

- Highest macro-F1 always wins.
- Lowest batch-1 latency means highest throughput.
- A 2x latency change means a 2x cost change.
- Measurements transfer across hardware and loads without qualification.

### Scoring: 12 points

Award 3 per scenario choice/defense and 3 for dominance plus a measurement that could reverse a decision.

---

## ACT-D4-04 - Design an Evaluation for Coding

### Exemplar observable claim

Version N+1 is better only if it improves held-out executable task completion across declared task families, preserves or improves high-value security/reliability slices, and does not increase brittle hard-coding or regressions under independent review.

### Exemplar design

| Component | Strong design | Failure detected |
|---|---|---|
| Task set/held-out policy | versioned private holdout; repository, language, difficulty, edit, debugging, and long-context slices | overfitting to public tasks or one language |
| Executable grader | clean environment; visible and hidden tests; resource limits; deterministic reruns where feasible | code that fails behavior despite plausible text |
| Human sample | blinded pairwise review using correctness, maintainability, security, and instruction adherence rubric | grader misses or rewards wrong behavior |
| Slices/uncertainty | per-slice effect with counts/intervals and explicit regression limits | aggregate gain hides a harmful slice |
| Contamination check | provenance audit, near-duplicate search, held-out task creation after data cutoff where possible | memorization mistaken for generalization |
| Regression gate | block on predefined high-value slice loss or severe failure even when aggregate rises | "average wins" release logic |

### Grader/human limitations

Automated tests can be incomplete, gameable, flaky, or reward hard-coded output. Human reviewers can disagree on style, miss execution/security defects, and be influenced by presentation. Use disagreement as evidence to inspect, not noise to hide.

### Adversarial reveals

- **Slice regression:** narrow or reject the broad claim; investigate the slice and apply its release gate.
- **Grader exploit:** invalidate the affected score; harden the grader and retest both versions.
- **Contamination:** suspend the generalization claim; use uncontaminated tasks and provenance evidence.
- **Reviewer disagreement:** refine the rubric, calibrate reviewers, quantify agreement, and adjudicate a sample.

### Acceptable alternatives

A learner may choose a narrower evaluation with fewer components if every component has a stated purpose and the claim is narrowed accordingly. Do not require named proprietary tools or claim this is a complete production evaluation system.

### Misconceptions

- Public-test pass rate is identical to coding capability.
- Automated graders are ground truth.
- Human evaluation is automatically superior.
- One aggregate benchmark supports a broad capability claim.

### Scoring: 16 points

Award 4 for observable claim/slices, 6 for evidence-chain design, 3 for grader/human limitations, and 3 for calibrated revision after the reveal.

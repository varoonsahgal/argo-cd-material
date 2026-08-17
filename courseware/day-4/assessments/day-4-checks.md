# Day 4 Checks: Think Like an ML Engineer

Complete every check individually. Team capstone evidence does not replace individual transfer evidence. A metric name, diagnosis label, or intervention without observations, alternatives, and rejection evidence is incomplete.

## Submission and Timing

Use the cohort participant channel labeled **Day 4 Checks**.

- **11:25-11:30:** submit `CHECK-D4-01`.
- **11:30-11:35:** submit `CHECK-D4-02`.
- **16:10-16:15:** submit `CHECK-D4-03`.
- **16:15-16:20:** submit `CHECK-D4-04`.
- Submit the marked **five-minute live minimum** during each window. Compact bullets and fragments are acceptable when the evidence link is explicit.
- Preserve your first response. Append, rather than replace, any revision or marked **end-of-day consolidation** in the same thread.
- **Final Day 4 deadline:** complete marked consolidation by **16:30**. The closing retrieval samples one alternative/rejection pair; it does not create another check.

---

## CHECK-D4-01 - Consequence-Aware Metric Decision

**Objective:** `OBJ-D4-01`  
**Allocation:** 5 minutes

A screening model evaluates 10,000 items. Only 100 require urgent review. At threshold `0.50` it produces:

- `TP=62`, `FN=38`, `FP=95`, `TN=9,805`.

Missing an urgent item costs 20 times as much as reviewing an ordinary item.

### Five-minute live minimum

1. State why accuracy alone is unsafe, citing one costly count or rate.
2. Predict the threshold direction you would test first; name one expected benefit and one harm.
3. Correct the ROC-AUC claim and name one consequence-model assumption that could reverse your recommendation.

### End-of-day consolidation - due 16:30

4. Add the minimum metric/count set you would report and one phrase explaining what each contributes.

---

## CHECK-D4-02 - Curve and Slice Diagnosis

**Objectives:** `OBJ-D4-02`, `OBJ-D4-03`  
**Allocation:** 5 minutes

A model's training loss falls smoothly. Training accuracy rises from `0.71` to `0.995`. Validation accuracy peaks at `0.88` in epoch 6 and falls to `0.82` by epoch 20. Validation errors are:

| Slice | Validation examples | Errors | Consequence weight |
|---|---:|---:|---:|
| low contrast | 90 | 24 | 2 |
| ordinary contrast | 510 | 38 | 1 |
| suspected label ambiguity | 20 | 9 | 5 |

### Five-minute live minimum

1. Give a primary curve diagnosis using two observations and name one competing explanation the curves do not eliminate.
2. Choose the first slice to investigate using one normalized or consequence-aware comparison; count alone is insufficient.
3. Propose one intervention or data audit, its expected observation, and a result that would reject its mechanism.

### End-of-day consolidation - due 16:30

4. Add one sentence explaining why a smaller train/validation gap would not by itself prove improvement.

---

## CHECK-D4-03 - Experiment Record and Resource Claim

**Objectives:** `OBJ-D4-04`, `OBJ-D4-05`, `OBJ-D4-06`  
**Allocation:** 5 minutes

A teammate reports:

> "Model B is reproducible and production-ready. I used the same seed twice. It is 1.8x faster and validation macro-F1 rose from 0.912 to 0.916."

The record includes the architecture and seed. It omits split hash, package/device details, threshold, timing warm-up/repeats, model size, and the second run's raw result. Model B changed hidden width, optimizer, and batch size together.

### Five-minute live minimum

1. Identify the two most damaging defects and state the inference each blocks.
2. Rewrite the experiment as one falsifiable major change with expected and rejection evidence.
3. Given the `0.005` macro-F1 tolerance, state the strongest calibrated quality claim the numbers support.

### End-of-day consolidation - due 16:30

4. Add the minimum omitted record fields needed to assess repeatability and the speed claim, plus one deployment constraint under which the faster model could be worse.

---

## CHECK-D4-04 - Individual Frontier Transfer

**Objectives:** `OBJ-D4-07`, `OBJ-D4-08`  
**Allocation:** 5 minutes  
**Individual evidence:** required even if your team completed the capstone defense

A coding model version improves aggregate pass rate from `54%` to `58%`. On security-sensitive tasks it falls from `46%` to `35%`. The executable grader accepts outputs that pass public tests, but a manual sample finds several hard-coded answers. The training-data audit is incomplete.

Submit this five-line live minimum after the team defense. Do not place it in the team evidence board or defense package.

1. **Claim + evidence:** State the bounded improvement, strongest support, and strongest threat.
2. **Alternatives:** Give one measurement explanation and one capability explanation for the aggregate gain.
3. **Decision:** Ship, block, or narrow the release claim; tie the decision to consequences.
4. **Next evaluation:** Choose one highest-information change and state both supporting and rejecting/narrowing results.
5. **Individual transfer:** Name one routing-code investigation habit that transfers and one reason the small digits task does not establish realism here.

---

## Exit Reflection

Complete in one sentence:

> A model result becomes an engineering decision only when ______; the next experiment should ______.

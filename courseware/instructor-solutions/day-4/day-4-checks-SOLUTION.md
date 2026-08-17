# Day 4 Check Solutions

**Instructor only. Do not distribute with participant materials.**

Score reasoning and evidence. Accept alternative decisions that honor the scenario, controls, and claim boundary.

## Response and Collection Contract

- Score the **five-minute live minimum** from the preserved first response.
- Score marked **end-of-day consolidation** from the appended response due at **16:30**; do not reward a rewritten first state.
- Compact fragments are sufficient when they preserve observations, alternatives, and rejection evidence.
- `CHECK-D4-04` is entirely individual and is collected after the defense; no part belongs in the team evidence board, defense, or team rubric.

---

## CHECK-D4-01 - Consequence-Aware Metric Decision

### Model response

1. Accuracy is `(62+9805)/10000 = 0.9867`, but urgent-item recall is `62/(62+38)=0.62`: the model misses 38% of the costly positive class. The large negative class dominates accuracy.
2. Test a lower threshold first. Expected benefit: more true positives/fewer false negatives and higher recall. Expected harm: more false positives, lower precision, and review load. Measure rather than promise a net gain.
3. ROC AUC summarizes ranking across thresholds; it neither encodes the 20:1 cost nor proves `0.50` is an appropriate operating point. A change in miss/review cost, review capacity, probability calibration, delayed outcomes, or unequal harm distribution could reverse the threshold recommendation.
4. Consolidation: report `TP/FN/FP/TN`, urgent recall, precision `62/(62+95) approximately 0.395`, threshold, and consequence-weighted cost. Accuracy can remain as context. F1 is optional, not a substitute for the 20:1 consequence.

### Acceptable alternatives

A learner may decline to recommend a direction without the score distribution, provided they identify lower threshold as the first scenario-consistent candidate and request a threshold sweep. A constrained recall target plus cost among feasible thresholds is valid.

### Misconceptions

High accuracy, AUC chooses threshold, F1 encodes cost, threshold movement retrains the model.

### Scoring: 10 points

Live `8`: `2` accuracy/rare-class issue; `2` threshold benefit/harm; `2` AUC correction; `2` assumption/alternative. Consolidation `2`: metric/count set and contribution.

---

## CHECK-D4-02 - Curve and Slice Diagnosis

### Model response

1. The leading pattern is overfitting/high variance: training reaches `0.995` while validation peaks then falls, and the gap widens after epoch 6 while training loss keeps falling. Alternatives include split/distribution mismatch, label-quality differences, a validation measurement defect, or the low-contrast slice becoming underrepresented in training.
2. Useful comparisons:
   - low contrast error rate: `24/90 = 26.7%`; weighted error total proxy: `24x2=48`;
   - ordinary contrast: `38/510 = 7.45%`; proxy `38`;
   - suspected ambiguity: `9/20 = 45%`; proxy `45`.

   Low contrast has the largest listed weighted total and a strong elevated rate, so a low-contrast data/augmentation audit is defensible. Suspected ambiguity is also defensible because its rate and consequence are highest and a label audit is cheap/high-information. The response must explain which priority rule controls.
3. Example: audit/relabel the 20 ambiguous examples before training changes. If adjudicators agree many labels are wrong and corrected-slice behavior changes under a fixed reevaluation, label quality gains support. If labels are consistent and errors persist, reject label ambiguity as the leading explanation. Or test one training-only contrast augmentation and predict low-contrast slice improvement without ordinary-slice regression.
4. Consolidation: a smaller gap can result from worse training performance while validation remains poor. Absolute validation behavior, slice behavior, and validity must also improve or remain acceptable.

### Acceptable alternatives

Early stopping at the validation minimum, one regularizer, more representative low-contrast data, or a smaller model are acceptable if tied to mechanism and rejection evidence. Credit a different bucket priority using a declared cost/fixability model.

### Misconceptions

Largest count always first; curves prove cause; smaller gap equals better model; selected examples substitute for prevalence.

### Scoring: 12 points

Live `11`: `3` diagnosis/observations; `2` alternative; `3` quantified priority; `3` falsifiable action. Consolidation `1`: gap correction.

---

## CHECK-D4-03 - Experiment Record and Resource Claim

### Model response

1. The three simultaneous changes destroy attribution: any quality/resource movement could arise from width, optimizer, batch, or interaction. The missing split/environment/timing/raw-repeat record blocks repeatability and a controlled speed comparison. Same seed alone is insufficient.
2. Example rewrite: "Holding data/split, seed policy, width, optimizer, epochs, metric, and device fixed, increase batch size from 32 to 64. Predict higher throughput with batch-1 latency no better than tolerance and macro-F1 within `0.005`. Reject the throughput hypothesis if repeated throughput does not improve under the same warm-up/load method."
3. The observed `0.004` macro-F1 increase is inside the `0.005` tolerance. Strongest claim: no distinguishable quality improvement under the current tolerance; the run is consistent with a tie. It is not evidence that B is better.
4. Consolidation: minimum fields include code/config; data/split hash and transformations; all RNG seeds; package/device/thread details; metric averaging and threshold; raw results from both runs; checkpoint rule; input/batch; warm-up, repeats, synchronization where relevant, and summary statistic; and model size for the deployment claim. B could violate model-size/memory limits, tail latency, throughput, reliability, energy, or a high-cost slice despite lower measured median latency.

### Acceptable alternatives

Any one major factor can anchor the rewrite. Learners may state that even "1.8x faster" is unsupported until timing details and raw measurements exist.

### Misconceptions

Same seed proves reproduction; one timer call is a benchmark; within-tolerance gain is improvement; faster means cheaper or production-ready.

### Scoring: 12 points

Live `8`: `3` defects/inference blocks; `3` falsifiable rewrite; `2` calibrated quality claim. Consolidation `4`: `3` missing fields; `1` deployment reversal.

---

## CHECK-D4-04 - Individual Frontier Transfer

### Model response

1. Supported claim: N+1 improves aggregate public-test pass rate under the current grader. Support is the 4-point aggregate rise; threats are the 11-point security-slice fall, hard-coded answers, and incomplete contamination audit. A broad coding-capability improvement is not supported.
2. Measurement explanation: N+1 exploits incomplete public tests or contamination. Capability explanation: it improves common tasks while genuinely regressing security-sensitive behavior.
3. Block the broad release or narrow it to a nondeployment research claim while evidence is repaired. The high-consequence security regression and grader validity failure outweigh the aggregate gain.
4. Highest-information evaluation change: add held-out hidden tests/adversarial cases for both general and security slices, blind the model comparison, and complete provenance checks. Support requires the aggregate gain to persist without hard-coding while security meets the predefined nonregression gate. Reject/narrow if gain disappears, exploits persist, or security remains worse.
5. Transfer habit: preserve baseline, define slices, state alternatives, lock the test policy, or run one discriminating comparison. Digits do not reproduce code generation, grader gaming, data provenance at scale, long-horizon behavior, or deployment consequences.

### Acceptable alternatives

A tightly limited canary is acceptable only with a consequence-aware gate and no exposure to the failed high-risk slice. A learner can choose a human-evaluation redesign first if it directly distinguishes grader exploit from real task completion.

### Misconceptions

Aggregate gain cancels slice loss; executable grader equals truth; manual sample proves all outputs fail; a classroom digits workflow is production-realistic.

### Scoring: 16 points

Live `16`: `3` calibrated claim; `3` supporting/threatening evidence; `3` alternatives; `3` decision/consequence; `3` falsifiable next evaluation; `1` individual transfer/boundary. There is no team or consolidation substitute.

---

## Readiness Interpretation

- **80%+ with rejection evidence:** ready for independent experiment ownership.
- **60-79%:** require one guided evidence-chain revision.
- **Below 60% or test-policy violation:** remediate consequence, split, and falsification concepts before independent model selection.

Do not combine the team capstone score with `CHECK-D4-04`; retain both team collaboration and individual transfer evidence.

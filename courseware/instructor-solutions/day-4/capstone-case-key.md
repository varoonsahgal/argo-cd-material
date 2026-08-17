# LAB-D4-04 Capstone Case Key

**Instructor only. Exclude from participant releases.** This supplements the selector-driven solution notebook; it does not duplicate the executable implementation.

## Shared Decision Contract

- Dataset: scikit-learn digits, framed as routing-code recognition.
- Fixed split: `1078/359/360`, hash `c9a534c56d9b1bb069bc2295d7adf87517e34b69ea9a5b046b79a3b29470b3d9`.
- Primary budget: one major change, one validation decision, one authorized test access.
- Required evidence: aggregate quality, macro-F1, class/slice evidence, train/validation path and gap, model bytes, warmed repeated batch-1 latency, environment, and limitations.
- Claim boundary: this fixed classroom split and environment, not production routing readiness.

## Profile A

**Primary hypothesis:** limited support for classes 8 and 9 in the case training set is harming class-aware performance, especially worst-class recall.

**Secondary hypotheses:** representation weakness, label ambiguity, or a class-specific preprocessing problem.

**Baseline evidence:** validation accuracy about `0.8301`, macro-F1 about `0.8014`, worst-class recall about `0.1714`; class counts reveal reduced support for classes 8 and 9. Aggregate accuracy understates the class consequence.

**Disconfirming checks:** class weighting does not improve worst-class recall by at least `0.05`; aggregate validation accuracy falls by more than `0.02`; weak classes change inconsistently; a label/slice audit explains the failures better than support.

**Strong primary intervention:** `class_weight: False -> True`, keeping architecture, optimizer, learning rate, epochs, batch size, seed, split, and metrics fixed.

**Other acceptable interventions:** balanced sampling, one targeted training-composition change, or a bounded collection plan. Require an overall-regression tolerance. A larger model is weak without representation evidence.

**Expected live result:** validation accuracy about `0.9109`, macro-F1 about `0.9097`, worst-class recall gain about `+0.5429`; authorized test accuracy/macro-F1 about `0.9222/0.9223`. Small platform variation is acceptable when direction, controls, and confusion arithmetic hold.

**Common wrong diagnoses:** "low accuracy means underfitting"; "class weighting proves data imbalance is the sole cause"; "better aggregate accuracy eliminates slice risk."

**Hint ladder:** compare macro-F1 with accuracy; inspect worst recall; request class counts; ask which one loss change tests sensitivity to support without changing capacity.

**Recovery:** fingerprint `df90f16c54f75588b33728ad5d6b7d6f4dd3282a7728cdc7ae269d364d337674`. Recovery supplies validation evidence/resources only. It supplies no cause label, checkpoint, or test metric.

**Scoring anchor:** strong work quantifies class support and worst recall, bounds aggregate regression, presents a real alternative, and states that weighting tests a mechanism rather than proving it.

## Profile B

**Primary hypothesis:** high capacity on a constrained training subset is producing high variance/generalization error.

**Secondary hypotheses:** split shift, duplicate/label issues, or unrepresentative case training data.

**Baseline evidence:** train accuracy `1.0000`, validation accuracy about `0.8802`, macro-F1 about `0.8809`, gap about `0.1198`; the late training/validation path remains separated. The model is `203,304` parameter bytes, materially larger than A/C.

**Disconfirming checks:** regularization does not reduce the gap or improve validation; validation behavior changes by less than tolerance; a split audit shows a stronger distribution explanation; both train and validation are weak, which would argue against pure high variance.

**Strong primary intervention:** `dropout: 0.0 -> 0.5`, with every other major field fixed.

**Other acceptable interventions:** smaller width, one weight-decay value, validation-selected early stopping under a predeclared rule, or more representative training data. Do not combine regularizers in the primary run.

**Expected live result:** validation accuracy about `0.9109`, macro-F1 about `0.9100`, gap reduction about `0.0306`, worst-recall gain about `+0.0571`; authorized test accuracy/macro-F1 about `0.8944/0.8946`.

**Common wrong diagnoses:** "any gap proves overfitting"; "near-perfect training means the model is good"; "dropout improvement proves split shift is impossible."

**Hint ladder:** compare absolute train and validation levels; find where validation stops following training; request curve dynamics; ask which one regularizer changes the generalization mechanism without changing data.

**Recovery:** fingerprint `2398151c14d5b4908ca6e2b5ecb57492b5f7938f24d0129dc88aff447fa849fc`. Recovery remains validation-only and has no test metric.

**Scoring anchor:** strong work uses absolute levels plus gap/path, distinguishes capacity from split shift, measures validation and resource effects, and does not spend the optional run as an unplanned sweep.

## Profile C

**Primary hypothesis:** learning rate `0.20` is too aggressive, producing ineffective or unstable optimization.

**Secondary hypotheses:** insufficient representation/capacity or an implementation/data invariant failure.

**Baseline evidence:** train accuracy about `0.8618`, validation accuracy about `0.7827`, macro-F1 about `0.7676`, worst recall about `0.2286`; loss/accuracy are weak and unstable. Weak training and validation make pure high variance unlikely.

**Disconfirming checks:** one bounded learning-rate correction does not stabilize the path or improve validation by at least `0.05`; invariant checks reveal data/loss errors; a width-only comparison is more explanatory.

**Strong primary intervention:** `learning_rate: 0.20 -> 0.003`, keeping optimizer and architecture fixed.

**Other acceptable interventions:** one optimizer change under the same learning rate contract, or an invariant/normalization repair when evidence supports a defect. Changing learning rate and optimizer together is not acceptable for the primary run.

**Expected live result:** validation accuracy about `0.8969`, macro-F1 about `0.8964`, accuracy gain about `+0.1142`, gap `0.0791 -> 0.0363`, worst-recall gain about `+0.4857`; authorized test accuracy/macro-F1 about `0.8944/0.8951`.

**Common wrong diagnoses:** "weak validation means overfitting"; "more capacity should come before stable optimization"; "a corrected learning rate proves architecture is irrelevant."

**Hint ladder:** compare train and validation absolute levels; inspect oscillation; request curve dynamics; ask whether the path is stable enough to diagnose capacity; authorize one step-size correction.

**Recovery:** fingerprint `d960dd0c81a92c981d54fd5631be1c38460f0c1f11eb86091adaa5b16cffd491`. Recovery remains validation-only and has no test metric.

**Scoring anchor:** strong work distinguishes optimization from bias/variance, predicts stability as well as final quality, checks invariants, and limits the mechanism claim.

## Defense and Rubric Anchors

The team score is exactly:

- Model performance: `25`
- Generalization: `20`
- Experimental design: `20`
- Diagnosis: `15`
- Efficiency: `10`
- Explanation: `10`
- Total: `100`

The individual `CHECK-D4-04` is separate transfer evidence and is not added to the team arithmetic.

A strong defense forms the chain facts -> competing hypotheses -> one predeclared change -> aligned result -> test-locked decision -> calibrated next step. A controlled negative result can score strongly. Apply the public caps for test-driven selection, multiple undeclared changes, missing baseline, absent alternatives, unsupported resource claims, or production claims from digits.

## Recovery and Live-Failure Notes

After one bounded repair, load only the exact fingerprint-matched recovery artifact and label it **CACHED EVIDENCE**. Preserve the original hypothesis and failed invariant. Complete the ledger, comparison, interpretation, and defense. Do not invent a checkpoint or test result. If validation and authorized test disagree on a live path, narrow the claim and stop; never reopen model selection against test evidence.

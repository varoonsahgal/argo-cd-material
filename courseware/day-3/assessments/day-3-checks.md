# Day 3 Checks: Scale It

Complete these checks individually unless the instructor states otherwise. A selected option or intervention without evidence and mechanism does not demonstrate the objective.

## Submission and Collection

Use the cohort participant channel labeled **Day 3 Checks**.

- **12:00-12:10:** complete and submit `CHECK-D3-01` before lunch.
- **16:05-16:20:** spend exactly five minutes on each minimum live response for `CHECK-D3-02` through `CHECK-D3-04`; submit each before moving to the next check.
- Spend five additional minutes total on the clearly marked consolidation additions, due before Day 4 at **09:00**, and append them in the same **Day 3 Checks** thread. Do not replace the live responses.
- Preserve predictions and add revisions without erasing the first state.
- At Day 4 opening, retrieve your original live response and consolidation before discussing sample chains. `CHECK-D3-04` is the readiness gate for consequence-aware evaluation and experiment design.

---

## CHECK-D3-01 - CNN Shape and Feature Evidence

**Objectives:** `OBJ-D3-01`, `OBJ-D3-03`  
**Allocation:** 10 minutes at 12:00

A compact CNN receives Fashion-MNIST batches shaped `(B, 1, 28, 28)` and uses:

1. `Conv2d(1, 8, kernel_size=3, stride=1, padding=1)`;
2. ReLU;
3. `MaxPool2d(kernel_size=2, stride=2)`;
4. `Conv2d(8, 16, kernel_size=3, stride=1, padding=1)`;
5. ReLU;
6. `MaxPool2d(kernel_size=2, stride=2)`;
7. flatten and a dense classification head.

### Part A: shape trace

1. Give the output shape after each convolution and pooling operation.
2. Give the flattened feature count per example.
3. Batch size changes from `32` to `128`. Identify exactly which dimensions and trainable parameter shapes change.
4. Explain how parameter sharing differs from giving every image location an independent detector.

### Part B: interpret without overclaiming

An early map preserves many edges and spatial details. A later map is sparse and responds strongly around the upper outline of several shirts.

1. State one descriptive claim supported by the maps.
2. State one tempting causal or semantic claim the maps do not establish.
3. Propose one input intervention that would test whether the later response depends on that outline.
4. Correct this statement: "The deeper CNN must outperform the shallow CNN because it can represent more features."

---

## CHECK-D3-02 - Repair a Leaked Pipeline

**Objective:** `OBJ-D3-02`  
**Allocation:** 5 minutes in the final block

A team predicts whether a support case will be escalated. It reports validation AUC `0.996` after this process:

1. create `resolution_code` when each case closes;
2. standardize all numeric rows together;
3. split the standardized rows into training, validation, and test sets;
4. train several models and choose the highest validation AUC.

At deployment, predictions are needed when a case opens.

### Minimum live response - submit after five minutes

1. Identify two independent leakage paths or validity violations.
2. Write a valid feature/split/preprocessing/model-selection/test order.
3. The repaired validation AUC falls to `0.83`. Explain why this can be an evidence improvement.

### Consolidation addition - concise, not a second full response

4. In one sentence, explain why stratification and shuffling do not repair either identified problem, then name one remaining validity question.

---

## CHECK-D3-03 - Diagnose and Rescue Generalization

**Objectives:** `OBJ-D3-04`, `OBJ-D3-05`  
**Allocation:** 5 minutes in the final block

A high-capacity image model is trained on `320` labeled examples. At epoch 4, train accuracy is `0.86` and validation accuracy is `0.75`. At epoch 20, train accuracy is `0.995` and validation accuracy is `0.69`. Training loss falls throughout; validation loss reaches its minimum at epoch 5 and then rises.

### Minimum live response - submit after five minutes

1. Diagnose the primary pattern and cite two observations.
2. Choose exactly one first intervention from: weight decay, dropout, early stopping, augmentation, smaller architecture, or more training examples.
3. State the mechanism you expect, one confirming observation, and one rejecting observation.

### Consolidation addition - concise, not a second full response

4. Name one competing explanation that curves alone do not eliminate, then explain why a smaller gap is insufficient without absolute train and validation behavior.

---

## CHECK-D3-04 - Transfer, Attention, and Scale Decision

**Objectives:** `OBJ-D3-06`, `OBJ-D3-07`, `OBJ-D3-08`  
**Allocation:** 5 minutes live plus part of the shared 5-minute consolidation before Day 4 at 09:00

### Minimum live response - submit after five minutes

#### Part A: choose a transfer strategy

A team has `2,000` labeled natural-color images from a domain moderately similar to common consumer photographs, one CPU workstation, a cached MobileNet V3 Small weight file, and 45 minutes to establish a baseline.

Choose one starting strategy: train a CNN from scratch, use a frozen pretrained backbone with a new head, or fine-tune the full pretrained model.

1. Defend the choice using data volume, domain match, trainable parameters, and time.
2. State one comparison needed before claiming pretraining caused an advantage.

#### Part B: correct two claims

1. "The token with the largest attention weight caused the final prediction." Correct the claim and name one omitted route or factor.
2. "Moving the model to a GPU guarantees high utilization and lower latency." Correct the claim and name two measurements needed.

### Consolidation additions - concise, not a second full response

1. Name one result that would make you switch transfer strategy and one reason the training winner could be the wrong serving choice.
2. Add a second omitted route or factor to the attention correction.
3. Complete the Day 4 bridge:

Choose one Day 3 result: leak repair, CNN feature-map interpretation, overfit rescue, or transfer race. Write:

> Claim: __________  
> Evidence: __________  
> Limitation or competing explanation: __________  
> Highest-information next experiment: __________

### Exit reflection

Complete in one sentence:

> A stronger architecture cannot rescue __________; a trustworthy improvement requires __________.
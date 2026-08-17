# Day 3 Check Solutions: Scale It

**Instructor only. Do not distribute with participant materials.**

This key answers every item, accepts defensible alternatives, and provides scoring, misconception, and remediation guidance. Assess reasoning and evidence rather than wording similarity.

---

## CHECK-D3-01 - CNN Shape and Feature Evidence

### Part A answers

| Stage | Shape |
|---|---|
| input | `(B, 1, 28, 28)` |
| first convolution | `(B, 8, 28, 28)` |
| first pool | `(B, 8, 14, 14)` |
| second convolution | `(B, 16, 14, 14)` |
| second pool | `(B, 16, 7, 7)` |
| flatten | `(B, 784)` |

The flattened feature count is `16 * 7 * 7 = 784` per example.

When `B` changes from `32` to `128`, only the first dimension of example-carrying activations/outputs and targets changes. Convolutional kernels, biases, and dense-head trainable shapes do not change.

Parameter sharing uses the same kernel weights at every spatial location. Independent local detectors would store separate weights per location, greatly increasing parameters and removing the same built-in response rule across positions.

### Part B answers

Supported description: the early map retains responses at many local boundaries, while the later selected channel is sparse and responds near upper-shirt outlines for the inspected examples.

Unsupported overclaim: "this channel is a shirt-outline concept" or "this response caused the class prediction." Selected examples and activations are descriptive, not a causal or exhaustive explanation.

A useful intervention masks, shifts, or alters the upper outline while preserving other content, then measures the channel and output change against control edits. Accept translated/synthetic probes when the learner states the comparison.

Correction: extra depth expands possible representations but can be harder to optimize, overfit limited data, cost more, or fail under invalid data/evaluation. Performance must be measured on valid held-out evidence.

### Scoring: 12 points

| Evidence | Points |
|---|---:|
| Four intermediate shapes | 2 |
| Flatten count | 1 |
| Batch versus parameter dimensions | 2 |
| Parameter sharing mechanism | 2 |
| Descriptive claim | 1 |
| Unsupported claim | 1 |
| Input intervention | 2 |
| Depth correction | 1 |

### Misconceptions and remediation

| Error | Immediate move |
|---|---|
| halves channels during pooling | trace spatial and channel dimensions separately |
| changes kernel shapes with batch size | ask which stored arrays are trainable |
| names a semantic detector as fact | require a controlled input intervention |
| assumes deeper wins | request optimization and validation evidence |

If more than one-third miss the channel/spatial distinction, begin the afternoon with dimension tiles before discussing curves.

---

## CHECK-D3-02 - Repair a Leaked Pipeline

### Timing and evidence disposition

The five-minute live minimum is complete when the learner names both leaks, gives a valid ownership order, and explains why `0.83` is better evidence. Shuffle/stratification limits and one remaining validity question are additional depth appended during the shared five-minute consolidation before Day 4 at 09:00. Score the combined live-plus-consolidation record; never overwrite the first response.

### Answers

Two independent violations are:

1. `resolution_code` is created at closure but prediction occurs at opening, so it is a post-outcome/future proxy unavailable at deployment.
2. Standardizing all rows before splitting lets validation/test values influence fitted preprocessing statistics.

A valid order is:

1. define the prediction-time feature contract and quarantine `resolution_code`;
2. create reproducible training/validation/test splits, stratified when appropriate;
3. fit preprocessing using training only;
4. apply the fixed preprocessing to training, validation, and test;
5. train on training and use validation to compare choices;
6. freeze choices and evaluate the untouched test set once.

Shuffling changes order, and stratification preserves class proportions. Neither removes a future feature nor unlearns full-dataset scaler statistics.

The fall from `0.996` to `0.83` is a validity improvement because the latter measures a deployment-available feature set under a cleaner held-out process. It is less flattering but more decision-relevant.

Remaining questions include duplicate/entity leakage, temporal or distribution shift, label quality, representativeness, imbalance consequences, proxy features, and whether test access remained limited. Any one accurately explained item earns credit.

### Scoring: 10 points

| Evidence | Points |
|---|---:|
| Post-outcome leak - live | 2 |
| Pre-split preprocessing leak - live | 2 |
| Valid order and test isolation - live | 3 |
| Lower honest score interpretation - live | 1 |
| Shuffle/stratification limitation - consolidation | 1 |
| Remaining validity question - consolidation | 1 |

### Acceptable alternatives

- Split before schema-based quarantine is acceptable if no value-driven inspection or fitting uses the forbidden feature and deployment availability is enforced before training.
- A learner may propose nested validation or cross-validation, but it may not replace an untouched final test set under the course contract.

### Misconception routing

| Error | Route |
|---|---|
| calls `0.83` a model regression | compare what information was available at each decision time |
| says stratification fixes it | ask what statistics were already fitted |
| removes only the explicit target | inspect feature creation time |

---

## CHECK-D3-03 - Diagnose and Rescue Generalization

### Timing and evidence disposition

The five-minute live minimum is complete when the learner diagnoses from two observations and defines exactly one intervention with mechanism, confirming evidence, and rejection evidence. One competing explanation and the absolute-behavior gap caveat are concise additions during the shared five-minute consolidation. This preserves the objective evidence while keeping the live task executable.

### Answers

Primary pattern: overfitting/high variance after early useful learning. Evidence: training accuracy rises to `0.995` and training loss continues falling, while validation accuracy declines from `0.75` to `0.69` and validation loss rises after epoch 5. The widening train/validation behavior matters more than one final value.

Curves alone do not eliminate validation distribution shift, label noise, a validation pipeline/mode defect, or instability hidden by the summaries.

Any one listed intervention can earn full credit when its mechanism and evidence match:

- **Early stopping:** preserve the epoch-5 checkpoint; confirm better held-out validation than epoch 20 under the same run; reject if the earlier checkpoint does not improve validation or the curve is invalid.
- **Augmentation:** expose training examples to plausible variations; confirm validation improves or degrades less without invalid validation augmentation; reject if both fit and validation collapse or transforms are label-invalid.
- **More examples:** reduce reliance on idiosyncratic cases; confirm validation improves under the same architecture/budget; reject if added data are mismatched/noisy and the gap persists.
- **Weight decay/dropout/smaller architecture:** constrain effective fit/capacity; confirm validation improves or the late decline weakens while useful accuracy remains; reject if only training collapses and validation does not improve.

A smaller gap is insufficient because both curves could collapse to poor performance. Inspect absolute training and validation metrics/losses, aligned budgets, and the direction of change.

### Scoring: 10 points

| Evidence | Points |
|---|---:|
| Diagnosis plus two observations - live | 3 |
| Exactly one intervention - live | 1 |
| Mechanism - live | 1 |
| Confirming observation - live | 1 |
| Rejecting observation - live | 1 |
| Competing explanation - consolidation | 1 |
| Gap limitation - consolidation | 2 |

### Misconception routing

| Error | Route |
|---|---|
| chooses all remedies | enforce one-intervention attribution |
| trains longer because train loss falls | point to validation-loss minimum |
| calls smaller gap success | show a model with both accuracies near chance |
| says one curve proves root cause | request pipeline/mode or slice evidence |

---

## CHECK-D3-04 - Transfer, Attention, and Scale Decision

### Timing and evidence disposition

The five-minute live minimum requires the constrained transfer choice, the random-frozen causal control, an attention correction with one omitted route, and a GPU correction with two measurements. The switch result, serving caveat, second omitted attention route, and Part C chain are appended during the shared five-minute consolidation before Day 4 at 09:00. At Day 4 opening, retrieve three anonymized chains from **Day 3 Checks** and have learners reopen their own original response before revision.

### Part A answers

Best starting strategy under the stated constraints: a frozen pretrained MobileNet V3 Small backbone with a new task head. The data are limited, the domain has moderate natural-image overlap, pretrained weights are cached, and freezing greatly reduces trainable parameters and optimization time. Full fine-tuning is a later experiment, not the 45-minute baseline. Scratch remains a required comparison before making a causal transfer claim.

Switch strategy if frozen features plateau well below a valid scratch baseline, error evidence suggests severe domain mismatch, or the resource/serving cost is unacceptable. Partial fine-tuning may be a bounded next experiment after a stable frozen baseline; full fine-tuning is not assumed to win.

To attribute advantage to pretraining, compare pretrained/frozen with random/frozen under the same backbone, transforms, split, head, and budget; also compare scratch under a declared fair budget. Freezing alone is not pretraining.

The training winner may have higher inference latency, memory, model size, dependency/caching burden, or worse consequential slices. Deployment optimizes a quality/resource/reliability frontier.

### Current torchvision grounding

As checked against stable official torchvision documentation on 2026-08-16:

```python
from torchvision.models import mobilenet_v3_small, MobileNet_V3_Small_Weights

weights = MobileNet_V3_Small_Weights.DEFAULT
model = mobilenet_v3_small(weights=weights)
preprocess = weights.transforms()
```

`DEFAULT` currently aliases `IMAGENET1K_V1`, but aliases may change across versions. Reproducible recovery artifacts should record the explicit enum identity and include the weight/transform/split contract in cache keys. Do not use deprecated `pretrained=True`.

Official source: [MobileNet V3 Small](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.mobilenet_v3_small.html) and [models and pretrained weights](https://docs.pytorch.org/vision/stable/models.html).

### Part B answers

Attention correction: a large attention weight describes one learned mixture relation at one operation. It does not by itself establish causal responsibility for the final output. Omitted factors include value content, other heads/layers, residual paths, feed-forward transformations, normalization, output head, and alternative attention patterns. One is required live; a second is added in consolidation.

GPU correction: accelerator placement does not guarantee that the workload is compute-bound, batches are large enough, the input pipeline keeps up, transfers are hidden, or kernels are efficiently scheduled. Measure at least two of latency distribution, throughput, utilization/timeline, peak memory, data-loader wait, transfer time, warm-up, concurrency, and end-to-end cost on a declared workload/device.

### Part C scoring guidance

There is no single correct Day 3 result. A strong response separates:

- **claim:** bounded and conditional;
- **evidence:** named split, aligned comparison, visual, invariant, or measured resource;
- **limitation:** a plausible alternative or omitted validity/resource dimension;
- **next experiment:** one change selected to separate alternatives.

Example:

> Claim: frozen pretrained features were the stronger 45-minute baseline on this limited natural-image subset.  
> Evidence: under the same split and head budget, validation improved while trainable parameters fell.  
> Limitation: transforms and source-domain match may explain the result, and inference cost was not compared.  
> Highest-information next experiment: compare pretrained/frozen with random/frozen under the same transform and cache contract.

### Exit reflection

One strong answer is:

> A stronger architecture cannot rescue invalid data or contaminated validation; a trustworthy improvement requires a valid comparison, mechanism-level evidence, and an explicit limitation.

### Scoring: 14 points

| Evidence | Points |
|---|---:|
| Transfer choice uses all four constraints - live | 3 |
| Pretraining comparison - live | 2 |
| Attention correction plus first omitted factor - live | 1 |
| GPU correction plus two measurements - live | 2 |
| Switching result and serving limitation - consolidation | 2 |
| Second omitted attention factor - consolidation | 1 |
| Part C evidence chain - consolidation | 3 |

### Misconception routing

| Error | Route |
|---|---|
| transfer always wins | introduce domain mismatch and random/frozen control |
| frozen means pretrained | compare `weights=None` with pretrained weights |
| largest attention means cause | expose value and residual routes |
| GPU means fast | ask for end-to-end timeline and batch-1 latency |

## Score Summary and Readiness

| Check | Points | Primary decision |
|---|---:|---|
| `CHECK-D3-01` | 12 | CNN shape/mechanism readiness |
| `CHECK-D3-02` | 10 | data-validity readiness |
| `CHECK-D3-03` | 10 | generalization diagnosis readiness |
| `CHECK-D3-04` | 14 | transfer/attention/scale and Day 4 readiness |

Total: 46 points.

Day 4-ready evidence requires the learner to:

1. reject contaminated validation even when its score is higher;
2. trace CNN channel/spatial shapes;
3. diagnose generalization from aligned train/validation evidence;
4. choose one falsifiable intervention;
5. treat transfer as conditional;
6. state that attention is not a complete causal explanation;
7. separate latency, throughput, memory, and utilization claims.

If a learner misses two or more categories, begin Day 4 with a guided claim/evidence/limitation/next-experiment table rather than additional architecture content.

The live allocations and consolidation length remain operational assumptions. An uninterrupted novice rehearsal has not been completed; retain that rehearsal as a nonblocking recommendation and do not claim novice timing validation.
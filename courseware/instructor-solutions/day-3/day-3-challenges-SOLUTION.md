# Day 3 Challenge Solutions: Scale It

**Instructor only. Do not distribute with participant materials.**

Use this key to collect commitments before reveals, accept evidence-backed alternatives, and score explanation quality. Do not display completed responses before the participant gate.

## Collection Contract

| Activity | Required preserved evidence | Collection/retrieval action |
|---|---|---|
| `ACT-D3-01` | original ladder, budget choice, revision, transfer evidence request | collect in opening; retrieve in D3-02 feature-map debrief |
| `ACT-D3-02` | evidence-only accusation, second leak, repair order, transfer response | accept before code reveal; retrieve in `CHECK-D3-02` |
| `ACT-D3-03` | map sketch, arithmetic, shape trace, limitation | collect before reveal; retrieve in D3-02 checkpoint |
| `ACT-D3-04` | token prediction, limitation audit, two resource choices | collect before map reveal; retrieve in `CHECK-D3-04` and Day 4 |

---

## ACT-D3-01 - Feature Ladder Under a Budget

### Strong response

A plausible ladder is:

| Stage | Candidate representation | Evidence wording |
|---|---|---|
| input | raw pixel intensity at one location | this is observed data, not a learned feature |
| early | local light-to-dark transitions | a channel responds near similarly oriented local boundaries across locations |
| middle | repeated textures and corners | responses combine nearby edges into recurring local motifs |
| later | arrangements resembling sleeves, soles, or collars | spatially broader patterns become class-relevant under the trained task |

The placements are not unique. A middle layer can encode an outline; an early layer can respond to texture; a late layer need not have a clean human concept. Full credit requires **can encode** language and an observable response pattern, not a layer-name rule.

Depth can reuse earlier features by composing local detectors into broader patterns. It can hurt because optimization becomes harder, capacity can overfit limited data, runtime limits can leave training incomplete, or the data/evaluation pipeline can be invalid.

### Constraint round

Any choice can earn full credit when the evidence matches the situation:

- **Audit pipeline first:** strongest default when validity is unknown. Expected observation is provenance/split/preprocessing evidence; proceed to architecture only after the evaluation is trustworthy.
- **Add blocks:** defensible when valid evidence suggests insufficient receptive field or hierarchy and the budget can optimize the added depth.
- **Widen:** defensible when existing hierarchy is suitable but channel capacity appears limiting.

Reject the selected route if its predicted evidence does not appear. For example, added blocks that lower train loss but worsen validation weaken a simple capacity-benefit claim.

### Misconception correction

A deeper model may represent functions the shallow model cannot, but actual performance also depends on optimization, data volume/quality, regularization, runtime, and evaluation validity. Representational inclusion is not a performance guarantee.

### Transfer response

- **Optimization:** weak gradient flow or insufficient budget prevents useful early layers from changing.
- **Generalization:** extra capacity fits the training sample but not validation.
- **Data/evaluation:** distribution mismatch or leakage/label problem makes validation misleading.
- **Cheap evidence:** aligned train/validation curves plus per-layer activation/gradient summaries and a split/provenance check. Accept one well-chosen item if it separates the learner's top alternatives.

### Facilitation and misconceptions

| Misconception | Move |
|---|---|
| deeper means more abstract in every layer | ask for an input intervention that tests the proposed role |
| lower training loss proves a better model | request validation and validity evidence |
| a bright map names a human concept | replace "is a sleeve detector" with a descriptive response claim |
| audit is not a model experiment | ask whether any architecture comparison is interpretable before validity is established |

### Scoring: 10 points

| Evidence | Points |
|---|---:|
| Four placements with observable support | 2 |
| Feature reuse explained | 1 |
| Two depth risks from distinct categories | 2 |
| Budget choice tied to confirming/rejecting evidence | 2 |
| "Can encode" revision and misconception correction | 2 |
| Transfer evidence request discriminates alternatives | 1 |

---

## ACT-D3-02 - Leakage Accusation: Chain of Custody

### Gate 1 rationale

Facts include `0.997` validation AUC, similar performance from a linear model, and the availability/creation-time metadata. Plausible explanations include genuine strong signal, post-outcome proxy, preprocessing leakage, duplicate/entity overlap, or an evaluation bug. High AUC alone is not proof.

The cheapest proxy check is to ask whether `case_resolution_code` exists at the prediction decision time, then compare a model with the feature quarantined under the same valid split. If the proxy is primary, performance should fall materially and the feature should show unusually strong association. If the feature was actually available at opening and the score remains under a clean audit, the specific post-outcome hypothesis weakens.

Quarantine `case_resolution_code` first because it is created after the target decision and unavailable at deployment time.

### Gate 2 rationale

Fitting a scaler on all records lets validation/test values influence the learned mean and scale used for training. Applying statistics fitted only on training to validation is allowed: the validation values do not alter the fitted state. Stratification preserves class proportions; it does not reverse information already used before the split.

### Valid order

1. Quarantine features unavailable at prediction time using schema/provenance knowledge.
2. Split records into training, validation, and test sets using a reproducible, appropriate strategy.
3. Fit learned preprocessing on training only.
4. Apply the fixed training-fitted preprocessing to validation and test.
5. Fit models on training and compare development choices on validation.
6. After choices are fixed, evaluate once on the untouched test set.

Accept splitting before dropping the known post-outcome column if the feature is never used to fit or inspect value-driven choices and the learner clearly preserves test isolation. Prefer quarantine first because deployment availability is a schema decision.

### Completion and transfer

The lower score is more useful because it estimates behavior without known contamination. It does not prove representativeness, correct labels, absence of duplicates, absence of all proxy features, deployment stability, or causal validity.

For the medical case, request feature availability time, source system, creation logic, update time, relation to treatment/outcome, entity identity, and whether any statistic was fitted using validation/test. Dropping the explicit target misses post-treatment proxies.

### Facilitation and misconceptions

| Misconception | Move |
|---|---|
| high score proves leakage | ask what clean task could legitimately be easy |
| target removed means leak-free | inspect feature availability time and construction |
| shuffling repairs leakage | ask when the scaler learned its state |
| lower score means regression | compare validity of the evidence-generating process |

Reveal order: metric -> provenance -> transformation ownership -> code. Accept two independent leak paths before exact repair guidance.

### Scoring: 12 points

| Evidence | Points |
|---|---:|
| Facts separated from diagnoses | 1 |
| Two plausible explanations | 1 |
| Proxy check with confirming and weakening evidence | 2 |
| Post-outcome feature quarantined for deployment reason | 1 |
| Pre-split scaler leak explained | 2 |
| Valid six-stage order | 2 |
| Lower honest score and remaining limitation | 2 |
| Transfer provenance fields | 1 |

---

## ACT-D3-03 - Kernel Reveal and Shape Trace

### Completed calculation

With a `5 x 5` input, `3 x 3` kernel, stride `1`, and no padding, the output is `3 x 3`.

The top-left patch is all zeros, so its output is `0`. The full map is:

```text
 0 12 12
 0 12 12
 0 12 12
```

The second and third output columns are positive because the right column of each corresponding patch contains `4` while the left weighted column contains `0`. The same nine kernel values are reused at every location; only the local input patch changes.

Torch-style shape trace:

| Operation | Output shape |
|---|---|
| input | `(B, 1, 28, 28)` |
| conv `1 -> 8`, `k=3`, `s=1`, `p=1` | `(B, 8, 28, 28)` |
| pool `2`, `s=2` | `(B, 8, 14, 14)` |
| conv `8 -> 16`, `k=3`, `s=1`, `p=1` | `(B, 16, 14, 14)` |
| pool `2`, `s=2` | `(B, 16, 7, 7)` |
| flatten | `(B, 784)` |

### Interpretation

The calculation demonstrates local connectivity and shared parameters. It does not prove that a learned channel has the semantic role of this hand-designed edge kernel, that a bright response caused the final class, or that no later/residual path matters.

For the transfer prompt, compare parameter counts and behavior under translated inputs. A shared convolution uses one kernel bank at every location and tends to carry response patterns with translation; independent local weights multiply parameters by position and need not respond similarly after translation.

### Facilitation and misconceptions

| Misconception | Move |
|---|---|
| convolution always flips the kernel in frameworks | state the exercise's cross-correlation convention before arithmetic |
| output channels equal input channels | identify one learned kernel per input/output-channel connection |
| pooling adds trainable parameters | ask which values are stored and learned |
| map brightness is a causal explanation | ask for an intervention that changes the proposed input feature |

Reveal one patch calculation before the full map. Then switch immediately to the batch/channel shape trace.

### Scoring: 10 points

| Evidence | Points |
|---|---:|
| Output shape and top-left value | 1 |
| Full sign/value pattern | 2 |
| Shared-kernel explanation | 1 |
| Four intermediate shapes | 2 |
| Flatten count `784` | 1 |
| Interpretation limitation | 1 |
| Shared versus local transfer evidence | 2 |

---

## ACT-D3-04 - Token Relevance, Missing Paths, and Scale

### Token-map response

For focus token **it**, a plausible ranking is **ball**, **rolling**, then **because/chased**. Accept alternatives that explain grammar or event structure and preserve uncertainty. The map is illustrative, so there is no model-specific correct ranking.

- A **query** represents what the current token is seeking from context.
- A **key** represents how each available token can be matched for relevance.
- A **value** carries content combined according to the resulting weights.

Without positional information, the mechanism has weaker access to token order; sequences with the same tokens in different orders can be harder to distinguish through attention alone.

### Limitation audit

Strong answers name at least three: value vectors, multiple heads, multiple layers, residual connections, feed-forward transformations, output head, normalization, alternative attention patterns, and lack of a causal intervention. A correct completion is:

> Attention weights show how one attention operation distributes mixture weight across available representations, but by themselves they do not establish why the final prediction occurred or which input causally determined it.

### Scale decisions

1. Choose **A** for the strict `50 ms` interactive target because its reported batch-1 latency is `42 ms`; B exceeds the target.
2. Choose **B** for the offline queue if the workload matches the measurement: it stays under `6 GB` and reports much higher throughput with no strict per-item latency target.

Missing evidence could reverse a choice: tail latency, concurrent-load behavior, cost, power, reliability, warm-up, request-size distribution, measurement device/method, score uncertainty or slices, or memory overhead outside the model.

The enduring fundamentals are inputs/token representations, parameters, activations, loss, gradients, optimization, and evaluation. New systems concerns include memory, data movement, communication, throughput, latency, checkpoint/recovery, reliability, and pipeline bottlenecks.

### Facilitation and misconceptions

| Misconception | Move |
|---|---|
| largest weight explains the answer | hide values/residual routes and ask what is missing |
| Q/K/V are literal words | restate them as learned vector roles |
| higher throughput means lower latency | compare A and B directly |
| GPU present means utilized | ask for timeline/profiling and idle-stage evidence |

### Scoring: 12 points

| Evidence | Points |
|---|---:|
| Defensible token ranking and uncertainty | 1 |
| Q/K/V roles | 2 |
| Positional-information consequence | 1 |
| Three omitted routes/facts | 2 |
| Attention limitation sentence | 2 |
| Both resource choices use constraints | 2 |
| Missing measurement | 1 |
| Fundamentals plus scale concerns | 1 |

## Score Summary

| Activity | Points |
|---|---:|
| `ACT-D3-01` | 10 |
| `ACT-D3-02` | 12 |
| `ACT-D3-03` | 10 |
| `ACT-D3-04` | 12 |

Total: 44 points. Use local grading policy for conversion; preserve the pre-reveal commitment and mechanism-level evidence even when activities are formative.
# Day 2 Challenge Solutions: Train It

**Instructor only. Do not distribute with participant materials.**

Use this key to facilitate prediction, reveal evidence in stages, accept defensible alternatives, and score reasoning. Do not display completed responses before the participant commitment is collected.

## Collection Contract

| Activity | Required preserved evidence | Collection/retrieval action |
|---|---|---|
| `ACT-D2-01` | original ranking, accuracy prediction, revised ranking, transfer claim | collect by 09:27; reveal at 09:30; retrieve in `LAB-D2-01` |
| `ACT-D2-02` | three-step sketches, labels, sign table, revised path | collect in 10:40-11:10 block; retrieve before `LAB-D2-02` sign prediction |
| `ACT-D2-03` | three batch columns, invariant, broadcasting diagnosis | collect original by 13:12 and revision by 13:23; retrieve at first `LAB-D2-03` shape checkpoint |
| `ACT-D2-04` | evidence-only gate before code plus final before/after board | collect gate before code and board by 16:00; retrieve in `CHECK-D2-04` and Day 3 |

---

## ACT-D2-01 - Loss Ranking: Same Accuracy, Different Signal

### Completed calculation

Targets are `y = [1, 0, 1, 0]`. For each element, BCE is

$$
-\left[y\log(p)+(1-y)\log(1-p)\right].
$$

| Model | Correct-class probabilities | Accuracy | Approximate mean BCE |
|---|---|---:|---:|
| A | `[0.90, 0.90, 0.80, 0.80]` | `4/4` | `0.164` |
| B | `[0.55, 0.55, 0.60, 0.60]` | `4/4` | `0.554` |
| C | `[0.90, 0.90, 0.49, 0.80]` | `3/4` | `0.287` |
| D | `[0.90, 0.90, 0.01, 0.80]` | `3/4` | `1.260` |

**Ranking, lowest to highest loss:** A, C, B, D.

The useful counterexample is C versus B: C has lower accuracy but lower mean loss because three strong/correct outputs outweigh one slightly wrong output, while B is hesitant on every example. A versus B shows equal accuracy with different loss. C versus D shows equal accuracy with a much stronger penalty for a confidently wrong output.

### Prompt-by-prompt rationale

1. **Ranking:** A < C < B < D. Require reasoning before arithmetic; do not award full credit for an unexplained order.
2. **Accuracy:** A and B are `100%`; C and D are `75%` under `p >= 0.5`.
3. **Best tests of different information:** A versus B is the clean equal-accuracy comparison. C versus D is also useful because accuracy ties while wrong-confidence differs.
4. **What BCE distinguishes:** probability assigned to the target class, including hesitant correct and confident wrong outputs, after thresholded accuracy has discarded that detail.
5. **Least-certain item:** no fixed answer; score honest uncertainty and later evidence-based revision.

### Transfer response

A defensible claim is that the lower-validation-BCE model assigns more probability to the observed target labels on average under this objective. It is not yet justified to claim better calibration, fairness, robustness, deployment value, or performance on consequential slices. Even "better generalization" should be qualified by the validity and representativeness of the validation set.

### Staged-reveal annotation exemplar

- **Thresholded predictions/accuracy:** supports the predicted class decisions; does not yet test the BCE order.
- **One correct-example loss:** supports the claim that stronger target-class probability lowers that example's BCE; does not determine the mean ranking.
- **One incorrect-example loss:** supports the stronger penalty for a confident wrong output; still does not determine every mean.
- **Mean losses:** directly tests the final ranking; revise any order that conflicts with A < C < B < D.

### Acceptable alternatives

- A learner may call sigmoid outputs "probabilities" if they also preserve the course caveat that probability-shaped values are not automatically calibrated.
- Exact decimal values can vary by rounding. Preserve the ordering and mechanism.
- A learner may identify both A/B and C/D as useful comparisons if they state what each isolates.

### Common misconceptions and moves

| Misconception | Facilitation move |
|---|---|
| Lower accuracy must mean higher BCE | Compare C and B one example at a time; aggregate only after the per-example evidence is visible. |
| Accuracy and loss should rank models identically | Hold decisions fixed for A/B and vary distance from the threshold. |
| Confident output is always good | Compare a confident correct output with D's confident wrong output. |
| Lower loss proves deployment superiority | Ask which cost, slice, calibration, and distribution evidence the loss omits. |

### Scoring: 8 points

| Evidence | Points |
|---|---:|
| Original ranking preserved before reveal | 1 |
| All four accuracies correct | 1 |
| Final loss ordering correct | 2 |
| Equal-accuracy comparison explained | 1 |
| Confident-wrong mechanism explained | 1 |
| Revision cites revealed evidence | 1 |
| Transfer claim and limitation both defensible | 1 |

---

## ACT-D2-02 - Learning-Rate Trajectory and Gradient Sign

### Direction and trajectory rationale

At `w = -1`, the gradient is negative. The update subtracts a negative number, so the first step moves `w` to the right, toward the stated minimum at `w = 3`, for a positive learning rate.

Expected reconstruction for $L(w)=(w-3)^2$ uses the distance multiplier $1-2\eta$:

| Rate | Evidence pattern |
|---|---|
| `0.01` | multiplier `0.98`; moves correctly but covers little distance in the fixed budget: crawl |
| `0.10` | multiplier `0.80`; approaches from one side: smooth convergence |
| `0.90` | multiplier `-0.80`; crosses the minimum while distance/loss shrink: oscillatory convergence |
| `1.10` | multiplier `-1.20`; crossings and distance/loss grow: divergence |

Exact first three post-update positions:

| Rate | $w_1$ | $w_2$ | $w_3$ |
|---:|---:|---:|---:|
| `0.01` | `-0.92` | `-0.8416` | `-0.764768` |
| `0.10` | `-0.20` | `0.44` | `0.952` |
| `0.90` | `6.20` | `0.44` | `5.048` |
| `1.10` | `7.80` | `-2.76` | `9.912` |

Crossing the minimum is not sufficient to distinguish convergence from divergence. The discriminating observation is whether distance/loss magnitude contracts or expands over repeated steps.

### Chain-rule sign table

| Upstream | Local | Product sign |
|---:|---:|---:|
| positive | positive | positive |
| positive | negative | negative |
| negative | negative | positive |

### Transfer response

An alternating curve with a falling envelope is consistent with oscillatory convergence, not divergence. Request parameter distance from a reference minimum for the classroom objective, loss-envelope magnitude, update norms, or a longer fixed-budget path. In a real model without a known minimum, use aligned loss/update evidence rather than claiming exact distance.

### Step-by-step revision exemplar

- **After the first step:** update direction tests gradient sign and rate-scaled step size; it cannot establish long-run convergence.
- **After two or three steps:** side crossing supports an oscillation label, while changing distance begins to distinguish contraction from expansion.
- **After the fixed budget:** shrinking distance/loss supports convergence; growing distance/loss supports divergence. A final scalar alone does not reconstruct side crossings.

### Acceptable alternatives

- "Right" may be stated as "increase `w`".
- A learner may request the absolute loss trend rather than distance if they explain why it distinguishes growing versus shrinking oscillation.
- A different path sketch is acceptable when it preserves the card's qualitative evidence; exact positions are objective-specific.

### Common misconceptions and moves

| Misconception | Facilitation move |
|---|---|
| Negative gradient means move left | Substitute the sign into `w_next = w - eta * gradient`. |
| Any oscillation is divergence | Freeze axes and compare successive peak distances. |
| One learning-rate number has a universal label | Change the objective's curvature conceptually; ask what evidence would reclassify it. |
| Gradient is the update | Separate sensitivity from multiplication by learning rate and subtraction. |

### Scoring: 8 points

| Evidence | Points |
|---|---:|
| Four pre-reveal path sketches and labels | 2 |
| First-step direction explained from signs | 1 |
| Contracting versus expanding evidence stated | 2 |
| Sign table correct | 1 |
| Revision cites an animation observation | 1 |
| Transfer asks for discriminating evidence | 1 |

---

## ACT-D2-03 - Batch Shape Map

### Completed shape table

Use a two-dimensional batch representation even for one example so all three columns use the same expression.

| Object | One example | Batch of 32 | Batch of 1,024 |
|---|---|---|---|
| `X` | `(1, 4)` | `(32, 4)` | `(1024, 4)` |
| `W1` | `(4, 8)` | `(4, 8)` | `(4, 8)` |
| `b1` | `(8,)` | `(8,)` | `(8,)` |
| `Z1` | `(1, 8)` | `(32, 8)` | `(1024, 8)` |
| `A1` | `(1, 8)` | `(32, 8)` | `(1024, 8)` |

Accept `x` shape `(4,)` and resulting `z/a` shape `(8,)` for a truly unbatched one-example expression only if the learner explicitly distinguishes it from the batch-first `X` convention.

### Prompt answers

1. The `4` feature dimension contracts in `X @ W1`.
2. The first dimension of `X`, `Z1`, and `A1` carries examples.
3. No trainable shape changes with batch size.
4. Broadcasting reuses one `(8,)` bias vector across example rows.
5. A loop equivalent is `Z1 = X @ W1 + b1`; applying `ReLU` yields `A1`.

The function per example remains the same. Example-carrying storage/work grows with `B`. Matrix/tensor kernels expose structured parallel work, but memory, device overhead, and optimization effects prevent a universal "larger batch is better" claim.

### Shape-valid, meaning-wrong answer

`(32, 1)` logits and `(32,)` targets can broadcast to an unintended pairwise `(32, 32)` intermediate in a hand-written elementwise expression. Print and assert exact equality of output/target shapes before elementwise loss, or intentionally reshape targets to `(32, 1)`/logits to `(32,)` under one documented contract. Compare the hand-written per-element result with a same-shape reference on a tiny batch.

PyTorch 2.11 `BCEWithLogitsLoss` documents input and target as the same shape. Course code should assert that contract rather than rely on broadcasting.

### Transfer response

- Invariant: parameter shapes and the per-example function.
- Changes: example-carrying tensor shapes, memory demand, number of batches/updates under a fixed dataset.
- Unsupported without measurement: latency, throughput, speedup, memory advantage, or accelerator utilization.

### Common misconceptions and moves

| Misconception | Facilitation move |
|---|---|
| Batch size appears in parameter count | Change only `B` and ask which stored trainable objects changed. |
| Broadcasting makes copies of parameters | Show one bias object and its aligned view across rows. |
| Vectorized means mathematically different | Compare one row from batch output with a one-example calculation. |
| Largest batch must be fastest/best | Ask for device, memory, data movement, and learning evidence. |

### Scoring: 8 points

| Evidence | Points |
|---|---:|
| All three shape columns correct | 2 |
| Contracted/example dimensions explained | 1 |
| Trainable-shape invariance explained | 1 |
| Broadcasting mechanism explained | 1 |
| Scalar-loop-to-matrix translation correct | 1 |
| Unintended broadcasting diagnosis and check | 1 |
| Transfer answer separates invariant/resource/measurement claim | 1 |

---

## ACT-D2-04 - Broken-Curve Detective

### Facilitation rule

Do not reveal source until the team submits observations, at least two hypotheses, a discriminating check, expected confirming evidence, disconfirming evidence, and a repair category. A correct guess without this gate earns at most half credit.

### Evidence card A

**Leading hypothesis:** missing nonlinear activation or an effectively linear architecture on nonlinear data.

**Alternatives:** unsuitable output/loss pairing, under-capacity architecture, uninformative features/labels, or a low learning rate. Finite nonzero gradients weaken "nothing is updating" but do not eliminate a low effective update.

**Discriminating check:** inspect hidden activation/architecture and compare the learned boundary with a same-shape nonlinear variant under matched data and budget. If missing nonlinearity is primary, the current representation/boundary remains linear; adding the intended nonlinearity should permit a nonlinear region and improve the stalled evidence.

**Do not overclaim:** one stalled curve does not uniquely identify the missing activation.

### Evidence card B

**Leading hypothesis:** omitted gradient reset causes gradients to accumulate across mini-batches.

**Alternative:** excessive learning rate or unstable/invalid inputs can also produce jagged loss and large gradients.

**Discriminating check:** record each parameter's gradient state immediately before reset, immediately after reset, and after `backward()`. Under PyTorch 2.11's documented default, the lab's plain `zero_grad()` leaves gradients `None` after reset and the current backward pass populates participating gradients. Compare this with a lower-learning-rate run only after verifying reset behavior.

**Expected repair:** restore the lab's `optimizer.zero_grad()` call before the current forward/backward sequence, then preserve the documented order. Under matched conditions, gradient norms should no longer show systematic batch-to-batch accumulation, and loss should become more stable if accumulation was primary.

### Evidence card C

**Leading hypothesis:** validation occurs while the module remains in training mode, so a mode-sensitive module such as dropout or batch normalization behaves differently.

**Alternatives:** stochastic data transforms, mutable input ordering/augmentation, state mutation elsewhere, or nondeterministic operations.

**Discriminating check:** record `model.training`, repeat a fixed validation batch, switch with `model.eval()`, and repeat under the same input. Independently record whether grad mode is enabled. `model.eval()` and no-grad/inference context answer different questions.

**Expected repair:** use `model.eval()` for validation and the lab's explicit `torch.inference_mode()` context, then call `model.train()` before resuming training. Evaluation mode changes only modules with mode-specific behavior; inference mode disables autograd recording. A `torch.no_grad()` block is also valid when outputs must later participate in grad-recorded computation.

### Final evidence board exemplar

| Field | Example for card B |
|---|---|
| Symptom | loss spikes; gradient norms grow across batches |
| Competing hypotheses | gradient accumulation; excessive learning rate |
| Discriminating check | inspect gradient state around reset/backward before changing rate |
| Fault found | reset absent from the loop |
| Targeted repair | explicit reset before forward/loss/backward |
| Before/after evidence | matched gradient-norm traces and loss axes |
| Why it worked | each update now uses the current batch gradient rather than an accumulated sum |
| Remaining uncertainty | the learning rate could still be suboptimal; test only if instability remains |

### Reusable transfer protocol

1. Record the symptom with axes, data, seed, and state.
2. Generate multiple mechanism-level hypotheses.
3. Choose the cheapest observation that separates the leading alternatives.
4. Make one targeted repair under matched conditions.
5. Compare before/after evidence and retain a disconfirming criterion.

### Scoring: 12 points

| Evidence | Points |
|---|---:|
| Evidence-only gate submitted before source | 2 |
| Two observations separated from inference | 1 |
| At least two plausible causes | 2 |
| Discriminating check and expected result | 2 |
| Disconfirming result | 1 |
| One targeted repair | 1 |
| Matched before/after evidence | 1 |
| Mechanism explanation | 1 |
| Remaining uncertainty/transfer protocol | 1 |

### Misconception routing

| Misconception | Response |
|---|---|
| One curve shape names one cause | Ask for a competing hypothesis with the same symptom. |
| `backward()` updates parameters | Inspect a parameter before/after backward and after step. |
| `eval()` disables gradients | Inspect `model.training` and `torch.is_grad_enabled()` separately. |
| A new seed is a repair | Keep seed fixed and repair the violated invariant. |
| Best repair is whichever raises accuracy | Require restoration of the predicted mechanism evidence. |

## Day 3 Retrieval Note

Sample one final sentence: "The evidence that most changed my diagnosis was ..." Choose a response that distinguishes implementation/optimization evidence from capacity or data evidence. Do not reopen Day 2 code during the Day 3 retrieval.
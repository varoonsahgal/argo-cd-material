# Day 2 Check Solutions: Train It

**Instructor only. Do not distribute with participant materials.**

This key provides completed responses, acceptable alternatives, scoring anchors, misconception cues, and remediation decisions. Assess reasoning and evidence, not wording similarity.

## Timing and Collection

- `CHECK-D2-01`: 5 minutes; `CHECK-D2-02`: 5 minutes; collect both before lunch.
- Final block: 3-minute `LESSON-D2-08` transfer, 5-minute `CHECK-D2-03`, 5-minute `CHECK-D2-04` live core, and 2-minute collection.
- `CHECK-D2-04` Part C: five-minute consolidation due before Day 3 at 09:00; sample one response at the Day 3 opening.

---

## CHECK-D2-01 - Loop and Loss Contract

### Scenario A answers

1. **Order:** initialize parameters -> forward pass -> scalar loss -> backpropagation/gradients -> parameter update -> repeat with next batch.
2. **Causal rationale:** Accept any one of these adjacent-pair explanations:
   - Parameters must exist before they can produce a forward output.
   - The loss needs the current output and target.
   - Backpropagation differentiates the current loss through the current forward graph/cache.
   - The update needs computed gradients.
   - Repetition uses changed parameters on another batch/iteration.
3. **Inference removes:** scalar training loss when targets are not being used, backpropagation, and parameter update. Initialization/trained-parameter loading and forward computation remain. Evaluation may still calculate loss/metrics with targets while keeping parameters fixed, so accept a learner who distinguishes evaluation from target-free inference.
4. `960 / 64 = 15` update iterations per complete epoch.

### Scenario B answers

1. The code applies sigmoid before a loss that expects logits, producing a double/incorrect contract.
2. Correct flow: `logits = model(X_batch)` followed by `loss = loss_fn(logits, y_batch)`. Sigmoid remains useful afterward when converting logits to probability-shaped values for thresholding, display, or metrics that require them.
3. Keep thresholded classes fixed while changing target-class probabilities: a hesitant correct and strong correct output share accuracy but have different BCE. Lower training loss still omits validation/generalization, data validity, calibration, error consequences, slices, robustness, and resource constraints. Any one correctly explained limitation is sufficient.

### Scoring: 8 points

| Evidence | Points |
|---|---:|
| Six stages in causal order | 2 |
| Adjacent-stage rationale | 1 |
| Training/inference distinction | 1 |
| Iteration count `15` with reasoning | 1 |
| Logit/loss mismatch identified | 1 |
| Sigmoid's repaired role explained | 1 |
| Loss/accuracy difference plus deployment limitation | 1 |

### Common errors and remediation

| Error | Meaning | Immediate move |
|---|---|---|
| Puts update before backward | optimizer/gradient roles conflated | inspect parameter before/after `backward()` and `step()` |
| Calls epoch one update | batching vocabulary weak | tile 960 examples into 15 groups |
| Keeps sigmoid before logits loss | output/loss contract weak | label raw logit and probability-shaped output separately |
| Says lower loss means better model | objective and evaluation conflated | ask which dataset and consequential error the number represents |

---

## CHECK-D2-02 - Learning Rate and Chain-Rule Trace

### Part A answers

1. Run A is oscillatory convergence; Run B is divergence.
2. Both cross the minimum. The discriminating evidence is whether distance/loss envelope shrinks or grows.
3. Reduce the learning rate while holding objective, start, update budget, and other settings fixed. A matched learning-rate comparison is the clean test.
4. If excessive rate is primary, the reduced-rate path should show smaller updates, contracting distance/loss, and fewer or shrinking overshoots. If instability remains unchanged, reject or weaken the hypothesis.

### Part B answers

At `w = 2`:

$$
a=3(2)=6, \qquad q=6-2=4, \qquad L=4^2=16.
$$

Local derivatives:

$$
\frac{\partial L}{\partial q}=2q=8,\qquad
\frac{\partial q}{\partial a}=1,\qquad
\frac{\partial a}{\partial w}=3.
$$

Therefore:

$$
\frac{\partial L}{\partial w}=8\times1\times3=24.
$$

For positive learning rate, `w_next = w - eta * 24`, so a sufficiently small update decreases `w`.

A centered check evaluates the full loss at `w + epsilon` and `w - epsilon`, then calculates

$$
\frac{L(w+\epsilon)-L(w-\epsilon)}{2\epsilon}.
$$

It tests the analytic value near the current point. It is not used as training because perturbing every parameter separately requires many forward evaluations and is sensitive to epsilon/numerical precision.

### Scoring: 8 points

| Evidence | Points |
|---|---:|
| Both path diagnoses correct | 1 |
| Shrinking/growing discriminator explained | 1 |
| Controlled learning-rate test and expected evidence | 1 |
| Forward values `6, 4, 16` | 1 |
| Local derivatives `8, 1, 3` | 1 |
| Combined gradient `24` | 1 |
| Update direction decreases `w` | 1 |
| Centered difference and limitation explained | 1 |

### Acceptable alternatives

- A learner may state an explicit small rate and calculate a new `w`; do not require a number.
- "Loss peaks shrink/grow" can replace parameter distance if axes are fixed and the logic is clear.
- Minor arithmetic slips earn mechanism credit when the chain-rule structure and sign are correct.

### Common errors

- Adds local derivatives rather than multiplying along one path.
- Uses the loss value `16` as the gradient.
- Moves in the positive-gradient direction.
- Claims finite differences prove the model or data are valid.

---

## CHECK-D2-03 - Batch Shape and Scratch-Training Evidence

### Part A answers

| Object | Shape |
|---|---|
| `X` | `(32, 4)` |
| `W1` | `(4, 8)` |
| `b1` | `(8,)` |
| `Z1` | `(32, 8)` |
| `W2` | `(8, 1)` |
| `logits` | `(32, 1)` |

2. `W1 @ X` attempts `(4, 8) @ (32, 4)`, whose inner dimensions do not match. Correct: `Z1 = X @ W1 + b1`.
3. At `B = 128`, `X`, `Z1`, `A1`, `logits`, and targets change first dimension. `W1`, `b1`, `W2`, and `b2` do not.
4. Broadcasting aligns one `(8,)` parameter vector with every row; it does not register row-specific trainable copies.

### Part B answers

1. **Supported, narrowly:** finite decreasing loss supports progress on the declared training objective.
2. **Not supported; needs more evidence:** one fitted linear-looking boundary does not establish what the architecture can represent. The current parameter state or optimization path could make a nonlinear-capable architecture behave linearly.

One cheap discriminating check is to compare the same architecture/data/training setup with the intended hidden nonlinearity versus identity activation, or inspect whether the hidden transformation is actually nonlinear while keeping optimization settings fixed. A gradient check addresses derivative implementation; it does not by itself test representational family.

### Scoring: 8 points

| Evidence | Points |
|---|---:|
| All six requested shapes correct | 2 |
| Orientation repair explained | 1 |
| Batch-size changes correctly isolated | 1 |
| Broadcasting mechanism explained | 1 |
| Two evidence classifications defensible | 2 |
| Discriminating representation/optimization check | 1 |

### Common errors and remediation

| Error | Response |
|---|---|
| Changes parameter shapes with `B` | Ask which arrays are stored trainable state. |
| Calls any decreasing loss proof of correct code | Request a no-nonlinearity boundary and validation evidence. |
| Immediately increases width | Ask whether current hidden operations alter the representational family. |

---

## CHECK-D2-04 - PyTorch Loop and Failure Diagnosis

### Part A answers

1. Observations include: early loss falls then becomes jagged; gradient norms grow across mini-batches; same seed reproduces the pattern; logits/loss pairing is stated as valid.
2. Plausible hypotheses include omitted gradient reset and excessive learning rate. Invalid/extreme input batches or unstable objective implementation are weaker but acceptable alternatives when paired with checks.
3. Inspect gradient state/norm immediately before reset, immediately after reset, and after backward. If reset is absent, gradients retain prior-batch contributions. A controlled lower-rate run can follow, but checking the explicit responsibility is cheaper.
4. The loop never resets gradients before calculating the current batch's gradient.
5. Add the lab's `optimizer.zero_grad()` before forward/loss/backward. Under PyTorch 2.11's documented default (`set_to_none=True`), the next `backward()` populates participating gradients for the current iteration rather than accumulating onto earlier values. Accept an explicit argument when the learner explains the resulting inspectable state.
6. Compare per-batch gradient norms and loss on identical axes/data/seed before and after repair. Expected: no systematic accumulation and more stable loss if omission was primary.

### Part B answers

1. `model.eval()` sets the module and its submodules to evaluation mode; only modules with mode-specific behavior change computation/state handling.
2. No. It does not disable gradient recording.
3. Use:

```python
model.eval()
with torch.inference_mode():
    val_logits = model(X_val)
    val_loss = loss_fn(val_logits, y_val)
```

`torch.inference_mode()` is the linked lab's isolated-evaluation path. `torch.no_grad()` is an acceptable alternative when the learner accurately states that it disables backward graph recording without inference mode's tensor-reuse restrictions.

4. Call `model.train()` before the next training phase/loop.
Facilitator note: explicit transitions document intended state and prevent future architecture changes from silently altering behavior. Do not imply that `eval()` must change outputs for a model with no mode-sensitive modules.

### Part C scoring guidance

There is no single required diagnosis. Strong responses distinguish at least:

- **optimization/gradient flow:** saturation, initialization, depth-related weak early gradients, unsuitable rate;
- **representation:** missing/ineffective nonlinearity or insufficient architecture for the pattern;
- **data/objective:** uninformative or mismatched labels/features, normalization problem, output/loss mismatch;
- **implementation:** detached graph, frozen early layers, incorrect tensor path.

High-information evidence requests include:

- activation distributions and saturation/zero fractions by layer;
- `requires_grad` and `.grad` presence/norm by layer;
- output/loss and target shape/range contract;
- simple-baseline performance and label/data sanity checks;
- same-example forward trace through early layers;
- one controlled initialization/normalization/rate comparison.

The chosen first experiment must match the leading hypothesis. Examples:

- If saturation/weak gradient flow leads: inspect activation distributions first; then test a bounded initialization/activation change with predicted early-gradient recovery.
- If data signal leads: run a simple baseline or tiny overfit test on a small subset before changing architecture.
- If missing nonlinearity leads: compare same shapes with intended activation versus identity.

Disconfirming evidence must be explicit. Immediate optimizer switching or widening is weak because each changes behavior without first separating data, representation, implementation, and optimization causes.

The final comparison sentence should identify a concrete evidence item, not "seeing the code."

### Scoring: 12 points

| Evidence | Points |
|---|---:|
| Part A observations and two plausible hypotheses | 2 |
| Discriminating gradient-reset check | 1 |
| Violated responsibility and repair | 2 |
| Matched before/after evidence | 1 |
| Eval mode semantics correct | 1 |
| Gradient-disabling context correct | 1 |
| Return to train mode | 1 |
| Part C cross-category alternatives and one evidence request | 1 |
| One falsifiable experiment with confirming/rejecting evidence | 1 |
| Comparison sentence cites evidence rather than source reveal | 1 |

### Exit reflection exemplar

The reflection is unscored but must be acknowledged. One strong response is:

> Training is a repeated, evidence-producing parameter-update experiment; trustworthy diagnosis begins with observations, competing hypotheses, and a discriminating check.

Accept alternatives that preserve both ideas. Redirect answers that define training only as "running epochs" or diagnosis only as "reading the code."

### Day 3 readiness decision

Ready evidence:

1. Maps PyTorch calls to reset/forward/loss/backward/update responsibilities.
2. Separates module mode from gradient recording.
3. Generates competing hypotheses from non-unique symptoms.
4. Chooses a discriminating check before a repair.
5. Distinguishes implementation/optimization failure from representational or data limitation.

If a learner misses two or more items, begin Day 3 with a guided evidence table rather than an additional framework lecture.

## Score Summary

| Check | Points | Primary decision |
|---|---:|---|
| `CHECK-D2-01` | 8 | loop/loss contract readiness |
| `CHECK-D2-02` | 8 | optimization/backprop readiness |
| `CHECK-D2-03` | 8 | batch/scratch implementation readiness |
| `CHECK-D2-04` | 12 | framework diagnosis and Day 3 readiness |

Total: 36 points. Use local grading policy for conversion; preserve the mechanism-level readiness decision even if scores are not formally graded.
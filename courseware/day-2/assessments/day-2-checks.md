# Day 2 Checks: Train It

Complete these checks individually unless the instructor states otherwise. Show the evidence behind each decision; an option or code edit without a mechanism does not demonstrate the objective.

## Submission and Collection

Use the cohort's participant submission channel labeled **Day 2 Checks**. If the cohort uses paper, hand the same artifacts to the instructor at the stated collection points.

- **11:55-12:05:** spend 5 minutes on `CHECK-D2-01` and 5 minutes on `CHECK-D2-02`; submit both before lunch.
- **16:05-16:20:** spend 3 minutes on the `LESSON-D2-08` transfer, 5 minutes on `CHECK-D2-03`, 5 minutes on the live core of `CHECK-D2-04`, and 2 minutes submitting both.
- **Before Day 3 at 09:00:** add the marked five-minute transfer item to `CHECK-D2-04`. Bring access to your original `ACT-D2-04` evidence-only diagnosis and final repair; one response will be sampled during the Day 3 opening.

Preserve your initial predictions. Add revisions without erasing the first state.

---

## CHECK-D2-01 - Loop and Loss Contract

**Objectives:** `OBJ-D2-01`, `OBJ-D2-02`  
**Allocation:** 5 minutes. Use concise phrases; the submission channel records automatically at 12:05.

### Scenario A: sequence the mechanism

A mini-batch training loop contains these stages in a shuffled order:

- update parameters;
- calculate a scalar loss;
- initialize parameters;
- run the forward pass;
- calculate gradients by backpropagation;
- repeat with the next batch.

1. Put the stages in a defensible causal order.
2. Choose one adjacent pair and explain why the first is needed before the second.
3. Circle the stages that disappear when the fitted model is used only for inference.
4. A training set has `960` examples and mini-batches of `64`. How many update iterations occur in one complete epoch if every example is used once and there is no partial batch?

### Scenario B: repair the output/loss contract

A binary classifier's final layer produces one value per example. A teammate writes:

```python
probabilities = torch.sigmoid(model(X_batch))
loss = torch.nn.BCEWithLogitsLoss()(probabilities, y_batch)
```

1. Identify the contract mismatch.
2. Write the corrected loss-facing data flow and state where sigmoid remains useful afterward.
3. Explain how two models can have equal accuracy but different BCE loss, then name one reason lower training loss is insufficient deployment evidence.

---

## CHECK-D2-02 - Learning Rate and Chain-Rule Trace

**Objectives:** `OBJ-D2-03`, `OBJ-D2-04`  
**Allocation:** 5 minutes. Use equations and short evidence phrases; the submission channel records automatically at 12:05.

### Part A: diagnose update paths

Two runs start from the same parameter on the same one-dimensional objective.

- **Run A:** the parameter crosses the minimum repeatedly; distance from the minimum shrinks each step; loss falls overall.
- **Run B:** the parameter crosses the minimum repeatedly; distance from the minimum grows each step; loss rises overall.

1. Classify each run as oscillatory convergence or divergence.
2. Explain why "it crosses the minimum" is insufficient, then name one controlled learning-rate test and the expected before/after evidence.

### Part B: trace one gradient path

A tiny graph uses:

$$
a=3w, \qquad q=a-2, \qquad L=q^2
$$

At `w = 2`:

1. Calculate the forward values `a`, `q`, and `L`.
2. Calculate the three local derivatives and combine them into $\partial L/\partial w$.
3. Predict whether a small gradient-descent update increases or decreases `w`.
4. In one phrase, state what a centered finite-difference check would test.

---

## CHECK-D2-03 - Batch Shape and Scratch-Training Evidence

**Objectives:** `OBJ-D2-05`, `OBJ-D2-06`  
**Allocation:** 5 minutes

### Part A: repair the batch computation

A batch-first network uses architecture `4 -> 8 -> 1` with `B = 32`.

1. Give the shapes of `X`, `W1`, `b1`, `Z1`, `W2`, and `logits`.
2. A teammate writes `Z1 = W1 @ X + b1`. Diagnose the orientation error and write the corrected expression.
3. Batch size changes from `32` to `128`. List exactly which shapes change.
4. Explain why bias broadcasting does not create `128` trainable bias vectors.

### Part B: classify the evidence

A NumPy model shows:

- finite loss that decreases from its initial value;
- finite, shape-correct gradients;
- high training accuracy;
- a decision region that remains one linear boundary on nonlinear data;
- low validation accuracy.

For each claim, mark **supported**, **not supported**, or **needs more evidence**, then justify:

1. "The optimizer is making progress on the declared training objective."
2. "This run demonstrates that its current computation represents the required nonlinear boundary."

Choose one cheap check that separates a missing or ineffective nonlinearity from an optimization defect.

---

## CHECK-D2-04 - PyTorch Loop and Failure Diagnosis

**Objectives:** `OBJ-D2-07`, `OBJ-D2-08`  
**Live core:** 5 minutes for Parts A and B  
**Five-minute transfer:** Part C before Day 3 at 09:00

### Part A: diagnose before repairing

A PyTorch binary model emits logits and uses `BCEWithLogitsLoss`. Its early loss falls, then becomes jagged. Parameter gradient norms grow from one mini-batch to the next. The pattern repeats under the same seed.

The loop is:

```python
model.train()

for X_batch, y_batch in train_loader:
    logits = model(X_batch)
    loss = loss_fn(logits, y_batch)
    loss.backward()
    optimizer.step()
```

1. State two observations and two plausible hypotheses.
2. Name the cheapest check that distinguishes omitted gradient reset from an excessive learning rate.
3. Identify the violated responsibility, write one targeted repair, and name one matched before/after measurement.

### Part B: separate evaluation mode from gradient recording

Validation code is:

```python
model.eval()
val_logits = model(X_val)
val_loss = loss_fn(val_logits, y_val)
```

1. State separately what `model.eval()` changes and whether it disables gradient recording.
2. Add a gradient-disabling context and state when `model.train()` should be called again.

### Part C: transfer to a non-unique failure

**Complete before Day 3 at 09:00.** Reopen your original `ACT-D2-04` evidence-only diagnosis before answering.

A deeper model has training and validation accuracy near chance. Loss decreases very slowly. Gradient norms in early layers are close to zero, but output-layer gradients are nonzero. The code has not yet been shown.

1. Rank two plausible explanations from different categories.
2. Request one evidence item that best separates them.
3. Choose one first experiment; state both confirming and rejecting evidence.
4. Add one sentence comparing this reasoning with your original `ACT-D2-04` diagnosis:

> The evidence that most changed my diagnosis was __________ because __________.

### Exit reflection

Complete in one sentence:

> Training is __________; trustworthy diagnosis begins with __________.
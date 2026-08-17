# Day 2 Challenges: Train It

Complete each activity before its reveal. Preserve your first prediction even when you revise it: the difference between the two states is evidence of learning.

## Submission and Retrieval

Use the cohort's participant submission channel labeled **Day 2 Activities**. If the cohort uses paper, keep one dated activity sheet and hand it to the instructor at each collection point.

| Activity | Commit and collect | Retrieve |
|---|---|---|
| `ACT-D2-01` | Commit at 09:20; snapshot collected by 09:27 before the staged reveal begins at 09:30 | Reopen during `LAB-D2-01` when equal-accuracy cases are compared |
| `ACT-D2-02` | Commit during the 10:40-11:10 block before the gradient-path reveal; collect after revision | Reopen during `LAB-D2-02` before predicting one gradient sign |
| `ACT-D2-03` | Collect the original commitment by 13:12 before reveal; collect the revised map at 13:23 | Reopen at the first shape checkpoint in `LAB-D2-03` |
| `ACT-D2-04` | Submit the evidence-only diagnosis before requesting faulty code; collect the repaired evidence board by 16:00 | Reopen during `CHECK-D2-04` and the Day 3 opening retrieval |

Do not replace an original response. Add revisions in a second color or under a clearly labeled **Revision after evidence** heading.

---

## ACT-D2-01 - Loss Ranking: Same Accuracy, Different Signal

**Objectives:** `OBJ-D2-02`, reinforcement of `OBJ-D2-01`  
**Time:** 7 minutes inside `LESSON-D2-02`  
**Format:** individual prediction, pair defense, staged reveal

Four binary classifiers make predictions for targets `y = [1, 0, 1, 0]`. The decision rule is `p >= 0.5 -> class 1`.

| Model | Predicted probabilities for class `1` |
|---|---|
| A | `[0.90, 0.10, 0.80, 0.20]` |
| B | `[0.55, 0.45, 0.60, 0.40]` |
| C | `[0.90, 0.10, 0.49, 0.20]` |
| D | `[0.90, 0.10, 0.01, 0.20]` |

### Commit before calculation

1. Rank the four models from lowest to highest expected binary cross-entropy loss.
2. Record each model's expected accuracy without calculating BCE.
3. Circle the comparison that best tests whether accuracy and loss contain the same information.
4. Write one sentence explaining what BCE can distinguish after thresholded accuracy ties.
5. Mark your least-certain ranking decision.

### Evidence reveal protocol

Request the reveal in this order:

1. thresholded predictions and accuracy;
2. loss for one correctly classified example;
3. loss for one incorrectly classified example;
4. mean loss for each model.

After each reveal, annotate whether the evidence **supports**, **weakens**, or **does not test** your ranking.

### Revision after evidence

- Correct the ranking without erasing the first state.
- Explain why a confident wrong prediction should affect BCE differently from a hesitant wrong prediction.
- Name one reason lower training loss would still be insufficient evidence that a model is better for deployment.

### Transfer prompt

Two models have identical validation accuracy. One has substantially lower validation BCE. What useful claim can you make, and what claim would still be unjustified without additional evidence?

---

## ACT-D2-02 - Learning-Rate Trajectory and Gradient Sign

**Objectives:** `OBJ-D2-03`, bridge to `OBJ-D2-04`  
**Time:** 8 minutes inside the 10:40-11:10 block  
**Format:** sketch, animated reveal, mechanism debrief

Without reopening `LAB-D2-01`, reconstruct the first steps for the same objective:

$$
L(w)=(w-3)^2, \qquad w_0=-1
$$

The four numeric rates are `0.01`, `0.10`, `0.90`, and `1.10`. Their behavior labels remain hidden.

### Commit before animation

For each hidden card:

1. sketch the first three parameter positions on a shared loss curve;
2. classify the expected path as **crawl**, **smooth convergence**, **oscillatory convergence**, or **divergence**;
3. predict whether the first update moves `w` left or right;
4. state which observation would distinguish oscillatory convergence from divergence;
5. mark the path you are least certain about.

Use the update rule as evidence, not as a slogan:

$$
w_{next}=w-\eta\frac{\partial L}{\partial w}
$$

### Reveal and revision

The instructor reveals one step at a time. After every step:

- keep or revise the trajectory label;
- cite distance from the minimum or loss magnitude;
- explain the movement from gradient sign and learning-rate scale.

### Chain-rule bridge

Suppose `w` affects an intermediate value `a`, which affects loss `L`.

$$
\frac{\partial L}{\partial w}
=
\frac{\partial L}{\partial a}
\frac{\partial a}{\partial w}
$$

Before any numbers appear, predict the sign of $\partial L/\partial w$ for each case:

| Upstream gradient $\partial L/\partial a$ | Local derivative $\partial a/\partial w$ | Predicted sign |
|---:|---:|---|
| positive | positive |  |
| positive | negative |  |
| negative | negative |  |

### Transfer prompt

A training curve alternates up and down while its envelope falls. Explain why the curve alone does not justify calling the run divergent. Name one additional observation you would request.

---

## ACT-D2-03 - Batch Shape Map

**Objectives:** `OBJ-D2-05`, preparation for `OBJ-D2-06`  
**Time:** 7 minutes inside `LESSON-D2-04`  
**Format:** team shape map and one semantic diagnosis

A dense layer maps `4` input features to `8` hidden units. Use the course's batch-first, examples-as-rows convention.

### Commit before the matrix reveal

Complete the table without code.

| Object | One example | Batch of 32 | Batch of 1,024 |
|---|---|---|---|
| `X` |  |  |  |
| `W1` |  |  |  |
| `b1` |  |  |  |
| `Z1 = X @ W1 + b1` |  |  |  |
| `A1 = ReLU(Z1)` |  |  |  |

Then answer:

1. Which matrix dimensions contract?
2. Which dimension carries examples?
3. Which trainable shapes change when batch size changes?
4. What does broadcasting reuse rather than duplicate as trainable state?
5. Rewrite a scalar loop over examples as one batched expression.

### Evidence reveal

The instructor reveals dimension tiles for `B = 1`, `32`, and `1,024`. Annotate:

- the function that stayed the same for each example;
- the storage/work that grew with `B`;
- one reason vectorized tensor operations map well to parallel hardware;
- one reason this does **not** imply that the largest possible batch is always best.

### Shape-valid, meaning-wrong challenge

A binary model returns logits with shape `(32, 1)`. Targets have shape `(32,)`, and a hand-written elementwise loss expression runs after implicit broadcasting.

1. Why is "the code ran" insufficient evidence?
2. What shapes should be printed before accepting the result?
3. Name a cheap invariant or comparison that could expose unintended broadcasting. Contrast this with PyTorch 2.11 `BCEWithLogitsLoss`, whose input and target contract requires the same shape.

### Transfer prompt

The same model is evaluated with `B = 1` and `B = 1,024`. Identify one quantity that should remain invariant, one that usually changes, and one performance claim that cannot be made without measurement on a declared device.

---

## ACT-D2-04 - Broken-Curve Detective

**Objectives:** `OBJ-D2-08`, reinforcement of `OBJ-D2-01`, `OBJ-D2-02`, and `OBJ-D2-07`  
**Time:** 10 minutes embedded in `LAB-D2-04`  
**Format:** mystery evidence first, source code second

### Non-negotiable reveal rule

You may not inspect faulty source code until your team submits an evidence-only diagnosis. A curve is not a unique fingerprint, so the required product is a discriminating check, not a confident guess.

### Evidence card A

- training loss falls slightly, then stalls;
- train and validation accuracy remain near the linear baseline;
- gradient norms are finite and nonzero;
- no shape exception occurs.

### Evidence card B

- early loss falls;
- later loss becomes jagged and occasionally spikes;
- parameter gradient norms tend to grow across successive mini-batches;
- restarting with the same seed reproduces the pattern.

### Evidence card C

- training loss decreases normally;
- repeated validation passes produce inconsistent outputs for the same examples;
- the model contains a module whose behavior can differ between training and evaluation modes;
- gradient recording state has not yet been revealed.

### Evidence-only submission gate

Choose one assigned card and submit:

1. two observations from the evidence;
2. at least two plausible causes;
3. the cheapest check that best separates those causes;
4. the result you expect if your leading hypothesis is correct;
5. one result that would make you reject that hypothesis;
6. a repair category, without writing the exact code change.

The instructor may then reveal exactly one requested evidence item: activation summary, gradient-reset trace, mode state, output/loss contract, or relevant source fragment.

### Code-inspection phase

Only after the gate is accepted:

1. inspect the assigned source fragment;
2. identify the violated training-loop or evaluation invariant;
3. make one targeted repair;
4. rerun with the same data, seed, axes, and budget;
5. compare before/after evidence;
6. explain the mechanism of the repair.

### PyTorch mode distinction

For any evaluation-mode diagnosis, answer both questions separately:

- Is the module in training or evaluation mode?
- Is autograd recording the operations in this evaluation block?

Do not treat `model.eval()` as a synonym for `torch.no_grad()` or an inference context.

### Final evidence board

| Field | Team response |
|---|---|
| Symptom |  |
| Competing hypotheses |  |
| Discriminating check |  |
| Fault found |  |
| Targeted repair |  |
| Before/after evidence |  |
| Why the repair worked |  |
| Remaining uncertainty |  |

### Transfer prompt

In a larger training run, chance-level accuracy, flat loss, or unstable gradients could each have several causes. Write a reusable five-step diagnostic protocol that begins with evidence and ends with a falsifiable next check.

---

## End-of-Day Retrieval

During `CHECK-D2-04`, reopen your `ACT-D2-04` evidence-only submission before viewing your final repair. Add one sentence:

> The evidence that most changed my diagnosis was __________ because __________.

Keep this sentence with the Day 2 exit artifact. The Day 3 opening will sample one response to distinguish an implementation or optimization failure from a model that is simply capacity-limited.
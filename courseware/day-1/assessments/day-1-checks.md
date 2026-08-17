# Day 1 Checks: See It

Complete these checks individually unless the instructor states otherwise. Show reasoning: a selected option without evidence does not demonstrate the objective.

## Submission and Collection

Use the cohort's participant submission channel announced at session start, labeled **Day 1 Checks**. Submit one digital artifact or clear photo containing your responses; if the cohort is working on paper, hand the same artifact to the instructor for equivalent collection.

- **Noon:** spend 8 minutes on all of `CHECK-D1-01`, including Scenario B.4; spend 5 minutes on the `CHECK-D1-02` commitment; use the final 2 minutes to submit `CHECK-D1-01` and a snapshot of the preserved D1-02 commitment. Keep the working copy for its later revision.
- **After `LAB-D1-03`:** add the revised D1-02 state to the same submission. Preserve both states.
- **Before Day 2 at 09:00:** add the five-minute consolidation consisting of `CHECK-D1-03` item 5 and `CHECK-D1-04` items 2 and 5. One response will be sampled during the Day 2 opening retrieval.

## CHECK-D1-01 - Model Choice and Boundary Evidence

**Objectives:** `OBJ-D1-01`, `OBJ-D1-03`  
**Noon allocation:** 8 minutes for both scenarios, including Scenario B.4

### Scenario A: choose a first baseline

A maintenance team has 1,800 labeled rows. Each row contains eight numeric sensor summaries, equipment age, and a binary target indicating whether a component failed within seven days. The team needs a transparent baseline by tomorrow and can compare richer models later.

Choose the most defensible **first** experiment:

- A. A compact linear or tree-based supervised baseline
- B. A deep neural network because the target is important
- C. No model; neural networks are the only form of machine learning
- D. A generative model because the input is numeric

Defend your choice with two scenario facts. Then name one piece of evidence that could later justify testing a neural network.

### Scenario B: predict boundary movement

A binary neuron uses `w = (2, 1)`, `b = -2`, and threshold `p >= 0.5`.

1. Write its decision-boundary equation.
2. The bias changes from `-2` to `-4` while the weights remain fixed. Predict what changes and what remains invariant.
3. Another experiment multiplies `w1`, `w2`, and `b` by `3`. Predict the effect on:
   - the `0.5` decision boundary;
   - the probability at a point not on the boundary.
4. **Follow-up evidence:** State one plot or numerical probe that would test each prediction.

---

## CHECK-D1-02 - Shape and Parameter Ticket

**Objectives:** `OBJ-D1-02`, `OBJ-D1-06`  
**Noon commitment:** 5 minutes, unscored  
**Scored revision:** 5 minutes at the end of the `LAB-D1-03` debrief

At noon, complete as much of the ticket as you can and circle uncertain entries. Do not erase this first commitment. After `LAB-D1-03`, revise in a second color and submit both states. Scoring uses the revised response plus the quality of your evidence-based corrections.

The final 2 minutes of the noon block are collection time for `CHECK-D1-01` and a snapshot of this commitment; they are not extra response time.

A batch-first dense network uses architecture `5 -> 6 -> 3` with batch size `B = 12`.

1. Give the shapes of `X`, `W1`, `b1`, `Z1`, `A1`, `W2`, `b2`, and `logits`.
2. Calculate the trainable parameter count for each dense layer and the total.
3. The batch size changes from `12` to `64`. List exactly which shapes change.
4. A teammate reports softmax output with shape `(12, 3)`, but the vector of per-example row sums begins `[0.23, 0.41, 0.36, ...]`. Diagnose the most likely semantic error and name an invariant that should fail.
5. Explain why passing every shape assertion is necessary but not sufficient for a correct forward pass.

---

## End-of-Day Consolidation Contract

Complete `CHECK-D1-03` item 5 and `CHECK-D1-04` items 2 and 5 as one five-minute consolidation. It is due through the **Day 1 Checks** submission channel before Day 2 at 09:00. Bring access to your submitted response: the instructor will sample one of the three items during the Day 2 opening retrieval.

---

## CHECK-D1-03 - Diagnose the Linear Limit

**Objectives:** `OBJ-D1-04`, `OBJ-D1-05`  
**Live core:** 6 minutes for items 1-4  
**Five-minute consolidation:** item 5, together with the two marked `CHECK-D1-04` items

Balanced XOR-like data has class `1` in the upper-left and lower-right clusters and class `0` in the other two clusters. A one-neuron logistic classifier remains near chance.

A teammate proposes:

> Add two dense hidden layers, use the identity activation after both, and train longer. Three lines should bend enough to solve XOR.

Respond with:

1. A geometric diagnosis of the one-neuron failure.
2. A concise algebraic or mechanism explanation of what stacked affine layers with identity activations represent.
3. The smallest architecture change that alters the representational family, not just the parameter count.
4. A before/after experiment that isolates the role of nonlinearity while holding data and layer shapes fixed.
5. **Follow-up evidence:** One observation that would support your explanation and one observation that would disconfirm it.

---

## CHECK-D1-04 - Explain a Mystery Forward Prediction

**Objectives:** `OBJ-D1-06`, `OBJ-D1-07`  
**Live core:** 7 minutes for items 1, 3, 4, and 6  
**Five-minute consolidation:** items 2 and 5, together with `CHECK-D1-03` item 5

A fixed `2 -> 2 -> 1` network uses ReLU in the hidden layer and sigmoid at the output. One probe has target class `0`. Its trace is:

| Stage | Value / shape |
|---|---|
| `x` | `(2.0, 1.0)`, shape `(2,)` |
| `z1` | `(2.5, -1.5)`, shape `(2,)` |
| `a1 = ReLU(z1)` | `(2.5, 0.0)`, shape `(2,)` |
| `z2` | `2.0`, shape `(1,)` |
| `p = sigmoid(z2)` | approximately `0.881`, shape `(1,)` |
| decision rule | predict `1` when `p >= 0.5` |

1. State the model's predicted class and whether it is correct for this probe.
2. **Follow-up evidence:** Use the trace to identify which hidden unit contributes a nonzero activation to the output calculation.
3. Explain the wrong prediction without anthropomorphic language. Cite at least two trace entries.
4. A second implementation transposes one matrix and raises a dimension-mismatch error before producing `z1`. Explain why that symptom is different from this wrong-but-complete prediction.
5. **Follow-up evidence:** Name one parameter perturbation you could test on a **copy** of the parameters and predict one local effect on this trace.
6. The forward pass does not change parameters. What two capabilities must Day 2 add if this example is to influence future predictions?

### Exit reflection

Complete in one sentence:

> A neural network prediction is __________; learning would need __________.
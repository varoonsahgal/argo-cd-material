# Day 1 Check Solutions

**Instructor only. Do not distribute with participant materials.**

Use mechanism evidence rather than exact phrasing. Suggested total: 24 points, 6 per check. A participant is Day 2 ready when `CHECK-D1-04` shows they can distinguish a completed but wrong forward pass from an implementation failure and can name error signal plus parameter-update rule.

## Assessment Operations

- **12:00-12:08:** learners complete all of `CHECK-D1-01`, including Scenario B.4.
- **12:08-12:13:** learners make the unscored `CHECK-D1-02` commitment.
- **12:13-12:15:** collect `CHECK-D1-01` and a snapshot of the preserved D1-02 commitment through the cohort's **Day 1 Checks** participant submission channel. For paper delivery, collect the same artifact by hand and return the D1-02 working copy.
- **End of `LAB-D1-03`:** collect both D1-02 states through the same channel after the scored revision.
- **Before Day 2 at 09:00:** collect `CHECK-D1-03` item 5 and `CHECK-D1-04` items 2 and 5 as one five-minute consolidation through the same channel. Sample one submitted response during the Day 2 opening retrieval.

Do not use the 16:20-16:30 buffer as routine completion time. It remains protected for recovery, questions, and close.

## CHECK-D1-01 - Model Choice and Boundary Evidence

### Expected answer

**Scenario A:** A is the strongest first experiment. The data are small, structured/tabular, and a transparent baseline is required quickly. The importance of the target does not itself justify a deep model. Evidence that could justify a neural experiment includes a valid baseline plateau plus evidence that important nonlinear interactions or learned representations remain unmodeled, or substantially more/less structured raw data becoming available.

Accept a compact neural baseline only if the learner frames it as a comparison rather than assumes superiority and still establishes a simpler reference. Do not accept B's stated reason.

**Scenario B:**

1. Boundary: `2*x1 + x2 - 2 = 0`, equivalently `x2 = -2*x1 + 2`.
2. With `b = -4`: `2*x1 + x2 - 4 = 0`, so the boundary translates parallel to itself. Orientation remains unchanged because the weight vector is unchanged.
3. Multiplying all terms by positive `3` yields `3*(2*x1 + x2 - 2) = 0`, so the `0.5` boundary is unchanged. Away from the boundary, the logit's magnitude triples; sigmoid probabilities move toward `0` or `1` according to the sign. This is not evidence of improved calibration.
4. Valid tests: overlay old/new `0.5` contours, compare slopes/normals, and evaluate a fixed off-boundary probe before/after scaling.

### Scoring anchor - 6 points

- 2: baseline choice uses scenario evidence.
- 1: names valid evidence for later neural comparison.
- 1: correct original and shifted boundary mechanism.
- 1: recognizes positive common scaling preserves the boundary.
- 1: predicts off-boundary probability change and proposes a discriminating test.

### Common wrong answers

- "Neural networks are best for important tasks": importance raises validation needs, not automatic model complexity.
- "Bias changes slope": with fixed weights, the normal is unchanged.
- "Scaling changes nothing": it preserves threshold decisions/boundary but changes score magnitude and sigmoid output.
- "Sharper probabilities are more accurate": accuracy and calibration require target evidence.

### Facilitation note

If a learner chooses a tree rather than linear baseline, accept it under A. The assessed decision is simpler credible baseline first, not a contest between two non-neural families.

## CHECK-D1-02 - Shape and Parameter Ticket

### Expected answer

| Object | Shape |
|---|---|
| `X` | `(12, 5)` |
| `W1` | `(5, 6)` |
| `b1` | `(6,)` |
| `Z1` | `(12, 6)` |
| `A1` | `(12, 6)` |
| `W2` | `(6, 3)` |
| `b2` | `(3,)` |
| `logits` | `(12, 3)` |

Counts: first layer `5*6 + 6 = 36`; second `6*3 + 3 = 21`; total `57`.

At batch size `64`, only arrays carrying examples change: `X (64, 5)`, `Z1 (64, 6)`, `A1 (64, 6)`, and `logits (64, 3)`; probabilities would also be `(64, 3)`. Parameter shapes/counts do not change.

The reported vector contains separate per-example row sums, so per-example normalization failed. The most likely cause is softmax along the batch axis (`axis=0`) instead of the class axis (`axis=1`). The invariant is `probabilities.sum(axis=1) == 1` within tolerance. Diagnosis should still be phrased as likely until the normalization code is inspected.

Shape assertions cannot detect wrong axis, wrong values, omitted activation, or wrong class semantics when shapes remain compatible.

### Scoring anchor - 6 points

- 2: all layer/data shapes follow batch-first convention.
- 1: parameter calculation is `36 + 21 = 57`.
- 1: batch-size changes are isolated to example-carrying arrays.
- 1: wrong-axis diagnosis plus row-sum invariant.
- 1: explains semantic correctness beyond shape correctness.

### Common wrong answers

- `W1 = (6, 5)`: inconsistent with `X @ W1` under the course convention.
- Total `48`: counts weights but omits all nine bias parameters; have learner expand each term.
- Parameter count scales with batch: confuses data volume with adjustable model state.
- "The code would crash": wrong-axis softmax can run and return the expected shape.

### Facilitation note

Accept "axis error is likely, but inspect the normalization code" as stronger than unwarranted certainty.

## CHECK-D1-03 - Diagnose the Linear Limit

### Expected answer

1. XOR classes occupy alternating corners. No single line can place both class-1 corners on one side while placing both class-0 corners on the other.
2. An affine composition remains affine. For two layers without nonlinearities, `(XW1 + b1)W2 + b2 = X(W1W2) + (b1W2 + b2)`. More identity-activated layers change parameterization, not the family of input-output boundary.
3. Add at least one hidden layer with a nonlinear activation and enough units to construct useful intermediate regions/features. Saying only "add neurons" is insufficient unless nonlinearity is included.
4. Hold data, layer widths, fixed parameters or controlled fitting procedure, and evaluation constant; compare identity hidden activation with a nonlinear hidden activation. Plot raw and hidden representations plus output boundary.
5. Supporting observation: identity stack remains approximately chance/linear while nonlinear hidden coordinates become linearly separable and output performance rises. Disconfirming evidence: the supposedly identity stack creates a nonlinear boundary under the same controlled conditions, which suggests an unrecognized nonlinear operation or flawed comparison. A nonlinear model not improving does **not alone** disprove the representational mechanism; parameters may be unsuitable.

### Acceptable alternatives

Feature engineering that maps the raw coordinates nonlinearly before a linear classifier also changes the representation and can solve XOR. Accept it as a mechanism alternative, while noting the objective asks why hidden nonlinear transformations are useful.

### Scoring anchor - 6 points

- 1: geometric impossibility.
- 2: affine-composition mechanism.
- 1: nonlinear representational change.
- 1: controlled before/after experiment.
- 1: supporting and genuinely disconfirming observations.

### Common wrong answers

- "Sigmoid bends the boundary": sigmoid changes output scale; its `0.5` contour remains where the affine score is zero.
- "More epochs make any model fit": optimization cannot expand the representational family.
- "A nonlinear network must solve XOR": capacity permits a solution; fixed or learned parameters still matter.

### Facilitation note

Press learners to separate **can represent** from **will learn**. Day 1 establishes representation; Day 2 addresses parameter learning.

## CHECK-D1-04 - Explain a Mystery Forward Prediction

### Expected answer

1. `p = 0.881 >= 0.5`, so the model predicts class `1`; target is `0`, so this probe is incorrect.
2. The first hidden unit contributes a nonzero activation (`2.5`); the second is zero after ReLU. Strictly, contribution to `z2` also depends on output weights, which are not shown. Strong learners should qualify that nonzero activation alone does not reveal sign/magnitude of its output contribution.
3. Example: the fixed first-layer parameters produce `z1 = (2.5, -1.5)`, ReLU passes the first value and zeros the second, and the fixed output transformation yields positive logit `2.0`; sigmoid maps that to `0.881`, above threshold. This is a trace of parameterized computation, not knowledge or intent.
4. A transpose error is an implementation/shape failure: no complete trace or prediction is produced. The mystery case is shape-valid and semantically executable but produces a target-disagreeing decision under fixed parameters.
5. Many answers are acceptable if directional reasoning is qualified. Examples: decrease the copied output weight connected to the positive first hidden activation, predicting a lower `z2` and lower `p`; or decrease the copied output bias, predicting a lower `z2` without changing `z1/a1`. An upstream weight change is acceptable if the learner states which `z1` component it changes.
6. Day 2 must add an error/loss signal and a rule for assigning sensitivity and updating parameters. "Backpropagation and gradient descent" is acceptable if the learner can state their roles; "more data" alone is not.

Possible exit sentence: "A neural network prediction is a trace through fixed parameterized transformations; learning would need an error signal and a rule for changing those parameters."

### Scoring anchor - 6 points

- 1: prediction and correctness.
- 1: hidden activation evidence with contribution caveat or reasonable interpretation.
- 1: two-stage mechanism explanation.
- 1: distinguishes shape failure from model error.
- 1: plausible copied-parameter perturbation and local prediction.
- 1: loss/error signal plus parameter-update mechanism.

### Common wrong answers

- "Unit 1 causes the decision": output weights are omitted, so causality/magnitude cannot be fully assigned from activation alone.
- "The network should flip the target automatically": no learning occurs in a forward pass.
- "Fix the transpose to correct the wrong prediction": these are separate scenarios and failure classes.
- "Raise confidence": the target is class `0`; more extreme class-1 output worsens this case.

### Facilitation note

Use this as the Day 2 gate. If learners can calculate but anthropomorphize, ask them to replace every intent verb with a parameter, activation, or threshold. If they cannot name loss plus update, begin Day 2 with the fixed-parameter mystery.
# Day 1 Challenge Solutions

**Instructor only. Do not distribute with participant materials.**

This key gives expected reasoning, acceptable alternatives, common wrong answers, and facilitation moves for every prompt in the Day 1 challenge brief.

## ACT-D1-01 - Boundary Motion Prediction

### Expected reasoning

For $w_2 \ne 0$, the boundary can be written $x_2 = -(w_1/w_2)x_1 - b/w_2$. This form helps, but do not reduce the activity to memorizing slope/intercept.

- Increasing `w1` with `w2` and `b` fixed changes the weight ratio, so orientation generally changes. The intercept stays `-b/w2` in this particular rearrangement, but the visible effect depends on the full parameterization and plotted domain.
- Increasing `w2` generally changes both slope and `x2` intercept because `w2` appears in both denominators. It is not a pure rotation control.
- Increasing `b` with weights fixed translates the boundary parallel to itself. The normal vector `w` and therefore orientation remain unchanged.
- Probe probabilities can change even without a probe crossing the boundary because sigmoid depends on signed score, not only the thresholded class.
- Scaling `w` and `b` by the same positive constant leaves `w dot x + b = 0` unchanged but increases score magnitudes away from the boundary, sharpening sigmoid outputs toward `0` or `1`. A negative scale also swaps sides/classes under the fixed decision convention.

### Evidence anchors

Accept any fixed probe or contour comparison that correctly distinguishes:

- location: old and new `0.5` contours differ;
- orientation: contour slopes/normals differ;
- confidence-shaped output: probe probabilities differ even when class and boundary are unchanged.

### Common wrong answers and moves

| Wrong answer | Why it fails | Facilitation move |
|---|---|---|
| "`w1` rotates, `w2` translates, `b` changes confidence." | Weights jointly determine the normal/orientation; bias shifts the zero-score contour. | Freeze two controls and show two points on each old/new contour. |
| "If accuracy stays fixed, nothing changed." | A contour or probability can move without changing decisions on the finite sample. | Probe an unlabeled grid point near the old boundary. |
| "Larger score magnitude means better calibrated confidence." | Sharper sigmoid outputs do not establish calibration. | Ask what target-frequency evidence would be required for calibration. |

### Facilitation note

Score revisions positively when learners cite a visible invariant. Do not penalize an imperfect freehand sketch if the mechanism explanation is sound.

## ACT-D1-02 - Be the Neural Network

### Start-state answer

With `w = (1, 0)` and `b = 0`, `z = x1`. Thresholding at `z >= 0` gives:

| Point | `z` | Prediction | Correct? |
|---|---:|---:|---|
| A | `-2.00` | `0` | yes |
| B | `-1.00` | `0` | yes |
| C | `0.00` | `1` | no |
| D | `1.00` | `1` | yes |
| E | `0.50` | `1` | yes |
| F | `-0.25` | `0` | no |

One efficient valid change is `w2: 0 -> 0.5`, leaving `w1 = 1`, `b = 0`:

| Point | New `z = x1 + 0.5*x2` | Prediction |
|---|---:|---:|
| A | `-2.50` | `0` |
| B | `-0.50` | `0` |
| C | `-0.50` | `0` |
| D | `1.25` | `1` |
| E | `1.25` | `1` |
| F | `0.75` | `1` |

### Acceptable alternatives

There are infinitely many valid separators. Accept any parameters that make A, B, C negative and D, E, F nonnegative under the stated threshold. Require the team to show all six signs. A team that reaches 5/6 with a precise conflict analysis can earn the evidence point but not the full-classification point.

The automated-search answer should name at least:

1. an objective/error signal that distinguishes better from worse settings; and
2. an update/search rule that uses that signal to choose parameter changes.

"Data" is a useful third ingredient, but it does not replace either item.

### Common wrong answers

- Treating `z = 0` as class `0`. The activity explicitly uses `z >= 0` for class `1`; this is why C initially fails.
- Changing all three parameters and claiming one caused the improvement. The score rewards one-variable attribution.
- Claiming the discovered setting is unique. Ask for a small perturbation that preserves every sign.
- Saying gradient descent copies manual trial-and-error. Day 2 will show a computed local update signal; keep this bridge provisional.

### Facilitation note

If teams finish immediately, ask them to find a second valid setting and identify a range around one parameter that preserves all predictions. Do not let the extension displace the automation debrief.

## ACT-D1-03 - Activation Card Sort

### Core matches

| Function | Behavior | Role/symptom cards |
|---|---|---|
| Sigmoid | A | 1, 6 |
| Tanh | B | 4, 6 |
| ReLU | C | 3 |
| Leaky ReLU | D | 5 |
| Softmax | E | 2, 7 |

Card 6 correctly applies to both sigmoid and tanh. Card 7 belongs specifically to softmax in this set. ReLU can produce zero output for negative input, but one zero is not enough to diagnose a permanently dead unit.

### Expected invariants

- Sigmoid: same shape as input; every finite output is strictly between `0` and `1`.
- ReLU: same shape; outputs are nonnegative; positive inputs are unchanged.
- Softmax: same shape; outputs are nonnegative; each example's class-axis sum is approximately `1`.

### Acceptable alternatives

Learners may note that sigmoid can be used independently for multiple labels, but do not let that optional output case displace the Day 1 binary role. Learners may describe tanh as hidden-layer-capable; the card asks for a bounded zero-centered property, not a universal recommendation.

### Common wrong answers and moves

| Wrong answer | Correction |
|---|---|
| Softmax is "a sigmoid for each class." | Change one logit and show that every output changes because the denominator is shared. |
| ReLU has output range `(0, 1)`. | Test `z = 3`. |
| A zero ReLU output proves the unit is dead forever. | Ask whether other examples or later parameter changes could make its pre-activation positive. |
| The most common activation is always correct. | Return to the layer's role and required output semantics; avoid unsupported prevalence claims. |

### Facilitation note

Reveal mathematical behavior first. Any claim about present-day popularity or framework defaults requires current verification and is unnecessary for the core answer.

## ACT-D1-04 - Shape Relay

### Completed shape map

| Object | Shape when `B = 5` |
|---|---|
| `X` | `(5, 4)` |
| `W1` | `(4, 8)` |
| `b1` | `(8,)` |
| `Z1` | `(5, 8)` |
| `A1` | `(5, 8)` |
| `W2` | `(8, 3)` |
| `b2` | `(3,)` |
| `logits` | `(5, 3)` |
| `probabilities` | `(5, 3)` |

Parameter count:

- first layer: `4*8 + 8 = 40`;
- second layer: `8*3 + 3 = 27`;
- total: `67`.

When `B` becomes `32`, only `X`, `Z1`, `A1`, `logits`, and `probabilities` change their first dimension from `5` to `32`. Parameter shapes and the total remain unchanged.

The contracted dimensions are the input/hidden widths: `(5, 4) @ (4, 8)` and `(5, 8) @ (8, 3)`. Bias broadcasts across the first dimension. Softmax normalizes across the class axis, axis `1` for `(B, 3)`.

### Shape-correct but semantically wrong examples

- softmax across axis `0`;
- incorrect parameter values;
- missing nonlinear hidden activation;
- swapped class meaning;
- applying a binary threshold independently to multiclass softmax outputs.

### Common wrong answers

- Counting `5*4` input values as parameters: data are not trainable objects.
- Using `W1` shape `(8, 4)`: this follows a different vector convention and does not match `X @ W1` under the course contract.
- Counting only weights: both weight matrices and bias vectors are trainable parameters.
- Changing `W` when batch size changes: ask whether the learned feature interface changed.

### Facilitation note

Require the dimension explanation before confirming a row. The relay is about predicting executable contracts, not racing through memorized shapes.
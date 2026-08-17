# Day 1 Challenges: See It

These four short activities turn Day 1 concepts into visible decisions. Record a commitment before the reveal or calculation. A changed answer after evidence is useful when you can explain what changed your mind.

## ACT-D1-01 - Boundary Motion Prediction

**Connected objectives:** `OBJ-D1-02`, `OBJ-D1-03`  
**Time:** 8 minutes, inside `LESSON-D1-02`  
**Materials:** three blank coordinate grids, pen or annotation tool, instructor boundary visual

### Setup

A binary neuron uses

$$
z = w_1x_1 + w_2x_2 + b, \qquad p = \sigma(z)
$$

and predicts class `1` when $p \ge 0.5$. The visible decision boundary is therefore where $z=0$.

### Commitment

Before any slider moves, copy the current boundary onto three grids. On each grid, sketch your predicted new boundary for one isolated change:

1. Increase `w1`; keep `w2` and `b` fixed.
2. Increase `w2`; keep `w1` and `b` fixed.
3. Increase `b`; keep both weights fixed.

For each sketch, complete:

| Change | Orientation: what might change? | Location: what might change? | Probe probabilities: what might change? |
|---|---|---|---|
| Increase `w1` only |  |  |  |
| Increase `w2` only |  |  |  |
| Increase `b` only |  |  |  |

Also mark one claim you are **least certain** about.

### Evidence sequence

1. Observe one slider change at a time; do not change two controls together.
2. Trace the ghosted old contour and solid new contour.
3. Record the before/after probability for one fixed probe point.
4. Circle any part of your sketch that survives the reveal; revise another part in a different color.

### Evidence record

For one change, identify:

- one quantity that changed;
- one geometric property that stayed invariant;
- one observation that separates boundary location from confidence away from the boundary.

### Debrief questions

1. Why is a weight not a pure "rotation knob" in isolation?
2. Which evidence would show a boundary movement even if class accuracy did not change?
3. How could probability shading change while a class boundary stays fixed?

---

## ACT-D1-02 - Be the Neural Network

**Connected objectives:** `OBJ-D1-02`, `OBJ-D1-03`  
**Time:** 7 minutes, embedded in `LAB-D1-01`  
**Pattern:** constrained manual parameter search

### Point cards

Use a `0.5` sigmoid threshold, equivalent to predicting class `1` when $z \ge 0$.

| Point | `(x1, x2)` | Target |
|---|---:|---:|
| A | `(-2.00, -1.00)` | `0` |
| B | `(-1.00, 1.00)` | `0` |
| C | `(0.00, -1.00)` | `0` |
| D | `(1.00, 0.50)` | `1` |
| E | `(0.50, 1.50)` | `1` |
| F | `(-0.25, 2.00)` | `1` |

Start with `w1 = 1`, `w2 = 0`, and `b = 0`.

### Commitment

1. Calculate or sign-check `z` for all six points under the start setting.
2. Identify the misclassified point(s).
3. Commit to at most **three one-parameter changes**. Before each change, write which point(s) it should affect and why.

| Attempt | Parameter changed | New value | Predicted effect | Observed correct / 6 |
|---:|---|---:|---|---:|
| Start | - | - | - |  |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

### Rules and scoring

- Change only one of `w1`, `w2`, or `b` per attempt.
- Do not erase unsuccessful attempts; they are evidence.
- Multiple parameter settings can be valid.

Score up to 6 points:

- 2 points: predictions are written before changes.
- 2 points: one-variable-at-a-time discipline is preserved.
- 1 point: final setting classifies all six points, or the team gives a precise explanation of the remaining conflict.
- 1 point: explanation uses score/boundary evidence rather than "we guessed."

### Debrief questions

1. Which failed or successful attempt taught you the most?
2. Why does a workable setting not imply it is the only setting?
3. What becomes impractical when a network has thousands or millions of parameters?
4. What two ingredients would an automated search need beyond the forward calculation?

---

## ACT-D1-03 - Activation Card Sort

**Connected objectives:** `OBJ-D1-05`, `OBJ-D1-06`  
**Time:** 8 minutes, inside `LESSON-D1-05`  
**Materials:** function-name cards, curve cards, behavior cards, role cards

### Function-name cards

**Core:** `sigmoid` | `tanh` | `ReLU` | `softmax`

**Optional extension:** `Leaky ReLU`

### Behavior cards

| Card | Behavior |
|---|---|
| A | Scalar output lies between `0` and `1`; extreme inputs compress near both ends. |
| B | Scalar output lies between `-1` and `1`; extreme positive and negative inputs compress. |
| C | Negative scalar inputs map to `0`; positive inputs pass through unchanged. |
| D | Negative scalar inputs keep a small nonzero slope; positive inputs pass through unchanged. |
| E | A vector of logits becomes coupled nonnegative outputs that sum to `1` along the class axis. |

### Role / symptom cards

| Card | Role or symptom |
|---|---|
| 1 | Binary output probability-shaped value |
| 2 | Multiclass output probability-shaped vector |
| 3 | Hidden nonlinearity with an exactly zero negative region |
| 4 | Zero-centered bounded activation |
| 5 | Hidden nonlinearity that preserves a small negative signal |
| 6 | Can visibly saturate for very large positive or negative values |
| 7 | Wrong normalization axis can produce valid-looking numbers but invalid per-example totals |

### Commitment

1. Match each core function name to one behavior card. Skip cards D and 5 unless you take the optional Leaky ReLU extension.
2. Assign each role/symptom card to every function for which it is a defensible match. Some functions receive more than one card.
3. For `sigmoid`, `ReLU`, and `softmax`, write one invariant or range you could test in code.
4. Mark one pairing you would change if the function were used in a hidden layer rather than an output layer.

**Optional:** Add the Leaky ReLU card, match cards D and 5, and explain what evidence distinguishes it from ReLU on negative inputs.

### Reveal sequence

The instructor reveals one curve or vector transformation at a time. After each reveal:

- keep or revise one pairing;
- cite the visible behavior that supports the revision;
- avoid relying only on "this function is common."

### Debrief questions

1. Why is choosing an activation partly about the role of the layer?
2. Why do independent sigmoids and softmax express different output relationships?
3. Does one zero ReLU output prove that a unit is permanently dead? What more would you inspect?

---

## ACT-D1-04 - Shape Relay

**Connected objectives:** `OBJ-D1-02`, `OBJ-D1-06`  
**Time:** 8 minutes, inside `LESSON-D1-04`  
**Pattern:** team relay with an executable shape hypothesis

### Architecture

A batch-first dense network has architecture `4 -> 8 -> 3`. Start with batch size `B = 5`.

### Relay sequence

Each teammate completes one row, explains the dimension logic, and passes the sheet. Do not run code until the table is complete.

| Object | Meaning | Predicted shape |
|---|---|---|
| `X` | batch input |  |
| `W1` | input-to-hidden weights |  |
| `b1` | hidden bias |  |
| `Z1 = X @ W1 + b1` | hidden pre-activations |  |
| `A1` | hidden activations |  |
| `W2` | hidden-to-output weights |  |
| `b2` | output bias |  |
| `logits = A1 @ W2 + b2` | output scores |  |
| `probabilities` | per-example softmax output |  |

### Parameter commitment

Show the calculation for:

1. input-to-hidden parameters;
2. hidden-to-output parameters;
3. total trainable parameters.

Then change only the batch size from `5` to `32`.

- Which shapes change?
- Which shapes do not change?
- Does the parameter count change? Defend your answer from the table.

### Evidence collection

When the shape map is revealed or code is run, annotate:

- one contracted matrix dimension;
- where bias broadcasting occurs;
- the axis across which softmax must normalize;
- one shape-correct computation that could still be semantically wrong.

### Debrief questions

1. Why is shape prediction a testable hypothesis rather than bookkeeping?
2. Why does the batch dimension pass through the network while feature width changes?
3. Which invariant catches wrong-axis softmax even when every array shape looks plausible?
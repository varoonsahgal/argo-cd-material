# Notation and Style Contract

This file controls notation, shapes, naming, evidence language, and participant/instructor separation across lessons, slides, challenges, checks, and labs.

## 1. Core Shape Convention

Use **batch-first, examples-as-rows** notation throughout.

| Symbol | Meaning | Shape |
|---|---|---|
| `B` | Batch size / number of examples in the current batch | scalar integer |
| `d_in` | Number of input features to a layer | scalar integer |
| `d_out` | Number of output units from a layer | scalar integer |
| `x` | One input example | `(d_in,)` |
| `X` | Batch of input examples | `(B, d_in)` |
| `W` | Dense-layer weight matrix | `(d_in, d_out)` |
| `b` | Dense-layer bias vector | `(d_out,)` |
| `Z` | Batch of pre-activations / logits | `(B, d_out)` |
| `A` | Batch of post-activation values | `(B, d_out)` |
| `y` | Targets | `(B,)` for class indices unless a lab explicitly needs `(B, 1)` |

The dense-layer convention is:

$$
Z = XW + b, \qquad A = g(Z)
$$

NumPy code mirrors the notation:

```python
Z = X @ W + b
A = activation(Z)
```

The bias broadcasts across examples. It remains one parameter vector with `d_out` elements.

### Named layers

For layer `l`, use `W_l`, `b_l`, `Z_l`, and `A_l` in prose/math, or `W1`, `b1`, `Z1`, and `A1` in compact code. State shapes before values:

$$
X_{(B, d_0)} \rightarrow Z_1{}_{(B, d_1)} \rightarrow A_1{}_{(B, d_1)} \rightarrow Z_2{}_{(B, d_2)}
$$

Do not switch to column-vector examples within a lesson or notebook. When citing an external source with another orientation, translate it explicitly.

## 2. Parameter Counts

For a dense layer from `d_in` to `d_out`:

$$
\text{parameters} = d_{in}d_{out} + d_{out}
$$

For `4 -> 8 -> 3`:

$$
(4\times8 + 8) + (8\times3 + 3) = 67
$$

Never count batch size, examples, activations, or an input placeholder as trainable parameters.

## 3. Scores, Logits, Probabilities, and Predictions

- **Pre-activation** is the affine result before an activation.
- **Logit** is a raw output score before probability conversion/normalization.
- **Probability** is a normalized, probability-shaped output in `[0, 1]`.
- **Prediction** is the task decision produced by an explicitly stated rule.

For a binary Day 1 example:

$$
z = x\cdot w + b, \qquad p = \sigma(z), \qquad \hat{y} = \mathbb{1}[p \ge 0.5]
$$

For multiclass examples, softmax operates across the class dimension for each row. Say **softmax row sums equal 1** under the batch-first convention. Do not call logits probabilities or imply that probability-shaped outputs are calibrated.

## 4. Dataset Split Names

Use only these primary names:

| Name | Purpose | Decision boundary |
|---|---|---|
| Training set | Fit parameters and any learned preprocessing statistics. | May influence training directly. |
| Validation set | Compare choices and diagnose during development. | Must not fit parameters or preprocessing statistics. |
| Test set | Final, limited-use estimate after development choices are fixed. | Must not guide model or hyperparameter selection. |

Prefer variable names `X_train`, `y_train`, `X_val`, `y_val`, `X_test`, and `y_test`. Use **validation**, not a rotating mix of *dev*, *holdout*, and *evaluation*, unless a source or scenario requires a mapped synonym.

## 5. Seeds, Reproducibility, and Ranges

- Say **seeded** only when every random generator used by the artifact is explicitly set.
- Record the seed beside the generated data or model setup.
- Treat a seed as a repeatability aid, not proof of universal or bitwise reproducibility.
- State expected results as **sanity ranges**, **broad bands**, or **invariants**, not guaranteed exact outputs.
- Pair ranges with environment assumptions when runtime, framework, or hardware matters.
- Prefer invariants such as shapes, finite values, probability bounds, and row sums when they test the mechanism directly.
- Use wording such as "typically falls in `0.82-0.92` under the supplied seed and fixed parameters" rather than "will be `0.87`."

Current framework determinism and hardware claims require dated primary-source verification before use.

## 6. Evidence Language

Use mechanism-aware, non-anthropomorphic wording:

| Prefer | Avoid |
|---|---|
| "The fixed parameters produce..." | "The network knows..." |
| "The hidden activations separate most points..." | "The hidden unit understands..." |
| "The plot supports the hypothesis..." | "The plot proves the cause..." |
| "The run is consistent with..." | "This symptom always means..." |
| "The output is probability-shaped..." | "The model is 90% confident" without calibration evidence |

For every important experiment, preserve this record:

1. **Prediction:** what should happen and why.
2. **Evidence:** what value, shape, visual, or invariant will be observed.
3. **Interpretation:** what the evidence supports and what competing explanation remains.
4. **Transfer:** where the same reasoning applies next.

## 7. Visual Style

- Give each visual one teaching job.
- State what learners should observe and what the visual must not imply.
- Preserve point identity/colors across raw-space and hidden-space plots.
- Use ghosted before/after boundaries when teaching parameter effects.
- Label axes, thresholds, dimensions, and units.
- Keep comparison axes aligned.
- Include concise alt text for every required slide visual.
- Use Mermaid for state flow and structure, not decorative diagrams.

## 8. Scope Labels

- `CORE`: planned live path required for the stated objective.
- `SHORTEN`: first explanatory detail to compress if time is lost.
- `OPTIONAL`: extension that is not required for objective evidence.
- `MOVE`: preserved reference topic taught elsewhere or at conceptual depth only.
- `VERIFY-CURRENT`: claim or API that needs dated primary-source verification before release.

Do not silently promote `OPTIONAL`, `MOVE`, or `VERIFY-CURRENT` material into required participant work.

## 9. Participant and Instructor Separation

Participant-facing files may contain:

- objectives, explanations, starter states, TODOs, prompts, evidence fields, sanity invariants, troubleshooting, and debrief questions;
- links to participant guides, challenges, checks, and participant notebooks.

Participant-facing files must not contain or link to:

- completed TODOs or prediction answers;
- answer keys, hidden diagnoses, scoring anchors, or instructor notes;
- any file under `courseware/instructor-solutions/` or `courseware/instructor-guide/`;
- a canonical instructor-only solution elsewhere in the repository.

Instructor artifacts may quote participant prompts and add expected answers, acceptable alternatives, misconceptions, hint ladders, recovery steps, and scoring guidance. Label solution artifacts **Instructor only** near the top.

## 10. Extensibility

Add notation only when a canonical objective needs it. New symbols must define meaning, shape/orientation, units or range, and the first lesson that introduces them. Reuse existing terms instead of creating day-local synonyms.
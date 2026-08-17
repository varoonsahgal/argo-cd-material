# Participant Validation: LAB-D1-03

**Current validation status: PASS WITH NOTES**  
**Interestingness: STRONG**

## Lab

- **Name:** Shape and Activation Observatory
- **Participant path:** `courseware/day-1/labs/LAB-D1-03-shapes-activations.ipynb`
- **Canonical SHA-256:** `8dc99076c5aaba05673f7c6d5388e1bc519f33dc366ac592b91bfbc33f61511e`
- **Learning objective:** Make dense shapes, parameter counts, broadcasting, activation behavior, stable multiclass normalization, and semantic-axis failures observable for `OBJ-D1-02`, `OBJ-D1-05`, and `OBJ-D1-06`.
- **Gate decision:** The revised core path completes without any Leaky ReLU cell or symbol. The separately optional Leaky ReLU branch also completes. No participant blocker or required notebook fix remains.

## Environment Tested

- macOS on Apple silicon, local CPU
- Fresh temporary virtual environment created from the published setup instructions
- Python 3.11.8
- NumPy 2.4.6
- matplotlib 3.11.1
- scikit-learn 1.9.0 installed but not imported by the notebook
- nbformat 5.11.0
- nbclient 0.11.0
- ipykernel 7.3.0 / fresh `python3` kernels
- No GPU, dataset, file dependency, network call, or previous-lab state was used by the notebook. Network access was used only to install the documented pins into the temporary validation environment.

## Commands and Cells Executed

1. Parsed the current notebook from disk as JSON, loaded it with `nbformat`, ran official schema validation, and syntax-checked all code cells.
2. Audited all 33 cells for IDs, language metadata, stored state, hidden metadata, response fields, TODOs, imports, leakage terms, local links, and optional/core symbol dependencies.
3. Executed the untouched canonical starter in a fresh kernel. It stopped intentionally at cell 6, the first shape/count prediction checkpoint.
4. Repeated fresh-kernel runs after each learner stage. The path stopped in order at the dense TODO, activation prediction, activation TODO, softmax prediction, softmax TODO, and final explanation checkpoint.
5. Created a temporary 29-cell participant-completed core copy. The optional heading and cells 30-33 were removed, and no Leaky ReLU term or optional symbol remained. Restarted with a new kernel and executed all core cells in order.
6. Created a separate temporary 33-cell completion, completed the optional Leaky ReLU predictions, implementation, plot, slope experiment, and interpretation, then executed it in another new kernel.
7. Ran an independent fresh-kernel probe with sigmoid inputs at `+/-1e6` and softmax logits at `+/-1e6`.
8. Extracted and visually inspected both core figures and the optional slope figure.

## Runtime Observed

- Untouched starter to first prediction stop: **1.895 s** including kernel startup
- Staged starter checks: **1.007-1.339 s** each including a fresh kernel startup
- Strict core-only completed run: **1.753 s**, 29 cells, 16 code cells, 2 figures, 0 error outputs
- Full completed run with optional branch: **1.422 s**, 33 cells, 19 code cells, 3 figures, 0 error outputs
- Independent extreme-value probe: **1.532 s** including kernel startup

Execution is comfortably below the notebook's 10-second compute target and is practical on CPU. Participant thinking and implementation time, not compute, will dominate the 40-minute block.

## What Worked

- JSON parsing and official `nbformat` validation passed for the current 33-cell artifact.
- Every cell has a unique `metadata.id` and the correct `metadata.language`; no output, execution count, or hidden source/output state is stored.
- All participant prediction and interpretation dictionaries are blank. The only incomplete implementations are the intended dense, sigmoid/tanh/ReLU, softmax, and optional Leaky ReLU TODOs.
- Imports are limited to `platform`, NumPy, and matplotlib. No solution path, instructor artifact, answer key, file I/O, dataset, package installation, or network call appears in the notebook.
- Prediction checkpoints occur before dense execution, activation plots, softmax normalization, and optional Leaky ReLU evidence. Their failure messages identify the required learner action.
- The `4 -> 8 -> 3` architecture reports exactly **67 parameters**. Bias broadcasting was verified by showing every row of `Z1 - X @ W1` equals `b1`.
- `Z1` and `A1` have shape `(5, 8)`; logits and probabilities have shape `(5, 3)`.
- Stable sigmoid remained finite for `[-1e6, 0, 1e6]`, returning `[0, 0.5, 1]`.
- Sigmoid and tanh visibly saturate. Their output changes from input 8 to 12 were `0.000329` and approximately `2.25e-7`.
- The supplied strongly negative `(5, 8)` matrix produced 0 nonzero ReLU outputs out of 40. The prompts correctly distinguish this current region from a permanently dead unit.
- Stable row-wise softmax remained finite for logits near `+/-1000` and `+/-1e6`; every row summed to 1 within `1e-6`.
- Wrong-axis softmax preserved shape `(5, 3)` but produced row sums `[0.647134, 0.635321, 0.406391, 0.715075, 0.596079]`; its columns summed to 1. The expected assertion was caught, printed clearly, and followed by successful recovery.
- The core-only notebook completed without loading, defining, or referencing any optional variable. The required checkpoint occurs before the optional section.
- The optional branch showed the expected negative outputs: for input `-12`, slopes `0.10` and `0.02` produced `-1.2` and `-0.24`, while nonnegative outputs and all shapes remained unchanged.
- Core and optional plots have readable titles, axes, legends/color bars, zero lines, and aligned comparisons. The optional curve visibly distinguishes both negative slopes from ReLU.
- All notebook prerequisite/debrief links resolve, including `LESSON-D1-04`, `LESSON-D1-05`, `ACT-D1-03`, `ACT-D1-04`, and the Student Guide D1-03 debrief. The Student Guide launch link points to the current notebook.

## Failures Encountered

- The wrong-axis row-sum assertion failed exactly as designed and was caught within the notebook. This is required diagnostic evidence, not an execution defect.
- Forced use of a noninteractive matplotlib backend suppressed inline image outputs during one tester run. Repeating with the notebook's normal inline backend produced all expected figures; this was a tester configuration effect, not a lab failure.
- No unexpected execution, metadata, leakage, link, shape, stability, or optional-dependency failure occurred.

## Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Parameter count | `67` | `67` |
| Dense/broadcast shapes | `Z1`, `A1`: `(5, 8)` | Passed |
| Output shapes | logits/probabilities: `(5, 3)` | Passed |
| Correct softmax | Finite; each row sums to 1 | Passed through magnitude `1e6` |
| Wrong-axis softmax | Same shape; row invariant fails | Failed rows; columns sum to 1 |
| Negative ReLU case | Current 40 outputs all zero | 0/40 nonzero |
| Saturation | Sigmoid/tanh flatten at extremes | Visible and numerically confirmed |
| Core without optional cells | Complete independently | Passed in a strict 29-cell copy |
| Optional Leaky ReLU | Negative slope changes only negative branch | Passed for slopes `0.10` and `0.02` |
| Figures | Two core; one additional optional | 2 core; 3 in full run |

## Reproducibility and Colab Concerns

- Seeded, in-memory arrays make the tested behavior deterministic.
- The exact environment setup commands in `courseware/shared/environment.md` installed successfully in a clean temporary Python 3.11.8 environment.
- The notebook is standalone, CPU-only, very small, and avoids local paths, downloads, and version-sensitive framework APIs. These properties make hosted Colab execution practical.
- A real hosted Colab CPU session was **not** performed. This report does not claim hosted validation. Colab remains a non-blocking environment note under the current local-or-Colab delivery contract.

## Required Fixes

None.

## Optional Improvements

- Run the notebook in a fresh hosted Colab CPU session before changing course language from "Colab practical" to "hosted Colab validated."
- Retain the printed saturation deltas as a nonvisual complement to the plots.

## Retest Requirements

- Retest after changes to cell ordering, core/optional boundaries, architecture widths, parameter count, activation definitions, softmax axes, extreme-value assertions, deliberate-failure handling, or prerequisite/debrief links.
- A future retest must again execute a strict core-only copy with every optional Leaky ReLU cell skipped, followed by a separate optional-branch run.

## Prior-History Disposition

An earlier report recorded an empty-notebook failure, and a later report validated a version that still included Leaky ReLU in core activation evidence. Both are superseded by this current-disk retest. The notebook is now substantive, and all Leaky ReLU prediction, implementation, plotting, and interpretation work is explicitly optional and independently skippable.

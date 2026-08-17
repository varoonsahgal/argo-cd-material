# Solution Validation: LAB-D1-01

## Lab and Solution

- **Lab:** `courseware/day-1/labs/LAB-D1-01-neuron-boundary.ipynb`
- **Solution:** `courseware/instructor-solutions/day-1/LAB-D1-01-neuron-boundary-SOLUTION.ipynb`
- **Objectives:** `OBJ-D1-01`, `OBJ-D1-02`, `OBJ-D1-03`
- **Final status:** **PASS WITH NOTES**

## Environment Used

- macOS on Apple silicon, local CPU
- Python 3.11.8
- NumPy 2.4.6
- matplotlib 3.11.1
- scikit-learn 1.9.0 available but not required by this notebook
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- No GPU, network call, download, external data file, or prior-notebook state

## Clean-Run Evidence

- Rebuilt canonical solution, cleared outputs, started a new `python3` kernel, and executed all cells in order with `NotebookClient` and `allow_errors=False`.
- Final clean wall time, including kernel startup: **2.438 s**.
- All **17 code cells** executed; **6 PNG** outputs rendered; no uncaught error output exists.
- Official nbformat validation passed after execution.
- All **41 cells** have unique matching top-level/`metadata.id` values and `metadata.language` set to `markdown` or `python`.

## Tasks and Questions Covered

- Completed boundary-motion and common-scaling predictions with an adjacent answer and hint ladder.
- Implemented vectorized weighted sum, stable sigmoid, threshold conversion, and coefficient validation.
- Completed six-probe shape/range checks and initial-boundary interpretation.
- Completed isolated `w1`, `w2`, bias, and common-scaling experiments and evidence records.
- Diagnosed the change-everything comparison and supplied the discriminating reset experiment.
- Completed a four-attempt one-change manual search, extension-set comparison, baseline-miss explanation, vertical/near-vertical check, and all five reflections.
- Completed the practical threshold extension and explained what changes without retraining.

## Expected Result Checks

| Contract | Observed reference evidence |
|---|---|
| Baseline | `10/12 = 0.8333`; exactly two misses |
| Manual checkpoint | Selected final controlled attempt `weights=[1.0, 2.0]`, `bias=-0.2`; fixed `12/12`, extension `40/40` |
| Probability/shape | One score and probability per example; finite extreme sigmoid; values in `[0,1]` |
| Scaling | Score signs and zero contour invariant under positive common scaling; off-boundary probabilities change |
| Vertical handling | `w2=0` and `w2=1e-12` render without slope division |
| Threshold extension | Threshold `0.50 -> 0.65` changes indices `[4, 6, 8, 11]`; scores/probabilities stay fixed |

## Instructor Readiness

- Major experiments answer **what happened, why, and what concept it demonstrates**.
- Adjacent notes include likely wrong answers, staged hints, evidence to point out, and discussion prompts.
- Troubleshooting covers imports/kernel selection, matrix orientation, stable sigmoid, execution order, plotting, metrics, random changes, memory/runtime, CPU, and Colab wording.
- Acceptable alternatives include other verified separators, equivalent stable sigmoid implementations, and other threshold comparisons that hold parameters fixed.
- Recovery options use stored contours and score-sign tables without skipping prediction or debrief.

## Separation and Leakage

- Participant notebook was rescanned after solution creation.
- Participant code outputs remain empty and no `INSTRUCTOR ONLY`, `Instructor Answer`, solution filename/link, or instructor-solution path was found.
- Participant SHA-256 prefix at final scan: `5ddc67e0f9e082e6`.
- **Leakage result: NONE.**

## Issues Found and Fixes Applied

- The first solution draft selected the first of two tied `1.000` manual attempts while its explanation described the final attempt. Tie-breaking now selects the latest equally accurate attempt, preserving the controlled sequence.
- The prior participant validation narrative reported two threshold changes for an incidental completion. The canonical final solution parameters deterministically change four decisions. The participant notebook does not prescribe an exact count, so this is a non-blocking report-value discrepancy, not a participant contract defect.
- No participant file was changed and no participant requirement was weakened.

## Final Status

**PASS WITH NOTES** - complete, standalone, clean-executable, instructor-ready, and correctly separated. The only note is the non-blocking prior validation narrative discrepancy above. Hosted Google Colab execution remains unvalidated.
# PASS WITH NOTES

## Solution Validation: LAB-D2-02

### Lab and Solution

- **Lab:** `courseware/day-2/labs/LAB-D2-02-backprop-gradient-check.ipynb`
- **Solution:** `courseware/instructor-solutions/day-2/LAB-D2-02-backprop-gradient-check-SOLUTION.ipynb`
- **Objectives:** `OBJ-D2-04`, with reinforcement of `OBJ-D2-02` and `OBJ-D2-03`
- **Solution SHA-256:** `6bd54fd53c800f2a1dcd0c6ddecad0c60f0cb32be6e6ad3c852eaf1eb56fc114`
- **Final status:** **PASS WITH NOTES**

### Environment Used

- macOS on Apple silicon, local CPU
- Python 3.11.8; NumPy 2.4.6; matplotlib 3.11.1
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- Float64 gradient-check path; no GPU, network, download, or cross-notebook state

### Clean-Run Evidence

- Cleared outputs/counts and executed the canonical solution in a new `python3` kernel.
- Clean wall time including kernel startup: **1.691 s**.
- Executed **18/18 code cells**; rendered **2 PNGs**; uncaught errors: **0**.
- All **42 cells** pass nbformat validation with unique matching official/metadata IDs and correct language metadata.
- No TODO, `NotImplementedError`, skipped optional path, or blank response remains.

### Tasks and Questions Covered

- Completed gradient-sign predictions and explained the least-certain chain-rule path.
- Implemented stable sigmoid, clipped BCE, batch-first forward cache, and vectorized backpropagation.
- Interpreted what finite-difference agreement supports and what it cannot establish.
- Predicted, executed, localized, and repaired both structured bugs: output sign reversal and omitted hidden sigmoid derivative.
- Implemented a non-mutating negative-gradient update and completed the scalar perturbation challenge.
- Executed the optional epsilon sweep and explained truncation versus cancellation/rounding error.
- Added hint ladders, layer-local misconceptions, alternatives, fast recovery, and instructor discussion prompts.

### Expected Result Checks

| Contract | Clean-run evidence |
|---|---|
| Initial fixed-example loss | `0.67389837` |
| Correct analytic/numeric agreement | Maximum relative errors: W1 `1.012e-09`, b1 `3.657e-10`, W2 `1.611e-10`, b2 `7.912e-11` |
| Sign defect | Relative error `1.000` for all parameter groups |
| Missing hidden factor | W1/b1 error `0.6476`; W2/b2 remain near `1e-10` |
| Negative-gradient update | Loss `0.67389837 -> 0.64313799`; original arrays unchanged |
| Scalar perturbation | Actual/predicted change `-1.71476391e-04/-1.71491679e-04` |

### Instructor Readiness

- The notebook distinguishes conceptual sign checks, formula checks, defect localization, and update behavior rather than treating them as one proof.
- It documents valid stable-sigmoid variants, alternate scalar perturbations, and tolerance-based rather than exact-decimal grading.
- Troubleshooting covers dtype, saturation, epsilon, mutation, shape, order, CPU, and Colab differences.

### Answer Separation

- Frozen participant SHA-256 remains `45708d638d16a5529bd8e460758d2d1c9c8d512061a0d917e9c293f72aeca2ca`, exactly matching the current participant PASS report.
- No solution label, answer key, instructor-only path, stored participant output, or instructor hint appears in the participant artifact.
- **Leakage result: NONE.**

### Issues Found and Fixes Applied

- No participant contradiction or solution defect was found.
- No participant file was changed.

### Remaining Note

A hosted Google Colab CPU runtime was not executed. Float64 agreement and plots pass locally, but hosted Colab is not claimed as validated.

### Final Status

**PASS WITH NOTES** - complete, clean-executable, numerically checked, instructor-ready, and correctly separated; hosted Colab remains unvalidated.
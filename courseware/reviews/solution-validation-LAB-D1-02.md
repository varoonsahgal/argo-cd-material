# Solution Validation: LAB-D1-02

## Lab and Solution

- **Lab:** `courseware/day-1/labs/LAB-D1-02-linear-limit.ipynb`
- **Solution:** `courseware/instructor-solutions/day-1/LAB-D1-02-linear-limit-SOLUTION.ipynb`
- **Objectives:** `OBJ-D1-04`, `OBJ-D1-05`, reinforcement of `OBJ-D1-03`
- **Final status:** **PASS**

## Environment Used

- macOS on Apple silicon, local CPU
- Python 3.11.8
- NumPy 2.4.6, matplotlib 3.11.1, scikit-learn 1.9.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- No GPU, network call, download, external data file, or Lab 1 kernel state

## Clean-Run Evidence

- Cleared and executed the canonical solution in its own fresh `python3` kernel from top to bottom.
- Clean wall time, including kernel startup: **2.804 s**.
- All **17 code cells** executed; **5 PNG** outputs rendered; no uncaught errors.
- Official nbformat validation passed after execution.
- All **35 cells** retain unique matching top-level/metadata IDs and required language metadata.

## Tasks and Questions Covered

- Completed predictions for separable blobs, balanced XOR, boundary family, and failure mechanism.
- Implemented explicit `LogisticRegression` fitting and scalar accuracy.
- Completed standard-versus-long-iteration recommitment and representation diagnosis.
- Completed ReLU, stable sigmoid, `2 -> 2 -> 1` fixed forward pass, and class conversion.
- Completed clean-corner/noisy-XOR/identity predictions, linked raw-hidden visual interpretation, five-part explanation, parameter immutability check, and practical copied-`b1` extension.
- Adjacent instructor answers distinguish optimization, representation, parameter choice, and implementation failure.

## Expected Result Checks

| Contract | Observed reference evidence |
|---|---|
| Separable blobs | `1.0000` accuracy; useful straight boundary |
| XOR logistic | `0.5000` at 1,000 and 10,000 maximum iterations; same linear family |
| Fixed nonlinear network | Clean corners `1.0000`; noisy XOR `1.0000` |
| Identity control | Same data and parameters, identity hidden activation: `0.5000` |
| Shapes/ranges | Hidden `(4,2)` / `(240,2)` and probability `(4,1)` / `(240,1)`; probabilities in `[0,1]` |
| Extension | Copied hidden-bias shift: accuracy `1.000 -> 0.996`; mean absolute probability shift `0.0332673` |

The nonlinear and identity runs use the same parameter arrays and data. The notebook asserts canonical parameter immutability.

## Instructor Readiness

- Every major comparison includes **what happened, why, and the demonstrated concept**.
- Hint ladders precede reveals; wrong answers include “sigmoid bends the line” and “more iterations add regions.”
- Delivery notes identify linked point identities, the straight hidden-space output cut, and the limit of fixed-forward evidence.
- Troubleshooting covers estimator fit, seed/noise drift, parameter shapes, identity/ReLU parity, plotting, imports, execution order, runtime, memory, CPU, and Colab.
- Acceptable alternatives include bounded copied hidden offsets and equivalent stable sigmoid implementations; the core same-parameter control may not be changed.

## Separation and Leakage

- Participant outputs remain empty; no instructor status, answer label, solution link, or instructor path appears.
- Participant SHA-256 prefix at final scan: `a608f0f83a7915a4`.
- **Leakage result: NONE.**

## Issues Found and Fixes Applied

- No participant contradiction or solution-behavior defect was found.
- The canonical solution passed on its first clean execution after schema construction.
- No participant file was changed and no requirement was weakened.

## Final Status

**PASS** - complete, independently executable, instructor-ready, and correctly separated. Hosted Google Colab execution remains unvalidated.
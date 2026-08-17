# Solution Validation: LAB-D1-04

## Lab and Solution

- **Lab:** `courseware/day-1/labs/LAB-D1-04-forward-network-mystery.ipynb`
- **Solution:** `courseware/instructor-solutions/day-1/LAB-D1-04-forward-network-mystery-SOLUTION.ipynb`
- **Objectives:** `OBJ-D1-06`, `OBJ-D1-07`, retrieval of `OBJ-D1-04` and `OBJ-D1-05`
- **Final status:** **PASS**

## Environment Used

- macOS on Apple silicon, local CPU
- Python 3.11.8
- NumPy 2.4.6, matplotlib 3.11.1, scikit-learn 1.9.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- No GPU, network, download, training call, external file, or state from Labs 2/3

## Clean-Run Evidence

- Cleared and executed the canonical solution in a new `python3` kernel from the first import through the opposite-delta extension.
- Final clean wall time, including kernel startup: **2.861 s**.
- All **17 code cells** executed; **2 PNG** outputs rendered; no uncaught errors.
- Official nbformat validation passed after execution.
- All **38 cells** have unique matching IDs and required language metadata.

## Tasks and Questions Covered

- Completed exact two-probe prediction, hidden/output shape predictions, projection expectation, and revision evidence.
- Implemented stable sigmoid, hidden step, output step, complete forward cache, and class conversion.
- Completed held-out and six-probe evaluation with exact evidence.
- Predicted, executed, caught, classified, and repaired the transposed-matrix failure.
- Completed mesh forward pass, mesh/batch parity, output-aligned hidden projection, and four-panel evidence board.
- Completed one correct and one incorrect trace, failure taxonomy, evidence limit, copied `b2` perturbation, four reflections, and opposite-delta extension.

## Expected Result Checks

| Contract | Observed reference evidence |
|---|---|
| Held-out accuracy | `0.9111`, inside required `0.82-0.92` band |
| Shapes | Hidden `(90,6)`; output `(90,1)`; probe recovery `(6,6)` |
| Probability range | Finite and in `[0,1]` |
| Named probes | Exactly `4/6` correct; wrong: `east-rim` (`p=0.502`) and `east-notch` (`p=0.605`) |
| Transpose demonstration | `(6,2) @ (6,2)` reports inner-dimension `2` versus `6`; correct path recovers |
| Mesh parity | Independently recomputed batch classes exactly equal plotted mesh classes |
| Perturbation | Copied `b2 +0.20` raises all six probabilities; held-out accuracy remains `0.9111`; canonical arrays unchanged |
| Opposite extension | All six shifts negative; positive/negative probability shifts are not perfectly symmetric |

Positive-delta probe probability shifts are `[0.041332, 0.037103, 0.034547, 0.020173, 0.049811, 0.046643]`. The corresponding negative shifts are `[-0.044530, -0.040748, -0.030713, -0.023440, -0.049855, -0.048644]`.

## Instructor Readiness

- Each evidence stage answers **what happened, why, and the demonstrated concept**.
- Hint ladders, likely anthropomorphic explanations, projection overclaims, shape/prediction failure confusion, and discussion triggers are adjacent to their prompts.
- Troubleshooting covers imports, seed/split/probe drift, matrix orientation, singleton output shape, sigmoid stability, plotting, parameter mutation, execution order, metrics, runtime, memory, CPU, and Colab.
- Alternative valid perturbations and hidden projections are documented with invariants and interpretation limits.
- Stored tables/plots provide a fast live-recovery route while preserving prediction and debrief.

## Separation and Leakage

- Participant outputs remain empty and no instructor-only label, answer, or solution link appears.
- Participant SHA-256 prefix at final scan: `51829b6e07b6eeb7`.
- **Leakage result: NONE.**

## Issues Found and Fixes Applied

- Initial solution construction replaced the mesh-helper cell instead of only its assignments; the first clean run failed because `mesh_X` was undefined.
- Restored the complete mesh and hidden-projection definitions, rebuilt the canonical notebook, restarted a fresh kernel, and reran successfully.
- No participant contradiction was found and no participant file was changed.

## Final Status

**PASS** - complete, clean-executable, instructor-ready, and correctly separated. Hosted Google Colab execution remains unvalidated.
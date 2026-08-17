# PASS

## Solution Validation: LAB-D3-01

### Artifacts

- **Lab:** `courseware/day-3/labs/LAB-D3-01-find-data-leak.ipynb`
- **Solution:** `courseware/instructor-solutions/day-3/LAB-D3-01-find-data-leak-SOLUTION.ipynb`
- **Participant SHA-256:** `6a0c1905d3d0fc7fdcacd417ae303997ac5d63cccdae77ea140130f0fed43340`
- **Solution SHA-256:** `b6ed5ca29064fa05b6bc93085d2016090504410c260b178aeec35760953d2246`
- **Objectives:** `OBJ-D3-02`; reinforces `OBJ-D2-08`
- **Validation date:** 2026-08-16

### Environment Used

- macOS on Apple silicon, fresh CPU kernels
- Python 3.11.8
- NumPy 2.2.4, matplotlib 3.11.1, scikit-learn 1.9.0
- PyTorch 2.6.0 for the optional loader path
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- Generated local records; no file, cache, network, or GPU dependency

### Execution Status

- Cleared outputs, started a new kernel, and executed all `12/12` code cells in order.
- Final wall time: **3.196 seconds**.
- Uncaught errors: **0**.
- Rendered plots: **2**.
- Final checkpoint: **passed**.
- Stored notebook outputs are from this final clean run only.

### Tasks and Exercises Covered

- Completed the pre-evidence provenance prediction and named competing explanations.
- Predicted the leaky score band and distinguished proxy leakage from split-boundary leakage.
- Diagnosed the post-outcome field from availability time and the scaler defect from fitted-state ownership.
- Implemented seeded, stratified `60/20/20` splits after removing the proxy.
- Fit `StandardScaler` and `LogisticRegression` as a training-owned pipeline.
- Compared contaminated and valid ROC AUC and confusion matrices.
- Executed the practical optional PyTorch loader path.
- Answered the additional-feature challenge, reflection, and checkpoint.
- Added instructor reasoning, hint ladder, expected evidence, misconceptions, discussion prompts, alternatives, troubleshooting, and live recovery notes.

### Expected Result Checks

| Check | Final clean-run evidence | Result |
|---|---:|---|
| Leaky validation ROC AUC | `0.9960` | Passed `0.99-1.00` |
| Valid validation ROC AUC | `0.8310` | Passed `0.78-0.90` |
| Valid split sizes | `3000/1000/1000` | Passed |
| Valid feature count | `8`; proxy absent | Passed |
| Training-only scaling | train means approximately zero; validation means not all zero | Passed |
| Optional batch shapes | `(64,8)` and `(64,)` | Passed |
| Runtime | `3.196 s` | Passed `<30 s` |

The correlation plot correctly prioritizes `case_resolution_code` for audit without treating correlation as the legal/provenance decision. The comparison plot makes the lower but valid score visible.

### Runtime and Platform Notes

- CPU is the required and sufficient path; an accelerator provides no meaningful benefit for this workload.
- Seeds cover generated data, proxy noise, splits, logistic regression, and the optional loader generator.
- A hosted Colab CPU was not available. The lab has no external data dependency, but hosted execution remains unclaimed.

### Answer-Separation Check

- The participant SHA-256 exactly matches the current participant validation report.
- The Day 3 participant tree contains no instructor-solution, instructor-guide, answer-key, model-answer, or solution-notebook reference.
- No participant notebook or support artifact was edited.
- Every solution cell has a unique official ID, matching `metadata.id`, and `metadata.language`.

### Issues Found and Fixes Applied

- No participant contradiction or solution defect was found.
- Instructor-relative links were adjusted for the instructor-solution directory and all five relative links resolve.

### Final Status

**PASS** - complete, executable, separated, and instructor-ready. Hosted Colab remains an unexecuted portability note, not a local solution blocker.
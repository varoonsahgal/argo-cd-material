# PASS WITH NOTES

## Solution Validation: LAB-D3-03

### Artifacts

- **Lab:** `courseware/day-3/labs/LAB-D3-03-overfit-and-rescue.ipynb`
- **Solution:** `courseware/instructor-solutions/day-3/LAB-D3-03-overfit-and-rescue-SOLUTION.ipynb`
- **Participant SHA-256:** `1027482a1674bee5875e6c6e52febed5fd6e8770aad8ec36e73306bd51084e49`
- **Solution SHA-256:** `523719da936ea925cef8670e067da97b0cc6703d209fdb5d41be08f3cf88724c`
- **Objectives:** `OBJ-D3-04`, `OBJ-D3-05`; reinforces `OBJ-D3-01`
- **Validation date:** 2026-08-16

### Environment Used

- macOS on Apple silicon, fresh CPU kernel
- Python 3.11.8
- NumPy 2.2.4, matplotlib 3.11.1, scikit-learn 1.9.0
- PyTorch 2.6.0, torchvision 0.21.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- `ALLOW_DOWNLOAD=False`; independently loaded packaged Fashion-MNIST fallback

### Execution Status

- Cleared outputs, started a new kernel, and executed all `15/15` code cells in order.
- Final wall time: **3.924 seconds**.
- Baseline training time: **0.21 seconds**.
- Dropout training time: **0.21 seconds**.
- Uncaught errors: **0**.
- Rendered plots: **2**.
- Final checkpoint: **passed**.
- Stored notebook outputs are from this final clean run only.

### Tasks and Exercises Covered

- Completed source and trajectory predictions before model construction.
- Implemented the high-capacity model and matched-budget trainer.
- Produced and diagnosed a conspicuous tiny-data generalization gap.
- Calculated the gap and located the late validation-loss divergence.
- Executed and caught the deliberate three-remedy confound.
- Selected exactly one intervention: dropout `0.4`.
- Declared the mechanism and acceptance criterion before the remedy run.
- Compared aligned curves and correctly rejected the remedy against the declared criterion.
- Completed the optional augmentation design/validation plan without adding a second core change.
- Completed interpretation, challenge, reflection, and checkpoint responses.
- Added instructor reasoning, hint ladder, misconceptions, discussion prompts, acceptable alternatives, troubleshooting, source limits, and live recovery notes.

### Expected Result Checks

| Check | Final clean-run evidence | Result |
|---|---:|---|
| Source mode | `packaged_fashion_mnist_fallback` | Passed |
| Tiny/validation counts | `400/800` | Passed |
| Baseline parameters | `535,818` | Passed high-capacity setup |
| Baseline train/validation/gap | `0.998/0.796/0.201` | Passed all overfit gates |
| Confounded rescue | three-remedy validator raised and was caught | Passed deliberate failure |
| Dropout train/validation/gap | `0.985/0.799/0.186` | Executed |
| Acceptance rule | neither `+0.03` validation nor `-0.05` gap | Correctly rejected |

The negative result is retained as useful evidence. Dropout reduced training fit and the gap slightly, but not enough to support the predeclared success claim.

### Source-Mode Disposition

- **Executed:** independent packaged Fashion-MNIST fallback, baseline plus one matched-budget remedy.
- **Structurally present:** cache-aware and opt-in Fashion-MNIST source path.
- **Planning only:** optional training-only augmentation design.
- **Not executed or validated:** online-source metrics/runtime and hosted Colab.

### Runtime and Platform Notes

- CPU is the required baseline. GPU execution may alter runtime and reproducibility details and requires separate calibration.
- The solution is independent of `LAB-D3-02` kernel/model state.
- If live time is short, run the baseline and supplied dropout comparison and preserve the predeclared decision rule.

### Answer-Separation Check

- The participant SHA-256 exactly matches the current participant validation report.
- The Day 3 participant tree leakage scan returned zero matches.
- The packaged Fashion-MNIST SHA-256 matches `manifest.json` exactly.
- Every solution cell has a unique official ID, matching `metadata.id`, and `metadata.language`.
- All five relative links resolve.

### Issues Found and Fixes Applied

- No participant contradiction or solution defect was found.
- Instructor-relative links were adjusted for the solution directory.
- Instructor notes make the negative-result decision and fallback limits explicit.

### Final Status

**PASS WITH NOTES** - the complete offline solution is executable and instructor-ready. Online-source and hosted Colab evidence remain unvalidated.
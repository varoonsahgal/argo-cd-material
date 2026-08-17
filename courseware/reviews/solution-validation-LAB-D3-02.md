# PASS WITH NOTES

## Solution Validation: LAB-D3-02

### Artifacts

- **Lab:** `courseware/day-3/labs/LAB-D3-02-cnn-feature-maps.ipynb`
- **Solution:** `courseware/instructor-solutions/day-3/LAB-D3-02-cnn-feature-maps-SOLUTION.ipynb`
- **Participant SHA-256:** `0041ce12334e94190c4202f6513a608c7ace0190f4cee934fbb504660f35ae8f`
- **Solution SHA-256:** `7b2ace4c8bc2b11eed56aa1d93d921e327f1083cbc763312715dac699ee14310`
- **Objectives:** `OBJ-D3-01`, `OBJ-D3-03`
- **Validation date:** 2026-08-16

### Environment Used

- macOS on Apple silicon, fresh CPU kernel
- Python 3.11.8
- NumPy 2.2.4, matplotlib 3.11.1, scikit-learn 1.9.0
- PyTorch 2.6.0, torchvision 0.21.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- `ALLOW_DOWNLOAD=False`; empty Torch cache; packaged real Fashion-MNIST fallback

### Execution Status

- Cleared outputs, started a new kernel, and executed all `19/19` code cells in order.
- Final wall time: **5.198 seconds**.
- Bounded two-epoch training time: **0.81 seconds**.
- Uncaught errors: **0**.
- Rendered plots: **4**.
- Final checkpoint: **passed**.
- Stored notebook outputs are from this final clean run only.

### Tasks and Exercises Covered

- Completed source-mode, shape, filter-response, and parameter predictions.
- Executed and caught the deliberate three-channel/one-channel mismatch.
- Implemented the two-block compact CNN and classifier head.
- Calculated and asserted every intermediate shape and the flattened width.
- Trained two bounded epochs and executed the practical optional third epoch.
- Captured temporary early/later feature maps, detached them, and removed hooks.
- Displayed correctly indexed high-confidence validation errors.
- Completed interpretations, challenge responses, reflection, and checkpoint.
- Added instructor reasoning, source-mode limits, hint ladder, expected plots, misconceptions, discussion prompts, alternatives, runtime notes, and live recovery guidance.

### Expected Result Checks

| Check | Final clean-run evidence | Result |
|---|---:|---|
| Source mode | `packaged_fashion_mnist_fallback` | Passed |
| Split shapes | `3000/800/800`, each `(N,1,28,28)` | Passed |
| Training-only mean/std | `0.2862/0.3531` | Passed |
| Shape trace | ends at `(8,32,7,7)` and `(8,1568)` | Passed |
| Trainable parameters | `105,866` | Passed `<250,000` |
| Epoch 1 validation | `0.685` | Observed |
| Epoch 2 validation | `0.762` | Passed fallback threshold |
| Optional epoch validation | `0.764` | Executed |
| Captured maps | `(1,16,28,28)`, `(1,32,14,14)` | Passed; hooks removed |

The feature-map explanation remains descriptive: early maps retain finer spatial detail and later maps are coarser/selective, without assigning unsupported semantics or causal meaning.

### Source-Mode Disposition

- **Executed:** packaged real Fashion-MNIST fallback, full shape/training/hook/error-analysis mechanics.
- **Structurally present:** cache-aware and opt-in Fashion-MNIST source path.
- **Not executed or validated:** online/full split, `0.80-0.88` full-data band, full-data throughput, hosted Colab.
- The fallback result is not used to validate the online band.

### Runtime and Platform Notes

- CPU is the required release path. GPU execution may change timing and small numerical details and requires separate calibration.
- The repository support directory is required for offline execution; uploading the notebook alone to Colab is insufficient.
- If live time is lost, keep the two core epochs and omit the optional third epoch rather than replacing training evidence with saved predictions.

### Answer-Separation Check

- The participant SHA-256 exactly matches the current participant validation report.
- The Day 3 participant tree leakage scan returned zero matches.
- The packaged Fashion-MNIST SHA-256 matches `manifest.json` exactly.
- Every solution cell has a unique official ID, matching `metadata.id`, and `metadata.language`.
- All seven relative links resolve.

### Issues Found and Fixes Applied

- No participant contradiction or solution defect was found.
- Instructor-relative links were adjusted for the solution directory.
- Instructor notes explicitly prevent applying fallback metrics to the online/full-data band.

### Final Status

**PASS WITH NOTES** - the complete offline solution is executable and instructor-ready. Online/full-data and hosted Colab claims remain unvalidated.
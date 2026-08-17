# PASS WITH NOTES

## Participant Validation: LAB-D4-02

### Lab

- **Name:** Model Detective - Curves and Error Buckets
- **Participant path:** `courseware/day-4/labs/LAB-D4-02-model-detective.ipynb`
- **Canonical SHA-256:** `259d689bd44501d761f2190e4e04f9bc0caa974179536cd67cb2c95dd24d74ff`
- **Learning objectives:** `OBJ-D4-02`, `OBJ-D4-03`
- **Validation date:** 2026-08-17
- **Validation status:** **PASS WITH NOTES**
- **Interestingness:** **STRONG** - participants diagnose anonymous curves, request evidence, inspect aligned errors, define reproducible slices, resolve overlapping errors into exclusive buckets, and choose a falsifiable next experiment from prevalence and consequence.

### Environment Tested

- macOS on Apple silicon, required local CPU path
- Python 3.11.8
- NumPy 2.4.6, matplotlib 3.11.1, scikit-learn 1.9.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- Fresh temporary venv/kernel; canonical packaged artifacts; no network or prior notebook state

A hosted Google Colab session was unavailable and was not executed.

### Commands and Cells Executed

1. Validated JSON/nbformat, syntax, IDs, language metadata, clean outputs, starter response fields, TODO placement, and participant separation.
2. Ran the untouched starter in a fresh kernel. It verified both artifact checksums, rendered the anonymous loss curves, and stopped intentionally at visible **Cell 8**.
3. Built a temporary participant-completed copy without reading solution artifacts.
4. Diagnosed all four mystery bundles from at least two observations plus an alternative and evidence request.
5. Inspected aggregate accuracy, `(10,10)` confusion, directed pairs, and confidence-ranked errors.
6. Defined high-border-ink and low-total-ink slices from fixed metadata quantiles.
7. Executed exclusive bucket accounting, payoff comparison, deliberate-failure recovery, next-experiment record, optional low-confidence bucket, and final checkpoint.
8. Restarted and ran all 17 code cells; inspected all five rendered plots.

### Runtime Observed

- Untouched starter to intentional stop: **2.359 s**
- Completed Restart/Run All: **2.805 s** wall time
- Notebook checkpoint time: **0.74 s**
- Executed code cells: **17/17**
- Nonblank PNG outputs: **5**
- Uncaught completed-run errors: **0**

### What Worked

- `mystery_curves.npz` exposed only neutral IDs `M1-M4`, aligned 24-epoch curves, and no labels/configuration/diagnosis strings.
- Curve evidence supports healthy, limited-fit, widening-gap, and unstable/stalled hypotheses while requiring alternatives rather than claiming unique causes.
- Fixed digits validation accuracy was **0.9526**, inside `0.90-0.96`; confusion shape was exactly `(10,10)`.
- All 359 images, labels, sample IDs, probability rows, predictions, and confidence values aligned exactly with `load_digits()` and `argmax/max` recomputation.
- There were **17** errors and at least one high-confidence error at confidence `>=0.70`.
- The high-border slice contained `93` examples and `6` errors; low-total-ink contained `90` examples and `8` errors. Their overlap (`18`) was reported rather than hidden.
- Exclusive bucket counts were high-border `4`, high-confidence `2`, low-total `7`, and other `4`, totaling all **17** errors exactly once.
- Payoff proxies were `12` for high-border ink and `8` for low-total ink under declared severity weights.
- The largest-pair-to-bigger-model draft was explicitly rejected because frequency alone does not establish cause or remedy.
- The optional low-confidence path ran and found **6** errors without changing core accounting.
- All loss/accuracy, confusion, gallery, and payoff plots contained nonblank pixels and correctly indexed labels/predictions.

### Failures Encountered

- The starter stopped intentionally at the curve-diagnosis gate.
- The unsupported "largest pair -> bigger model" draft failed intentionally and recovered to a quantified, falsifiable experiment.
- No unintended checksum, alignment, slice, accounting, plotting, runtime, or checkpoint failure occurred.

### Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Mystery bundles | Four neutral bundles, no labels/configs | `M1-M4`, passed |
| Digits accuracy | `0.90-0.96` | **0.9526** |
| Confusion shape | `(10,10)` | **(10,10)** |
| High-confidence errors | At least one | **1** at `>=0.70` |
| Index/probability alignment | Exact | Passed |
| Slice/bucket accounting | Reproducible; all errors accounted | **17/17** exactly once |
| Runtime | Core under 30 s | **2.805 s** completed wall time |

### Reproducibility and Colab Concerns

- The default lab loads compact, checksum-verified local artifacts and performs no training or download.
- Artifact keys/dtypes are pickle-free and practical for hosted CPU notebooks when the shared Day 4 data directory is uploaded with the notebook.
- A notebook uploaded alone cannot resolve repository-relative artifacts; the shared environment guide documents that requirement.
- No hosted Colab execution claim is made.

### Required Fixes

None for the participant notebook or packaged evidence.

### Optional Improvements

None required. Multiple diagnosis and intervention alternatives are explicitly supported by the evidence-request and disconfirming-evidence prompts.

### Retest Requirements

- Run the completed notebook with its support directory in hosted Colab before claiming hosted readiness.
- Retest after changes to artifact hashes/schema, curve bundles, sample ordering, probabilities, confidence thresholds, slice metadata, bucket precedence, links, or metadata.
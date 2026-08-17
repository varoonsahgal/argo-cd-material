# PASS WITH NOTES

## Participant Validation: LAB-D3-01

### Lab

- **Name:** Find the Data Leak
- **Participant path:** `courseware/day-3/labs/LAB-D3-01-find-data-leak.ipynb`
- **Canonical SHA-256:** `6a0c1905d3d0fc7fdcacd417ae303997ac5d63cccdae77ea140130f0fed43340`
- **Learning objective:** `OBJ-D3-02`, with reinforcement of `OBJ-D2-08`
- **Validation date:** 2026-08-16
- **Validation status:** **PASS WITH NOTES**
- **Interestingness:** **STRONG** - participants commit a provenance prediction, expose two independent leak paths, repair ownership and split order, compare contaminated and valid evidence, and defend why the lower score is more trustworthy.

### Environment Tested

- macOS on Apple silicon, required CPU path
- Python 3.11.8
- NumPy 2.2.4, matplotlib 3.11.1, scikit-learn 1.9.0
- PyTorch 2.6.0 only for the optional `DataLoader` path
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- Generated local data; no network, download, GPU, or prior notebook state

A hosted Google Colab session was not available. This report validates the local CPU path and assesses Colab practicality; it does not claim a hosted Colab execution.

### Commands and Cells Executed

1. Parsed the canonical file with standard JSON and official nbformat validation.
2. Parsed every code cell with Python `ast` and checked official IDs, matching `metadata.id`, `metadata.language`, execution counts, stored outputs, participant response state, and forbidden participant-to-instructor references.
3. Ran the untouched canonical notebook in a fresh kernel. It stopped intentionally at visible **Cell 4**, before data generation or fitting, with `Prediction gate: complete the provenance audit before generating or fitting anything.` No later cell executed.
4. Built a temporary participant-completed copy from the canonical notebook without opening or importing any instructor solution.
5. Completed every prediction, diagnosis, implementation, challenge, reflection, and the practical optional loader path.
6. Restarted the kernel and ran all 12 code cells in order.
7. Rendered and inspected the feature-correlation plot and the leaky-versus-valid AUC/confusion-matrix comparison.
8. Resolved prerequisite, activity, Student Guide debrief, and continuation links.

### Runtime Observed

- Untouched starter to intentional stop: **19.660 s** wall time, including first-kernel startup/import overhead
- Final completed Restart Kernel -> Run All: **3.372 s** wall time
- Executed code cells: **12/12**
- Rendered PNG outputs: **2**
- Uncaught errors in completed run: **0**
- Notebook checkpoint runtime assertion: passed under **30 s**

### What Worked

- The participant sees provenance and must respond before records or model evidence are generated.
- Both leak paths are independently discoverable:
  - `case_resolution_code` is explicitly marked as created after closure and unavailable at prediction time.
  - `StandardScaler.fit(X_leaky)` occurs before the train/validation split.
- The deliberate leaky path executed and produced ROC AUC **0.9960**, inside the required `0.99-1.00` band.
- The correlation plot made the post-outcome proxy conspicuous at approximately `0.98` correlation without presenting correlation alone as proof.
- The participant repair removed the ninth proxy feature before splitting.
- Two seeded, stratified split stages produced `3,000/1,000/1,000` train/validation/test examples.
- Class proportions remained within the notebook's `<0.01` tolerance across splits.
- A `Pipeline` containing `StandardScaler` and `LogisticRegression` was fit only on training data.
- The valid validation ROC AUC was **0.8310**, inside the required `0.78-0.90` range.
- Scaled training means were numerically zero; scaled validation means were not all zero, supporting train-only scaler ownership.
- The test split remained outside model-selection evidence.
- The optional loader path executed with batch shapes `(64,8)` and `(64,)`; training alone shuffled.
- The final visual showed the expected score reduction and materially less perfect confusion matrix without implying the valid model was deployment-ready.
- The final checkpoint passed.

### Failures Encountered

- The untouched starter stopped intentionally at the first prediction gate.
- The deliberately contaminated pipeline produced the suspiciously strong metric as designed.
- No unintended syntax, split, metric-band, scaling, plotting, link, or recovery failure occurred.

### Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Leaky ROC AUC | `0.99-1.00` | **0.9960** |
| Valid ROC AUC | `0.78-0.90` | **0.8310** |
| Valid feature count | `8`; proxy absent | **8**, passed |
| Valid split | Stratified `60/20/20` | `3000/1000/1000`, passed |
| Scaler ownership | Train means near zero; validation not exactly zero | Passed |
| Optional loader | `(64,8)` features, `(64,)` targets | Passed |
| Completed runtime | Under 30 s CPU | **3.372 s** wall time |

### Reproducibility and Colab Concerns

- The dataset generator, both split stages, and logistic regression use the supplied seed.
- The lab has no external files, downloads, GPU assumptions, or mutable cache.
- Memory and runtime are comfortably practical for a typical Colab CPU.
- A real hosted Colab session was not executed, so Colab readiness remains an evidence-based expectation rather than a validated claim.

### Required Fixes

None for the participant notebook.

### Optional Improvements

None required. The optional PyTorch loader check is correctly isolated from the core checkpoint.

### Retest Requirements

- Run the untouched starter and completed path in a fresh hosted Colab CPU session before labeling the lab Colab-validated.
- Retest after changes to the generator seed, proxy construction, split proportions, stratification, scaler/model pipeline, AUC bands, prediction ordering, links, or notebook metadata.

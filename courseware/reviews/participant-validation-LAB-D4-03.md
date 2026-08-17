# PASS WITH NOTES

## Participant Validation: LAB-D4-03

### Lab

- **Name:** You Get One Experiment
- **Participant path:** `courseware/day-4/labs/LAB-D4-03-one-experiment.ipynb`
- **Canonical SHA-256:** `bd32475e6cdd08db0b1c552c218472536b50596c20b191d2ece6b9420b0d207e`
- **Learning objectives:** `OBJ-D4-04`, `OBJ-D4-05`, `OBJ-D4-06`
- **Validation date:** 2026-08-17
- **Validation status:** **PASS WITH NOTES**
- **Interestingness:** **STRONG** - participants commit a falsifiable hypothesis, pass a machine-enforced one-change gate, run fresh reproductions, preserve a negative result, serialize a complete record, and defend quality/resource evidence.

### Environment Tested

- macOS on Apple silicon, required local CPU path
- Python 3.11.8
- NumPy 2.4.6, matplotlib 3.11.1, scikit-learn 1.9.0, PyTorch 2.6.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- Fresh temporary venv/kernel; `torch.set_num_threads(1)`; no network, GPU, or prior state

A hosted Google Colab session was unavailable and was not executed.

### Commands and Cells Executed

1. Validated JSON/nbformat, syntax, IDs, metadata, clean outputs, response fields, TODOs, and participant separation.
2. Ran the untouched starter in a fresh kernel. It loaded the fixed split/baseline and stopped intentionally at visible **Cell 8** before experiment selection.
3. Built a temporary participant-completed copy without reading solution artifacts.
4. Triggered the supplied width/optimizer/learning-rate confounded draft and confirmed rejection before training.
5. Changed exactly one major factor: learning rate `0.003 -> 0.001`.
6. Executed two fresh same-seed runs, then a separately labeled optional seed-variation run.
7. Completed the serializable ledger, checkpoint identity, hypothesis decision, deployment challenge, and reflection.
8. Restarted and ran all 16 code cells; inspected both plots.

### Runtime Observed

- Untouched starter to intentional stop: **6.417 s**
- Completed Restart/Run All: **4.527 s** wall time
- Notebook checkpoint time including three bounded runs: **1.11 s**
- Primary training time: **0.092 s**
- Executed code cells: **16/16**
- Nonblank PNG outputs: **2**
- Uncaught completed-run errors: **0**

### What Worked

- Fixed split hash matched `c9a534c56d9b1bb069bc2295d7adf87517e34b69ea9a5b046b79a3b29470b3d9`.
- Baseline validation accuracy was **0.8969**, inside `0.88-0.94`; macro-F1 was **0.8940**.
- The confounded draft raised the expected diagnostic listing `hidden`, `optimizer_name`, and `learning_rate`.
- The bounded menu authorized exactly `learning_rate`; split, architecture, optimizer, batch size, epochs, and seed remained fixed.
- Two freshly constructed model/optimizer/loader runs matched exactly: accuracy difference `0.0`, macro-F1 difference `0.0`, both within the `0.02` tolerance.
- The intervention produced accuracy **0.8496** and macro-F1 **0.8445**, a useful negative result under the fixed seven-epoch budget. The checkpoint passed without requiring improvement.
- The optional alternate seed produced accuracy **0.7911** and was correctly framed as sensitivity evidence, not same-seed reproduction.
- The record serialized through JSON with split hash, source, seed, device, package versions, full config, changed factor, primary/repeat metrics, training time, parameter count/bytes, latency method, and checkpoint identity.
- Parameter evidence was **2,410 parameters / 9,640 bytes**.
- Batch-1 latency used **20 warmups and 100 repeats**: median **0.01065 ms**, p90 **0.01305 ms**.
- The aligned quality and quality/resource plots were nonblank.

### Failures Encountered

- The starter stopped intentionally at the hypothesis gate.
- The three-change draft failed intentionally before compute.
- The selected intervention materially reduced validation quality. This is an accepted, informative negative result rather than a lab failure.
- No unintended split, reproduction, serialization, resource, runtime, plotting, or checkpoint failure occurred.

### Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Baseline accuracy | `0.88-0.94` | **0.8969** |
| One-major-change gate | Reject confounded draft | Passed; three fields reported |
| Fresh repeats | Accuracy/F1 difference `<=0.02` | **0.0 / 0.0** |
| Negative result allowed | Complete evidence can reject intervention | Passed; **0.8496** accuracy |
| Record | Complete and JSON serializable | Passed |
| Resource method | Bytes + warmed repeated batch-1 latency | **9,640 B**, `20/100` timing |
| Runtime | Under 8 min | **4.527 s** completed wall time |

### Reproducibility and Colab Concerns

- Each run resets Python, NumPy, and PyTorch seeds and creates fresh model, optimizer, and shuffled loader state.
- CPU-only digits training is far below the live budget and has no network dependency.
- Exact latency is hardware-specific; the method and environment are recorded, and no production latency claim is made.
- No hosted Colab execution claim is made.

### Required Fixes

None for the participant notebook.

### Optional Improvements

None required. The observed regression demonstrates that the success criterion correctly rewards information quality rather than mandatory score improvement.

### Retest Requirements

- Run a completed path in hosted Colab CPU before claiming hosted readiness.
- Retest after changes to the split, baseline artifact, seeds, intervention menu, major-field gate, run reset, tolerance, ledger schema, timing method, plots, links, or metadata.
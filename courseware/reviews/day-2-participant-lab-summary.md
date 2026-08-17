# PASS WITH NOTES

## Day 2 Participant Lab Validation Summary

### Retest Scope

This 2026-08-17 retest covers the exact current canonical participant bytes for `LAB-D2-01`, `LAB-D2-02`, and `LAB-D2-03`. The hashes and results below were recomputed directly; prior hashes and source-unchanged claims were not used. `LAB-D2-04` was outside this retest and is not reclassified here.

### Status Matrix

| Lab | Current status | Interestingness | Current canonical SHA-256 | Completed clean run | Key current evidence |
|---|---|---|---|---:|---|
| `LAB-D2-01` | **PASS WITH NOTES** | **STRONG** | `d7ee72d824676ae32c6eac8f55693fb48c3b91d8f398fdfadb0dec5f95560400` | **1.596 s** | A/B accuracy `1.00`, BCE `0.164252/0.554331`; four rate regimes, clipped endpoint recovery, optional curvature path |
| `LAB-D2-02` | **PASS WITH NOTES** | **STRONG** | `a2cfee7ba3f9597d54a098bcf7e835d6069ec51927aea72638dcfda0d3e73143` | **1.602 s** | Max relative error `1.012e-09`; two defect signatures; loss `0.67389837 -> 0.64313799`; optional epsilon sweep |
| `LAB-D2-03` | **PASS WITH NOTES** | **STRONG** | `d1e427ffbcb40bbe2f81702d096dc859ac841e7627e83c20ff87577bf1a24089` | **3.946 s** | Initial BCE `0.686020`; final train/val loss `0.1857/0.1820`; accuracy `0.915/0.905`; bounded failures and optional width path |

All three retested labs are classroom-ready on the tested local CPU environment. The only nonblocking note is that a hosted Google Colab CPU runtime was not executed.

### Environment

- macOS on Apple silicon, local CPU; Python 3.11.8
- NumPy 2.4.6, matplotlib 3.11.1, scikit-learn 1.9.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- No GPU, network, dataset download, or state carried between notebooks

### Execution Coverage

For every retested lab independently:

1. Parsed current raw JSON and ran official nbformat schema validation.
2. Syntax-checked every Python cell and confirmed zero canonical stored outputs/execution counts.
3. Verified unique official IDs exactly equal unique `metadata.id` values and checked complete language metadata.
4. Audited participant leakage, instructor/solution paths, network calls, file dependencies, and local links.
5. Ran an exact untouched temporary copy in a new kernel and reproduced its intentional prediction stop.
6. Built a fresh learner-completed copy from the current starter and ran Restart Kernel -> Run All with `allow_errors=False`.
7. Executed deliberate failures/recovery evidence, optional branches, plots, and final checkpoints.
8. Visually inspected every plot, checked each PNG was nonblank, and confirmed canonical hashes were unchanged after execution.

### Untouched and Completed Runs

| Lab | Untouched stop | Completed cells | Plots | Uncaught errors |
|---|---|---:|---:|---:|
| `LAB-D2-01` | Cell 7 prediction checkpoint, **1.295 s** | `16/16` | 1 | 0 |
| `LAB-D2-02` | Cell 7 prediction checkpoint, **1.224 s** | `18/18` | 2 | 0 |
| `LAB-D2-03` | Cell 8 prediction checkpoint, **2.181 s** | `23/23` | 4 | 0 |

### Contract Results

- **D2-01:** clipped BCE finite; equal accuracy/different loss visible; all four deterministic learning-rate regimes correct; divergence remains visible on aligned/log axes.
- **D2-02:** float64 `2 -> 2 -> 1`; analytic/numeric error far below `1e-5`; sign and missing-factor signatures are distinct; negative-gradient update lowers loss.
- **D2-03:** seeded/stratified 800 moons; training-only standardization; `2 -> 8 -> 1`; initial/final loss and accuracy bands pass; no-activation and excessive-rate evidence differ.

### Integration and Leakage

- Current Student Guide launch links and lab headings are present for all three retested notebooks.
- Current `ACT-D2-01`, `ACT-D2-02`, and `ACT-D2-03` headings are present and all notebook links resolve.
- The environment contract lists the correct CPU/package requirements and runtime targets.
- Prediction/evidence/source ordering passed for every notebook.
- Canonical notebooks have no stored outputs, hidden answers, instructor/solution paths, external files, or network calls.
- Canonical participant notebooks were not modified; temporary completions were written only under `$TMPDIR`.

### Current Supporting Artifact Hashes

| Artifact | Current SHA-256 |
|---|---|
| `courseware/day-2/student-guide/day-2-student-guide.md` | `1cab7b92e5c4ee8339c447e6476edacb872aa4fc77415b6e4ad536b266a64e69` |
| `courseware/day-2/challenges/day-2-challenges.md` | `1f6246bef162a399565c1902d68b27581e4ff8632940c3d4363c7e6e879ebc53` |
| `courseware/shared/environment.md` | `65a661c24dfa8e9bfed4ad3ab9e9c873976e3ee8dfb2ceb348d3618357ef19e5` |

### Remaining Notes

A hosted Google Colab CPU runtime was not executed. Do not label these three labs hosted-Colab-validated until that path is run.

### Detailed Reports

- `courseware/reviews/participant-validation-LAB-D2-01.md`
- `courseware/reviews/participant-validation-LAB-D2-02.md`
- `courseware/reviews/participant-validation-LAB-D2-03.md`

### Retest Requirements

- Run all three completed paths and deliberate failure/recovery branches in a fresh hosted Colab CPU runtime before upgrading hosted readiness.
- Recompute hashes and rerun the affected structural, link, untouched-stop, completed-copy, optional, plot, checkpoint, range, and runtime checks after any canonical notebook or linked support-artifact change.
# Day 1 Participant Lab Validation Summary

**Current validation status: PASS WITH NOTES**

## Gate Result

The repaired Day 1 participant package passed the required second execution gate on the validated local CPU environment. All four primary labs are **PASS WITH NOTES** with no release-blocking participant defect.

| Lab | Canonical SHA-256 | Status | Interestingness | Completed runtime | Key evidence |
|---|---|---|---|---:|---|
| `LAB-D1-01` | `5ddc67e0f9e082e672fa5c4e34bf74beb2f946f9b08f75651bd2978342a02b0a` | **PASS WITH NOTES** | **STRONG** | 2.421 s | Baseline `10/12`, manual `12/12`, extension `40/40`, scaling invariance, vertical/near-vertical contours |
| `LAB-D1-02` | `a608f0f83a7915a4a683dbca0cb53ad7c47bb9a8a0322bdacf6471e8734ceb8d` | **PASS WITH NOTES** | **STRONG** | 3.094 s | Blobs `1.000`, XOR `0.500`, nonlinear `1.000`, same-parameter identity `0.500` |
| `LAB-D1-03` | `8dc99076c5aaba05673f7c6d5388e1bc519f33dc366ac592b91bfbc33f61511e` | **PASS WITH NOTES** | **STRONG** | Core 1.753 s; optional 1.422 s | 67 parameters, `(5,8)`/`(5,3)`, stable softmax, wrong-axis failure/recovery, all-zero current ReLU region |
| `LAB-D1-04` | `51829b6e07b6eeb79152fbc5f358fce49d017924967c330073ff3c825ac1f44e` | **PASS WITH NOTES** | **STRONG** | 3.382 s | Accuracy `0.9111`, exact `4/2` probes, transpose recovery, mesh parity, immutable copied perturbation |

The D1-03 core and optional values are separate execution-path runtimes; no combined runtime is reported.

## Setup Readiness

- **Local CPU readiness:** **READY**
- **Google Colab hosted execution:** **NOT YET VALIDATED**

`courseware/shared/pre-course-readiness.ipynb` was parsed and validated, then executed from a fresh local kernel in **3.313 s**. It produced the expected `(5,3)` dense shape, a visible labeled PNG plot, logistic-regression accuracy `1.000`, all ordered `PASS` messages, and the final `READY` message.

All five notebooks have valid nbformat JSON, Python syntax, `metadata.language` on every cell, and unique `metadata.id` values matching official cell IDs. The readiness notebook has 11 cells; the canonical primary labs have 31, 28, 33, and 29 cells respectively. The independently validated D1-03 strict core-only path has 29 cells.

The local environment matched the documented pins: Python 3.11.8, NumPy 2.4.6, matplotlib 3.11.1, scikit-learn 1.9.0, nbformat 5.11.0, nbclient 0.11.0, and ipykernel 7.3.0. No notebook required network access, a dataset download, GPU hardware, a local data file, or state from another notebook.

The hosted Colab path was not executable from this local QA session. No Colab-ready claim is made until readiness plus all four temporary participant-completed paths run in a fresh Colab CPU runtime.

## Execution Method

For each primary notebook independently:

1. The canonical starter ran from a fresh kernel and stopped at its first prediction commitment before revealing results.
2. A temporary copy with only prediction fields completed stopped at the first learner implementation TODO with the intended targeted `NotImplementedError`.
3. A separate temporary participant-completed copy completed every required TODO and written checkpoint without changing canonical files.
4. The completed copy restarted and ran top to bottom with notebook assertions and tester-only behavior checks.
5. Required plots were extracted and visually inspected.
6. Optional paths were exercised where practical: D1-01 threshold variation, D1-02 copied hidden-bias offset, D1-03 Leaky-ReLU slope, and D1-04 opposite perturbation delta.

## Integration and Leakage

- All Student Guide notebook launch links resolve.
- All four notebook debrief links resolve to real Student Guide anchors.
- Notebook prerequisite ID sets exactly match the lab map.
- All notebook-local participant links resolve; no broken local link was found.
- Canonical notebooks contain no stored outputs, hidden cells/outputs, completed TODO bodies, solution labels, answer keys, instructor-only links, network calls, or GPU code.
- Interactivity is learner-edited and plot-driven; no widget, browser, or local-server dependency exists.

## Non-Blocking Notes

- Some fixed-point/probe labels overlap in D1-01, D1-02, and D1-04 plots. The evidence remains readable, but small offsets would improve presentation.
- The repository should retain the current local-only wording until a real Colab CPU run passes.
- `git` was unavailable in the validation shell, so worktree status could not be queried. Testing wrote completed notebook copies and rendered images only under `$TMPDIR`; canonical participant notebooks were not edited.

## Detailed Reports

- `courseware/reviews/participant-validation-LAB-D1-01.md`
- `courseware/reviews/participant-validation-LAB-D1-02.md`
- `courseware/reviews/participant-validation-LAB-D1-03.md`
- `courseware/reviews/participant-validation-LAB-D1-04.md`

## Release Disposition

The Day 1 participant package may proceed past the participant execution gate. Overall course release still requires the separate instructor-solution gate defined by the lab map.
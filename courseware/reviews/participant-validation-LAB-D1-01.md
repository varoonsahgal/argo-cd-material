# Participant Validation: LAB-D1-01

**Current validation status: PASS WITH NOTES**

## Lab

- **Name:** One-Neuron Boundary Workshop
- **Participant path:** `courseware/day-1/labs/LAB-D1-01-neuron-boundary.ipynb`
- **Canonical SHA-256:** `5ddc67e0f9e082e672fa5c4e34bf74beb2f946f9b08f75651bd2978342a02b0a`
- **Learning objectives:** `OBJ-D1-01`, `OBJ-D1-02`, `OBJ-D1-03`
- **Interestingness:** **STRONG** - participants predict, implement, isolate variables, compare visual evidence, conduct a reasoned manual search, diagnose ambiguous changes, and test a vertical-boundary failure mode.

## Environment Tested

- macOS on Apple silicon, local CPU
- Python 3.11.8
- NumPy 2.4.6
- matplotlib 3.11.1
- scikit-learn 1.9.0
- nbformat 5.11.0
- nbclient 0.11.0
- ipykernel 7.3.0 / `python3` kernel
- No GPU, network call, download, or cross-notebook kernel state was used.

These versions match the local pins in `courseware/shared/environment.md`.

## Commands and Cells Executed

1. Parsed the canonical file with `json`, validated it with `nbformat`, and parsed every code cell with `ast`.
2. Ran the canonical starter from a fresh kernel. Cell 7 stopped at the required empty prediction checkpoint before any neuron result was revealed.
3. Filled only the prediction commitments in a temporary copy and restarted. Cell 11 stopped at the first implementation TODO with the targeted `NotImplementedError` for `weighted_sum`.
4. Created a separate temporary participant-completed copy under `$TMPDIR`; completed every prediction, TODO, diagnosis, attempt-history, and reflection field without modifying the canonical file.
5. Restarted and executed the completed copy from top to bottom with `NotebookClient`.
6. Ran tester-only assertions for extreme sigmoid inputs, threshold variation, affine score scaling, fixed/extension accuracy, vertical and near-vertical coefficients, and canonical shape/range contracts.
7. Inspected all six rendered plots, including isolated parameter comparisons, manual-search evidence, and vertical-boundary views.
8. Checked stored outputs, hidden metadata, solution terms, instructor links, network/GPU code, Student Guide launch/debrief anchors, and prerequisite IDs.

## Runtime Observed

- Canonical starter to prediction checkpoint: **1.307 s**
- Prediction-complete starter to first implementation TODO: **1.460 s**
- Temporary completed clean run plus tester checks: **2.421 s**
- Rendered PNG outputs: **6**
- Uncaught errors in completed run: **0**

The compute path is comfortably below the planned 10-second target. Participant reasoning and discussion, not computation, account for the 40-minute live allocation.

## What Worked

- Raw JSON, official nbformat schema, and Python syntax passed.
- All **31 cells** have `metadata.language` and unique `metadata.id`; nested IDs match official cell IDs.
- The prediction gate blocks result reveal until every field is non-empty.
- The next stop is a clear learner-owned TODO rather than an undefined variable or accidental error.
- The completed implementation preserves `(n_examples,)` score/probability shapes, returns integer classes, and remains finite at sigmoid inputs `[-1000, 0, 1000]`.
- The supplied baseline reproduced **10/12 = 0.8333** with exactly two misses.
- The controlled manual path reached **12/12 = 1.0000** on fixed points and **40/40 = 1.0000** on the seeded extension while retaining prior attempts and reasons.
- Isolated `w1` and `w2` changes visibly rotate the contour; bias translation preserves orientation.
- Common positive scaling preserves score signs and the zero/0.5 contour while changing off-boundary probabilities.
- Vertical `w2=0` and near-vertical `w2=1e-12` contours render without slope division.
- The deliberately ambiguous change-everything path runs and is explicitly diagnosed as non-attributable.
- The optional threshold path executed; increasing the threshold to `0.65` changed two fixed-point class decisions without changing the probability field.
- Canonical source has no stored outputs, hidden cells, completed TODOs, solution terms, instructor-only links, network calls, or GPU code.
- Student Guide launch/debrief links and all six notebook-local links resolve; prerequisites exactly match `LESSON-D1-01`, `LESSON-D1-02`, and `ACT-D1-01`.

## Failures Encountered

- No canonical, learner-completion, deliberate-failure-recovery, metadata, leakage, or core-behavior defect was found.
- One tester-only assertion initially assumed extension accuracy `0.975`; the seeded run produced `1.0000`. The assertion was corrected to validate the documented contract rather than an invented exact score, then the temporary copy passed cleanly.

## Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Baseline behavior | Two near-boundary misses; at least 10/12 correct | Exactly two misses; `10/12` |
| Manual checkpoint | At least 10/12 | `12/12` |
| Seeded extension | Separate evidence, range `[0,1]` | `40/40`; reported separately |
| Probability contract | Shape `(n,)`, values in `[0,1]` | Passed for probes, fixed points, mesh, and extremes |
| Scaling | Same zero contour/signs; changed off-boundary probabilities | Passed numerically and visually |
| Vertical boundary | No divide-by-zero | Vertical and near-vertical plots rendered |
| Optional threshold | Decisions may change; probability field does not | Two decisions changed at `0.65` |

## Reproducibility and Colab Concerns

- Local CPU reproducibility passed with the supplied seed and no external files.
- Arrays and meshes are small; no memory, runtime, package-restart, or device concern appeared.
- The notebook uses standard NumPy/matplotlib APIs and has no local path dependency.
- A real Google Colab CPU execution was not available in this retest. This report validates local CPU practicality and does **not** upgrade the repository's hosted Colab status.

## Required Fixes

None. No release-blocking participant defect remains.

## Optional Improvements

- Avoid annotating the same fixed-point index twice in plots that request `annotate=True`; the current overlap is readable but visually dense.
- A hosted Colab CPU smoke run remains desirable before making an explicit Colab-validated claim.

## Retest Requirements

- Retest after any change to data, seed, baseline parameters, TODO signatures, prediction gates, contour helper, checkpoint assertions, or metadata.
- Hosted Colab validation should rerun readiness and this completed path from a new CPU runtime.

## Prior Failure Disposition

The prior blocking findings are resolved: the notebook is no longer truncated, all required experiment/recovery/debrief stages exist, strict cell metadata is present, prediction is gated, and prerequisite/debrief links resolve.

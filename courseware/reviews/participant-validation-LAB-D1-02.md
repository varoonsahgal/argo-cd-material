# Participant Validation: LAB-D1-02

**Current validation status: PASS WITH NOTES**

## Lab

- **Name:** The Linear Limit
- **Participant path:** `courseware/day-1/labs/LAB-D1-02-linear-limit.ipynb`
- **Canonical SHA-256:** `a608f0f83a7915a4a683dbca0cb53ad7c47bb9a8a0322bdacf6471e8734ceb8d`
- **Learning objectives:** `OBJ-D1-04`, `OBJ-D1-05`, reinforcement of `OBJ-D1-03`
- **Interestingness:** **STRONG** - the lab establishes a success control, makes learners commit to an XOR prediction, distinguishes optimization from representation, and isolates nonlinearity with a same-data/same-parameter identity control.

## Environment Tested

- macOS on Apple silicon, local CPU
- Python 3.11.8
- NumPy 2.4.6
- matplotlib 3.11.1
- scikit-learn 1.9.0
- nbformat 5.11.0
- nbclient 0.11.0
- ipykernel 7.3.0 / `python3` kernel
- No GPU, network call, download, or Lab 1 kernel state was used.

## Commands and Cells Executed

1. Parsed canonical JSON, ran official nbformat validation, and syntax-checked every code cell.
2. Ran the canonical starter in a fresh kernel. Cell 7 stopped at the prediction checkpoint before fitting.
3. Filled only prediction fields in a temporary copy and restarted. Cell 10 stopped at the first estimator TODO with its targeted `NotImplementedError`.
4. Built a temporary participant-completed copy under `$TMPDIR`; completed every prediction, TODO, diagnosis, and explanation field.
5. Restarted and ran the completed copy from top to bottom.
6. Tested blob and XOR fits, the 1,000/10,000-iteration comparison, clean corners, noisy XOR, ReLU and identity controls, raw/hidden plots, region meshes, parameter immutability, and the copied-`b1` extension.
7. Algebraically reconstructed the identity-activation logit and compared it with the network output to verify same-parameter affine collapse.
8. Scanned canonical source and Student Guide integration for leakage, hidden dependencies, invalid links, and prerequisite mismatches.

## Runtime Observed

- Canonical starter to prediction checkpoint: **2.356 s**
- Prediction-complete starter to first implementation TODO: **2.544 s**
- Temporary completed clean run plus tester checks: **3.094 s**
- Rendered PNG outputs: **5**
- Uncaught errors in completed run: **0**

The completed compute path is below the planned 20-second target.

## What Worked

- All **28 cells** pass JSON/nbformat/syntax checks and contain required `metadata.language` plus unique matching `metadata.id` values.
- Prediction checkpoints precede fitting, the longer-iteration reveal, and the fixed-parameter reveal.
- The blob success control reached **1.0000** accuracy with a visibly linear useful boundary.
- Logistic regression on balanced noisy XOR reached **0.5000** at both 1,000 and 10,000 iterations; both plots remain in the same linear boundary family.
- The fixed ReLU network reached **1.0000** on clean corners and **1.0000** on the noisy XOR samples.
- Replacing only ReLU with identity, while retaining the same data and parameters, returned **0.5000**.
- The direct affine reconstruction exactly matched the identity-network probabilities.
- Raw and hidden plots preserve class styles and clean-corner labels; the hidden output boundary remains a straight cut in transformed coordinates.
- Region mesh predictions agree with the same forward function used for sample metrics.
- A copied `b1` perturbation changed outputs without mutating canonical parameters.
- Canonical source has no stored outputs, hidden cells, solution/instructor links, network calls, or GPU code.
- Student Guide launch/debrief links and all notebook links resolve; prerequisites exactly match `LESSON-D1-03` and `LAB-D1-01`.

## Failures Encountered

No execution, metadata, leakage, deliberate-control, metric-band, or core-behavior failure was encountered.

## Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Separable blobs | `0.95-1.00` | `1.0000` |
| Balanced XOR logistic | `0.45-0.60` | `0.5000` |
| Larger iteration budget | Still linear and near chance | `0.5000`; same boundary family |
| ReLU clean corners | `1.00` | `1.0000` |
| ReLU noisy XOR | Above `0.90` | `1.0000` |
| Identity, same parameters | Roughly chance | `0.5000` |
| Parameter parity | Canonical arrays unchanged | Passed |

## Reproducibility and Colab Concerns

- Generated data, explicit estimator settings, and the supplied seed reproduced all bands locally.
- The notebook is CPU-only, small, independent, and contains no downloads or file-path assumptions.
- The fitted logistic models use scikit-learn 1.9.0 behavior in the validated environment.
- No real Google Colab CPU session was available, so hosted compatibility remains unclaimed rather than inferred.

## Required Fixes

None. No participant blocker remains.

## Optional Improvements

- The clean-corner labels overlap dense hidden-space points in places. Small label offsets would improve visual scanning without changing behavior.
- Run the package once in a new Colab CPU runtime before labeling the hosted path validated.

## Retest Requirements

- Retest if the seed, cluster noise, estimator settings, fixed parameters, activation comparison, metric bands, or plotting helper changes.
- Recheck exact parameter/data parity whenever the identity control is edited.

## Prior Failure Disposition

The prior empty-notebook failure is fully resolved. The participant starter, prediction sequence, data, model controls, visual comparisons, checkpoints, troubleshooting, extension, metadata, and cross-links are now present and executable.

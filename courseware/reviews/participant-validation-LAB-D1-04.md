# Participant Validation: LAB-D1-04

**Current validation status: PASS WITH NOTES**

## Lab

- **Name:** Build a Network That Thinks Forward / Forward Network Mystery
- **Participant path:** `courseware/day-1/labs/LAB-D1-04-forward-network-mystery.ipynb`
- **Canonical SHA-256:** `51829b6e07b6eeb79152fbc5f358fce49d017924967c330073ff3c825ac1f44e`
- **Learning objectives:** `OBJ-D1-06`, `OBJ-D1-07`, retrieval of `OBJ-D1-04` and `OBJ-D1-05`
- **Interestingness:** **STRONG** - learners commit to mystery probes, assemble the forward pass, diagnose an interface failure, reconcile four evidence views, trace correct and incorrect cases, and run a controlled copied-parameter perturbation.

## Environment Tested

- macOS on Apple silicon, local CPU
- Python 3.11.8
- NumPy 2.4.6
- matplotlib 3.11.1
- scikit-learn 1.9.0
- nbformat 5.11.0
- nbclient 0.11.0
- ipykernel 7.3.0 / `python3` kernel
- No GPU, network, download, training call, or state from Labs 2/3 was used.

## Commands and Cells Executed

1. Parsed canonical JSON, validated official nbformat structure, and syntax-checked every code cell.
2. Ran the canonical starter from a fresh kernel. Cell 7 stopped before parameter reveal until exactly two probes and all shape/evidence predictions were entered.
3. Filled only those commitments in a temporary copy and restarted. Cell 12 stopped at the first called forward TODO with its targeted `NotImplementedError`.
4. Built a temporary participant-completed copy under `$TMPDIR`; completed every forward, mesh/projection, diagnosis, perturbation, and reflection TODO.
5. Restarted and executed the copy from top to bottom, including the deliberate transpose failure and recovery.
6. Tested held-out accuracy, six-probe outcomes, hidden/output shapes, probability range, mesh parity, four-panel evidence board, canonical-parameter immutability, and a copied `b2 + 0.20` perturbation.
7. Executed the optional opposite-delta experiment and tested the expected nonlinear asymmetry in probability shifts.
8. Inspected both plots and scanned canonical source and Student Guide wiring for answer leakage, hidden dependencies, and broken links.

## Runtime Observed

- Canonical starter to prediction checkpoint: **2.702 s**
- Prediction-complete starter to first implementation TODO: **1.921 s**
- Temporary completed clean run plus tester checks: **3.382 s**
- Rendered PNG outputs: **2**
- Uncaught errors in completed run: **0**

The completed path is below the planned 20-second compute target and far below the three-minute completed-execution allowance.

## What Worked

- All **29 cells** pass JSON/nbformat/syntax checks and contain required language metadata plus unique matching IDs.
- The prediction checkpoint precedes fixed-parameter reveal and requires exactly two valid probe names.
- The forward cache produced `Z1/A1` shape `(90, 6)` and `Z2/P` shape `(90, 1)`; probabilities are finite and in `[0,1]`.
- Held-out accuracy was **0.9111**, inside the required `0.82-0.92` band.
- Exactly **4 probes were correct and 2 were wrong**. The reproducible wrong probes were `east-rim` (`p=0.502`) and `east-notch` (`p=0.605`).
- The deliberate `X @ W1.T` path raised a readable core-dimension mismatch (`2` versus `6`), and the correct hidden step recovered shape `(6, 6)`.
- The mesh forward pass returned `(32400, 1)` probabilities; independently recomputed batch classes exactly match the plotted mesh classes.
- The four-panel board renders raw geometry, the fixed decision region, a two-dimensional hidden projection, and the six-probe trace together.
- The trace table includes `Z1`/`A1` ranges, `Z2`, probability, and result for all six probes.
- The copied `b2 + 0.20` perturbation increased all six probe probabilities, left held-out accuracy at `0.9111`, and did not mutate canonical arrays.
- The opposite copied delta lowered all six probabilities; shifts were not assumed to be perfectly symmetric through sigmoid.
- No training or inference-time parameter update occurs.
- Canonical source contains no stored output, hidden cells, solution terms, instructor links, network calls, or GPU code.
- Student Guide launch/debrief links and all notebook links resolve; prerequisites exactly match `LESSON-D1-06`, `LAB-D1-02`, and `LAB-D1-03`.

## Failures Encountered

- The transpose variant failed exactly as intended and recovery passed.
- One tester-only assertion initially expected an invented exact accuracy of `0.8444`; the actual fixed run was `0.9111`, inside the documented band. The tester check was corrected to the stated band and the temporary notebook then passed from a fresh kernel.
- No canonical execution, metadata, leakage, metric-band, probe-pattern, or parameter-mutation failure occurred.

## Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Held-out accuracy | `0.82-0.92` | `0.9111` |
| Hidden/output shapes | `(n,6)` / `(n,1)` | `(90,6)` / `(90,1)` |
| Probability range | `[0,1]` | Passed |
| Probe mystery | Exactly 4 correct / 2 wrong | Exactly `4/2` |
| Transpose case | Clear shape failure and recovery | `2` vs `6` mismatch; recovery `(6,6)` |
| Mesh parity | Mesh and batch forward agree | Exact class-array agreement |
| Perturbation | Copied parameter changes output; canonical values fixed | All probe probabilities increased; baseline arrays unchanged |

## Reproducibility and Colab Concerns

- The seed, split, probe indices, and fixed parameter arrays reproduced all required evidence locally.
- CPU runtime and memory are practical; the largest forward batch is 32,400 mesh rows.
- There is no download, local file, GPU, training, or package-restart dependency.
- A real hosted Colab run was not available, so Colab readiness remains an open setup note rather than a participant-lab blocker.

## Required Fixes

None. No participant blocker remains.

## Optional Improvements

- Several probe labels overlap in the raw, decision-region, and hidden panels. Label offsets or lightweight collision avoidance would make the evidence board easier to scan.
- Complete a hosted Colab CPU run before claiming that environment as validated.

## Retest Requirements

- Retest after any change to seed/split/probe indices, fixed parameters, function signatures, evidence band, projection helper, mesh resolution, transpose case, or perturbation immutability checks.
- Preserve exact `4/2` behavior or update the lab contract and Student Guide together before release.

## Prior Failure Disposition

The prior empty-notebook failure is resolved. The fixed network, named probes, forward TODOs, prediction gate, exact mystery, transpose failure/recovery, decision/hidden/trace evidence, perturbation, checkpoint, metadata, and participant links now exist and execute independently.

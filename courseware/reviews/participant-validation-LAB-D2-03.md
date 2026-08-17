# PASS WITH NOTES

## Participant Validation: LAB-D2-03

### Lab

- **Name/path:** Train a Neural Network with NumPy, `courseware/day-2/labs/LAB-D2-03-numpy-training.ipynb`
- **Current canonical SHA-256:** `d1e427ffbcb40bbe2f81702d096dc859ac841e7627e83c20ff87577bf1a24089`
- **Learning objectives:** `OBJ-D2-01`, `OBJ-D2-03`, `OBJ-D2-04`, `OBJ-D2-05`, `OBJ-D2-06`
- **Validation date:** 2026-08-17
- **Validation status:** **PASS WITH NOTES**
- **Interestingness:** **STRONG** - current cells require shape/range predictions, ownership of every training stage, bounded failure diagnosis, representation-versus-optimization comparison, and one controlled experiment plus an optional second variable.

This report was regenerated from the exact current canonical bytes. No prior execution or isolation evidence was carried forward.

### Environment Tested

- macOS 26.2 on Apple silicon, local CPU
- Python 3.11.8; NumPy 2.4.6; matplotlib 3.11.1; scikit-learn 1.9.0
- nbformat 5.11.0; nbclient 0.11.0; ipykernel 7.3.0
- 800 generated `make_moons` examples; no GPU, network, download, or external file

### Commands and Cells Executed

1. Read the current canonical bytes and computed the SHA-256 above.
2. Parsed raw JSON, ran official `nbformat.validate`, syntax-checked every code cell, and checked IDs, language metadata, stored outputs, leakage, dependencies, and local links.
3. Ran an exact untouched temporary copy in a new kernel. It stopped intentionally at Cell 8 with `Prediction checkpoint: complete every shape, range, and mechanism field before implementation.`
4. Built a fresh learner-completed copy from the current starter without changing canonical markdown or metadata.
5. Restarted the kernel and ran all 23 participant code cells in order with `allow_errors=False`, including baseline, copied-state NaN failure/recovery, identity/high-rate diagnostics, challenge, optional branch, plots, and checkpoint.
6. Inspected all four rendered figures visually and checked their PNGs were nonblank.

### Runtime Observed

- Untouched intentional-stop run: **2.181 s**
- Completed Restart Kernel -> Run All: **3.946 s**
- Baseline training measured inside notebook: **0.309 s**
- Participant code cells: **23/23**, execution counts `1..23`
- Rendered plots: **4** nonblank PNGs
- Uncaught errors: **0**

### What Worked

- All 42 cells pass raw JSON, nbformat schema, and Python syntax checks.
- All 42 official IDs are unique and exactly equal the unique `metadata.id` values; language metadata is complete.
- The canonical notebook has zero stored outputs/execution counts and no hidden answers, instructor/solution paths, network calls, or file dependencies.
- All six local links resolve against the current Student Guide, `ACT-D2-03`, D2-01, and D2-02.
- Current prediction gates occur before implementation, baseline execution, NaN injection, failure variants, and the controlled experiment.
- The split is seeded and stratified: `(600,2)` train and `(200,2)` validation, with class rate `0.500` in each.
- Standardization statistics are fit on training data only; training feature means pass the supplied near-zero assertion.
- The architecture and all cache/gradient shapes match `2 -> 8 -> 1` with targets `(B,1)`.
- Initial BCE was `0.686020`, inside the broad `0.65-0.75` band.
- Final train loss/accuracy were `0.1857/0.915`; validation loss/accuracy were `0.1820/0.905`.
- The rendered baseline boundary is visibly nonlinear and the loss/accuracy/gradient panels are aligned and readable.
- The deliberate NaN produced the bounded message `Non-finite state at epoch 7, batch 3` while canonical trained parameters remained finite.
- The identity-hidden model produced a linear boundary and validation accuracy `0.850`, below the nonlinear baseline.
- Learning rate `30.0` produced unstable validation loss ranging from `0.432` to `8.216`; the log-scale evidence panel kept the signal visible.
- The core one-change experiment changed only learning rate (`0.6 -> 0.3`) and produced validation `0.3398/0.850`, valid evidence that the smaller rate had not escaped the early plateau in the fixed budget.
- The optional hidden-width path executed independently and produced validation loss/accuracy `0.3420/0.850`.
- The final checkpoint printed `LAB-D2-03 checkpoint passed`.

### Failures Encountered

- The untouched starter stop, copied-state NaN injection, identity limit, and excessive-rate instability occurred intentionally and remained isolated from baseline state.
- Recovery was preserved: the NaN stayed in a copied parameter dictionary, the baseline represented restored tanh and a stable rate, and all later cells executed.
- No unintended training, state-leakage, metric-band, plot, link, metadata, or recovery failure occurred.

### Expected vs. Actual Results

| Contract | Expected | Current actual |
|---|---|---|
| Data | Seeded/stratified about 800; train-only scaling | `800`, split `600/200`, rate `0.500/0.500`, passed |
| Architecture | `2 -> 8 -> 1` | Passed all parameter/cache/gradient shapes |
| Initial BCE | Broadly near `0.69` | `0.686020` |
| Final train loss | Generally `<0.35` | `0.1857` |
| Validation accuracy | `0.85-0.95` | `0.905` |
| Identity diagnosis | Linear/underperforming | Linear boundary; `0.850` |
| High-rate diagnosis | Unstable or bounded stop | Validation loss up to `8.216` |

### Reproducibility and Colab Concerns

- Seeds cover data, initialization, and batch order. The current clean run reproduced the documented baseline.
- The complete path is vectorized, CPU-only, has a 2,000-epoch guard, and ran far below the 60-second baseline limit.
- A hosted Google Colab CPU runtime was not executed, so this report does not claim hosted Colab validation.

### Required Fixes

None.

### Optional Improvements

None identified from the current execution.

### Retest Requirements

- Run the baseline and deliberate failure/recovery paths in a fresh hosted Colab CPU runtime before claiming hosted validation.
- Recompute the canonical SHA-256 and rerun all checks after changes to seeds, split, scaling, initialization, architecture, activation, rates, epochs, batching, diagnostics, plots, links, or metadata.
# PASS WITH NOTES

## Participant Validation: LAB-D2-02

### Lab

- **Name/path:** Backpropagation and Gradient Check, `courseware/day-2/labs/LAB-D2-02-backprop-gradient-check.ipynb`
- **Current canonical SHA-256:** `a2cfee7ba3f9597d54a098bcf7e835d6069ec51927aea72638dcfda0d3e73143`
- **Learning objectives:** `OBJ-D2-04`, reinforcement of `OBJ-D2-02` and `OBJ-D2-03`
- **Validation date:** 2026-08-17
- **Validation status:** **PASS WITH NOTES**
- **Interestingness:** **STRONG** - current cells require sign prediction, manual forward/backward construction, numerical falsification, structured-defect localization, an update check, a perturbation challenge, and an optional epsilon experiment.

This report was regenerated from the exact current canonical bytes. No prior execution evidence was carried forward.

### Environment Tested

- macOS 26.2 on Apple silicon, local CPU
- Python 3.11.8; NumPy 2.4.6; matplotlib 3.11.1
- nbformat 5.11.0; nbclient 0.11.0; ipykernel 7.3.0
- Float64 throughout the gradient check; no GPU, network, download, or cross-notebook state

### Commands and Cells Executed

1. Read the current canonical bytes and computed the SHA-256 above.
2. Parsed raw JSON, ran official `nbformat.validate`, syntax-checked every code cell, and checked IDs, language metadata, stored outputs, leakage, dependencies, and local links.
3. Ran an exact untouched temporary copy in a new kernel. It stopped intentionally at Cell 7 with `Prediction checkpoint: record every sign and one path reason before the forward reveal.`
4. Built a fresh learner-completed copy from the current starter without changing canonical markdown or metadata.
5. Restarted the kernel and ran all 18 participant code cells in order with `allow_errors=False`, including finite differences, both faulty paths, corrected gradients, update, perturbation, optional epsilon sweep, plots, and checkpoint.
6. Inspected both rendered figures visually and checked their PNGs were nonblank.

### Runtime Observed

- Untouched intentional-stop run: **1.224 s**
- Completed Restart Kernel -> Run All: **1.602 s**
- Participant code cells: **18/18**, execution counts `1..18`
- Rendered plots: **2** nonblank PNGs
- Uncaught errors: **0**

### What Worked

- All 35 cells pass raw JSON, nbformat schema, and Python syntax checks.
- All 35 official IDs are unique and exactly equal the unique `metadata.id` values; language metadata is complete.
- The canonical notebook has zero stored outputs/execution counts and no hidden answers, instructor/solution paths, network calls, or file dependencies.
- All four local links resolve against the current Student Guide, `ACT-D2-02`, and D2-01 notebook.
- Current prediction gates occur before forward values, numerical gradients, defect evidence, and update evidence.
- The fixed network remains float64 with shapes `2 -> 2 -> 1`; cache and gradient arrays match their contracts.
- Maximum analytic/numeric relative errors were `1.012e-09` (`W1`), `3.657e-10` (`b1`), `1.611e-10` (`W2`), and `7.912e-11` (`b2`), all far below `1e-5`.
- The sign defect produced relative error `1.0` for every parameter group.
- The missing-hidden-sigmoid defect produced `0.6476` error for `W1/b1` while `W2/b2` remained near `1e-10`, giving a distinct layer-local signature.
- One negative-gradient update lowered loss from `0.67389837` to `0.64313799` without mutating the original parameter dictionary.
- The scalar perturbation changed loss by `-1.71476391e-04`, matching the first-order prediction `-1.71491679e-04` in sign and scale.
- The epsilon sweep rendered the expected truncation/rounding trade-off, with its minimum near `1e-4` in this current run.
- The final checkpoint printed `LAB-D2-02 checkpoint passed`.

### Failures Encountered

- The untouched starter stop and both faulty backward paths failed exactly as designed; the correct backward implementation recovered full numerical agreement.
- No unintended implementation, numerical, plot, leakage, link, metadata, or recovery failure occurred.

### Expected vs. Actual Results

| Contract | Expected | Current actual |
|---|---|---|
| Network/dtype | Float64 `2 -> 2 -> 1` | Passed all shape/dtype assertions |
| Correct gradient error | `<1e-5` | Maximum `1.012e-09` |
| Sign bug | Broad sign mismatch | Relative error `1.0` for all groups |
| Missing factor | Hidden layer fails; output layer agrees | `0.6476` hidden; about `1e-10` output |
| Negative-gradient update | Lower fixed-example loss | `0.67389837 -> 0.64313799` |
| Perturbation | Observed/predicted local changes agree | `-1.71476391e-04/-1.71491679e-04` |

### Reproducibility and Colab Concerns

- Fixed arrays, float64 arithmetic, and no external data make the path deterministic and lightweight; it completed below the documented 10-second target.
- A hosted Google Colab CPU runtime was not executed, so this report does not claim hosted Colab validation.

### Required Fixes

None.

### Optional Improvements

None identified from the current execution.

### Retest Requirements

- Run the full float64 gradient check and epsilon sweep in a fresh hosted Colab CPU runtime before claiming hosted validation.
- Recompute the canonical SHA-256 and rerun all checks after changes to fixed values, dtype, epsilon, cache keys, gradient formulas, defect presets, update rate, plots, links, or metadata.
# PASS WITH NOTES

## Participant Validation: LAB-D2-01

### Lab

- **Name/path:** Loss Landscapes and Learning-Rate Roulette, `courseware/day-2/labs/LAB-D2-01-loss-learning-rate.ipynb`
- **Current canonical SHA-256:** `d7ee72d824676ae32c6eac8f55693fb48c3b91d8f398fdfadb0dec5f95560400`
- **Learning objectives:** `OBJ-D2-02`, `OBJ-D2-03`
- **Validation date:** 2026-08-17
- **Validation status:** **PASS WITH NOTES**
- **Interestingness:** **STRONG** - current cells require loss ranking, trajectory predictions, implementation, endpoint diagnosis, mechanism explanation, a new-rate commitment, and an optional curvature experiment before evidence is revealed.

This report was regenerated from the exact current canonical bytes. No prior execution evidence was carried forward.

### Environment Tested

- macOS 26.2 on Apple silicon, local CPU
- Python 3.11.8
- NumPy 2.4.6; matplotlib 3.11.1
- nbformat 5.11.0; nbclient 0.11.0; ipykernel 7.3.0
- No GPU, network, download, external data file, or cross-notebook state

### Commands and Cells Executed

1. Read the current canonical bytes and computed the SHA-256 above.
2. Parsed raw JSON, ran official `nbformat.validate`, syntax-checked every code cell, and checked IDs, language metadata, stored outputs, leakage, dependencies, and local links.
3. Ran an exact untouched temporary copy in a new kernel. It stopped intentionally at Cell 7 with `Prediction checkpoint: complete every BCE field before calculating loss.`
4. Built a fresh learner-completed copy from the current starter without changing canonical markdown or metadata.
5. Restarted the kernel and ran all 16 participant code cells in order with `allow_errors=False`, including endpoint failure/recovery, four rates, challenge, optional branch, plot, and checkpoint.
6. Inspected the rendered trajectory figure visually and checked its PNG was nonblank.

### Runtime Observed

- Untouched intentional-stop run: **1.295 s**
- Completed Restart Kernel -> Run All: **1.596 s**
- Participant code cells: **16/16**, execution counts `1..16`
- Rendered plots: **1** nonblank PNG, `990 x 990`
- Uncaught errors: **0**

### What Worked

- JSON, official nbformat schema, and Python syntax passed for all 33 cells.
- All 33 official IDs are unique and exactly equal the unique `metadata.id` values; language metadata is complete.
- Canonical source has zero stored outputs/execution counts and no hidden answers, instructor/solution paths, network calls, or file dependencies.
- All six local links resolve against the current Student Guide, `ACT-D2-01`, environment, and notation artifacts.
- Current prediction gates occur before BCE, trajectory, and challenge results.
- Cases A and B both achieved accuracy `1.00`, while BCE differed (`0.164252` versus `0.554331`), making equal-accuracy/different-loss evidence explicit.
- Cases C and D both achieved accuracy `0.75`, while BCE differed (`0.286804` versus `1.259759`) because D contains a much more confident error.
- Naive endpoint BCE produced `inf`; clipped BCE remained finite at `27.631032`.
- The four rates reproduced crawl, smooth convergence, oscillatory convergence, and divergence after 12 updates.
- Shared position and logarithmic loss/distance axes kept every path visible; the plot was legible and correctly labeled.
- The `0.60` challenge crossed the optimum while distance contracted by about `0.20` per update.
- The optional curvature branch produced alternating distances growing by about `1.4` per update.
- The final checkpoint printed `LAB-D2-01 checkpoint passed`.

### Failures Encountered

- The untouched starter stop and naive BCE `inf` were intentional; clipping recovered in the same Run All path.
- No unintended execution, range, plot, leakage, link, metadata, or recovery failure occurred.

### Expected vs. Actual Results

| Contract | Expected | Current actual |
|---|---|---|
| Clipped BCE | Finite at exact `0/1` inputs | `27.631032`, finite |
| Equal-accuracy evidence | Same accuracy, different BCE | A/B: `1.00`, losses `0.164252/0.554331` |
| `eta=0.01` | Crawl | Distance `4.000 -> 3.139`; loss `9.852` |
| `eta=0.10` | Smooth convergence | Final distance `0.274878`; loss `0.075558` |
| `eta=0.90` | Oscillatory convergence | Crossed every step; final distance `0.274878` |
| `eta=1.10` | Divergence | Final distance `35.664402`; loss `1271.949555` |

### Reproducibility and Colab Concerns

- The deterministic, generated-in-memory CPU path completed below the documented 10-second target.
- A hosted Google Colab CPU runtime was not executed, so this report does not claim hosted Colab validation.

### Required Fixes

None.

### Optional Improvements

None identified from the current execution.

### Retest Requirements

- Run the full completed path in a fresh hosted Colab CPU runtime before claiming hosted validation.
- Recompute the canonical SHA-256 and rerun all checks after changes to the notebook, linked support artifacts, objective, rates, budget, clipping, prediction gates, plot scales, links, or metadata.
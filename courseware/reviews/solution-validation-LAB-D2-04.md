# PASS WITH NOTES

## Solution Validation: LAB-D2-04

### Lab and Solution

- **Lab:** `courseware/day-2/labs/LAB-D2-04-pytorch-break-fix.ipynb`
- **Solution:** `courseware/instructor-solutions/day-2/LAB-D2-04-pytorch-break-fix-SOLUTION.ipynb`
- **Objectives:** `OBJ-D2-01`, `OBJ-D2-02`, `OBJ-D2-05`, `OBJ-D2-07`, `OBJ-D2-08`
- **Participant SHA-256:** `b3dfb495468ac7ec05c41df9ee4bbe49b11620f1c28504425ab02cbd852e0d52`
- **Solution SHA-256:** `2c6510bdc00acb8ca415f8c0d7e520dd4abfed3c31e81165b5e9d1cf9ff4de51`
- **Final status:** **PASS WITH NOTES**

### Environment and Source Check

- macOS on Apple silicon, required local CPU path
- Python 3.11.8; PyTorch 2.6.0; NumPy 2.4.6; matplotlib 3.11.1; scikit-learn 1.9.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- No GPU, download, external data file, or prior notebook state; notebook execution itself required no network
- The official [PyTorch 2.11 `Optimizer.zero_grad` page](https://docs.pytorch.org/docs/2.11/generated/torch.optim.Optimizer.zero_grad.html) was fetched and checked on 2026-08-16. It verifies `set_to_none=True` as the plain-call default, `None` for parameters that receive no gradient, and optimizer behavior that skips `None` but processes a zero tensor.
- Exact PyTorch 2.11 runtime execution is not claimed; the clean run reproduced the documented behavior on compatible local PyTorch 2.6.0.

### Clean-Run Evidence

- Cleared all outputs and counts, started a fresh `python3` kernel, and executed the canonical solution from top to bottom.
- Final clean wall time including kernel startup: **7.795 s**; baseline training measured inside the notebook: **0.733 s**.
- Executed **21/21 code cells** with sequential counts; rendered **2 nonblank PNGs** at `1390x990` and `1590x1690`; uncaught errors: **0**.
- All **51 cells** pass nbformat and syntax validation with unique official IDs exactly matching unique `metadata.id` values and correct `python`/`markdown` language metadata.
- Imports verified: Python standard library plus NumPy, matplotlib, scikit-learn, PyTorch, and `torch.utils.data`.
- All **5 local links and anchors** resolve. The official PyTorch link also returned the documented 2.11 page.
- The optional shape `ValueError` is caught and repaired; no deliberate failure escapes its handling block.

### Tasks and Questions Covered

- Completed the NumPy-to-PyTorch responsibility map, logits/target predictions, `nn.Module`, evaluation helper, explicit optimizer order, baseline predictions, and training loop.
- Preserved evidence-only diagnosis before source reveal for cards A-D.
- Solved, executed, and explained all four defects with one-field configuration repairs.
- Distinguished `model.eval()` from `torch.inference_mode()` using direct `requires_grad` evidence.
- Executed the optional `(B,1)` versus `(B,)` target-shape mismatch and recovery.
- Executed an isolated gradient-state probe for plain default reset, post-backward tensors, unused parameters, explicit zero buffers, and optimizer `None`-versus-zero behavior without referencing or mutating the baseline or diagnostic models.
- Answered every prediction, interpretation, reflection, and optional prompt; supplied all-card expected evidence, instructor notes, hint ladders, misconceptions, troubleshooting, acceptable alternatives, demo prompts, and fast recovery paths.
- Mapped `DataLoader`, `nn.Linear`, `nn.Tanh`, `nn.Dropout`, `BCEWithLogitsLoss`, plain `zero_grad`, `backward`, gradient norm, `step`, `eval`, `inference_mode`, and `sigmoid` to NumPy mechanics or training-loop responsibilities.

### Expected Result Checks

| Contract | Clean-run evidence |
|---|---|
| Baseline | Train loss/accuracy `0.2439/0.900`; validation `0.2554/0.900`; nonlinear boundary |
| Card A: missing nonlinearity | Broken `0.3343/0.850`; repaired `0.2478/0.895` |
| Card B: omitted reset | Broken `4.2597/0.690`; gradient norm `1.146 -> 6.828`; repaired `0.2478/0.895`, norm range `0.071-0.286` |
| Card C: mode/context misuse | Broken accuracy `0.865`, repeat std `0.06525`, outputs tracked; repaired std `0`, no tracked output |
| Card D: probabilities as logits | Broken `0.5731/0.500`; repaired `0.2478/0.895` |
| Plain default reset | Used and unused optimized gradients both inspect as `None` immediately after plain `zero_grad()` |
| Post-backward state | Used parameter has a tensor; unused parameter remains `None` |
| Explicit zero-buffer contrast | `set_to_none=False` produces used-gradient sum `0.0`; never-materialized unused gradient remains `None` |
| Optimizer distinction | Weight-decay SGD leaves the `None`-gradient parameter at `1.0` and changes the zero-gradient parameter to `0.89999998` |
| Mode versus autograd | `eval()` only: `requires_grad=True`; with `inference_mode()`: `False` |
| Shape mismatch | Caught target `(16,)` versus input `(16,1)` `ValueError`; same-shaped recovery is finite |

### Instructor Readiness

- Hint ladders precede the baseline and defect reveals; diagnoses include competing causes, discriminating checks, rejection conditions, and residual uncertainty.
- The all-card path uses a common seeded repaired configuration and proves each broken configuration differs by exactly one expected field.
- `nn.Linear.weight` storage `(d_out,d_in)` is explicitly reconciled with the course NumPy convention `(d_in,d_out)`.
- Instructor notes explicitly correct the plain-call misconception, explain why unused gradients can remain `None` even after explicit `set_to_none=False`, and distinguish ordinary reset from intentional accumulation.
- Stored output permits a fast live recovery while the complete all-card and isolated-probe code remains independently executable.

### Answer Separation

- Participant SHA-256 remained `b3dfb495468ac7ec05c41df9ee4bbe49b11620f1c28504425ab02cbd852e0d52` before and after solution work, exactly matching the current Student **PASS WITH NOTES** report.
- The participant notebook retains zero outputs, unexecuted counts, five deliberate `NotImplementedError` gates, and blank response fields.
- No solution label, completed diagnosis, model answer, answer key, instructor-only path, instructor note, or gradient-state probe was found in the participant artifact.
- **Leakage result: NONE.**

### Issues Found and Fixes Applied

- Removed the stale claims that plain `zero_grad()` supplies visible zero tensors and that `set_to_none=True` is merely an advanced alternative.
- Mirrored the corrected participant wording and added executable, asserted evidence for every required gradient state and optimizer distinction.
- Corrected five final navigation targets from participant-relative to instructor-solution-relative paths; every local link and anchor now resolves.
- No participant contradiction was found, and no participant file was changed.

### Remaining Notes

1. A hosted Google Colab CPU runtime was not executed; hosted readiness is not claimed.
2. An exact PyTorch 2.11 runtime was not executed; API source checking is not an exact-version runtime substitute.

### Final Status

**PASS WITH NOTES** - complete, all-card and optional-path clean-executable, corrected for PyTorch 2.11 reset semantics, instructor-ready, and correctly separated; hosted Colab and exact PyTorch 2.11 remain unvalidated.
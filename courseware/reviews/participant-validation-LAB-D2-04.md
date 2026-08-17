# PASS WITH NOTES

## Participant Validation: LAB-D2-04

### Lab

- **Name:** PyTorch Autograd - Break It and Fix It
- **Participant path:** `courseware/day-2/labs/LAB-D2-04-pytorch-break-fix.ipynb`
- **Current canonical SHA-256:** `b3dfb495468ac7ec05c41df9ee4bbe49b11620f1c28504425ab02cbd852e0d52`
- **Learning objectives:** `OBJ-D2-01`, `OBJ-D2-02`, `OBJ-D2-05`, `OBJ-D2-07`, `OBJ-D2-08`
- **Validation date:** 2026-08-16
- **Validation status:** **PASS WITH NOTES**
- **Interestingness:** **STRONG** - learners map mechanics to framework calls, build a valid baseline, commit an evidence-only diagnosis before source reveal, repair one invariant, and separate module mode from autograd state.

### Environment Tested

- macOS on Apple silicon, required CPU path
- Python 3.11.8; PyTorch 2.6.0; NumPy 2.4.6; matplotlib 3.11.1; scikit-learn 1.9.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- No GPU, network, download, external file, or prior notebook state

The current readiness notebook also passed from a clean kernel in **3.332 s**, including the documented imports, explicit CPU tensor operation, optional device detection, and all readiness messages. PyTorch 2.11 was not installed locally; the current execution used 2.6.0.

### Commands and Cells Executed

1. Ran JSON, official nbformat, syntax, outputs, leakage, and local-link audits.
2. Verified all 41 official IDs are unique, all 41 `metadata.id` values match them uniquely, and every language field is correct.
3. Resolved all local links against the current Student Guide anchors.
4. Verified the revised wording against the official PyTorch 2.11 `Optimizer.zero_grad`, autograd grad-mode, and module-mode documentation.
5. Built one temporary participant-completed copy for assigned card B from the current canonical notebook; the canonical notebook was not edited.
6. Executed all 21 participant code cells plus two isolated tester probe cells from a fresh kernel. The path covered baseline, omitted-reset defect, one-field repair, mode/autograd distinction, checkpoint, and both plots.
7. Recomputed the canonical SHA-256 before and after execution; both hashes were `b3dfb495468ac7ec05c41df9ee4bbe49b11620f1c28504425ab02cbd852e0d52`.

### Runtime Observed

- Final current-hash card B clean run, including tester probes: **5.373 s**
- Executed code cells: **21/21 participant cells plus 2/2 tester probes**
- Baseline training measured inside notebook: **1.145 s**
- Rendered PNG outputs: **2**
- Uncaught errors: **0**

### What Worked

- All 41 cells pass JSON/nbformat/syntax checks; official IDs, matching duplicate metadata IDs, language metadata, and clean participant state pass.
- D2-04 exactly reproduces D2-03's generated split and training-only standardization; tensors are `(600,2)/(600,1)` and `(200,2)/(200,1)`.
- `MoonClassifier` emits raw logits and uses `BCEWithLogitsLoss` with same-shaped targets.
- The training loop executes `zero_grad -> forward -> loss -> backward -> gradient norm -> step` and returns to `model.train()` each epoch.
- The PyTorch 2.11 wording is accurate: plain `optimizer.zero_grad()` uses `set_to_none=True`; after that call optimized gradients are `None`, while explicit `set_to_none=False` zero-fills existing gradient buffers.
- The wording also accurately states that a parameter receiving no gradient remains `None` after backward and that optimizers distinguish `None` from a zero tensor.
- Baseline train loss/accuracy were `0.2439/0.900`; validation loss/accuracy were `0.2554/0.900`.
- Baseline and repaired boundaries are nonlinear; card B repaired accuracy was `0.895`, inside `0.85-0.95`.
- `eval()` alone returned logits with `requires_grad=True`; `eval()` plus `inference_mode()` returned `False`.
- A tester probe confirmed both `no_grad()` and `inference_mode()` return tensors with `requires_grad=False`; a tensor created under `no_grad()` remained usable in a later autograd-recorded computation, while equivalent inference-tensor reuse was rejected.
- The evidence-only diagnosis cell and its assertion occur before any defect mapping or faulty source.
- Card B's one-invariant defect was reproducible and repaired by changing only `reset_gradients`.
- Its broken mean gradient norm grew from `1.146` to `5.918` with maximum `6.828`; repaired norms stayed between `0.197` and `0.286`.
- After plain `zero_grad()`, both optimized probe gradients were `None`; after backward, the used parameter held a tensor and the unused parameter remained `None`.
- After explicit `set_to_none=False`, the existing used gradient was a zero tensor and the never-materialized unused gradient remained `None`.
- An isolated SGD weight-decay probe left a `None`-gradient parameter at `1.0` but changed the zero-gradient parameter from `1.0` to about `0.9`, demonstrating the documented optimizer distinction without touching canonical training state.
- Canonical source contains no stored output, hidden answer, instructor path, solution link, network call, or local file dependency.
- The repaired `LESSON-D2-07` link resolves, and the shared environment now documents the Day 2 PyTorch setup, CPU contract, and validation limits.

### Defect and Recovery Evidence

| Card | Defect | Broken evidence | Repaired evidence |
|---|---|---|---|
| B | Omitted gradient reset | Loss `4.2597`, accuracy `0.690`, norms up to `6.828` | Loss `0.2478`, accuracy `0.895`, norms at most `0.286` |

### Failures Encountered

- The card B omitted-reset preset failed intentionally and its documented one-field recovery passed.
- Early temporary-copy attempts stopped at required learner gates because the tester had not yet completed the framework map and model TODO. A tester-only probe later reached its final print with a missing `json` import. These were temporary tester-completion defects; after correction, the final fresh-kernel run completed with zero uncaught errors.
- No unintended API, metric-band, mode, gradient, plot, link, metadata, setup, or recovery failure occurred.

### Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Baseline/repaired accuracy | `0.85-0.95` | Baseline `0.900`; repaired `0.895` |
| Output/loss | Raw `(B,1)` logits with same-shaped target | Passed; exact shape assertion executed |
| Optimizer order | Reset, forward, loss, backward, step | Implemented and executed |
| Mode/autograd distinction | Independent controls | `True` after eval only; `False` in inference mode |
| Plain reset state | Optimized grads are `None` before backward | Passed for used and unused parameters |
| Post-backward state | Receiving parameters have tensors; unused stays `None` | Passed |
| Explicit zero-buffer contrast | Existing grads become zero tensors | Used grad `0.0`; never-materialized unused grad remained `None` |
| Optimizer distinction | `None` can skip a step while zero can take one | Weight-decay probe: `1.0 -> 1.0` versus `1.0 -> 0.9` |
| Card B gradient evidence | Accumulation grows; repair remains bounded | Broken max `6.828`; repaired max `0.286` |

### PyTorch 2.11 Source Check

- **Claim:** plain `Optimizer.zero_grad()` uses `set_to_none=True`; explicit `set_to_none=False` zero-fills existing gradients. **Status:** verified against the official [PyTorch 2.11 `Optimizer.zero_grad` documentation](https://docs.pytorch.org/docs/2.11/generated/torch.optim.Optimizer.zero_grad.html).
- **Claim:** parameters that receive no gradient remain `None` after backward, and optimizers can skip `None` gradients while processing zero tensors. **Status:** verified against the same official API page and reproduced by isolated local probes.
- **Claim:** `nn.Module.eval()` is orthogonal to no-grad and inference modes; inference tensors have stricter later-autograd use than tensors created under `no_grad()`. **Status:** verified against the official PyTorch 2.11 autograd grad-mode notes and reproduced locally.
- **Version relevance:** source claims are specific to 2.11. Runtime behavior was exercised on local PyTorch 2.6.0 using the same stable APIs; this is not an exact-2.11 execution claim.

### Reproducibility and Colab Concerns

- Data, Python, NumPy, model, and DataLoader seeds are set; the current card B run reproduced the baseline.
- CPU runtime is far below the six-minute allowance. Dataset and model are small, and no accelerator is assumed.
- A hosted Google Colab CPU runtime and an exact PyTorch 2.11 runtime were not executed. These are the only remaining validation notes; no hosted or exact-version validation claim is made.

### Required Fixes

None. The `zero_grad()` semantics correction is accurate and the current participant path passed the requested retest.

### Optional Improvements

None identified by this repair-focused retest.

### Retest Requirements

- Run card B in a fresh hosted Colab CPU runtime and at least the baseline plus card B repair on PyTorch 2.11 before claiming hosted or exact-version validation.
- Retest all four cards after changes to seeds, architecture, dropout, learning rate, epochs, defect mapping, evaluation helper, loss pairing, optimizer order, links, or metadata.
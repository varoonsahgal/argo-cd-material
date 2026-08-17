# PASS WITH NOTES

## Participant Validation: LAB-D3-03

### Lab

- **Name:** Make It Overfit, Then Rescue It
- **Participant path:** `courseware/day-3/labs/LAB-D3-03-overfit-and-rescue.ipynb`
- **Canonical SHA-256:** `1027482a1674bee5875e6c6e52febed5fd6e8770aad8ec36e73306bd51084e49`
- **Learning objectives:** `OBJ-D3-04`, `OBJ-D3-05`, with reinforcement of `OBJ-D3-01`
- **Validation date:** 2026-08-16
- **Validation status:** **PASS WITH NOTES**
- **Interestingness:** **STRONG** - participants predict and create a conspicuous generalization failure, choose exactly one remedy, preserve a matched budget, inspect aligned curves, and accept or reject the hypothesis from evidence rather than forcing an improvement story.

### Environment Tested

- macOS on Apple silicon, required CPU path
- Python 3.11.8
- NumPy 2.2.4, matplotlib 3.11.1, scikit-learn 1.9.0
- PyTorch 2.6.0, torchvision 0.21.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- `ALLOW_DOWNLOAD=False`; independently loaded packaged Fashion-MNIST fallback
- No network, GPU, prior notebook variables, or model state from `LAB-D3-02`

A hosted Google Colab session and the opt-in Fashion-MNIST cache/download branch were not executed.

### Commands and Cells Executed

1. Validated raw JSON, official nbformat, syntax, matching unique cell IDs, language metadata, empty output state, learner responses, and participant separation.
2. Ran the untouched canonical notebook in a fresh kernel. It independently loaded data, then stopped intentionally at visible **Cell 7** before model construction and training. No later cell executed.
3. Built a temporary participant-completed copy without reading solution artifacts.
4. Implemented `CapacityNet` and the matched-budget training harness.
5. Ran the 24-epoch high-capacity baseline on 400 balanced training images and 800 validation images.
6. Triggered the confounded three-remedy validator and confirmed the documented recovery is to choose one intervention.
7. Selected exactly one core remedy: dropout `0.4`. Split, seed, model widths, optimizer family, learning rate, batch size, and 24-epoch budget otherwise remained fixed.
8. Completed the optional augmentation design path without adding it to the core experiment.
9. Restarted the kernel and ran all 15 code cells in order.
10. Rendered and inspected the baseline and matched-comparison plots.

### Runtime Observed

- Untouched starter to intentional stop: **3.102 s** wall time
- Final completed Restart Kernel -> Run All: **4.107 s** wall time
- Baseline training measured inside the notebook: **0.20 s**
- Dropout run measured inside the notebook: **0.21 s**
- Baseline plus one intervention: approximately **0.41 s** measured training time
- Executed code cells: **15/15**
- Rendered PNG outputs: **2**
- Uncaught errors in completed run: **0**
- CPU runtime checkpoint: passed under **10 min**

### What Worked

- The notebook reloaded the fallback independently and selected exactly 400 balanced training examples (`40` per class) plus 800 validation examples.
- The baseline model had **535,818** parameters, satisfying the intended high-capacity/tiny-data setup.
- The baseline produced:
  - final training accuracy **0.998**
  - final validation accuracy **0.796**
  - final generalization gap **0.201**
- All required baseline gates passed: train `>0.98`, validation `0.65-0.82`, and gap `>=0.15`.
- Baseline validation loss reached its minimum at approximately epoch **7**, then rose while training loss approached zero. The plot clearly distinguishes overfitting from failed optimization.
- The confounded rescue raised the intended error: `Core experiment requires exactly one remedy; received ['dropout', 'weight_decay', 'smaller_model']`.
- The one-change dropout run produced:
  - final training accuracy **0.985**
  - final validation accuracy **0.799**
  - final gap **0.186**
- The predeclared acceptance criterion required at least `+0.03` validation accuracy or a gap reduction of at least `0.05` without lower validation. Actual deltas were about `+0.003` validation and `-0.015` gap, so the participant conclusion correctly **rejected** this dropout strength as a successful rescue.
- The negative result remained useful: dropout reduced training fit and late validation-loss growth, but not enough to satisfy the declared performance criterion.
- Baseline and intervention curves use the same epoch axis, loss/accuracy scales, split, and budget.
- The optional augmentation plan remained planning-only and included a deterministic validation check, so it did not confound the core comparison.
- The final checkpoint passed despite the remedy not materially improving validation, as intended by the lab contract.

### Failures Encountered

- The untouched starter stopped intentionally at the pre-training prediction gate.
- The combined three-remedy configuration failed intentionally and was recovered by selecting one remedy.
- Dropout did not meet the participant's improvement criterion. This is a valid evidence-based rejection, not an execution defect.
- No unintended source, split, baseline-band, runtime, plotting, or checkpoint failure occurred.

### Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Independent fallback load | No dependence on D3-02 state | Passed |
| Tiny train / validation | `400/800`, balanced train | Passed; `40` per class |
| Baseline parameters | More than 500,000 | **535,818** |
| Baseline train accuracy | `>0.98` | **0.998** |
| Baseline validation accuracy | `0.65-0.82` | **0.796** |
| Baseline gap | `>=0.15` | **0.201** |
| Exactly one remedy | One of dropout/decay/smaller model | Dropout `0.4`, passed |
| Remedy outcome | Improvement or supported rejection | Rejected: `+0.003` validation, `-0.015` gap |
| Matched runtime | Baseline + remedy under 10 min | **4.107 s** total wall time |

### Reproducibility and Colab Concerns

- Data sampling, model initialization, and each newly constructed loader use supplied seeds.
- Each run creates a fresh model, optimizer, and loader; no state crosses from baseline to remedy.
- The small fallback and CPU execution are practical for hosted notebooks.
- Colab must include the repository support directory; the notebook alone is insufficient for offline fallback.
- A real hosted Colab CPU session was not executed, so no hosted-validation claim is made.

### Required Fixes

None for the participant notebook or fallback path.

### Optional Improvements

None required. The prompt explicitly supports evidence-based rejection, and the observed dropout result demonstrates that design well.

### Retest Requirements

- Run the completed fallback path in a fresh hosted Colab CPU session before claiming hosted readiness.
- Execute the opt-in Fashion-MNIST branch before extending these metric or runtime conclusions to that source mode.
- Retest after changes to fallback data, tiny split, model widths, epochs, learning rate, dropout/decay values, one-change validator, acceptance prompt, axes, links, or metadata.

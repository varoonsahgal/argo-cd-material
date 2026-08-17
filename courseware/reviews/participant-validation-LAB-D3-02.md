# PASS WITH NOTES

## Participant Validation: LAB-D3-02

### Lab

- **Name:** Compact CNN and Feature Maps
- **Participant path:** `courseware/day-3/labs/LAB-D3-02-cnn-feature-maps.ipynb`
- **Canonical SHA-256:** `0041ce12334e94190c4202f6513a608c7ace0190f4cee934fbb504660f35ae8f`
- **Learning objectives:** `OBJ-D3-01`, `OBJ-D3-03`
- **Validation date:** 2026-08-16
- **Validation status:** **PASS WITH NOTES**
- **Interestingness:** **STRONG** - participants predict source and shapes, trigger and repair a channel defect, implement and train a compact CNN, capture temporary feature maps, inspect confident mistakes, and separate descriptive activations from causal explanation.

### Environment Tested

- macOS on Apple silicon, required CPU path
- Python 3.11.8
- NumPy 2.2.4, matplotlib 3.11.1, scikit-learn 1.9.0
- PyTorch 2.6.0, torchvision 0.21.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- `ALLOW_DOWNLOAD=False`; no Fashion-MNIST cache; packaged real Fashion-MNIST fallback
- No network, GPU, or prior notebook state

A hosted Google Colab session and the opt-in full Fashion-MNIST path were not executed. The report does not apply the online/full-split metric band to fallback results.

### Commands and Cells Executed

1. Validated raw JSON, official nbformat, Python syntax, IDs, matching metadata IDs, language metadata, empty output state, response fields, and participant separation.
2. Ran the untouched canonical notebook in a fresh kernel. It stopped intentionally at visible **Cell 4**, before loading data, at the source-mode prediction assertion. No later cell executed.
3. Built a temporary participant-completed copy without using solution files.
4. Completed all source, architecture, training, mistake, interpretation, and reflection responses.
5. Implemented the compact CNN, one explicit training epoch, temporary feature-map hooks, and hook cleanup.
6. Executed the deliberate three-channel failure and repaired one-channel architecture.
7. Enabled and ran the optional third epoch.
8. Restarted the kernel and ran all 19 code cells from top to bottom.
9. Rendered and inspected the input grid, aligned learning curves, early/later activation maps, and ten highest-confidence validation errors.
10. Structurally inspected the opt-in/cache branch and resolved all prerequisite, challenge, assessment, and debrief links.

### Runtime Observed

- Untouched starter to intentional stop: **8.544 s** wall time
- Final completed Restart Kernel -> Run All: **5.638 s** wall time
- Bounded two-epoch training measured inside the notebook: **0.79 s**
- Executed code cells: **19/19**
- Rendered PNG outputs: **4**
- Uncaught errors in completed run: **0**
- CPU runtime checkpoint: passed under **12 min**

### What Worked

- With `ALLOW_DOWNLOAD=False` and no cache, the notebook selected `packaged_fashion_mnist_fallback` automatically.
- The fallback is real Fashion-MNIST data with split shapes `(3000,1,28,28)`, `(800,1,28,28)`, and `(800,1,28,28)`.
- Training-only normalization measured mean/std **0.2862/0.3531** and applied the fixed values to validation/test.
- The input grid rendered readable Fashion-MNIST examples with correct class labels.
- The deliberate `Conv2d(3,16,...)` call raised the expected channel mismatch for input `(B,1,28,28)`.
- The repaired shape trace was exactly:
  - `(8,1,28,28)` input
  - `(8,16,28,28)` first convolution
  - `(8,16,14,14)` first pool
  - `(8,32,14,14)` second convolution
  - `(8,32,7,7)` second pool
  - `(8,1568)` flatten
- The completed model had **105,866** trainable parameters, below the `250,000` ceiling.
- Two bounded epochs produced:
  - epoch 1: train loss `1.5464`, train accuracy `0.531`, validation accuracy `0.685`
  - epoch 2: train loss `0.7570`, train accuracy `0.722`, validation accuracy `0.762`
- The fallback checkpoint used only its documented minimum `>=0.68`; the full `0.80-0.88` band was not applied.
- Temporary hooks captured `conv1 (1,16,28,28)` and `conv2 (1,32,14,14)` tensors, detached them to CPU, and left both modules with zero registered hooks.
- The map panel visibly preserved finer spatial detail in early maps and coarser/selective patterns in later maps without assigning unsupported semantic names.
- The misclassification panel paired validation indices, true labels, predictions, and confidence correctly. The observed errors included plausible `Shirt/T-shirt/top/Dress`, `Coat/Pullover`, and `Sneaker/Ankle boot` confusions.
- The optional third epoch executed: train accuracy **0.772**, validation accuracy **0.764**.
- The final checkpoint passed.

### Failures Encountered

- The untouched starter stopped intentionally at the first prediction gate.
- The wrong-channel convolution failed intentionally and the architecture repair resolved it.
- The torchvision cache lookup reported `Dataset not found`; the documented packaged fallback recovered without network.
- No unintended model, training, hook, label-indexing, plot, or metric-band failure occurred.

### Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Offline source | Packaged real Fashion-MNIST | Passed, `3000/800/800` |
| Input/shape trace | `(B,1,28,28)` through `(B,32,7,7)` | Passed exactly |
| Trainable parameters | `<250,000` | **105,866** |
| Deliberate bug | Reproducible channel error and repair | Passed |
| Fallback validation | No full-split claim; checkpoint `>=0.68` | **0.762** after core run |
| Hooks | Two maps, detached; handles removed | Passed |
| Optional epoch | Practical and core-independent | **0.764** validation |
| Completed CPU runtime | Under 12 min | **5.638 s** wall time |

### Online and Fallback Status

- **Fallback:** executed end to end, including full training/evaluation mechanics, plots, hooks, error analysis, optional epoch, and checkpoint.
- **Opt-in/cache branch:** structurally inspected. It uses `FashionMNIST(..., download=allow_download)`, seeded balanced selection, and training-derived normalization.
- **Not executed:** full `10,000/2,000/2,000` Fashion-MNIST mode, download behavior, full-mode `0.80-0.88` accuracy band, and full-data throughput.

### Reproducibility and Colab Concerns

- Data selection, model initialization, and training-loader order have separate supplied seeds.
- The CPU model and packaged data are small; observed runtime is far below the live-class ceiling.
- Colab must receive the repository support directory with the notebook; uploading the notebook alone cannot satisfy the relative fallback path. This requirement is documented in the shared environment guide.
- A hosted Colab CPU runtime was not executed, so the lab must not be labeled Colab-validated.

### Required Fixes

None for the participant notebook or default fallback path.

### Optional Improvements

None required. The notebook correctly labels the fallback claim boundary and keeps the extra epoch outside the core checkpoint.

### Retest Requirements

- Run the complete fallback path in a fresh hosted Colab CPU runtime before making a hosted-readiness claim.
- Execute the opt-in/cache path from a clean cache before validating the full Fashion-MNIST band or download behavior.
- Retest after changes to fallback data, normalization, seeds, architecture, parameter ceiling, epochs, hooks, source-mode conditions, labels, links, or metadata.
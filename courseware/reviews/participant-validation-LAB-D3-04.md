# PASS WITH NOTES

## Participant Validation: LAB-D3-04

### Lab

- **Name:** Transfer-Learning Race
- **Participant path:** `courseware/day-3/labs/LAB-D3-04-transfer-learning-race.ipynb`
- **Canonical SHA-256:** `a7a28eecb783c96c1df2eb8bd4045e2143e63f040fe17c7860424baae0bcf9d0`
- **Learning objective:** `OBJ-D3-06`, with reinforcement of `OBJ-D3-01`, `OBJ-D3-05`, and `OBJ-D3-08`
- **Validation date:** 2026-08-16
- **Validation status:** **PASS WITH NOTES**
- **Interestingness:** **STRONG** - participants diagnose invalid transfer claims, verify freezing by parameters and gradients, train both scratch and head paths, construct a provenance-aware cache key and scoreboard, and defend a conditional engineering choice.

### Environment Tested

- macOS on Apple silicon, required CPU path
- Python 3.11.8
- NumPy 2.2.4, matplotlib 3.11.1
- PyTorch 2.6.0, torchvision 0.21.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- `ALLOW_DOWNLOAD=False`
- Unique empty `TORCH_HOME` for the completed run and offline-order probe
- Packaged Fashion-MNIST recovery images and label-blind surrogate embeddings
- No network, GPU, cached MobileNet weights, cached CIFAR-10, or prior notebook state

A hosted Google Colab session and the canonical CIFAR-10/MobileNet path were not executed. No online metric, extraction-time, cache-hit, or transfer-advantage claim is made.

### Commands and Cells Executed

1. Validated JSON, official nbformat, Python syntax, official/metadata IDs, language metadata, empty outputs, response fields, participant separation, and links.
2. Ran the untouched canonical notebook in a fresh kernel. It stopped intentionally at visible **Cell 4**, before transfer diagnostics or model construction. No later cell executed.
3. Built a temporary participant-completed copy without using solution files.
4. Implemented the exact canonical pretrained branch contract: `MobileNet_V3_Small_Weights.DEFAULT`, `weights.transforms()`, `mobilenet_v3_small(weights=weights)`, classifier replacement, and full backbone freezing.
5. Implemented the cache key, scratch CNN, shared bounded trainer, and fresh linear head.
6. Restarted and ran all 16 code cells with an empty Torch Hub cache.
7. Executed both invalid-transfer diagnostics, freeze parameter/gradient checks, recovery scratch training, packaged-feature head training, scoreboard, reflection, and optional fine-tuning plan.
8. Rendered and inspected the quality/parameter scoreboard.
9. Ran a separate fresh-kernel offline-order probe that replaced socket connection and CIFAR constructor access with recording failures before source selection.
10. Structurally inspected the opt-in weight preflight, CIFAR source, extraction/cache branch, transform identity, frozen backbone, and cache-key inputs.

### Runtime Observed

- Untouched starter to intentional stop: **2.169 s** wall time
- Final completed fallback Restart Kernel -> Run All: **4.066 s** wall time
- Scratch training: **1.070 s**
- Recovery-head training: **0.174 s**
- Recovery extraction time: **0.000 s**, correctly labeled as packaged features rather than a cache-hit extraction benchmark
- Executed code cells: **16/16**
- Rendered PNG outputs: **1**
- Uncaught errors in completed run: **0**
- Recovery total-time checkpoint: passed under **15 min**

### What Worked

- Both invalid configurations failed with actionable diagnoses:
  - frozen `weights=None` is a frozen random backbone, not pretrained transfer;
  - unmatched normalization violates the selected weights' preprocessing contract.
- Recovery constructed MobileNet V3 Small with `weights=None` only for architecture/freeze mechanics and labeled it accordingly.
- Replacing the classifier with `nn.Identity()` left **927,008** backbone parameters, with **0** trainable.
- A dummy backward pass produced **0** backbone gradient tensors and **2** temporary-head gradient tensors.
- With a unique empty weight cache, the notebook selected `packaged_recovery_surrogate_not_cifar_or_mobilenet` and reported `2400/800/800` examples.
- The dedicated offline-order probe recorded:
  - socket/network attempts: **0**
  - CIFAR constructor calls: **0**
  - selected mode: packaged recovery
- This proves recovery activates before CIFAR access or a network request when weights are absent and downloads are disabled.
- The completed cache key hashes weight identity, `repr(transform)`, split image/label fingerprint, and torchvision version; it returned a 64-character SHA-256 value.
- The scratch recovery model had **105,866** trainable parameters and reached validation accuracy **0.7575** in **1.070 s**.
- Packaged embeddings had shapes `(2400,256)` and `(800,256)` and were converted to float32.
- A newly initialized linear head had **2,570** trainable parameters and reached validation accuracy **0.77125** in **0.174 s**.
- Both fallback thresholds passed: scratch `>=0.55`, head `>=0.45`.
- Every scoreboard row retains `packaged_recovery_surrogate_not_cifar_or_mobilenet`; the feature row also records `course-surrogate-v1-not-mobilenet` and `packaged recovery`.
- The plot correctly shows the small recovery-task quality difference and large trainable-parameter difference.
- The participant interpretation explicitly states that the result is not CIFAR-10, not MobileNet features, and not evidence of a transfer-learning advantage.
- The optional fine-tuning plan remains outside the core budget and names a final block, smaller rate, validation evidence, and resource risk.
- The final checkpoint passed.

### Failures Encountered

- The untouched starter stopped intentionally at its first prediction gate.
- Frozen-random and wrong-normalization configurations failed intentionally and produced the expected diagnoses.
- The missing pretrained-weight cache intentionally selected recovery before CIFAR access.
- No unintended fallback, training, gradient, label alignment, scoreboard, runtime, or checkpoint failure occurred.

### Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Offline ordering | No network or CIFAR before recovery | **0** socket, **0** CIFAR calls |
| Recovery mode | Clearly not CIFAR/MobileNet | Passed in mode and scoreboard |
| Frozen backbone | No trainable params/gradients | `0/927,008`; `0` gradient tensors |
| Scratch path | Trains; recovery threshold `>=0.55` | **0.7575**, **1.070 s** |
| Head path | Fresh head trains; threshold `>=0.45` | **0.77125**, **0.174 s**, `2,570` params |
| Cache key | 64-char hash with weights/transforms/split/version | Passed |
| Invalid transfer | Both defects diagnosed | Passed |
| Recovery runtime | Under 15 min | **4.066 s** wall time |

### Online and Fallback Status

- **Fallback:** executed end to end, including scratch training, new-head training, freeze mechanics, gradient checks, cache reasoning, scoreboard, optional planning, and checkpoint.
- **Canonical path:** structurally inspected only. The current source explicitly uses the default MobileNet V3 Small weight enum, its bundled transforms, a frozen classifier-free backbone, CIFAR-10 balanced splits, and a cache key tied to weights/transforms/split/version.
- **Not executed:** MobileNet weight download/load, CIFAR-10 load/download, canonical feature extraction, canonical cache creation/hit, wrong-normalization metric degradation, canonical quality bands, canonical extraction time, or online winner.

### Reproducibility and Colab Concerns

- Data, model, and loader seeds are explicit. Recovery artifacts are fixed and hash-verified separately.
- CPU fallback runtime and memory are practical for Colab, but the notebook and support directory must be uploaded together.
- The online branch depends on network availability, weight and dataset caches, and upstream artifact behavior; none was execution-validated here.
- A hosted Colab CPU runtime was not available, so neither fallback nor online mode is claimed as hosted-validated.

### Required Fixes

None for the participant notebook or its default offline recovery path.

The separate support generator's previously documented no-flag defect is resolved. Its focused post-guard support retest passed with zero unexpected dataset, MobileNet, or network calls; this does not change the lab status or expand the untested canonical-path claims above.

### Optional Improvements

None required in the participant notebook. Its recovery claim boundary is appropriately explicit.

### Retest Requirements

- Run the fallback path in a fresh hosted Colab CPU session before claiming hosted readiness.
- Execute the full opt-in CIFAR-10/MobileNet branch from an empty cache before claiming canonical metrics, extraction runtime, cache behavior, or transfer advantage.
- Re-run the no-network/CIFAR-order probe after changes to preflight or source-selection logic.
- Retest after changes to weight enum, transforms, freeze logic, cache key, split fingerprint, support artifacts, training budgets, scoreboards, links, or metadata.
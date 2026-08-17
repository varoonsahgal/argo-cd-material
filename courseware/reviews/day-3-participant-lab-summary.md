# PASS WITH NOTES - GENERATOR SUPPORT CONTRACT PASS

## Day 3 Participant Lab Validation Summary

### Status Matrix

| Lab | Status | Interestingness | Completed clean run | Source mode | Key evidence |
|---|---|---|---:|---|---|
| `LAB-D3-01` | **PASS WITH NOTES** | **STRONG** | **3.372 s** | Generated local records | Leaky AUC `0.9960`; valid AUC `0.8310`; proxy removed; stratified `60/20/20`; train-only scaling |
| `LAB-D3-02` | **PASS WITH NOTES** | **STRONG** | **5.638 s** | Packaged real Fashion-MNIST fallback | `105,866` params; validation `0.685 -> 0.762`; hooks removed; optional epoch `0.764` |
| `LAB-D3-03` | **PASS WITH NOTES** | **STRONG** | **4.107 s** | Independently loaded Fashion-MNIST fallback | Baseline `0.998/0.796`, gap `0.201`; dropout `0.985/0.799`, gap `0.186`; remedy correctly rejected |
| `LAB-D3-04` | **PASS WITH NOTES** | **STRONG** | **4.066 s** | Packaged recovery surrogate, not CIFAR/MobileNet | `0` network and CIFAR calls before recovery; scratch `0.7575`; head `0.77125`; explicit claim limits |

Every default local participant path executed end to end from a fresh kernel. No participant-blocking notebook defect was found. The focused support retest passed after the generator guard edit: the no-flag path exits before construction or network access, and canonical CIFAR/MobileNet generation is reachable only with `--download`. Notes remain because a hosted Colab runtime and the opt-in online/full-data branches were unavailable.

### Environment

- macOS on Apple silicon, local CPU
- Python 3.11.8
- NumPy 2.2.4, matplotlib 3.11.1, scikit-learn 1.9.0
- PyTorch 2.6.0, torchvision 0.21.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- Default notebook setting `ALLOW_DOWNLOAD=False`
- No GPU, hosted Colab session, or network required for executed paths

The scientific stack was installed into a fresh temp venv because the workspace's bare Python lacked the course dependencies. All notebook runs used new kernels through nbclient.

### Canonical Notebook Hashes

| Participant notebook | SHA-256 |
|---|---|
| `LAB-D3-01-find-data-leak.ipynb` | `6a0c1905d3d0fc7fdcacd417ae303997ac5d63cccdae77ea140130f0fed43340` |
| `LAB-D3-02-cnn-feature-maps.ipynb` | `0041ce12334e94190c4202f6513a608c7ace0190f4cee934fbb504660f35ae8f` |
| `LAB-D3-03-overfit-and-rescue.ipynb` | `1027482a1674bee5875e6c6e52febed5fd6e8770aad8ec36e73306bd51084e49` |
| `LAB-D3-04-transfer-learning-race.ipynb` | `a7a28eecb783c96c1df2eb8bd4045e2143e63f040fe17c7860424baae0bcf9d0` |

### Execution Coverage

For every lab independently:

1. Validated raw JSON, official nbformat, and every Python code cell's syntax.
2. Confirmed official cell IDs are present and unique, every `metadata.id` matches its official ID uniquely, and every cell has `metadata.language`.
3. Confirmed canonical code cells have no stored outputs or execution counts.
4. Confirmed learner prediction, diagnosis, interpretation, challenge, and reflection fields are blank in the starter.
5. Confirmed no participant artifact links to instructor guides, instructor solutions, answer keys, or solution notebooks. Apparent search hits were harmless substrings such as `case_resolution_code` and “model answered.”
6. Ran each untouched starter in a fresh kernel and confirmed its first intentional response assertion stopped execution before revealing the relevant evidence.
7. Built a fresh temporary participant-completed copy from the current canonical notebook without reading solution files.
8. Completed every core TODO and response, ran practical optional paths, restarted the kernel, and ran all cells in order.
9. Inspected every rendered plot: 2 for D3-01, 4 for D3-02, 2 for D3-03, and 1 for D3-04.
10. Resolved all 36 relative links and anchors across the four notebooks, Student Guide, and challenge file. Every lab launch, prerequisite/activity target, continuation, and debrief link passed.

Temporary completed and executed notebooks remained under `$TMPDIR/day3-independent-completed/`. Canonical notebooks and support files were not edited.

### Clean-Run Timings and Metrics

| Lab | Starter stop | Code cells completed | Wall time | Training/runtime evidence | Final evidence |
|---|---:|---:|---:|---|---|
| D3-01 | Cell 4, `19.660 s` including cold kernel/imports | `12/12` | **3.372 s** | Full lab under 30 s | AUC `0.9960 -> 0.8310`; loader `(64,8)/(64,)` |
| D3-02 | Cell 4, `8.544 s` | `19/19` | **5.638 s** | Core two epochs `0.79 s` | Validation `0.762`; optional third epoch `0.764` |
| D3-03 | Cell 7, `3.102 s` | `15/15` | **4.107 s** | Baseline `0.20 s`; dropout `0.21 s` | Baseline gap `0.201`; remedy gap `0.186`, hypothesis rejected |
| D3-04 | Cell 4, `2.169 s` | `16/16` | **4.066 s** | Scratch `1.070 s`; head `0.174 s`; packaged extraction `0.000 s` | Scratch `0.7575`; recovery head `0.77125` |

### Deliberate Failure and Recovery Results

- **D3-01:** post-outcome proxy plus scaler-before-split produced AUC `0.9960`; removing the proxy and fitting preprocessing only on training produced valid AUC `0.8310`.
- **D3-02:** a three-channel convolution rejected one-channel images; the repaired CNN matched the complete shape trace, trained, captured maps, removed hooks, and displayed correctly indexed errors.
- **D3-03:** enabling dropout, weight decay, and a smaller model together triggered the expected one-change validator. Dropout alone did not meet the declared improvement criterion, and the participant path correctly retained it as a negative result.
- **D3-04:** frozen-random and unmatched-normalization configurations triggered distinct diagnostics. The fallback freeze check produced no backbone gradients, while the temporary/new heads trained normally.

### Support Artifact Audit

All manifest byte sizes and SHA-256 values match the packaged files exactly.

| Artifact | Bytes | SHA-256 | Audited contents |
|---|---:|---|---|
| `fashion_mnist_fallback.npz` | `2,024,650` | `c3fd6c0581b5baf626dfd59e735ac6f787a858a488db4afd09d2e0cbd4294122` | Real Fashion-MNIST `3000/800/800`; uint8 `(28,28)` images; int64 labels; balanced classes |
| `transfer_surrogate_fashion_subset.npz` | `1,761,595` | `605aa62f6b4260203c6d205dac3fac432c434818e77316cc2f254ee84e85c9db` | Recovery images `2400/800/800`; uint8 `(28,28)`; balanced labels |
| `transfer_surrogate_embeddings.npz` | `1,901,816` | `39fd63a657d0a2ecdc2e88c4a512aaea9f55e5af86c424908e7d5250934e6c5a` | Float16 `(2400,256)/(800,256)/(800,256)` plus aligned int64 labels |

Additional support checks passed:

- Manifest source-artifact linkage matches the Fashion-MNIST artifact hash.
- Validation/test recovery images exactly equal the corresponding packaged Fashion-MNIST splits.
- Image and embedding labels align row-for-row in every split.
- All six image splits are exactly class-balanced.
- Re-running `surrogate_features(images, SEED + 5)` reproduced train, validation, and test embedding arrays exactly.
- The feature generator accepts images and a seed, not labels; generation is label-blind.
- NPZ keys contain images, ordinary class labels, class names, seeds, and feature vectors only. They contain no trained head, model checkpoint, predictions, responses, or instructor artifact.

### Generator Finding

**Support contract: PASS.** The focused post-guard retest used Python 3.11.8, NumPy 2.2.4, PyTorch 2.6.0, and torchvision 0.21.0 on local CPU. No canonical dataset, model, or weight download was performed.

- The literal no-flag command ran from an empty temporary working directory with an empty `TORCH_HOME`, exited `2`, named `--download`, `--surrogate-transfer`, and `--skip-transfer`, and created no file, cache, raw-data directory, or output directory.
- An instrumented no-flag run placed tripwires on Fashion-MNIST, CIFAR-10, MobileNet construction, all three generation functions, sockets, URL helpers, and `torch.hub.download_url_to_file`. It recorded **0 construction calls** and **0 network calls** before the same exit.
- `--skip-transfer` with empty temporary source/output directories called Fashion-MNIST once with `train=True` and `download=False`, then reported the expected missing-source `RuntimeError`. It made **0 CIFAR, MobileNet, surrogate, or network calls** and generated no artifact; no generation success is claimed for that absent-source case.
- `--surrogate-transfer --skip-fashion` ran against a temporary copy of packaged `fashion_mnist_fallback.npz`. It made **0 Fashion-MNIST, CIFAR-10, MobileNet, canonical-transfer, or network calls**. Both generated transfer NPZs matched the packaged files byte-for-byte, key-for-key, shape-for-shape, dtype-for-dtype, and array-for-array with maximum absolute numerical difference `0.0`.
- Instrumented enumeration of all eight `--download`/`--surrogate-transfer`/`--skip-transfer` combinations found exactly one canonical route: `download=True`, `surrogate_transfer=False`, and `skip_transfer=False`. The unsafe all-false combination was rejected before routing; surrogate and skip modes never entered canonical generation.

Current generator SHA-256: `baeebb53e85bfe022b72f85fa5f1ca74730a9175d095c91d786dd2432b40a86f`.

The packaged NPZs remained unchanged after the retest:

| Artifact | SHA-256 |
|---|---|
| `fashion_mnist_fallback.npz` | `c3fd6c0581b5baf626dfd59e735ac6f787a858a488db4afd09d2e0cbd4294122` |
| `transfer_surrogate_fashion_subset.npz` | `605aa62f6b4260203c6d205dac3fac432c434818e77316cc2f254ee84e85c9db` |
| `transfer_surrogate_embeddings.npz` | `39fd63a657d0a2ecdc2e88c4a512aaea9f55e5af86c424908e7d5250934e6c5a` |

### Online and Fallback Status

| Lab | Executed default/fallback | Structurally inspected only | Explicitly not validated |
|---|---|---|---|
| D3-01 | Generated local records | N/A | Hosted Colab |
| D3-02 | Packaged real Fashion-MNIST, full mechanics | Cache/opt-in Fashion-MNIST branch | Download, full-split `0.80-0.88`, full throughput, hosted Colab |
| D3-03 | Independent packaged Fashion-MNIST load, baseline + one remedy | Cache/opt-in Fashion-MNIST branch | Online-source metrics/runtime, hosted Colab |
| D3-04 | Recovery images/features, scratch + new head, freeze and scoreboard | Weight enum, `weights.transforms()`, frozen MobileNet, CIFAR split, extraction cache key | CIFAR/MobileNet metrics, downloads, extraction time, cache hit, wrong-normalization degradation, transfer advantage, hosted Colab |

The D3-04 offline-order probe used a unique empty `TORCH_HOME` and recorded **0 socket connections** and **0 CIFAR constructor calls** before recovery. This validates the notebook's default branch order, not the generator's separate behavior.

### Reproducibility and Colab Practicality

- Supplied seeds cover generated/sampled data, model initialization, and shuffled loaders where applicable.
- CPU runtimes are far below the stated live-class limits on the tested host.
- D3-02 through D3-04 require the repository support directory. A notebook uploaded alone to Colab will not find the fallback files; the shared environment guide documents this.
- No GPU-only assumption was found.
- A real hosted Colab runtime was unavailable. The labs are locally CPU-practical but must not be labeled Colab-validated.

### Required Fixes

- None for the tested participant paths or the generator support contract. The no-flag canonical-transfer guard passed the focused retest.

No participant notebook fix is required for the executed default paths.

### Blockers and Notes

- **No blocker:** all four local default participant paths passed.
- **Not executed:** hosted Colab, online Fashion-MNIST modes, and canonical CIFAR-10/MobileNet mode.
- **Do not claim:** online metric bands, MobileNet extraction runtime, cache-hit behavior, wrong-normalization degradation magnitude, or transfer advantage.
- **Support note:** the generator's documented no-download guarantee passed literal-command, instrumented routing, temporary surrogate-regeneration, and packaged-checksum checks. Canonical CIFAR/MobileNet generation itself remains intentionally unexecuted.

### Files Created

- `courseware/reviews/participant-validation-LAB-D3-01.md`
- `courseware/reviews/participant-validation-LAB-D3-02.md`
- `courseware/reviews/participant-validation-LAB-D3-03.md`
- `courseware/reviews/participant-validation-LAB-D3-04.md`
- `courseware/reviews/day-3-participant-lab-summary.md`

### Detailed Reports

- `courseware/reviews/participant-validation-LAB-D3-01.md`
- `courseware/reviews/participant-validation-LAB-D3-02.md`
- `courseware/reviews/participant-validation-LAB-D3-03.md`
- `courseware/reviews/participant-validation-LAB-D3-04.md`

### Retest Requirements

- Execute all four completed paths in a fresh hosted Colab CPU runtime before making a hosted-readiness claim.
- Execute D3-02 and D3-03 from the opt-in Fashion-MNIST source before validating full-mode bands or throughput.
- Execute D3-04 from empty online caches before validating CIFAR/MobileNet metrics, downloads, extraction time, cache behavior, or transfer advantage.
- Re-run the D3-04 no-network/CIFAR-order probe after source-preflight changes.
- Re-run artifact size/hash/schema/determinism checks after any generator or NPZ change.
- Re-run the affected starter, completed copy, plots, links, IDs, and metadata after any participant-notebook change.
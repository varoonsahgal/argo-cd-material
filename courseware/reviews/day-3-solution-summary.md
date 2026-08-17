# PASS WITH NOTES

## Day 3 Instructor Solution Validation Summary

### Status Matrix

| Lab | Status | Final clean run | Source mode | Core evidence |
|---|---|---:|---|---|
| `LAB-D3-01` | **PASS** | **3.196 s** | Generated local records | AUC `0.9960 -> 0.8310`; proxy removed; train-only scaling; optional loader `(64,8)/(64,)` |
| `LAB-D3-02` | **PASS WITH NOTES** | **5.198 s** | Packaged real Fashion-MNIST fallback | `105,866` params; validation `0.685 -> 0.762`; hooks removed; optional epoch `0.764` |
| `LAB-D3-03` | **PASS WITH NOTES** | **3.924 s** | Independently loaded Fashion-MNIST fallback | Baseline `0.998/0.796`, gap `0.201`; dropout `0.985/0.799`, gap `0.186`; remedy rejected |
| `LAB-D3-04` | **PASS WITH NOTES** | **3.830 s** | Packaged recovery surrogate, not CIFAR/MobileNet | zero network/CIFAR calls; scratch `0.7575`; head `0.77125`; no transfer-advantage claim |

All four solutions completed Clear Outputs -> new CPU kernel -> Run All. Every deliberate failure was caught, every final checkpoint passed, and only final clean-run outputs remain stored.

### Environment

- macOS on Apple silicon
- Python 3.11.8
- NumPy 2.2.4, matplotlib 3.11.1, scikit-learn 1.9.0
- PyTorch 2.6.0, torchvision 0.21.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- CPU required; `ALLOW_DOWNLOAD=False`; D3-04 used a unique empty `TORCH_HOME`
- Current torchvision multi-weight API source-checked on 2026-08-16

### Solution Hashes

| Solution | SHA-256 |
|---|---|
| `LAB-D3-01-find-data-leak-SOLUTION.ipynb` | `b6ed5ca29064fa05b6bc93085d2016090504410c260b178aeec35760953d2246` |
| `LAB-D3-02-cnn-feature-maps-SOLUTION.ipynb` | `7b2ace4c8bc2b11eed56aa1d93d921e327f1083cbc763312715dac699ee14310` |
| `LAB-D3-03-overfit-and-rescue-SOLUTION.ipynb` | `523719da936ea925cef8670e067da97b0cc6703d209fdb5d41be08f3cf88724c` |
| `LAB-D3-04-transfer-learning-race-SOLUTION.ipynb` | `12da6f1c7cd26ad737e2370377c181f272a9e473b31d39ab92705f860b1352a1` |

### Frozen Participant Hashes

| Participant notebook | SHA-256 | Report match |
|---|---|---|
| `LAB-D3-01-find-data-leak.ipynb` | `6a0c1905d3d0fc7fdcacd417ae303997ac5d63cccdae77ea140130f0fed43340` | Exact |
| `LAB-D3-02-cnn-feature-maps.ipynb` | `0041ce12334e94190c4202f6513a608c7ace0190f4cee934fbb504660f35ae8f` | Exact |
| `LAB-D3-03-overfit-and-rescue.ipynb` | `1027482a1674bee5875e6c6e52febed5fd6e8770aad8ec36e73306bd51084e49` | Exact |
| `LAB-D3-04-transfer-learning-race.ipynb` | `a7a28eecb783c96c1df2eb8bd4045e2143e63f040fe17c7860424baae0bcf9d0` | Exact |

### Execution Coverage

| Lab | Code cells | Plots | Deliberate failure/recovery | Practical optional path |
|---|---:|---:|---|---|
| D3-01 | `12/12` | 2 | two leak paths exposed and repaired | DataLoader shape/shuffle check executed |
| D3-02 | `19/19` | 4 | wrong input channels caught and repaired | third epoch executed |
| D3-03 | `15/15` | 2 | three-remedy confound caught; one remedy retained | augmentation design completed, not added to core run |
| D3-04 | `16/16` | 1 | frozen-random and wrong-normalization diagnoses caught | partial fine-tuning plan completed, not executed in recovery |

Every prediction, diagnosis, implementation, calculation, interpretation, challenge, reflection, and checkpoint in the participant structure is completed. Each solution adds instructor reasoning for mechanism, expected visuals and calibrated evidence, hint ladders, misconceptions, discussion triggers, troubleshooting, live recovery, acceptable alternatives, and CPU/GPU/network/cache differences.

### Source-Mode Dispositions

| Lab | Executed | Structurally checked | Not validated |
|---|---|---|---|
| D3-01 | Generated local records | N/A | Hosted Colab |
| D3-02 | Packaged real Fashion-MNIST fallback | cache/opt-in Fashion-MNIST branch | online/full-data band and throughput; hosted Colab |
| D3-03 | Independent packaged Fashion-MNIST fallback | cache/opt-in Fashion-MNIST branch | online-source metrics/runtime; hosted Colab |
| D3-04 | Recovery images/features, scratch and fresh head, freeze and scoreboard | weight enum, `weights.transforms()`, frozen MobileNet, CIFAR split, extraction/cache key | all canonical CIFAR/MobileNet metrics, timings, cache behavior, degradation magnitude, and winner; hosted Colab |

D3-02 and D3-03 fallback metrics are not presented as validation of online/full-data bands. D3-04 recovery is explicitly not CIFAR-10, not MobileNet output, not a canonical cache hit, and not evidence that transfer wins.

### No-Download Verification

- D3-04 final execution used `ALLOW_DOWNLOAD=False` and an empty Torch cache.
- A separate fresh-kernel probe blocked socket connections and CIFAR construction.
- Observed before and through recovery: **0 network attempts**, **0 CIFAR constructor calls**.
- The support generator's no-flag guard exited `2` before file creation and directed the operator to `--download`, `--surrogate-transfer`, or `--skip-transfer`.
- Online branches were recorded as unexecuted.

### Support Artifact Integrity

| Artifact | SHA-256 | Manifest match |
|---|---|---|
| `fashion_mnist_fallback.npz` | `c3fd6c0581b5baf626dfd59e735ac6f787a858a488db4afd09d2e0cbd4294122` | Exact |
| `transfer_surrogate_fashion_subset.npz` | `605aa62f6b4260203c6d205dac3fac432c434818e77316cc2f254ee84e85c9db` | Exact |
| `transfer_surrogate_embeddings.npz` | `39fd63a657d0a2ecdc2e88c4a512aaea9f55e5af86c424908e7d5250934e6c5a` | Exact |

The support package remains participant-safe: images, labels, and label-blind feature vectors only. No trained head, predictions, completed responses, or instructor content was added.

### Notebook and Separation Audit

- Official notebook validation passed for all four solutions.
- Cell IDs are unique; every official ID equals `metadata.id`; every cell has `metadata.language`.
- Executed code cells: `62/62`; error outputs: `0`; rendered plots: `9`.
- All 20 relative solution links and anchors resolve from the instructor directory.
- Participant notebook hashes exactly match the existing D3-01 through D3-04 reports.
- Participant-tree leakage scan returned zero matches for instructor paths, answer keys, model answers, or solution notebooks.
- No participant notebook or support artifact was edited.

### Issues and Notes

- No participant contradiction was exposed; no lab required failure routing to the Course Orchestrator.
- The previous support-generator no-flag concern is now guarded in the current source and passed the zero-file probe.
- Hosted Colab was unavailable.
- D3-02/D3-03 online data paths and D3-04 canonical CIFAR/MobileNet path remain the only substantive execution gaps.

### Final Status

**PASS WITH NOTES** - all four offline/default instructor solutions are complete, executable, correctly separated, and instructor-ready. Notes are limited to explicitly unexecuted online/full-data and hosted Colab paths.

### Detailed Reports

- `courseware/reviews/solution-validation-LAB-D3-01.md`
- `courseware/reviews/solution-validation-LAB-D3-02.md`
- `courseware/reviews/solution-validation-LAB-D3-03.md`
- `courseware/reviews/solution-validation-LAB-D3-04.md`
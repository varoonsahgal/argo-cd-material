# Student Lab Test Report

**Validation date:** 2026-08-17  
**Rollup status:** **FAIL - current-hash and report-consistency gate**

All 16 canonical participant notebooks have a current detailed report, and every report's controlling disposition is **PASS WITH NOTES**. There are no active **FAIL** or **RETEST** lab dispositions. The course-level rollup nevertheless fails because three current Day 2 notebook hashes do not match the hashes named by their reports, and three Day 1 report files append stale **FAIL** reports after their current passing retests. Those are evidence-integrity blockers, not acceptable release notes.

**PASS WITH NOTES acceptance rule:** this rollup accepts **PASS WITH NOTES** only for nonblocking environment, accessibility, or release-process qualifications. Examples are an unexecuted hosted Colab run, host-specific latency, minor readable label overlap, an unexecuted exact framework version, or external release-packaging enforcement. A current notebook/report hash mismatch or contradictory active/stale status content is not accepted as a note.

## Coverage Summary

| Check | Result |
|---|---:|
| Required lab IDs | 16/16, `LAB-D1-01` through `LAB-D4-04` |
| Current detailed participant reports | 16/16, exactly one file per lab ID |
| Canonical participant notebooks hashed from current bytes | 16/16 |
| Active report dispositions | 16 **PASS WITH NOTES**, 0 **PASS**, 0 active **FAIL**, 0 active **RETEST** |
| Interestingness | 16 **STRONG**, 0 **ACCEPTABLE**, 0 **WEAK** |
| Current hashes matching a hash in the participant report | 9/16 |
| Current hashes mismatching the participant report | 3/16: D2-01, D2-02, D2-03 |
| Participant reports with no canonical hash field | 4/16: all Day 1 reports |
| Hosted Google Colab executions | 0/16; no hosted-validation claim |

The Day 1 current hashes are corroborated by the later instructor-solution validation records, but they are not recorded in the four participant reports themselves. That is weaker traceability than a participant-report hash match and is reported as such.

## Lab Matrix

| Lab and participant path | Reported status | Detailed report | Tested environment and source mode | Completed clean runtime | Key execution evidence | Current SHA-256 | Unresolved notes |
|---|---|---|---|---:|---|---|---|
| `LAB-D1-01` [One-Neuron Boundary Workshop](../day-1/labs/LAB-D1-01-neuron-boundary.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D1-01.md) | macOS Apple silicon, local CPU; Python 3.11.8; NumPy 2.4.6; generated in memory; no notebook network/GPU | **2.421 s** | Baseline `10/12`, manual `12/12`, extension `40/40`; scaling invariant; vertical and near-vertical contours passed | `5ddc67e0f9e082e672fa5c4e34bf74beb2f946f9b08f75651bd2978342a02b0a` | Participant report has no hash and appends a stale **FAIL** report after the current retest. Hosted Colab not run; readable label overlap remains. |
| `LAB-D1-02` [The Linear Limit](../day-1/labs/LAB-D1-02-linear-limit.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D1-02.md) | macOS Apple silicon, local CPU; Python 3.11.8; NumPy 2.4.6/scikit-learn 1.9.0; generated in memory; no notebook network/GPU | **3.094 s** | Blobs `1.000`; XOR logistic `0.500`; fixed ReLU `1.000`; same-parameter identity control `0.500` | `a608f0f83a7915a4a683dbca0cb53ad7c47bb9a8a0322bdacf6471e8734ceb8d` | Participant report has no hash and appends a stale **FAIL** report after the current retest. Hosted Colab not run; readable label overlap remains. |
| `LAB-D1-03` [Shape and Activation Observatory](../day-1/labs/LAB-D1-03-shapes-activations.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D1-03.md) | Fresh local CPU venv; Python 3.11.8; NumPy 2.4.6; in-memory arrays; network used only to install documented pins | **1.753 s core**; **1.422 s with optional** | `67` parameters; `(5,8)` and `(5,3)` shapes; stable softmax; wrong-axis assertion failed and recovered; optional branch independently skippable | `8dc99076c5aaba05673f7c6d5388e1bc519f33dc366ac592b91bfbc33f61511e` | Participant report has no hash. Day 1 summary says `1.556 s`, which does not match either detailed clean-run value. Hosted Colab not run. |
| `LAB-D1-04` [Forward Network Mystery](../day-1/labs/LAB-D1-04-forward-network-mystery.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D1-04.md) | macOS Apple silicon, local CPU; Python 3.11.8; NumPy 2.4.6/scikit-learn 1.9.0; generated data and fixed parameters; no network/GPU | **3.382 s** | Accuracy `0.9111`; exact `4/2` probe pattern; transpose mismatch recovered; mesh parity and copied-parameter immutability passed | `51829b6e07b6eeb79152fbc5f358fce49d017924967c330073ff3c825ac1f44e` | Participant report has no hash and appends a stale **FAIL** report after the current retest. Hosted Colab not run; readable label overlap remains. |
| `LAB-D2-01` [Loss Landscapes and Learning-Rate Roulette](../day-2/labs/LAB-D2-01-loss-learning-rate.ipynb) | **PASS WITH NOTES**, not accepted for current bytes | [Participant validation](../reviews/participant-validation-LAB-D2-01.md) | macOS Apple silicon, local CPU; Python 3.11.8; NumPy 2.4.6; deterministic in-memory path; no network/GPU | **1.509 s** | Finite clipped BCE; equal-accuracy/different-loss evidence; crawl, smooth, oscillatory, and divergent trajectories; endpoint recovery | `d7ee72d824676ae32c6eac8f55693fb48c3b91d8f398fdfadb0dec5f95560400` | **Blocking:** report and Day 2 summary name `8779f5d7...6488c3`, not the current hash. Current bytes require a fresh completed-path retest or an evidence-preserving hash reconciliation. Hosted Colab not run. |
| `LAB-D2-02` [Backpropagation and Gradient Check](../day-2/labs/LAB-D2-02-backprop-gradient-check.ipynb) | **PASS WITH NOTES**, not accepted for current bytes | [Participant validation](../reviews/participant-validation-LAB-D2-02.md) | macOS Apple silicon, local CPU; Python 3.11.8; NumPy 2.4.6 float64; no network/GPU | **1.435 s** | Maximum relative error `1.012e-09`; sign and missing-factor defects localized; negative-gradient update lowered loss | `a2cfee7ba3f9597d54a098bcf7e835d6069ec51927aea72638dcfda0d3e73143` | **Blocking:** report and Day 2 summary name `45708d63...aeca2ca`, not the current hash. Current bytes require a fresh completed-path retest or an evidence-preserving hash reconciliation. Hosted Colab not run. |
| `LAB-D2-03` [Train a Neural Network with NumPy](../day-2/labs/LAB-D2-03-numpy-training.ipynb) | **PASS WITH NOTES**, not accepted for current bytes | [Participant validation](../reviews/participant-validation-LAB-D2-03.md) | macOS Apple silicon, local CPU; Python 3.11.8; NumPy 2.4.6/scikit-learn 1.9.0; generated moons; no network/GPU | **4.257 s** | Initial BCE `0.6860`; validation accuracy `0.905`; bounded NaN recovery; identity/high-rate diagnostics; isolated one-change experiment | `d1e427ffbcb40bbe2f81702d096dc859ac841e7627e83c20ff87577bf1a24089` | **Blocking:** report and Day 2 summary name `18a5b0a6...3010a`, not the current hash. Current bytes require a fresh completed-path retest or an evidence-preserving hash reconciliation. Hosted Colab not run. |
| `LAB-D2-04` [PyTorch Autograd: Break It and Fix It](../day-2/labs/LAB-D2-04-pytorch-break-fix.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D2-04.md) | macOS Apple silicon, required CPU; Python 3.11.8; PyTorch 2.6.0; card B current-hash run; APIs source-checked for 2.11 | **5.373 s** | Baseline `0.900`; omitted-reset card B `0.690`/max norm `6.828`; repaired `0.895`/max norm `0.286`; mode/grad probes passed | `b3dfb495468ac7ec05c41df9ee4bbe49b11620f1c28504425ab02cbd852e0d52` | Hosted Colab and exact PyTorch 2.11 runtime not run. Cards A, C, and D were not rerun in the current correction-focused retest. |
| `LAB-D3-01` [Find the Data Leak](../day-3/labs/LAB-D3-01-find-data-leak.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D3-01.md) | macOS Apple silicon, local CPU; Python 3.11.8; NumPy 2.2.4/scikit-learn 1.9.0; generated local records; offline | **3.372 s** | Leaky AUC `0.9960`; repaired AUC `0.8310`; proxy removed; stratified `60/20/20`; train-only scaling passed | `6a0c1905d3d0fc7fdcacd417ae303997ac5d63cccdae77ea140130f0fed43340` | Hosted Colab not run. No online branch exists for the tested core path. |
| `LAB-D3-02` [Compact CNN and Feature Maps](../day-3/labs/LAB-D3-02-cnn-feature-maps.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D3-02.md) | macOS Apple silicon, CPU; PyTorch 2.6.0/torchvision 0.21.0; `ALLOW_DOWNLOAD=False`; packaged real Fashion-MNIST fallback | **5.638 s** | One-channel repair; `105,866` parameters; validation `0.762`; hooks removed; optional epoch `0.764` | `0041ce12334e94190c4202f6513a608c7ace0190f4cee934fbb504660f35ae8f` | Hosted Colab and opt-in/full Fashion-MNIST branch not run. Full-split metric band and throughput are not validated; support directory is required. |
| `LAB-D3-03` [Make It Overfit, Then Rescue It](../day-3/labs/LAB-D3-03-overfit-and-rescue.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D3-03.md) | macOS Apple silicon, CPU; PyTorch 2.6.0/torchvision 0.21.0; independently loaded packaged Fashion-MNIST fallback | **4.107 s** | Baseline `0.998/0.796`, gap `0.201`; three-remedy draft rejected; dropout result correctly rejected against predeclared criterion | `1027482a1674bee5875e6c6e52febed5fd6e8770aad8ec36e73306bd51084e49` | Hosted Colab and opt-in Fashion-MNIST branch not run. Online-source metrics/runtime are not validated; support directory is required. |
| `LAB-D3-04` [Transfer-Learning Race](../day-3/labs/LAB-D3-04-transfer-learning-race.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D3-04.md) | macOS Apple silicon, CPU; PyTorch 2.6.0/torchvision 0.21.0; packaged recovery surrogate, explicitly not CIFAR-10/MobileNet | **4.066 s** | Invalid transfer diagnoses passed; `0` network/CIFAR calls before recovery; scratch `0.7575`; head `0.77125`; freeze/cache evidence passed | `a7a28eecb783c96c1df2eb8bd4045e2143e63f040fe17c7860424baae0bcf9d0` | Hosted Colab and canonical CIFAR-10/MobileNet branch not run. No online metrics, extraction/cache runtime, wrong-normalization magnitude, or transfer-advantage claim. |
| `LAB-D4-01` [Accuracy Is Not Enough](../day-4/labs/LAB-D4-01-accuracy-is-not-enough.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D4-01.md) | Fresh local CPU venv/kernel; Python 3.11.8; NumPy 2.4.6/scikit-learn 1.9.0; generated data; no network | **2.864 s** | Majority accuracy `0.9539` with recall/F1 `0`; useful recall `0.6627`; cost thresholds `0.19/0.43`; optional `0.26` | `08a02a0ed4ec7866dd208192193903e8455839cba8910003c086ce04c16deff1` | Hosted Colab not run. Bare system Python lacked `nbformat`; documented isolated setup succeeded. |
| `LAB-D4-02` [Model Detective](../day-4/labs/LAB-D4-02-model-detective.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D4-02.md) | Fresh local CPU venv/kernel; fixed checksum-verified digits evidence; no network | **2.805 s** | Accuracy `0.9526`; `(10,10)` confusion; 17 aligned errors; exclusive buckets account for `17/17`; unsupported draft recovered | `259d689bd44501d761f2190e4e04f9bc0caa974179536cd67cb2c95dd24d74ff` | Hosted Colab not run; notebook alone is insufficient without the shared Day 4 data directory. |
| `LAB-D4-03` [You Get One Experiment](../day-4/labs/LAB-D4-03-one-experiment.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D4-03.md) | Fresh local CPU venv/kernel; PyTorch 2.6.0; fixed digits split/baseline; no network/GPU | **4.527 s** | Confounded draft rejected; two fresh runs identical; accepted negative intervention `0.8496`; complete serializable evidence record | `bd32475e6cdd08db0b1c552c218472536b50596c20b191d2ece6b9420b0d207e` | Hosted Colab not run. Exact latency values are host-specific and are not production claims. |
| `LAB-D4-04` [Capstone Starter](../capstone/capstone-starter.ipynb) | **PASS WITH NOTES** | [Participant validation](../reviews/participant-validation-LAB-D4-04.md) | Fresh local CPU venv; PyTorch 2.6.0; independent A/B/C live and exact-fingerprint recovery kernels; fixed packaged evidence; no network/GPU | **3.972-4.948 s live/profile**; **3.182-3.393 s recovery/profile** | A/B/C targets passed; one major change; early test denied; test used once after frozen decision; recovery withheld test evidence; rubric and release separation passed | `a191355d19d2dc64810cde7591fcee9dd1865116f70a04a7dbf2ba8b9c5462a4` | Hash exactly matches required `a191355d...5462a4`. Hosted Colab not run; external participant packaging must enforce release exclusions. |

## Current-Hash Reconciliation

The final SHA-256 check read the current bytes of all 16 canonical participant notebooks. No notebook was edited.

| Lab | Hash recorded by participant report | Current hash | Result |
|---|---|---|---|
| D1-01 | Not recorded | `5ddc67e0f9e082e672fa5c4e34bf74beb2f946f9b08f75651bd2978342a02b0a` | Current digest captured; participant-report binding absent |
| D1-02 | Not recorded | `a608f0f83a7915a4a683dbca0cb53ad7c47bb9a8a0322bdacf6471e8734ceb8d` | Current digest captured; participant-report binding absent |
| D1-03 | Not recorded | `8dc99076c5aaba05673f7c6d5388e1bc519f33dc366ac592b91bfbc33f61511e` | Current digest captured; participant-report binding absent |
| D1-04 | Not recorded | `51829b6e07b6eeb79152fbc5f358fce49d017924967c330073ff3c825ac1f44e` | Current digest captured; participant-report binding absent |
| D2-01 | `8779f5d76a66e8aa209be3668a1dbad23745be5a0e0016075a8f15a18f6488c3` | `d7ee72d824676ae32c6eac8f55693fb48c3b91d8f398fdfadb0dec5f95560400` | **MISMATCH** |
| D2-02 | `45708d638d16a5529bd8e460758d2d1c9c8d512061a0d917e9c293f72aeca2ca` | `a2cfee7ba3f9597d54a098bcf7e835d6069ec51927aea72638dcfda0d3e73143` | **MISMATCH** |
| D2-03 | `18a5b0a63ae261fae428936899d5e66513fe9ebef8cdde182aae011237a3010a` | `d1e427ffbcb40bbe2f81702d096dc859ac841e7627e83c20ff87577bf1a24089` | **MISMATCH** |
| D2-04 | `b3dfb495468ac7ec05c41df9ee4bbe49b11620f1c28504425ab02cbd852e0d52` | Same | Match |
| D3-01 | `6a0c1905d3d0fc7fdcacd417ae303997ac5d63cccdae77ea140130f0fed43340` | Same | Match |
| D3-02 | `0041ce12334e94190c4202f6513a608c7ace0190f4cee934fbb504660f35ae8f` | Same | Match |
| D3-03 | `1027482a1674bee5875e6c6e52febed5fd6e8770aad8ec36e73306bd51084e49` | Same | Match |
| D3-04 | `a7a28eecb783c96c1df2eb8bd4045e2143e63f040fe17c7860424baae0bcf9d0` | Same | Match |
| D4-01 | `08a02a0ed4ec7866dd208192193903e8455839cba8910003c086ce04c16deff1` | Same | Match |
| D4-02 | `259d689bd44501d761f2190e4e04f9bc0caa974179536cd67cb2c95dd24d74ff` | Same | Match |
| D4-03 | `bd32475e6cdd08db0b1c552c218472536b50596c20b191d2ece6b9420b0d207e` | Same | Match |
| D4-04 | `a191355d19d2dc64810cde7591fcee9dd1865116f70a04a7dbf2ba8b9c5462a4` | Same | Match; required digest confirmed |

## Deliberate Failures and Recoveries

All 16 reports include executable diagnostic, failure, negative-result, or recovery evidence rather than only a happy-path run.

- **Day 1:** ambiguous multi-parameter evidence and vertical boundaries; XOR linear limitation versus nonlinear/identity controls; wrong-axis softmax failure/recovery; transpose mismatch/recovery and immutable perturbation.
- **Day 2:** naive endpoint BCE versus clipping; sign and missing-factor gradient defects; bounded NaN, identity, and high-rate diagnostics; omitted gradient reset and one-field repair.
- **Day 3:** post-outcome/scaler leakage and ownership repair; channel mismatch and CNN repair; rejected confounded remedies plus an accepted negative result; frozen-random/wrong-normalization diagnostics and offline recovery.
- **Day 4:** high-accuracy majority failure; unsupported error-bucket inference recovery; rejected multi-change experiment plus a preserved negative result; capstone test lock, one-change gate, A/B/C live paths, and validation-only cached recovery.

The negative intervention results in D3-03 and D4-03 are valid learning evidence because their checkpoints reward predeclared, controlled reasoning rather than mandatory metric improvement.

## Offline, Online, and Colab Boundaries

- Days 1 and 2 use generated or in-memory data and required no notebook network access. Package installation can still require network access.
- D3-01's generated local-record path ran offline.
- D3-02 and D3-03 ran the packaged real Fashion-MNIST fallback. Their opt-in cache/download and full-data modes were not executed.
- D3-04 ran the packaged recovery surrogate. It is not CIFAR-10 or MobileNet evidence. The canonical online branch was structurally inspected only.
- Day 4 ran generated data or checksum-verified packaged digits evidence with no network.
- No lab was executed in a hosted Google Colab session. Local CPU practicality does not constitute hosted validation. D3-02 through D3-04 and D4-02/D4-04 require their shared data directories when moved to another environment.
- Local PyTorch execution used 2.6.0 and Day 3 used torchvision 0.21.0. D2-04's relevant APIs were checked against PyTorch 2.11 documentation, but no exact PyTorch 2.11 runtime was executed. No exact-2.11 runtime claim is made.
- No exact framework runtime is generalized beyond the versions and paths explicitly executed in each detailed report.

## Stale and Contradictory Evidence

1. `participant-validation-LAB-D1-01.md`, `participant-validation-LAB-D1-02.md`, and `participant-validation-LAB-D1-04.md` each start with a current passing retest but append the superseded failing report in the same file. The active second-gate status is **PASS WITH NOTES**, but the files do not present one unambiguous current report body.
2. The D1-03 detailed report records a `1.753 s` strict-core clean run and a `1.422 s` full optional run, while the Day 1 summary records `1.556 s`. The detailed values control this rollup; the summary value is unreconciled.
3. D2-01, D2-02, and D2-03 current notebook hashes differ from the hashes identified as current in both their detailed reports and the Day 2 participant summary. The prior execution results are not accepted as proof for the current bytes.
4. The Day 1 participant reports omit canonical hashes. Their current bytes are corroborated only by later solution-validation records, not by their own participant reports.

## Source Records

- [Shared lab environment](../shared/environment.md)
- [Canonical lab map](../00-course-design/lab-map.md)
- [Day 1 participant summary](../reviews/day-1-participant-lab-summary.md)
- [Day 2 participant summary](../reviews/day-2-participant-lab-summary.md)
- [Day 3 participant summary](../reviews/day-3-participant-lab-summary.md)
- [Day 4 participant summary](../reviews/day-4-participant-lab-summary.md)

## Required Retest and Cleanup

1. Re-execute D2-01, D2-02, and D2-03 from their current hashes through the completed participant paths, deliberate failures/recoveries, plots, links, and checkpoints; then update their detailed reports and Day 2 summary.
2. Replace the three concatenated Day 1 report files with one unambiguous current report body apiece and add the current canonical SHA-256 to all four Day 1 participant reports.
3. Reconcile the D1-03 clean runtime in the Day 1 summary with the controlling detailed report.
4. Recompute all 16 hashes and regenerate this rollup. The rollup may move to **PASS WITH NOTES** only after the hash/report blockers are closed; hosted Colab and the explicitly unexecuted online/exact-version paths may remain nonblocking notes if their claim boundaries stay explicit.
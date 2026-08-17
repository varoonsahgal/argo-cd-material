# Instructor-Solution Test Report

**Validation date:** 2026-08-17  
**Overall status:** **PASS WITH NOTES - 16/16 solution reports are PASS-family; 3 participant-hash attestations require RETEST**

This rollup reconciles the 16 current solution-validation reports, four day solution summaries, the primary lab map, current participant validation reports and hashes, and every canonical solution notebook. It does not rerun the notebooks; clean-kernel evidence and runtimes below come from the linked detailed reports. SHA-256 values, canonical-path counts, D4-04 uniqueness, and current leakage terms were checked against the current tree for this rollup.

## Gate Summary

| Check | Result |
|---|---|
| Lab-map contract | **16 labs**: four per day; one participant lab and one canonical solution per lab |
| Canonical solution inventory | **16 total**: 15 notebooks under `courseware/instructor-solutions/day-X/` and only D4-04 at `courseware/capstone/capstone-solution.ipynb` |
| Duplicate capstone/D4-04 solution | **None found**; the only solution notebook is the canonical capstone solution |
| Detailed solution reports | **16/16 present** |
| Reported solution statuses | **4 PASS**, **12 PASS WITH NOTES**, **0 FAIL**, **0 current solution RETEST** |
| Current solution hashes | **16 recomputed**; all 13 reports that record a final solution SHA-256 match exactly; D1-01, D1-02, and D1-04 reports do not record a solution hash |
| Clean-kernel execution | **16/16 reported complete** with fresh kernels, ordered execution, zero uncaught errors, and passing final checkpoints |
| Task coverage | **16/16 reported complete** for required TODOs, questions, predictions, diagnoses, challenges, reflections, deliberate failures/recoveries, and practical optional paths |
| Participant hash attestation | **13 exact/prefix matches; 3 mismatches requiring RETEST**: D2-01, D2-02, and D2-03 |
| Participant leakage | Existing day/report scans report **NONE**; current-tree scan found no instructor path, answer-key, model-answer, or solution-notebook reference in participant lab/capstone trees |
| Required D4-04 hashes | Participant `a191355d19d2dc64810cde7591fcee9dd1865116f70a04a7dbf2ba8b9c5462a4`; solution `30ce02c6208996d829086da78726dcf41c9cf5486c28cdbfab44d17fb2589e27` - **both exact** |

The three participant-hash mismatches do not change the linked solution reports' clean-run results or current solution hashes. They do invalidate the reports' claim that the participant bytes are still frozen, so participant/solution parity and the participant completed-path checks for D2-01 through D2-03 must be rerun before a fully current paired gate can be claimed.

## Day 1 Pairing

| Lab | Canonical solution and report | Status / clean runtime | Key evidence and branches | Current hashes / separation | Notes |
|---|---|---|---|---|---|
| `LAB-D1-01` | [Solution](../instructor-solutions/day-1/LAB-D1-01-neuron-boundary-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D1-01.md) | **PASS WITH NOTES**<br>2.438 s | 17/17 code cells; baseline `10/12`; controlled manual `12/12`; extension `40/40`; scaling invariance; vertical/near-vertical checks; threshold extension | Solution `368ca163c20362daaf0453ee384f63f2f8f40037b944efabc437d620e34a0fa9` (**not recorded in report**)<br>Participant `5ddc67e0f9e082e672fa5c4e34bf74beb2f946f9b08f75651bd2978342a02b0a` (**recorded prefix matches**)<br>Leakage: **NONE** | Non-blocking prior participant-report threshold-count discrepancy; hosted Colab unexecuted |
| `LAB-D1-02` | [Solution](../instructor-solutions/day-1/LAB-D1-02-linear-limit-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D1-02.md) | **PASS**<br>2.804 s | 17/17; blobs `1.000`; XOR `0.500` at both iteration budgets; nonlinear `1.000`; identity control `0.500`; copied-parameter extension | Solution `aa2a0f99ecadf4fc0746bdb1b79403637fbbffab34a81969117f8332a5e3c15c` (**not recorded in report**)<br>Participant `a608f0f83a7915a4a683dbca0cb53ad7c47bb9a8a0322bdacf6471e8734ceb8d` (**recorded prefix matches**)<br>Leakage: **NONE** | Hosted Colab unexecuted |
| `LAB-D1-03` | [Solution](../instructor-solutions/day-1/LAB-D1-03-shapes-activations-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D1-03.md) | **PASS**<br>2.09 s full; 1.668 s strict core | 17/17 full; 16/16 strict core; 67 parameters; `(5,8)` and `(5,3)` shapes; stable softmax; wrong-axis failure/recovery; optional Leaky ReLU independently skippable | Solution `5920d4c93af1435294ab146056ca56db459560a6f9a671dffa381c8c72b1e8dd` (**exact report match**)<br>Participant `8dc99076c5aaba05673f7c6d5388e1bc519f33dc366ac592b91bfbc33f61511e` (**exact**)<br>Leakage: **NONE** | Core contains no optional symbol or dependency; hosted Colab unexecuted |
| `LAB-D1-04` | [Solution](../instructor-solutions/day-1/LAB-D1-04-forward-network-mystery-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D1-04.md) | **PASS**<br>2.861 s | 17/17; held-out `0.9111`; named probes exactly `4/6`; transpose failure/recovery; mesh parity; positive and opposite copied-bias perturbations | Solution `105e32189da4463440c05c202ac983bd5683cb27ce6980c17846887e1bab4568` (**not recorded in report**)<br>Participant `51829b6e07b6eeb79152fbc5f358fce49d017924967c330073ff3c825ac1f44e` (**recorded prefix matches**)<br>Leakage: **NONE** | Earlier solution helper defect was fixed and rerun; hosted Colab unexecuted |

## Day 2 Pairing

| Lab | Canonical solution and report | Status / clean runtime | Key evidence and branches | Current hashes / separation | Notes |
|---|---|---|---|---|---|
| `LAB-D2-01` | [Solution](../instructor-solutions/day-2/LAB-D2-01-loss-learning-rate-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D2-01.md) | **PASS WITH NOTES**<br>1.754 s | 16/16; finite clipped BCE; crawl/smooth/oscillate/diverge paths; `0.60` challenge; curvature extension | Solution `3e4a9f2f1902625e6f416ca1014ca4ed2375563af21cf788fa8d82a4555de630` (**exact report match**)<br>Participant current `d7ee72d824676ae32c6eac8f55693fb48c3b91d8f398fdfadb0dec5f95560400`; reports assert `8779f5d76a66e8aa209be3668a1dbad23745be5a0e0016075a8f15a18f6488c3` (**MISMATCH**)<br>Current leakage scan: **NONE** | **RETEST participant pairing**; hosted Colab unexecuted |
| `LAB-D2-02` | [Solution](../instructor-solutions/day-2/LAB-D2-02-backprop-gradient-check-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D2-02.md) | **PASS WITH NOTES**<br>1.691 s | 18/18; max gradient error `1.012e-09`; sign and missing-factor defects localized; loss-lowering update; perturbation and epsilon sweep | Solution `6bd54fd53c800f2a1dcd0c6ddecad0c60f0cb32be6e6ad3c852eaf1eb56fc114` (**exact report match**)<br>Participant current `a2cfee7ba3f9597d54a098bcf7e835d6069ec51927aea72638dcfda0d3e73143`; reports assert `45708d638d16a5529bd8e460758d2d1c9c8d512061a0d917e9c293f72aeca2ca` (**MISMATCH**)<br>Current leakage scan: **NONE** | **RETEST participant pairing**; hosted Colab unexecuted |
| `LAB-D2-03` | [Solution](../instructor-solutions/day-2/LAB-D2-03-numpy-training-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D2-03.md) | **PASS WITH NOTES**<br>4.488 s | 23/23; initial BCE `0.6860`; validation `0.1820/0.905`; NaN recovery; identity/high-rate failures; isolated LR and width branches | Solution `510cca4fcb44b2e12f447ca1f4eeb64a2716101314cd8455dc9ec4462cd33135` (**exact report match**)<br>Participant current `d1e427ffbcb40bbe2f81702d096dc859ac841e7627e83c20ff87577bf1a24089`; reports assert `18a5b0a63ae261fae428936899d5e66513fe9ebef8cdde182aae011237a3010a` (**MISMATCH**)<br>Current leakage scan: **NONE** | **RETEST participant pairing**; optional width narrative was calibrated and rerun; hosted Colab unexecuted |
| `LAB-D2-04` | [Solution](../instructor-solutions/day-2/LAB-D2-04-pytorch-break-fix-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D2-04.md) | **PASS WITH NOTES**<br>7.795 s | 21/21; baseline `0.900`; all defect cards A-D; plain-reset `None`, explicit-zero, unused-gradient and optimizer probes; mode/context and shape recovery | Solution `2c6510bdc00acb8ca415f8c0d7e520dd4abfed3c31e81165b5e9d1cf9ff4de51` (**exact report match**)<br>Participant `b3dfb495468ac7ec05c41df9ee4bbe49b11620f1c28504425ab02cbd852e0d52` (**exact**)<br>Leakage: **NONE** | Hosted Colab and exact PyTorch 2.11 runtime unexecuted; API was source-checked and run on PyTorch 2.6.0 |

## Day 3 Pairing

| Lab | Canonical solution and report | Status / clean runtime | Key evidence and branches | Current hashes / separation | Notes |
|---|---|---|---|---|---|
| `LAB-D3-01` | [Solution](../instructor-solutions/day-3/LAB-D3-01-find-data-leak-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D3-01.md) | **PASS**<br>3.196 s | 12/12; generated records; AUC `0.9960 -> 0.8310`; proxy removal; training-only scaling; optional loader `(64,8)/(64,)` | Solution `b6ed5ca29064fa05b6bc93085d2016090504410c260b178aeec35760953d2246` (**exact report match**)<br>Participant `6a0c1905d3d0fc7fdcacd417ae303997ac5d63cccdae77ea140130f0fed43340` (**exact**)<br>Leakage: **NONE** | Hosted Colab unexecuted |
| `LAB-D3-02` | [Solution](../instructor-solutions/day-3/LAB-D3-02-cnn-feature-maps-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D3-02.md) | **PASS WITH NOTES**<br>5.198 s | 19/19; packaged real Fashion-MNIST fallback; `105,866` parameters; validation `0.685 -> 0.762`; optional epoch `0.764`; hooks removed | Solution `7b2ace4c8bc2b11eed56aa1d93d921e327f1083cbc763312715dac699ee14310` (**exact report match**)<br>Participant `0041ce12334e94190c4202f6513a608c7ace0190f4cee934fbb504660f35ae8f` (**exact**)<br>Leakage: **NONE** | Online/full-data band, throughput, and hosted Colab unexecuted |
| `LAB-D3-03` | [Solution](../instructor-solutions/day-3/LAB-D3-03-overfit-and-rescue-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D3-03.md) | **PASS WITH NOTES**<br>3.924 s | 15/15; independent fallback load; baseline `0.998/0.796`, gap `0.201`; dropout `0.985/0.799`, gap `0.186`; confound caught; remedy correctly rejected | Solution `523719da936ea925cef8670e067da97b0cc6703d209fdb5d41be08f3cf88724c` (**exact report match**)<br>Participant `1027482a1674bee5875e6c6e52febed5fd6e8770aad8ec36e73306bd51084e49` (**exact**)<br>Leakage: **NONE** | Negative result is expected evidence, not a test failure; online-source and hosted Colab unexecuted |
| `LAB-D3-04` | [Solution](../instructor-solutions/day-3/LAB-D3-04-transfer-learning-race-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D3-04.md) | **PASS WITH NOTES**<br>3.830 s | 16/16; no-download recovery; scratch `0.7575`; fresh head `0.77125`; frozen/wrong-normalization diagnoses; zero network/CIFAR calls | Solution `12da6f1c7cd26ad737e2370377c181f272a9e473b31d39ab92705f860b1352a1` (**exact report match**)<br>Participant `a7a28eecb783c96c1df2eb8bd4045e2143e63f040fe17c7860424baae0bcf9d0` (**exact**)<br>Leakage: **NONE** | Recovery is not CIFAR-10 or MobileNet evidence; canonical online metrics/cache/timing/winner and hosted Colab unexecuted |

## Day 4 Pairing

| Lab | Canonical solution and report | Status / clean runtime | Key evidence and branches | Current hashes / separation | Notes |
|---|---|---|---|---|---|
| `LAB-D4-01` | [Solution](../instructor-solutions/day-4/LAB-D4-01-accuracy-is-not-enough-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D4-01.md) | **PASS WITH NOTES**<br>2.875 s | 16/16; majority accuracy `0.9539` with recall/F1 `0/0`; default recall `0.6627`; cost thresholds `0.19/0.43`; optional `0.26` | Solution `a207f709911e1d422f364c4321e407c196aa099b7f0d03c51082c5cae206d3b0` (**exact report match**)<br>Participant `08a02a0ed4ec7866dd208192193903e8455839cba8910003c086ce04c16deff1` (**exact**)<br>Leakage: **NONE** | Hosted Colab unexecuted |
| `LAB-D4-02` | [Solution](../instructor-solutions/day-4/LAB-D4-02-model-detective-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D4-02.md) | **PASS WITH NOTES**<br>2.621 s | 17/17; four curve bundles; accuracy `0.9526`; 17 errors; overlapping slices; exclusive buckets total `17/17`; optional low-confidence view | Solution `0e2db8a7325339fdc0cf40cf67193c2cb30ffe5607bfe3f9822b5f2bd5533e40` (**exact report match**)<br>Participant `259d689bd44501d761f2190e4e04f9bc0caa974179536cd67cb2c95dd24d74ff` (**exact**)<br>Leakage: **NONE** | Hosted Colab unexecuted |
| `LAB-D4-03` | [Solution](../instructor-solutions/day-4/LAB-D4-03-one-experiment-SOLUTION.ipynb)<br>[Report](../reviews/solution-validation-LAB-D4-03.md) | **PASS WITH NOTES**<br>4.236 s canonical | 16/16 canonical; controlled negative result `0.8496`; same-seed delta `0`; all nine menu branches serialized; confounded draft and 21-epoch proposal rejected before compute | Solution `e7f6b54d4176d0d46f888e3a8029d4851a56eda8e2a0357b2505bd47163e7c0d` (**exact report match**)<br>Participant `bd32475e6cdd08db0b1c552c218472536b50596c20b191d2ece6b9420b0d207e` (**exact**)<br>Leakage: **NONE** | Hosted Colab unexecuted; branch timings are host-specific evidence, not a leaderboard |
| `LAB-D4-04` | [Canonical capstone solution](../capstone/capstone-solution.ipynb)<br>[Report](../reviews/solution-validation-LAB-D4-04.md) | **PASS WITH NOTES**<br>Live A/B/C: 4.681/4.045/3.596 s<br>Recovery A/B/C: 3.098/3.085/2.982 s | Six fresh paths; 19/19 each; profiles A/B/C live plus cached recovery; one major change; ledger/board/defense; decision freeze; one authorized test access; optional validation-only | Solution `30ce02c6208996d829086da78726dcf41c9cf5486c28cdbfab44d17fb2589e27` (**exact report match**)<br>Participant `a191355d19d2dc64810cde7591fcee9dd1865116f70a04a7dbf2ba8b9c5462a4` (**exact**)<br>Leakage: **NONE** | Hosted Colab unexecuted; external release tooling must enforce exclusions |

## Clean-Kernel and Coverage Rollup

- Every canonical solution report records cleared outputs, a new CPU kernel, ordered Run All execution, zero uncaught errors, and a passed final checkpoint. Stored reference outputs were checked as current in the day reports.
- Reported code-cell coverage is complete for all 16 labs. Day 4 D4-04 additionally completed `19/19` code cells independently in each of six profile/source paths.
- Every report states that participant TODOs, prediction questions, implementation tasks, diagnosis prompts, interpretation questions, challenges, reflections, and checkpoints have completed instructor answers.
- Deliberate failures were executed and recovered rather than described only in prose. Examples include wrong-axis softmax, transpose mismatch, BCE endpoints, gradient defects, NaN/high-rate paths, channel/shape errors, confounded interventions, transfer-contract violations, cost-insensitive selection, and capstone test-access denial.
- Practical optional work was executed where the report defines it as runnable. Planning-only branches are explicitly labeled: D3-03 augmentation and D3-04 partial fine-tuning are not presented as executed evidence.

## Day 3 Source-Mode Boundaries

| Lab | Executed source mode | Structurally checked | Not validated |
|---|---|---|---|
| D3-01 | Generated local records | N/A | Hosted Colab |
| D3-02 | Packaged real Fashion-MNIST fallback | Cache-aware, opt-in Fashion-MNIST path | Online/full-data `0.80-0.88` band, throughput, hosted Colab |
| D3-03 | Independently loaded packaged Fashion-MNIST fallback | Cache-aware, opt-in Fashion-MNIST path | Online-source metrics/runtime, hosted Colab |
| D3-04 | Packaged recovery images and label-blind surrogate embeddings; scratch and fresh head | Weight enum, `weights.transforms()`, frozen MobileNet, CIFAR split, extraction, provenance-aware cache key | Weight/CIFAR download, MobileNet extraction, canonical cache behavior, online metrics/timings/degradation/winner, hosted Colab |

Fallback metrics are not evidence for online/full-data bands. D3-04 recovery is explicitly not CIFAR-10, not MobileNet output, not a canonical cache hit, and not evidence that transfer learning wins.

## Capstone Lock and Recovery

- **Profiles:** A, B, and C each passed both live and cached-recovery execution from the final solution hash.
- **Live changes:** A enabled class weighting; B set dropout to `0.5`; C changed learning rate to `0.003` and used upward validation-loss variation after the solution-only stability-gate fix.
- **Recovery:** all three artifacts passed SHA-256 and exact committed-config fingerprint checks. Recovery exposed validation evidence only, with no diagnosis, intervention, trained checkpoint, test authorization, test arrays, or test metric.
- **Decision/test lock:** every live path denied early test access, required evidence and ranked hypotheses, changed exactly one major field, serialized the ledger/evidence board, froze the decision, accessed test once, and recorded `used_for_further_tuning=False`.
- **Optional lock:** optional runs remained validation-only and recorded `test_reused=False`.
- **Team/individual lock:** the 10-field team defense excludes `individual_transfer`; team rubric arithmetic is `25 + 20 + 20 + 15 + 10 + 10 = 100`; `CHECK-D4-04` remains separate.
- **Uniqueness:** no D4-04 solution notebook exists under `courseware/instructor-solutions/day-4/`; `capstone-case-key.md` is a guide/key, not a duplicate solution notebook.

## Separation and Leakage

- Existing detailed/day reports record participant-tree leakage result **NONE** for all four days.
- Current participant lab and capstone source was scanned for instructor-solution/instructor-guide paths, answer-key/model-answer terms, and solution-notebook references; no leak was found.
- Participant notebooks remain paired by exact hash for 13 labs. D2-01, D2-02, and D2-03 changed after their reports; the current scan is clean, but their completed participant execution and exact answer-separation attestations require retest.
- `courseware/participant-release-exclusions.txt` excludes instructor solution/guide trees, the capstone solution and instructor guide, the Day 4 generator, solution builders/validators, and reviews.
- The repository has no release builder that automatically enforces the exclusion list. External participant packaging must consume or mirror it.

## FAIL and RETEST Disclosure

- **Current solution statuses:** no FAIL and no RETEST among the 16 detailed solution reports.
- **Current rollup RETEST:** D2-01, D2-02, and D2-03 participant hash/parity checks because current participant hashes differ from both their participant and solution validation reports.
- The D1-01, D1-02, and D1-04 participant validation Markdown files retain older FAIL sections after newer `Participant Validation Retest` PASS WITH NOTES sections. Those historical failures are superseded by each file's leading retest status and the current solution reports. D1-03 has no retained FAIL status section, but its prior-history note acknowledges an earlier empty-notebook failure.
- All 16 participant reports include conditional `Retest Requirements` for future source/environment changes. Those headings are not current RETEST statuses; the only current rollup retest items are the D2-01, D2-02, and D2-03 participant hash/parity mismatches above.
- Expected negative results, caught deliberate failures, rejected hypotheses, and unexecuted online/hosted branches are not hidden as PASS evidence; they are called out in the per-lab rows and source-mode table.

## Unresolved Notes

1. **Hosted environment:** no report claims an actual hosted Google Colab CPU run. This remains open for all 16 labs.
2. **Day 2 participant drift:** D2-01, D2-02, and D2-03 require participant validation and solution-pair separation retests against their current hashes.
3. **PyTorch version:** D2-04 was source-checked against PyTorch 2.11 documentation but executed on local PyTorch 2.6.0; exact 2.11 runtime behavior is unvalidated.
4. **Day 3 online paths:** D3-02/D3-03 online/full-data paths and D3-04 canonical CIFAR/MobileNet path remain unexecuted.
5. **Accelerators:** CPU is the required validated path. GPU timing, memory, and small numerical differences are not calibrated unless a detailed report explicitly says otherwise.
6. **Release enforcement:** external participant-release tooling must honor `courseware/participant-release-exclusions.txt`.

## Final Declaration

**Instructor solution execution gate: PASS WITH NOTES.** All 16 canonical solutions have PASS-family detailed reports, current canonical paths, and current solution hashes; all report-verifiable solution hashes match. Exact one-to-one solution inventory and D4-04 uniqueness pass. The paired courseware gate remains **RETEST REQUIRED for D2-01, D2-02, and D2-03 participant hash/parity only**; no solution execution failure is being reclassified or hidden.
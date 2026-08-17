# PASS WITH NOTES

## Day 2 Instructor Solution Validation Summary

### Status Matrix

| Lab | Status | Clean-run wall time | Executed code cells | Key clean-run evidence |
|---|---|---:|---:|---|
| `LAB-D2-01` | **PASS WITH NOTES** | **1.754 s** | 16/16 | BCE A/B `0.164/0.554`; all four learning-rate regimes; challenge/curvature paths |
| `LAB-D2-02` | **PASS WITH NOTES** | **1.691 s** | 18/18 | Max relative error `1.012e-09`; distinct sign/missing-factor defects; loss-lowering update |
| `LAB-D2-03` | **PASS WITH NOTES** | **4.488 s** | 23/23 | Initial BCE `0.6860`; final train/validation accuracy `0.915/0.905`; both failures and two isolated experiments |
| `LAB-D2-04` | **PASS WITH NOTES** | **7.795 s** | 21/21 | Baseline `0.900`; default-`None` and optimizer-state probes; all A-D signatures; repaired `0.895`; mode/shape checks |

All four solutions count as complete. Total observed clean-run wall time, including a fresh kernel startup per notebook, was **15.728 s** on the local CPU environment.

### Canonical Outputs

| Lab | Solution path | Solution SHA-256 |
|---|---|---|
| `LAB-D2-01` | `courseware/instructor-solutions/day-2/LAB-D2-01-loss-learning-rate-SOLUTION.ipynb` | `3e4a9f2f1902625e6f416ca1014ca4ed2375563af21cf788fa8d82a4555de630` |
| `LAB-D2-02` | `courseware/instructor-solutions/day-2/LAB-D2-02-backprop-gradient-check-SOLUTION.ipynb` | `6bd54fd53c800f2a1dcd0c6ddecad0c60f0cb32be6e6ad3c852eaf1eb56fc114` |
| `LAB-D2-03` | `courseware/instructor-solutions/day-2/LAB-D2-03-numpy-training-SOLUTION.ipynb` | `510cca4fcb44b2e12f447ca1f4eeb64a2716101314cd8455dc9ec4462cd33135` |
| `LAB-D2-04` | `courseware/instructor-solutions/day-2/LAB-D2-04-pytorch-break-fix-SOLUTION.ipynb` | `2c6510bdc00acb8ca415f8c0d7e520dd4abfed3c31e81165b5e9d1cf9ff4de51` |

### Execution and Metadata Coverage

- Every canonical solution was cleared, restarted in a fresh kernel, and run from top to bottom.
- Execution counts are sequential for every code cell; uncaught error outputs: **0**.
- Stored PNG outputs: D2-01 **1**, D2-02 **2**, D2-03 **4**, D2-04 **2**.
- Cell totals are **40**, **42**, **52**, and **51**. Every cell has a unique official `id`, matching unique `metadata.id`, and correct `metadata.language`.
- Required tasks, deliberate failures, repairs, challenges, practical optional extensions, reflections, and checkpoints executed.
- D2-04 was source-checked against the official PyTorch 2.11 `Optimizer.zero_grad` page and executed locally with PyTorch 2.6.0 CPU; plain-reset `None`, unused-parameter, explicit-zero-buffer, and optimizer `None`-versus-zero behaviors all passed. No exact-2.11 runtime claim is made.

### Key Ranges and Behaviors

- **D2-01:** clipped endpoint BCE `27.6310`; `eta=0.01/0.10/0.90/1.10` reproduce crawl/smooth/oscillatory/divergent behavior; `0.60` challenge contracts distance by `0.20` per step.
- **D2-02:** analytic/numeric errors remain far below `1e-5`; sign defect affects all layers; missing hidden factor affects only hidden-layer parameter gradients; one update lowers loss `0.6739 -> 0.6431`.
- **D2-03:** baseline train/validation loss `0.1857/0.1820`, accuracy `0.915/0.905`; identity path `0.850`; high-rate validation loss reaches `8.216`; isolated variants stay finite and interpretable.
- **D2-04:** baseline validation accuracy `0.900`; repaired all-card reference `0.895`; card B norm grows `1.146 -> 6.828` versus repaired max `0.286`; plain reset yields `None`, explicit `False` yields an existing zero buffer, and optimizer `None`-versus-zero behavior is directly evidenced.

### Separation and Frozen Inputs

| Participant lab | Confirmed SHA-256 |
|---|---|
| `LAB-D2-01-loss-learning-rate.ipynb` | `8779f5d76a66e8aa209be3668a1dbad23745be5a0e0016075a8f15a18f6488c3` |
| `LAB-D2-02-backprop-gradient-check.ipynb` | `45708d638d16a5529bd8e460758d2d1c9c8d512061a0d917e9c293f72aeca2ca` |
| `LAB-D2-03-numpy-training.ipynb` | `18a5b0a63ae261fae428936899d5e66513fe9ebef8cdde182aae011237a3010a` |
| `LAB-D2-04-pytorch-break-fix.ipynb` | `b3dfb495468ac7ec05c41df9ee4bbe49b11620f1c28504425ab02cbd852e0d52` |

All hashes exactly match the current participant PASS WITH NOTES reports. A hard scan of the full Day 2 participant tree found no solution labels, answer keys/model answers, instructor-only paths, or instructor hint ladders. Two uses of “the instructor reveals” in the participant challenge file are facilitation instructions, not answers or links.

**Leakage result: NONE.** No participant notebook or Day 2 participant artifact was edited.

### Issues and Fixes

- No participant contradiction was found; no lab required failure routing to the Course Orchestrator.
- D2-03 solution QA rejected an optional width-4 narrative because the actual run improved. The optional path was recalibrated to width 16, reconciled with evidence, cleared, and rerun successfully.
- A temporary generator indentation defect was fixed before the final D2-03 clean run. Canonical outputs contain no syntax or execution error.
- D2-04 solution QA replaced stale zero-filled-default claims, added isolated `None`/zero optimizer probes, corrected five instructor-solution navigation links, and reran the complete canonical notebook with zero uncaught errors.

### Remaining Notes

1. A hosted Google Colab CPU runtime was not executed. None of these reports claims hosted Colab validation.
2. An exact PyTorch 2.11 runtime was not executed. D2-04 uses source-checked compatible APIs but is validated locally on PyTorch 2.6.0.

### Final Status

**PASS WITH NOTES** - all four Day 2 instructor solutions are complete, clean-executable, instructor-ready, correctly separated, and locally validated; hosted Colab and exact PyTorch 2.11 remain open environment checks.
# PASS WITH NOTES - DAY 4 INSTRUCTOR SOLUTIONS

## Status Matrix

| Lab | Status | Canonical clean run | Plots | Principal evidence |
|---|---|---:|---:|---|
| `LAB-D4-01` | **PASS WITH NOTES** | 2.875 s | 2 | majority `0.9539/0/0`; default recall `0.6627`; cost thresholds `0.19/0.43`; optional `0.26` |
| `LAB-D4-02` | **PASS WITH NOTES** | 2.621 s | 5 | four bundles answered; accuracy `0.9526`; 17 errors; buckets `17/17` |
| `LAB-D4-03` | **PASS WITH NOTES** | 4.236 s | 2 | controlled negative result `0.8496`; all 9 menu branches and budget rejection passed |
| `LAB-D4-04` | **PASS WITH NOTES** | 4.681 s default A | 3 | final-hash A/B/C live and recovery passed; corrected C stability gate, test lock, rubric, optional, ledger, board, defense passed |

All canonical solutions were cleared and executed from fresh kernels. All code cells completed, all stored plots decoded with nonblank pixels, all official cell IDs equaled `metadata.id`, every ID was unique, and every cell had `metadata.language`.

## Environment

- macOS Apple silicon, local CPU
- Python 3.11.8
- NumPy 2.4.6; matplotlib 3.11.1; scikit-learn 1.9.0
- PyTorch 2.6.0 for D4-03/D4-04; one thread
- nbformat 5.11.0; nbclient 0.11.0
- Fixed seeds/splits; fresh model/optimizer/loader state; no network or GPU

Current PyTorch/scikit-learn APIs and reproducibility behavior were checked against current primary Context7 documentation. Seeds aid repeatability but do not guarantee cross-platform/release/device identity. Latency is a host-specific comparison under the declared warmup/repeat method.

## Participant and Solution Hashes

| Artifact | SHA-256 |
|---|---|
| participant D4-01 | `08a02a0ed4ec7866dd208192193903e8455839cba8910003c086ce04c16deff1` |
| participant D4-02 | `259d689bd44501d761f2190e4e04f9bc0caa974179536cd67cb2c95dd24d74ff` |
| participant D4-03 | `bd32475e6cdd08db0b1c552c218472536b50596c20b191d2ece6b9420b0d207e` |
| participant capstone starter | `a191355d19d2dc64810cde7591fcee9dd1865116f70a04a7dbf2ba8b9c5462a4` |
| solution D4-01 | `a207f709911e1d422f364c4321e407c196aa099b7f0d03c51082c5cae206d3b0` |
| solution D4-02 | `0e2db8a7325339fdc0cf40cf67193c2cb30ffe5607bfe3f9822b5f2bd5533e40` |
| solution D4-03 | `e7f6b54d4176d0d46f888e3a8029d4851a56eda8e2a0357b2505bd47163e7c0d` |
| canonical capstone solution | `30ce02c6208996d829086da78726dcf41c9cf5486c28cdbfab44d17fb2589e27` |

Participant hashes exactly match the existing participant reports; no participant notebook or support artifact was edited.

The D4-04 gate started from the required solution hash `75dafa25997626685264b5e727c87a3491512e011cd1fc3704450cc721724e6c`. Fresh profile C execution exposed a solution-only target bug: raw total variation penalized useful loss descent. The final solution uses upward validation-loss variation for stability, and all six paths were rerun from the final canonical hash above.

## D4-03 Menu Execution

All nine bounded options ran in fresh kernels and serialized complete records. Accuracy ranged from `0.4652` for fixed-budget SGD to `0.9415` for learning rate `0.01`; this spread is validation evidence for menu executability, not permission to select post hoc. Width changed bytes as expected (`4,840` for 16, `19,240` for 64); all other tested configurations used `9,640` bytes. Same-seed repeat accuracy deltas were `0.0`. The confounded three-change draft and 21-epoch budget violation were both rejected before compute.

## Capstone Profile Matrix

| Profile | Primary / secondary | Change | Validation result | Test result | Live / recovery wall s |
|---|---|---|---|---|---:|
| A | class support / representation-label ambiguity | class weight | acc `0.9109`, F1 `0.9097`, worst recall `+0.5429` | `0.9222/0.9223` | 4.681 / 3.098 |
| B | capacity variance / split shift | dropout `0.5` | acc `0.9109`, F1 `0.9100`, gap `-0.0306` | `0.8944/0.8946` | 4.045 / 3.085 |
| C | aggressive optimization / capacity | LR `0.003` | acc `0.8969`, F1 `0.8964`, acc `+0.1142`; upward loss variation `0.2738 -> 0.0000` | `0.8944/0.8951` | 3.596 / 2.982 |

Recovery matched opaque config fingerprints, supported full validation defense, and exposed no test metrics. Live test evidence appeared once only after the decision record and was never used for further tuning.

## Support Hashes

| Artifact | SHA-256 |
|---|---|
| `manifest.json` | `a64a23e7ada2c14a143fd8ae2cbbe7d285456b3ce4dbfbe99841b28131b0eac3` |
| `generate_day4_artifacts.py` | `fd100bef4e3528bf4620411e6cbcd73c53302f529a9995fdada3671eebcac729` |
| `digits_fixed_splits.npz` | `d137096786526f03f48e17744c6a25e59ac2059e8d7f8d5929121ccc2a8ffd36` |
| `mystery_curves.npz` | `e90fc9590ff11e748b1caa5732de8c7d5ab78a7e18282a5f3d7978d1a62c643b` |
| `digits_evidence.npz` | `1118cf4e6c57f23acabd8b5af20d7c8aae1352b0296078c28fa9e5ff48b02cf6` |
| `experiment_baseline.npz` | `158d5786b20af18623477ce5ae31315d96770e48cb0671c4c45313d967efe34f` |
| `profile_A_baseline.npz` | `08b31bb061def36876ca5fd6d8e2a41ef2da2eb974db8fdcef68c886642de07b` |
| `profile_B_baseline.npz` | `edf856314abb5287f93848d8172dcb499d2c2a4c2a25a67421b84a1ee51bf2ba` |
| `profile_C_baseline.npz` | `e4d3430e074b0ab9581a82362377ac8f32446ebcf8b90a7531c21fbb0a2de3cc` |
| `profile_A_recovery.npz` | `eb6469424d2ac622d6ccb4f03a81225a69ade68c643e779d9be71bb902119f90` |
| `profile_B_recovery.npz` | `ffef55704b2992a23d9886f21fafade55982c5dbfbcf61fb66495b69a19d6780` |
| `profile_C_recovery.npz` | `bcd176dbb17fce2d75fc12135ec6423061d2e5ba2045a1363565d986dd2ed4cf` |

All manifest bytes/checksums passed. Two isolated, blocked-network generator runs reproduced the manifest and every NPZ byte-for-byte. NPZs had no object arrays and no diagnosis, intervention, solution, checkpoint, or test-metric strings.

## Separation and Rubric

- Participant-tree scan found no instructor/solution/case-key link, completed answer, or profile diagnosis. Generic vocabulary such as high variance appears only as legitimate participant learning content.
- Profile letters, filenames, colors, metadata, and support strings do not map A/B/C to causes.
- `participant-release-exclusions.txt` excludes `courseware/instructor-solutions/**`, `courseware/instructor-guide/**`, the capstone solution, and the capstone instructor guide.
- The repository has no archive builder that consumes this list; external release packaging must enforce it.
- Team rubric arithmetic is exactly `25/20/20/15/10/10 = 100`.
- Individual `CHECK-D4-04` remains separate from the team score.

## Files Created

- `courseware/instructor-solutions/day-4/LAB-D4-01-accuracy-is-not-enough-SOLUTION.ipynb`
- `courseware/instructor-solutions/day-4/LAB-D4-02-model-detective-SOLUTION.ipynb`
- `courseware/instructor-solutions/day-4/LAB-D4-03-one-experiment-SOLUTION.ipynb`
- `courseware/capstone/capstone-solution.ipynb`
- `courseware/instructor-solutions/day-4/capstone-case-key.md`
- `courseware/participant-release-exclusions.txt`
- `courseware/reviews/solution-validation-LAB-D4-01.md`
- `courseware/reviews/solution-validation-LAB-D4-02.md`
- `courseware/reviews/solution-validation-LAB-D4-03.md`
- `courseware/reviews/solution-validation-LAB-D4-04.md`
- `courseware/reviews/day-4-solution-summary.md`

## Unresolved Notes

- Hosted Google Colab CPU was unavailable. Do not claim hosted validation until all four canonical paths, A/B/C live, and at least one recovery path run there with the shared Day 4 directory uploaded.
- The canonical manifest and local validation environment both record NumPy 2.4.6.
- External participant-release tooling must consume or mirror `participant-release-exclusions.txt`.

## Final Status

**PASS WITH NOTES** - all four canonical instructor solutions are complete, independently executable, correctly separated, under runtime ceilings, and instructor-ready on the validated local CPU stack. Notes are environmental/release-process qualifications, not solution failures.

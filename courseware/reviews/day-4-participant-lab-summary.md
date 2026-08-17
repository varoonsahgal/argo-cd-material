# PASS WITH NOTES - ALL LOCAL CPU PATHS AND SUPPORT CONTRACT PASS

## Day 4 Participant Lab Validation Summary

### Status Matrix

| Lab | Status | Interestingness | Completed clean run | Key evidence |
|---|---|---|---:|---|
| `LAB-D4-01` | **PASS WITH NOTES** | **STRONG** | **2.864 s** | Majority `0.9539` accuracy with recall/F1 `0`; useful recall `0.6627`; cost thresholds `0.19/0.43`; optional `0.26` |
| `LAB-D4-02` | **PASS WITH NOTES** | **STRONG** | **2.805 s** | Digits accuracy `0.9526`; `(10,10)` confusion; 17 aligned errors; exclusive buckets `17/17`; 5 plots |
| `LAB-D4-03` | **PASS WITH NOTES** | **STRONG** | **4.527 s** | Baseline `0.8969`; confounded draft rejected; two fresh runs identical; negative intervention `0.8496`; complete `9,640`-byte record |
| `LAB-D4-04` | **PASS WITH NOTES** | **STRONG** | **3.972-4.948 s/profile** | Revised anonymity passed; A/B/C live + recovery targets and test lock passed; team defense excludes individual transfer and links to separate `CHECK-D4-04` |

Every local CPU participant path executed end to end from a fresh kernel. No participant-blocking notebook or support-artifact defect was found. Notes remain because hosted Colab was unavailable.

### Environment

- macOS on Apple silicon, local CPU
- Python 3.11.8
- NumPy 2.4.6, matplotlib 3.11.1, scikit-learn 1.9.0
- PyTorch 2.6.0 for D4-03/D4-04
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- Fresh temporary venv and a new kernel for every canonical starter/completed/recovery run
- No GPU or network required for any executed participant path

The bare system Python lacked `nbformat`; the documented isolated setup installed successfully from cached wheels. Hosted Colab was unavailable.

### Canonical Notebook Hashes

| Participant notebook | SHA-256 |
|---|---|
| `LAB-D4-01-accuracy-is-not-enough.ipynb` | `08a02a0ed4ec7866dd208192193903e8455839cba8910003c086ce04c16deff1` |
| `LAB-D4-02-model-detective.ipynb` | `259d689bd44501d761f2190e4e04f9bc0caa974179536cd67cb2c95dd24d74ff` |
| `LAB-D4-03-one-experiment.ipynb` | `bd32475e6cdd08db0b1c552c218472536b50596c20b191d2ece6b9420b0d207e` |
| `capstone-starter.ipynb` | `a191355d19d2dc64810cde7591fcee9dd1865116f70a04a7dbf2ba8b9c5462a4` |

### Execution Coverage

For every lab independently:

1. Validated raw JSON, official nbformat, and all Python syntax.
2. Confirmed notebook `lab_id`, unique official cell IDs, exact official ID = `metadata.id`, unique metadata IDs, and `metadata.language` on every cell.
3. Confirmed canonical code cells contain no outputs or execution counts.
4. Confirmed learner predictions, diagnoses, interpretations, challenge fields, reflections, and implementation TODOs remain blank/visible in the starter.
5. Confirmed no participant artifact references instructor solutions/guides, answer keys, case keys, or solution notebooks.
6. Ran each untouched starter in a fresh kernel and confirmed the first stop was an intentional participant gate.
7. Built temporary participant-completed copies without reading solution artifacts.
8. Completed every core response/TODO and practical optional path, restarted, and ran all cells in order.
9. Executed all deliberate failure/recovery paths, including D4-03's negative-result acceptance and D4-04's A/B/C cached recovery branches.
10. Inspected 18 live-run PNG outputs; every image was decodable, nonblank, and stably sized.
11. Resolved all 31 relative participant links/anchors. All lab launches, challenge links, debriefs, capstone guide/rubric links, and continuation links passed.

Temporary completed/executed notebooks remained under `$TMPDIR`. Canonical notebooks and support artifacts were not edited.

### Timings and Metrics

| Lab/profile | Starter stop | Completed wall time | Principal evidence |
|---|---:|---:|---|
| D4-01 | Cell 6, `18.718 s` cold start | **2.864 s** | majority `0.9539/0/0`; default recall `0.6627`; thresholds `0.19/0.43` |
| D4-02 | Cell 8, `2.359 s` | **2.805 s** | accuracy `0.9526`; 17 errors; bucket total 17 |
| D4-03 | Cell 8, `6.417 s` | **4.527 s** | baseline `0.8969`; experiment `0.8496`; repeat delta `0`; median `0.01065 ms` |
| D4-04 A live | Cell 13 in canonical starter, `3.733 s` | **4.948 s** | accuracy `+0.0808`; worst recall `+0.5429`; test `0.9222` |
| D4-04 B live | same canonical gate | **4.926 s** | gap reduction `0.0306`; validation `+0.0306`; test `0.8944` |
| D4-04 C live | same canonical gate | **3.972 s** | validation `+0.1142`; gap `0.0791 -> 0.0363`; test `0.8944` |
| D4-04 A/B/C recovery | independent fresh kernels | **3.182-3.393 s** | same validation evidence; no checkpoint/cause/intervention/test metric |

All local runtimes are far below the required 30-second, 8-minute, and 12-minute limits.

### Support and Separation Audit

All manifest byte sizes, SHA-256 hashes, exact key schemas, and non-object dtypes match all 10 packaged NPZs.

| Artifact | Bytes | SHA-256 | Key audit |
|---|---:|---|---|
| `digits_fixed_splits.npz` | 5,205 | `d137096786526f03f48e17744c6a25e59ac2059e8d7f8d5929121ccc2a8ffd36` | Disjoint `1078/359/360`, fixed hash |
| `mystery_curves.npz` | 4,295 | `e90fc9590ff11e748b1caa5732de8c7d5ab78a7e18282a5f3d7978d1a62c643b` | Only `M1-M4` and aligned curves |
| `digits_evidence.npz` | 34,375 | `1118cf4e6c57f23acabd8b5af20d7c8aae1352b0296078c28fa9e5ff48b02cf6` | Images/labels/probabilities/predictions/metadata aligned |
| `experiment_baseline.npz` | 18,626 | `158d5786b20af18623477ce5ae31315d96770e48cb0671c4c45313d967efe34f` | Validation curves/metrics/resources only |
| `profile_A_baseline.npz` | 21,763 | `08b31bb061def36876ca5fd6d8e2a41ef2da2eb974db8fdcef68c886642de07b` | Selected-case target/config/indices plus anonymous validation evidence |
| `profile_B_baseline.npz` | 21,058 | `edf856314abb5287f93848d8172dcb499d2c2a4c2a25a67421b84a1ee51bf2ba` | Selected-case target/config/indices plus anonymous validation evidence |
| `profile_C_baseline.npz` | 22,041 | `e4d3430e074b0ab9581a82362377ac8f32446ebcf8b90a7531c21fbb0a2de3cc` | Selected-case target/config/indices plus anonymous validation evidence |
| `profile_A_recovery.npz` | 18,808 | `eb6469424d2ac622d6ccb4f03a81225a69ade68c643e779d9be71bb902119f90` | Fingerprinted validation-only recovery |
| `profile_B_recovery.npz` | 19,880 | `ffef55704b2992a23d9886f21fafade55982c5dbfbcf61fb66495b69a19d6780` | Fingerprinted validation-only recovery |
| `profile_C_recovery.npz` | 18,745 | `bcd176dbb17fce2d75fc12135ec6423061d2e5ba2045a1363565d986dd2ed4cf` | Fingerprinted validation-only recovery |

Additional support results:

- Two isolated generator runs with sandbox network blocking were bitwise identical to each other and to the canonical manifest and all ten NPZs.
- Every regenerated file matched its canonical SHA-256 exactly under NumPy 2.4.6, scikit-learn 1.9.0, and PyTorch 2.6.0.
- Manifest SHA-256: `a64a23e7ada2c14a143fd8ae2cbbe7d285456b3ce4dbfbe99841b28131b0eac3`.
- Generator SHA-256: `fd100bef4e3528bf4620411e6cbcd73c53302f529a9995fdada3671eebcac729`.
- The generator imports no network/subprocess library, contains no URL/download path, fixes CPU use, seeds Python/NumPy/PyTorch, sorts NPZ entries, and fixes ZIP timestamps.
- Fixed splits are disjoint and cover all 1,797 examples; the hash is `c9a534c56d9b1bb069bc2295d7adf87517e34b69ea9a5b046b79a3b29470b3d9`.
- Digits evidence exactly equals `load_digits()` at `sample_ids`; predictions/confidence recompute from probabilities; probability rows sum to one.
- NPZ keys/string values contain no diagnosis, intervention, solution, answer, checkpoint, test metric, or configuration labels.
- Pre-Diagnosis-Gate source/metadata contains no cross-profile config/target/sampling map, profile-conditioned construction rule, cause/intervention mapping, or diagnosis-revealing color/comment. The selected case exposes only its allowed target/config/train indices and anonymous evidence.
- Recovery selection requires the exact committed config fingerprint and supplies no cause label, intervention name, trained checkpoint, or test metric.
- Participant capstone artifacts link only among the starter, Student Guide, and rubric. They never link to a solution, instructor guide, or case key.
- Rubric weights are exactly `25/20/20/15/10/10`; the 10-field team defense excludes `individual_transfer` and directs each learner to separate `CHECK-D4-04` after defense.
- The simulated participant release contains only one `LAB-D4-04` notebook: `capstone-starter.ipynb`. The repository-only solution is excluded as declared.

### Required Fixes

None for the tested participant notebooks, local support artifacts, or generator contract.

### Blockers and Notes

- **No local blocker:** all four participant labs and every required profile/recovery path passed.
- **Not executed:** hosted Google Colab. Do not label Day 4 Colab-validated until a real hosted CPU run is completed with the support directory present.
- **Version note:** the canonical manifest and this validation both record NumPy 2.4.6; two isolated regenerations matched the complete canonical support set byte-for-byte.

### Files Created

- `courseware/reviews/participant-validation-LAB-D4-01.md`
- `courseware/reviews/participant-validation-LAB-D4-02.md`
- `courseware/reviews/participant-validation-LAB-D4-03.md`
- `courseware/reviews/participant-validation-LAB-D4-04.md`
- `courseware/reviews/day-4-participant-lab-summary.md`

### Retest Requirements

- Execute all four completed paths and all three capstone profiles in a fresh hosted Colab CPU runtime before making a hosted-readiness claim.
- Re-run size/hash/schema/string-leakage/determinism checks after any generator, manifest, or NPZ change.
- Re-run affected starter, completed copy, optional/failure/recovery path, plot inspection, link audit, IDs, metadata, and profile calibration after any participant-notebook or support change.
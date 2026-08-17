# PASS WITH NOTES

## Solution Validation: LAB-D4-04

### Artifacts and Hashes

| Artifact | Bytes | SHA-256 | Gate result |
|---|---:|---|---|
| `courseware/capstone/capstone-starter.ipynb` | 33,021 | `a191355d19d2dc64810cde7591fcee9dd1865116f70a04a7dbf2ba8b9c5462a4` | Matches the current Student PASS report |
| Solution observed at gate start | 214,906 | `75dafa25997626685264b5e727c87a3491512e011cd1fc3704450cc721724e6c` | Required input hash validated; profile C exposed a stale stability gate |
| `courseware/capstone/capstone-solution.ipynb` after fix | 215,533 | `30ce02c6208996d829086da78726dcf41c9cf5486c28cdbfab44d17fb2589e27` | Final canonical solution; all six paths rerun from this hash |
| `courseware/shared/data/day-4/manifest.json` | 4,496 | `a64a23e7ada2c14a143fd8ae2cbbe7d285456b3ce4dbfbe99841b28131b0eac3` | Required hash matched |
| `courseware/shared/data/day-4/generate_day4_artifacts.py` | 26,396 | `fd100bef4e3528bf4620411e6cbcd73c53302f529a9995fdada3671eebcac729` | Required hash matched |

The final solution hash differs from the supplied hash because validation found and fixed one solution-only defect. Raw validation-loss total variation penalized a successful larger loss descent, causing profile C to fail its own final checkpoint. The solution now retains total variation as descriptive evidence and uses upward validation-loss variation to measure reversals: `0.2738 -> 0.0000` for profile C.

### Environment and Method

- Validation date: 2026-08-17
- macOS Apple silicon; required CPU path; one PyTorch thread
- Python 3.11.8; NumPy 2.4.6; matplotlib 3.11.1; scikit-learn 1.9.0; PyTorch 2.6.0
- nbformat 5.11.0; nbclient 0.11.0; ipykernel 7.3.0; Pillow 12.3.0
- For each path, loaded the final canonical source, cleared all code-cell outputs and execution counts in an independent temporary copy, then launched a new Jupyter kernel and ran all cells in order.
- Every run completed 19/19 code cells with zero errors and produced three decoded, nonblank PNG plots.
- Temporary executed notebooks and the machine-readable run summary were retained only under `$TMPDIR/d404-final-six-run/`.

### Current Source Contract

- The mirrored learner path selects only `profile_{PROFILE_ID}_baseline` through the manifest, verifies its SHA-256, and derives the selected target, baseline config, and case training indices from that one opaque artifact.
- Neither `BASELINE_CONFIGS` nor `profile_train_indices` exists in participant or solution code.
- Profile-specific solution material appears only in instructor answer dictionaries after profile selection; it is not present in the participant notebook or support strings.
- The 10-field team defense forbids `individual_transfer` and directs every learner to the separate `CHECK-D4-04` after defense.
- Team rubric arithmetic is exactly `25 + 20 + 20 + 15 + 10 + 10 = 100`; the individual check is not added to team points.

### Final Live Results

| Profile | Evidence / primary change | Validation result | Target evidence | Optional validation-only path | Authorized test | Wall / checkpoint |
|---|---|---|---|---|---|---:|
| A | class counts; `class_weight: False -> True` | accuracy `0.9109`, macro-F1 `0.9097` | accuracy `+0.0808`; worst recall `+0.5429` | weight decay; accuracy/F1 `0.9109/0.9092` | accuracy/F1 `0.9222/0.9223` | `4.681 / 1.26 s` |
| B | curve dynamics; `dropout: 0.0 -> 0.5` | accuracy `0.9109`, macro-F1 `0.9100` | gap `0.1198 -> 0.0891`, reduction `0.0306` | smaller width; accuracy/F1 `0.8997/0.8998` | accuracy/F1 `0.8944/0.8946` | `4.045 / 1.43 s` |
| C | curve dynamics; `learning_rate: 0.20 -> 0.003` | accuracy `0.8969`, macro-F1 `0.8964` | accuracy `+0.1142`; upward loss variation `0.2738 -> 0.0000` | AdamW; accuracy/F1 `0.8969/0.8964` | accuracy/F1 `0.8944/0.8951` | `3.596 / 0.99 s` |

Each live path denied early test access, requested one evidence card, completed ranked hypotheses and disconfirming evidence, changed exactly one major field, serialized the ledger and evidence board, froze the decision, accessed test once, marked `used_for_further_tuning=False`, and kept the optional run validation-only with `test_reused=False`.

### Final Cached-Recovery Results

| Profile | Validation accuracy / macro-F1 | Recovery contract | Optional path | Wall / checkpoint |
|---|---:|---|---|---:|
| A | `0.9109 / 0.9097` | exact fingerprint; no test authorization, arrays, or metric | not spent | `3.098 / 0.49 s` |
| B | `0.9109 / 0.9100` | exact fingerprint; no test authorization, arrays, or metric | not spent | `3.085 / 0.48 s` |
| C | `0.8969 / 0.8964` | exact fingerprint; no test authorization, arrays, or metric | not spent | `2.982 / 0.49 s` |

All recovery artifacts passed SHA-256 and exact committed-config fingerprint checks. Their keys and string values contained no cause, diagnosis, intervention, checkpoint, or test evidence. Recovery still completed comparison, target evaluation, ledger, evidence board, team defense, reflection, and checkpoint with visible cached provenance.

### Support Hashes and Determinism

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `digits_fixed_splits.npz` | 5,205 | `d137096786526f03f48e17744c6a25e59ac2059e8d7f8d5929121ccc2a8ffd36` |
| `mystery_curves.npz` | 4,295 | `e90fc9590ff11e748b1caa5732de8c7d5ab78a7e18282a5f3d7978d1a62c643b` |
| `digits_evidence.npz` | 34,375 | `1118cf4e6c57f23acabd8b5af20d7c8aae1352b0296078c28fa9e5ff48b02cf6` |
| `experiment_baseline.npz` | 18,626 | `158d5786b20af18623477ce5ae31315d96770e48cb0671c4c45313d967efe34f` |
| `profile_A_baseline.npz` | 21,763 | `08b31bb061def36876ca5fd6d8e2a41ef2da2eb974db8fdcef68c886642de07b` |
| `profile_B_baseline.npz` | 21,058 | `edf856314abb5287f93848d8172dcb499d2c2a4c2a25a67421b84a1ee51bf2ba` |
| `profile_C_baseline.npz` | 22,041 | `e4d3430e074b0ab9581a82362377ac8f32446ebcf8b90a7531c21fbb0a2de3cc` |
| `profile_A_recovery.npz` | 18,808 | `eb6469424d2ac622d6ccb4f03a81225a69ade68c643e779d9be71bb902119f90` |
| `profile_B_recovery.npz` | 19,880 | `ffef55704b2992a23d9886f21fafade55982c5dbfbcf61fb66495b69a19d6780` |
| `profile_C_recovery.npz` | 18,745 | `bcd176dbb17fce2d75fc12135ec6423061d2e5ba2045a1363565d986dd2ed4cf` |

- All sizes and hashes match the current manifest.
- Two isolated generator runs under the terminal sandbox's blocked-network policy reproduced the manifest and all ten NPZs byte-for-byte against canonical and each other.
- The generator contains no network-call code and the manifest records `network_required: false`.
- Every NPZ loaded with `allow_pickle=False`, had no object arrays, and contained no diagnosis, intervention, solution, checkpoint, or test-metric strings.

### Leakage, Release, and Uniqueness

- The participant hash exactly matches `courseware/reviews/participant-validation-LAB-D4-04.md`.
- Participant source contains no instructor/solution/case-key references, completed diagnosis, cross-profile config/change/interpretation map, `individual_transfer` team field, obsolete learner-path helper, or network call.
- `courseware/participant-release-exclusions.txt` excludes the solution notebook, capstone instructor guide, generator, reviews, and all instructor guide/solution trees.
- The only capstone/D4-04 notebooks are the canonical starter and canonical solution; no alternate D4-04 exists.
- `courseware/instructor-solutions/day-4/capstone-case-key.md` already matches opaque loading, validation-only recovery, and team/individual separation, so it was not edited.

### Issues and Notes

- **Fixed:** profile C's solution-only stability gate used total variation, which conflated useful descent with oscillation. It now evaluates upward validation-loss variation and the evidence-board/range text uses the same measure.
- A hosted Google Colab CPU session was unavailable, so hosted readiness was not claimed.
- External participant packaging must continue to honor `participant-release-exclusions.txt`; no repository release builder enforces it automatically.

## Final Status

**PASS WITH NOTES** - the final solution is complete, executable across live and cached-recovery A/B/C, correctly separated, deterministic on the validated local CPU stack, and instructor-ready. Notes are limited to unexecuted hosted Colab validation and external release-tool enforcement.

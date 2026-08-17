# PASS WITH NOTES

## Solution Validation: LAB-D4-03

### Artifacts

- Participant: `courseware/day-4/labs/LAB-D4-03-one-experiment.ipynb`
- Solution: `courseware/instructor-solutions/day-4/LAB-D4-03-one-experiment-SOLUTION.ipynb`
- Participant SHA-256: `bd32475e6cdd08db0b1c552c218472536b50596c20b191d2ece6b9420b0d207e`
- Solution SHA-256: `e7f6b54d4176d0d46f888e3a8029d4851a56eda8e2a0357b2505bd47163e7c0d`

### Environment and Canonical Execution

- macOS Apple silicon, CPU, one PyTorch thread
- Python 3.11.8; NumPy 2.4.6; matplotlib 3.11.1; scikit-learn 1.9.0; PyTorch 2.6.0
- Fresh kernel; fixed local split; no GPU or network
- Clear outputs -> fresh kernel -> Run All: **4.236 s**
- Executed code cells: **16/16**; nonblank PNGs: **2**; errors: **0**

### Canonical Solution Result

- Baseline validation accuracy/macro-F1: `0.8969/0.8940`.
- One primary change: learning rate `0.003 -> 0.001`.
- Primary validation accuracy/macro-F1: `0.8496/0.8445`, an informative negative result under seven epochs.
- Same-seed fresh rerun deltas: `0.0`, within `0.02` tolerance.
- Optional alternate seed executed and was explicitly treated as sensitivity, not reproduction proof.
- Record serialized with split/source/seed/device/versions/config/metrics/repeat/resources/timing/checkpoint identity.
- Canonical parameter evidence: `2,410` parameters, `9,640` bytes; latency uses 20 warmups and 100 repeats with median and p90.

### All Menu Branches

Every bounded branch ran from a fresh kernel. Values are host-specific execution evidence, not a participant tuning leaderboard.

| Branch | Accuracy | Macro-F1 | Bytes | Median ms | Wall s |
|---|---:|---:|---:|---:|---:|
| hidden `(16,)` | 0.8440 | 0.8368 | 4,840 | 0.01027 | 4.364 |
| hidden `(64,)` | 0.9192 | 0.9185 | 19,240 | 0.01058 | 3.488 |
| optimizer `sgd` | 0.4652 | 0.4048 | 9,640 | 0.00988 | 3.555 |
| optimizer `adamw` | 0.8969 | 0.8940 | 9,640 | 0.00985 | 3.450 |
| learning rate `0.001` | 0.8496 | 0.8445 | 9,640 | 0.01025 | 3.503 |
| learning rate `0.01` | 0.9415 | 0.9411 | 9,640 | 0.00979 | 3.512 |
| weight decay `0.001` | 0.8969 | 0.8936 | 9,640 | 0.01025 | 3.553 |
| weight decay `0.01` | 0.9025 | 0.9002 | 9,640 | 0.01000 | 3.430 |
| class weight `True` | 0.8969 | 0.8940 | 9,640 | 0.01010 | 3.481 |

All nine records serialized; all same-seed accuracy deltas were `0.0`. The confounded width/optimizer/learning-rate draft was rejected before compute. A proposal with `epochs=21` raised `Epoch budget exceeds the bounded lab contract` before training.

### Method, Separation, and Issues

- Fresh run recreates model, optimizer, loader generator, and state. Reusing a trained model is not accepted as reproduction.
- Latency method is bounded and valid for local comparison; production alternatives include throughput, peak memory, service tail latency, energy, and artifact bytes with environment/method.
- Participant hash matches its report and participant scan found no solution/instructor links or answers.
- Fixed split and baseline checksums passed. Notebook code contains no network path.
- No solution defect found. Hosted Colab CPU was unavailable and was not executed.

### Final Status

**PASS WITH NOTES** - canonical negative-result path and every practical menu branch are executable, serialized, within budget, and instructor-ready. Note is limited to unexecuted hosted Colab.

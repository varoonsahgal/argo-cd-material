# PASS WITH NOTES

## Solution Validation: LAB-D4-01

### Artifacts

- Participant: `courseware/day-4/labs/LAB-D4-01-accuracy-is-not-enough.ipynb`
- Solution: `courseware/instructor-solutions/day-4/LAB-D4-01-accuracy-is-not-enough-SOLUTION.ipynb`
- Participant SHA-256: `08a02a0ed4ec7866dd208192193903e8455839cba8910003c086ce04c16deff1`
- Solution SHA-256: `a207f709911e1d422f364c4321e407c196aa099b7f0d03c51082c5cae206d3b0`

### Environment and Execution

- macOS Apple silicon, CPU
- Python 3.11.8; NumPy 2.4.6; matplotlib 3.11.1; scikit-learn 1.9.0
- nbformat 5.11.0; nbclient 0.11.0; fresh kernel; no network
- Clear outputs -> fresh kernel -> Run All: **2.875 s**
- Executed code cells: **16/16**; nonblank PNGs: **2**; errors: **0**

### Tasks Covered

- Completed every prediction, metric TODO, threshold sweep, diagnosis, decision, deliberate failure, optional cost scenario, reflection, and checkpoint.
- Explained confusion orientation, `zero_division=0`, majority baseline, threshold effects, asymmetric cost, PR/AP and ROC AUC limits.
- Added expected bands, what/why/concept explanations, hint ladder, misconceptions, alternative decision rules, discussion trigger, troubleshooting, and recovery notes.

### Expected Result Checks

| Check | Result |
|---|---|
| Majority baseline | accuracy `0.9539`; `TN=1717`, `FP=0`, `FN=83`, `TP=0`; minority recall/F1 `0/0` |
| Probability model at `0.50` | recall `0.6627`, precision `0.9167`, F1 `0.7692` |
| Miss-dominant optimum | threshold `0.19` |
| Block-dominant optimum | threshold `0.43` |
| Optional intermediate cost | threshold `0.26` |
| Accuracy-only distinction | selects `probability@0.5`; cost-aware rule selects `probability@0.19` |
| AUC interpretation | ranking summary only; no threshold or consequence choice |
| Plot pixels | both decoded, stable dimensions, nonblank |

### Separation and Issues

- Participant hash matches its current PASS WITH NOTES report and did not change.
- Participant scan found no solution/instructor links, answer key, or completed response.
- Solution metadata is instructor-only and the path is in `participant-release-exclusions.txt`.
- No solution defect found. The authoritative lab map now matches the validated distinction: the majority baseline exposes rare-class failure, and the later accuracy-only rule selects non-cost-optimal `probability@0.5` instead of the miss-dominant `probability@0.19` operating point.
- Hosted Colab CPU was unavailable and was not executed.

### Final Status

**PASS WITH NOTES** - complete, cleanly executable, correctly separated, and instructor-ready on the validated local CPU stack. The only note is the unexecuted hosted Colab environment.

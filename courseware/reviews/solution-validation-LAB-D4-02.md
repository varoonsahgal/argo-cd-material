# PASS WITH NOTES

## Solution Validation: LAB-D4-02

### Artifacts

- Participant: `courseware/day-4/labs/LAB-D4-02-model-detective.ipynb`
- Solution: `courseware/instructor-solutions/day-4/LAB-D4-02-model-detective-SOLUTION.ipynb`
- Participant SHA-256: `259d689bd44501d761f2190e4e04f9bc0caa974179536cd67cb2c95dd24d74ff`
- Solution SHA-256: `0e2db8a7325339fdc0cf40cf67193c2cb30ffe5607bfe3f9822b5f2bd5533e40`

### Environment and Execution

- macOS Apple silicon, CPU
- Python 3.11.8; NumPy 2.4.6; matplotlib 3.11.1; scikit-learn 1.9.0
- Fresh kernel; checksum-verified local artifacts; no network or training
- Clear outputs -> fresh kernel -> Run All: **2.621 s**
- Executed code cells: **17/17**; nonblank PNGs: **5**; errors: **0**

### Tasks Covered

- Answered all four curve bundles with two observations, alternatives, and requested discriminating checks.
- Completed gallery prediction, two reproducible slices, overlap report, exclusive buckets, payoff comparison, next experiment, deliberate failure, optional low-confidence view, reflection, and checkpoint.
- Added what/why/concept notes, multiple valid bucket schemas, hint ladder, misconceptions, discussion prompts, expected outputs, troubleshooting, and recovery.

### Expected Result Checks

| Check | Result |
|---|---|
| Curve bundles | M1 healthy, M2 limited fit, M3 widening gap, M4 unstable; each retains a competing explanation |
| Validation accuracy | `0.9526` in `0.90-0.96` band |
| Confusion | `(10,10)`, true rows/predicted columns |
| Errors | `17`; at least one confidence `>=0.70` |
| High-border slice | `93` examples, `6` errors, payoff proxy `12` |
| Low-total-ink slice | `90` examples, `8` errors, payoff proxy `8` |
| Slice overlap | `18`, reported explicitly |
| Exclusive buckets | high-border `4`, high-confidence `2`, low-total `7`, other `4`; total `17/17` |
| Optional low-confidence errors | `6` |
| Plot pixels | five decoded, nonblank plots |

### Alternative Schemas and Separation

- Accepted schemas include alternate deterministic precedence, directed-pair-first buckets, and multi-label tags plus a separate primary-bucket rule.
- The solution states that gallery selection is not prevalence and payoff is a declared proxy, not causal or business-value proof.
- Both required NPZs matched manifest size/SHA-256, contained no object dtype, and exposed no diagnosis/intervention/test strings.
- Participant hash matches its current report; participant scan found no instructor link, completed answer, or case key.
- Hosted Colab CPU was unavailable and was not executed.

### Final Status

**PASS WITH NOTES** - complete, executable, separated, and instructor-ready locally. The only note is the outstanding hosted Colab environment run.

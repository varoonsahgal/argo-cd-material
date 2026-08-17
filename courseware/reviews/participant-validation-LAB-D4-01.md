# PASS WITH NOTES

## Participant Validation: LAB-D4-01

### Lab

- **Name:** Accuracy Is Not Enough
- **Participant path:** `courseware/day-4/labs/LAB-D4-01-accuracy-is-not-enough.ipynb`
- **Canonical SHA-256:** `08a02a0ed4ec7866dd208192193903e8455839cba8910003c086ce04c16deff1`
- **Learning objective:** `OBJ-D4-01`
- **Validation date:** 2026-08-17
- **Validation status:** **PASS WITH NOTES**
- **Interestingness:** **STRONG** - participants predict consequences, implement zero-division-safe metrics, synchronize threshold/metric/cost evidence, challenge the cost model, and defend an operating point rather than only running supplied code.

### Environment Tested

- macOS on Apple silicon, required local CPU path
- Python 3.11.8
- NumPy 2.4.6, matplotlib 3.11.1, scikit-learn 1.9.0
- nbformat 5.11.0, nbclient 0.11.0, ipykernel 7.3.0
- Fresh temporary venv and fresh kernel; generated local data; no network or prior notebook state

A hosted Google Colab session was unavailable and was not executed.

### Commands and Cells Executed

1. Validated JSON/nbformat, Python syntax, `lab_id`, matching unique official/metadata cell IDs, `metadata.language`, and clean outputs/execution counts.
2. Confirmed blank prediction/diagnosis/decision fields, two visible `NotImplementedError` TODOs, and no instructor path, solution label, or hidden answer.
3. Ran the untouched starter in a fresh kernel. It stopped intentionally at visible **Cell 6** before baseline metrics were revealed.
4. Built a temporary participant-completed copy without reading solution artifacts.
5. Implemented the confusion/metric row with `labels=[0,1]` and `zero_division=0`.
6. Implemented the synchronized threshold sweep and both cost columns.
7. Completed every prediction, diagnosis, threshold decision, challenge, and reflection field.
8. Enabled and executed the optional third cost scenario.
9. Restarted and ran all 16 code cells in order; inspected both rendered plots.

### Runtime Observed

- Untouched starter to intentional stop: **18.718 s** including the first cold kernel/import startup
- Completed Restart/Run All: **2.864 s** wall time
- Notebook checkpoint time: **0.65 s**
- Executed code cells: **16/16**
- Nonblank PNG outputs: **2**
- Uncaught completed-run errors: **0**

### What Worked

- Validation negative-class prevalence was **0.9539**, inside the required `0.95-0.97` range.
- The majority baseline produced `TN=1717`, `FP=0`, `FN=83`, `TP=0`, accuracy **0.9539**, minority recall **0**, and F1 **0** without metric warnings.
- The probability model at the explicit default threshold `0.50` produced recall **0.6627**, inside `0.55-0.85`, with precision **0.9167** and F1 **0.7692**.
- Confusion orientation remained rows=true and columns=predicted throughout metrics, costs, and the plot.
- Miss-dominant cost selected threshold **0.19**; block-dominant cost selected **0.43**. The default `0.50` remained in the sweep.
- The optional intermediate scenario selected **0.26** without refitting or changing score order.
- PR/AP and ROC AUC were used as ranking/overview evidence. The notebook explicitly states that AUC does not choose a deployment threshold.
- The deliberate accuracy-only comparison selected `probability@0.5`, while the consequence-aware rule selected `probability@0.19`; this demonstrates a non-cost-optimal accuracy choice without changing the fitted model.
- Both plot payloads were nonblank: the threshold/confusion/metric/cost dashboard and the PR operating-point plot.

### Failures Encountered

- The starter stopped intentionally at the prediction gate.
- The all-majority classifier intentionally failed the rare-class objective while retaining high accuracy.
- No unintended import, metric, threshold, plotting, runtime, or checkpoint failure occurred.

### Expected vs. Actual Results

| Contract | Expected | Actual |
|---|---|---|
| Majority accuracy | `0.95-0.97` | **0.9539** |
| Majority minority recall/F1 | `0 / 0` | **0 / 0** |
| Useful-model recall at `0.50` | `0.55-0.85` | **0.6627** |
| Confusion orientation | `[[TN,FP],[FN,TP]]` | Passed |
| Scenario thresholds | Distinct, include `0.50` candidate | **0.19 vs 0.43**; `0.50` present |
| AUC interpretation | No AUC-to-threshold claim | Passed |
| Runtime | Under 30 s | **2.864 s** completed wall time |

### Reproducibility and Colab Concerns

- Data, split, and model seeds are fixed; the CPU path requires no files or network.
- APIs and runtime are practical for a hosted CPU notebook, but no hosted Colab execution claim is made.
- The bare system Python lacked `nbformat`; the documented isolated-environment setup resolved this cleanly.

### Required Fixes

None for the participant notebook.

### Optional Improvements

None.

### Retest Requirements

- Run the completed notebook in a fresh hosted Colab CPU session before claiming hosted readiness.
- Retest after changes to the seed, class balance, model, threshold grid, costs, confusion orientation, metric helper, AUC wording, links, or metadata.
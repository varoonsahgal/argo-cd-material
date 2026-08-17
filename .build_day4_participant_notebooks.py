from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def source_lines(text: str) -> list[str]:
    return text.strip("\n").splitlines(keepends=True)


def cell(kind: str, cell_id: str, text: str) -> dict:
    item = {
        "cell_type": kind,
        "id": cell_id,
        "metadata": {"id": cell_id, "language": "python" if kind == "code" else "markdown"},
        "source": source_lines(text),
    }
    if kind == "code":
        item.update({"execution_count": None, "outputs": []})
    return item


def notebook(lab_id: str, cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
            "lab_id": lab_id,
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write(path: str, lab_id: str, cells: list[dict]) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(notebook(lab_id, cells), indent=1) + "\n")


def d401() -> list[dict]:
    return [
        cell("markdown", "d401-01", r"""
# LAB-D4-01: Accuracy Is Not Enough

**Purpose:** Choose metrics and operating thresholds from asymmetric error consequences, then expose how a high aggregate score can hide complete rare-class failure.

**Objectives:** `OBJ-D4-01`  
**Estimated duration:** 40 minutes live; completed CPU path under 30 seconds  
**Prerequisites:** [LESSON-D4-01](../student-guide/day-4-student-guide.md#lesson-d4-01---evaluation-begins-with-consequences), [ACT-D4-01](../challenges/day-4-challenges.md#act-d4-01---cost-council), `OBJ-D2-02`, and Day 3 split validity  
**Environment:** CPU; NumPy, matplotlib, scikit-learn; generated local data; no network or files

Workflow: **Name consequences -> Predict -> Compare baselines -> Implement metrics -> Sweep threshold -> Inspect synchronized evidence -> Choose -> Explain -> Extend**. Fraud is class `1`. The cost tables are teaching scenarios, not complete stakeholder-impact models.
"""),
        cell("code", "d401-02", r"""
import platform
import time

import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score, confusion_matrix, precision_recall_curve,
    precision_recall_fscore_support, roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

SEED = 4101
MODEL_SEED = 4102
DEFAULT_THRESHOLD = 0.50
plt.rcParams.update({"figure.figsize": (9, 5), "axes.grid": True, "grid.alpha": 0.2})
print(f"Python {platform.python_version()} | NumPy {np.__version__} | scikit-learn {sklearn.__version__}")
print("Required path: CPU, local generated data, no network. Runtime target: under 30 seconds.")
"""),
        cell("markdown", "d401-03", r"""
## Recap: Metrics Serve a Decision

Accuracy asks how often a class decision matches. Precision asks what fraction of predicted fraud is fraud. Recall asks what fraction of fraud is found. F1 balances precision and recall, but it does not encode a scenario's actual costs. AUC summarizes ranking over many thresholds; it does not select the operating threshold.
"""),
        cell("code", "d401-04", r"""
started = time.perf_counter()
X, y = make_classification(
    n_samples=6000, n_features=10, n_informative=5, n_redundant=2,
    weights=[0.96, 0.04], class_sep=1.20, flip_y=0.01, random_state=SEED,
)
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=SEED,
)
assert 0.95 <= np.mean(y_val == 0) <= 0.97
print(f"Train/validation: {X_train.shape}/{X_val.shape}; validation fraud rate: {y_val.mean():.3f}")
"""),
        cell("markdown", "d401-05", r"""
## Predict Before Evidence

Commit before calculating anything: predict majority-baseline accuracy and fraud recall, name the costlier error in each scenario, choose a metric set, and predict how lowering the threshold changes false negatives and false positives.
"""),
        cell("code", "d401-06", r"""
metric_predictions = {
    "majority_accuracy_band": "",
    "majority_fraud_recall": "",
    "scenario_one_costlier_error": "",
    "scenario_two_costlier_error": "",
    "metric_set_and_why": "",
    "lower_threshold_effect": "",
}
assert all(value.strip() for value in metric_predictions.values()), (
    "Prediction gate: complete every field before revealing baseline metrics."
)
"""),
        cell("markdown", "d401-07", r"""
## Focused TODO: One Metric Row

Implement `metric_row`. Use confusion-matrix orientation `[[TN, FP], [FN, TP]]`, set `labels=[0,1]`, and pass `zero_division=0` so a no-positive-prediction baseline is informative rather than noisy.
"""),
        cell("code", "d401-08", r"""
def metric_row(y_true, predictions):
    # TODO: return TN, FP, FN, TP, accuracy, precision, recall, and F1.
    raise NotImplementedError("TODO: implement the zero_division-safe metric row")
"""),
        cell("code", "d401-09", r"""
majority_predictions = np.zeros_like(y_val)
majority_metrics = metric_row(y_val, majority_predictions)
print("Majority baseline:", majority_metrics)
assert 0.95 <= majority_metrics["accuracy"] <= 0.97
assert majority_metrics["recall"] == 0.0 and majority_metrics["f1"] == 0.0
"""),
        cell("markdown", "d401-10", r"""
## Observe the Accuracy-Only Failure

An accuracy-only selector may approve the majority baseline. State why that rule fails before fitting a probability model. Repair the *evaluation rule*: do not assume changing the classifier is always the first action.
"""),
        cell("code", "d401-11", r"""
accuracy_only_diagnosis = {"why_it_fails": "", "replacement_evidence": ""}
assert all(value.strip() for value in accuracy_only_diagnosis.values())
"""),
        cell("code", "d401-12", r"""
probability_model = Pipeline([
    ("scale", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000, random_state=MODEL_SEED)),
])
probability_model.fit(X_train, y_train)
fraud_probability = probability_model.predict_proba(X_val)[:, 1]
default_predictions = (fraud_probability >= DEFAULT_THRESHOLD).astype(int)
default_metrics = metric_row(y_val, default_predictions)
default_metrics["roc_auc"] = float(roc_auc_score(y_val, fraud_probability))
default_metrics["average_precision"] = float(average_precision_score(y_val, fraud_probability))
print("Probability model at threshold 0.50:", default_metrics)
assert 0.55 <= default_metrics["recall"] <= 0.85
"""),
        cell("markdown", "d401-13", r"""
## Predict the Threshold Sweep

Two scenarios use the same model scores:

- `miss_dominant`: false negative cost `20`, false positive cost `1`.
- `block_dominant`: false negative cost `5`, false positive cost `4`.

Predict which scenario selects the lower threshold. The synthetic costs simplify delayed and uneven real consequences.
"""),
        cell("code", "d401-14", r"""
threshold_prediction = {"lower_threshold_scenario": "", "reason": "", "what_model_output_stays_fixed": ""}
assert all(value.strip() for value in threshold_prediction.values())

COST_SCENARIOS = {
    "miss_dominant": {"false_negative": 20.0, "false_positive": 1.0},
    "block_dominant": {"false_negative": 5.0, "false_positive": 4.0},
}
thresholds = np.unique(np.r_[np.linspace(0.02, 0.98, 97), DEFAULT_THRESHOLD])
assert DEFAULT_THRESHOLD in thresholds
"""),
        cell("markdown", "d401-15", r"""
## Focused TODO: Synchronized Sweep

For every threshold, call `metric_row` and add each scenario cost: `FN * false_negative + FP * false_positive`. Keep all rows aligned so one selected threshold drives the table and plots.
"""),
        cell("code", "d401-16", r"""
def threshold_sweep(y_true, probabilities, thresholds, cost_scenarios):
    # TODO: return one dictionary per threshold with metrics and one cost per scenario.
    raise NotImplementedError("TODO: build the synchronized threshold sweep")

sweep = threshold_sweep(y_val, fraud_probability, thresholds, COST_SCENARIOS)
assert len(sweep) == len(thresholds)
assert any(np.isclose(row["threshold"], DEFAULT_THRESHOLD) for row in sweep)
"""),
        cell("code", "d401-17", r"""
optimal_rows = {
    scenario: min(sweep, key=lambda row: row[f"cost_{scenario}"])
    for scenario in COST_SCENARIOS
}
for scenario, row in optimal_rows.items():
    print(scenario, {key: round(value, 4) if isinstance(value, float) else value for key, value in row.items()})
assert optimal_rows["miss_dominant"]["threshold"] != optimal_rows["block_dominant"]["threshold"]
"""),
        cell("markdown", "d401-18", r"""
## Inspect: One Threshold, Multiple Consequences

Choose one scenario below. The histogram, confusion matrix, metric traces, and cost trace use the same selected row. Observe what moves with the threshold and what remains a property of the fixed probability model.
"""),
        cell("code", "d401-19", r"""
SELECTED_SCENARIO = "miss_dominant"
selected = optimal_rows[SELECTED_SCENARIO]
selected_threshold = selected["threshold"]
selected_predictions = (fraud_probability >= selected_threshold).astype(int)
selected_confusion = confusion_matrix(y_val, selected_predictions, labels=[0, 1])

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].hist(fraud_probability[y_val == 0], bins=25, alpha=0.65, label="legitimate")
axes[0, 0].hist(fraud_probability[y_val == 1], bins=25, alpha=0.65, label="fraud")
axes[0, 0].axvline(selected_threshold, color="black", linestyle="--", label=f"t={selected_threshold:.2f}")
axes[0, 0].set(title="Fixed probabilities and selected threshold", xlabel="fraud probability", ylabel="examples")
axes[0, 0].legend()
image = axes[0, 1].imshow(selected_confusion, cmap="Greys")
for (row, col), value in np.ndenumerate(selected_confusion): axes[0, 1].text(col, row, str(value), ha="center", va="center")
axes[0, 1].set(title="Confusion matrix", xlabel="predicted", ylabel="actual", xticks=[0,1], yticks=[0,1])
axes[1, 0].plot(thresholds, [row["precision"] for row in sweep], label="precision")
axes[1, 0].plot(thresholds, [row["recall"] for row in sweep], label="recall")
axes[1, 0].plot(thresholds, [row["f1"] for row in sweep], label="F1")
axes[1, 0].axvline(selected_threshold, color="black", linestyle="--")
axes[1, 0].set(title="Metrics move with threshold", xlabel="threshold", ylabel="metric", ylim=(0,1.02)); axes[1,0].legend()
for scenario in COST_SCENARIOS: axes[1, 1].plot(thresholds, [row[f"cost_{scenario}"] for row in sweep], label=scenario)
axes[1, 1].axvline(selected_threshold, color="black", linestyle="--")
axes[1, 1].set(title="Scenario costs", xlabel="threshold", ylabel="synthetic cost"); axes[1,1].legend()
plt.tight_layout(); plt.show()
"""),
        cell("code", "d401-20", r"""
pr_precision, pr_recall, _ = precision_recall_curve(y_val, fraud_probability)
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(pr_recall, pr_precision, color="#2a6f97", label=f"PR curve; AP={default_metrics['average_precision']:.3f}")
ax.scatter(selected["recall"], selected["precision"], color="#c44536", s=80, label=f"selected t={selected_threshold:.2f}")
ax.set(title="Precision-recall overview and operating point", xlabel="recall", ylabel="precision", xlim=(0,1.02), ylim=(0,1.02)); ax.legend()
plt.show()
print(f"ROC AUC overview: {default_metrics['roc_auc']:.3f}; it ranks scores but does not choose the threshold.")
"""),
        cell("markdown", "d401-21", r"""
## Interpret and Defend

Cite confusion counts and consequence assumptions. A defensible answer may choose a different threshold from the cost minimum if it identifies an omitted constraint.
"""),
        cell("code", "d401-22", r"""
threshold_decision = {
    "scenario": "",
    "chosen_threshold": "",
    "confusion_evidence": "",
    "metric_set": "",
    "cost_assumption": "",
    "what_auc_does_not_decide": "",
    "remaining_risk": "",
}
assert all(value.strip() for value in threshold_decision.values())
"""),
        cell("markdown", "d401-23", r"""
## Deliberate Failure and Recovery

The failed rule is `max accuracy => best model`. Compare it with a consequence-aware rule. Explain why the repair changes evaluation rather than changing the already fitted probability scores.
"""),
        cell("code", "d401-24", r"""
accuracy_only_choice = max([("majority", majority_metrics), ("probability@0.5", default_metrics)], key=lambda item: item[1]["accuracy"])[0]
consequence_aware_choice = f"probability@{optimal_rows['miss_dominant']['threshold']:.2f}"
print("Accuracy-only choice:", accuracy_only_choice)
print("Consequence-aware operating point:", consequence_aware_choice)
assert majority_metrics["recall"] == 0.0
"""),
        cell("markdown", "d401-25", r"""
## Challenge: Change the Consequences, Not the Model

Create one additional bounded cost scenario, predict its threshold direction, recompute only the cost column, and explain the new operating point. Do not refit the classifier.
"""),
        cell("code", "d401-26", r"""
RUN_OPTIONAL_SCENARIO = False
optional_scenario = {"false_negative": 12.0, "false_positive": 2.0}
optional_interpretation = {"prediction": "", "observed_threshold": "", "explanation": ""}
if RUN_OPTIONAL_SCENARIO:
    optional_rows = threshold_sweep(y_val, fraud_probability, thresholds, {"optional": optional_scenario})
    optional_best = min(optional_rows, key=lambda row: row["cost_optional"])
    print("Optional best row:", optional_best)
    assert all(value.strip() for value in optional_interpretation.values())
"""),
        cell("markdown", "d401-27", r"""
## Reflection, Takeaways, and Troubleshooting

1. High accuracy can coexist with zero rare-class recall.
2. Threshold movement changes class decisions, not the underlying probability ranking.
3. Precision, recall, F1, PR, and ROC/AUC answer different questions; none supplies stakeholder costs.
4. State the positive class and confusion orientation every time.

| Symptom | Likely cause | Recovery |
|---|---|---|
| Undefined metric warning | No positive predictions and unsafe defaults | Use `zero_division=0` and inspect counts |
| Costs appear reversed | FN/FP orientation swapped | Confirm `[[TN,FP],[FN,TP]]` |
| Threshold `0.5` missing | Sweep grid omitted it | Include it explicitly |
| Runtime exceeds 30 seconds | Dataset/model budget changed | Restore 6,000 examples and one logistic fit |
"""),
        cell("code", "d401-28", r"""
assert majority_metrics["recall"] == 0.0
assert 0.55 <= default_metrics["recall"] <= 0.85
assert optimal_rows["miss_dominant"]["threshold"] != optimal_rows["block_dominant"]["threshold"]
assert all(value.strip() for value in threshold_decision.values())
print(f"LAB-D4-01 checkpoint passed in {time.perf_counter() - started:.2f}s: baseline exposed, thresholds synchronized, and a consequence-aware decision recorded.")
"""),
        cell("markdown", "d401-29", r"""
## Continue

Use the Day 4 guide debrief: [LAB-D4-01 Debrief - What Changed, and What Did Not?](../student-guide/day-4-student-guide.md#lab-d4-01-debrief---what-changed-and-what-did-not).
"""),
    ]


def d402() -> list[dict]:
    return [
        cell("markdown", "d402-01", r"""
# LAB-D4-02: Model Detective - Curves and Error Buckets

**Purpose:** Diagnose unlabeled learning evidence, then turn aligned prediction failures into a prioritized and falsifiable next experiment.

**Objectives:** `OBJ-D4-02`, `OBJ-D4-03`  
**Estimated duration:** 40 minutes live; core CPU analysis under 30 seconds  
**Prerequisites:** [LESSON-D4-02](../student-guide/day-4-student-guide.md#lesson-d4-02---read-curves-as-competing-hypotheses), [LESSON-D4-03](../student-guide/day-4-student-guide.md#lesson-d4-03---error-analysis-turns-an-average-into-a-work-queue), [ACT-D4-02](../challenges/day-4-challenges.md#act-d4-02---mystery-curves), and Day 3 curve evidence  
**Environment:** CPU; NumPy, matplotlib, scikit-learn; packaged fixed artifacts; no network or training required

Workflow: **Observe anonymous curves -> Predict -> Cite two observations -> Inspect aggregate -> Drill into errors -> Define slices -> Quantify prevalence/severity/payoff -> Propose one disconfirming experiment**.
"""),
        cell("code", "d402-02", r"""
import hashlib
import json
import platform
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.metrics import confusion_matrix

started = time.perf_counter()
plt.rcParams.update({"figure.figsize": (9, 5), "axes.grid": True, "grid.alpha": 0.2})

def find_repo_root():
    for candidate in [Path.cwd(), *Path.cwd().parents]:
        if (candidate / "courseware/shared/data/day-4/manifest.json").exists(): return candidate
    raise FileNotFoundError("Run from the repository checkout with courseware/shared/data/day-4 present.")

def file_sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""): digest.update(chunk)
    return digest.hexdigest()

ROOT = find_repo_root(); DATA_DIR = ROOT / "courseware/shared/data/day-4"
manifest = json.loads((DATA_DIR / "manifest.json").read_text())
print(f"Python {platform.python_version()} | NumPy {np.__version__} | scikit-learn {sklearn.__version__}")
"""),
        cell("markdown", "d402-03", r"""
## Local Artifact Contract

The four curve bundles are deterministic and unlabeled. The digits artifact contains aligned validation sample IDs, images, labels, probabilities, predictions, confidence, and label-blind image metadata. It contains no model configuration, diagnosis, bucket answer, or test evidence.
"""),
        cell("code", "d402-04", r"""
for key in ["mystery_curves", "digits_evidence"]:
    record = manifest["artifacts"][key]
    path = DATA_DIR / record["path"]
    assert path.is_file() and file_sha256(path) == record["sha256"]
curves = np.load(DATA_DIR / manifest["artifacts"]["mystery_curves"]["path"], allow_pickle=False)
evidence = np.load(DATA_DIR / manifest["artifacts"]["digits_evidence"]["path"], allow_pickle=False)
print("Verified artifact checksums and aligned arrays.")
"""),
        cell("markdown", "d402-05", r"""
## Observe Anonymous Curves

All bundles use the same neutral colors and axes. Configuration names are intentionally absent. Diagnose from relationships, not styling.
"""),
        cell("code", "d402-06", r"""
fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True)
for bundle_index, (bundle_id, ax) in enumerate(zip(curves["bundle_ids"], axes.ravel())):
    ax.plot(curves["epochs"], curves["train_loss"][bundle_index], color="#3b6c8e", label="train loss")
    ax.plot(curves["epochs"], curves["val_loss"][bundle_index], color="#9b5d42", label="validation loss")
    ax.set(title=f"Mystery {bundle_id}", xlabel="epoch", ylabel="loss"); ax.legend()
plt.tight_layout(); plt.show()
"""),
        cell("markdown", "d402-07", r"""
## Predict Before Labels

For each bundle, record a leading pattern, two curve observations, one competing explanation, and one evidence request. Use the vocabulary healthy fit, limited fit, widening generalization gap, and unstable/stalled optimization only as hypotheses, not unique causes.
"""),
        cell("code", "d402-08", r"""
curve_diagnoses = {
    bundle: {"leading_pattern": "", "observation_one": "", "observation_two": "", "alternative": "", "requested_evidence": ""}
    for bundle in curves["bundle_ids"].tolist()
}
assert all(all(value.strip() for value in response.values()) for response in curve_diagnoses.values())
"""),
        cell("code", "d402-09", r"""
fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True, sharey=True)
for bundle_index, (bundle_id, ax) in enumerate(zip(curves["bundle_ids"], axes.ravel())):
    ax.plot(curves["epochs"], curves["train_accuracy"][bundle_index], color="#3b6c8e", label="train")
    ax.plot(curves["epochs"], curves["val_accuracy"][bundle_index], color="#9b5d42", label="validation")
    ax.set(title=f"Requested accuracy evidence: {bundle_id}", xlabel="epoch", ylabel="accuracy", ylim=(0,1.02)); ax.legend()
plt.tight_layout(); plt.show()
"""),
        cell("markdown", "d402-10", r"""
## Aggregate Digits Baseline

Treat each 8x8 image as a routing-code glyph. First verify alignment, then inspect accuracy and the complete `(10,10)` confusion matrix.
"""),
        cell("code", "d402-11", r"""
sample_ids = evidence["sample_ids"]
images, labels = evidence["images"], evidence["labels"]
probabilities, predictions, confidence = evidence["probabilities"], evidence["predictions"], evidence["confidence"]
assert images.shape[0] == labels.shape[0] == probabilities.shape[0] == len(sample_ids)
assert probabilities.shape[1] == 10 and np.allclose(probabilities.sum(axis=1), 1.0, atol=1e-5)
accuracy = float(np.mean(predictions == labels))
confusion = confusion_matrix(labels, predictions, labels=np.arange(10))
assert 0.90 <= accuracy <= 0.96 and confusion.shape == (10, 10)
print(f"Fixed validation accuracy: {accuracy:.3f}; errors: {np.sum(predictions != labels)}")
"""),
        cell("code", "d402-12", r"""
fig, ax = plt.subplots(figsize=(7, 6)); ax.imshow(confusion, cmap="Greys")
for (row, col), value in np.ndenumerate(confusion):
    if value: ax.text(col, row, str(value), ha="center", va="center", fontsize=8)
ax.set(title="Routing-code confusion matrix", xlabel="predicted", ylabel="actual", xticks=range(10), yticks=range(10)); plt.show()
pair_counts = confusion.copy(); np.fill_diagonal(pair_counts, 0)
top_pairs = np.dstack(np.unravel_index(np.argsort(pair_counts.ravel())[::-1][:5], pair_counts.shape))[0]
print("Top directed confusion pairs:", [(int(a), int(b), int(pair_counts[a,b])) for a,b in top_pairs])
"""),
        cell("markdown", "d402-13", r"""
## Predict Before the Error Gallery

Choose two likely high-value error categories from confusion counts alone. Then state why selected images cannot substitute for prevalence counts.
"""),
        cell("code", "d402-14", r"""
gallery_predictions = {"two_candidate_categories": "", "likely_high_cost_pair": "", "why_gallery_is_not_prevalence": ""}
assert all(value.strip() for value in gallery_predictions.values())
"""),
        cell("code", "d402-15", r"""
error_indices = np.flatnonzero(predictions != labels)
ranked_errors = error_indices[np.argsort(confidence[error_indices])[::-1]]
gallery_indices = ranked_errors[:12]
fig, axes = plt.subplots(3, 4, figsize=(9, 7))
for index, ax in zip(gallery_indices, axes.ravel()):
    ax.imshow(images[index], cmap="gray_r")
    ax.set_title(f"id {sample_ids[index]} | y={labels[index]} p={predictions[index]}\nscore={confidence[index]:.2f}", fontsize=9)
    ax.axis("off")
plt.suptitle("Highest-confidence errors; examples are evidence, not prevalence")
plt.tight_layout(); plt.show()
assert len(gallery_indices) > 0
"""),
        cell("markdown", "d402-16", r"""
## Focused TODO: Two Reproducible Slices

Define at least two boolean masks from supplied metadata. Suggested starting points are high border ink and low total ink; thresholds must be computed from the fixed artifact, not chosen after reading labels. Masks may overlap, but report overlap explicitly.
"""),
        cell("code", "d402-17", r"""
slice_masks = {
    "high_border_ink": None,  # TODO: boolean mask, for example from a fixed metadata quantile.
    "low_total_ink": None,    # TODO: boolean mask with the same length.
}
assert all(isinstance(mask, np.ndarray) and mask.dtype == bool and mask.shape == labels.shape for mask in slice_masks.values())
"""),
        cell("code", "d402-18", r"""
def slice_row(name, mask, severity_weight):
    count = int(mask.sum()); errors = int(np.sum(mask & (predictions != labels)))
    return {
        "slice": name, "count": count, "prevalence": count / len(labels), "errors": errors,
        "error_rate": errors / max(count, 1), "severity_weight": severity_weight,
        "payoff_proxy": errors * severity_weight,
    }

severity_weights = {"high_border_ink": 2.0, "low_total_ink": 1.0}
slice_table = [slice_row(name, mask, severity_weights[name]) for name, mask in slice_masks.items()]
overlap = int(np.logical_and.reduce(list(slice_masks.values())).sum())
for row in slice_table: print(row)
print("Slice overlap:", overlap)
assert all(row["count"] > 0 for row in slice_table)
"""),
        cell("markdown", "d402-19", r"""
## Build Error Buckets Without Double Counting

Assign every error to one primary bucket using a declared precedence. The starter precedence is: high-confidence -> high-border -> low-ink -> other. You may rename categories after inspecting images, but do not encode a diagnosis in the artifact itself.
"""),
        cell("code", "d402-20", r"""
primary_bucket = np.full(len(labels), "not_error", dtype=object)
remaining = predictions != labels
for name, mask in [
    ("high_confidence", confidence >= 0.60),
    ("high_border_ink", slice_masks["high_border_ink"]),
    ("low_total_ink", slice_masks["low_total_ink"]),
]:
    assigned = remaining & mask
    primary_bucket[assigned] = name
    remaining &= ~assigned
primary_bucket[remaining] = "other_error"
bucket_names, bucket_counts = np.unique(primary_bucket[predictions != labels], return_counts=True)
assert bucket_counts.sum() == len(error_indices)
print("Exclusive error buckets:", dict(zip(bucket_names, bucket_counts)))
"""),
        cell("code", "d402-21", r"""
fig, ax = plt.subplots(figsize=(8, 4.5))
payoff_names = [row["slice"] for row in slice_table]
payoff_values = [row["payoff_proxy"] for row in slice_table]
ax.bar(payoff_names, payoff_values, color=["#3b6c8e", "#9b5d42"])
ax.set(title="Payoff proxy combines observed errors and declared severity", ylabel="errors x severity weight")
plt.show()
"""),
        cell("markdown", "d402-22", r"""
## Prioritize One Next Experiment

Frequency, severity, fixability, and spillover can disagree. State one experiment and the evidence that would disconfirm its mechanism. Do not propose several simultaneous changes.
"""),
        cell("code", "d402-23", r"""
next_experiment = {
    "priority_bucket": "", "prevalence_evidence": "", "severity_assumption": "",
    "single_intervention": "", "predicted_observation": "", "disconfirming_evidence": "",
    "competing_explanation": "", "stop_rule": "",
}
assert all(value.strip() for value in next_experiment.values())
"""),
        cell("markdown", "d402-24", r"""
## Deliberate Failure and Recovery

Failure: choose the largest confusion pair and prescribe a bigger model without inspecting train/validation evidence, images, metadata, or labels. Recovery: connect one quantified bucket to one intervention and one falsifying result.
"""),
        cell("code", "d402-25", r"""
failed_draft = {"rule": "largest pair -> bigger model", "attribution_supported": False}
assert not failed_draft["attribution_supported"]
print("Expected design failure caught: aggregate frequency alone does not identify cause or remedy.")
"""),
        cell("markdown", "d402-26", r"""
## Optional Challenge: Add One Non-Overlapping Bucket

Define one additional bucket from confidence or image metadata, insert it into the precedence, and verify that all errors are still counted exactly once. Explain what this category makes visible and what it cannot establish causally.
"""),
        cell("code", "d402-27", r"""
RUN_OPTIONAL_BUCKET = False
optional_bucket = {"name": "", "definition": "", "interpretation_limit": ""}
if RUN_OPTIONAL_BUCKET:
    assert all(value.strip() for value in optional_bucket.values())
    optional_mask = (confidence < 0.45) & (predictions != labels)
    print("Optional low-confidence errors:", int(optional_mask.sum()))
"""),
        cell("markdown", "d402-28", r"""
## Reflection, Takeaways, and Troubleshooting

- A curve pattern supports hypotheses; it does not uniquely name a cause.
- Aggregate -> confusion pair -> examples -> reproducible slices is a narrowing evidence path.
- Report prevalence and consequence before proposing a fix.
- A next experiment earns value by separating plausible explanations.

| Symptom | Likely cause | Recovery |
|---|---|---|
| Checksum mismatch | Stale or modified artifact | Regenerate with the packaged script |
| Images/labels disagree | Arrays were reordered independently | Reload the aligned artifact |
| Bucket totals exceed errors | Overlap was not resolved | Declare precedence or use multi-label accounting explicitly |
| Core exceeds 30 seconds | Training was added | Restore fixed-artifact analysis |
"""),
        cell("code", "d402-29", r"""
assert 0.90 <= accuracy <= 0.96 and confusion.shape == (10, 10)
assert len(slice_table) >= 2 and bucket_counts.sum() == len(error_indices)
assert all(value.strip() for value in next_experiment.values())
print(f"LAB-D4-02 checkpoint passed in {time.perf_counter() - started:.2f}s: curves diagnosed, errors accounted, slices quantified, and one falsifiable experiment prioritized.")
"""),
        cell("markdown", "d402-30", r"""
## Continue

Use the Day 4 guide debrief: [LAB-D4-02 Debrief - From Symptom to Priority](../student-guide/day-4-student-guide.md#lab-d4-02-debrief---from-symptom-to-priority).
"""),
    ]


HARNESS = r'''
import random
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

DEVICE = torch.device("cpu")

def set_all_seeds(seed):
    random.seed(seed); np.random.seed(seed); torch.manual_seed(seed)

class DigitsMLP(nn.Module):
    def __init__(self, hidden=(32,), dropout=0.0):
        super().__init__(); layers = [nn.Flatten()]; input_dim = 64
        for width in hidden:
            layers.extend([nn.Linear(input_dim, width), nn.ReLU()])
            if dropout > 0: layers.append(nn.Dropout(dropout))
            input_dim = width
        layers.append(nn.Linear(input_dim, 10)); self.network = nn.Sequential(*layers)
    def forward(self, inputs): return self.network(inputs)

def evaluate_model(model, X, y):
    model.eval()
    with torch.inference_mode():
        logits = model(X); probabilities = torch.softmax(logits, dim=1).cpu().numpy()
    predictions = probabilities.argmax(1); targets = y.cpu().numpy()
    return {
        "loss": float(nn.CrossEntropyLoss()(logits, y).item()),
        "accuracy": float(accuracy_score(targets, predictions)),
        "macro_f1": float(f1_score(targets, predictions, average="macro", zero_division=0)),
        "probabilities": probabilities, "predictions": predictions,
    }

def run_experiment(config, train_indices, val_indices):
    set_all_seeds(config["seed"])
    model = DigitsMLP(tuple(config["hidden"]), config["dropout"]).to(DEVICE)
    optimizer_class = {"adam": torch.optim.Adam, "adamw": torch.optim.AdamW, "sgd": torch.optim.SGD}[config["optimizer_name"]]
    extra = {"momentum": 0.9} if config["optimizer_name"] == "sgd" else {}
    optimizer = optimizer_class(model.parameters(), lr=config["learning_rate"], weight_decay=config["weight_decay"], **extra)
    selected_labels = y_all[train_indices]
    if config["class_weight"]:
        counts = np.bincount(selected_labels, minlength=10); weights = len(selected_labels) / (10 * np.maximum(counts, 1))
        loss_fn = nn.CrossEntropyLoss(weight=torch.tensor(weights, dtype=torch.float32))
    else: loss_fn = nn.CrossEntropyLoss()
    generator = torch.Generator().manual_seed(4403 + config["seed"])
    loader = DataLoader(TensorDataset(X_all_tensor[train_indices], y_all_tensor[train_indices]), batch_size=config["batch_size"], shuffle=True, generator=generator, num_workers=0)
    history = {name: [] for name in ["train_loss", "val_loss", "train_accuracy", "val_accuracy"]}; started = time.perf_counter()
    for _ in range(config["epochs"]):
        model.train()
        for X_batch, y_batch in loader:
            optimizer.zero_grad(); loss = loss_fn(model(X_batch), y_batch); loss.backward(); optimizer.step()
        train_metrics = evaluate_model(model, X_all_tensor[train_indices], y_all_tensor[train_indices])
        val_metrics = evaluate_model(model, X_all_tensor[val_indices], y_all_tensor[val_indices])
        for prefix, values in [("train", train_metrics), ("val", val_metrics)]:
            history[f"{prefix}_loss"].append(values["loss"]); history[f"{prefix}_accuracy"].append(values["accuracy"])
    return {"model": model, "config": dict(config), "history": history,
            "train": evaluate_model(model, X_all_tensor[train_indices], y_all_tensor[train_indices]),
            "validation": evaluate_model(model, X_all_tensor[val_indices], y_all_tensor[val_indices]),
            "training_seconds": time.perf_counter() - started,
            "parameter_count": sum(p.numel() for p in model.parameters()),
            "parameter_bytes": sum(p.numel() * p.element_size() for p in model.parameters())}

def benchmark_batch1(model, sample, warmup=20, repeats=100):
    model.eval(); timings = []
    with torch.inference_mode():
        for _ in range(warmup): model(sample)
        for _ in range(repeats):
            started = time.perf_counter(); model(sample); timings.append((time.perf_counter() - started) * 1000)
    return {"median_ms": float(np.median(timings)), "p90_ms": float(np.percentile(timings, 90)), "warmup": warmup, "repeats": repeats}
'''


def d403() -> list[dict]:
    return [
        cell("markdown", "d403-01", r"""
# LAB-D4-03: You Get One Experiment

**Purpose:** Design one falsifiable major change, reproduce it with a fresh harness, and compare quality, latency, and size with a complete serializable record.

**Objectives:** `OBJ-D4-04`, `OBJ-D4-05`, `OBJ-D4-06`  
**Estimated duration:** 50 minutes live; completed CPU path under 8 minutes  
**Prerequisites:** [LESSON-D4-04](../student-guide/day-4-student-guide.md#lesson-d4-04---one-experiment-should-teach-one-clear-thing), [LESSON-D4-05](../student-guide/day-4-student-guide.md#lesson-d4-05---reproducibility-makes-evidence-shareable), [LESSON-D4-06](../student-guide/day-4-student-guide.md#lesson-d4-06---quality-lives-on-a-resource-frontier), [ACT-D4-03](../challenges/day-4-challenges.md#act-d4-03---speed-quality-trade-off), and `LAB-D4-02`  
**Environment:** CPU; PyTorch, NumPy, matplotlib, scikit-learn; fixed local digits split; no network

Workflow: **Inspect baseline -> State hypothesis -> Reject confounded draft -> Change one major factor -> Run fresh -> Rerun fresh -> Check tolerance -> Benchmark -> Serialize -> Accept/reject -> Name next experiment without running it**.
"""),
        cell("code", "d403-02", r"""
import hashlib
import json
import platform
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import sklearn
import torch
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, f1_score

torch.set_num_threads(1)
started_lab = time.perf_counter()

def find_repo_root():
    for candidate in [Path.cwd(), *Path.cwd().parents]:
        if (candidate / "courseware/shared/data/day-4/manifest.json").exists(): return candidate
    raise FileNotFoundError("Run from the repository checkout with courseware/shared/data/day-4 present.")

ROOT = find_repo_root(); DATA_DIR = ROOT / "courseware/shared/data/day-4"
manifest = json.loads((DATA_DIR / "manifest.json").read_text())
print(f"Python {platform.python_version()} | torch {torch.__version__} | scikit-learn {sklearn.__version__}")
print("Seeds support repeatability on this stack; they do not promise cross-device or cross-release bitwise equality.")
"""),
        cell("markdown", "d403-03", r"""
## Fixed Data and Baseline Contract

The fixed stratified split hash owns comparison validity. The packaged baseline supplies curves, validation metrics, parameter bytes, and warmed repeated batch-1 latency. This notebook reloads the digits source and independently trains every participant experiment.
"""),
        cell("code", "d403-04", r"""
digits = load_digits(); X_all = digits.images.astype(np.float32); y_all = digits.target.astype(np.int64)
splits = np.load(DATA_DIR / manifest["artifacts"]["fixed_splits"]["path"], allow_pickle=False)
train_indices, val_indices, test_indices = splits["train_indices"], splits["val_indices"], splits["test_indices"]
split_hash = str(splits["split_hash"])
assert split_hash == manifest["fixed_split"]["hash"]
X_all_tensor = torch.tensor(X_all / 16.0, dtype=torch.float32)
y_all_tensor = torch.tensor(y_all, dtype=torch.long)
baseline = np.load(DATA_DIR / manifest["artifacts"]["experiment_baseline"]["path"], allow_pickle=False)
baseline_summary = {
    "validation_accuracy": float(baseline["val_accuracy"][-1]),
    "validation_macro_f1": float(f1_score(baseline["val_labels"], baseline["val_predictions"], average="macro", zero_division=0)),
    "parameter_bytes": int(baseline["parameter_bytes"]),
    "latency_ms": float(baseline["latency_ms_median"]),
}
assert 0.88 <= baseline_summary["validation_accuracy"] <= 0.94
print("Split hash:", split_hash); print("Baseline:", baseline_summary)
"""),
        cell("code", "d403-05", HARNESS),
        cell("code", "d403-06", r"""
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(baseline["epochs"], baseline["train_loss"], label="train"); axes[0].plot(baseline["epochs"], baseline["val_loss"], label="validation")
axes[0].set(title="Fixed baseline loss", xlabel="epoch", ylabel="loss"); axes[0].legend()
axes[1].plot(baseline["epochs"], baseline["train_accuracy"], label="train"); axes[1].plot(baseline["epochs"], baseline["val_accuracy"], label="validation")
axes[1].set(title="Fixed baseline accuracy", xlabel="epoch", ylabel="accuracy", ylim=(0,1.02)); axes[1].legend(); plt.show()
"""),
        cell("markdown", "d403-07", r"""
## Choose One Major Factor

Menu: learning rate, hidden width, weight decay, class weighting, or optimizer. State expected metric, curve, and resource effects plus evidence that rejects the hypothesis.
"""),
        cell("code", "d403-08", r"""
experiment_hypothesis = {
    "baseline_observation": "", "mechanism": "", "single_factor": "",
    "predicted_metric_effect": "", "predicted_curve_effect": "", "predicted_resource_effect": "",
    "disconfirming_evidence": "", "stop_rule": "",
}
assert all(value.strip() for value in experiment_hypothesis.values())
"""),
        cell("code", "d403-09", r"""
BASELINE_CONFIG = {
    "hidden": (32,), "dropout": 0.0, "optimizer_name": "adam", "learning_rate": 0.003,
    "weight_decay": 0.0, "class_weight": False, "epochs": 7, "batch_size": 64, "seed": 4402,
}
MAJOR_FIELDS = {"hidden", "optimizer_name", "learning_rate", "weight_decay", "class_weight"}
INTERVENTION_MENU = {
        "hidden": [(16,), (64,)],
        "optimizer_name": ["sgd", "adamw"],
        "learning_rate": [0.001, 0.01],
        "weight_decay": [0.001, 0.01],
        "class_weight": [True],
}

def major_changes(baseline_config, proposed_config):
    return [field for field in MAJOR_FIELDS if proposed_config[field] != baseline_config[field]]

def validate_one_major_change(baseline_config, proposed_config):
    changes = major_changes(baseline_config, proposed_config)
    if len(changes) != 1: raise ValueError(f"Exactly one major change required; received {changes}")
        changed_field = changes[0]
        if proposed_config[changed_field] not in INTERVENTION_MENU[changed_field]:
                raise ValueError(f"{changed_field} must use one bounded menu value: {INTERVENTION_MENU[changed_field]}")
    if proposed_config["epochs"] > 20: raise ValueError("Epoch budget exceeds the bounded lab contract")
    json.dumps(proposed_config)
        return changed_field
"""),
        cell("markdown", "d403-10", r"""
## Deliberate Failure: Three Changes

The draft below changes width, optimizer, and learning rate. It must fail before compute is spent.
"""),
        cell("code", "d403-11", r"""
confounded_draft = {**BASELINE_CONFIG, "hidden": (128,), "optimizer_name": "sgd", "learning_rate": 0.03}
try:
    validate_one_major_change(BASELINE_CONFIG, confounded_draft)
    raise AssertionError("The confounded draft should not pass")
except ValueError as error:
    print("Expected experiment-design diagnostic:", error)
"""),
        cell("markdown", "d403-12", r"""
## Focused TODO: Select the Experiment

Edit exactly one major field. Epochs, split, seed, batch size, measurement method, and device stay fixed for attribution.
"""),
        cell("code", "d403-13", r"""
PROPOSED_CONFIG = dict(BASELINE_CONFIG)
# TODO: change exactly one of hidden, optimizer_name, learning_rate, weight_decay, or class_weight.
CHANGED_FACTOR = validate_one_major_change(BASELINE_CONFIG, PROPOSED_CONFIG)
print("Authorized factor:", CHANGED_FACTOR)
"""),
        cell("markdown", "d403-14", r"""
## Run Twice From Fresh State

Each call reconstructs model, optimizer, loader, and histories. The same-environment tolerance is absolute difference at most `0.02` for validation accuracy and macro-F1.
"""),
        cell("code", "d403-15", r"""
first_run = run_experiment(PROPOSED_CONFIG, train_indices, val_indices)
second_run = run_experiment(PROPOSED_CONFIG, train_indices, val_indices)
for metric in ["accuracy", "macro_f1"]:
    difference = abs(first_run["validation"][metric] - second_run["validation"][metric])
    print(metric, "difference", difference)
    assert difference <= 0.02
"""),
        cell("code", "d403-16", r"""
latency = benchmark_batch1(first_run["model"], X_all_tensor[val_indices[:1]], warmup=20, repeats=100)
print("Intervention validation:", {key: first_run["validation"][key] for key in ["accuracy", "macro_f1"]})
print("Resources:", {"parameter_bytes": first_run["parameter_bytes"], **latency})
"""),
        cell("markdown", "d403-17", r"""
## Focused TODO: Complete the Serializable Record

Record data/split version, seed, full config, device, package versions, metrics, runtime, parameter bytes, timing method, and a checkpoint identity. The checkpoint identity is a record field; the lab does not persist a trained participant model.
"""),
        cell("code", "d403-18", r"""
experiment_record = {
    "record_schema": 1,
    "run_id": "",  # TODO
    "split_hash": split_hash,
    "data_source": "sklearn.datasets.load_digits",
    "seed": PROPOSED_CONFIG["seed"],
    "device": str(DEVICE),
    "versions": {"torch": torch.__version__, "numpy": np.__version__, "sklearn": sklearn.__version__},
    "changed_factor": CHANGED_FACTOR,
    "config": PROPOSED_CONFIG,
    "metrics": {"accuracy": first_run["validation"]["accuracy"], "macro_f1": first_run["validation"]["macro_f1"]},
    "repeat_metrics": {"accuracy": second_run["validation"]["accuracy"], "macro_f1": second_run["validation"]["macro_f1"]},
    "training_seconds": first_run["training_seconds"],
    "parameter_count": first_run["parameter_count"],
    "parameter_bytes": first_run["parameter_bytes"],
    "latency": latency,
    "checkpoint_identity": "",  # TODO: stable name/hash you would use if persisting this run.
}
assert experiment_record["run_id"] and experiment_record["checkpoint_identity"]
serialized_record = json.dumps(experiment_record, sort_keys=True, indent=2)
print(serialized_record)
"""),
        cell("code", "d403-19", r"""
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
axes[0].plot(baseline["epochs"], baseline["val_accuracy"], label="baseline validation")
axes[0].plot(range(1, len(first_run["history"]["val_accuracy"]) + 1), first_run["history"]["val_accuracy"], label="experiment validation")
axes[0].set(title="Aligned quality evidence", xlabel="epoch", ylabel="accuracy", ylim=(0,1.02)); axes[0].legend()
axes[1].scatter(baseline_summary["latency_ms"], baseline_summary["validation_accuracy"], s=80, label=f"baseline ({baseline_summary['parameter_bytes']} bytes)")
axes[1].scatter(latency["median_ms"], first_run["validation"]["accuracy"], s=80, label=f"experiment ({first_run['parameter_bytes']} bytes)")
axes[1].set(title="Quality-resource comparison", xlabel="median batch-1 latency (ms)", ylabel="validation accuracy"); axes[1].legend()
plt.tight_layout(); plt.show()
"""),
        cell("markdown", "d403-20", r"""
## Interpret: Information Before Improvement

A clean negative result can resolve a hypothesis. Accept or reject based on predicted mechanism, metric evidence, repeatability, and the stated resource constraint.
"""),
        cell("code", "d403-21", r"""
experiment_decision = {
    "hypothesis_supported": "", "metric_delta": "", "curve_evidence": "",
    "repeatability_evidence": "", "resource_tradeoff": "", "accept_or_reject": "",
    "next_single_experiment_not_run": "", "remaining_uncertainty": "",
}
assert all(value.strip() for value in experiment_decision.values())
"""),
        cell("markdown", "d403-22", r"""
## Optional Bounded Rerun: Seed Variation

Only after the core record is complete, change the seed alone for a sensitivity check. This is not a second intervention and must be labeled separately from same-seed reproduction.
"""),
        cell("code", "d403-23", r"""
RUN_OPTIONAL_SEED_VARIATION = False
optional_seed_interpretation = {"difference": "", "what_it_does_not_prove": ""}
if RUN_OPTIONAL_SEED_VARIATION:
    optional_config = {**PROPOSED_CONFIG, "seed": PROPOSED_CONFIG["seed"] + 1}
    optional_run = run_experiment(optional_config, train_indices, val_indices)
    print("Optional seed validation accuracy:", optional_run["validation"]["accuracy"])
    assert all(value.strip() for value in optional_seed_interpretation.values())
"""),
        cell("markdown", "d403-24", r"""
## Challenge: Deployment Constraint Changes

Re-evaluate the same two measured points under one constraint: maximum model bytes, maximum median latency, or minimum macro-F1. Do not run another model. State whether either point is dominated and which production facts this classroom benchmark omits.
"""),
        cell("code", "d403-25", r"""
deployment_decision = {"constraint": "", "chosen_point": "", "dominated_or_not": "", "missing_production_measurements": ""}
assert all(value.strip() for value in deployment_decision.values())
"""),
        cell("markdown", "d403-26", r"""
## Reflection, Takeaways, and Troubleshooting

- Change one major factor when attribution is the learning goal.
- Reset model, optimizer, loader, and seeds for every run.
- A record needs split identity, complete config, environment, metrics, resources, and checkpoint identity.
- Warm up and repeat latency; batch-1 latency is not throughput or production tail latency.

| Symptom | Likely cause | Recovery |
|---|---|---|
| Gate lists several fields | Confounded draft | Reset from `BASELINE_CONFIG` and edit one major field |
| Reruns differ by over `0.02` | State or split was reused/changed | Recreate all state and restore the fixed split |
| Record will not serialize | Tuple/object or missing field | Use JSON-compatible values and complete every identity field |
| Runtime approaches 8 minutes | Epoch/model budget expanded | Restore the bounded menu and CPU thread setting |
"""),
        cell("code", "d403-27", r"""
assert len(major_changes(BASELINE_CONFIG, PROPOSED_CONFIG)) == 1
assert abs(first_run["validation"]["accuracy"] - second_run["validation"]["accuracy"]) <= 0.02
assert abs(first_run["validation"]["macro_f1"] - second_run["validation"]["macro_f1"]) <= 0.02
json.loads(serialized_record)
assert all(value.strip() for value in experiment_decision.values())
assert all(value.strip() for value in deployment_decision.values())
print(f"LAB-D4-03 checkpoint passed in {time.perf_counter() - started_lab:.2f}s: one factor, two fresh runs, complete record, and quality-resource defense.")
"""),
        cell("markdown", "d403-28", r"""
## Continue

Use the Day 4 guide debrief: [LAB-D4-03 Debrief - What Did the Run Buy?](../student-guide/day-4-student-guide.md#lab-d4-03-debrief---what-did-the-run-buy).
"""),
    ]


def d404() -> list[dict]:
    return [
        cell("markdown", "d404-01", r"""
# LAB-D4-04: Capstone - The Neural Network Investigation

**Purpose:** Investigate one anonymous routing-code model profile, commit a falsifiable diagnosis, spend one primary experiment, unlock test evidence only after the decision, and defend the complete evidence chain.

**Objectives:** `OBJ-D4-01` through `OBJ-D4-08`, with primary evidence for `OBJ-D4-08`  
**Estimated duration:** 95 minutes work plus defense; complete single-profile CPU path under 12 minutes  
**Prerequisites:** all prior core labs, especially `LAB-D4-01`, `LAB-D4-02`, `LAB-D4-03`, and [LESSON-D4-08](../day-4/student-guide/day-4-student-guide.md#lesson-d4-08---capstone-defend-the-evidence-chain)  
**Environment:** CPU; PyTorch, NumPy, matplotlib, scikit-learn; fixed local digits data and cached baseline/recovery evidence; no network

Read the [Capstone Student Guide](capstone-student-guide.md) and [Capstone Rubric](capstone-rubric.md). This is the sole participant implementation of `LAB-D4-04`.
"""),
        cell("code", "d404-02", r"""
import hashlib
import json
import platform
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import sklearn
import torch
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

torch.set_num_threads(1)
started_capstone = time.perf_counter()

def find_repo_root():
    for candidate in [Path.cwd(), *Path.cwd().parents]:
        if (candidate / "courseware/shared/data/day-4/manifest.json").exists(): return candidate
    raise FileNotFoundError("Run from the repository checkout with courseware/shared/data/day-4 present.")

ROOT = find_repo_root(); DATA_DIR = ROOT / "courseware/shared/data/day-4"
manifest = json.loads((DATA_DIR / "manifest.json").read_text())
print(f"Python {platform.python_version()} | torch {torch.__version__} | scikit-learn {sklearn.__version__}")
print("Required device: CPU. Fixed seeds aid repeatability but do not imply cross-device bitwise equality.")
"""),
        cell("markdown", "d404-03", r"""
## Case Brief: Routing-Code Recognition

The input is an 8x8 handwritten digit image. A routing system predicts one of ten codes. Misrouting a weak class is costly, but overall quality, generalization, latency, and size still matter. Profiles `A`, `B`, and `C` are anonymous; names, filenames, colors, and metadata do not state a cause.
"""),
        cell("code", "d404-04", r"""
PROFILE_ID = "A"  # TODO: enter the assigned profile: A, B, or C.
assert PROFILE_ID in {"A", "B", "C"}
PROFILE_TARGETS = {
    "A": "Raise worst-class recall by at least 0.05 with no more than 0.02 overall validation-accuracy degradation.",
    "B": "Reduce the train/validation gap by about 0.03 or produce a defensible validation improvement.",
    "C": "Improve validation accuracy by at least 0.05 and make the optimization path more stable.",
}
print("Assigned target:", PROFILE_TARGETS[PROFILE_ID])
"""),
        cell("markdown", "d404-05", r"""
## Fixed Split and Test Lock

The split hash is evidence. Training and validation arrays are bound now. Test indices remain behind a function gate until the primary experiment is interpreted and the decision record is complete.
"""),
        cell("code", "d404-06", r"""
digits = load_digits(); X_all = digits.images.astype(np.float32); y_all = digits.target.astype(np.int64)
splits = np.load(DATA_DIR / manifest["artifacts"]["fixed_splits"]["path"], allow_pickle=False)
train_indices, val_indices = splits["train_indices"], splits["val_indices"]
_locked_test_indices = splits["test_indices"]
split_hash = str(splits["split_hash"])
assert split_hash == manifest["fixed_split"]["hash"]
X_all_tensor = torch.tensor(X_all / 16.0, dtype=torch.float32)
y_all_tensor = torch.tensor(y_all, dtype=torch.long)
TEST_AUTHORIZED = False

def access_test_split():
    if not TEST_AUTHORIZED: raise PermissionError("Test is locked until the decision gate passes.")
    return X_all_tensor[_locked_test_indices], y_all_tensor[_locked_test_indices]

try:
    access_test_split(); raise AssertionError("Test lock failed")
except PermissionError as error:
    print("Expected lock diagnostic:", error)
print("Fixed split hash:", split_hash)
"""),
        cell("code", "d404-07", HARNESS),
        cell("code", "d404-08", r"""
BASELINE_CONFIGS = {
    "A": {"hidden": (32,), "dropout": 0.0, "optimizer_name": "adam", "learning_rate": 0.003, "weight_decay": 0.0, "class_weight": False, "epochs": 10, "batch_size": 64, "seed": 4412},
    "B": {"hidden": (256,128), "dropout": 0.0, "optimizer_name": "adam", "learning_rate": 0.003, "weight_decay": 0.0, "class_weight": False, "epochs": 70, "batch_size": 32, "seed": 4422},
    "C": {"hidden": (32,), "dropout": 0.0, "optimizer_name": "adam", "learning_rate": 0.20, "weight_decay": 0.0, "class_weight": False, "epochs": 8, "batch_size": 64, "seed": 4432},
}

def profile_train_indices(profile_id):
    rng = np.random.default_rng(4401 + {"A":10,"B":20,"C":30}[profile_id])
    if profile_id == "C": return train_indices.copy()
    limits = {class_id: len(train_indices) for class_id in range(10)} if profile_id == "A" else {class_id: 10 for class_id in range(10)}
    if profile_id == "A": limits.update({8:24, 9:32})
    chosen = []
    for class_id in range(10):
        candidates = train_indices[y_all[train_indices] == class_id]
        chosen.append(rng.permutation(candidates)[:limits[class_id]])
    combined = np.concatenate(chosen); return combined[rng.permutation(len(combined))]

case_train_indices = profile_train_indices(PROFILE_ID)
BASELINE_CONFIG = dict(BASELINE_CONFIGS[PROFILE_ID])
baseline = np.load(DATA_DIR / manifest["artifacts"][f"profile_{PROFILE_ID}_baseline"]["path"], allow_pickle=False)
"""),
        cell("markdown", "d404-09", r"""
## Baseline Evidence Board: Facts First

Inspect curves, metrics, confusion, high-confidence errors, runtime, and size before naming a cause. Facts and inferences belong in different fields.
"""),
        cell("code", "d404-10", r"""
baseline_confusion = baseline["confusion"]
baseline_summary = {
    "train_accuracy": float(baseline["train_accuracy"][-1]),
    "validation_accuracy": float(baseline["val_accuracy"][-1]),
    "validation_macro_f1": float(f1_score(baseline["val_labels"], baseline["val_predictions"], average="macro", zero_division=0)),
    "worst_class_recall": float(baseline["class_recall"].min()),
    "training_seconds": float(baseline["training_seconds"]),
    "parameter_bytes": int(baseline["parameter_bytes"]),
    "batch1_latency_ms": float(baseline["latency_ms_median"]),
}
print("Baseline facts:", baseline_summary)
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].plot(baseline["epochs"], baseline["train_loss"], label="train"); axes[0].plot(baseline["epochs"], baseline["val_loss"], label="validation"); axes[0].set(title="Loss", xlabel="epoch"); axes[0].legend()
axes[1].plot(baseline["epochs"], baseline["train_accuracy"], label="train"); axes[1].plot(baseline["epochs"], baseline["val_accuracy"], label="validation"); axes[1].set(title="Accuracy", xlabel="epoch", ylim=(0,1.02)); axes[1].legend()
axes[2].imshow(baseline_confusion, cmap="Greys"); axes[2].set(title="Validation confusion", xlabel="predicted", ylabel="actual", xticks=range(10), yticks=range(10))
plt.tight_layout(); plt.show()
"""),
        cell("code", "d404-11", r"""
val_confidence = baseline["val_probabilities"].max(axis=1)
error_positions = np.flatnonzero(baseline["val_predictions"] != baseline["val_labels"])
shown = error_positions[np.argsort(val_confidence[error_positions])[::-1]][:8]
fig, axes = plt.subplots(2, 4, figsize=(9, 5))
for position, ax in zip(shown, axes.ravel()):
    sample_id = int(baseline["val_sample_ids"][position]); ax.imshow(X_all[sample_id], cmap="gray_r")
    ax.set_title(f"id {sample_id} | y={baseline['val_labels'][position]} p={baseline['val_predictions'][position]}\nscore={val_confidence[position]:.2f}", fontsize=8); ax.axis("off")
plt.suptitle("Selected validation errors; inspect without treating them as prevalence")
plt.tight_layout(); plt.show()
"""),
        cell("markdown", "d404-12", r"""
## Request Exactly One Evidence Card

Choose one: `class_counts`, `curve_dynamics`, `confidence_errors`, or `resource_profile`. Explain why it separates your top two hypotheses before revealing it.
"""),
        cell("code", "d404-13", r"""
evidence_request = {"card": "", "top_two_hypotheses": "", "why_discriminating": ""}
assert evidence_request["card"] in {"class_counts", "curve_dynamics", "confidence_errors", "resource_profile"}
assert all(value.strip() for value in evidence_request.values())

EVIDENCE_CARDS = {
    "class_counts": baseline["train_class_counts"].tolist(),
    "curve_dynamics": {"last_train_loss": float(baseline["train_loss"][-1]), "last_val_loss": float(baseline["val_loss"][-1]), "val_loss_range": float(np.ptp(baseline["val_loss"]))},
    "confidence_errors": {"errors": int(len(error_positions)), "errors_above_0_60": int(np.sum(val_confidence[error_positions] >= 0.60))},
    "resource_profile": {key: baseline_summary[key] for key in ["training_seconds", "parameter_bytes", "batch1_latency_ms"]},
}
print("Requested card:", evidence_request["card"], EVIDENCE_CARDS[evidence_request["card"]])
"""),
        cell("markdown", "d404-14", r"""
## Diagnosis Gate

Rank data/composition, generalization/capacity, optimization, architecture, evaluation, and compute explanations. Name evidence that supports the leader and evidence that would make it wrong. The gate scores reasoning, not a secret label.
"""),
        cell("code", "d404-15", r"""
diagnosis_gate = {
    "ranked_hypotheses": "", "primary_limitation": "", "supporting_metric": "",
    "supporting_curve_or_slice": "", "competing_explanation": "", "disconfirming_evidence": "",
    "target_connection": "", "confidence_and_limit": "",
}
assert all(value.strip() for value in diagnosis_gate.values()), "Complete the diagnosis and disconfirming-evidence gate before spending the run."
"""),
        cell("markdown", "d404-16", r"""
## Choose One Primary Intervention

Allowed major fields: `hidden`, `dropout`, `optimizer_name`, `learning_rate`, `weight_decay`, or `class_weight`. Change exactly one. Predict observations in metrics, curves/slices, and resources before running.
"""),
        cell("code", "d404-17", r"""
MAJOR_FIELDS = {"hidden", "dropout", "optimizer_name", "learning_rate", "weight_decay", "class_weight"}
PRIMARY_CONFIG = dict(BASELINE_CONFIG)
# TODO: change exactly one allowed major field.

changed_fields = [field for field in MAJOR_FIELDS if PRIMARY_CONFIG[field] != BASELINE_CONFIG[field]]
assert len(changed_fields) == 1, f"One primary change required; received {changed_fields}"
assert PRIMARY_CONFIG["epochs"] <= 70
intervention_prediction = {
    "changed_field": changed_fields[0], "mechanism": "", "predicted_metric": "",
    "predicted_curve_or_slice": "", "predicted_resource_effect": "", "rejection_rule": "",
}
assert all(str(value).strip() for value in intervention_prediction.values())
"""),
        cell("markdown", "d404-18", r"""
## Run the Primary Experiment

The default path trains from a fresh model/optimizer/loader. Set recovery only after a technical failure and only after the diagnosis/intervention gates. Recovery succeeds only when the selected config fingerprint matches the anonymous cached run; it never supplies test evidence.
"""),
        cell("code", "d404-19", r"""
def config_fingerprint(config): return hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest()

USE_RECOVERY_AFTER_TECHNICAL_FAILURE = False
primary_run = None; recovery_used = False
if not USE_RECOVERY_AFTER_TECHNICAL_FAILURE:
    primary_run = run_experiment(PRIMARY_CONFIG, case_train_indices, val_indices)
    primary_validation = primary_run["validation"]
    primary_history = primary_run["history"]
    primary_resources = {"training_seconds": primary_run["training_seconds"], "parameter_bytes": primary_run["parameter_bytes"], **benchmark_batch1(primary_run["model"], X_all_tensor[val_indices[:1]])}
else:
    recovery_record = manifest["artifacts"][f"profile_{PROFILE_ID}_recovery"]
    assert config_fingerprint(PRIMARY_CONFIG) == recovery_record["selection_fingerprint"], "No cached recovery matches this already-committed primary config."
    recovery = np.load(DATA_DIR / recovery_record["path"], allow_pickle=False); recovery_used = True
    primary_validation = {"accuracy": float(recovery["val_accuracy"][-1]), "macro_f1": float(f1_score(recovery["val_labels"], recovery["val_predictions"], average="macro", zero_division=0)), "predictions": recovery["val_predictions"], "probabilities": recovery["val_probabilities"]}
    primary_history = {key: recovery[key] for key in ["train_loss", "val_loss", "train_accuracy", "val_accuracy"]}
    primary_resources = {"training_seconds": float(recovery["training_seconds"]), "parameter_bytes": int(recovery["parameter_bytes"]), "median_ms": float(recovery["latency_ms_median"]), "p90_ms": float(recovery["latency_ms_p90"]), "warmup": int(recovery["latency_warmup"]), "repeats": int(recovery["latency_repeats"])}
print("Primary validation:", {key: primary_validation[key] for key in ["accuracy", "macro_f1"]}); print("Recovery used:", recovery_used)
"""),
        cell("code", "d404-20", r"""
primary_confusion = confusion_matrix(y_all[val_indices], primary_validation["predictions"], labels=np.arange(10))
primary_recall = np.diag(primary_confusion) / np.maximum(primary_confusion.sum(1), 1)
comparison = {
    "accuracy_delta": primary_validation["accuracy"] - baseline_summary["validation_accuracy"],
    "macro_f1_delta": primary_validation["macro_f1"] - baseline_summary["validation_macro_f1"],
    "worst_recall_delta": float(primary_recall.min()) - baseline_summary["worst_class_recall"],
    "gap_before": baseline_summary["train_accuracy"] - baseline_summary["validation_accuracy"],
    "gap_after": float(primary_history["train_accuracy"][-1]) - primary_validation["accuracy"],
}
print("Comparison:", comparison)
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(baseline["epochs"], baseline["val_accuracy"], label="baseline"); axes[0].plot(range(1,len(primary_history["val_accuracy"])+1), primary_history["val_accuracy"], label="primary")
axes[0].set(title="Aligned validation accuracy", xlabel="epoch", ylabel="accuracy", ylim=(0,1.02)); axes[0].legend()
axes[1].bar(["baseline", "primary"], [baseline_summary["worst_class_recall"], float(primary_recall.min())], color=["#3b6c8e", "#9b5d42"])
axes[1].set(title="Worst-class recall", ylim=(0,1.02)); plt.tight_layout(); plt.show()
"""),
        cell("markdown", "d404-21", r"""
## Serialize the Ledger and Evidence Board

Separate facts, inference, prediction, observed result, and interpretation. No test evidence belongs here yet.
"""),
        cell("code", "d404-22", r"""
experiment_ledger = {
    "schema": 1, "profile": PROFILE_ID, "split_hash": split_hash, "data_source": "sklearn.datasets.load_digits",
    "device": str(DEVICE), "versions": {"torch": torch.__version__, "numpy": np.__version__, "sklearn": sklearn.__version__},
    "baseline_config": BASELINE_CONFIG, "primary_config": PRIMARY_CONFIG, "changed_field": changed_fields[0],
    "baseline_metrics": baseline_summary, "primary_metrics": {"accuracy": primary_validation["accuracy"], "macro_f1": primary_validation["macro_f1"], "worst_class_recall": float(primary_recall.min())},
    "comparison": comparison, "resources": primary_resources, "recovery_used": recovery_used,
}
evidence_board = {
    "baseline_facts": "", "diagnosis": "", "threatening_evidence": "", "prediction": "",
    "observed_result": "", "interpretation": "", "cost_or_constraint": "", "next_step": "",
}
assert all(value.strip() for value in evidence_board.values())
serialized_ledger = json.dumps(experiment_ledger, sort_keys=True, indent=2); serialized_board = json.dumps(evidence_board, sort_keys=True, indent=2)
json.loads(serialized_ledger); json.loads(serialized_board)
"""),
        cell("markdown", "d404-23", r"""
## Decision Gate Before Test

Accept, reject, or revise the diagnosis. State whether the case target was met, what regression is unacceptable, and what choice is now frozen. This decision consumes validation evidence; test remains untouched until the gate passes.
"""),
        cell("code", "d404-24", r"""
decision_record = {
    "diagnosis_status": "", "target_met_or_not": "", "supporting_delta": "",
    "unacceptable_regression_check": "", "frozen_model_choice": "", "why_no_more_validation_tuning": "",
}
assert all(value.strip() for value in decision_record.values())
TEST_AUTHORIZED = True
X_test, y_test = access_test_split()
print("Test authorized after decision; count:", len(y_test))
"""),
        cell("code", "d404-25", r"""
if primary_run is not None:
    test_metrics = evaluate_model(primary_run["model"], X_test, y_test)
    authorized_test_record = {"accuracy": test_metrics["accuracy"], "macro_f1": test_metrics["macro_f1"], "used_for_further_tuning": False}
else:
    authorized_test_record = {"status": "not available from validation-only recovery artifact", "used_for_further_tuning": False}
print("Authorized test record:", authorized_test_record)
"""),
        cell("markdown", "d404-26", r"""
## Optional Bounded Follow-Up

Only after the primary decision and test record, name a second intervention. The optional branch may run once for learning, but it must not replace the frozen test claim or trigger another test evaluation.
"""),
        cell("code", "d404-27", r"""
RUN_OPTIONAL_FOLLOW_UP = False
optional_follow_up = {"single_change": "", "reason": "", "predicted_validation_evidence": "", "why_test_stays_closed": ""}
if RUN_OPTIONAL_FOLLOW_UP:
    assert all(value.strip() for value in optional_follow_up.values())
    OPTIONAL_CONFIG = dict(PRIMARY_CONFIG)
    # TODO: choose one bounded follow-up field before enabling this branch.
    optional_changed = [field for field in MAJOR_FIELDS if OPTIONAL_CONFIG[field] != PRIMARY_CONFIG[field]]
    assert len(optional_changed) == 1
    optional_run = run_experiment(OPTIONAL_CONFIG, case_train_indices, val_indices)
    print("Optional validation only:", optional_run["validation"]["accuracy"])
"""),
        cell("markdown", "d404-28", r"""
## Defense Fields

Prepare a five-minute defense: what was wrong, what evidence supports and threatens that view, what changed, what happened, why, what it cost, and what should happen next. Include one individual transfer statement for an unfamiliar model problem.
"""),
        cell("code", "d404-29", r"""
defense = {
    "problem_and_consequence": "", "primary_diagnosis": "", "supporting_evidence": "",
    "disconfirming_or_threatening_evidence": "", "single_intervention": "", "observed_result": "",
    "mechanism_explanation": "", "efficiency_and_reproducibility": "", "test_statement": "",
    "next_experiment": "", "individual_transfer": "",
}
assert all(value.strip() for value in defense.values())
"""),
        cell("markdown", "d404-30", r"""
## Challenge and Reflection

Challenge your own case: write the strongest alternative explanation that remains consistent with the evidence and the cheapest new observation that would separate it from your current view. Then identify one way the small digits framing fails to represent a production routing system.
"""),
        cell("code", "d404-31", r"""
reflection = {"strongest_alternative": "", "cheapest_discriminating_observation": "", "simulation_limit": "", "what_you_would_monitor": ""}
assert all(value.strip() for value in reflection.values())
"""),
        cell("markdown", "d404-32", r"""
## Takeaways and Troubleshooting

- The deliverable is a defensible decision trail, not only a score delta.
- Test is a limited final estimate, not an iterative diagnosis surface.
- One requested evidence card and one primary intervention enforce information discipline.
- Recovery artifacts preserve validation defense after technical failure but deliberately contain no test result.

| Symptom | Likely cause | Recovery |
|---|---|---|
| Test access raises `PermissionError` | Decision gate incomplete | Finish and freeze the decision record |
| Recovery fingerprint mismatch | Cached run does not match committed config | Use the live run or defend baseline evidence; do not relabel recovery |
| More than one changed field | Confounded intervention | Reset from the assigned baseline config |
| Profile metrics differ | Split/seed/config changed | Restore manifest split hash and assigned settings |
| Runtime approaches 12 minutes | Optional or epoch budget expanded | Stop after the primary bounded run |
"""),
        cell("code", "d404-33", r"""
assert split_hash == manifest["fixed_split"]["hash"] and TEST_AUTHORIZED
assert len(changed_fields) == 1
json.loads(serialized_ledger); json.loads(serialized_board)
assert all(value.strip() for value in defense.values())
assert all(value.strip() for value in reflection.values())
print(f"LAB-D4-04 checkpoint passed for profile {PROFILE_ID} in {time.perf_counter() - started_capstone:.2f}s: diagnosis gated, primary run recorded, test lock honored, and defense complete.")
"""),
        cell("markdown", "d404-34", r"""
## Submit

Return to the [Day 4 capstone debrief](../day-4/student-guide/day-4-student-guide.md#capstone-debrief) and check every field against the [Capstone Rubric](capstone-rubric.md). Keep the serialized ledger and evidence board with your participant submission.
"""),
    ]


write("courseware/day-4/labs/LAB-D4-01-accuracy-is-not-enough.ipynb", "LAB-D4-01", d401())
write("courseware/day-4/labs/LAB-D4-02-model-detective.ipynb", "LAB-D4-02", d402())
write("courseware/day-4/labs/LAB-D4-03-one-experiment.ipynb", "LAB-D4-03", d403())
write("courseware/capstone/capstone-starter.ipynb", "LAB-D4-04", d404())
print("Wrote four Day 4 participant notebooks.")
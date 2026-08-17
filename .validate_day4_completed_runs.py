from __future__ import annotations

import json
import os
import time
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent


def load(path):
    return json.loads((ROOT / path).read_text())


def replace_cell(notebook, cell_id, source):
    for cell in notebook["cells"]:
        if cell["id"] == cell_id:
            cell["source"] = source.strip("\n").splitlines(keepends=True)
            return
    raise KeyError(cell_id)


def execute(notebook, label):
    namespace = {"__name__": "__main__"}
    started = time.perf_counter()
    for number, cell in enumerate(notebook["cells"], 1):
        if cell["cell_type"] != "code":
            continue
        source = "".join(cell["source"])
        try:
            exec(compile(source, f"{label}:cell-{number}", "exec"), namespace)
        except Exception as error:
            raise RuntimeError(f"{label} failed in visible cell {number}: {error}") from error
        finally:
            plt.close("all")
    namespace["validation_wall_seconds"] = time.perf_counter() - started
    return namespace


def filled_dict(name, keys):
    body = ",\n".join(f'    "{key}": "completed evidence"' for key in keys)
    return f"{name} = {{\n{body}\n}}\nassert all(value.strip() for value in {name}.values())"


def validate_d401():
    nb = load("courseware/day-4/labs/LAB-D4-01-accuracy-is-not-enough.ipynb")
    replace_cell(nb, "d401-06", filled_dict("metric_predictions", ["majority_accuracy_band", "majority_fraud_recall", "scenario_one_costlier_error", "scenario_two_costlier_error", "metric_set_and_why", "lower_threshold_effect"]))
    replace_cell(nb, "d401-08", '''
def metric_row(y_true, predictions):
    tn, fp, fn, tp = confusion_matrix(y_true, predictions, labels=[0, 1]).ravel()
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, predictions, average="binary", zero_division=0)
    return {"tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp), "accuracy": float(np.mean(predictions == y_true)), "precision": float(precision), "recall": float(recall), "f1": float(f1)}
''')
    replace_cell(nb, "d401-11", filled_dict("accuracy_only_diagnosis", ["why_it_fails", "replacement_evidence"]))
    replace_cell(nb, "d401-14", '''
threshold_prediction = {"lower_threshold_scenario": "miss dominant", "reason": "false negatives cost more", "what_model_output_stays_fixed": "probability scores"}
COST_SCENARIOS = {"miss_dominant": {"false_negative": 20.0, "false_positive": 1.0}, "block_dominant": {"false_negative": 5.0, "false_positive": 4.0}}
thresholds = np.unique(np.r_[np.linspace(0.02, 0.98, 97), DEFAULT_THRESHOLD])
assert DEFAULT_THRESHOLD in thresholds
''')
    replace_cell(nb, "d401-16", '''
def threshold_sweep(y_true, probabilities, thresholds, cost_scenarios):
    rows = []
    for threshold in thresholds:
        row = {"threshold": float(threshold), **metric_row(y_true, (probabilities >= threshold).astype(int))}
        for name, costs in cost_scenarios.items():
            row[f"cost_{name}"] = row["fn"] * costs["false_negative"] + row["fp"] * costs["false_positive"]
        rows.append(row)
    return rows
sweep = threshold_sweep(y_val, fraud_probability, thresholds, COST_SCENARIOS)
assert len(sweep) == len(thresholds) and any(np.isclose(row["threshold"], DEFAULT_THRESHOLD) for row in sweep)
''')
    replace_cell(nb, "d401-22", filled_dict("threshold_decision", ["scenario", "chosen_threshold", "confusion_evidence", "metric_set", "cost_assumption", "what_auc_does_not_decide", "remaining_risk"]))
    replace_cell(nb, "d401-26", '''
RUN_OPTIONAL_SCENARIO = True
optional_scenario = {"false_negative": 12.0, "false_positive": 2.0}
optional_interpretation = {"prediction": "between scenarios", "observed_threshold": "recorded", "explanation": "cost ratio changed"}
if RUN_OPTIONAL_SCENARIO:
    optional_rows = threshold_sweep(y_val, fraud_probability, thresholds, {"optional": optional_scenario})
    optional_best = min(optional_rows, key=lambda row: row["cost_optional"])
    print("Optional best row:", optional_best)
    assert all(value.strip() for value in optional_interpretation.values())
''')
    ns = execute(nb, "LAB-D4-01")
    return {"seconds": ns["validation_wall_seconds"], "majority_accuracy": ns["majority_metrics"]["accuracy"], "majority_recall": ns["majority_metrics"]["recall"], "default_recall": ns["default_metrics"]["recall"], "thresholds": {key: row["threshold"] for key, row in ns["optimal_rows"].items()}}


def validate_d402():
    nb = load("courseware/day-4/labs/LAB-D4-02-model-detective.ipynb")
    replace_cell(nb, "d402-08", '''
curve_diagnoses = {bundle: {"leading_pattern": "hypothesis", "observation_one": "train evidence", "observation_two": "validation evidence", "alternative": "competing explanation", "requested_evidence": "accuracy"} for bundle in curves["bundle_ids"].tolist()}
assert all(all(value.strip() for value in response.values()) for response in curve_diagnoses.values())
''')
    replace_cell(nb, "d402-14", filled_dict("gallery_predictions", ["two_candidate_categories", "likely_high_cost_pair", "why_gallery_is_not_prevalence"]))
    replace_cell(nb, "d402-17", '''
slice_masks = {
    "high_border_ink": evidence["border_ink"] >= np.quantile(evidence["border_ink"], 0.75),
    "low_total_ink": evidence["ink_total"] <= np.quantile(evidence["ink_total"], 0.25),
}
assert all(isinstance(mask, np.ndarray) and mask.dtype == bool and mask.shape == labels.shape for mask in slice_masks.values())
''')
    replace_cell(nb, "d402-23", filled_dict("next_experiment", ["priority_bucket", "prevalence_evidence", "severity_assumption", "single_intervention", "predicted_observation", "disconfirming_evidence", "competing_explanation", "stop_rule"]))
    replace_cell(nb, "d402-27", '''
RUN_OPTIONAL_BUCKET = True
optional_bucket = {"name": "low confidence", "definition": "score below 0.45", "interpretation_limit": "not causal"}
if RUN_OPTIONAL_BUCKET:
    assert all(value.strip() for value in optional_bucket.values())
    optional_mask = (confidence < 0.45) & (predictions != labels)
    print("Optional low-confidence errors:", int(optional_mask.sum()))
''')
    ns = execute(nb, "LAB-D4-02")
    return {"seconds": ns["validation_wall_seconds"], "accuracy": ns["accuracy"], "confusion_shape": list(ns["confusion"].shape), "errors": len(ns["error_indices"]), "slice_counts": {row["slice"]: row["count"] for row in ns["slice_table"]}}


def validate_d403():
    nb = load("courseware/day-4/labs/LAB-D4-03-one-experiment.ipynb")
    replace_cell(nb, "d403-08", filled_dict("experiment_hypothesis", ["baseline_observation", "mechanism", "single_factor", "predicted_metric_effect", "predicted_curve_effect", "predicted_resource_effect", "disconfirming_evidence", "stop_rule"]))
    replace_cell(nb, "d403-13", '''
PROPOSED_CONFIG = dict(BASELINE_CONFIG)
PROPOSED_CONFIG["learning_rate"] = 0.001
CHANGED_FACTOR = validate_one_major_change(BASELINE_CONFIG, PROPOSED_CONFIG)
print("Authorized factor:", CHANGED_FACTOR)
''')
    original = next(cell for cell in nb["cells"] if cell["id"] == "d403-18")
    text = "".join(original["source"]).replace('"run_id": "",  # TODO', '"run_id": "validation-run",  # TODO').replace('"checkpoint_identity": "",  # TODO: stable name/hash you would use if persisting this run.', '"checkpoint_identity": "validation-run-state",  # TODO: stable name/hash you would use if persisting this run.')
    replace_cell(nb, "d403-18", text)
    replace_cell(nb, "d403-21", filled_dict("experiment_decision", ["hypothesis_supported", "metric_delta", "curve_evidence", "repeatability_evidence", "resource_tradeoff", "accept_or_reject", "next_single_experiment_not_run", "remaining_uncertainty"]))
    replace_cell(nb, "d403-23", '''
RUN_OPTIONAL_SEED_VARIATION = True
optional_seed_interpretation = {"difference": "recorded", "what_it_does_not_prove": "universal determinism"}
if RUN_OPTIONAL_SEED_VARIATION:
    optional_config = {**PROPOSED_CONFIG, "seed": PROPOSED_CONFIG["seed"] + 1}
    optional_run = run_experiment(optional_config, train_indices, val_indices)
    print("Optional seed validation accuracy:", optional_run["validation"]["accuracy"])
    assert all(value.strip() for value in optional_seed_interpretation.values())
''')
    replace_cell(nb, "d403-25", filled_dict("deployment_decision", ["constraint", "chosen_point", "dominated_or_not", "missing_production_measurements"]))
    ns = execute(nb, "LAB-D4-03")
    return {"seconds": ns["validation_wall_seconds"], "baseline_accuracy": ns["baseline_summary"]["validation_accuracy"], "run_accuracy": ns["first_run"]["validation"]["accuracy"], "macro_f1": ns["first_run"]["validation"]["macro_f1"], "repeat_accuracy_delta": abs(ns["first_run"]["validation"]["accuracy"] - ns["second_run"]["validation"]["accuracy"]), "parameter_bytes": ns["first_run"]["parameter_bytes"], "latency_ms": ns["latency"]["median_ms"]}


def validate_d404(profile, recovery=False, optional=True):
    nb = load("courseware/capstone/capstone-starter.ipynb")
    replace_cell(nb, "d404-04", f'''PROFILE_ID = "{profile}"
assert PROFILE_ID in {{"A", "B", "C"}}
PROFILE_TARGETS = {{"A": "Raise worst-class recall by at least 0.05 with no more than 0.02 overall validation-accuracy degradation.", "B": "Reduce the train/validation gap by about 0.03 or produce a defensible validation improvement.", "C": "Improve validation accuracy by at least 0.05 and make the optimization path more stable."}}
print("Assigned target:", PROFILE_TARGETS[PROFILE_ID])''')
    replace_cell(nb, "d404-13", '''
evidence_request = {"card": "curve_dynamics", "top_two_hypotheses": "two plausible explanations", "why_discriminating": "relationships differ"}
assert evidence_request["card"] in {"class_counts", "curve_dynamics", "confidence_errors", "resource_profile"}
assert all(value.strip() for value in evidence_request.values())
EVIDENCE_CARDS = {"class_counts": baseline["train_class_counts"].tolist(), "curve_dynamics": {"last_train_loss": float(baseline["train_loss"][-1]), "last_val_loss": float(baseline["val_loss"][-1]), "val_loss_range": float(np.ptp(baseline["val_loss"]))}, "confidence_errors": {"errors": int(len(error_positions)), "errors_above_0_60": int(np.sum(val_confidence[error_positions] >= 0.60))}, "resource_profile": {key: baseline_summary[key] for key in ["training_seconds", "parameter_bytes", "batch1_latency_ms"]}}
print("Requested card:", evidence_request["card"], EVIDENCE_CARDS[evidence_request["card"]])
''')
    replace_cell(nb, "d404-15", filled_dict("diagnosis_gate", ["ranked_hypotheses", "primary_limitation", "supporting_metric", "supporting_curve_or_slice", "competing_explanation", "disconfirming_evidence", "target_connection", "confidence_and_limit"]))
    changes = {"A": 'PRIMARY_CONFIG["class_weight"] = True', "B": 'PRIMARY_CONFIG["dropout"] = 0.5', "C": 'PRIMARY_CONFIG["learning_rate"] = 0.003'}
    replace_cell(nb, "d404-17", f'''
MAJOR_FIELDS = {{"hidden", "dropout", "optimizer_name", "learning_rate", "weight_decay", "class_weight"}}
PRIMARY_CONFIG = dict(BASELINE_CONFIG)
{changes[profile]}
changed_fields = [field for field in MAJOR_FIELDS if PRIMARY_CONFIG[field] != BASELINE_CONFIG[field]]
assert len(changed_fields) == 1 and PRIMARY_CONFIG["epochs"] <= 70
intervention_prediction = {{"changed_field": changed_fields[0], "mechanism": "predicted mechanism", "predicted_metric": "target movement", "predicted_curve_or_slice": "aligned evidence", "predicted_resource_effect": "bounded", "rejection_rule": "no target movement"}}
assert all(str(value).strip() for value in intervention_prediction.values())
''')
    original = next(cell for cell in nb["cells"] if cell["id"] == "d404-19")
    replace_cell(nb, "d404-19", "".join(original["source"]).replace("USE_RECOVERY_AFTER_TECHNICAL_FAILURE = False", f"USE_RECOVERY_AFTER_TECHNICAL_FAILURE = {str(recovery)}"))
    replace_cell(nb, "d404-22", '''
experiment_ledger = {"schema": 1, "profile": PROFILE_ID, "split_hash": split_hash, "data_source": "sklearn.datasets.load_digits", "device": str(DEVICE), "versions": {"torch": torch.__version__, "numpy": np.__version__, "sklearn": sklearn.__version__}, "baseline_config": BASELINE_CONFIG, "primary_config": PRIMARY_CONFIG, "changed_field": changed_fields[0], "baseline_metrics": baseline_summary, "primary_metrics": {"accuracy": primary_validation["accuracy"], "macro_f1": primary_validation["macro_f1"], "worst_class_recall": float(primary_recall.min())}, "comparison": comparison, "resources": primary_resources, "recovery_used": recovery_used}
evidence_board = {"baseline_facts": "recorded", "diagnosis": "reasoned", "threatening_evidence": "recorded", "prediction": "recorded", "observed_result": "recorded", "interpretation": "recorded", "cost_or_constraint": "recorded", "next_step": "recorded"}
serialized_ledger = json.dumps(experiment_ledger, sort_keys=True, indent=2); serialized_board = json.dumps(evidence_board, sort_keys=True, indent=2)
json.loads(serialized_ledger); json.loads(serialized_board)
''')
    replace_cell(nb, "d404-24", '''
decision_record = {"diagnosis_status": "supported or revised", "target_met_or_not": "evaluated", "supporting_delta": "recorded", "unacceptable_regression_check": "checked", "frozen_model_choice": "primary", "why_no_more_validation_tuning": "test integrity"}
assert all(value.strip() for value in decision_record.values())
TEST_AUTHORIZED = True
X_test, y_test = access_test_split()
print("Test authorized after decision; count:", len(y_test))
''')
    if optional and not recovery:
        replace_cell(nb, "d404-27", '''
RUN_OPTIONAL_FOLLOW_UP = True
optional_follow_up = {"single_change": "weight decay", "reason": "bounded sensitivity", "predicted_validation_evidence": "small change", "why_test_stays_closed": "decision already consumed test"}
if RUN_OPTIONAL_FOLLOW_UP:
    assert all(value.strip() for value in optional_follow_up.values())
    OPTIONAL_CONFIG = dict(PRIMARY_CONFIG); OPTIONAL_CONFIG["weight_decay"] = 0.001
    optional_changed = [field for field in MAJOR_FIELDS if OPTIONAL_CONFIG[field] != PRIMARY_CONFIG[field]]
    assert len(optional_changed) == 1
    optional_run = run_experiment(OPTIONAL_CONFIG, case_train_indices, val_indices)
    print("Optional validation only:", optional_run["validation"]["accuracy"])
''')
    replace_cell(nb, "d404-29", filled_dict("defense", ["problem_and_consequence", "primary_diagnosis", "supporting_evidence", "disconfirming_or_threatening_evidence", "single_intervention", "observed_result", "mechanism_explanation", "efficiency_and_reproducibility", "test_statement", "next_experiment", "individual_transfer"]))
    replace_cell(nb, "d404-31", filled_dict("reflection", ["strongest_alternative", "cheapest_discriminating_observation", "simulation_limit", "what_you_would_monitor"]))
    ns = execute(nb, f"LAB-D4-04-{profile}-{'recovery' if recovery else 'live'}")
    return {"seconds": ns["validation_wall_seconds"], "profile": profile, "recovery": recovery, "baseline": ns["baseline_summary"], "primary_accuracy": ns["primary_validation"]["accuracy"], "primary_macro_f1": ns["primary_validation"]["macro_f1"], "worst_recall_delta": ns["comparison"]["worst_recall_delta"], "gap_before": ns["comparison"]["gap_before"], "gap_after": ns["comparison"]["gap_after"], "test": ns["authorized_test_record"]}


results = {
    "LAB-D4-01": validate_d401(),
    "LAB-D4-02": validate_d402(),
    "LAB-D4-03": validate_d403(),
    "capstone_live": [validate_d404(profile, recovery=False, optional=True) for profile in "ABC"],
    "capstone_recovery": [validate_d404(profile, recovery=True, optional=False) for profile in "ABC"],
}
print("VALIDATION_RESULTS")
print(json.dumps(results, indent=2))
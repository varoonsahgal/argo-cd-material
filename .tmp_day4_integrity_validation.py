from __future__ import annotations

import contextlib
import io
import json
import os
import time
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent
PROFILE = os.environ["DAY4_PROFILE"]
RECOVERY = os.environ.get("DAY4_RECOVERY", "0") == "1"


def load_notebook() -> dict:
    return json.loads((ROOT / "courseware/capstone/capstone-starter.ipynb").read_text())


def replace_cell(notebook: dict, cell_id: str, source: str) -> None:
    for cell in notebook["cells"]:
        if cell["id"] == cell_id:
            cell["source"] = source.strip("\n").splitlines(keepends=True)
            return
    raise KeyError(cell_id)


def filled_dict(name: str, keys: list[str]) -> str:
    body = ",\n".join(f'    "{key}": "completed evidence"' for key in keys)
    return f"{name} = {{\n{body}\n}}\nassert all(value.strip() for value in {name}.values())"


notebook = load_notebook()
selector = next(cell for cell in notebook["cells"] if cell["id"] == "d404-04")
selector_source = "".join(selector["source"]).replace('PROFILE_ID = "A"', f'PROFILE_ID = "{PROFILE}"', 1)
replace_cell(notebook, "d404-04", selector_source)
replace_cell(
    notebook,
    "d404-13",
    '''
evidence_request = {"card": "curve_dynamics", "top_two_hypotheses": "two plausible explanations", "why_discriminating": "relationships differ"}
assert evidence_request["card"] in {"class_counts", "curve_dynamics", "confidence_errors", "resource_profile"}
assert all(value.strip() for value in evidence_request.values())
EVIDENCE_CARDS = {
    "class_counts": baseline["train_class_counts"].tolist(),
    "curve_dynamics": {"last_train_loss": float(baseline["train_loss"][-1]), "last_val_loss": float(baseline["val_loss"][-1]), "val_loss_range": float(np.ptp(baseline["val_loss"]))},
    "confidence_errors": {"errors": int(len(error_positions)), "errors_above_0_60": int(np.sum(val_confidence[error_positions] >= 0.60))},
    "resource_profile": {key: baseline_summary[key] for key in ["training_seconds", "parameter_bytes", "batch1_latency_ms"]},
}
print("Requested card:", evidence_request["card"], EVIDENCE_CARDS[evidence_request["card"]])
''',
)
replace_cell(
    notebook,
    "d404-15",
    filled_dict(
        "diagnosis_gate",
        [
            "ranked_hypotheses",
            "primary_limitation",
            "supporting_metric",
            "supporting_curve_or_slice",
            "competing_explanation",
            "disconfirming_evidence",
            "target_connection",
            "confidence_and_limit",
        ],
    ),
)
changes = {
    "A": 'PRIMARY_CONFIG["class_weight"] = True',
    "B": 'PRIMARY_CONFIG["dropout"] = 0.5',
    "C": 'PRIMARY_CONFIG["learning_rate"] = 0.003',
}
replace_cell(
    notebook,
    "d404-17",
    f'''
MAJOR_FIELDS = {{"hidden", "dropout", "optimizer_name", "learning_rate", "weight_decay", "class_weight"}}
PRIMARY_CONFIG = dict(BASELINE_CONFIG)
{changes[PROFILE]}
changed_fields = [field for field in MAJOR_FIELDS if PRIMARY_CONFIG[field] != BASELINE_CONFIG[field]]
assert len(changed_fields) == 1 and PRIMARY_CONFIG["epochs"] <= 70
intervention_prediction = {{"changed_field": changed_fields[0], "mechanism": "predicted mechanism", "predicted_metric": "target movement", "predicted_curve_or_slice": "aligned evidence", "predicted_resource_effect": "bounded", "rejection_rule": "no target movement"}}
assert all(str(value).strip() for value in intervention_prediction.values())
''',
)
run_cell = next(cell for cell in notebook["cells"] if cell["id"] == "d404-19")
replace_cell(
    notebook,
    "d404-19",
    "".join(run_cell["source"]).replace(
        "USE_RECOVERY_AFTER_TECHNICAL_FAILURE = False",
        f"USE_RECOVERY_AFTER_TECHNICAL_FAILURE = {RECOVERY}",
    ),
)
replace_cell(
    notebook,
    "d404-22",
    '''
experiment_ledger = {
    "schema": 1, "profile": PROFILE_ID, "split_hash": split_hash, "data_source": "sklearn.datasets.load_digits",
    "device": str(DEVICE), "versions": {"torch": torch.__version__, "numpy": np.__version__, "sklearn": sklearn.__version__},
    "baseline_config": BASELINE_CONFIG, "primary_config": PRIMARY_CONFIG, "changed_field": changed_fields[0],
    "baseline_metrics": baseline_summary,
    "primary_metrics": {"accuracy": primary_validation["accuracy"], "macro_f1": primary_validation["macro_f1"], "worst_class_recall": float(primary_recall.min())},
    "comparison": comparison, "resources": primary_resources, "recovery_used": recovery_used,
}
evidence_board = {"baseline_facts": "recorded", "diagnosis": "reasoned", "threatening_evidence": "recorded", "prediction": "recorded", "observed_result": "recorded", "interpretation": "recorded", "cost_or_constraint": "recorded", "next_step": "recorded"}
serialized_ledger = json.dumps(experiment_ledger, sort_keys=True, indent=2)
serialized_board = json.dumps(evidence_board, sort_keys=True, indent=2)
json.loads(serialized_ledger); json.loads(serialized_board)
''',
)
replace_cell(
    notebook,
    "d404-24",
    '''
decision_record = {"diagnosis_status": "supported or revised", "target_met_or_not": "evaluated", "supporting_delta": "recorded", "unacceptable_regression_check": "checked", "frozen_model_choice": "primary", "why_no_more_validation_tuning": "test integrity"}
assert all(value.strip() for value in decision_record.values())
TEST_AUTHORIZED = True
X_test, y_test = access_test_split()
print("Test authorized after decision; count:", len(y_test))
''',
)
if not RECOVERY:
    replace_cell(
        notebook,
        "d404-27",
        '''
RUN_OPTIONAL_FOLLOW_UP = True
optional_follow_up = {"single_change": "weight decay", "reason": "bounded sensitivity", "predicted_validation_evidence": "small validation change", "why_test_stays_closed": "frozen test claim"}
if RUN_OPTIONAL_FOLLOW_UP:
    assert all(value.strip() for value in optional_follow_up.values())
    OPTIONAL_CONFIG = dict(PRIMARY_CONFIG)
    OPTIONAL_CONFIG["weight_decay"] = 0.001
    optional_changed = [field for field in MAJOR_FIELDS if OPTIONAL_CONFIG[field] != PRIMARY_CONFIG[field]]
    assert len(optional_changed) == 1
    optional_run = run_experiment(OPTIONAL_CONFIG, case_train_indices, val_indices)
    print("Optional validation only:", optional_run["validation"]["accuracy"])
''',
    )
replace_cell(
    notebook,
    "d404-29",
    filled_dict(
        "defense",
        [
            "problem_and_consequence",
            "primary_diagnosis",
            "supporting_evidence",
            "disconfirming_or_threatening_evidence",
            "single_intervention",
            "observed_result",
            "mechanism_explanation",
            "efficiency_and_reproducibility",
            "test_statement",
            "next_experiment",
        ],
    ),
)
replace_cell(
    notebook,
    "d404-31",
    filled_dict(
        "reflection",
        ["strongest_alternative", "cheapest_discriminating_observation", "simulation_limit", "what_you_would_monitor"],
    ),
)

namespace = {"__name__": "__main__"}
captured = io.StringIO()
started = time.perf_counter()
test_denied_before_decision = False
test_authorized_after_decision = False
with contextlib.redirect_stdout(captured):
    for cell_number, cell in enumerate(notebook["cells"], 1):
        if cell["cell_type"] != "code":
            continue
        if cell["id"] == "d404-24":
            assert namespace["TEST_AUTHORIZED"] is False
            try:
                namespace["access_test_split"]()
            except PermissionError:
                test_denied_before_decision = True
            else:
                raise AssertionError("Test access unexpectedly succeeded before decision")
        exec(compile("".join(cell["source"]), f"completed-cell-{cell_number}", "exec"), namespace)
        if cell["id"] == "d404-24":
            test_authorized_after_decision = namespace["TEST_AUTHORIZED"] is True and len(namespace["y_test"]) == 360
        plt.close("all")
wall_seconds = time.perf_counter() - started

comparison = namespace["comparison"]
accuracy_delta = comparison["accuracy_delta"]
gap_reduction = comparison["gap_before"] - comparison["gap_after"]
val_loss_range_before = float(np.ptp(namespace["baseline"]["val_loss"]))
val_loss_range_after = float(np.ptp(namespace["primary_history"]["val_loss"]))
late_loss_reversals_before = int(np.sum(np.diff(namespace["baseline"]["val_loss"][-5:]) > 0.0))
late_loss_reversals_after = int(np.sum(np.diff(namespace["primary_history"]["val_loss"][-5:]) > 0.0))
target_pass = {
    "A": comparison["worst_recall_delta"] >= 0.05 and accuracy_delta >= -0.02,
    "B": gap_reduction >= 0.029 or accuracy_delta > 0.0,
    "C": accuracy_delta >= 0.05 and late_loss_reversals_after < late_loss_reversals_before,
}[PROFILE]
result = {
    "profile": PROFILE,
    "mode": "recovery" if RECOVERY else "live",
    "wall_seconds": wall_seconds,
    "checkpoint_seconds": time.perf_counter() - namespace["started_capstone"],
    "baseline_accuracy": namespace["baseline_summary"]["validation_accuracy"],
    "primary_accuracy": namespace["primary_validation"]["accuracy"],
    "primary_macro_f1": namespace["primary_validation"]["macro_f1"],
    "accuracy_delta": accuracy_delta,
    "worst_recall_delta": comparison["worst_recall_delta"],
    "gap_before": comparison["gap_before"],
    "gap_after": comparison["gap_after"],
    "gap_reduction": gap_reduction,
    "val_loss_range_before": val_loss_range_before,
    "val_loss_range_after": val_loss_range_after,
    "late_loss_reversals_before": late_loss_reversals_before,
    "late_loss_reversals_after": late_loss_reversals_after,
    "target_pass": bool(target_pass),
    "test_denied_before_decision": test_denied_before_decision,
    "test_authorized_after_decision": test_authorized_after_decision,
    "test_record": namespace["authorized_test_record"],
    "evidence_board_complete": all(namespace["evidence_board"].values()),
    "defense_fields": len(namespace["defense"]),
    "individual_transfer_present": "individual_transfer" in namespace["defense"],
    "recovery_used": namespace["recovery_used"],
    "optional_ran": "optional_run" in namespace,
}
assert result["target_pass"]
assert result["test_denied_before_decision"] and result["test_authorized_after_decision"]
assert result["evidence_board_complete"] and result["defense_fields"] == 10
assert not result["individual_transfer_present"]
assert result["wall_seconds"] < 720
if RECOVERY:
    assert result["recovery_used"] and result["test_record"]["status"].startswith("not available")
else:
    assert not result["recovery_used"] and result["optional_ran"]
    assert result["test_record"]["used_for_further_tuning"] is False
print(json.dumps(result, sort_keys=True))

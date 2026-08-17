import json
from pathlib import Path

path = Path("courseware/day-4/labs/LAB-D4-03-one-experiment.ipynb")
notebook = json.loads(path.read_text())
source = '''
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
    if len(changes) != 1:
        raise ValueError(f"Exactly one major change required; received {changes}")
    changed_field = changes[0]
    if proposed_config[changed_field] not in INTERVENTION_MENU[changed_field]:
        raise ValueError(f"{changed_field} must use one bounded menu value: {INTERVENTION_MENU[changed_field]}")
    if proposed_config["epochs"] > 20:
        raise ValueError("Epoch budget exceeds the bounded lab contract")
    json.dumps(proposed_config)
    return changed_field
'''.strip("\n").splitlines(keepends=True)

for cell in notebook["cells"]:
    if cell["id"] == "d403-09":
        cell["source"] = source
        break
else:
    raise KeyError("d403-09")

path.write_text(json.dumps(notebook, indent=1) + "\n")
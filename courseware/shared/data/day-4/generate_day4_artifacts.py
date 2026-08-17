"""Generate participant-safe, deterministic Day 4 evidence artifacts.

The generated files contain inputs, split indices, anonymous curves, predictions,
and cached baseline evidence. They contain no diagnoses, intervention answers,
trained checkpoints, test metrics, or completed participant responses.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import platform
import random
import time
import zipfile
from pathlib import Path

import numpy as np
import sklearn
import torch
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


SCHEMA_VERSION = 1
GENERATOR_VERSION = "day4-evidence-v1"
DATA_SEED = 4401
MODEL_SEED = 4402
BATCH_SEED = 4403
DEVICE = torch.device("cpu")
REFERENCE_MEASUREMENTS = {
    "experiment_baseline": {"training_seconds": 0.10, "latency_ms_median": 0.0105, "latency_ms_p90": 0.0140},
    "profile_A_baseline": {"training_seconds": 0.08, "latency_ms_median": 0.0105, "latency_ms_p90": 0.0140},
    "profile_B_baseline": {"training_seconds": 0.34, "latency_ms_median": 0.0210, "latency_ms_p90": 0.0280},
    "profile_C_baseline": {"training_seconds": 0.07, "latency_ms_median": 0.0110, "latency_ms_p90": 0.0150},
    "profile_A_recovery": {"training_seconds": 0.08, "latency_ms_median": 0.0105, "latency_ms_p90": 0.0140},
    "profile_B_recovery": {"training_seconds": 0.34, "latency_ms_median": 0.0260, "latency_ms_p90": 0.0350},
    "profile_C_recovery": {"training_seconds": 0.08, "latency_ms_median": 0.0105, "latency_ms_p90": 0.0140},
}
PROFILE_TARGETS = {
    "A": "Raise worst-class recall by at least 0.05 with no more than 0.02 overall validation-accuracy degradation.",
    "B": "Reduce the train/validation gap by about 0.03 or produce a defensible validation improvement.",
    "C": "Improve validation accuracy by at least 0.05 and make the optimization path more stable.",
}


def set_all_seeds(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def split_hash(train_indices: np.ndarray, val_indices: np.ndarray, test_indices: np.ndarray) -> str:
    digest = hashlib.sha256()
    for name, values in (
        ("train", train_indices),
        ("validation", val_indices),
        ("test", test_indices),
    ):
        digest.update(name.encode("ascii"))
        digest.update(np.asarray(values, dtype=np.int64).tobytes())
    return digest.hexdigest()


def save_npz(path: Path, **arrays: np.ndarray) -> dict:
    with zipfile.ZipFile(path, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(arrays):
            buffer = io.BytesIO()
            np.save(buffer, np.asarray(arrays[name]), allow_pickle=False)
            entry = zipfile.ZipInfo(f"{name}.npy", date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o600 << 16
            archive.writestr(entry, buffer.getvalue(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)}


def make_splits(labels: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    all_indices = np.arange(len(labels))
    train_indices, remainder_indices = train_test_split(
        all_indices,
        test_size=0.40,
        random_state=DATA_SEED,
        stratify=labels,
    )
    val_indices, test_indices = train_test_split(
        remainder_indices,
        test_size=0.50,
        random_state=DATA_SEED + 1,
        stratify=labels[remainder_indices],
    )
    return train_indices, val_indices, test_indices


def mystery_curves() -> dict[str, np.ndarray]:
    epochs = np.arange(1, 25, dtype=np.int64)
    phase = np.linspace(0.0, 1.0, len(epochs))
    return {
        "epochs": epochs,
        "bundle_ids": np.asarray(["M1", "M2", "M3", "M4"]),
        "train_loss": np.stack([
            1.85 * np.exp(-4.0 * phase) + 0.16,
            1.75 * np.exp(-1.0 * phase) + 0.72,
            2.05 * np.exp(-5.2 * phase) + 0.045,
            1.15 + 0.48 * np.sin(phase * 9.5 * np.pi) + 0.18 * phase,
        ]),
        "val_loss": np.stack([
            1.90 * np.exp(-3.5 * phase) + 0.23,
            1.78 * np.exp(-0.9 * phase) + 0.77,
            1.55 * np.exp(-4.0 * phase) + 0.27 + 1.08 * phase**2,
            1.25 + 0.52 * np.sin(phase * 9.5 * np.pi + 0.7) + 0.25 * phase,
        ]),
        "train_accuracy": np.stack([
            0.26 + 0.70 * (1.0 - np.exp(-4.2 * phase)),
            0.22 + 0.55 * (1.0 - np.exp(-1.2 * phase)),
            0.20 + 0.795 * (1.0 - np.exp(-5.0 * phase)),
            np.clip(0.54 + 0.22 * np.sin(phase * 9.5 * np.pi + 0.2), 0.18, 0.82),
        ]),
        "val_accuracy": np.stack([
            0.24 + 0.68 * (1.0 - np.exp(-3.8 * phase)),
            0.21 + 0.52 * (1.0 - np.exp(-1.1 * phase)),
            0.22 + 0.72 * (1.0 - np.exp(-4.2 * phase)) - 0.12 * phase**2,
            np.clip(0.49 + 0.24 * np.sin(phase * 9.5 * np.pi + 0.9), 0.15, 0.79),
        ]),
    }


def digit_metadata(images: np.ndarray) -> dict[str, np.ndarray]:
    normalized = images / 16.0
    rows = np.arange(8, dtype=np.float64).reshape(1, 8, 1)
    cols = np.arange(8, dtype=np.float64).reshape(1, 1, 8)
    mass = normalized.sum(axis=(1, 2)) + 1e-12
    center_row = (normalized * rows).sum(axis=(1, 2)) / mass
    center_col = (normalized * cols).sum(axis=(1, 2)) / mass
    border = np.zeros((8, 8), dtype=bool)
    border[[0, -1], :] = True
    border[:, [0, -1]] = True
    return {
        "ink_total": mass.astype(np.float32),
        "center_row": center_row.astype(np.float32),
        "center_col": center_col.astype(np.float32),
        "border_ink": normalized[:, border].sum(axis=1).astype(np.float32),
        "active_pixels": (images >= 6).sum(axis=(1, 2)).astype(np.int64),
    }


def generate_detective_artifact(
    output_dir: Path,
    images: np.ndarray,
    labels: np.ndarray,
    train_indices: np.ndarray,
    val_indices: np.ndarray,
) -> tuple[dict, dict]:
    scaler = StandardScaler()
    X_train = scaler.fit_transform(images[train_indices].reshape(len(train_indices), -1))
    X_val = scaler.transform(images[val_indices].reshape(len(val_indices), -1))
    model = LogisticRegression(C=0.12, max_iter=2000, random_state=MODEL_SEED)
    model.fit(X_train, labels[train_indices])
    probabilities = model.predict_proba(X_val)
    predictions = probabilities.argmax(axis=1)
    confidence = probabilities.max(axis=1)
    metadata = digit_metadata(images[val_indices])
    path = output_dir / "digits_evidence.npz"
    artifact = save_npz(
        path,
        sample_ids=val_indices.astype(np.int64),
        images=images[val_indices].astype(np.float32),
        labels=labels[val_indices].astype(np.int64),
        probabilities=probabilities.astype(np.float32),
        predictions=predictions.astype(np.int64),
        confidence=confidence.astype(np.float32),
        **metadata,
    )
    metrics = {
        "validation_accuracy": float(accuracy_score(labels[val_indices], predictions)),
        "confusion_shape": list(confusion_matrix(labels[val_indices], predictions, labels=np.arange(10)).shape),
        "high_confidence_error_count": int(np.sum((predictions != labels[val_indices]) & (confidence >= 0.70))),
    }
    return artifact, metrics


class DigitsMLP(nn.Module):
    def __init__(self, hidden: tuple[int, ...], dropout: float = 0.0):
        super().__init__()
        layers: list[nn.Module] = [nn.Flatten()]
        input_dim = 64
        for width in hidden:
            layers.extend([nn.Linear(input_dim, width), nn.ReLU()])
            if dropout > 0.0:
                layers.append(nn.Dropout(dropout))
            input_dim = width
        layers.append(nn.Linear(input_dim, 10))
        self.network = nn.Sequential(*layers)

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        return self.network(inputs)


def evaluate(model: nn.Module, X: torch.Tensor, y: torch.Tensor) -> dict:
    model.eval()
    with torch.inference_mode():
        logits = model(X)
        probabilities = torch.softmax(logits, dim=1).cpu().numpy()
    predictions = probabilities.argmax(axis=1)
    targets = y.cpu().numpy()
    return {
        "loss": float(nn.CrossEntropyLoss()(logits, y).item()),
        "accuracy": float(accuracy_score(targets, predictions)),
        "macro_f1": float(f1_score(targets, predictions, average="macro", zero_division=0)),
        "probabilities": probabilities,
        "predictions": predictions,
    }


def train_run(
    X: np.ndarray,
    y: np.ndarray,
    train_indices: np.ndarray,
    val_indices: np.ndarray,
    *,
    hidden: tuple[int, ...],
    dropout: float,
    optimizer_name: str,
    learning_rate: float,
    weight_decay: float,
    epochs: int,
    batch_size: int,
    seed: int,
    class_weight: bool = False,
) -> tuple[nn.Module, dict]:
    set_all_seeds(seed)
    X_tensor = torch.tensor(X / 16.0, dtype=torch.float32, device=DEVICE)
    y_tensor = torch.tensor(y, dtype=torch.long, device=DEVICE)
    model = DigitsMLP(hidden, dropout).to(DEVICE)
    if optimizer_name == "adam":
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
    elif optimizer_name == "adamw":
        optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
    elif optimizer_name == "sgd":
        optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9, weight_decay=weight_decay)
    else:
        raise ValueError(f"Unsupported optimizer: {optimizer_name}")

    selected_targets = y[train_indices]
    if class_weight:
        counts = np.bincount(selected_targets, minlength=10)
        weights = len(selected_targets) / (10 * np.maximum(counts, 1))
        loss_fn = nn.CrossEntropyLoss(weight=torch.tensor(weights, dtype=torch.float32, device=DEVICE))
    else:
        loss_fn = nn.CrossEntropyLoss()

    generator = torch.Generator().manual_seed(BATCH_SEED + seed)
    loader = DataLoader(
        TensorDataset(X_tensor[train_indices], y_tensor[train_indices]),
        batch_size=batch_size,
        shuffle=True,
        generator=generator,
        num_workers=0,
    )
    history = {name: [] for name in ("train_loss", "val_loss", "train_accuracy", "val_accuracy")}
    started = time.perf_counter()
    for _ in range(epochs):
        model.train()
        for X_batch, y_batch in loader:
            optimizer.zero_grad()
            loss = loss_fn(model(X_batch), y_batch)
            loss.backward()
            optimizer.step()
        train_metrics = evaluate(model, X_tensor[train_indices], y_tensor[train_indices])
        val_metrics = evaluate(model, X_tensor[val_indices], y_tensor[val_indices])
        history["train_loss"].append(train_metrics["loss"])
        history["val_loss"].append(val_metrics["loss"])
        history["train_accuracy"].append(train_metrics["accuracy"])
        history["val_accuracy"].append(val_metrics["accuracy"])
    elapsed = time.perf_counter() - started
    final_train = evaluate(model, X_tensor[train_indices], y_tensor[train_indices])
    final_val = evaluate(model, X_tensor[val_indices], y_tensor[val_indices])
    result = {
        "history": {name: np.asarray(values, dtype=np.float32) for name, values in history.items()},
        "train": final_train,
        "validation": final_val,
        "training_seconds": elapsed,
        "parameter_count": sum(parameter.numel() for parameter in model.parameters()),
        "parameter_bytes": sum(parameter.numel() * parameter.element_size() for parameter in model.parameters()),
    }
    return model, result


def benchmark_batch1(model: nn.Module, X: np.ndarray, warmup: int = 20, repeats: int = 100) -> dict:
    model.eval()
    sample = torch.tensor(X[:1] / 16.0, dtype=torch.float32, device=DEVICE)
    with torch.inference_mode():
        for _ in range(warmup):
            model(sample)
        timings = []
        for _ in range(repeats):
            started = time.perf_counter()
            model(sample)
            timings.append((time.perf_counter() - started) * 1000.0)
    return {
        "latency_ms_median": float(np.median(timings)),
        "latency_ms_p90": float(np.percentile(timings, 90)),
        "warmup": warmup,
        "repeats": repeats,
    }


def save_run_artifact(
    path: Path,
    result: dict,
    labels: np.ndarray,
    val_indices: np.ndarray,
    train_indices: np.ndarray,
    benchmark: dict,
    additional_arrays: dict[str, np.ndarray] | None = None,
) -> tuple[dict, dict]:
    targets = labels[val_indices]
    predictions = result["validation"]["predictions"]
    confusion = confusion_matrix(targets, predictions, labels=np.arange(10))
    recall = np.diag(confusion) / np.maximum(confusion.sum(axis=1), 1)
    artifact = save_npz(
        path,
        epochs=np.arange(1, len(result["history"]["train_loss"]) + 1, dtype=np.int64),
        train_loss=result["history"]["train_loss"],
        val_loss=result["history"]["val_loss"],
        train_accuracy=result["history"]["train_accuracy"],
        val_accuracy=result["history"]["val_accuracy"],
        val_sample_ids=val_indices.astype(np.int64),
        val_labels=targets.astype(np.int64),
        val_probabilities=result["validation"]["probabilities"].astype(np.float32),
        val_predictions=predictions.astype(np.int64),
        confusion=confusion.astype(np.int64),
        class_recall=recall.astype(np.float32),
        train_class_counts=np.bincount(labels[train_indices], minlength=10).astype(np.int64),
        training_seconds=np.asarray(result["training_seconds"], dtype=np.float64),
        parameter_count=np.asarray(result["parameter_count"], dtype=np.int64),
        parameter_bytes=np.asarray(result["parameter_bytes"], dtype=np.int64),
        latency_ms_median=np.asarray(benchmark["latency_ms_median"], dtype=np.float64),
        latency_ms_p90=np.asarray(benchmark["latency_ms_p90"], dtype=np.float64),
        latency_warmup=np.asarray(benchmark["warmup"], dtype=np.int64),
        latency_repeats=np.asarray(benchmark["repeats"], dtype=np.int64),
        **(additional_arrays or {}),
    )
    metrics = {
        "train_accuracy": result["train"]["accuracy"],
        "validation_accuracy": result["validation"]["accuracy"],
        "validation_macro_f1": result["validation"]["macro_f1"],
        "worst_class_recall": float(recall.min()),
        "parameter_bytes": result["parameter_bytes"],
        "latency_ms_median": benchmark["latency_ms_median"],
        "training_seconds": result["training_seconds"],
    }
    return artifact, metrics


def config_fingerprint(config: dict) -> str:
    return hashlib.sha256(json.dumps(config, sort_keys=True).encode("utf-8")).hexdigest()


def class_limited_indices(labels: np.ndarray, base_indices: np.ndarray, limits: dict[int, int], seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    selected = []
    for class_id in range(10):
        class_indices = base_indices[labels[base_indices] == class_id]
        selected.append(rng.permutation(class_indices)[: limits.get(class_id, len(class_indices))])
    combined = np.concatenate(selected)
    return combined[rng.permutation(len(combined))]


def generate_training_artifacts(
    output_dir: Path,
    X: np.ndarray,
    y: np.ndarray,
    train_indices: np.ndarray,
    val_indices: np.ndarray,
) -> tuple[dict, dict]:
    run_specs = {
        "experiment_baseline": {
            "train_indices": train_indices,
            "hidden": (32,), "dropout": 0.0, "optimizer_name": "adam",
            "learning_rate": 0.003, "weight_decay": 0.0, "epochs": 7,
            "batch_size": 64, "seed": MODEL_SEED,
        },
        "profile_A_baseline": {
            "train_indices": class_limited_indices(y, train_indices, {8: 24, 9: 32}, DATA_SEED + 10),
            "hidden": (32,), "dropout": 0.0, "optimizer_name": "adam",
            "learning_rate": 0.003, "weight_decay": 0.0, "epochs": 10,
            "batch_size": 64, "seed": MODEL_SEED + 10,
        },
        "profile_B_baseline": {
            "train_indices": class_limited_indices(y, train_indices, {class_id: 10 for class_id in range(10)}, DATA_SEED + 20),
            "hidden": (256, 128), "dropout": 0.0, "optimizer_name": "adam",
            "learning_rate": 0.003, "weight_decay": 0.0, "epochs": 70,
            "batch_size": 32, "seed": MODEL_SEED + 20,
        },
        "profile_C_baseline": {
            "train_indices": train_indices,
            "hidden": (32,), "dropout": 0.0, "optimizer_name": "adam",
            "learning_rate": 0.20, "weight_decay": 0.0, "epochs": 8,
            "batch_size": 64, "seed": MODEL_SEED + 30,
        },
    }
    artifacts, metrics = {}, {}
    for name, specification in run_specs.items():
        specification = dict(specification)
        selected_indices = specification.pop("train_indices")
        model, result = train_run(X, y, selected_indices, val_indices, **specification)
        benchmark = benchmark_batch1(model, X[val_indices])
        result["training_seconds"] = REFERENCE_MEASUREMENTS[name]["training_seconds"]
        benchmark.update(REFERENCE_MEASUREMENTS[name])
        additional_arrays = None
        if name.startswith("profile_"):
            profile_id = name.split("_", maxsplit=2)[1]
            baseline_config = {**specification, "class_weight": False}
            additional_arrays = {
                "case_train_indices": selected_indices.astype(np.int64),
                "baseline_config_json": np.asarray(json.dumps(baseline_config, sort_keys=True)),
                "case_target": np.asarray(PROFILE_TARGETS[profile_id]),
            }
        artifact, run_metrics = save_run_artifact(
            output_dir / f"{name}.npz",
            result,
            y,
            val_indices,
            selected_indices,
            benchmark,
            additional_arrays,
        )
        artifacts[name] = artifact
        metrics[name] = run_metrics

    recovery_specs = {
        "profile_A_recovery": {
            "profile": "A",
            "train_indices": run_specs["profile_A_baseline"]["train_indices"],
            "config": {
                "hidden": (32,), "dropout": 0.0, "optimizer_name": "adam",
                "learning_rate": 0.003, "weight_decay": 0.0, "epochs": 10,
                "batch_size": 64, "seed": MODEL_SEED + 10, "class_weight": True,
            },
        },
        "profile_B_recovery": {
            "profile": "B",
            "train_indices": run_specs["profile_B_baseline"]["train_indices"],
            "config": {
                "hidden": (256, 128), "dropout": 0.5, "optimizer_name": "adam",
                "learning_rate": 0.003, "weight_decay": 0.0, "epochs": 70,
                "batch_size": 32, "seed": MODEL_SEED + 20, "class_weight": False,
            },
        },
        "profile_C_recovery": {
            "profile": "C",
            "train_indices": run_specs["profile_C_baseline"]["train_indices"],
            "config": {
                "hidden": (32,), "dropout": 0.0, "optimizer_name": "adam",
                "learning_rate": 0.003, "weight_decay": 0.0, "epochs": 8,
                "batch_size": 64, "seed": MODEL_SEED + 30, "class_weight": False,
            },
        },
    }
    for name, specification in recovery_specs.items():
        model, result = train_run(
            X,
            y,
            specification["train_indices"],
            val_indices,
            **specification["config"],
        )
        benchmark = benchmark_batch1(model, X[val_indices])
        result["training_seconds"] = REFERENCE_MEASUREMENTS[name]["training_seconds"]
        benchmark.update(REFERENCE_MEASUREMENTS[name])
        artifact, run_metrics = save_run_artifact(
            output_dir / f"{name}.npz",
            result,
            y,
            val_indices,
            specification["train_indices"],
            benchmark,
        )
        artifact["selection_fingerprint"] = config_fingerprint(specification["config"])
        artifacts[name] = artifact
        metrics[name] = run_metrics
    return artifacts, metrics


def main(output_dir: Path | None = None) -> None:
    output_dir = output_dir or Path(__file__).resolve().parent
    output_dir.mkdir(parents=True, exist_ok=True)
    torch.set_num_threads(1)
    set_all_seeds(MODEL_SEED)
    digits = load_digits()
    images = digits.images.astype(np.float32)
    labels = digits.target.astype(np.int64)
    train_indices, val_indices, test_indices = make_splits(labels)
    fixed_split_hash = split_hash(train_indices, val_indices, test_indices)

    artifacts = {}
    artifacts["fixed_splits"] = save_npz(
        output_dir / "digits_fixed_splits.npz",
        train_indices=train_indices.astype(np.int64),
        val_indices=val_indices.astype(np.int64),
        test_indices=test_indices.astype(np.int64),
        split_hash=np.asarray(fixed_split_hash),
        data_seed=np.asarray(DATA_SEED, dtype=np.int64),
    )
    artifacts["mystery_curves"] = save_npz(output_dir / "mystery_curves.npz", **mystery_curves())
    detective_artifact, detective_metrics = generate_detective_artifact(
        output_dir, images, labels, train_indices, val_indices
    )
    artifacts["digits_evidence"] = detective_artifact
    training_artifacts, training_metrics = generate_training_artifacts(
        output_dir, images, labels, train_indices, val_indices
    )
    artifacts.update(training_artifacts)

    assert 0.90 <= detective_metrics["validation_accuracy"] <= 0.96
    assert detective_metrics["confusion_shape"] == [10, 10]
    assert detective_metrics["high_confidence_error_count"] >= 1
    assert 0.88 <= training_metrics["experiment_baseline"]["validation_accuracy"] <= 0.94
    assert 0.72 <= training_metrics["profile_A_baseline"]["validation_macro_f1"] <= 0.84
    assert training_metrics["profile_A_baseline"]["worst_class_recall"] < 0.55
    assert training_metrics["profile_B_baseline"]["train_accuracy"] > 0.98
    assert 0.82 <= training_metrics["profile_B_baseline"]["validation_accuracy"] <= 0.90
    assert 0.65 <= training_metrics["profile_C_baseline"]["validation_accuracy"] <= 0.85
    assert (
        training_metrics["profile_A_recovery"]["worst_class_recall"]
        - training_metrics["profile_A_baseline"]["worst_class_recall"]
    ) >= 0.05
    assert (
        training_metrics["profile_A_recovery"]["validation_accuracy"]
        - training_metrics["profile_A_baseline"]["validation_accuracy"]
    ) >= -0.02
    assert (
        (training_metrics["profile_B_baseline"]["train_accuracy"] - training_metrics["profile_B_baseline"]["validation_accuracy"])
        - (training_metrics["profile_B_recovery"]["train_accuracy"] - training_metrics["profile_B_recovery"]["validation_accuracy"])
    ) >= 0.03
    assert (
        training_metrics["profile_C_recovery"]["validation_accuracy"]
        - training_metrics["profile_C_baseline"]["validation_accuracy"]
    ) >= 0.05

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "generator_version": GENERATOR_VERSION,
        "generator": Path(__file__).name,
        "generated_utc": "2026-08-17T00:00:00Z",
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scikit_learn": sklearn.__version__,
            "torch": torch.__version__,
            "device": str(DEVICE),
        },
        "seeds": {"data": DATA_SEED, "model": MODEL_SEED, "batch": BATCH_SEED},
        "source": {
            "dataset": "scikit-learn load_digits bundled dataset",
            "api": "sklearn.datasets.load_digits",
            "description": "8x8 handwritten digit images framed in the labs as routing-code recognition",
            "network_required": False,
        },
        "fixed_split": {
            "counts": {"train": len(train_indices), "validation": len(val_indices), "test": len(test_indices)},
            "stratified": True,
            "hash": fixed_split_hash,
            "test_policy": "Indices are packaged for reproducibility; participant notebooks bind test arrays only after their decision gate.",
        },
        "artifacts": artifacts,
        "calibration": {
            "digits_evidence": detective_metrics,
            "experiment_baseline": training_metrics["experiment_baseline"],
        },
        "generation_runtime_note": (
            "Artifact timing fields are fixed reference measurements from the recorded 2026-08-17 CPU validation. "
            "Live invocation timing is intentionally excluded so regenerating identical evidence does not change checksums."
        ),
        "participant_safety": (
            "Contains fixed indices, images/labels, anonymous curves, validation probabilities, selected-case contracts, "
            "and cached baseline evidence only. Generic contract keys provide the selected target, baseline configuration, "
            "and train-index identity without construction rules. No diagnosis labels, case key, recommended intervention, "
            "trained checkpoint, completed response, cross-profile calibration summary, or test metric is included."
        ),
        "reproducibility_note": (
            "Seeds and a fixed CPU harness support repeatability on the recorded stack; they do not promise bitwise equality "
            "across devices, releases, BLAS implementations, or hardware."
        ),
    }
    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest["calibration"], indent=2))
    print(f"Wrote {manifest_path} and {len(artifacts)} participant-safe artifacts.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    main(args.output_dir)
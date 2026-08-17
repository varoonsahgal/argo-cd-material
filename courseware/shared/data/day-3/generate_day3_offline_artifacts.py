"""Generate participant-safe Day 3 offline data and embedding artifacts.

Downloads are opt-in. Run from the repository root with ``--download`` when
preparing a release; participant notebooks never invoke this script.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import random
import time
from pathlib import Path

import numpy as np
import torch
import torchvision
from PIL import Image
from torch import nn
from torch.utils.data import DataLoader, Dataset
from torchvision.datasets import CIFAR10, FashionMNIST
from torchvision.models import MobileNet_V3_Small_Weights, mobilenet_v3_small


SEED = 31415
FASHION_COUNTS = {"train": 3000, "validation": 800, "test": 800}
CIFAR_COUNTS = {"train": 2400, "validation": 800, "test": 800}


def set_all_seeds(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def balanced_indices(labels: np.ndarray, count: int, seed: int) -> np.ndarray:
    classes = np.unique(labels)
    if count % len(classes) != 0:
        raise ValueError(f"count={count} is not divisible by {len(classes)} classes")
    rng = np.random.default_rng(seed)
    per_class = count // len(classes)
    selected = []
    for class_id in classes:
        class_indices = np.flatnonzero(labels == class_id)
        selected.append(rng.choice(class_indices, size=per_class, replace=False))
    combined = np.concatenate(selected)
    return combined[rng.permutation(len(combined))]


def disjoint_balanced_indices(
    labels: np.ndarray,
    first_count: int,
    second_count: int,
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    classes = np.unique(labels)
    if first_count % len(classes) or second_count % len(classes):
        raise ValueError("split counts must be divisible by the class count")
    rng = np.random.default_rng(seed)
    first_per_class = first_count // len(classes)
    second_per_class = second_count // len(classes)
    first, second = [], []
    for class_id in classes:
        class_indices = rng.permutation(np.flatnonzero(labels == class_id))
        first.append(class_indices[:first_per_class])
        second.append(class_indices[first_per_class:first_per_class + second_per_class])
    first_indices = np.concatenate(first)
    second_indices = np.concatenate(second)
    return (
        first_indices[rng.permutation(len(first_indices))],
        second_indices[rng.permutation(len(second_indices))],
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def save_fashion_fallback(raw_root: Path, output_dir: Path, download: bool) -> dict:
    train_dataset = FashionMNIST(raw_root, train=True, download=download)
    test_dataset = FashionMNIST(raw_root, train=False, download=download)
    train_images = train_dataset.data.numpy()
    train_labels = train_dataset.targets.numpy()
    test_images = test_dataset.data.numpy()
    test_labels = test_dataset.targets.numpy()

    train_indices, val_indices = disjoint_balanced_indices(
        train_labels,
        FASHION_COUNTS["train"],
        FASHION_COUNTS["validation"],
        SEED,
    )
    test_indices = balanced_indices(test_labels, FASHION_COUNTS["test"], SEED + 1)
    output_path = output_dir / "fashion_mnist_fallback.npz"
    np.savez_compressed(
        output_path,
        train_images=train_images[train_indices].astype(np.uint8),
        train_labels=train_labels[train_indices].astype(np.int64),
        val_images=train_images[val_indices].astype(np.uint8),
        val_labels=train_labels[val_indices].astype(np.int64),
        test_images=test_images[test_indices].astype(np.uint8),
        test_labels=test_labels[test_indices].astype(np.int64),
        class_names=np.asarray(train_dataset.classes),
        seed=np.asarray(SEED),
    )
    return {
        "path": output_path.name,
        "bytes": output_path.stat().st_size,
        "sha256": sha256(output_path),
        "counts": FASHION_COUNTS,
        "source": "Fashion-MNIST via torchvision.datasets.FashionMNIST",
        "source_url": "https://github.com/zalandoresearch/fashion-mnist",
        "license": "MIT (Fashion-MNIST repository)",
        "generation": "Balanced subset sampled without replacement from official train/test files.",
        "fallback_scope": [
            "image tensor and channel shapes",
            "bounded CNN training/evaluation",
            "feature-map capture and hook cleanup",
            "misclassification inspection",
            "tiny-data overfitting and one-remedy comparison",
        ],
        "not_validated_by_fallback": [
            "the 10k/2k/2k online split metric band",
            "full Fashion-MNIST training throughput",
        ],
    }


class ImageArrayDataset(Dataset):
    def __init__(self, images: np.ndarray, transform):
        self.images = images
        self.transform = transform

    def __len__(self) -> int:
        return len(self.images)

    def __getitem__(self, index: int) -> torch.Tensor:
        return self.transform(Image.fromarray(self.images[index]))


def extract_embeddings(
    model: nn.Module,
    images: np.ndarray,
    transform,
    batch_size: int,
) -> tuple[np.ndarray, float]:
    loader = DataLoader(
        ImageArrayDataset(images, transform),
        batch_size=batch_size,
        shuffle=False,
        num_workers=0,
    )
    batches = []
    started = time.perf_counter()
    model.eval()
    with torch.inference_mode():
        for image_batch in loader:
            batches.append(model(image_batch).cpu().numpy().astype(np.float16))
    return np.concatenate(batches), time.perf_counter() - started


def save_cifar_transfer_fallback(
    raw_root: Path,
    output_dir: Path,
    download: bool,
    batch_size: int,
) -> dict:
    train_dataset = CIFAR10(raw_root, train=True, download=download)
    test_dataset = CIFAR10(raw_root, train=False, download=download)
    train_images = np.asarray(train_dataset.data)
    train_labels = np.asarray(train_dataset.targets, dtype=np.int64)
    test_images = np.asarray(test_dataset.data)
    test_labels = np.asarray(test_dataset.targets, dtype=np.int64)

    train_indices, val_indices = disjoint_balanced_indices(
        train_labels,
        CIFAR_COUNTS["train"],
        CIFAR_COUNTS["validation"],
        SEED + 2,
    )
    test_indices = balanced_indices(test_labels, CIFAR_COUNTS["test"], SEED + 3)
    split_images = {
        "train": train_images[train_indices],
        "validation": train_images[val_indices],
        "test": test_images[test_indices],
    }
    split_labels = {
        "train": train_labels[train_indices],
        "validation": train_labels[val_indices],
        "test": test_labels[test_indices],
    }

    subset_path = output_dir / "cifar10_transfer_subset.npz"
    np.savez_compressed(
        subset_path,
        train_images=split_images["train"].astype(np.uint8),
        train_labels=split_labels["train"],
        val_images=split_images["validation"].astype(np.uint8),
        val_labels=split_labels["validation"],
        test_images=split_images["test"].astype(np.uint8),
        test_labels=split_labels["test"],
        class_names=np.asarray(train_dataset.classes),
        seed=np.asarray(SEED),
    )

    weights = MobileNet_V3_Small_Weights.DEFAULT
    transform = weights.transforms()
    set_all_seeds(SEED)
    backbone = mobilenet_v3_small(weights=weights)
    backbone.classifier = nn.Identity()

    embeddings, timings = {}, {}
    for split_name, images in split_images.items():
        embeddings[split_name], timings[split_name] = extract_embeddings(
            backbone,
            images,
            transform,
            batch_size,
        )
    embedding_path = output_dir / "cifar10_mobilenet_v3_small_embeddings.npz"
    np.savez_compressed(
        embedding_path,
        train_embeddings=embeddings["train"],
        train_labels=split_labels["train"],
        val_embeddings=embeddings["validation"],
        val_labels=split_labels["validation"],
        test_embeddings=embeddings["test"],
        test_labels=split_labels["test"],
        class_names=np.asarray(train_dataset.classes),
        seed=np.asarray(SEED),
    )

    split_hash = hashlib.sha256(
        np.concatenate([train_indices, val_indices, test_indices]).astype(np.int64).tobytes()
    ).hexdigest()
    cache_key_source = json.dumps(
        {
            "weights": "MobileNet_V3_Small_Weights.DEFAULT",
            "resolved_weights": str(weights),
            "transforms": repr(transform),
            "split_seed": SEED,
            "split_hash": split_hash,
            "counts": CIFAR_COUNTS,
        },
        sort_keys=True,
    )
    return {
        "subset": {
            "path": subset_path.name,
            "bytes": subset_path.stat().st_size,
            "sha256": sha256(subset_path),
        },
        "embeddings": {
            "path": embedding_path.name,
            "bytes": embedding_path.stat().st_size,
            "sha256": sha256(embedding_path),
            "shape": {name: list(value.shape) for name, value in embeddings.items()},
            "dtype": "float16 (converted to float32 by participant notebook)",
        },
        "counts": CIFAR_COUNTS,
        "source": "CIFAR-10 via torchvision.datasets.CIFAR10",
        "source_url": "https://www.cs.toronto.edu/~kriz/cifar.html",
        "license": "The upstream CIFAR-10 source page does not state a separate license; verify redistribution terms before external release.",
        "weights": "MobileNet_V3_Small_Weights.DEFAULT",
        "resolved_weights": str(weights),
        "weight_source": "torchvision MobileNet V3 Small pretrained weights",
        "weight_terms": "Torchvision is BSD-3-Clause; upstream pretrained-data/weight terms should be checked for the release destination.",
        "transforms": repr(transform),
        "split_hash": split_hash,
        "cache_key": hashlib.sha256(cache_key_source.encode("utf-8")).hexdigest(),
        "extraction_seconds": timings,
        "fallback_scope": [
            "scratch-CNN training on the fixed 2400/800/800 split",
            "frozen-embedding head training and evaluation",
            "trainable-versus-total parameter reasoning",
            "quality/time/sample-count scoreboard construction",
        ],
        "not_validated_by_fallback": [
            "a fresh pretrained-weight download",
            "participant-side MobileNet feature extraction",
            "the wrong-normalization extraction diagnostic",
            "feature-extraction time on the participant machine",
        ],
    }


def surrogate_features(images: np.ndarray, seed: int) -> np.ndarray:
    """Create label-blind recovery features from 28x28 grayscale images."""
    values = images.astype(np.float32) / 255.0
    pooled = values.reshape(len(values), 7, 4, 7, 4).mean(axis=(2, 4))
    horizontal = np.diff(values, axis=2, append=values[:, :, -1:])
    vertical = np.diff(values, axis=1, append=values[:, -1:, :])
    horizontal_pooled = horizontal.reshape(len(values), 7, 4, 7, 4).mean(axis=(2, 4))
    vertical_pooled = vertical.reshape(len(values), 7, 4, 7, 4).mean(axis=(2, 4))
    base_features = np.concatenate(
        [
            pooled.reshape(len(values), -1),
            horizontal_pooled.reshape(len(values), -1),
            vertical_pooled.reshape(len(values), -1),
        ],
        axis=1,
    )
    rng = np.random.default_rng(seed)
    projection = rng.normal(
        0.0,
        1.0 / np.sqrt(base_features.shape[1]),
        size=(base_features.shape[1], 256),
    ).astype(np.float32)
    return np.tanh(base_features @ projection).astype(np.float16)


def save_surrogate_transfer_fallback(output_dir: Path) -> dict:
    fashion_path = output_dir / "fashion_mnist_fallback.npz"
    if not fashion_path.exists():
        raise FileNotFoundError(
            "Generate fashion_mnist_fallback.npz before the no-network transfer surrogate."
        )
    source = np.load(fashion_path, allow_pickle=False)
    train_indices = balanced_indices(source["train_labels"], CIFAR_COUNTS["train"], SEED + 4)
    split_images = {
        "train": source["train_images"][train_indices],
        "validation": source["val_images"],
        "test": source["test_images"],
    }
    split_labels = {
        "train": source["train_labels"][train_indices],
        "validation": source["val_labels"],
        "test": source["test_labels"],
    }
    subset_path = output_dir / "transfer_surrogate_fashion_subset.npz"
    np.savez_compressed(
        subset_path,
        train_images=split_images["train"],
        train_labels=split_labels["train"],
        val_images=split_images["validation"],
        val_labels=split_labels["validation"],
        test_images=split_images["test"],
        test_labels=split_labels["test"],
        class_names=source["class_names"],
        seed=np.asarray(SEED),
    )
    embeddings = {
        split_name: surrogate_features(images, SEED + 5)
        for split_name, images in split_images.items()
    }
    embedding_path = output_dir / "transfer_surrogate_embeddings.npz"
    np.savez_compressed(
        embedding_path,
        train_embeddings=embeddings["train"],
        train_labels=split_labels["train"],
        val_embeddings=embeddings["validation"],
        val_labels=split_labels["validation"],
        test_embeddings=embeddings["test"],
        test_labels=split_labels["test"],
        class_names=source["class_names"],
        seed=np.asarray(SEED),
    )
    split_hash = hashlib.sha256(
        b"".join(split_labels[name].astype(np.int64).tobytes() for name in split_labels)
    ).hexdigest()
    cache_description = {
        "feature_extractor": "label-blind 4x4 mean/gradient pooling plus seeded random projection and tanh",
        "transform": "uint8 / 255; no augmentation",
        "split_seed": SEED,
        "split_hash": split_hash,
        "counts": CIFAR_COUNTS,
    }
    return {
        "mode": "course-supplied recovery surrogate; not CIFAR-10 or MobileNet features",
        "subset": {
            "path": subset_path.name,
            "bytes": subset_path.stat().st_size,
            "sha256": sha256(subset_path),
        },
        "embeddings": {
            "path": embedding_path.name,
            "bytes": embedding_path.stat().st_size,
            "sha256": sha256(embedding_path),
            "shape": {name: list(value.shape) for name, value in embeddings.items()},
            "dtype": "float16 (converted to float32 by participant notebook)",
        },
        "counts": CIFAR_COUNTS,
        "source": "The packaged balanced Fashion-MNIST recovery subset",
        "source_artifact": fashion_path.name,
        "source_artifact_sha256": sha256(fashion_path),
        "license": "MIT (Fashion-MNIST repository)",
        "generation": cache_description,
        "cache_key": hashlib.sha256(
            json.dumps(cache_description, sort_keys=True).encode("utf-8")
        ).hexdigest(),
        "fallback_scope": [
            "fixed-split image loading and bounded scratch-model training",
            "precomputed-feature loading without labels embedded in features",
            "new classifier-head training and evaluation",
            "trainable-versus-total parameter reasoning",
            "quality/time/sample-count scoreboard construction",
        ],
        "not_validated_by_fallback": [
            "CIFAR-10 class behavior or metric bands",
            "MobileNet V3 Small weights, transforms, gradients, or extraction",
            "a transfer-learning advantage over scratch training",
            "online download/cache behavior or participant-machine extraction time",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true", help="Allow torchvision dataset and weight downloads.")
    parser.add_argument("--raw-root", type=Path, default=Path(".cache/day-3-source-data"))
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--skip-fashion", action="store_true")
    parser.add_argument("--skip-transfer", action="store_true")
    parser.add_argument(
        "--surrogate-transfer",
        action="store_true",
        help="Build a clearly labeled no-network recovery cache instead of CIFAR/MobileNet embeddings.",
    )
    args = parser.parse_args()

    if not args.download and not args.surrogate_transfer and not args.skip_transfer:
        parser.error(
            "canonical CIFAR/MobileNet generation requires --download; "
            "use --surrogate-transfer for the no-network recovery package "
            "or --skip-transfer to generate only Fashion-MNIST artifacts"
        )

    args.raw_root.mkdir(parents=True, exist_ok=True)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    set_all_seeds(SEED)
    artifacts = {}
    started = time.perf_counter()
    if not args.skip_fashion:
        artifacts["fashion_mnist_fallback"] = save_fashion_fallback(
            args.raw_root,
            args.output_dir,
            args.download,
        )
    if not args.skip_transfer:
        if args.surrogate_transfer:
            artifacts["transfer_recovery_surrogate"] = save_surrogate_transfer_fallback(
                args.output_dir
            )
        else:
            artifacts["cifar10_transfer_fallback"] = save_cifar_transfer_fallback(
                args.raw_root,
                args.output_dir,
                args.download,
                args.batch_size,
            )

    manifest = {
        "schema_version": 1,
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "generator": Path(__file__).name,
        "seed": SEED,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "torch": torch.__version__,
            "torchvision": torchvision.__version__,
            "device": "cpu",
        },
        "generation_seconds": time.perf_counter() - started,
        "artifacts": artifacts,
        "participant_safety": "Contains images, class labels, and frozen feature vectors only. No trained task head, predictions, answer key, hidden diagnosis, or completed learner model is included.",
    }
    manifest_path = args.output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
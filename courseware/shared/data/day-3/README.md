# Day 3 Participant-Safe Offline Support

These files make the four Day 3 participant notebooks runnable after a repository checkout without network access. `manifest.json` is the machine-readable provenance and checksum record.

## Artifacts

| File | Bytes | SHA-256 | Contents |
|---|---:|---|---|
| `fashion_mnist_fallback.npz` | 2,024,650 | `c3fd6c0581b5baf626dfd59e735ac6f787a858a488db4afd09d2e0cbd4294122` | Balanced Fashion-MNIST `3,000/800/800` image/label splits |
| `transfer_surrogate_fashion_subset.npz` | 1,761,595 | `605aa62f6b4260203c6d205dac3fac432c434818e77316cc2f254ee84e85c9db` | Balanced `2,400/800/800` recovery images/labels |
| `transfer_surrogate_embeddings.npz` | 1,901,816 | `39fd63a657d0a2ecdc2e88c4a512aaea9f55e5af86c424908e7d5250934e6c5a` | Label-blind 256-wide recovery features for the same rows |

## Provenance and Generation

- Source images: official Fashion-MNIST files loaded with `torchvision.datasets.FashionMNIST`.
- Upstream source: <https://github.com/zalandoresearch/fashion-mnist>.
- Upstream license: MIT as stated by the Fashion-MNIST repository.
- Sampling: seeded, class-balanced, without replacement; seed `31415`.
- Recovery features: image values scaled to `[0,1]`; label-blind 4x4 mean and horizontal/vertical gradient pooling; seeded random projection to 256 dimensions; `tanh`; stored as float16 and converted to float32 by the notebook.
- Generation environment: Python 3.11.8, NumPy 2.2.4, PyTorch 2.6.0, torchvision 0.21.0, CPU.

Regenerate the tested no-network package after source files are cached:

```bash
python courseware/shared/data/day-3/generate_day3_offline_artifacts.py --surrogate-transfer
```

The generator does not download unless `--download` is passed. It recomputes byte sizes and SHA-256 values in `manifest.json`.

## Claim Boundary

The artifacts preserve participant work on image shapes, bounded scratch training, feature maps, misclassifications, tiny-data overfitting, a one-remedy comparison, feature-cache loading, new-head training, freeze reasoning, and quality/resource scoreboards.

The transfer surrogate is not CIFAR-10, not pretrained MobileNet output, and not evidence that transfer beats scratch. It does not validate the canonical CIFAR metric bands, MobileNet extraction, weight-specific normalization effects, extraction time, or participant-machine cache behavior. The notebook labels every recovery scoreboard row with its mode.

No artifact contains a trained classifier head, predictions, completed learner model, hidden label beyond the ordinary dataset target, response key, or instructor-only content.

## Canonical Preparation

For a connected release-preparation environment, the generator can attempt official CIFAR-10 and `MobileNet_V3_Small_Weights.DEFAULT` extraction:

```bash
python courseware/shared/data/day-3/generate_day3_offline_artifacts.py --download
```

That path calls `weights.transforms()`, freezes the feature extractor, and builds a cache key from weights, transforms, split, and version metadata. Review upstream CIFAR-10 redistribution terms before distributing a packaged CIFAR subset outside this repository.

The participant `LAB-D3-04` notebook separately preflights the exact default-weight cache. With `ALLOW_DOWNLOAD=False`, missing weights select the labeled recovery package before CIFAR access; with `ALLOW_DOWNLOAD=True`, a successful weight preflight is required before the canonical CIFAR race begins.
# Insight Recommendations: Design-Facing Index

**Purpose:** Concise pointer into the canonical [`courseware/01-insight-map.md`](../01-insight-map.md). This file is not a second insight map and does not change IDs, paths, timing, objectives, or scope labels.

## Selection Priorities

1. Preserve the existing **Explain -> Visualize -> Predict -> Experiment -> Observe -> Diagnose -> Explain Why** rhythm.
2. Use one signature reveal per timed cluster rather than stacking many activities.
3. Protect learner prediction and debrief time before `SHORTEN`, `MOVE`, or `OPTIONAL` detail.
4. Make each visual state both **what learners must observe** and **what it must not imply**.
5. Treat every modern-practice bridge as representative and bounded; verify current claims before production.

## Day 1: See It

Canonical section: [Day 1: See It](../01-insight-map.md#day-1-see-it)

| Priority | Canonical IDs | Carry-forward recommendation |
|---|---|---|
| Sticky explanation | `LESSON-D1-02` | "A boundary is where weighted evidence and bias exactly cancel." Let motion precede $w\cdot x+b=0$. |
| Signature visual | `ACT-D1-01`, `LAB-D1-01` | Ghosted before/after contours separate boundary rotation, translation, and confidence change. |
| Conceptual reveal | `LESSON-D1-03`, `LESSON-D1-05`, `LAB-D1-02` | Let a linear model succeed before XOR; show the same point identities in raw and nonlinear hidden spaces. |
| Shape habit | `LESSON-D1-04`, `ACT-D1-04`, `LAB-D1-03` | Make expected shape/range an executable hypothesis before every matrix operation. |
| Day mystery | `LESSON-D1-06`, `LAB-D1-04` | Reveal raw geometry -> probability -> boundary -> hidden representation; require evidence for each correct/failing probe. |

Use the detailed [Day 1 lesson](../01-insight-map.md#day-1-lesson-insights), [lab](../01-insight-map.md#day-1-lab-signature-moments), and [activity](../01-insight-map.md#day-1-activity-refinements) entries when drafting.

## Day 2: Train It

Canonical section: [Day 2: Train It](../01-insight-map.md#day-2-train-it)

| Priority | Canonical IDs | Carry-forward recommendation |
|---|---|---|
| Sticky explanation | `LESSON-D2-01`, `LESSON-D2-03` | Forward computes; backprop carries local sensitivity; optimization applies the change. Avoid causal-blame language. |
| Counterintuitive result | `ACT-D2-01`, `LAB-D2-01` | Equal accuracy can hide different loss; oscillation can still converge. |
| Invisible process | `LESSON-D2-03`, `LAB-D2-02` | Pair forward values, backward sensitivities, predicted signs, and finite-difference evidence on one tiny graph. |
| Framework reveal | `LESSON-D2-05`, `LESSON-D2-06` | Highlight exactly what PyTorch automates and what judgment remains explicit. |
| Model detective | `LESSON-D2-07`, `ACT-D2-04`, `LAB-D2-04` | Reveal symptom evidence before faulty code; require the cheapest discriminating check before a repair. |

Use the detailed [Day 2 lesson](../01-insight-map.md#day-2-lesson-insights), [lab](../01-insight-map.md#day-2-lab-signature-moments), and [activity](../01-insight-map.md#day-2-activity-refinements) entries when drafting.

## Day 3: Scale It

Canonical section: [Day 3: Scale It](../01-insight-map.md#day-3-scale-it)

| Priority | Canonical IDs | Carry-forward recommendation |
|---|---|---|
| Sticky explanation | `LESSON-D3-02`, `LAB-D3-01` | "A validation score is evidence only if validation stayed outside the training decisions." |
| Provenance reveal | `ACT-D3-02`, `LAB-D3-01` | Reveal metric -> correlation -> provenance -> code -> repaired evidence. Treat the lower valid score as a win. |
| Feature-map visual | `LESSON-D3-03`, `ACT-D3-03`, `LAB-D3-02` | Tie every selected map to shape and tested stimulus; do not label bright activations as complete explanations. |
| Make/fix failure | `LESSON-D3-04`, `LESSON-D3-05`, `LAB-D3-03` | Create visible overfit, choose one rescue, and compare aligned curves; a failed rescue can still be strong evidence. |
| Transfer race | `LESSON-D3-06`, `LAB-D3-04` | Isolate pretraining, freezing, and preprocessing; score quality, time, trainable parameters, and explanation. |
| Bounded modern bridge | `LESSON-D3-07`, `LESSON-D3-08`, `ACT-D3-04` | Keep attention and scale conceptual; attention is not complete explanation, and GPU presence is not utilization. |

Use the detailed [Day 3 lesson](../01-insight-map.md#day-3-lesson-insights), [lab](../01-insight-map.md#day-3-lab-signature-moments), and [activity](../01-insight-map.md#day-3-activity-refinements) entries when drafting.

## Day 4: Think Like an ML Engineer

Canonical section: [Day 4: Think Like an ML Engineer](../01-insight-map.md#day-4-think-like-an-ml-engineer)

| Priority | Canonical IDs | Carry-forward recommendation |
|---|---|---|
| Consequence-first evaluation | `LESSON-D4-01`, `ACT-D4-01`, `LAB-D4-01` | Move the threshold while confusion counts and scenario cost update; accuracy/AUC do not choose the operating point. |
| Error-slice funnel | `LESSON-D4-02`, `LESSON-D4-03`, `LAB-D4-02` | Aggregate -> curve pattern -> confusion pair -> examples -> slice/payoff; frequency and consequence may disagree. |
| One-experiment discipline | `LESSON-D4-04`, `LAB-D4-03` | Require expected and disconfirming evidence before compute; reward a clean negative result over an unexplained win. |
| Reproducibility and resources | `LESSON-D4-05`, `LESSON-D4-06`, `ACT-D4-03` | Record data/split, seed, device, tolerance, timing method, size, latency, throughput, and quality; do not promise bitwise repeatability. |
| Frontier transfer | `LESSON-D4-07`, `ACT-D4-04` | Ask what "better" means and how evaluation could be fooled; keep examples representative and source-checked. |
| Capstone evidence board | `LESSON-D4-08`, `LAB-D4-04` | Gate the primary run behind diagnosis, disconfirming evidence, one intervention, and predicted observations; score the canonical evidence chain. |

Use the detailed [Day 4 lesson](../01-insight-map.md#day-4-lesson-insights), [lab](../01-insight-map.md#day-4-lab-signature-moments), and [activity](../01-insight-map.md#day-4-activity-refinements) entries when drafting.

## Cross-Course Visual Assets

Prioritize reusable visual systems rather than decorative graphics:

- Boundary motion with fixed probes and ghosted contours.
- Raw/hidden-space linked points.
- Forward/backward dual trace.
- Matrix/tensor shape tiles.
- Data-provenance timeline and split boundary.
- Feature-map progression with shape and interpretation caveat.
- Aligned baseline/intervention learning curves.
- Moving threshold with confusion/cost updates.
- Aggregate-to-slice error funnel.
- Quality/resource Pareto chart and capstone evidence board.

The observation and non-implication contracts are in [Visual and Challenge Grammar](../01-insight-map.md#visual-and-challenge-grammar).

## Modern-Practice Boundaries

Use the [Modern-Practice Connection Guardrails](../01-insight-map.md#modern-practice-connection-guardrails) to connect fundamentals to training, post-training, evaluation/graders, data quality, debugging, transfer/fine-tuning, behavior analysis, safety evaluation, GPU utilization, throughput, latency, memory, regression detection, and capability improvement.

These are transfer prompts, not new implementation outcomes. Reinforcement learning, distributed training, mixed-precision implementation, quantization, and deep interpretability retain their canonical `MOVE`/reference status.

## Verification Gate

Before lesson or notebook production, review [Claims Requiring Current Primary-Source Verification](../01-insight-map.md#claims-requiring-current-primary-source-verification). Highest-risk checks are:

- Current PyTorch training, loss, mode, zero-grad, checkpoint, and determinism behavior.
- Current TorchVision datasets/transforms and pretrained MobileNet V3 Small weights/transforms.
- Mixed-precision and device-specific behavior.
- Accelerator timing, memory, latency, and throughput methodology.
- Current public claims about post-training, graders/evaluation, safety evaluation, interpretability, and frontier engineering practice.
- Pinned Python/PyTorch/TorchVision/scikit-learn/Colab compatibility and calibrated runtime/metric bands.

Record final evidence in `courseware/reviews/source-verification.md`; do not convert a planning snapshot into an undated fact.
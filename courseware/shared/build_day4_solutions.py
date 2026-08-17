from __future__ import annotations

import ast
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TMPDIR = Path(os.environ["TMPDIR"])


def markdown_cell(cell_id: str, source: str) -> dict:
    return {
        "cell_type": "markdown",
        "id": cell_id,
        "metadata": {"id": cell_id, "language": "markdown"},
        "source": source.splitlines(keepends=True),
    }


def write_solution(
    source_name: str,
    destination: Path,
    appendix: list[dict],
    title_prefix: str,
) -> None:
    notebook = json.loads((TMPDIR / source_name).read_text())
    title = "".join(notebook["cells"][0]["source"])
    notebook["cells"][0]["source"] = title.replace("# LAB-", title_prefix, 1).splitlines(keepends=True)
    notebook["cells"].extend(appendix)
    notebook.setdefault("metadata", {})["instructor_only"] = True
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(notebook, indent=1, ensure_ascii=True) + "\n")


def literal_assignment(source: str, name: str):
    for node in ast.parse(source).body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == name
        ):
            return ast.literal_eval(node.value)
    raise ValueError(f"Could not find literal assignment for {name}")


def subscript_assignment(source: str, container: str) -> tuple[str, object]:
    for node in ast.walk(ast.parse(source)):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name) and target.value.id == container:
            return ast.literal_eval(target.slice), ast.literal_eval(node.value)
    raise ValueError(f"Could not find subscript assignment for {container}")


D4_01_APPENDIX = [
    markdown_cell(
        "d401-sol-01",
        """---

## Instructor Debrief: What, Why, and Concept

**Correct implementation.** `metric_row` fixes the label order as `[0, 1]`, unpacks `[[TN, FP], [FN, TP]]`, and computes precision, recall, and F1 with `zero_division=0`. `threshold_sweep` applies one threshold at a time to the unchanged probability scores, then computes every metric and every declared consequence cost from the same confusion counts.

**Why it is correct.** The majority classifier obtains about **0.9539 accuracy** because the negative class is about 95.4% of validation examples, yet its minority recall and F1 are both **0**. Accuracy answers how often the classifier is right under the observed class mix; it does not encode the asymmetric consequence of a missed positive. The fitted probability model at threshold `0.50` recovers about **0.6627 recall**, **0.9167 precision**, and **0.7692 F1**. Under the miss-dominant cost, the minimum-cost operating point is `0.19`; under the block-dominant cost it is `0.43`. The optional intermediate cost selects about `0.26`.

**Concept.** The deliberate accuracy-only rule selects `probability@0.5`, not the majority baseline, on this seeded data. That choice is still wrong for the miss-dominant decision because `0.19` has lower declared cost. Keep this distinction explicit: the lesson is not that accuracy must always select the majority model; it is that an accuracy-only model/threshold rule can select a non-cost-optimal operating point.
""",
    ),
    markdown_cell(
        "d401-sol-02",
        """## Expected Evidence and Plot Reading

- Majority baseline: accuracy in `0.95-0.97`, `TN=1717`, `FP=0`, `FN=83`, `TP=0`, minority recall `0`, F1 `0`.
- Probability model at `0.50`: recall in the calibrated `0.55-0.85` band; this run is about `0.6627`.
- Cost optima: miss-dominant `0.19`, block-dominant `0.43`, optional intermediate `0.26`. Small version-level numeric changes are acceptable only if the confusion/cost arithmetic is internally consistent and the scenarios still lead to different decisions.
- Threshold dashboard: all confusion counts, rates, and costs at one x-position must come from the same threshold. Lowering the threshold normally raises both TP and FP; it does not refit or reorder the probability scores.
- Precision-recall plot: the selected operating point belongs to the declared consequence model. Average precision and ROC AUC summarize ranking behavior across thresholds; neither chooses a deployment threshold or supplies a cost model.

Discussion trigger: "If AUC is unchanged when the threshold moves, what decision-relevant evidence did change?" Expected answer: the confusion counts, precision/recall trade-off, and consequence cost changed while score ranking stayed fixed.
""",
    ),
    markdown_cell(
        "d401-sol-03",
        """## Hint Ladder, Misconceptions, and Alternatives

1. Ask which class a majority classifier never predicts.
2. Ask participants to mark true-label rows and predicted-label columns before naming TN/FP/FN/TP.
3. Ask which error receives the larger multiplier in each scenario.
4. Point to the same probability vector and ask what the threshold changes.
5. Only then suggest comparing `FN * C_FN + FP * C_FP` for each row.

Common wrong answers:

- "95% accuracy means the baseline is useful." It misses every positive example.
- "Lower threshold improves the model." It changes the operating point, not the fitted ranking model, and can increase false positives.
- "AUC says to use `0.19`." AUC contains no deployment consequence or threshold-selection rule.
- "F1 is the cost function." F1 weights precision and recall through its own definition; it does not represent the stated monetary or operational costs.
- "The optimal threshold is permanent." It is conditional on prevalence, calibration, data drift, and the declared cost assumptions.

Acceptable alternatives include a constrained-recall rule, a maximum false-positive-rate rule, or expected utility with a different documented cost matrix. They are valid only when the decision rule is declared before selecting the threshold and evaluated on held-out evidence.
""",
    ),
    markdown_cell(
        "d401-sol-04",
        """## Instructor Operations and Recovery

Run from top to bottom on CPU. The required path uses generated in-notebook data, fixed seeds, no files, and no network. Expect a few seconds after kernel startup and two nonblank plots. Exact timing is host-specific.

Troubleshooting:

- If confusion values appear swapped, verify `labels=[0, 1]` and rows=true, columns=predicted.
- If metric warnings appear for the majority baseline, verify `zero_division=0` is passed to precision, recall, and F1.
- If the selected threshold is absent, verify `0.50` is explicitly unioned into the grid and do not round before cost minimization.
- If scenario decisions are identical, inspect whether each scenario uses its own FN/FP multipliers.
- If a live plot fails, preserve predictions and the cost declaration, rerun the synchronized table, and discuss from the printed optimum rows. Do not substitute an AUC-only conclusion.

Reproducibility note: fixed seeds support this local CPU result but do not turn the calibrated values into universal production thresholds. A hosted Colab CPU run remains a separate environment check.
""",
    ),
]


D4_02_APPENDIX = [
    markdown_cell(
        "d402-sol-01",
        """---

## Instructor Debrief: Four Curve Bundles

| Bundle | Leading diagnosis | Independent observations | Competing explanation | Discriminating next evidence |
|---|---|---|---|---|
| `M1` | healthy fit | train/validation loss fall together; accuracy rises with a modest gap | an important class or slice may still fail | class recall and slice metrics |
| `M2` | limited fit/high bias | both losses remain high; both accuracies plateau low | weak features or representation can mimic insufficient capacity | one capacity-controlled comparison plus feature audit |
| `M3` | widening generalization gap | training loss keeps falling; validation loss reverses upward | split shift or label noise can produce the same symptom | split/slice audit, duplicate/label checks, and a single regularization comparison |
| `M4` | unstable optimization | loss oscillates; accuracy jumps rather than settling | a corrupted batch or implementation invariant can create spikes | learning-rate/gradient trace and batch/invariant check |

These are ranked hypotheses, not unique causal labels. Absolute levels, train/validation gaps, and paths all matter. A gap without absolute levels is insufficient: two poor curves can have a small gap and still indicate limited fit.
""",
    ),
    markdown_cell(
        "d402-sol-02",
        """## Expected Error Evidence

- Validation accuracy: about **0.9526**, calibrated band `0.90-0.96`.
- Confusion matrix: exactly `(10, 10)`, with rows=true labels and columns=predictions.
- Errors: **17** total; at least one has confidence `>=0.70`.
- High-border-ink slice: **93** examples, **6** errors, severity-weighted payoff proxy **12**.
- Low-total-ink slice: **90** examples, **8** errors, payoff proxy **8**.
- Slice overlap: **18** examples. Overlap is allowed for slice analysis and must be reported.
- Required exclusive-bucket accounting in this solution: high-border `4`, high-confidence `2`, low-total `7`, other `4`; total **17/17**.
- Optional low-confidence error view: **6** errors below confidence `0.45`. It is an additional view, not a replacement for the required exclusive accounting.

The confidence-ranked gallery is useful for inspection but cannot estimate prevalence. The confusion matrix counts directed errors, while a gallery may intentionally overrepresent unusual or high-confidence cases.
""",
    ),
    markdown_cell(
        "d402-sol-03",
        """## Multiple Valid Bucket Schemas

The supplied precedence is only one valid schema. Any schema is acceptable when definitions are fixed before reading outcomes, every error is assigned exactly once for the exclusive table, and overlaps remain visible in the nonexclusive slice table.

Valid examples:

- `high_confidence -> high_border -> low_ink -> other` prioritizes surprising errors.
- `high_border -> low_ink -> high_confidence -> other` prioritizes intervention ownership.
- Directed confusion pair buckets followed by metadata buckets are valid when the pair definitions and precedence are explicit.
- A multi-label tag table is valid for exploratory analysis, but it must not be presented as an exclusive count unless a deterministic primary-bucket rule is added.

The payoff proxy is `observed errors * declared severity weight`. It is a classroom prioritization device, not a causal estimate or a production business value. An acceptable next intervention can target low-total-ink instead of border ink if the team declares a different consequence weight and a falsifiable observation.
""",
    ),
    markdown_cell(
        "d402-sol-04",
        """## Hint Ladder, Misconceptions, and Operations

1. Ask participants to describe curve direction without naming a diagnosis.
2. Require a second independent observation.
3. Ask for one alternative that predicts a similar curve.
4. Ask which single evidence card separates the two.
5. For error analysis, distinguish overlapping slice membership from exclusive accounting.

Common misconceptions:

- "The largest confusion pair proves the architecture is too small." Frequency does not identify mechanism or intervention.
- "High confidence means the label is wrong." It is a review priority, not proof of label error.
- "A slice with more errors is worse." Compare support, error rate, consequence, and uncertainty.
- "One image explains the bucket." Galleries generate hypotheses; quantified aligned arrays test prevalence.

Run on CPU from the repository root with `courseware/shared/data/day-4/` present. The solution performs no training or network access and should finish in a few seconds with five nonblank plots. If an artifact check fails, stop and compare its manifest SHA-256; do not silently regenerate during class. If a gallery fails, retain the aligned sample IDs and quantified tables, then recover the visualization after the evidence decision.
""",
    ),
]


D4_03_APPENDIX = [
    markdown_cell(
        "d403-sol-01",
        """---

## Instructor Debrief: The Controlled Negative Result

The canonical solution changes only learning rate, `0.003 -> 0.001`, under the fixed seven-epoch budget. It reaches about **0.8496 validation accuracy** and **0.8445 macro-F1**, below the packaged baseline accuracy **0.8969** and macro-F1 **0.8940**. Two freshly constructed same-seed runs match within the declared `0.02` tolerance (exactly on the recorded stack). This is a successful experiment and a rejected intervention: the result separates slow convergence under the fixed budget from an assumption that a smaller learning rate must improve generalization.

The confounded draft changes width, optimizer, and learning rate and must fail before training. The epoch gate also rejects any proposal above 20 epochs. A budget violation is an experiment-design failure, not a reason to silently extend the run.
""",
    ),
    markdown_cell(
        "d403-sol-02",
        """## Intervention Menu Solution Notes

Every bounded menu option is executable and was exercised during solution validation. Interpret each as one experiment, not as a tuning sweep available to participants.

| Changed factor | Values | Mechanism tested | Resource expectation | Valid rejection evidence |
|---|---|---|---|---|
| hidden width | `(16,)`, `(64,)` | capacity limitation | parameter bytes and often latency change | quality does not move as predicted or trade-off is dominated |
| optimizer | `sgd`, `adamw` | update dynamics/regularization | bytes fixed; training path and timing may change | curves/quality do not improve under fixed budget |
| learning rate | `0.001`, `0.01` | step size too small/large | bytes fixed; latency broadly comparable | instability, slow convergence, or validation regression |
| weight decay | `0.001`, `0.01` | regularization improves held-out behavior | bytes fixed | no gap/validation benefit or underfit regression |
| class weight | `True` | class-frequency-sensitive loss | bytes fixed | class-aware evidence does not improve or aggregate regression exceeds tolerance |

A participant should choose one branch from prior evidence. The instructor validation sweep exists to prove menu executability, not to license post-hoc best-score selection.
""",
    ),
    markdown_cell(
        "d403-sol-03",
        """## Record, Reproduction, and Resource Method

The JSON-serializable record includes source/split hash, seed, CPU device, package versions, full configuration, changed factor, primary and repeat metrics, training seconds, parameter count/bytes, timing method, and checkpoint identity. Tuples serialize as JSON arrays; a persisted checkpoint identity should additionally bind model state and preprocessing in a real system.

Fresh reproduction means recreating model, optimizer, seeded loader generator, and training state. Reusing a trained model is not a rerun. The optional alternate seed is sensitivity evidence, not same-seed reproduction and not proof of distributional robustness.

Parameter bytes are computed from tensor element counts and element sizes. Batch-1 latency uses evaluation mode, inference mode, 20 warmups, and 100 repeated measurements, reporting median and p90. On accelerators, synchronization is required around timed work; end-to-end service claims also require data transfer, preprocessing, batching, throughput, memory, tail latency, and deployment environment. Host-specific timing differences do not invalidate the method.
""",
    ),
    markdown_cell(
        "d403-sol-04",
        """## Hint Ladder, Alternatives, and Recovery

1. Ask which baseline observation motivates the proposed factor.
2. Circle every field that differs from baseline.
3. Require predicted metric, curve, and resource directions.
4. Require an observation that would reject the idea.
5. Authorize compute only after the serialized contract can be explained.

Common wrong answers include calling a negative score a failed lab, treating one alternate seed as reproducibility proof, comparing latency without warmup/repeats/environment, or changing epochs alongside the intervention. Acceptable alternatives include confidence intervals over several predeclared seeds, operation counts, peak memory, throughput, or model-file bytes, provided the comparison contract and limitations are explicit.

Run on one CPU thread from the repository root; no network is used. If training fails, preserve the hypothesis and exact configuration, identify the first failed invariant, attempt one bounded repair, and use the matching packaged baseline only for continued reasoning. Do not relabel cached evidence as a live intervention result.
""",
    ),
]


CAPSTONE_APPENDIX = [
    markdown_cell(
        "d404-sol-01",
        """---

## Instructor Debrief: Selector and Case Dispositions

Set environment variable `DAY4_PROFILE` to `A`, `B`, or `C` before **Restart Kernel -> Run All**. The default is `A`. Each fresh run requests one evidence card, commits one major intervention, completes the ledger and evidence board, locks the development decision, accesses test once, runs one validation-only optional follow-up, and completes the defense.

| Profile | Primary hypothesis | Secondary hypothesis | One primary change | Validation disposition |
|---|---|---|---|---|
| A | limited class support/composition harms worst-class recall | representation or label ambiguity | `class_weight: False -> True` | supported/narrowed; worst recall and aggregate quality improve |
| B | excess capacity on constrained data creates high variance | split shift | `dropout: 0.0 -> 0.5` | supported/narrowed; gap falls and validation improves |
| C | excessively aggressive optimization prevents stable fit | insufficient capacity | `learning_rate: 0.20 -> 0.003` | supported/narrowed; curves stabilize and validation improves |

These are calibration keys, not causes participants must guess. A coherent off-key intervention can earn strong credit when evidence, rejection criteria, controls, and interpretation are sound.
""",
    ),
    markdown_cell(
        "d404-sol-02",
        """## Expected Live Evidence

| Profile | Baseline validation / macro-F1 / worst recall | Primary validation / macro-F1 | Key delta | Authorized test accuracy / macro-F1 |
|---|---|---|---|---|
| A | `0.8301 / 0.8014 / 0.1714` | `0.9109 / 0.9097` | accuracy `+0.0808`; worst recall `+0.5429` | `0.9222 / 0.9223` |
| B | `0.8802 / 0.8809 / 0.7143`, train `1.0000` | `0.9109 / 0.9100` | gap reduction about `0.0306` | `0.8944 / 0.8946` |
| C | `0.7827 / 0.7676 / 0.2286` | `0.8969 / 0.8964` | accuracy `+0.1142`; gap `0.0791 -> 0.0363` | `0.8944 / 0.8951` |

Use calibrated bands, not exact-value grading: allow small package/platform differences while requiring the target direction, one-factor attribution, internally consistent confusion/recall, and declared tolerance. Latency is host-specific; parameter bytes and split hash should remain exact for a fixed configuration.
""",
    ),
    markdown_cell(
        "d404-sol-03",
        """## Test Lock, Recovery, and Optional Follow-Up

The notebook denies `access_test_split()` before authorization. Diagnosis, intervention, validation comparison, ledger, evidence board, checkpoint choice, expected test behavior, and decision record must all exist before `TEST_AUTHORIZED = True`. The authorized test record is used once and explicitly records `used_for_further_tuning=False`.

Cached recovery is selected only by the SHA-256 fingerprint of the already committed primary configuration. It provides validation curves, probabilities, predictions, resources, and no trained checkpoint, cause label, intervention name, or test metric. A recovery run therefore supports diagnosis/defense but truthfully reports that authorized test metrics are unavailable.

The optional follow-up changes one additional field, uses validation only, and cannot replace the frozen test claim. Profile A tests weight decay, B tests smaller width, and C tests AdamW. The strongest default decision is often not to spend this run unless it separates a remaining uncertainty.
""",
    ),
    markdown_cell(
        "d404-sol-04",
        """## Hint Ladder, Misconceptions, and Defense Triggers

1. Separate facts from hypotheses on the board.
2. Compare absolute train and validation levels, the gap, and the path.
3. Name a real alternative and one disconfirming observation.
4. Circle the single changed field and state expected quality/slice/resource effects.
5. Lock the model choice and expected test range before authorization.

Profile nudges: A compares class support with worst recall; B locates where validation stops following training; C asks whether optimization is stable enough to diagnose capacity.

Common wrong diagnoses include equating every gap with overfitting, treating weak train/validation scores as high variance, assuming class weighting proves data imbalance, and treating a corrected learning rate as proof that architecture is irrelevant. Discussion triggers: "Which result threatened your mechanism?", "Why was this experiment higher-information than the next best?", and "Which resource number is least portable?"
""",
    ),
    markdown_cell(
        "d404-sol-05",
        """## Rubric and Instructor Operations

The team rubric is exactly **25 model performance + 20 generalization + 20 experimental design + 15 diagnosis + 10 efficiency + 10 explanation = 100**. The individual `CHECK-D4-04` is separate evidence of transfer and is not folded into the team arithmetic.

Run each profile from a fresh CPU kernel with one thread and the shared Day 4 directory present. Expect three nonblank plots and completion far below the 12-minute ceiling on the validated local stack. No network is required. Record package versions, split hash, device, timing warmups/repeats, profile, live/recovery status, and test-lock state.

Troubleshooting: a fingerprint mismatch means the cached recovery does not match the committed intervention; do not bypass it. A second test access or post-test model selection invalidates the generalization claim. If a live run fails after one bounded repair, use exact matched recovery, label it **CACHED EVIDENCE**, omit test metrics, and continue the defense with the limitation visible.
""",
    ),
]


def build_capstone_solution() -> None:
    notebooks = {
        profile: json.loads((TMPDIR / f"LAB-D4-04-profile-{profile}-participant-completed.ipynb").read_text())
        for profile in "ABC"
    }
    notebook = notebooks["A"]
    notebook["cells"][0]["source"] = "".join(notebook["cells"][0]["source"]).replace(
        "# LAB-D4-04:", "# LAB-D4-04 Instructor Solution:", 1
    ).splitlines(keepends=True)

    selector_source = "".join(notebook["cells"][3]["source"])
    notebook["cells"][3]["source"] = (
        'PROFILE_ID = os.environ.get("DAY4_PROFILE", "A").strip().upper()\n'
        + selector_source.split("\n", 1)[1]
    ).splitlines(keepends=True)
    imports = "".join(notebook["cells"][1]["source"])
    notebook["cells"][1]["source"] = ("import os\n" + imports).splitlines(keepends=True)

    evidence_requests = {
        profile: literal_assignment("".join(value["cells"][12]["source"]), "evidence_request")
        for profile, value in notebooks.items()
    }
    evidence_tail = "".join(notebook["cells"][12]["source"]).split("assert evidence_request", 1)[1]
    notebook["cells"][12]["source"] = (
        f"EVIDENCE_REQUESTS = {evidence_requests!r}\n"
        "evidence_request = dict(EVIDENCE_REQUESTS[PROFILE_ID])\n"
        "assert evidence_request"
        + evidence_tail
    ).splitlines(keepends=True)

    diagnoses = {
        profile: literal_assignment("".join(value["cells"][14]["source"]), "diagnosis_gate")
        for profile, value in notebooks.items()
    }
    diagnosis_tail = "".join(notebook["cells"][14]["source"]).split("assert all", 1)[1]
    notebook["cells"][14]["source"] = (
        f"DIAGNOSIS_GATES = {diagnoses!r}\n"
        "diagnosis_gate = dict(DIAGNOSIS_GATES[PROFILE_ID])\n"
        "assert all"
        + diagnosis_tail
    ).splitlines(keepends=True)

    primary_changes = {
        profile: subscript_assignment("".join(value["cells"][16]["source"]), "PRIMARY_CONFIG")
        for profile, value in notebooks.items()
    }
    predictions = {
        profile: literal_assignment(
            "".join(value["cells"][16]["source"]).replace(
                '"changed_field": changed_fields[0]',
                f'"changed_field": {primary_changes[profile][0]!r}',
            ),
            "intervention_prediction",
        )
        for profile, value in notebooks.items()
    }
    primary_tail = "".join(notebook["cells"][16]["source"]).split("changed_fields =", 1)[1]
    prediction_assert = primary_tail.split("assert all", 1)[1]
    notebook["cells"][16]["source"] = (
        'MAJOR_FIELDS = {"hidden", "dropout", "optimizer_name", "learning_rate", "weight_decay", "class_weight"}\n'
        "PRIMARY_CONFIG = dict(BASELINE_CONFIG)\n"
        f"PRIMARY_CHANGES = {primary_changes!r}\n"
        "primary_field, primary_value = PRIMARY_CHANGES[PROFILE_ID]\n"
        "PRIMARY_CONFIG[primary_field] = primary_value\n\n"
        "changed_fields ="
        + primary_tail.split("intervention_prediction =", 1)[0]
        + f"INTERVENTION_PREDICTIONS = {predictions!r}\n"
        "intervention_prediction = dict(INTERVENTION_PREDICTIONS[PROFILE_ID])\n"
        "assert all"
        + prediction_assert
    ).splitlines(keepends=True)

    optional_changes = {
        profile: subscript_assignment("".join(value["cells"][26]["source"]), "OPTIONAL_CONFIG")
        for profile, value in notebooks.items()
    }
    optional_follow_up = literal_assignment("".join(notebook["cells"][26]["source"]), "optional_follow_up")
    notebook["cells"][26]["source"] = (
        "RUN_OPTIONAL_FOLLOW_UP = True\n"
        f"optional_follow_up = {optional_follow_up!r}\n"
        "OPTIONAL_CHANGES = "
        f"{optional_changes!r}\n"
        "if RUN_OPTIONAL_FOLLOW_UP:\n"
        "    assert all(value.strip() for value in optional_follow_up.values())\n"
        "    OPTIONAL_CONFIG = dict(PRIMARY_CONFIG)\n"
        "    optional_field, optional_value = OPTIONAL_CHANGES[PROFILE_ID]\n"
        "    OPTIONAL_CONFIG[optional_field] = optional_value\n"
        "    optional_changed = [field for field in MAJOR_FIELDS if OPTIONAL_CONFIG[field] != PRIMARY_CONFIG[field]]\n"
        "    assert len(optional_changed) == 1\n"
        "    optional_run = run_experiment(OPTIONAL_CONFIG, case_train_indices, val_indices)\n"
        '    print("Optional validation only:", optional_run["validation"]["accuracy"])\n'
    ).splitlines(keepends=True)

    notebook["cells"].extend(CAPSTONE_APPENDIX)
    notebook.setdefault("metadata", {})["instructor_only"] = True
    destination = ROOT / "courseware/capstone/capstone-solution.ipynb"
    destination.write_text(json.dumps(notebook, indent=1, ensure_ascii=True) + "\n")


if __name__ == "__main__":
    write_solution(
        "LAB-D4-01-participant-completed.ipynb",
        ROOT / "courseware/instructor-solutions/day-4/LAB-D4-01-accuracy-is-not-enough-SOLUTION.ipynb",
        D4_01_APPENDIX,
        "# LAB-D4-01 Instructor Solution:",
    )
    write_solution(
        "LAB-D4-02-participant-completed.ipynb",
        ROOT / "courseware/instructor-solutions/day-4/LAB-D4-02-model-detective-SOLUTION.ipynb",
        D4_02_APPENDIX,
        "# LAB-D4-02 Instructor Solution:",
    )
    write_solution(
        "LAB-D4-03-participant-completed.ipynb",
        ROOT / "courseware/instructor-solutions/day-4/LAB-D4-03-one-experiment-SOLUTION.ipynb",
        D4_03_APPENDIX,
        "# LAB-D4-03 Instructor Solution:",
    )
    build_capstone_solution()
# Day 3 Instructor Guide: Scale It

**Instructor only. Do not distribute with participant materials.**

**Canonical question:** How do the fundamentals become the systems used in modern AI?  
**Day outcome:** Participants build a valid compact image workflow, expose a generalization failure, compare scratch and transfer evidence, and connect the same fundamentals to bounded attention and systems-scale decisions.  
**Must-land sentence:** **A stronger architecture cannot rescue invalid evidence.**

## Controlling Artifacts

- Participant guide: [courseware/day-3/student-guide/day-3-student-guide.md](../day-3/student-guide/day-3-student-guide.md)
- Participant challenges: [courseware/day-3/challenges/day-3-challenges.md](../day-3/challenges/day-3-challenges.md)
- Challenge key: [courseware/instructor-solutions/day-3/day-3-challenges-SOLUTION.md](../instructor-solutions/day-3/day-3-challenges-SOLUTION.md)
- Participant checks: [courseware/day-3/assessments/day-3-checks.md](../day-3/assessments/day-3-checks.md)
- Check key: [courseware/instructor-solutions/day-3/day-3-checks-SOLUTION.md](../instructor-solutions/day-3/day-3-checks-SOLUTION.md)
- Slide source: [courseware/slides/day-3-scale-it.md](../slides/day-3-scale-it.md)
- Shared glossary: [courseware/shared/glossary.md](../shared/glossary.md)
- Shared notation: [courseware/shared/notation-and-style.md](../shared/notation-and-style.md)
- Shared environment: [courseware/shared/environment.md](../shared/environment.md)

## Objective and Evidence Map

| Objective | Must observe | Practice | Check |
|---|---|---|---|
| `OBJ-D3-01` | hierarchy/capacity benefits separated from optimization and generalization | `ACT-D3-01`, D3-02/D3-03 comparisons | `CHECK-D3-01` |
| `OBJ-D3-02` | feature time, split boundary, and training-owned fitted state | `ACT-D3-02`, `LAB-D3-01` | `CHECK-D3-02` |
| `OBJ-D3-03` | shared local kernel, `(B,C,H,W)` trace, selected maps | `ACT-D3-03`, `LAB-D3-02` | `CHECK-D3-01` |
| `OBJ-D3-04` | aligned curves distinguish fit/generalization/instability | `LAB-D3-03` | `CHECK-D3-03` |
| `OBJ-D3-05` | one intervention predicts a visible before/after change | `LAB-D3-03` | `CHECK-D3-03` |
| `OBJ-D3-06` | scratch/frozen/pretrained controls and resource scoreboard | `LAB-D3-04` | `CHECK-D3-04` |
| `OBJ-D3-07` | Q/K/V intuition plus explicit attention limitation | `ACT-D3-04` | `CHECK-D3-04` |
| `OBJ-D3-08` | latency/throughput/memory/utilization kept distinct | D3-04 scoreboard, `ACT-D3-04` | `CHECK-D3-04` |

## Exact 450-Minute Schedule

| Time | Min | Mode and canonical IDs | Scope |
|---|---:|---|---|
| 09:00-09:15 | 15 | Retrieve/visualize: `LESSON-D3-01`, `ACT-D3-01` | `CORE`; initialization catalogue is `SHORTEN` |
| 09:15-09:35 | 20 | Explain/predict: `LESSON-D3-02` | `CORE`; DataLoader API detail is `SHORTEN` |
| 09:35-10:20 | 45 | Investigate/diagnose: `LAB-D3-01`, `ACT-D3-02` | `CORE` |
| 10:20-10:35 | 15 | Break | Protected |
| 10:35-11:00 | 25 | Explain/visualize: `LESSON-D3-03`, `ACT-D3-03` | `CORE`; extended receptive-field arithmetic is `SHORTEN` |
| 11:00-12:00 | 60 | Build/observe: `LAB-D3-02` | `CORE` |
| 12:00-12:10 | 10 | Assess/debrief: `CHECK-D3-01` | `CORE` |
| 12:10-13:10 | 60 | Lunch | Protected |
| 13:10-13:25 | 15 | Predict/explain: `LESSON-D3-04`, `LESSON-D3-05` | `CORE`; optimizer/scheduler survey is `SHORTEN` |
| 13:25-14:20 | 55 | Make fail/rescue: `LAB-D3-03` | `CORE`; multiple-remedy sweep is `OPTIONAL` and excluded live |
| 14:20-14:35 | 15 | Break | Protected |
| 14:35-14:50 | 15 | Explain/choose: `LESSON-D3-06` | `CORE`; full fine-tuning is `OPTIONAL`/outside core |
| 14:50-15:45 | 55 | Compare/explain: `LAB-D3-04` | `CORE`; partial unfreezing is `OPTIONAL` |
| 15:45-16:05 | 20 | Conceptual visual: `LESSON-D3-07`, `LESSON-D3-08`, `ACT-D3-04` | `CORE` conceptual; equations/distributed implementation are `MOVE` |
| 16:05-16:20 | 15 | Assess/explain: `CHECK-D3-02` through `CHECK-D3-04` | `CORE` |
| 16:20-16:30 | 10 | Recovery/questions/close | Protected; no new content |

Total: `15+20+45+15+25+60+10+60+15+55+15+15+55+20+15+10 = 450` minutes.

## Current Technical Grounding

**Source-check date:** 2026-08-16. Recheck against the pinned classroom environment before delivery.

| Claim | Status and primary source | Course implication |
|---|---|---|
| MobileNet V3 Small accepts a `weights` enum; `DEFAULT` currently aliases `IMAGENET1K_V1` | Verified/qualified: [official MobileNet V3 Small docs](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.mobilenet_v3_small.html) | `mobilenet_v3_small(weights=MobileNet_V3_Small_Weights.DEFAULT)` is current; record the resolved enum because aliases may change |
| weight-specific preprocessing is bundled on the weight object | Verified: [official torchvision weights guide](https://docs.pytorch.org/vision/stable/models.html) | call `weights.transforms()` or use an equivalent weight-bound transform contract; do not copy constants casually |
| `pretrained=True` is deprecated under the multi-weight API | Verified: [official torchvision weights guide](https://docs.pytorch.org/vision/stable/models.html) | do not teach or use `pretrained=True` |
| FashionMNIST and CIFAR10 constructors include `root`, `train`, `transform`, and `download`; cached data are reused | Verified: [FashionMNIST](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.FashionMNIST.html), [CIFAR10](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR10.html) | download is explicit, opt-in, and cache-aware; train/evaluation transform ownership remains separate |

Do not claim:

- pretrained transfer always wins;
- attention reveals causality;
- a GPU automatically improves utilization or latency;
- hosted Colab execution is validated;
- planning metric bands are current execution evidence.

## Before Class

### Current lab and solution validation

All four participant/solution pairs have current local CPU evidence. Participant paths are **PASS WITH NOTES**. The D3-01 solution is **PASS**; the D3-02 through D3-04 solutions are **PASS WITH NOTES**. Open each participant notebook from a clean kernel and pre-run its corresponding solution before delivery.

| Lab | Participant | Instructor solution | Validated source mode |
|---|---|---|---|
| `LAB-D3-01` | **PASS WITH NOTES** | **PASS** | generated local records |
| `LAB-D3-02` | **PASS WITH NOTES** | **PASS WITH NOTES** | packaged real Fashion-MNIST fallback |
| `LAB-D3-03` | **PASS WITH NOTES** | **PASS WITH NOTES** | independently loaded packaged Fashion-MNIST fallback |
| `LAB-D3-04` | **PASS WITH NOTES** | **PASS WITH NOTES** | packaged Fashion-MNIST recovery images plus label-blind 256-wide surrogate features |

The shared environment covers these Day 3 offline paths on the required local CPU route. Online Fashion-MNIST, canonical CIFAR-10/MobileNet execution and metrics, hosted Colab, and novice completion timing remain explicitly unvalidated.

Do not expose solution paths to participants or use a solution notebook as a setup workaround.

### Cache and network preflight

Run this process before learners arrive:

1. Record Python, PyTorch, torchvision, NumPy, matplotlib, and scikit-learn versions.
2. Record the required CPU path. Optional CUDA/MPS availability is informational.
3. Choose one writable `data_root`; verify FashionMNIST and CIFAR10 cache directories there.
4. Check the torch hub cache used by pretrained weights and record the resolved MobileNet weight enum.
5. Run with downloads disabled first. Enable the notebook's explicit opt-in download only when the expected cache item is absent and network use is approved.
6. Verify that training augmentation is absent from validation/test transforms.
7. Verify that the MobileNet path uses the selected weight object's `transforms()` contract.
8. Verify cache keys include dataset split, weight identity, transform contract, and relevant package/version information.
9. Run CPU reference paths and measure actual runtime. Do not substitute architecture planning ranges.
10. Do not claim hosted Colab validation unless a real hosted run report exists.

The shared environment guide records the tested Day 3 offline source modes and checksums. Treat only the explicitly unvalidated online, canonical, hosted, and novice-timing routes as unresolved.

### Offline fallback and precomputed-evidence recovery

Prepare these before class; verify checksums and open every file offline:

- D3-01 generated-data leaky and repaired metric/provenance tables;
- D3-02 reduced Fashion-MNIST sample, validated checkpoint, shape trace, selected maps, curves, and misclassification panel;
- D3-03 cached baseline and one-intervention histories with aligned axes and best-checkpoint metadata;
- D3-04 packaged `transfer_surrogate_fashion_subset.npz` Fashion-MNIST image/label subset plus `transfer_surrogate_embeddings.npz` label-blind 256-wide surrogate features;
- all Day 3 slide SVG assets under `courseware/shared/assets/day-3/`.

For D3-04, display the recovery boundary before loading either artifact: this route is **not CIFAR-10**, the features are **not MobileNet output**, its metrics and runtime are **not canonical metrics/runtime**, and its result is **not proof that transfer wins**. It preserves recovery practice, fresh-head training, freeze reasoning, and scoreboard construction only. Do not look for a CIFAR manifest or substitute a generic pretrained model.

Recovery sequence:

1. Preserve the participant's prediction and evidence request.
2. Attempt one bounded local repair using the cheapest invariant.
3. Stop a run that exceeds the tested ceiling.
4. Load the matched precomputed evidence, clearly label it as recovery evidence, and continue observation/diagnosis.
5. Record the failed path for retest. Fallback evidence preserves learning; it does not create a Student PASS.

If no validated data/checkpoint/embedding fallback exists, use slide assets only for discussion and mark the lab execution gate unresolved. Do not invent numeric outputs live.

### Pair roles

- **Driver:** edits and runs the current notebook section.
- **Evidence lead:** preserves predictions and records observations/limitations.
- **Provenance/shape checker:** states availability time or `(B,C,H,W)` before each reveal.
- Swap roles halfway through every lab.

## Operational Pacing Routes

### If behind

Cut in this order:

1. initialization and optimizer/scheduler catalogues;
2. extra receptive-field arithmetic;
3. additional D3-02 map channels/mistakes;
4. all multi-intervention or augmentation sweeps;
5. partial/full fine-tuning discussion beyond the core comparison;
6. attention equations and distributed algorithms, which are already `MOVE`.

Switch to validated precomputed evidence after one bounded recovery attempt. Preserve predictions, leak audit, kernel shape trace, one overfit rescue, transfer scoreboard, attention limitation, all debriefs/checks, protected breaks/lunch, and final buffer.

### If ahead

1. Ask for one disconfirming observation before a second model change.
2. Translate one input and ask whether selected CNN responses move consistently.
3. Compare pretrained/frozen with random/frozen under the same contract.
4. Add one error slice to the transfer scoreboard.
5. Ask which systems measurement could reverse a resource choice.
6. Do not begin Day 4 metric formulas or capstone content.

---

# Facilitation Runbook

## 09:00-09:15 - LESSON-D3-01 + ACT-D3-01: Retrieve, Categorize, Build the Feature Ladder

**Objective:** `OBJ-D3-01`  
**Must land:** A Day 2 failure can come from implementation/optimization, representation, or data/evaluation; depth is an intervention, not a diagnosis.

### Sequence

| Minute | Move |
|---:|---|
| 0-3 | Learners open `ACT-D2-04` and `CHECK-D2-04` Part C without editing. |
| 3-7 | Sort one actual response into implementation, optimization, representation, and data/evaluation evidence. |
| 7-10 | Build raw -> local -> intermediate -> task-relevant feature ladder. |
| 10-14 | Run `ACT-D3-01` constraint round and collect the original commitment. |
| 14-15 | State the day's question and must-land sentence. |

### Required Day 2 retrieval

Sample the `ACT-D2-04` field "The evidence that most changed my diagnosis..." and `CHECK-D2-04` Part C. Ask:

- **Q:** Which evidence is implementation or optimization evidence?  
  **Expected:** reset trace, mode state, gradient/activation path, update behavior, output/loss contract.
- **Q:** Which evidence points instead to representation or data limits?  
  **Expected:** unchanged linear boundary, uninformative/mismatched features/labels, clean but weak validation, absent task signal.
- **Q:** Why not add layers immediately?  
  **Expected:** it does not test data validity or fix a broken loop and can worsen optimization/generalization.

### Visual steps

1. Show the Day 2 evidence table before the feature ladder.
2. Add feature stages one at a time.
3. Add a separate capacity/risk arrow so benefit and cost do not collapse into one axis.
4. Replace any "always detects" label with "can encode."

**Asset:** `courseware/shared/assets/day-3/feature-ladder.svg`  
**Alt-text intent:** Raw pixels progress to possible local, intermediate, and task-relevant representations while separate bars show rising capacity and optimization/generalization risk.

### Cut line

Cut initialization examples. Never cut the real Day 2 artifact retrieval or category distinction.

## 09:15-09:35 - LESSON-D3-02: Data Chain of Custody

**Objective:** `OBJ-D3-02`  
**Must land:** Validation may influence development choices but may not fit preprocessing/model parameters; prediction-time feature availability matters.

### Sequence

| Minute | Move |
|---:|---|
| 0-5 | Draw train/validation/test ownership and ask which arrow fits state. |
| 5-9 | Sort stateful/stateless transforms; separate training augmentation from evaluation transforms. |
| 9-13 | Add feature availability time and a post-outcome proxy. |
| 13-16 | Contrast stratification/shuffling with provenance. |
| 16-19 | Explain opt-in cached torchvision constructors. |
| 19-20 | Rank high-score explanations and launch D3-01. |

### Questions and expected answers

- **Q:** Why can validation influence a model choice but not scaler fitting?  
  **Expected:** validation estimates alternatives; fitting its values into state contaminates the evidence used to compare them.
- **Q:** Does shuffling remove a future feature?  
  **Expected:** no; order changes, availability does not.
- **Q:** Is applying a training-fitted scaler to validation leakage?  
  **Expected:** no; validation does not alter the fitted state.

### Visual steps

Use `data-provenance-leak-pipeline.svg`. Reveal the valid blue path first; then reveal red arrows for post-outcome feature and pre-split scaler fit. Do not reveal the repair before `ACT-D3-02` submissions.

### Cut line

Cut DataLoader syntax. Preserve ownership, availability time, and the prediction.

## 09:35-10:20 - LAB-D3-01 + ACT-D3-02: Find the Data Leak

**Participant notebook:** [courseware/day-3/labs/LAB-D3-01-find-data-leak.ipynb](../day-3/labs/LAB-D3-01-find-data-leak.ipynb)  
**Validated solution:** [courseware/instructor-solutions/day-3/LAB-D3-01-find-data-leak-SOLUTION.ipynb](../instructor-solutions/day-3/LAB-D3-01-find-data-leak-SOLUTION.ipynb)  
**Must land:** A lower valid score is better evidence than a contaminated high score.

### Launch script

"The score is a clue, not a verdict. Submit facts, alternatives, one check, confirming evidence, and disconfirming evidence before requesting pipeline code. We need two independent leak paths."

### Checkpoints

| Lab minute | Evidence checkpoint |
|---:|---|
| 7 | metric plausibility prediction and two hypotheses recorded |
| 14 | feature provenance/availability table audited |
| 20 | `ACT-D3-02` first gate accepted before code |
| 27 | pre-split scaler leak identified |
| 35 | valid split/preprocessing order implemented or recovered |
| 41 | leaky/repaired evidence compared under matched model |
| 45 | lower-score validity explanation and remaining risk submitted |

### Hint ladder

1. Separate creation time from correlation strength.
2. Ask whether each feature exists when the prediction must be made.
3. Ask which rows contributed to every fitted statistic.
4. Split first, then fit the scaler on training only.
5. Apply the fixed scaler to validation/test without refitting.
6. Confirm the proxy is absent from every split and model input.

### Expected evidence and alternatives

Planning bands from the lab map are leaky AUC `0.99-1.00` and valid AUC `0.78-0.90`; use only after execution calibration. Genuine strong signal, duplicate leakage, and an evaluation bug remain valid initial alternatives. Require an evidence item that distinguishes them.

### Recovery

- If generated-data setup fails, provide the validated provenance/metric table, not solution code.
- If split/scaler code blocks progress, provide a fixed pipeline skeleton after the learner submits the ownership order.
- If results differ materially, switch to calibrated precomputed tables and open a retest issue.

### Debrief

Ask: "What crossed the boundary? When did it become available? Why is the lower score more useful? What has not yet been validated?"

## 10:20-10:35 - Protected Break

Do not compress. Queue kernel arithmetic, shape tiles, cached Fashion-MNIST state, and D3-02 recovery evidence.

## 10:35-11:00 - LESSON-D3-03 + ACT-D3-03: Kernel and Shape Trace

**Objective:** `OBJ-D3-03`  
**Must land:** A convolution reuses a local detector across space; channels and spatial dimensions have distinct roles.

### Sequence

| Minute | Move |
|---:|---|
| 0-4 | Contrast flattened independent weights with local shared weights. |
| 4-12 | Run `ACT-D3-03`: predict shape/map, reveal one patch, then full map. |
| 12-17 | Build `(B,C,H,W)` trace through two conv/pool blocks. |
| 17-21 | Define channels, feature maps, padding, stride, pooling, receptive field, head. |
| 21-24 | State feature-map interpretation limit. |
| 24-25 | Launch D3-02. |

### Questions and expected answers

- **Q:** What is shared?  
  **Expected:** kernel weights across spatial locations.
- **Q:** What does pooling halve here?  
  **Expected:** height and width, not channels by default.
- **Q:** Does a bright map prove an edge caused the output?  
  **Expected:** no; it is descriptive and later paths remain.

### Visual steps

1. Use `kernel-feature-map-shape-trace.svg` for one patch and the full shape path.
2. Keep batch, channel, height, width colors fixed.
3. Use `cnn-map-hierarchy.svg` only after learners predict early/later map differences.
4. Label learned semantic roles as hypotheses.

### Cut line

Cut extended receptive-field arithmetic and pooling variants. Keep one kernel calculation and the full shape trace.

## 11:00-12:00 - LAB-D3-02: Compact CNN and Feature Maps

**Participant notebook:** [courseware/day-3/labs/LAB-D3-02-cnn-feature-maps.ipynb](../day-3/labs/LAB-D3-02-cnn-feature-maps.ipynb)  
**Validated solution:** [courseware/instructor-solutions/day-3/LAB-D3-02-cnn-feature-maps-SOLUTION.ipynb](../instructor-solutions/day-3/LAB-D3-02-cnn-feature-maps-SOLUTION.ipynb)  
**Must land:** Shapes and selected feature maps expose mechanics, but maps are not complete causal explanations.

### Launch script

"Confirm cache status before any download. Predict every shape before the forward pass. Repair the head from printed evidence, then train. Describe maps before assigning meanings."

### Checkpoints

| Lab minute | Evidence checkpoint |
|---:|---|
| 7 | cache/download choice and transform ownership recorded |
| 15 | complete `(B,C,H,W)` prediction committed |
| 23 | deliberate flattened/channel defect repaired from shape trace |
| 38 | bounded training completes or matched history is loaded |
| 47 | hooks capture and are removed; selected maps labeled by layer/shape |
| 54 | misclassifications inspected with true/predicted labels |
| 60 | descriptive claim, unsupported claim, and intervention submitted |

### Hint ladder

1. Print the input shape before the first layer.
2. Track channels separately from height/width.
3. Compute flatten count from the observed final activation, not memory.
4. Compare one early and one later channel for the same input.
5. Remove hooks after capture.
6. To test a proposed feature role, change the input feature while preserving a control.

### Planning evidence

The lab map targets a compact model below `250,000` parameters and validation accuracy broadly `0.80-0.88` after bounded training. These are sanity bands pending execution, not grading cutoffs.

### Recovery

- Cache missing/network blocked: use reduced packaged data or validated checkpoint/map bundle.
- Training slow: stop at ceiling and load matched curves/checkpoint.
- Hooks fail: use precomputed layer-labeled maps, then continue interpretation.
- Shape defect persists: supply the observed final activation shape, not the dense dimension answer.

### Debrief

Use `cnn-map-hierarchy.svg`. Ask which observations are descriptive, which semantic names are hypotheses, and what intervention could test one.

## 12:00-12:10 - CHECK-D3-01

Collect through **Day 3 Checks** before lunch. Use all 10 minutes.

Expected evidence: `(B,8,28,28) -> (B,8,14,14) -> (B,16,14,14) -> (B,16,7,7) -> (B,784)`; batch changes example dimension only; shared weights differ from local independent detectors; one descriptive map claim and one intervention.

Remediation:

- channel/spatial confusion: use dimension tiles after lunch;
- parameter-sharing weakness: compare parameter reuse at two locations;
- map-as-cause claim: require a controlled input edit.

## 12:10-13:10 - Protected Lunch

Do not compress. Preflight D3-03 cache/history, reset roles, and verify aligned baseline/intervention axes.

## 13:10-13:25 - LESSON-D3-04 + LESSON-D3-05: Curves and One Rescue

**Objectives:** `OBJ-D3-04`, `OBJ-D3-05`  
**Must land:** A curve supports a hypothesis, not a unique root cause; a rescue changes one major factor and must improve absolute held-out behavior, not only shrink a gap.

### Sequence

| Minute | Move |
|---:|---|
| 0-4 | Show hidden aligned curve cards; require two observations before labels. |
| 4-8 | Distinguish underfit, overfit, instability, and pipeline/mode alternatives. |
| 8-11 | Introduce generalization gap and the "both collapsed" counterexample. |
| 11-14 | Match one remedy to its expected curve mechanism. |
| 14-15 | Commit D3-03 baseline and rescue prediction. |

### Questions and expected answers

- **Q:** Train improves while validation worsens. What does this support?  
  **Expected:** overfitting/generalization concern, while split/mode/shift remain alternatives.
- **Q:** Is a smaller gap always better?  
  **Expected:** no; both metrics can be poor.
- **Q:** Why not combine dropout, augmentation, and weight decay?  
  **Expected:** the result cannot identify which mechanism mattered.

### Visual steps

Use `overfit-rescue-aligned-curves.svg`. Reveal baseline first, hide intervention label, collect predictions, then reveal aligned rescue. Keep the same axes and epoch budget.

### Cut line

Cut optimizer/scheduler survey. Preserve curve diagnosis, one mechanism card, and prediction.

## 13:25-14:20 - LAB-D3-03: Make It Overfit, Then Rescue It

**Participant notebook:** [courseware/day-3/labs/LAB-D3-03-overfit-and-rescue.ipynb](../day-3/labs/LAB-D3-03-overfit-and-rescue.ipynb)  
**Validated solution:** [courseware/instructor-solutions/day-3/LAB-D3-03-overfit-and-rescue-SOLUTION.ipynb](../instructor-solutions/day-3/LAB-D3-03-overfit-and-rescue-SOLUTION.ipynb)  
**Must land:** The baseline failure and one matched rescue produce a falsifiable before/after comparison.

### Launch script

"Draw the failure before running it. Mark the expected overfit onset. Select one rescue and predict both training and validation behavior. An unexplained score gain is weaker than a controlled negative result."

### Checkpoints

| Lab minute | Evidence checkpoint |
|---:|---|
| 8 | baseline curves and gap predicted |
| 20 | high-capacity/tiny-data baseline completed or loaded |
| 27 | overfit onset and two observations marked |
| 32 | exactly one intervention and rejection criterion accepted |
| 45 | matched intervention run completed or loaded |
| 51 | aligned overlay distinguishes validation gain from train collapse |
| 55 | mechanism, competing explanation, next experiment submitted |

### Hint ladder

1. Compare train and validation trends, not only final values.
2. Mark the minimum validation loss.
3. State what the selected remedy changes directly.
4. Keep seed, split, axes, and major budget fixed.
5. Inspect absolute validation and gap together.
6. For early stopping, compare restored best checkpoint with final checkpoint.

### Planning evidence

The map expects baseline train accuracy above `0.98`, validation `0.65-0.82`, and gap at least `0.15` under the calibrated setup. A useful rescue may reduce the gap around `0.05` or improve validation around `0.03`, but a well-diagnosed non-improvement is valid evidence.

### Recovery

- Baseline fails to overfit: use validated baseline history and record a calibration issue.
- Intervention exceeds time: load the matched history for the learner's chosen card.
- All-remedies branch chosen: return to one major factor before compute.
- Curves use different axes: replot or use the aligned fallback; do not compare visually misaligned charts.

### Debrief

Ask: "Did validation improve? Did the predicted mechanism appear? What alternative survives? What one experiment would separate it?"

## 14:20-14:35 - Protected Break

Do not compress. Confirm CIFAR10, weight, transform, and embedding-cache state for D3-04.

## 14:35-14:50 - LESSON-D3-06: Transfer Strategy

**Objective:** `OBJ-D3-06`  
**Must land:** Transfer reuses representation; freezing and pretraining are separate variables; domain match and resource constraints decide value.

### Sequence

| Minute | Move |
|---:|---|
| 0-4 | Compare scratch, frozen feature extraction, and fine-tuning. |
| 4-8 | Show backbone/head and total versus trainable parameters. |
| 8-11 | Reveal current weights enum and `weights.transforms()` contract. |
| 11-13 | Ask how random/frozen isolates pretraining. |
| 13-15 | Collect race predictions and launch D3-04. |

### Questions and expected answers

- **Q:** What is transferred?  
  **Expected:** learned feature transformations/representation, not target answers.
- **Q:** Is a frozen random backbone transfer learning?  
  **Expected:** no; it isolates freezing without pretrained features.
- **Q:** Why can transfer lose?  
  **Expected:** domain/transform mismatch, source bias, insufficient adaptation, or resource cost.

### Visual steps

Use `transfer-scoreboard.svg`: reveal the architecture/parameter contrast first, then hide scoreboard values until both paths are complete.

### Cut line

Cut full fine-tuning and unfreezing mechanics. Frozen feature extraction remains core.

## 14:50-15:45 - LAB-D3-04: Transfer-Learning Race

**Participant notebook:** [courseware/day-3/labs/LAB-D3-04-transfer-learning-race.ipynb](../day-3/labs/LAB-D3-04-transfer-learning-race.ipynb)  
**Validated solution:** [courseware/instructor-solutions/day-3/LAB-D3-04-transfer-learning-race-SOLUTION.ipynb](../instructor-solutions/day-3/LAB-D3-04-transfer-learning-race-SOLUTION.ipynb)  
**Must land:** The winner is conditional and must be explained with quality, time, transforms, trainable parameters, and domain evidence.

### Launch script

"Record cache, split, weight, transform, device, and budget before the race. Predict scratch and transfer separately. Verify frozen parameters. Compare pretrained/frozen with random/frozen before crediting pretraining."

### Checkpoints

| Lab minute | Evidence checkpoint |
|---:|---|
| 6 | cache/network route and metadata recorded |
| 13 | scratch/transfer predictions and fair-comparison contract committed |
| 24 | scratch baseline complete or matched evidence loaded |
| 31 | weight/transform identity and freeze verified |
| 40 | embeddings extracted/loaded and cache key inspected |
| 48 | head training and scoreboard completed |
| 53 | random-frozen/wrong-transform diagnosis recorded |
| 55 | conditional winner and serving caveat submitted |

### Hint ladder

1. Count `requires_grad=True` parameters separately from total parameters.
2. Record the weight enum before constructing the model.
3. Derive preprocessing from `weights.transforms()`.
4. Compare the same split and labels.
5. If frozen performance is weak, test pretrained versus random frozen before unfreezing.
6. Include weight, transforms, split, and package identity in the embedding cache key.

### Planning evidence

The lab map's broad bands are scratch validation `0.25-0.50` and frozen pretrained `0.45-0.70`. Exact winner is not promised. First CPU extraction targets under 12 minutes with cached reruns under 2 minutes; actual validated runtime controls delivery.

### Recovery

- Canonical CIFAR-10 or MobileNet unavailable: load packaged `transfer_surrogate_fashion_subset.npz` images/labels and `transfer_surrogate_embeddings.npz` label-blind 256-wide surrogate features.
- Display and record: **not CIFAR-10; not MobileNet output; not canonical metrics/runtime; not proof transfer wins**.
- Do not reference a CIFAR manifest, call this a pretrained fallback, or silently substitute random/generic pretrained weights.
- Canonical extraction slow: stop at the tested ceiling. Use a matching canonical cache only when its weight/transform/split metadata are validated; otherwise switch to the visibly labeled surrogate recovery route.
- Transfer loses: treat as evidence; inspect transforms/domain/control rather than declaring the lab broken.

### Debrief

Use the scoreboard. Ask what was transferred, what the random-frozen control isolates, and whether the training winner is also the serving choice.

## 15:45-16:05 - LESSON-D3-07 + LESSON-D3-08 + ACT-D3-04

**Objectives:** `OBJ-D3-07`, `OBJ-D3-08`  
**Must land:** Attention is context-dependent mixing inside the same training mechanics, not a complete causal explanation; scale introduces distinct resource and reliability constraints.

### Sequence

| Minute | Move |
|---:|---|
| 0-5 | Predict token relationships for **it** before Q/K/V labels. |
| 5-9 | Reveal illustrative token map and conceptual Transformer block. |
| 9-12 | Require three omitted paths and the attention limitation sentence. |
| 12-17 | Use memory/throughput/latency chart; make two scenario choices. |
| 17-20 | Map inputs/parameters/loss/gradients to the larger system and state scope limits. |

### Questions and expected answers

- **Q:** What does a large attention weight establish?  
  **Expected:** a strong mixture relation at that operation, not causal responsibility for final output.
- **Q:** What is omitted?  
  **Expected:** values, other heads/layers, residuals, later transforms, output head, alternatives.
- **Q:** Throughput rises while batch-1 latency worsens. Contradiction?  
  **Expected:** no; batching/concurrency can process more work while an individual request waits longer.
- **Q:** Does GPU availability prove utilization?  
  **Expected:** no; profile the declared workload and input/transfer/compute timeline.

### Visual steps

1. Use `token-relevance-limitation.svg`; hide weights until predictions are collected.
2. Add a visible "illustrative, not model output" label.
3. Overlay omitted residual/later routes after the initial map.
4. Use `memory-throughput-latency.svg` and change the scenario constraint between rounds.

### Scope protection

Attention equations, Transformer code, distributed algorithms, mixed precision, model parallelism, and quantization are `MOVE`. Full fine-tuning remains outside core. Do not use the final buffer to add them.

## 16:05-16:20 - CHECK-D3-02 through CHECK-D3-04

Use exactly five minutes per check. Collect each minimum live response through the cohort participant channel **Day 3 Checks** before the buffer. The additional-depth consolidation is a separate five-minute task due in that same channel before Day 4 at **09:00**; learners append to, rather than replace, their live responses.

| Check | Minimum live response that fits five minutes | Five-minute consolidation due before Day 4 at 09:00 |
|---|---|---|
| `CHECK-D3-02` | name the post-outcome feature and pre-split scaler leaks; give the repaired ownership order; explain why the lower honest score is better evidence | explain why shuffle/stratification do not repair the leaks; add one remaining validity question |
| `CHECK-D3-03` | diagnose from two curve observations; choose exactly one intervention; give its mechanism plus one confirming and one rejecting observation | add one competing explanation and explain why gap reduction without absolute held-out behavior is insufficient |
| `CHECK-D3-04` | choose a strategy using data/domain/time/trainable-parameter constraints; name the random-frozen control; correct the attention claim with one omitted route; correct the GPU claim with two measurements | add the switch result, serving caveat, a second omitted attention route, and Part C's claim -> evidence -> limitation -> highest-information next experiment chain |

At Day 4 opening, project three anonymized consolidation chains from **Day 3 Checks**: one strong chain, one chain with a weak limitation, and one chain with an unfocused next experiment. Learners retrieve their own original live response before revising the limitation or experiment. If a learner has no consolidation, use the guided four-column table before new content.

### Expected evidence snapshot

- D3-02: post-outcome feature plus pre-split scaler; valid order; lower honest score.
- D3-03: overfit evidence; one rescue; confirming and rejecting observations; gap caveat.
- D3-04: frozen pretrained baseline under stated constraints; random-frozen control; attention and GPU claim corrections; claim/evidence/limitation/next experiment.

### Assessment collection record

Capture:

- percent correctly separating Day 2 implementation/optimization from representation/data evidence;
- percent tracing CNN channel/spatial shapes and flatten count;
- percent identifying both leak paths;
- percent choosing exactly one rescue with rejection evidence;
- percent distinguishing frozen from pretrained;
- percent stating the attention causal limitation;
- percent separating latency, throughput, memory, and utilization;
- one Day 4 retrieval artifact based on actual Day 3 evidence.

### Remediation decisions

- **Leak weak:** use a six-card ownership order at Day 4 opening before metrics.
- **Curve weak:** require train and validation observations before bias/variance labels.
- **Transfer universalized:** compare random/frozen and domain-mismatch cases.
- **Attention overclaim:** ask what value/residual routes are omitted.
- **Resource terms conflated:** restate one interactive and one offline scenario.

## 16:20-16:30 - Protected Buffer and Day 4 Bridge

Use only for a blocked core debrief, must-land question, or clean close. Do not add optional unfreezing, attention equations, or distributed systems.

Close with:

> "Today you learned that a higher score can be less trustworthy, a deeper model can generalize worse, transfer can lose, and a resource winner depends on the constraint. Tomorrow every model claim must name the metric, slice, cost, experiment, and limitation that support it."

Participants bring `CHECK-D3-04` Part C in **claim -> evidence -> limitation -> highest-information next experiment** form.

### Outstanding operational recommendation

An uninterrupted 450-minute novice rehearsal has not been run. Keep it as an accepted nonblocking recommendation: record completion times, help events, debrief quality, check completion, and whether the five-minute consolidation is workable. Do not report novice timing as validated until that rehearsal exists.

---

# Cross-Block Facilitation Notes

## Misconception Routing Table

| Symptom | Likely misconception | Cheapest question | Route |
|---|---|---|---|
| adds depth to a broken loop | capacity treated as universal fix | "Which invariant says the current loop is valid?" | Day 2 evidence category table |
| celebrates `0.997` immediately | score detached from provenance | "When did each feature become available?" | `ACT-D3-02` |
| says stratification prevents leakage | class balance confused with ownership | "Who fitted the scaler?" | D3-01 lineage |
| swaps batch and channel | image shape weak | "Which dimension indexes examples?" | `ACT-D3-03` tiles |
| calls map a detector/cause | activation description overclaimed | "What intervention tests that role?" | D3-02 debrief |
| treats smaller gap as success | gap detached from absolute behavior | "What if both accuracies are 0.5?" | D3-03 aligned curves |
| combines every remedy | intervention is not controlled | "Which change caused the result?" | one-rescue gate |
| says frozen equals pretrained | variables conflated | "What happens with random frozen weights?" | D3-04 control |
| says transfer always wins | domain/budget ignored | "What target differs from the source?" | transfer scoreboard |
| says attention explains cause | one weight treated as full path | "What did values/residuals/later layers do?" | `ACT-D3-04` limitation |
| says GPU means fast | availability treated as utilization | "Where is time spent end to end?" | resource chart |

## Day 4 Bridge Evidence

Prefer retrieval artifacts that contain:

1. a bounded claim;
2. named data/split/comparison evidence;
3. an explicit alternative or limitation;
4. one experiment chosen to distinguish alternatives.

Do not select only the highest score. A repaired lower score or failed controlled rescue can be the stronger Day 4 bridge.

## Scope Protection Summary

### Core

- Day 2 evidence retrieval and depth/capacity distinction;
- valid split/provenance/preprocessing ownership;
- CNN locality, sharing, shapes, maps, and interpretation caveat;
- aligned training/validation curves;
- one overfit rescue;
- frozen-feature transfer comparison and current weight/transform contract;
- conceptual Q/K/V and Transformer/foundation-model connection;
- memory/throughput/latency/utilization/reliability trade-offs.

### First items to shorten

- initialization and optimizer/scheduler catalogues;
- extra receptive-field arithmetic;
- extra feature-map channels/misclassifications;
- augmentation/remedy catalogue examples;
- transform implementation details beyond the current contract.

### Optional or moved only

- partial unfreezing after a valid frozen baseline;
- full fine-tuning;
- attention equations and Transformer implementation;
- distributed-training algorithms;
- mixed precision, model parallelism, quantization, and deep interpretability methods.
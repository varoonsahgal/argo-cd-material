# Day 2 Instructor Guide: Train It

**Instructor only. Do not distribute with participant materials.**

**Canonical question:** When a neural network makes a mistake, how does it know what to change?  
**Day outcome:** Participants train the same small network from scratch and in PyTorch, then diagnose broken runs from evidence before changing code.  
**Must-land sentence:** **Forward propagation makes the prediction; backpropagation carries sensitivity backward; the optimizer turns that sensitivity into a parameter change.**

## Controlling Artifacts

- Participant guide: [courseware/day-2/student-guide/day-2-student-guide.md](../day-2/student-guide/day-2-student-guide.md)
- Participant challenges: [courseware/day-2/challenges/day-2-challenges.md](../day-2/challenges/day-2-challenges.md)
- Challenge key: [courseware/instructor-solutions/day-2/day-2-challenges-SOLUTION.md](../instructor-solutions/day-2/day-2-challenges-SOLUTION.md)
- Participant checks: [courseware/day-2/assessments/day-2-checks.md](../day-2/assessments/day-2-checks.md)
- Check key: [courseware/instructor-solutions/day-2/day-2-checks-SOLUTION.md](../instructor-solutions/day-2/day-2-checks-SOLUTION.md)
- Slide source: [courseware/slides/day-2-train-it.md](../slides/day-2-train-it.md)
- Shared glossary: [courseware/shared/glossary.md](../shared/glossary.md)
- Shared notation: [courseware/shared/notation-and-style.md](../shared/notation-and-style.md)
- Shared environment: [courseware/shared/environment.md](../shared/environment.md)

## Objective and Evidence Map

| Objective | Must observe | Practice | Check |
|---|---|---|---|
| `OBJ-D2-01` | Day 1 trace placed inside initialize/forward/loss/backward/update/repeat | loop tracing in `LAB-D2-03`, `LAB-D2-04` | `CHECK-D2-01` |
| `OBJ-D2-02` | output/loss contract and equal-accuracy/different-loss evidence | `ACT-D2-01`, `LAB-D2-01`, `LAB-D2-04` | `CHECK-D2-01` |
| `OBJ-D2-03` | update direction and crawl/converge/oscillate/diverge evidence | `ACT-D2-02`, `LAB-D2-01`, `LAB-D2-03` | `CHECK-D2-02` |
| `OBJ-D2-04` | local derivative times upstream gradient plus numerical agreement | `LAB-D2-02`, `LAB-D2-03` | `CHECK-D2-02` |
| `OBJ-D2-05` | batch dimension, contraction, broadcasting, shape repair | `ACT-D2-03`, `LAB-D2-03`, `LAB-D2-04` | `CHECK-D2-03` |
| `OBJ-D2-06` | complete NumPy responsibilities emit curves and boundary evidence | `LAB-D2-03` | `CHECK-D2-03` |
| `OBJ-D2-07` | PyTorch calls mapped to NumPy mechanics; mode/grad states separated | `LAB-D2-04` | `CHECK-D2-04` |
| `OBJ-D2-08` | symptom -> alternatives -> discriminating check -> repair -> evidence | `ACT-D2-04`, `LAB-D2-04` | `CHECK-D2-04` |

## Exact 450-Minute Schedule

| Time | Min | Mode and canonical IDs | Scope |
|---|---:|---|---|
| 09:00-09:20 | 20 | Retrieve/explain: `LESSON-D2-01` | `CORE` |
| 09:20-09:45 | 25 | Predict/calculate: `LESSON-D2-02`, `ACT-D2-01` | `CORE`; shorten log-likelihood depth first |
| 09:45-10:25 | 40 | Visualize/experiment: `LAB-D2-01` | `CORE` |
| 10:25-10:40 | 15 | Break | Protected |
| 10:40-11:10 | 30 | Explain/visualize: `LESSON-D2-03`, `ACT-D2-02` | `CORE`; extended graph branches are `SHORTEN` |
| 11:10-11:55 | 45 | Experiment/diagnose: `LAB-D2-02` | `CORE` |
| 11:55-12:05 | 10 | Assess: `CHECK-D2-01`, `CHECK-D2-02` | `CORE` |
| 12:05-13:05 | 60 | Lunch | Protected |
| 13:05-13:25 | 20 | Shape map/predict: `LESSON-D2-04`, `ACT-D2-03` | `CORE`; hardware detail is `SHORTEN` |
| 13:25-14:35 | 70 | Build/observe: `LESSON-D2-05`, `LAB-D2-03` | `CORE`; activation/width sweep is `OPTIONAL` |
| 14:35-14:50 | 15 | Break | Protected |
| 14:50-15:10 | 20 | Compare/explain: `LESSON-D2-06` | `CORE`; device nuance is `SHORTEN` |
| 15:10-16:05 | 55 | Break/fix/diagnose: `LESSON-D2-07`, `LAB-D2-04`, `ACT-D2-04` | `CORE`; extra fault is `OPTIONAL` |
| 16:05-16:20 | 15 | Transfer/assess: `LESSON-D2-08`, `CHECK-D2-03`, `CHECK-D2-04` | `CORE` |
| 16:20-16:30 | 10 | Recovery/questions/close | Protected; no new content |

Total: `20+25+40+15+30+45+10+60+20+70+15+20+55+15+10 = 450` minutes.

## PyTorch 2.11 Source Grounding

The package is written against official PyTorch 2.11 semantics. Keep these claims narrow.

| Claim | Status and source | Teaching implication |
|---|---|---|
| `BCEWithLogitsLoss` combines sigmoid and BCE with a numerically stable formulation; input and target have the same shape | Verified for 2.11: [official loss documentation](https://docs.pytorch.org/docs/2.11/generated/torch.nn.BCEWithLogitsLoss.html) | binary model emits logits; apply sigmoid only for interpretation/thresholding |
| canonical optimizer loop is reset -> forward -> loss -> backward -> step | Verified for 2.11: [official optimizer documentation](https://docs.pytorch.org/docs/2.11/optim.html#taking-an-optimization-step) | map each call to a NumPy responsibility; `backward()` does not update |
| `optimizer.zero_grad()` resets optimized gradients; its 2.11 default is `set_to_none=True`, so `None` differs from zero | Verified/qualified for 2.11: [official zero-grad documentation](https://docs.pytorch.org/docs/2.11/generated/torch.optim.Optimizer.zero_grad.html) | use the lab's plain call; handle `None` in gradient inspection; make no universal performance claim |
| `model.eval()` affects only modules with train/evaluation-specific behavior and equals `train(False)` | Verified for 2.11: [official Module documentation](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Module.html#torch.nn.Module.eval) | set evaluation mode and later restore training mode |
| evaluation mode is orthogonal to no-grad/inference mode | Verified for 2.11: [official autograd mechanics](https://docs.pytorch.org/docs/2.11/notes/autograd.html#evaluation-mode-nn-module-eval) | ask mode state and gradient-recording state as separate questions |
| inference mode disables autograd recording with additional tracking savings and tensor-reuse restrictions; `torch.no_grad()` is the less restrictive alternative | Verified/qualified for 2.11: [no-grad documentation](https://docs.pytorch.org/docs/2.11/generated/torch.no_grad.html), [autograd grad modes](https://docs.pytorch.org/docs/2.11/notes/autograd.html#grad-modes) | use the lab's inference context for isolated evaluation; teach `no_grad()` as the reusable-output alternative |

Do not claim that a GPU is required, always faster, or commonly used in a particular way. CPU is the required path. Device/performance statements require a declared workload and measurement.

## Before Class

### Lab and solution preflight

Open each participant notebook from a clean kernel, then pre-run its future instructor solution. These notebooks are dependencies owned by the Lab Engineer/Lab Solution Engineer and are not created by this narrative package.

| Lab | Participant path | Future instructor solution path |
|---|---|---|
| `LAB-D2-01` | [courseware/day-2/labs/LAB-D2-01-loss-learning-rate.ipynb](../day-2/labs/LAB-D2-01-loss-learning-rate.ipynb) | [courseware/instructor-solutions/day-2/LAB-D2-01-loss-learning-rate-SOLUTION.ipynb](../instructor-solutions/day-2/LAB-D2-01-loss-learning-rate-SOLUTION.ipynb) |
| `LAB-D2-02` | [courseware/day-2/labs/LAB-D2-02-backprop-gradient-check.ipynb](../day-2/labs/LAB-D2-02-backprop-gradient-check.ipynb) | [courseware/instructor-solutions/day-2/LAB-D2-02-backprop-gradient-check-SOLUTION.ipynb](../instructor-solutions/day-2/LAB-D2-02-backprop-gradient-check-SOLUTION.ipynb) |
| `LAB-D2-03` | [courseware/day-2/labs/LAB-D2-03-numpy-training.ipynb](../day-2/labs/LAB-D2-03-numpy-training.ipynb) | [courseware/instructor-solutions/day-2/LAB-D2-03-numpy-training-SOLUTION.ipynb](../instructor-solutions/day-2/LAB-D2-03-numpy-training-SOLUTION.ipynb) |
| `LAB-D2-04` | [courseware/day-2/labs/LAB-D2-04-pytorch-break-fix.ipynb](../day-2/labs/LAB-D2-04-pytorch-break-fix.ipynb) | [courseware/instructor-solutions/day-2/LAB-D2-04-pytorch-break-fix-SOLUTION.ipynb](../instructor-solutions/day-2/LAB-D2-04-pytorch-break-fix-SOLUTION.ipynb) |

Confirm before delivery:

1. The intended participant and solution execution gates have passed; planning bands are not substitutes for test reports.
2. The same seeded moons split specification is used in D2-03 and D2-04.
3. D2-04 emits logits and uses `BCEWithLogitsLoss` with exact target shape.
4. D2-04 mystery evidence appears before faulty source.
5. Gradient inspection handles `None` after the plain 2.11 `zero_grad()` call, whose documented default is `set_to_none=True`.
6. CPU is usable; any optional device branch records the device and preserves required evidence.

### Fallback evidence to prepare

- equal-accuracy/different-loss table;
- four learning-rate paths on fixed axes;
- computational graph with forward/backward labels;
- analytic/numeric gradient table including two defect patterns;
- batch shape map for `B = 1, 32, 1,024`;
- NumPy training curves plus nonlinear/no-activation boundaries;
- NumPy/PyTorch responsibility map;
- three non-unique mystery evidence cards and repaired before/after panels.

Fallbacks support interpretation when execution fails; they do not turn an untested notebook into a passing artifact.

### Pair roles

- **Driver:** edits and runs the current notebook section.
- **Evidence lead:** records prediction, invariant, and before/after evidence.
- In teams of three, add a **shape/gradient checker** who states expected dimensions or signs before execution.
- Swap roles at the midpoint of every lab.

## Operational Pacing Routes

### If behind

1. Cut full negative-log-likelihood derivation, additional graph branches, GPU hardware detail, NumPy width/activation sweep, device-management nuance, and extra D2-04 fault cards in that order.
2. Switch to validated precomputed evidence after one bounded recovery attempt.
3. Preserve every pre-run commitment, D2-02 gradient check, D2-03 core loop, D2-04 evidence-before-code gate, debriefs, checks, breaks, lunch, and final buffer.
4. Never use the final buffer for optional optimizer, reinforcement-learning, or hardware content.

### If ahead

1. Ask for one disconfirming observation before a proposed repair.
2. Give a new architecture and require batch/parameter/target shapes.
3. Ask participants to map one PyTorch line to the NumPy cache or mutation it replaces.
4. Allow one additional D2-04 evidence request, not a second random repair.
5. Do not begin Day 3 depth, normalization, or generalization content.

### Generic recovery ladder

1. **Visual interaction fails:** use static staged frames and preserve prediction/reveal order.
2. **One cell fails:** inspect one discriminating invariant, then switch to validated cached output.
3. **Environment fails:** pair with a working run; affected learner becomes evidence lead.
4. **Training exceeds ceiling:** stop the run; use a matched precomputed curve/boundary and continue diagnosis.
5. **Evidence differs materially from the planned band:** do not invent a new explanation; use validated fallback and record a retest issue.

---

# Facilitation Runbook

## 09:00-09:20 - LESSON-D2-01: Retrieve the Forward Trace, Add the Loop

**Objective:** `OBJ-D2-01`  
**Must land:** The Day 1 forward trace is the forward portion of training; loss, backward sensitivities, update, and repetition are new.

### Sequence

| Minute | Move |
|---:|---|
| 0-3 | Learners open their submitted Day 1 consolidation. Sample one response without allowing edits first. |
| 3-8 | Reconstruct `X -> Z1 -> A1 -> Z2 -> p -> class`; require one shape/range/invariant per stage. |
| 8-13 | Ask which Day 1 arrow changed parameters. Add target/loss/backward/update to the same board. |
| 13-17 | Tile examples into mini-batches; count iteration versus epoch. |
| 17-20 | Contrast training, evaluation, and target-free inference; state the day's question. |

### Required Day 1 retrieval sample

Select one submitted response from `CHECK-D1-03` item 5 or `CHECK-D1-04` items 2/5. A strong sample cites evidence, not only a conclusion. Ask the room to add a second-color revision after discussion.

### Questions and answers

- **Q:** Which stages use the target?  
  **Expected:** loss/evaluation comparison; the forward model itself consumes inputs, not targets.
- **Q:** Does `backward` change parameters?  
  **Expected:** no; it calculates/populates gradients. The update stage changes parameters.
- **Q:** Is one epoch one update?  
  **Expected:** only in full-batch training; mini-batch epochs contain multiple iterations.
- **Q:** Can evaluation calculate a loss without training?  
  **Expected:** yes; fixed outputs can be compared with targets without backward/update.

### Visual/demo procedure

1. Reveal the Day 1 trace first with forward arrows only.
2. Add target and scalar loss.
3. Add backward arrows with a different color.
4. Add update only after gradients exist.
5. Close the loop to the next batch.

**Alt-text intent:** A Day 1 forward trace becomes one segment of a six-stage repeated training loop.

### Cut line

Cut extra stochastic/full-batch examples. Never cut the submitted-response sample or forward-trace reconstruction.

## 09:20-09:45 - LESSON-D2-02 + ACT-D2-01: Loss and Learning Rate

**Objectives:** `OBJ-D2-02`, `OBJ-D2-03`  
**Must land:** Loss supplies a scalar optimization signal; accuracy answers a different question; learning rate scales local sensitivity.

### Sequence

| Minute | Move |
|---:|---|
| 0-3 | State why a scalar objective is needed. Do not show BCE yet. |
| 3-7 | Run `ACT-D2-01`: rank A-D and record accuracy; collect the snapshot by 09:27. |
| 7-10 | Pair defense while evidence remains hidden. |
| 10-15 | Reveal classes, per-example loss, then means. Use C versus B as counterintuitive comparison. |
| 15-19 | Match regression/binary/multiclass tasks to output/loss contracts. |
| 19-23 | Introduce gradient as local sensitivity and update rule. |
| 23-25 | Commit learning-rate trajectory predictions; launch D2-01. |

### Questions and answers

- **Q:** Can lower-accuracy C have lower loss than B?  
  **Expected:** yes; C is strong on three and only slightly wrong on one, while B is hesitant on all four.
- **Q:** Why logits into `BCEWithLogitsLoss`?  
  **Expected:** it combines sigmoid and BCE stably; do not sigmoid twice.
- **Q:** Does lower training loss mean better deployment behavior?  
  **Expected:** no; validation, costs/slices, calibration, and validity remain.
- **Q:** What determines update size?  
  **Expected:** gradient magnitude and learning rate together.

### Misconceptions

- loss and accuracy should rank models identically;
- BCE requires probabilities in PyTorch's logits-combined loss;
- confident output is inherently better;
- one numeric learning rate has a universal label.

### Cut line

Cut full NLL derivation and extra task types. Keep A/B/C/D reveal and logits/loss pairing.

## 09:45-10:25 - LAB-D2-01: Loss Landscapes and Learning-Rate Roulette

**Participant notebook:** [courseware/day-2/labs/LAB-D2-01-loss-learning-rate.ipynb](../day-2/labs/LAB-D2-01-loss-learning-rate.ipynb)  
**Instructor solution:** [courseware/instructor-solutions/day-2/LAB-D2-01-loss-learning-rate-SOLUTION.ipynb](../instructor-solutions/day-2/LAB-D2-01-loss-learning-rate-SOLUTION.ipynb)  
**Must land:** Path evidence distinguishes crawl, smooth convergence, oscillatory convergence, and divergence.

### Launch script

"Retrieve your loss ranking. Sketch the first three updates for each hidden rate before running. Keep axes fixed and classify only after seeing whether distance and loss shrink or grow."

### Checkpoints

| Lab minute | Evidence checkpoint |
|---:|---|
| 7 | BCE ranking reconciled with accuracy |
| 14 | finite extreme-probability loss implementation |
| 20 | all four first-three-step predictions recorded |
| 29 | trajectories plotted on fixed scales with divergence visible |
| 35 | path classification cites update sign/magnitude |
| 40 | debrief identifies one non-unique observation |

### Hint ladder

1. Calculate the gradient sign at the start.
2. Substitute the sign into `theta_next = theta - eta * gradient`.
3. Compare successive distance from the known minimum.
4. Compare loss envelope, not only alternating direction.
5. For BCE extremes, inspect `log(0)` and use the notebook's bounded stability strategy.

### Planning evidence

Under the lab map's chosen quadratic: `0.01` crawls, `0.10` converges smoothly, `0.90` oscillates while converging, and `1.10` diverges. Treat these labels as local to this objective.

### Debrief

Ask: "Which label required the whole path? Why did equal accuracy hide loss? What would make a numeric learning-rate recommendation transferable?"

### Recovery

If plotting fails, reveal a trajectory table one step at a time. If divergence stretches axes, use a fixed main panel plus an off-scale inset; do not autoscale it away.

## 10:25-10:40 - Protected Break

Do not compress. Queue the computational graph and gradient-check table.

## 10:40-11:10 - LESSON-D2-03 + ACT-D2-02: Backpropagation

**Objective:** `OBJ-D2-04`  
**Must land:** Backpropagation composes local derivative times upstream gradient and reuses work; it is not an unchanged error signal.

### Sequence

| Minute | Move |
|---:|---|
| 0-4 | Perturb one value numerically before introducing derivative notation. |
| 4-10 | Work `u=2w`, `q=u+1`, `L=q^2` forward; predict backward signs. |
| 10-16 | Reveal local derivatives one edge at a time; multiply along the path. |
| 16-18 | Show one branch and add contributions conceptually. |
| 18-26 | Run the full 8-minute `ACT-D2-02`: retrieve numeric trajectories, complete signs, and revise. |
| 26-30 | Introduce centered finite difference as an independent check; launch D2-02. |

### Questions and answers

- **Q:** Does backpropagate send the scalar loss backward unchanged?  
  **Expected:** no; each node combines upstream sensitivity with its local derivative.
- **Q:** Why add contributions at a branch?  
  **Expected:** the shared value affects loss through multiple downstream paths.
- **Q:** What can gradient agreement prove?  
  **Expected:** supports local derivative implementation at tested values; not data/model usefulness.

### Visual/demo procedure

1. Draw forward values above edges.
2. Ask sign before magnitude for each backward edge.
3. Draw upstream gradients below edges.
4. Keep numeric labels even when color/width shows sign/magnitude.
5. Add numeric gradient only after analytic values are committed.

### Cut line

Cut extra branches and symbolic expansion. Keep one complete path and finite-difference purpose.

## 11:10-11:55 - LAB-D2-02: Backpropagation and Gradient Check

**Participant notebook:** [courseware/day-2/labs/LAB-D2-02-backprop-gradient-check.ipynb](../day-2/labs/LAB-D2-02-backprop-gradient-check.ipynb)  
**Instructor solution:** [courseware/instructor-solutions/day-2/LAB-D2-02-backprop-gradient-check-SOLUTION.ipynb](../instructor-solutions/day-2/LAB-D2-02-backprop-gradient-check-SOLUTION.ipynb)  
**Must land:** The analytic backward pass is testable against finite differences; defect patterns are structured evidence.

### Launch script

"Predict signs before values. Fill the analytic column before running finite differences. If the check fails, inspect whether the mismatch is sign-only, shared across a layer, or consistent with one missing factor."

### Checkpoints

| Lab minute | Evidence checkpoint |
|---:|---|
| 8 | forward cache and shapes verified |
| 16 | selected gradient signs committed |
| 25 | analytic table completed |
| 32 | numerical table and relative error generated |
| 38 | sign-bug/missing-factor pattern diagnosed |
| 43 | one negative-gradient update tested |
| 45 | limitation of gradient checking stated |

### Hint ladder

1. Start at scalar loss and identify the immediate parent.
2. Write the upstream gradient entering the node.
3. Multiply by the node's local derivative.
4. Match each gradient's shape with its parameter.
5. Perturb only one parameter for the numeric check.
6. If all values are wrong by a similar factor, inspect a shared local derivative.

### Planning evidence

Correct selected gradients should have relative error below `1e-5` under the supplied float64 graph; faulty paths should exceed `1e-2`. These are lab-specific calibration targets, not universal thresholds.

### Debrief

Ask: "Why does one perturbation test the whole chain? What does agreement not validate? When could epsilon make the result misleading?"

### Recovery

If manual arithmetic blocks progress, provide the completed forward cache but not backward values. If numeric check code fails, use the precomputed signed table and preserve diagnosis.

## 11:55-12:05 - CHECK-D2-01 and CHECK-D2-02

Use exactly 5 minutes per check. Collect both through **Day 2 Checks** before lunch.

### Expected evidence snapshot

- D2-01: causal loop order; 15 updates for `960/64`; raw logits into `BCEWithLogitsLoss`; sigmoid after for interpretation.
- D2-02: shrinking versus growing oscillation; forward values `6,4,16`; local derivatives `8,1,3`; combined gradient `24`; update decreases `w`.

### Remediation decisions

- If more than one-third place `step()` before `backward()`, begin PyTorch reveal with a parameter-before/after probe.
- If local derivatives are added rather than multiplied, revisit one path only.
- If finite difference is treated as training, compare required forward evaluations per parameter.
- If output/loss pairing is weak, keep a logits/probability/loss three-column board visible in the afternoon.

## 12:05-13:05 - Protected Lunch

Do not compress. Preflight D2-03, verify expected initial-loss/boundary fallback, and check the same-shape target contract.

## 13:05-13:25 - LESSON-D2-04 + ACT-D2-03: Vectorization and Batch Shapes

**Objective:** `OBJ-D2-05`  
**Must land:** Batch adds an example dimension; the per-example function and parameter shapes remain the same.

### Sequence

| Minute | Move |
|---:|---|
| 0-4 | Retrieve Day 1 batch-versus-parameter distinction. |
| 4-7 | Run `ACT-D2-03` shape map for `B=1,32,1024`; collect the original commitment by 13:12. |
| 7-13 | Reveal contraction and bias broadcasting one dimension at a time. |
| 13-17 | Diagnose hand-written `(B,1)` versus `(B,)` broadcasting; collect the revised map at 13:23 and contrast the BCE same-shape contract. |
| 17-20 | State bounded accelerator rationale; launch D2-03. |

### Questions and answers

- **Q:** Which shapes change with `B`?  
  **Expected:** example-carrying arrays; not trainable arrays.
- **Q:** Why can `(B,1)` and `(B,)` be dangerous in hand-written elementwise code?  
  **Expected:** unintended pairwise expansion; assert exact shape.
- **Q:** Does vectorization guarantee GPU speedup?  
  **Expected:** no; measure declared workload/device/data movement.

### Cut line

Cut GPU architecture detail. Preserve three batch sizes and semantic shape hazard.

## 13:25-14:35 - LESSON-D2-05 + LAB-D2-03: NumPy Training

**Participant notebook:** [courseware/day-2/labs/LAB-D2-03-numpy-training.ipynb](../day-2/labs/LAB-D2-03-numpy-training.ipynb)  
**Instructor solution:** [courseware/instructor-solutions/day-2/LAB-D2-03-numpy-training-SOLUTION.ipynb](../instructor-solutions/day-2/LAB-D2-03-numpy-training-SOLUTION.ipynb)  
**Must land:** Every training responsibility emits an invariant; decreasing loss alone does not prove representation, correctness, or generalization.

### Launch script

"Use the responsibility checklist. Predict initial loss, every shape, and the boundary family before implementation. Stop on non-finite values. Complete one controlled comparison only after the baseline evidence is recorded."

### Checkpoints

| Lab minute | Evidence checkpoint |
|---:|---|
| 10 | split/seed and parameter shapes recorded |
| 20 | forward cache and initial-loss prediction reconciled |
| 31 | gradient shapes/finite norms verified |
| 41 | one update moves a copied parameter as predicted |
| 52 | mini-batch loop produces aligned curves |
| 61 | nonlinear boundary and validation evidence inspected |
| 66 | one controlled comparison complete or precomputed evidence loaded |
| 70 | optimization/representation/generalization debrief submitted |

### Hint ladder

1. Write shape beside each parameter and cache.
2. Test one example, then compare with one batch row.
3. Verify output/target exact shape before loss.
4. Match each gradient shape to its parameter.
5. Apply one update to copied parameters and recalculate loss.
6. Stop on `NaN`/`inf`; inspect input, log argument, gradient, and update magnitude in that order.
7. Compare no-activation and nonlinear boundaries under matched settings.

### Planning evidence

- initial BCE broadly near `0.69` under the supplied initialization;
- final training loss generally below `0.35`;
- train/validation accuracy generally `0.85-0.95`;
- visible nonlinear decision region.

Use only after lab execution calibration. Range misses are diagnostic, not automatic learner failure.

### Debrief

Ask teams to place one observation in each column: optimization, representation, generalization. Require one alternative explanation and one disconfirming check.

### Failure recovery

- **Forward blocked:** provide a shape-correct forward/cache shell; learner keeps predictions and implements loss/backward.
- **Backward blocked:** provide validated gradients only after the learner predicts shapes/signs; continue update/curve interpretation.
- **Training slow:** load cached aligned curves and boundary; preserve one-change diagnosis.
- **Loss non-finite:** stop rather than clipping blindly; inspect where non-finite values first appear.

### Cut line

Cut optional width/activation sweep. Preserve baseline, one update probe, curves, boundary, and debrief.

## 14:35-14:50 - Protected Break

Do not compress. Queue side-by-side code and D2-04 evidence cards without opening faulty source.

## 14:50-15:10 - LESSON-D2-06: PyTorch Automation Reveal

**Objective:** `OBJ-D2-07`  
**Must land:** PyTorch automates derivative/parameter bookkeeping; objective choice, modes, data validity, and diagnosis remain explicit responsibilities.

### Sequence

| Minute | Move |
|---:|---|
| 0-6 | Map NumPy arrays/functions to `nn.Module`, logits, loss, autograd, optimizer. |
| 6-10 | Reveal `zero_grad -> forward -> loss -> backward -> step`; probe parameters around backward/step. |
| 10-14 | Explain logits into `BCEWithLogitsLoss`; sigmoid only for interpretation. |
| 14-18 | Separate `model.eval()` from `torch.inference_mode()` with two independent state indicators; name `no_grad()` as the reusable-output alternative. |
| 18-20 | Qualify `set_to_none` and device claims; launch D2-04. |

### Demo procedure

1. Print one parameter copy.
2. Run forward/loss/backward; show gradient exists and parameter is unchanged.
3. Run `step()`; show parameter changed.
4. Call the lab's plain `zero_grad()`; show selected `.grad is None` under the documented 2.11 default before next backward.
5. Print `model.training` and `torch.is_grad_enabled()` in four combinations to establish orthogonality.

### Questions and answers

- **Q:** What does `backward()` automate?  
  **Expected:** reverse-mode derivative calculation/accumulation through the current graph.
- **Q:** What does `step()` need first?  
  **Expected:** gradients.
- **Q:** Does `eval()` turn off gradients?  
  **Expected:** no.
- **Q:** Why can plain `zero_grad()` produce `None` in 2.11?  
  **Expected:** its documented default is `set_to_none=True`; `None` differs from zero. Do not claim universal superiority.

### Cut line

Cut device-management examples and extended grad-context depth. Never cut mode/grad orthogonality or the one-sentence no-grad alternative.

## 15:10-16:05 - LESSON-D2-07 + LAB-D2-04 + ACT-D2-04

**Participant notebook:** [courseware/day-2/labs/LAB-D2-04-pytorch-break-fix.ipynb](../day-2/labs/LAB-D2-04-pytorch-break-fix.ipynb)  
**Instructor solution:** [courseware/instructor-solutions/day-2/LAB-D2-04-pytorch-break-fix-SOLUTION.ipynb](../instructor-solutions/day-2/LAB-D2-04-pytorch-break-fix-SOLUTION.ipynb)  
**Must land:** No source reveal before an evidence-only diagnosis with alternatives and a discriminating check.

### Launch script

"Build and verify the valid baseline first. Your mystery card is not a unique fingerprint. Submit observations, two hypotheses, one discriminating check, confirming evidence, and disconfirming evidence before requesting source. One targeted repair; matched rerun."

### Checkpoints

| Lab minute | Evidence checkpoint |
|---:|---|
| 10 | logits/loss/target contract and loop order mapped |
| 19 | valid baseline and evaluation state recorded |
| 26 | mystery evidence read; source still hidden |
| 33 | `ACT-D2-04` evidence-only gate accepted |
| 38 | one requested evidence item revealed |
| 44 | source inspected and one fault identified |
| 50 | one repair rerun under matched conditions |
| 55 | evidence board and mechanism explanation complete |

### Hint ladder

1. Separate observations from inferred causes.
2. Name another cause that could create the same curve.
3. Ask which state/value can be inspected without changing training.
4. Check output/loss/target shape and range.
5. Check gradients around reset/backward.
6. Check `model.training` and grad-enabled state separately.
7. Check hidden activation/boundary family before adding capacity.

### Mystery routing

| Card | Leading route | Competing route | Cheapest check |
|---|---|---|---|
| A: stalls near linear baseline, finite gradients | missing nonlinearity/effectively linear representation | low rate or weak signal | inspect activation path and matched nonlinear boundary |
| B: growing gradient norms/jagged loss | omitted reset | excessive rate | inspect gradient state before/after reset/backward |
| C: inconsistent repeated validation with mode-sensitive module | evaluation left in train mode | stochastic data/state | inspect `model.training`, fixed-batch repeats, then grad state separately |

### Debrief

Ask in order:

1. Which observation was fact rather than diagnosis?
2. Which evidence eliminated an alternative?
3. Which invariant did the repair restore?
4. What judgment did PyTorch not automate?
5. What monitoring evidence could catch this earlier?

### Recovery

- Never reveal a solution notebook to repair participant setup.
- If baseline fails, provide a validated baseline state and continue the mystery from cached evidence.
- If the assigned faulty preset does not reproduce, switch to its precomputed evidence card and record a retest issue.
- If time is lost, use one fault per team and a shared jigsaw debrief; do not remove the gate.

### Cut line

Cut optional shape-mismatch case and additional faults. Preserve one full evidence-first repair per team.

## 16:05-16:20 - LESSON-D2-08 + CHECK-D2-03 + CHECK-D2-04

**Objectives:** `OBJ-D2-05` through `OBJ-D2-08`  
**Must land:** The scientific loop transfers; Day 3 readiness requires mapping framework calls to mechanics and diagnosing non-unique evidence.

### Timing

- 3 minutes: bounded `LESSON-D2-08` transfer mapping.
- 5 minutes: `CHECK-D2-03`.
- 5 minutes: live core of `CHECK-D2-04`.
- 2 minutes: submit both through **Day 2 Checks**.
- Assign `CHECK-D2-04` Part C as five-minute consolidation due before Day 3 at 09:00.

### Transfer connection

Use one slide only: training/post-training objective, evaluation/grader, data pipeline, behavior diagnostic, and resource measurement all map to hypothesis -> experiment -> measurement -> diagnosis -> next experiment. State explicitly that RL implementation, distributed training, and hardware internals are outside core.

### Expected evidence snapshot

- D2-03: six requested `4 -> 8 -> 1` shapes; `X @ W`; only example-carrying first dimensions change; one bias-broadcasting explanation; cautious interpretation of the linear-looking run.
- D2-04: omitted reset diagnosis with alternatives/check; plain reset restored; `eval()` separate from inference context; return to train mode.

### Readiness remediation

- **Loop role weak:** use a five-card sequence at Day 3 opening, no extra code.
- **Shape weak:** require a named batch/channel/feature map before the first CNN operation on Day 3.
- **Mode weak:** print module mode and grad state separately before any Day 3 validation.
- **One-symptom/one-cause thinking:** require two hypotheses and one requested evidence card in the Day 3 leak investigation.

## 16:20-16:30 - Protected Buffer and Day 3 Bridge

Use only for blocked core debrief, must-land questions, or clean close. Do not introduce depth, CNNs, regularization, or data leakage early.

Close with:

> "Today you made a small network learn and repaired failures inside the training loop. Tomorrow a stronger model will not be enough: the data pipeline and validation evidence must also be trustworthy."

Participants bring `ACT-D2-04` evidence board and completed `CHECK-D2-04` Part C. Sample one response that distinguishes implementation/optimization evidence from representation/data evidence.

---

# Cross-Block Facilitation Notes

## Misconception Routing Table

| Symptom | Likely misconception | Cheapest question | Route |
|---|---|---|---|
| calls loss "accuracy" | objective and metric conflated | "Can classes stay fixed while probabilities change?" | A/B comparison in `ACT-D2-01` |
| says negative gradient moves parameter negative | gradient and descent direction conflated | "What sign results after subtracting it?" | update-rule substitution |
| sends scalar loss backward unchanged | backprop mechanism weak | "What local derivative is applied at this node?" | dual-trace graph |
| counts batch size in parameters | data and state dimensions conflated | "Which stored trainable array changes with B?" | `ACT-D2-03` |
| trusts decreasing loss as proof | optimization evidence overgeneralized | "What boundary and validation evidence are still missing?" | D2-03 evidence columns |
| says `backward()` updates | autograd/optimizer roles conflated | inspect parameter around backward/step | PyTorch reveal |
| says `eval()` disables gradients | mode and grad state conflated | print `model.training` and `torch.is_grad_enabled()` | D2-04 state table |
| fixes first guessed cause | symptom treated as unique | "What other cause makes this curve?" | `ACT-D2-04` gate |

## Assessment Collection Record

Capture:

- percent sequencing reset/forward/loss/backward/step correctly;
- percent matching logits to `BCEWithLogitsLoss`;
- chain-rule sign versus arithmetic errors;
- batch/target shape errors;
- percent separating optimization, representation, and generalization evidence;
- percent separating eval mode from gradient disabling;
- quality of `ACT-D2-04` discriminating checks;
- `CHECK-D2-04` readiness distribution;
- one Day 3 retrieval response based on actual exit evidence.

## Scope Protection

### Core

- complete learning loop and inference contrast;
- scalar loss versus metric;
- gradient descent and learning rate;
- one practical computational graph and gradient check;
- vectorization, batch dimension, broadcasting;
- complete NumPy training loop;
- PyTorch logits/autograd/optimizer/mode mapping;
- evidence-first failure diagnosis;
- bounded modern engineering transfer.

### First items to shorten

- full negative-log-likelihood derivation;
- additional computational-graph branches;
- optimizer catalogues;
- GPU hardware details;
- NumPy hyperparameter sweep;
- extra broken cases.

### Optional/reference only

- optimizer internals beyond practical SGD/Adam distinction;
- no-grad/inference-mode depth beyond their accurate core comparison;
- vanishing/exploding gradient theory beyond preview;
- reinforcement-learning implementation;
- distributed training and hardware internals;
- unsupported claims about prevalence or device speed.
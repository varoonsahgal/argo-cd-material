# Day 1 Instructor Guide: See It

**Instructor only. Do not distribute with participant materials.**

**Canonical question:** How can simple mathematical operations produce intelligent-looking behavior?  
**Day outcome:** Participants trace and investigate a forward-only NumPy network and explain correct/incorrect predictions from parameter, activation, shape, and boundary evidence.  
**Must-land sentence:** **A neural network is a chain of adjustable transformations; a prediction is the trace those settings produce.**

## Controlling Artifacts

- Participant guide: [courseware/day-1/student-guide/day-1-student-guide.md](../day-1/student-guide/day-1-student-guide.md)
- Participant challenges: [courseware/day-1/challenges/day-1-challenges.md](../day-1/challenges/day-1-challenges.md)
- Challenge key: [courseware/instructor-solutions/day-1/day-1-challenges-SOLUTION.md](../instructor-solutions/day-1/day-1-challenges-SOLUTION.md)
- Participant checks: [courseware/day-1/assessments/day-1-checks.md](../day-1/assessments/day-1-checks.md)
- Check key: [courseware/instructor-solutions/day-1/day-1-checks-SOLUTION.md](../instructor-solutions/day-1/day-1-checks-SOLUTION.md)
- Shared glossary: [courseware/shared/glossary.md](../shared/glossary.md)
- Shared notation: [courseware/shared/notation-and-style.md](../shared/notation-and-style.md)

## Objective and Evidence Map

| Objective | Must observe during instruction | Practice | Check |
|---|---|---|---|
| `OBJ-D1-01` | Neural network justified as one model family; training/inference distinguished | `LESSON-D1-01` scenario exercise and slide 4 model-choice defense | `CHECK-D1-01` |
| `OBJ-D1-02` | Inputs, weights, bias, activations, layers, outputs, parameters/hyperparameters labeled by role | `LAB-D1-01`, `LAB-D1-03` | `CHECK-D1-02` |
| `OBJ-D1-03` | Boundary motion explained from `w dot x + b = 0` | `ACT-D1-01`, `ACT-D1-02`, `LAB-D1-01` | `CHECK-D1-01` |
| `OBJ-D1-04` | One line shown impossible for XOR in raw space | `LAB-D1-02` | `CHECK-D1-03` |
| `OBJ-D1-05` | Identity stack collapsed algebraically; nonlinear hidden representation compared | `ACT-D1-03`, `LAB-D1-02`, `LAB-D1-03` | `CHECK-D1-03` |
| `OBJ-D1-06` | Batch-first shapes and forward stages stated before execution | `ACT-D1-04`, `LAB-D1-03`, `LAB-D1-04` | `CHECK-D1-02`, `CHECK-D1-04` |
| `OBJ-D1-07` | Fixed forward network investigated from four evidence views | `LAB-D1-04` | `CHECK-D1-04` |

## Exact 450-Minute Schedule

| Time | Min | Mode and canonical IDs | Scope |
|---|---:|---|---|
| 09:00-09:25 | 25 | Explain/retrieve: `LESSON-D1-01` | `CORE`; shorten application catalogue first |
| 09:25-09:55 | 30 | Visualize/predict: `LESSON-D1-02`, `ACT-D1-01` | `CORE` |
| 09:55-10:35 | 40 | Experiment: `LAB-D1-01`, embedded `ACT-D1-02` | `CORE` |
| 10:35-10:50 | 15 | Break | Protected |
| 10:50-11:15 | 25 | Explain/visualize: `LESSON-D1-03` | `CORE`; cut implementation detail first |
| 11:15-12:00 | 45 | Experiment/diagnose: `LAB-D1-02` | `CORE` |
| 12:00-12:15 | 15 | Assess: `CHECK-D1-01`, `CHECK-D1-02` | `CORE` |
| 12:15-13:15 | 60 | Lunch | Protected |
| 13:15-13:45 | 30 | Explain/shape map: `LESSON-D1-04`, `ACT-D1-04` | `CORE`; output nuance optional |
| 13:45-14:02 | 17 | Predict/visualize: `LESSON-D1-05`, `ACT-D1-03` | `CORE`; Leaky ReLU is optional extension only |
| 14:02-14:42 | 40 | Predict/experiment: `LAB-D1-03` | `CORE` |
| 14:42-14:57 | 15 | Break | Protected |
| 14:57-15:05 | 8 | Explain/trace: `LESSON-D1-06` | `CORE` |
| 15:05-16:05 | 60 | Experiment/diagnose: `LAB-D1-04` | `CORE` |
| 16:05-16:20 | 15 | Exit checks: `CHECK-D1-03`, `CHECK-D1-04` | `CORE` |
| 16:20-16:30 | 10 | Recovery/questions/close | Protected; no new content |

Total: `25+30+40+15+25+45+15+60+30+17+40+15+8+60+15+10 = 450` minutes.

## Operational Pacing Routes

### If behind

1. Cut the application catalogue, threshold edge cases, additional architecture examples, extra output-head examples, optional Leaky-ReLU work, and extra D1-04 probes in that order.
2. When environment recovery consumes working time, switch to the supplied precomputed arrays or static evidence board and continue the prediction-observation-debrief sequence.
3. Preserve every prediction commitment, the D1-03 wrong-axis diagnosis, every core lab debrief, both breaks, lunch, `CHECK-D1-04`, the two-minute Day 2 bridge, and the 16:20-16:30 buffer.
4. Do not use the final buffer to repay routine schedule drift or introduce new activation or Day 2 content.

### If ahead

1. Give one unfamiliar `3 -> 5 -> 2` architecture and require shapes, parameter count, and a labeled semantic invariant.
2. Ask for one observation that would disconfirm a proposed diagnosis.
3. During D1-04, allow one additional copied-parameter probe while preserving canonical parameters and the scheduled debrief.
4. Do not begin loss, gradients, backpropagation, or optional activation taxonomy.

## Before Class

### Required preflight

1. Open all four participant notebooks from a clean kernel and confirm the first runnable state.
2. Open the four corresponding instructor solution notebooks and pre-run them once. These notebooks are dependencies owned by the Lab Solution Engineer and are **not created by this lesson package**:
   - [courseware/instructor-solutions/day-1/LAB-D1-01-neuron-boundary-SOLUTION.ipynb](../instructor-solutions/day-1/LAB-D1-01-neuron-boundary-SOLUTION.ipynb)
   - [courseware/instructor-solutions/day-1/LAB-D1-02-linear-limit-SOLUTION.ipynb](../instructor-solutions/day-1/LAB-D1-02-linear-limit-SOLUTION.ipynb)
   - [courseware/instructor-solutions/day-1/LAB-D1-03-shapes-activations-SOLUTION.ipynb](../instructor-solutions/day-1/LAB-D1-03-shapes-activations-SOLUTION.ipynb)
   - [courseware/instructor-solutions/day-1/LAB-D1-04-forward-network-mystery-SOLUTION.ipynb](../instructor-solutions/day-1/LAB-D1-04-forward-network-mystery-SOLUTION.ipynb)
3. Export static fallback images after notebooks exist: initial/final boundary, linear/XOR comparison, activation panels plus softmax sums, and the four-panel forward evidence board.
4. Confirm the supplied Day 1 seed/fixed parameters reproduce all intended evidence bands.
5. Keep participant and instructor browser tabs visibly separated. Never screen-share a solution path before the participant run.
6. Prepare three colors: data/examples, trainable parameters, and activations. Reuse them throughout the day.

### Room and pairing

- Pairs use **driver** (types/runs) and **evidence lead** (records prediction, invariant, and debrief evidence). Swap at each lab midpoint.
- For teams of three, add a **shape checker** who states expected dimensions before execution.
- Keep printed or digital challenge sheets closed until their timed launch.

### Demo recovery ladder

1. **Interaction fails, code works:** use two precomputed before/after frames; preserve the prediction and observation questions.
2. **Notebook cell fails:** show the error as evidence, take one bounded diagnosis attempt, then switch to pre-run output from the instructor solution.
3. **Environment fails broadly:** pair affected participants with a working run and give them the evidence-lead role; use supplied screenshots/tables for interpretation.
4. **Time fails:** cut optional explanation and extra examples, never the prediction commitment or core debrief.

Do not claim a notebook has passed until the participant and solution execution reports exist. The ranges below are planning bands from the lab map and require calibration by lab testing.

---

# Facilitation Runbook

## 09:00-09:25 - LESSON-D1-01: Landscape and Retrieval

**Objectives:** `OBJ-D1-01`  
**Must land:** Neural networks are one adjustable model family, not the definition of AI; model choice begins with task/evidence/constraints.

### Sequence

| Minute | Move |
|---:|---|
| 0-3 | Display big question. Ask learners to write a one-sentence current model of a neural network. Do not correct yet. |
| 3-8 | Present nested-toolbox visual and explicitly state its limit: orientation, not strict ontology. |
| 8-14 | Use three cases: small tabular maintenance, image recognition, high-cost decision. Require simplest credible baseline first. |
| 14-20 | Build feature/target/prediction/parameter/hyperparameter vocabulary from one case. |
| 20-24 | Contrast training with inference; place Day 1 entirely on the fixed-parameter forward path. |
| 24-25 | Transition: "If we choose a neural model, what is its smallest visible computation?" |

### Visual direction

Use a two-axis choice map: input representation burden versus data/compute/debugging cost. Place a linear model, tree, compact neural model, and a large representation-learning system as examples, not universal rankings.

**Alt-text concept:** Model families occupy different regions of a trade-off map; no model is universally best.

### Questions and expected answers

- **Q:** Why start with a simple baseline on small named-feature data?  
  **Expected:** Fast, interpretable evidence; establishes what added complexity must beat or explain.
- **Q:** Is inference the same as evaluation?  
  **Expected:** Inference produces outputs; evaluation compares them to chosen targets/metrics and consequences.
- **Q:** Does an important target imply a deep network?  
  **Expected:** No; it implies stronger validity/evaluation requirements.

### Misconceptions to sample

- AI equals neural networks.
- generative AI equals all deep learning.
- training is simply running inputs through a model.
- parameters and hyperparameters are interchangeable.

### Cut line and optional material

- **First cut:** extended application catalogue and historical sequence.
- **Optional/reference:** detailed model taxonomy.
- **Never cut:** baseline defense and training/inference contrast.

### Demo recovery

If the choice-map interaction is unavailable, use the three verbal scenarios and physically place model cards on a whiteboard. The decision, not the software, is the teaching event.

## 09:25-09:55 - LESSON-D1-02 + ACT-D1-01: One Neuron

**Objectives:** `OBJ-D1-02`, `OBJ-D1-03`  
**Must land:** A boundary is where weighted evidence and bias cancel; orientation, location, and off-boundary probability are separate observables.

### Sequence

| Minute | Move |
|---:|---|
| 0-5 | Introduce evidence multipliers and adjustable offset without notation. |
| 5-10 | Show fixed probes and boundary. Ask what a boundary point means before showing an equation. |
| 10-15 | Introduce `z = w dot x + b`, sigmoid, and the `z = 0` boundary. Work one numeric example. |
| 15-23 | Run `ACT-D1-01`: three sketches and least-certain claim before controls move. |
| 23-27 | Reveal one parameter at a time with ghosted old contour and fixed probe values. |
| 27-30 | Debrief invariants; launch `LAB-D1-01`. |

### ACT-D1-01 compact answer

- Bias change with fixed weights translates the boundary parallel to itself.
- Changing either weight generally changes the full weight ratio; neither is a universally pure rotation/translation knob.
- Common positive scaling of `w` and `b` preserves the `z=0` boundary but pushes sigmoid outputs away from `0.5` off the boundary.

Use the full challenge key for alternatives and errors.

### Questions and expected answers

- **Q:** At `p=0.5`, what is `z`?  
  **Expected:** `0` for sigmoid.
- **Q:** What does changing `b` leave invariant?  
  **Expected:** Boundary normal/orientation while weights remain fixed.
- **Q:** If no sample changes class, can the model output still change?  
  **Expected:** Yes; scores/probabilities or the boundary can change without crossing finite sample points.

### Likely struggles

- Treating a weight as a named physical control.
- Confusing logit, probability, and class decision.
- Equating sharper output with calibrated confidence.

### Hint ladder

1. Find the boundary by replacing `p=0.5` with the corresponding `z`.
2. Hold the full weight vector fixed and compare two biases.
3. For common scaling, factor out the positive constant from the zero equation.

### Cut line

Cut formal vertical-line edge cases. Keep the contour interpretation and common-scaling counterexample.

## 09:55-10:35 - LAB-D1-01 + ACT-D1-02

**Participant notebook:** [courseware/day-1/labs/LAB-D1-01-neuron-boundary.ipynb](../day-1/labs/LAB-D1-01-neuron-boundary.ipynb)  
**Instructor solution:** [courseware/instructor-solutions/day-1/LAB-D1-01-neuron-boundary-SOLUTION.ipynb](../instructor-solutions/day-1/LAB-D1-01-neuron-boundary-SOLUTION.ipynb)  
**Must land:** Parameter effects become interpretable through one-change experiments and invariants.

### Launch script - 2 minutes

"Write the motion prediction before touching a control. Keep probe identities fixed. Your evidence is not only final accuracy; it is the old/new contour, the probe score, and what remained invariant. At the manual-search section, change one parameter at a time."

### Facilitation checkpoints

| Lab minute | Evidence checkpoint | Instructor action |
|---:|---|---|
| 8 | `weighted_sum` shape `(n_examples,)`; probability range valid | Ask for predicted shape before inspecting code. |
| 17 | Isolated parameter comparison with old/new contour | Challenge "accuracy did not change" as an incomplete observation. |
| 25 | `ACT-D1-02` commitment table started | Enforce one-parameter rule; swap pair roles. |
| 34 | Six probes and boundary agree | Ask one team to explain location versus confidence. |
| 40 | Debrief artifact selected | Stop coding; collect one screenshot/sketch plus invariant. |

### ACT-D1-02 compact answer

At start `w=(1,0), b=0`, points C and F are wrong under `z>=0 -> class 1`. One valid single change is `w2=0.5`; all six then have the required score sign. Accept any verified separator. The automation bridge requires an error/objective plus a rule for updating/searching parameters.

### Planning evidence band

- probabilities in `[0,1]`;
- `0.5` contour agrees with `w dot x + b = 0`;
- reasonable manual settings classify at least 10 of 12 notebook points;
- completed run is expected to be fast on CPU once the notebook exists.

### Hint ladder

1. Print one example's feature shape and the weight shape.
2. Write the scalar formula for one row.
3. Use a vectorized dot product and add one scalar bias.
4. If a boundary plot divides by a near-zero coefficient, use a contour of `z=0` instead of slope/intercept arithmetic.

### Likely struggles and responses

| Struggle | Response |
|---|---|
| Changes all parameters at once | Reset and require a predicted effect for one control. |
| Gets correct classes but inconsistent contour | Probe `z` on contour locations; inspect sign and threshold convention. |
| Treats multiple valid weights as a problem | Ask which predictions are invariant within a local parameter range. |
| Finishes early | Find a second valid setting and explain why it is equivalent for the six points. |

### Debrief - 4 minutes inside lab

Ask: "Which evidence distinguished translation from confidence change? Why is a workable setting not unique? What scales poorly about manual search?"

### Recovery

If plotting fails, use the six-probe score table plus two static contours. If environment startup consumes more than 8 minutes, pair on a working kernel and preserve the evidence-lead task.

## 10:35-10:50 - Protected Break

Do not compress. During break, verify that `LAB-D1-02` opens and the first plot renders. Do not begin content early.

## 10:50-11:15 - LESSON-D1-03: Linear Success, Then XOR

**Objectives:** `OBJ-D1-04`, `OBJ-D1-05`  
**Must land:** Optimization can move a line; it cannot change the representational family into a curved/multi-region boundary.

### Sequence

| Minute | Move |
|---:|---|
| 0-5 | Retrieve the one-neuron boundary; identify logistic regression as the same binary form. |
| 5-10 | Show separable blobs and require predicted success. Reveal boundary before accuracy. |
| 10-16 | Show XOR corners; require every learner to attempt a single separating line. |
| 16-21 | Introduce hidden coordinates as a response to visible impossibility. |
| 21-25 | Predict nonlinear versus identity hidden transforms; launch lab. |

### Visual direction

Use raw and hidden-space plots with identical point colors and four linked anchors. Do not label hidden axes with human concepts.

### Questions and expected answers

- **Q:** Would more epochs let one logistic boundary solve raw XOR?  
  **Expected:** No; fitting can reposition one line but not alter its family.
- **Q:** Does the output boundary need to be complex after a useful hidden transform?  
  **Expected:** No; hidden coordinates can make a simple output boundary sufficient.
- **Q:** Does a nonlinear architecture guarantee success?  
  **Expected:** It permits richer representation; useful parameters still matter.

### Cut line

Cut logistic-regression implementation detail and extended feature-engineering examples. Preserve the success-first reveal and the identity comparison.

## 11:15-12:00 - LAB-D1-02: The Linear Limit

**Participant notebook:** [courseware/day-1/labs/LAB-D1-02-linear-limit.ipynb](../day-1/labs/LAB-D1-02-linear-limit.ipynb)  
**Instructor solution:** [courseware/instructor-solutions/day-1/LAB-D1-02-linear-limit-SOLUTION.ipynb](../instructor-solutions/day-1/LAB-D1-02-linear-limit-SOLUTION.ipynb)  
**Must land:** Nonlinear hidden transformation changes representation; extra identity layers do not.

### Launch script - 2 minutes

"Rank four outcomes before fitting: linear blobs, XOR, fixed nonlinear hidden features, and the same stack with identity activations. Reveal region before score. Preserve point identities between raw and hidden plots."

### Facilitation checkpoints

| Lab minute | Evidence checkpoint |
|---:|---|
| 10 | Linear-data prediction reconciled with region and score |
| 20 | XOR prediction committed before run |
| 29 | XOR region diagnosed as representationally linear |
| 37 | Raw/hidden anchor identities compared |
| 42 | Identity versus nonlinear comparison explained |
| 45 | One-sentence representation/optimization distinction submitted |

### Planning evidence band

- separable data accuracy generally `0.95-1.00`;
- balanced XOR logistic accuracy generally `0.45-0.60`;
- fixed nonlinear network clean-corner accuracy `1.00`, noisy samples typically above `0.90`;
- identity comparison roughly chance.

Treat these as calibration bands, not grading cutoffs.

### Hint ladder

1. Ask whether any single line can separate alternating corners.
2. Inspect the classifier's region, not only accuracy.
3. Compare the same point colors before and after hidden transformation.
4. Replace hidden activation with identity while preserving all shapes/parameters.
5. Algebraically combine the two affine transforms.

### Likely struggles

- Assuming a noisy XOR score above chance disproves the limitation.
- Claiming hidden units "understand" corner types.
- Confusing a fixed forward network with participant-trained neural learning.
- Comparing nonlinear and identity paths with different parameters or data.

### Debrief - 5 minutes inside lab

Expected response: the hidden nonlinear transform changes coordinates so a simple output boundary becomes useful; the output line did not literally bend in hidden space. Ask for the evidence that distinguishes this from "train longer."

### Recovery

If fitting or mesh generation fails, provide precomputed region panels without labels and run the diagnosis/reveal sequence. Preserve the raw/hidden anchor comparison.

## 12:00-12:15 - CHECK-D1-01 and CHECK-D1-02

**Format:** 8 minutes for all of `CHECK-D1-01`, including Scenario B.4; 5 minutes for the unscored `CHECK-D1-02` commitment; 2 minutes for collection.

Tell participants that `CHECK-D1-02` deliberately precedes formal shape instruction. It is a baseline prediction, not a scored assessment at noon. They must preserve it and revise it after `LAB-D1-03`; the revised response and evidence-based correction are scored.

At minute 13, collect `CHECK-D1-01` and a snapshot of the preserved D1-02 commitment through the cohort's **Day 1 Checks** participant submission channel announced at session start. For paper delivery, collect the same artifact by hand and return the D1-02 working copy. Do not turn the two-minute collection window into pair comparison or added response time.

### Expected answer summary

- `CHECK-D1-01`: choose a compact linear/tree baseline for the small named-feature case; bias-only change translates parallel; common positive scaling preserves boundary but changes off-boundary probability.
- `CHECK-D1-02` (hold at noon): `X(12,5)`, `W1(5,6)`, `b1(6,)`, `Z1/A1(12,6)`, `W2(6,3)`, `b2(3,)`, logits `(12,3)`; `36+21=57`; wrong-axis softmax is shape-valid and violates per-example row sums. Do not reveal this until the post-`LAB-D1-03` revision.

Use the full check key for scoring and acceptable ambiguity.

### Remediation decision

- If more than one-third count batch entries as parameters, begin the afternoon with trainable-object color coding before `ACT-D1-04`.
- If common scaling is missed, repeat one fixed off-boundary probe; do not add a new derivation.
- If baseline choice is justified by "neural networks are bad for tables," correct the absolute claim and return to evidence/constraints.

## 12:15-13:15 - Protected Lunch

Do not compress. During lunch, preflight `LAB-D1-03`, verify activation plot ranges, and prepare a wrong-axis softmax output for the afternoon reveal.

## 13:15-13:45 - LESSON-D1-04 + ACT-D1-04: Layers and Shapes

**Objectives:** `OBJ-D1-02`, `OBJ-D1-06`  
**Must land:** `X(B,d_in) @ W(d_in,d_out) + b(d_out,) -> Z(B,d_out)`; parameter count excludes `B`.

### Sequence

| Minute | Move |
|---:|---|
| 0-5 | Retrieve one-neuron vector; widen it into a layer. Color data, parameters, activations. |
| 5-11 | Build batch-first shape equation using dimension tiles. |
| 11-16 | Count parameters for one layer, then `4 -> 8 -> 3`. |
| 16-24 | Run `ACT-D1-04` relay; change only `B` from 5 to 32. |
| 24-28 | Compare regression/binary/multiclass output heads at conceptual depth. |
| 28-30 | Preview activation invariants; launch observatory. |

### ACT-D1-04 compact answer

`X(5,4)`, `W1(4,8)`, `b1(8,)`, `Z1/A1(5,8)`, `W2(8,3)`, `b2(3,)`, logits/probabilities `(5,3)`; parameters `40+27=67`. At `B=32`, only example-carrying arrays change first dimension. Softmax normalizes axis `1` under this convention.

### Questions and expected answers

- **Q:** Which dimension contracts in `X @ W1`?  
  **Expected:** `d_in=4`.
- **Q:** Why does bias not add `B*8` parameters?  
  **Expected:** One vector broadcasts; it is reused, not copied as trainable state.
- **Q:** Can all shapes pass while output semantics are wrong?  
  **Expected:** Yes; wrong softmax axis or omitted activation can preserve shape.

### Cut line and optional material

- Cut additional architecture examples and extended output-head nuance.
- Leaky-ReLU details are optional.
- Never cut the batch-size change or `67`-parameter explanation.

## 13:45-14:02 - LESSON-D1-05 + ACT-D1-03: Nonlinearity and Activation Roles

**Objective:** `OBJ-D1-05`  
**Must land:** Stacked identity-activated affine layers remain affine; nonlinear hidden transformations alter the representational family, while output activation is task-specific.

### Sequence

| Minute | Move |
|---:|---|
| 0-4 | Algebraically collapse two identity-activated affine layers. |
| 4-7 | Show raw XOR -> identity hidden -> nonlinear hidden evidence. |
| 7-14 | Run the four-function `ACT-D1-03` core sort and reveal one mechanism at a time. |
| 14-17 | State one range/invariant per core function and launch the observatory. |

### ACT-D1-03 compact answer

- sigmoid -> `(0,1)`, saturates, binary output-shaped role;
- tanh -> `(-1,1)`, zero-centered, saturates;
- ReLU -> zero negative region, identity positive region;
- softmax -> coupled class vector, class-axis sum `1`, wrong-axis hazard.

Leaky ReLU is an optional extension, not a fifth core card or a required lab dependency.

### Questions and expected answers

- **Q:** What does adding an identity-activated layer change?  
  **Expected:** Parameterization and intermediate shape; the composed input-output map remains affine.
- **Q:** Why is softmax treated differently from the scalar curves?  
  **Expected:** It transforms a class vector jointly and its semantic invariant depends on the labeled class axis.
- **Q:** Does one all-zero ReLU batch prove permanent dead units?  
  **Expected:** No; inspect other data and parameter states.

### Cut line and recovery

Skip all Leaky-ReLU detail and extra role examples first. Preserve identity collapse, the four core functions, hidden/output-role distinction, and one executable invariant. If animation fails, reveal static mechanism cards one at a time.

## 14:02-14:42 - LAB-D1-03: Shape and Activation Observatory

**Participant notebook:** [courseware/day-1/labs/LAB-D1-03-shapes-activations.ipynb](../day-1/labs/LAB-D1-03-shapes-activations.ipynb)  
**Instructor solution:** [courseware/instructor-solutions/day-1/LAB-D1-03-shapes-activations-SOLUTION.ipynb](../instructor-solutions/day-1/LAB-D1-03-shapes-activations-SOLUTION.ipynb)  
**Must land:** Shapes are executable hypotheses; semantic invariants catch errors that array compatibility does not.

### Launch script - 2 minutes

"Use the activation mechanisms you just classified. Write expected shape and range before every revealing cell. For softmax, label the class axis and predict the per-example sum before choosing an axis. Core work is sigmoid, tanh, ReLU, and softmax; Leaky ReLU is optional extension work."

### Facilitation checkpoints

| Lab minute | Evidence checkpoint |
|---:|---|
| 8 | Dense step yields `(5,8)` with visible broadcasting |
| 16 | Activation curves and actual value heatmap aligned |
| 24 | Extreme sigmoid/tanh and negative ReLU observations recorded |
| 31 | Correct softmax row sums pass |
| 35 | Wrong-axis variant diagnosed from invariant, not crash |
| 40 | Shape-correct/semantic-wrong example submitted |

### Planning evidence

- parameter count `67`;
- hidden `(5,8)` and logits/softmax `(5,3)`;
- correct row sums `1` within `1e-6`;
- wrong-axis assertion fails;
- strongly negative ReLU input yields current all-zero hidden output.

### Hint ladder

1. Write one example's dense calculation before vectorizing.
2. Identify which axis contains classes.
3. For stable softmax, subtract the row maximum before exponentiating.
4. Sum probabilities along the class axis and print the vector.
5. Compare one input before/after each activation at the same scale.

### Likely struggles

- Treating one zero ReLU output as permanent death.
- Implementing unstable softmax and seeing overflow.
- Choosing an axis from memorized number rather than labeled dimension.
- Comparing activation curves with mismatched axes.

### Debrief - 5 minutes inside lab

Use the final 5 minutes for the debrief and `CHECK-D1-02` revision. Ask: "Why can wrong-axis code run? Which invariant catches it? Why is shape correctness necessary but insufficient?" Then have participants revise the noon ticket in a second color and cite one lab observation. Score the revised response; preserve the original as evidence of learning.

### Recovery

If participant implementation blocks the activation comparison, provide the plotting-ready pre/post arrays from a pre-run solution, but require shape/range predictions and wrong-axis diagnosis.

## 14:42-14:57 - Protected Break

Do not compress. Queue the forward-trace visual and the `LAB-D1-04` pre-run four-panel evidence board.

## 14:57-15:05 - LESSON-D1-06: Forward-Trace Consolidation

**Objectives:** `OBJ-D1-06`, `OBJ-D1-07`  
**Must land:** Forward propagation is an auditable sequence with shape, range, invariant, and fixed-parameter evidence.

### Sequence

| Minute | Move |
|---:|---|
| 0-3 | Trace one named example through `x -> z1 -> a1 -> z2 -> p -> class`; predict the next shape/range. |
| 3-6 | Widen the trace to a batch and identify what does and does not change. |
| 6-8 | State the evidence reveal order and launch the mystery lab. |

### Questions and expected answers

- **Q:** What can a forward trace explain?  
  **Expected:** How fixed inputs/parameters/intermediates produced an output; not training history, calibration, or complete causality.
- **Q:** What changes when one example becomes a batch?  
  **Expected:** Example-carrying arrays gain or change their first dimension; trainable parameter shapes do not change.

### Cut line and recovery

Preserve the named-stage trace, batch widening, and mystery reveal order. If animation fails, reveal six static trace cards one at a time and ask for the next shape and range before each card.

## 15:05-16:05 - LAB-D1-04: Forward Network Mystery

**Participant notebook:** [courseware/day-1/labs/LAB-D1-04-forward-network-mystery.ipynb](../day-1/labs/LAB-D1-04-forward-network-mystery.ipynb)  
**Instructor solution:** [courseware/instructor-solutions/day-1/LAB-D1-04-forward-network-mystery-SOLUTION.ipynb](../instructor-solutions/day-1/LAB-D1-04-forward-network-mystery-SOLUTION.ipynb)  
**Must land:** A mostly correct fixed network and its failures are both traceable without anthropomorphism.

### Launch script - 3 minutes

"Select two likely failing probes from raw geometry and name the hidden/boundary evidence you expect. Complete the forward path in order. Do not mutate the canonical parameter dictionary; perturb a copy. Reveal raw geometry, probability, boundary, hidden representation, then trace table."

### Facilitation checkpoints

| Lab minute | Evidence checkpoint |
|---:|---|
| 8 | Failure predictions committed; shape hypotheses written |
| 18 | Hidden `(n,6)` and output `(n,1)` invariants pass |
| 28 | Transpose error classified and repaired |
| 38 | Probability and decision region reconciled |
| 48 | Hidden plot interpreted with projection caveat |
| 55 | Six-probe table contains parameter/activation/threshold evidence |
| 60 | One correct and one wrong case debriefed; Day 2 need named |

### Planning evidence band

- probabilities in `[0,1]`;
- fixed network accuracy generally `0.82-0.92`;
- four named probes correct and two boundary/noise probes incorrect;
- hidden representation separates most classes more clearly than raw input;
- mesh and batch forward outputs agree.

### Hint ladder

1. Write the expected shape beside every intermediate.
2. Check `X.shape[1] == W1.shape[0]` before multiplication.
3. Compare one row from batch forward with a one-example trace.
4. Check whether `z2` is a logit before applying sigmoid.
5. Keep canonical parameters immutable and use a copied dictionary for perturbation.
6. For a wrong probe, cite a contour and one trace row before proposing a story.

### Likely struggles

- Mutating canonical parameters and losing the mystery evidence.
- Calling a hidden projection a complete explanation.
- Explaining errors as "confusion" instead of parameterized computation.
- Treating wrong prediction and shape exception as the same failure.
- Spending too long polishing plots instead of completing the evidence table.

### Debrief - 7 minutes inside lab

Use a four-panel board: raw probes, decision region, hidden projection, trace table.

Ask in order:

1. "Which probe prediction survived the evidence?"
2. "Which intermediate observation changed your explanation?"
3. "What can this trace not tell us?"
4. "What would learning need so this error can change future parameters?"

Expected bridge: an error/loss signal, a way to calculate parameter sensitivity/responsibility, and an update rule. Accept "loss, backpropagation, optimizer" when roles are clear.

### Recovery

- Shape bug consumes more than 5 minutes: provide a correctly shaped forward function shell, then continue with evidence interpretation.
- Plot fails: use the pre-run four-panel board and require each pair to annotate one probe.
- Fixed outputs do not match planning band: stop; do not improvise new parameters. Use validated cached output and record the notebook as requiring retest.

## 16:05-16:20 - CHECK-D1-03 and CHECK-D1-04

**Format:** `CHECK-D1-03` live core 6 minutes; `CHECK-D1-04` live core 7 minutes; Day 2 bridge 2 minutes. Marked consolidation items are completed outside the live block.

Assign `CHECK-D1-03` item 5 and `CHECK-D1-04` items 2 and 5 as one five-minute consolidation due through the **Day 1 Checks** participant submission channel before Day 2 at 09:00. Sample one submitted response during the Day 2 opening retrieval.

### Expected answer summary

- `CHECK-D1-03`: no single raw-space line separates XOR; affine compositions collapse to one affine map; a nonlinear hidden activation changes representation; compare identity versus nonlinear under the same data/shapes/settings.
- `CHECK-D1-04`: the supplied trace predicts class `1` incorrectly for target `0`; first hidden activation is nonzero while second is zero; fixed transformations produce positive logit/probability; transpose exception is an implementation failure; learning requires error signal plus update mechanism.

### Scoring and Day 2 readiness

Use the 6-point anchors in the check key. For readiness, prioritize whether the learner can:

1. distinguish a wrong complete trace from a failed computation;
2. explain a result with parameters/activations/threshold;
3. name error signal and parameter-change rule.

### Immediate remediation

- If identity-collapse is weak, write the two-layer substitution once; do not add more activation taxonomy.
- If forward/error distinction is weak, contrast "no `z1` produced" with "full trace, target disagreement."
- If learners say "the model changes when wrong," ask them to point to any Day 1 assignment that mutates a parameter.

### Transition to Day 2

Close with: "Today the parameters stayed fixed. Tomorrow the forward trace becomes the first half of a loop: predict, measure error, carry sensitivity backward, update, repeat."

## 16:20-16:30 - Protected Buffer

Use only for:

- environment recovery that blocked a core debrief;
- questions about a must-land concept;
- clean transition and next-day preparation.

Do not introduce loss equations, gradient descent, or backpropagation here.

---

# Cross-Block Facilitation Notes

## Misconception Routing Table

| Symptom | Likely misconception | Cheapest discriminating question | Route |
|---|---|---|---|
| Says bias rotates the boundary | Parameters treated as independent visual controls | "With weights fixed, did the normal vector change?" | Revisit `ACT-D1-01` overlay |
| Counts batch entries as parameters | Data dimensions confused with trainable state | "If `B` changes only, which stored trainable arrays change?" | Revisit `ACT-D1-04` colors |
| Expects more epochs to solve XOR | Optimization confused with representation | "Can you draw any one separating line?" | Revisit `LAB-D1-02` raw plot |
| Says more layers imply nonlinear boundary | Layer count confused with function composition | "What happens when every activation is identity?" | Collapse two affine layers |
| Treats softmax shape as proof | Compatibility confused with semantics | "What should each example's class total be?" | Run row-sum invariant |
| Says hidden unit "understands" a concept | Anthropomorphic interpretation | "Which activation/weight/contour is your evidence?" | Rewrite claim using trace terms |
| Treats a wrong prediction as a code bug | Model error confused with implementation failure | "Did every stage produce valid shape/range?" | Contrast mystery with transpose error |

## Challenge Scoring Snapshot

| Activity | Evidence of success | Do not reward |
|---|---|---|
| `ACT-D1-01` | Prediction before reveal, invariant, evidence-based revision | Artistic boundary precision alone |
| `ACT-D1-02` | One-variable changes, score signs, explanation; up to 6 points | Speed or a magic parameter value |
| `ACT-D1-03` | Behavior/role match and executable invariant | Unsupported "most common" claims |
| `ACT-D1-04` | Dimension logic, `67` parameters, batch invariance | Memorized shapes without contraction explanation |

## Scope Protection

### Core

- model choice and training/inference;
- neuron score, sigmoid, threshold, boundary geometry;
- linear success and XOR limitation;
- hidden nonlinearity;
- dense shapes and parameter count;
- activation behavior and output roles;
- vectorized forward trace and mystery diagnosis.

### First items to shorten

- application catalogue and AI history;
- threshold edge cases;
- logistic-regression implementation detail;
- additional architecture examples;
- extra output-head cases.

### Optional/reference only

- extended Leaky-ReLU nuance;
- multilabel output design;
- named interpretability methods;
- current claims about activation prevalence or modern internal-analysis tooling.

Any current API, hardware, framework-default, or modern-practice claim must be verified against a dated primary source before delivery. Day 1 core mathematical claims do not require current-source assertions.

## End-of-Day Instructor Record

Capture:

- percent of participants who distinguish parameters from hyperparameters;
- most common boundary-motion error;
- percent who calculate `67` without counting batch size;
- most common wrong-axis explanation;
- `CHECK-D1-04` readiness distribution;
- any notebook path, output band, or runtime issue requiring Lab Tester follow-up;
- one retrieval prompt to open Day 2 based on actual exit evidence.
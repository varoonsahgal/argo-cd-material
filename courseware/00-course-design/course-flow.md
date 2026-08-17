# Course Flow and Delivery Map

## Delivery Frame

- Four days, 09:00-16:30.
- Each day is 450 elapsed minutes: 360 minutes of instruction/activity, 60 minutes of lunch, 30 minutes of breaks.
- The final 10 minutes are protected recovery buffer. Do not pre-fill them with optional content.
- Four primary notebook labs and four short activities appear each day.
- Each content cycle follows **Explain -> Visualize -> Predict -> Experiment -> Observe -> Diagnose -> Explain Why**. A cycle may span several adjacent rows, but prediction must precede the revealing run.
- `CORE` is the planned live path. `SHORTEN` gives the facilitator's first compression point. `OPTIONAL` is never required for a stated outcome.

## Day 1: See It

**Question:** How can simple mathematical operations produce intelligent-looking behavior?  
**Outcome:** Trace and investigate a forward-only NumPy network.  
**Instructor guide:** `courseware/instructor-guide/day-1-instructor-guide.md`  
**Student Guide:** `courseware/day-1/student-guide/day-1-student-guide.md`  
**Challenges:** `courseware/day-1/challenges/day-1-challenges.md`  
**Assessments:** `courseware/day-1/assessments/day-1-checks.md`  
**Slides:** `courseware/slides/day-1-see-it.md` and rendered PDF

| Time | Min | Loop phase | Instruction/activity and IDs | Evidence/debrief | Scope control |
|---|---:|---|---|---|---|
| 09:00-09:25 | 25 | Explain | `LESSON-D1-01`: AI -> ML -> deep learning -> generative AI; structured/unstructured data; training/inference; features, labels, parameters, hyperparameters; when simpler models win | Participants defend a simple baseline for one scenario | `CORE`; `SHORTEN` historical evolution first |
| 09:25-09:55 | 30 | Visualize + predict | `LESSON-D1-02`, `ACT-D1-01`: weighted sum, sigmoid, geometric boundary sliders | Commit which parameter rotates vs. translates; reveal and explain | `CORE` |
| 09:55-10:35 | 40 | Experiment + observe | `LAB-D1-01`: one-neuron boundary workshop | Boundary screenshots, probability changes, explanation of six points | `CORE` |
| 10:35-10:50 | 15 | Break | Protected | None | Do not compress |
| 10:50-11:15 | 25 | Explain + visualize | `LESSON-D1-03`: logistic regression as one neuron, threshold, linear limitation, XOR | Predict performance on linear data and XOR before plots | `CORE` |
| 11:15-12:00 | 45 | Experiment + diagnose | `LAB-D1-02`: linear limit and nonlinear data | Compare boundary/accuracy; explain how hidden units combine regions | `CORE` |
| 12:00-12:15 | 15 | Explain why + assess | `CHECK-D1-01`, `CHECK-D1-02`; one model-choice scenario and one shape/parameter ticket | Facilitator samples misconceptions before layers | `CORE` |
| 12:15-13:15 | 60 | Lunch | Protected | None | Do not compress |
| 13:15-13:45 | 30 | Explain + visualize | `LESSON-D1-04`, `ACT-D1-04`: dense layers, depth/width, matrix/bias shapes, parameter count, regression/binary/multiclass outputs | Teams complete `4 -> 8 -> 3` shape relay | `CORE`; extra output-head nuance is `OPTIONAL` |
| 13:45-14:02 | 17 | Explain + predict | `LESSON-D1-05`, `ACT-D1-03`: stacked-linear collapse and activation choices | Predict hidden/output activation effects before the observatory | `CORE`; Leaky-ReLU comparison is `OPTIONAL` |
| 14:02-14:42 | 40 | Experiment + diagnose | `LAB-D1-03`: shape and activation observatory | Activation curves, shape assertions, softmax row sums, dead/saturated cases | `CORE` |
| 14:42-14:57 | 15 | Break | Protected | None | Do not compress |
| 14:57-15:05 | 8 | Consolidate + visualize | `LESSON-D1-06`: forward-trace consolidation | Reconnect shapes, activations, and outputs as one trace before the complete network | `CORE`; additional batch examples are `SHORTEN` |
| 15:05-16:05 | 60 | Experiment + diagnose | `LAB-D1-04`: complete forward network and mystery examples | Decision regions, hidden representation, evidence for correct/failing cases | `CORE` |
| 16:05-16:20 | 15 | Explain why + assess | `CHECK-D1-03`, `CHECK-D1-04`; Day 2 bridge: "What would learning need to change?" | Individual exit response establishes Day 2 retrieval | `CORE` |
| 16:20-16:30 | 10 | Buffer | Environment recovery, questions, clean close | No new content | Protected |

### Day 1 short activities

| ID | Minutes embedded | Format | Prompt and debrief |
|---|---:|---|---|
| `ACT-D1-01` | 8 | Interactive visual | Predict weight/bias effects before moving sliders; distinguish rotation, translation, and confidence change. |
| `ACT-D1-02` | 7 in `LAB-D1-01` | Constrained challenge | Manually classify fixed points with weights; debrief why search becomes impractical as parameters grow. |
| `ACT-D1-03` | 8 | Card sort/poll | Match sigmoid, tanh, ReLU, and softmax to visible behavior and roles; explain hidden vs. output choices. A Leaky-ReLU comparison card is independently `OPTIONAL`. |
| `ACT-D1-04` | 8 | Team shape relay | Determine matrices, biases, activations, and 67 parameters for `4 -> 8 -> 3`; explain each term. |

### Day 1 lesson integration and cut lines

| Lesson | Core idea | Launches | First cut if behind |
|---|---|---|---|
| `LESSON-D1-01` | Neural networks are one model family, not the definition of AI | `ACT-D1-01` | Detailed application catalogue |
| `LESSON-D1-02` | A neuron is a parameterized transformation with geometry | `LAB-D1-01` | Formal threshold edge cases |
| `LESSON-D1-03` | Evidence from XOR earns hidden units | `LAB-D1-02` | Extended logistic-regression implementation discussion |
| `LESSON-D1-04` | Layers are shape-constrained matrix transformations | `ACT-D1-04`, `LAB-D1-03` | Additional architecture examples |
| `LESSON-D1-05` | Nonlinearity prevents stacked layers collapsing to one linear map | `ACT-D1-03`, `LAB-D1-03` | Leaky-ReLU derivation |
| `LESSON-D1-06` | Forward propagation is a traceable sequence | `LAB-D1-04` | Additional batch examples |

## Day 2: Train It

**Question:** When a neural network makes a mistake, how does it know what to change?  
**Outcome:** Train the same small model from scratch and in PyTorch, then repair broken runs.  
**Instructor guide:** `courseware/instructor-guide/day-2-instructor-guide.md`  
**Student Guide:** `courseware/day-2/student-guide/day-2-student-guide.md`  
**Challenges:** `courseware/day-2/challenges/day-2-challenges.md`  
**Assessments:** `courseware/day-2/assessments/day-2-checks.md`  
**Slides:** `courseware/slides/day-2-train-it.md` and rendered PDF

| Time | Min | Loop phase | Instruction/activity and IDs | Evidence/debrief | Scope control |
|---|---:|---|---|---|---|
| 09:00-09:20 | 20 | Retrieve + explain | `LESSON-D2-01`: initialize -> forward -> loss -> backward -> update -> repeat; epoch/iteration/batch; train vs. inference | Reconstruct the loop using Day 1 artifacts | `CORE` |
| 09:20-09:45 | 25 | Predict + calculate | `LESSON-D2-02`, `ACT-D2-01`: scalar objective, MSE/BCE/cross-entropy intuition, loss vs. accuracy, output/loss pairing | Rank prediction vectors before calculating loss | `CORE`; log-likelihood depth is `SHORTEN` |
| 09:45-10:25 | 40 | Visualize + experiment | `LAB-D2-01`: loss landscapes and learning-rate roulette | Paths visibly crawl, converge, oscillate, or diverge | `CORE` |
| 10:25-10:40 | 15 | Break | Protected | None | Do not compress |
| 10:40-11:10 | 30 | Explain + visualize | `LESSON-D2-03`, `ACT-D2-02`: derivative as sensitivity, graph, chain rule, local x upstream gradient | Predict gradient sign before numeric reveal | `CORE`; extended symbolic algebra is `SHORTEN` |
| 11:10-11:55 | 45 | Experiment + diagnose | `LAB-D2-02`: manual backprop and finite-difference gradient check | Relative-error table identifies sign/missing-factor bugs | `CORE` |
| 11:55-12:05 | 10 | Assess | `CHECK-D2-01`, `CHECK-D2-02` | Repair loss pairing and one gradient path | `CORE` |
| 12:05-13:05 | 60 | Lunch | Protected | None | Do not compress |
| 13:05-13:25 | 20 | Visualize + predict | `LESSON-D2-04`, `ACT-D2-03`: vectorization, batch dimension, broadcasting, tensor shapes, GPU rationale | Predict matrix shapes for 1, 32, and 1,024 examples | `CORE` |
| 13:25-14:35 | 70 | Build + observe | `LESSON-D2-05`, `LAB-D2-03`: initialize, forward, stable loss, backward, update, train, plot | Loss/accuracy curve and nonlinear boundary meet sanity ranges | `CORE` |
| 14:35-14:50 | 15 | Break | Protected | None | Do not compress |
| 14:50-15:10 | 20 | Compare + explain | `LESSON-D2-06`: NumPy/PyTorch side-by-side; modules, autograd, loss, optimizer, zero-grad, mode, device | Map every framework line to an automated mechanic | `CORE` |
| 15:10-16:05 | 55 | Break/fix + diagnose | `LESSON-D2-07`, `LAB-D2-04`, `ACT-D2-04`: PyTorch baseline plus broken cases | Teams identify symptom, discriminating check, cause, fix, and mechanism | `CORE`; extra failures are `OPTIONAL` |
| 16:05-16:20 | 15 | Transfer + assess | `LESSON-D2-08`, `CHECK-D2-03`, `CHECK-D2-04`: hypothesis/experiment/measurement loop in post-training and evaluation | Day 3 readiness diagnosis | `CORE` |
| 16:20-16:30 | 10 | Buffer | Recovery and questions | No new content | Protected |

### Day 2 short activities

| ID | Minutes embedded | Format | Prompt and debrief |
|---|---:|---|---|
| `ACT-D2-01` | 7 | Prediction vote | Rank probabilities by expected BCE/cross-entropy; reveal that equal accuracy can hide different confidence/loss. |
| `ACT-D2-02` | 8 | Animated path | Predict tiny/reasonable/large learning-rate trajectories; name curve evidence rather than memorizing labels. |
| `ACT-D2-03` | 7 | Matrix shape map | Translate a scalar loop to batched matrix multiplication and explain why the computation maps to accelerators. |
| `ACT-D2-04` | 10 in `LAB-D2-04` | Model detective | Diagnose mystery curves before seeing the faulty code; require a discriminating check before a fix. |

### Day 2 lesson integration and cut lines

| Lesson | Core idea | Launches | First cut if behind |
|---|---|---|---|
| `LESSON-D2-01` | Training repeats a six-stage causal loop | `CHECK-D2-01`, all labs | Extended terminology examples |
| `LESSON-D2-02` | Loss supplies a scalar optimization signal | `ACT-D2-01`, `LAB-D2-01` | Full NLL derivation |
| `LESSON-D2-03` | Backprop efficiently composes local sensitivities | `LAB-D2-02` | Additional graph branches |
| `LESSON-D2-04` | Batch computation is the same operation with an added dimension | `ACT-D2-03`, `LAB-D2-03` | GPU hardware detail |
| `LESSON-D2-05` | Scratch mechanics expose every training responsibility | `LAB-D2-03` | Optional activation sweep |
| `LESSON-D2-06` | PyTorch automates, but does not remove, the mechanics | `LAB-D2-04` | Device-management nuance |
| `LESSON-D2-07` | Symptoms become useful when tied to discriminating checks | `ACT-D2-04`, `LAB-D2-04` | Extra broken cases |
| `LESSON-D2-08` | The same scientific loop appears in modern model work | `CHECK-D2-04` | RL/reward detail |

## Day 3: Scale It

**Question:** How do the fundamentals become the systems used in modern AI?  
**Outcome:** Build a valid compact image workflow, expose generalization failures, and compare scratch with transfer.  
**Instructor guide:** `courseware/instructor-guide/day-3-instructor-guide.md`  
**Student Guide:** `courseware/day-3/student-guide/day-3-student-guide.md`  
**Challenges:** `courseware/day-3/challenges/day-3-challenges.md`  
**Assessments:** `courseware/day-3/assessments/day-3-checks.md`  
**Slides:** `courseware/slides/day-3-scale-it.md` and rendered PDF

| Time | Min | Loop phase | Instruction/activity and IDs | Evidence/debrief | Scope control |
|---|---:|---|---|---|---|
| 09:00-09:15 | 15 | Retrieve + visualize | `LESSON-D3-01`, `ACT-D3-01`: depth, width, capacity, parameter count, feature hierarchy, optimization risk | Map raw -> simple -> intermediate -> high-level features | `CORE`; initialization/normalization details recur later |
| 09:15-09:35 | 20 | Explain + predict | `LESSON-D3-02`: datasets/loaders, splits, stratification, normalization, transformations, augmentation, imbalance, leakage | Identify which operations may learn only from training data | `CORE` |
| 09:35-10:20 | 45 | Investigate + diagnose | `LAB-D3-01`, `ACT-D3-02`: suspicious validation score and provenance | Produce leak report and valid pipeline order | `CORE` |
| 10:20-10:35 | 15 | Break | Protected | None | Do not compress |
| 10:35-11:00 | 25 | Explain + visualize | `LESSON-D3-03`, `ACT-D3-03`: locality, kernels, channels, padding, stride, maps, pooling, sharing, receptive field | Predict edge-map and output shapes | `CORE` |
| 11:00-12:00 | 60 | Build + observe | `LAB-D3-02`: compact Fashion-MNIST CNN and feature maps | Shapes, curves, validation range, misclassified examples | `CORE` |
| 12:00-12:10 | 10 | Assess + debrief | `CHECK-D3-01` | Infer a feature-map shape and mechanism | `CORE` |
| 12:10-13:10 | 60 | Lunch | Protected | None | Do not compress |
| 13:10-13:25 | 15 | Predict + explain | `LESSON-D3-04`, `LESSON-D3-05`: training knobs, instability, under/overfit, gap, regularization, early stopping, augmentation | Predict effects of longer training and less data | `CORE`; optimizer/scheduler survey is `SHORTEN` |
| 13:25-14:20 | 55 | Make fail + rescue | `LAB-D3-03`: overfit tiny data, choose one intervention, compare curves | Before/after gap and mechanism defense | `CORE`; multi-intervention sweep is `OPTIONAL` |
| 14:20-14:35 | 15 | Break | Protected | None | Do not compress |
| 14:35-14:50 | 15 | Explain + choose | `LESSON-D3-06`: pretrained representation, freeze, head replacement, fine-tune, domain match | Teams predict scratch vs. frozen outcome | `CORE` |
| 14:50-15:45 | 55 | Compare + explain | `LAB-D3-04`: transfer-learning race | Quality, time, sample efficiency, and compute scoreboard | `CORE`; partial fine-tuning is `OPTIONAL` |
| 15:45-16:05 | 20 | Conceptual visual | `LESSON-D3-07`, `LESSON-D3-08`, `ACT-D3-04`: Q/K/V intuition, self-attention, positional information, Transformer/pretraining; memory/throughput/distribution/serving | Predict token links; map fundamentals and identify attention caveat/resource trade-off | `CORE` conceptual; equations/systems implementation are `MOVE` |
| 16:05-16:20 | 15 | Assess + explain why | `CHECK-D3-02`, `CHECK-D3-03`, `CHECK-D3-04` | Pipeline, generalization, transfer/scale readiness gate | `CORE` |
| 16:20-16:30 | 10 | Buffer | Recovery and questions | No new content | Protected |

### Day 3 short activities

| ID | Minutes embedded | Format | Prompt and debrief |
|---|---:|---|---|
| `ACT-D3-01` | 6 | Feature ladder | Infer useful representations at successive depths; reject "deeper always better." |
| `ACT-D3-02` | 8 in `LAB-D3-01` | Find the leak | Use provenance and impossible metrics to identify post-outcome data and training-only transformations. |
| `ACT-D3-03` | 8 | Kernel reveal | Sketch/predict a filter's output before convolution; explain locality and sharing. |
| `ACT-D3-04` | 8 | Token-map prediction | Predict token relationships, reveal a stylized map, and state why attention weight is not complete causal explanation. |

### Day 3 lesson integration and cut lines

| Lesson | Core idea | Launches | First cut if behind |
|---|---|---|---|
| `LESSON-D3-01` | Depth enables feature reuse but increases capacity/optimization demands | `ACT-D3-01` | Initialization catalogue |
| `LESSON-D3-02` | Valid evidence depends on split and transformation provenance | `LAB-D3-01` | DataLoader API detail |
| `LESSON-D3-03` | CNNs encode locality and share parameters | `LAB-D3-02` | Receptive-field arithmetic |
| `LESSON-D3-04` | Curves separate optimization and fit patterns | `LAB-D3-03` | Batch-size survey |
| `LESSON-D3-05` | Regularization is a hypothesis about generalization | `LAB-D3-03` | Multiple simultaneous remedies |
| `LESSON-D3-06` | Reuse is valuable when representation and domain align | `LAB-D3-04` | Full fine-tuning |
| `LESSON-D3-07` | Attention is learned relevance inside the same training mechanics | `ACT-D3-04` | Transformer equations |
| `LESSON-D3-08` | Scale converts model work into systems trade-offs | `CHECK-D3-04` | Distributed algorithms |

## Day 4: Think Like an ML Engineer

**Question:** The model trained successfully, but is it good, and what should be improved next?  
**Outcome:** Complete and defend a constrained neural-network investigation.  
**Instructor guides:** `courseware/instructor-guide/day-4-instructor-guide.md` plus the instructor-only `courseware/capstone/capstone-instructor-guide.md`  
**Student Guide:** `courseware/day-4/student-guide/day-4-student-guide.md`  
**Challenges:** `courseware/day-4/challenges/day-4-challenges.md`  
**Assessments:** `courseware/day-4/assessments/day-4-checks.md`  
**Canonical `LAB-D4-04` pair:** `courseware/capstone/capstone-starter.ipynb` and instructor-only `courseware/capstone/capstone-solution.ipynb`  
**Slides:** `courseware/slides/day-4-think-like-an-ml-engineer.md` and rendered PDF

| Time | Min | Loop phase | Instruction/activity and IDs | Evidence/debrief | Scope control |
|---|---:|---|---|---|---|
| 09:00-09:15 | 15 | Retrieve + baseline | `LESSON-D4-01`: splits, baselines, aggregate vs. class/slice evidence | Recall loss/metric distinction and valid validation | `CORE` |
| 09:15-09:35 | 20 | Scenario + visualize | `ACT-D4-01`: accuracy, precision, recall, F1, confusion matrix, thresholds, PR trade-off, ROC/AUC overview | Choose metric from fraud costs before formula discussion | `CORE`; ROC mechanics are `SHORTEN` |
| 09:35-10:15 | 40 | Experiment + diagnose | `LAB-D4-01`: accuracy is not enough | Threshold table and cost-aware recommendation | `CORE` |
| 10:15-10:30 | 15 | Break | Protected | None | Do not compress |
| 10:30-10:45 | 15 | Explain + predict | `LESSON-D4-02`, `ACT-D4-02`: high bias/variance, generalization gap, optimization failure | Classify hidden curves before labels | `CORE` |
| 10:45-11:25 | 40 | Investigate + prioritize | `LESSON-D4-03`, `LAB-D4-02`: errors, buckets, class patterns, label noise, shift, edge cases | Evidence-backed error taxonomy and next experiment | `CORE` |
| 11:25-11:35 | 10 | Assess + debrief | `CHECK-D4-01`, `CHECK-D4-02` | Metric and diagnosis readiness | `CORE` |
| 11:35-12:35 | 60 | Lunch | Protected | None | Do not compress |
| 12:35-12:55 | 20 | Explain + trade-off | `LESSON-D4-04`, `LESSON-D4-05`, `LESSON-D4-06`, `ACT-D4-03`: one-variable hypothesis, records/seeds/checkpoints, CPU/GPU, batch, precision, size, latency, throughput | Choose between models for a deployment constraint | `CORE`; mixed-precision implementation is `MOVE` |
| 12:55-13:45 | 50 | Decide + experiment | `LAB-D4-03`: one experiment, tracked and benchmarked | Reproduction tolerance plus quality/resource evidence | `CORE` |
| 13:45-14:00 | 15 | Break | Protected | None | Do not compress |
| 14:00-14:15 | 15 | Transfer gallery | `LESSON-D4-07`, `ACT-D4-04`: capability, evaluation, regression, data, efficiency, safety, internals | Define evidence that a coding model is actually better | `CORE` conceptual; implementation depth is `MOVE` |
| 14:15-15:50 | 95 | Investigate + improve | `LESSON-D4-08`, `LAB-D4-04`: inspect -> hypothesize -> predict -> run -> record -> diagnose -> improve | Case-specific evidence board | `CORE`; second intervention is `OPTIONAL` |
| 15:50-16:10 | 20 | Explain why | Team defense: wrong/evidence/change/result/why/next | Score using outline weights; peers submit one challenge question | `CORE` |
| 16:10-16:20 | 10 | Final assess | `CHECK-D4-03`, `CHECK-D4-04`; individual unfamiliar-scenario response | Individual transfer evidence | `CORE` |
| 16:20-16:30 | 10 | Buffer | Recovery and close | No new content | Protected |

### Day 4 short activities

| ID | Minutes embedded | Format | Prompt and debrief |
|---|---:|---|---|
| `ACT-D4-01` | 10 | Cost council | Decide whether missing fraud or blocking a legitimate transaction dominates; derive metric/threshold priorities. |
| `ACT-D4-02` | 7 | Model detective | Match four hidden learning curves to healthy, underfit, overfit, and optimization-failure stories. |
| `ACT-D4-03` | 8 | Engineering trade-off | Choose between near-equal-quality models given a latency/size/throughput objective; defend the constraint. |
| `ACT-D4-04` | 8 | Evaluation design | Define slices, graders, human checks, and regressions needed to support "better at coding." |

### Day 4 lesson integration and cut lines

| Lesson | Core idea | Launches | First cut if behind |
|---|---|---|---|
| `LESSON-D4-01` | Metric choice begins with the cost of errors | `ACT-D4-01`, `LAB-D4-01` | ROC derivation |
| `LESSON-D4-02` | Curves distinguish fit, generalization, and optimization | `ACT-D4-02`, `LAB-D4-02` | Extra mystery curve |
| `LESSON-D4-03` | Aggregate metrics hide actionable error categories | `LAB-D4-02` | Extended shift taxonomy |
| `LESSON-D4-04` | One controlled experiment maximizes causal information | `LAB-D4-03`, `LAB-D4-04` | Hyperparameter catalogue |
| `LESSON-D4-05` | Reproducibility makes a result usable by a team | `LAB-D4-03` | Nondeterminism internals |
| `LESSON-D4-06` | Production decisions optimize a quality/resource frontier | `ACT-D4-03`, `LAB-D4-03` | Quantization/mixed-precision implementation |
| `LESSON-D4-07` | Frontier categories reuse the same scientific loop | `ACT-D4-04` | Category implementation detail |
| `LESSON-D4-08` | A strong engineer defends the evidence chain, not just the score | `LAB-D4-04` | Second capstone run |

## Assessment Map

### Challenge artifact map

| Day | Participant artifact | Instructor solution/rationale |
|---|---|---|
| 1 | `courseware/day-1/challenges/day-1-challenges.md` | `courseware/instructor-solutions/day-1/day-1-challenges-SOLUTION.md` |
| 2 | `courseware/day-2/challenges/day-2-challenges.md` | `courseware/instructor-solutions/day-2/day-2-challenges-SOLUTION.md` |
| 3 | `courseware/day-3/challenges/day-3-challenges.md` | `courseware/instructor-solutions/day-3/day-3-challenges-SOLUTION.md` |
| 4 | `courseware/day-4/challenges/day-4-challenges.md` | `courseware/instructor-solutions/day-4/day-4-challenges-SOLUTION.md` |

### Daily check map

| Day | Checks | Format | Participant artifact | Instructor rationale |
|---|---|---|---|---|
| 1 | `CHECK-D1-01` through `CHECK-D1-04` | Model-choice defense, shape ticket, XOR diagnosis, mystery forward explanation | `courseware/day-1/assessments/day-1-checks.md` | `courseware/instructor-solutions/day-1/day-1-checks-SOLUTION.md` |
| 2 | `CHECK-D2-01` through `CHECK-D2-04` | Loss/output match, gradient/LR prediction, batch repair, broken-loop diagnosis | `courseware/day-2/assessments/day-2-checks.md` | `courseware/instructor-solutions/day-2/day-2-checks-SOLUTION.md` |
| 3 | `CHECK-D3-01` through `CHECK-D3-04` | CNN shapes, leak repair, generalization rescue, transfer/attention/scale decision | `courseware/day-3/assessments/day-3-checks.md` | `courseware/instructor-solutions/day-3/day-3-checks-SOLUTION.md` |
| 4 | `CHECK-D4-01` through `CHECK-D4-04` | Metric decision, error diagnosis, experiment record, capstone/transfer defense | `courseware/day-4/assessments/day-4-checks.md` | `courseware/instructor-solutions/day-4/day-4-checks-SOLUTION.md` |

Rationales, acceptable alternatives, completed challenge responses, and misconception-based distractors appear only in instructor artifacts.

## Instructor Guide Production Map

| Guide section | Required content |
|---|---|
| Before class | Environment/cache check, datasets, checkpoints, slide assets, expected runtimes, fallback screenshots/results |
| Daily opening | Narrative question, retrieval prompt, outcome, agenda, prior-day misconceptions to sample |
| Timed block | IDs, objective, "must land" point, talking points, visual cue, prediction, launch/debrief, cut line |
| Lab facilitation | Pair/team roles, checkpoints, observation prompts, expected ranges, hint ladder, recovery path |
| Assessment | Prompt timing, evidence to collect, scoring/rationale, remediation decision |
| Daily close | Three takeaways, transition, optional/reference route, next-day preparation |

## Slide Production Plan

Slides are required and content-bearing. Each source deck must render to PDF, include alt text/notes for visuals, and pass a clipping/link/legibility check.

| Deck | Approx. slides | Required visual sequence | Activity/assessment slides |
|---|---:|---|---|
| Day 1: See It | 32 | AI landscape; neuron anatomy; boundary slider frames; linear/XOR boundaries; shape map; activation small multiples; forward trace; hidden representation | Four prediction prompts, four lab launch/debrief pairs, exit bridge |
| Day 2: Train It | 34 | Training loop; loss confidence comparison; LR paths; computational graph; gradient table; batch shape map; NumPy/PyTorch side-by-side; broken curves | Four activity prompts, four lab launch/debrief pairs, framework mapping check |
| Day 3: Scale It | 36 | Feature hierarchy; pipeline provenance; leak contrast; kernel animation frames; feature maps; overfit/rescue curves; transfer scoreboard; token map; resource chart | Four activity prompts, four lab launch/debrief pairs, three-part exit gate |
| Day 4: Engineer It | 30 + capstone brief | Confusion/cost matrix; threshold sweep; mystery curves; error buckets; experiment record; quality/resource frontier; frontier case gallery; capstone evidence board | Four activity prompts, four lab launch/debrief pairs, defense rubric, individual transfer |

Decks do not duplicate Student Guide prose. A slide should reveal one relationship, solicit one decision, or support one transition.

## Pacing Recovery Rules

1. Spend the protected buffer only on recovery, questions, or completing a core debrief.
2. Cut `OPTIONAL` and `SHORTEN` material before reducing participant prediction or debrief time.
3. Use precomputed outputs when live training exceeds the notebook runtime ceiling; still require participants to interpret evidence.
4. Never skip the Student PASS setup/checkpoint path to gain lecture time.
5. On Day 4, preserve at least 95 minutes of capstone work and 20 minutes of defense; compress the frontier gallery before the capstone.
6. Record material moved out of live delivery in the Student Guide reference path so objective coverage remains visible.
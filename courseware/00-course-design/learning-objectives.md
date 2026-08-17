# Learning Objectives and Evidence Map

## ID Contract

- `OBJ-Dx-yy`: observable course objective derived from the authoritative outline.
- `LESSON-Dx-yy`: Student Guide and instructor-guide lesson section.
- `LAB-Dx-yy`: substantial participant notebook with a separate solution.
- `ACT-Dx-yy`: short demo, prediction, diagnosis, or trade-off activity.
- `CHECK-Dx-yy`: scored or reviewed evidence of learning.

IDs are immutable once downstream production starts. A lesson may support several objectives, but each objective requires at least one practice artifact and one assessment artifact.

## Evidence Artifact Path Contract

The 31 objective IDs and their mappings below are unchanged. Participant evidence artifacts use day-local paths, while completed answers and rationales remain in the central instructor-only tree.

| Day | Student Guide | Participant challenges | Participant daily checks | Instructor challenge/check answers |
|---|---|---|---|---|
| 1 | `courseware/day-1/student-guide/day-1-student-guide.md` | `courseware/day-1/challenges/day-1-challenges.md` | `courseware/day-1/assessments/day-1-checks.md` | `courseware/instructor-solutions/day-1/day-1-challenges-SOLUTION.md`; `courseware/instructor-solutions/day-1/day-1-checks-SOLUTION.md` |
| 2 | `courseware/day-2/student-guide/day-2-student-guide.md` | `courseware/day-2/challenges/day-2-challenges.md` | `courseware/day-2/assessments/day-2-checks.md` | `courseware/instructor-solutions/day-2/day-2-challenges-SOLUTION.md`; `courseware/instructor-solutions/day-2/day-2-checks-SOLUTION.md` |
| 3 | `courseware/day-3/student-guide/day-3-student-guide.md` | `courseware/day-3/challenges/day-3-challenges.md` | `courseware/day-3/assessments/day-3-checks.md` | `courseware/instructor-solutions/day-3/day-3-challenges-SOLUTION.md`; `courseware/instructor-solutions/day-3/day-3-checks-SOLUTION.md` |
| 4 | `courseware/day-4/student-guide/day-4-student-guide.md` | `courseware/day-4/challenges/day-4-challenges.md` | `courseware/day-4/assessments/day-4-checks.md` | `courseware/instructor-solutions/day-4/day-4-challenges-SOLUTION.md`; `courseware/instructor-solutions/day-4/day-4-checks-SOLUTION.md` |

The canonical `LAB-D4-04` evidence pair is `courseware/capstone/capstone-starter.ipynb` and the instructor-only `courseware/capstone/capstone-solution.ipynb`. Its participant brief and scoring evidence live in `courseware/capstone/capstone-student-guide.md` and `courseware/capstone/capstone-rubric.md`; no participant artifact may link to the solution or `courseware/capstone/capstone-instructor-guide.md`.

## Day 1 Objectives: How Neural Networks Actually Work

| Objective | Observable performance | Prerequisite | Instruction | Practice | Assessment |
|---|---|---|---|---|---|
| `OBJ-D1-01` | Given a problem/data scenario, place neural networks within AI/ML/deep learning and justify a neural or simpler baseline; distinguish training from inference and parameters from hyperparameters. | Basic supervised-learning vocabulary introduced in section | `LESSON-D1-01` | Model-choice cases in `ACT-D1-01` and `LAB-D1-01` | `CHECK-D1-01`: choose and defend a model family |
| `OBJ-D1-02` | Label inputs, weights, bias, weighted sum, activation, layer, output, parameters, and hyperparameters in a small network and state each role. | `OBJ-D1-01` | `LESSON-D1-02`, `LESSON-D1-04` | `LAB-D1-01`, `LAB-D1-03` | `CHECK-D1-02`: annotate architecture and count parameters |
| `OBJ-D1-03` | Compute `z = w dot x + b`, convert it to a prediction, and explain geometrically how changing weights or bias moves a 2D boundary. | `OBJ-D1-02` | `LESSON-D1-02` | `ACT-D1-01`, `ACT-D1-02`, `LAB-D1-01` | `CHECK-D1-01`: predict boundary movement and explain it |
| `OBJ-D1-04` | Examine data and a boundary plot and determine whether one linear boundary can represent the required classification. | `OBJ-D1-03` | `LESSON-D1-03` | `LAB-D1-02` | `CHECK-D1-03`: diagnose linear failure on XOR |
| `OBJ-D1-05` | Explain why composing only linear layers remains linear and how hidden units plus nonlinear activations create a nonlinear decision region. | `OBJ-D1-04` | `LESSON-D1-03`, `LESSON-D1-05` | `ACT-D1-03`, `LAB-D1-02`, `LAB-D1-03` | `CHECK-D1-03`: correct the "more linear layers" misconception |
| `OBJ-D1-06` | Trace one example and a batch through a small dense network, reporting matrix/bias shapes, parameter count, activations, output probabilities, and prediction. | `OBJ-D1-02`, `OBJ-D1-05` | `LESSON-D1-04`, `LESSON-D1-06` | `ACT-D1-04`, `LAB-D1-03`, `LAB-D1-04` | `CHECK-D1-02`, `CHECK-D1-04` |
| `OBJ-D1-07` | Complete a vectorized NumPy forward network and use outputs, hidden representations, and decision regions to explain correct and incorrect cases. | `OBJ-D1-06` | `LESSON-D1-06` | `LAB-D1-04` | `CHECK-D1-04`: mystery-prediction explanation |

### Day 1 readiness evidence

A participant is ready for Day 2 when they can trace a forward pass, identify that the fixed parameters caused the observed errors, and articulate that learning needs an error signal plus a rule for changing parameters.

## Day 2 Objectives: How Neural Networks Learn

| Objective | Observable performance | Prerequisite | Instruction | Practice | Assessment |
|---|---|---|---|---|---|
| `OBJ-D2-01` | Order initialization, forward pass, loss, backward pass, update, and repetition; distinguish an epoch, iteration, batch, training loop, and inference loop. | `OBJ-D1-06` | `LESSON-D2-01` | Loop tracing in `LAB-D2-03`, `LAB-D2-04` | `CHECK-D2-01`: sequence and explain the loop |
| `OBJ-D2-02` | Select MSE, binary cross-entropy, or categorical cross-entropy for a stated task/output and explain why loss and accuracy can move differently. | `OBJ-D1-03`, output heads from `OBJ-D1-06` | `LESSON-D2-02` | `ACT-D2-01`, `LAB-D2-01`, `LAB-D2-04` | `CHECK-D2-01`: match task/output/loss/metric |
| `OBJ-D2-03` | Use slope and update direction to predict whether a learning rate will crawl, converge, oscillate, or diverge and justify the result from curves. | `OBJ-D2-02` | `LESSON-D2-02` | `ACT-D2-02`, `LAB-D2-01`, `LAB-D2-03` | `CHECK-D2-02`: predict and diagnose update behavior |
| `OBJ-D2-04` | Trace local derivative times upstream gradient through a tiny graph, calculate selected weight/bias gradients, and validate them numerically. | `OBJ-D2-02`, `OBJ-D2-03` | `LESSON-D2-03` | `LAB-D2-02`, reuse in `LAB-D2-03` | `CHECK-D2-02`: chain-rule trace and mechanism explanation |
| `OBJ-D2-05` | Convert a one-example computation to a batch computation, label tensor dimensions, explain broadcasting, and repair a shape mismatch. | `OBJ-D1-06` | `LESSON-D2-04` | `ACT-D2-03`, `LAB-D2-03`, `LAB-D2-04` | `CHECK-D2-03`: batch-shape repair |
| `OBJ-D2-06` | Implement initialization, vectorized forward pass, stable loss, backpropagation, updates, training loop, accuracy, and learning curves for a small NumPy network. | `OBJ-D2-01` through `OBJ-D2-05` | `LESSON-D2-05` | `LAB-D2-03` | `CHECK-D2-03`: executable checkpoint plus explanation |
| `OBJ-D2-07` | Express the same workflow with PyTorch tensors, `nn.Module`, autograd, loss, optimizer, gradient reset, and train/eval mode. | `OBJ-D2-06` | `LESSON-D2-06` | `LAB-D2-04` | `CHECK-D2-04`: map framework calls to automated mechanics |
| `OBJ-D2-08` | Given curves, metrics, shapes, or a short training loop, diagnose high/low learning rate, wrong output/loss, missing nonlinearity/normalization, gradient accumulation, shape errors, or mode errors and propose a discriminating check. | `OBJ-D2-01` through `OBJ-D2-07` | `LESSON-D2-07`, `LESSON-D2-08` | `ACT-D2-04`, `LAB-D2-04` | `CHECK-D2-04`: break/fix diagnosis with cause |

### Day 2 readiness evidence

A participant is ready for Day 3 when they can map PyTorch operations back to the training loop, read a learning curve, and distinguish implementation/optimization failure from a model that is merely limited.

## Day 3 Objectives: From Neural Networks to Modern Deep Learning

| Objective | Observable performance | Prerequisite | Instruction | Practice | Assessment |
|---|---|---|---|---|---|
| `OBJ-D3-01` | Compare depth, width, capacity, parameter count, and hierarchical feature reuse; explain why deeper is not automatically better and identify optimization risks. | `OBJ-D1-05`, `OBJ-D2-08` | `LESSON-D3-01` | `ACT-D3-01`, comparisons in `LAB-D3-02`, `LAB-D3-03` | `CHECK-D3-01`: architecture/feature reasoning |
| `OBJ-D3-02` | Construct reproducible train/validation/test handling with stratification, training-only preprocessing, batching/shuffling, and transformations; identify leakage and imbalance. | `OBJ-D2-05`, `OBJ-D2-07` | `LESSON-D3-02` | `ACT-D3-02`, `LAB-D3-01` | `CHECK-D3-02`: repair a leaked pipeline |
| `OBJ-D3-03` | Explain locality, kernels, stride, padding, channels, feature maps, pooling, sharing, receptive fields, and classification heads; train and inspect a compact CNN. | `OBJ-D3-01`, `OBJ-D3-02` | `LESSON-D3-03` | `ACT-D3-03`, `LAB-D3-02` | `CHECK-D3-01`: infer shapes and feature role |
| `OBJ-D3-04` | Use training/validation curves to distinguish underfitting, overfitting, and unstable optimization, then deliberately produce a generalization gap. | `OBJ-D2-08`, `OBJ-D3-01` | `LESSON-D3-04` | `LAB-D3-03` | `CHECK-D3-03`: diagnose curve evidence |
| `OBJ-D3-05` | Choose and apply a justified intervention among weight decay, dropout, early stopping, augmentation, smaller architecture, or more data and evaluate before/after evidence. | `OBJ-D3-04` | `LESSON-D3-05` | `LAB-D3-03` | `CHECK-D3-03`: defend the rescue mechanism |
| `OBJ-D3-06` | Compare training from scratch, frozen feature extraction, and partial/full fine-tuning using validation quality, time, data volume, and domain match. | `OBJ-D3-01`, `OBJ-D3-02`, `OBJ-D3-05` | `LESSON-D3-06` | `LAB-D3-04` | `CHECK-D3-04`: choose a transfer strategy |
| `OBJ-D3-07` | Describe attention as learned relevance using query/key/value intuition, place self-attention and positional information in a Transformer block, and connect pretraining/fine-tuning to foundation models without treating attention as a complete explanation. | `OBJ-D1-02`, `OBJ-D2-01`, `OBJ-D3-06` | `LESSON-D3-07` | `ACT-D3-04` | `CHECK-D3-04`: explain mechanism and limitation |
| `OBJ-D3-08` | Explain how memory, throughput, communication, checkpointing, utilization, latency, reliability, and data pipelines become constraints at scale. | `OBJ-D2-05`, `OBJ-D3-01` | `LESSON-D3-08` | Resource comparison in `LAB-D3-04` and `ACT-D3-04` debrief | `CHECK-D3-04`: reason about a scale trade-off |

### Day 3 readiness evidence

A participant is ready for Day 4 when they reject suspicious validation evidence, can read generalization curves, can justify transfer rather than assume it always wins, and can name a resource trade-off that a quality metric omits.

## Day 4 Objectives: Think Like an ML Engineer

| Objective | Observable performance | Prerequisite | Instruction | Practice | Assessment |
|---|---|---|---|---|---|
| `OBJ-D4-01` | Given asymmetric error consequences and class imbalance, select a baseline, metric set, and threshold; interpret precision, recall, F1, confusion matrix, PR trade-off, and ROC/AUC overview appropriately. | `OBJ-D2-02`, `OBJ-D3-02` | `LESSON-D4-01` | `ACT-D4-01`, `LAB-D4-01` | `CHECK-D4-01`: consequence-aware metric decision |
| `OBJ-D4-02` | Classify learning evidence as high bias, high variance, healthy training, or optimization failure and distinguish training from validation/test evidence. | `OBJ-D3-04`, `OBJ-D3-05` | `LESSON-D4-02` | `ACT-D4-02`, `LAB-D4-02` | `CHECK-D4-02`: mystery-curve diagnosis |
| `OBJ-D4-03` | Inspect mistakes, create meaningful error buckets/slices, identify label/data/distribution issues, and estimate which intervention has the highest likely payoff. | `OBJ-D3-02`, `OBJ-D4-01`, `OBJ-D4-02` | `LESSON-D4-03` | `LAB-D4-02`, `LAB-D4-04` | `CHECK-D4-02` and capstone diagnosis score |
| `OBJ-D4-04` | Establish a baseline, state a falsifiable hypothesis, choose one high-information intervention, declare expected evidence, and stop or continue based on results. | `OBJ-D4-02`, `OBJ-D4-03` | `LESSON-D4-04` | `LAB-D4-03`, `LAB-D4-04` | `CHECK-D4-03` and capstone experiment-design score |
| `OBJ-D4-05` | Record architecture, hyperparameters, data/split version, seed, metrics, runtime, and checkpoint; reproduce a run within a stated tolerance. | `OBJ-D2-07`, `OBJ-D3-02` | `LESSON-D4-05` | `LAB-D4-03`, `LAB-D4-04` | `CHECK-D4-03` and capstone reproducibility evidence |
| `OBJ-D4-06` | Compare CPU/GPU, batch, precision, size, memory, latency, throughput, and quality trade-offs and justify a deployment-oriented choice. | `OBJ-D2-05`, `OBJ-D3-08` | `LESSON-D4-06` | `ACT-D4-03`, `LAB-D4-03`, `LAB-D4-04` | `CHECK-D4-03` and capstone efficiency score |
| `OBJ-D4-07` | Map the course's hypothesis/evaluation loop to capability improvement, graders/evaluations, regression diagnosis, data quality, efficiency, safety evaluation, and internal-behavior analysis. | All earlier daily outcomes | `LESSON-D4-07` | `ACT-D4-04`, capstone role cards | `CHECK-D4-04`: unfamiliar frontier-work scenario |
| `OBJ-D4-08` | Improve or meaningfully diagnose a model and defend what was wrong, supporting evidence, intervention, result, mechanism, constraints, and next experiment. | `OBJ-D4-01` through `OBJ-D4-07` | `LESSON-D4-08` | `LAB-D4-04` and team defense | `CHECK-D4-04`, capstone rubric, individual transfer response |

## Retrieval and Reinforcement Plan

| Retrieval point | Earlier knowledge reused | New context |
|---|---|---|
| Day 2 opening | Forward pass, parameters, activation choices | Add loss, responsibility, and updates |
| Day 2 PyTorch reveal | NumPy mechanics and shape tracking | Identify what autograd/modules automate |
| Day 3 opening | Hidden representations and training failures | Depth, hierarchy, initialization, normalization |
| Day 3 leakage lab | Training/validation distinction | Prove that invalid data handling invalidates metrics |
| Day 3 transfer lab | Feature reuse and generalization | Pretrained representation and domain match |
| Day 4 metrics lab | Loss vs. metric, validation split | Consequence-aware thresholding |
| Day 4 detective lab | Day 2 failure curves and Day 3 generalization | Separate optimization, bias, variance, and data errors |
| Capstone | Full course loop | Unscaffolded diagnosis and defended intervention |

## Assessment Coverage Audit

- Every objective maps to at least one `CHECK` or a named capstone rubric dimension.
- No daily check is pure vocabulary recall; each uses a scenario, prediction, diagnosis, comparison, mechanism, or transfer task.
- Team capstone evidence is paired with an individual transfer response.
- Checks occur before the course advances to a dependent concept, enabling remediation rather than post-course discovery.
- Released check prompts resolve to the day-local assessment paths above; answer rationales resolve only to the central instructor solution paths.
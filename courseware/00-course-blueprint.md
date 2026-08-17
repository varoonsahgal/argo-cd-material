# Neural Networks and Deep Learning: Canonical Course Blueprint

**Status:** Phase 1 architecture baseline  
**Authority:** `neural-networks-outline.md` is the source of truth.  
**Delivery model:** Four in-person or live-virtual days, 09:00-16:30, 450 elapsed minutes per day including a 60-minute lunch, two 15-minute breaks, assessment, and recovery buffer.  
**Learning loop:** **Explain -> Visualize -> Predict -> Experiment -> Observe -> Diagnose -> Explain Why**

This file is the canonical orchestration contract. The files under `courseware/00-course-design/` expand its objective, flow, lab, and production details without changing IDs, paths, scope labels, or time budgets.

## 1. Course Promise

Participants will move from inspecting one neuron's decision boundary to investigating and defending a complete neural-network experiment. They will not merely call a framework API: they will predict behavior, expose the mathematics through visuals, build key mechanics, deliberately create failures, diagnose evidence, choose constrained interventions, and explain why results changed.

By the end, a participant can answer: **What is the model doing, how do I know, what should I try next, and what evidence would justify that decision?**

## 2. Audience Assumptions and Prerequisites

### Intended audience

- Software engineers, data practitioners, technical analysts, and early-career ML engineers who can read Python but are new to neural-network mechanics.
- Participants who benefit from an engineering-first bridge from NumPy models to PyTorch and modern deep-learning practice.

### Required entering skills

- Write and run basic Python: functions, loops, conditionals, lists, and dictionaries.
- Read basic NumPy arrays and plots; a 20-minute pre-course primer is provided for participants who need it.
- Interpret an average and a 2D coordinate plot.
- No calculus, linear algebra, GPU, or prior deep-learning course is assumed.

### Environment contract

- Primary environment: Jupyter notebook in Google Colab or local Python 3.11+.
- Core dependencies: NumPy, matplotlib, scikit-learn, PyTorch, and torchvision only in image/transfer labs.
- CPU is the required baseline. GPU is an optional accelerator, never a prerequisite for completing the core path.
- Datasets are generated locally or supplied by scikit-learn unless an image lab explicitly uses a small torchvision download. Day 3 includes a cached/offline fallback plan.
- Seeds, package versions, device choice, expected runtime, and sanity ranges appear in every notebook.

## 3. Final Learning Outcomes

The outline's 31 objectives are preserved as stable IDs. Full wording and traceability live in `courseware/00-course-design/learning-objectives.md`.

### Day 1: See It

- `OBJ-D1-01` Place neural networks within ML, deep learning, generative AI, and practical model selection.
- `OBJ-D1-02` Describe inputs, weights, biases, activations, layers, outputs, parameters, and hyperparameters.
- `OBJ-D1-03` Explain and geometrically interpret how one neuron transforms input into a prediction.
- `OBJ-D1-04` Distinguish linear and nonlinear decision boundaries.
- `OBJ-D1-05` Explain why hidden layers and nonlinear activations are necessary.
- `OBJ-D1-06` Perform forward propagation through a small network while tracking shapes.
- `OBJ-D1-07` Build and investigate a forward-only NumPy network.

### Day 2: Train It

- `OBJ-D2-01` Explain the complete training loop and distinguish it from inference.
- `OBJ-D2-02` Distinguish loss functions from evaluation metrics and match loss to output design.
- `OBJ-D2-03` Explain gradient descent, learning rate, convergence, oscillation, and divergence.
- `OBJ-D2-04` Explain and calculate practical backpropagation using computational graphs and the chain rule.
- `OBJ-D2-05` Explain why vectorization, tensors, broadcasting, and mini-batches matter.
- `OBJ-D2-06` Build and train a small NumPy network from scratch.
- `OBJ-D2-07` Rebuild the workflow with PyTorch autograd, modules, losses, and optimizers.
- `OBJ-D2-08` Diagnose common training failures from symptoms and evidence.

### Day 3: Scale It

- `OBJ-D3-01` Explain depth, capacity, hierarchical representation learning, and optimization difficulty.
- `OBJ-D3-02` Build reliable train/validation/test data pipelines without leakage.
- `OBJ-D3-03` Explain CNN mechanics and train a compact image classifier.
- `OBJ-D3-04` Diagnose and intentionally create overfitting and underfitting.
- `OBJ-D3-05` Apply regularization, early stopping, and data augmentation using before/after evidence.
- `OBJ-D3-06` Explain and compare feature extraction, freezing, and fine-tuning.
- `OBJ-D3-07` Describe attention, Transformers, pretraining, fine-tuning, and foundation models conceptually.
- `OBJ-D3-08` Explain how scale changes memory, throughput, distributed training, reliability, and serving constraints.

### Day 4: Think Like an ML Engineer

- `OBJ-D4-01` Select evaluation metrics and thresholds based on error consequences.
- `OBJ-D4-02` Diagnose bias, variance, optimization failure, underfitting, and overfitting.
- `OBJ-D4-03` Perform structured, slice-based error analysis and prioritize likely improvements.
- `OBJ-D4-04` Design targeted, hypothesis-driven experiments under constraints.
- `OBJ-D4-05` Track and reproduce experiments, checkpoints, data versions, and results.
- `OBJ-D4-06` Explain training and inference trade-offs across quality, latency, throughput, memory, and size.
- `OBJ-D4-07` Connect course mechanics to representative frontier ML engineering problem categories.
- `OBJ-D4-08` Improve a model and defend the diagnosis, intervention, evidence, efficiency, and next step.

## 4. Four-Day Narrative Arc

| Day | Narrative question | Conceptual progression | Tangible outcome |
|---|---|---|---|
| 1 | How can simple operations produce intelligent-looking behavior? | Landscape -> neuron geometry -> linear limitation -> hidden transformations -> forward propagation | A forward-only NumPy network plus an evidence-based explanation of its failures |
| 2 | When a network is wrong, how does it know what to change? | Loss -> slopes -> chain rule -> vectorization -> training loop -> autograd -> debugging | The same small network trained from scratch and in PyTorch, with failures diagnosed |
| 3 | How do these fundamentals become modern deep learning? | Depth -> data validity -> CNNs -> generalization -> transfer -> attention -> systems scale | A compact image workflow with leakage, overfitting, regularization, and transfer evidence |
| 4 | The model trained; is it good, and what should change next? | Consequence-aware metrics -> error analysis -> experiment design -> reproducibility -> efficiency -> frontier cases -> capstone | A defensible model investigation and five-minute engineering defense |

Prerequisite chain: Day 1 forward mechanics -> Day 2 gradients/training -> Day 3 architectures/generalization -> Day 4 evidence-driven decisions. Retrieval prompts at each day's opening deliberately reuse the previous day's artifacts.

## 5. Time Allocation by Section

All rows sum to 450 elapsed minutes per day. Labs include their immediate prediction and evidence debrief unless a separate debrief row is shown. The final buffer protects questions, environment recovery, and transitions; it is not planned content.

### Day 1 timing: See It

| Time | Min | Mode | IDs and focus |
|---|---:|---|---|
| 09:00-09:25 | 25 | Explain + retrieval | `LESSON-D1-01`: AI/ML/deep-learning landscape, training vs. inference, when simpler models win |
| 09:25-09:55 | 30 | Visualize + predict | `LESSON-D1-02`, `ACT-D1-01`: neuron geometry and boundary sliders |
| 09:55-10:35 | 40 | Lab | `LAB-D1-01`: one-neuron boundary workshop |
| 10:35-10:50 | 15 | Break | Protected break |
| 10:50-11:15 | 25 | Explain + visualize | `LESSON-D1-03`: logistic regression, linear boundaries, XOR limitation |
| 11:15-12:00 | 45 | Lab | `LAB-D1-02`: linear limit and nonlinear data |
| 12:00-12:15 | 15 | Diagnose + check | `CHECK-D1-01`, `CHECK-D1-02`: boundary evidence and model choice |
| 12:15-13:15 | 60 | Lunch | Protected lunch |
| 13:15-13:45 | 30 | Explain + shape map | `LESSON-D1-04`, `ACT-D1-04`: layers, matrix shapes, parameter count, output heads |
| 13:45-14:02 | 17 | Explain + predict | `LESSON-D1-05`, `ACT-D1-03`: nonlinearity and activation choices |
| 14:02-14:42 | 40 | Lab | `LAB-D1-03`: shape and activation observatory |
| 14:42-14:57 | 15 | Break | Protected break |
| 14:57-15:05 | 8 | Consolidate + visualize | `LESSON-D1-06`: forward-trace consolidation |
| 15:05-16:05 | 60 | Lab | `LAB-D1-04`: network that thinks forward / mystery failures |
| 16:05-16:20 | 15 | Explain why + exit check | `CHECK-D1-03`, `CHECK-D1-04`; Day 2 bridge: "Could we automate the weights?" |
| 16:20-16:30 | 10 | Buffer | Recovery and questions |

### Day 2 timing: Train It

| Time | Min | Mode | IDs and focus |
|---|---:|---|---|
| 09:00-09:20 | 20 | Retrieval + explain | `LESSON-D2-01`: complete learning loop and inference contrast |
| 09:20-09:45 | 25 | Predict + calculate | `LESSON-D2-02`, `ACT-D2-01`: scalar loss and loss/metric distinction |
| 09:45-10:25 | 40 | Lab | `LAB-D2-01`: loss landscapes and learning-rate roulette |
| 10:25-10:40 | 15 | Break | Protected break |
| 10:40-11:10 | 30 | Visualize + explain | `LESSON-D2-03`: computational graph, local derivative x upstream gradient |
| 11:10-11:55 | 45 | Lab | `LAB-D2-02`: backpropagation gradient check |
| 11:55-12:05 | 10 | Diagnose + check | `CHECK-D2-01`, `CHECK-D2-02` |
| 12:05-13:05 | 60 | Lunch | Protected lunch |
| 13:05-13:25 | 20 | Shape map + demo | `LESSON-D2-04`: tensors, batch dimensions, broadcasting, vectorization |
| 13:25-14:35 | 70 | Major lab | `LAB-D2-03`: train a NumPy network from scratch |
| 14:35-14:50 | 15 | Break | Protected break |
| 14:50-15:10 | 20 | Side-by-side reveal | `LESSON-D2-05`, `LESSON-D2-06`: what PyTorch automates |
| 15:10-16:05 | 55 | Lab + break/fix | `LAB-D2-04`: autograd and broken training loops |
| 16:05-16:20 | 15 | Frontier connection + exit | `LESSON-D2-07`, `LESSON-D2-08`, `CHECK-D2-03`, `CHECK-D2-04` |
| 16:20-16:30 | 10 | Buffer | Recovery and questions |

### Day 3 timing: Scale It

| Time | Min | Mode | IDs and focus |
|---|---:|---|---|
| 09:00-09:15 | 15 | Retrieval + feature ladder | `LESSON-D3-01`: depth, width, capacity, hierarchy, initialization preview |
| 09:15-09:35 | 20 | Explain + predict | `LESSON-D3-02`: splits, normalization, transformations, class balance, leakage |
| 09:35-10:20 | 45 | Lab | `LAB-D3-01`: find the data leak |
| 10:20-10:35 | 15 | Break | Protected break |
| 10:35-11:00 | 25 | Visualize | `LESSON-D3-03`, `ACT-D3-03`: kernels, maps, sharing, receptive fields |
| 11:00-12:00 | 60 | Lab | `LAB-D3-02`: compact CNN and feature-map inspection |
| 12:00-12:10 | 10 | Diagnose + check | `CHECK-D3-01`: shape and feature evidence |
| 12:10-13:10 | 60 | Lunch | Protected lunch |
| 13:10-13:25 | 15 | Explain + predict | `LESSON-D3-04`, `LESSON-D3-05`: training stability and generalization |
| 13:25-14:20 | 55 | Lab | `LAB-D3-03`: make it overfit, then rescue it |
| 14:20-14:35 | 15 | Break | Protected break |
| 14:35-14:50 | 15 | Explain + choose | `LESSON-D3-06`: feature extraction, freezing, fine-tuning, domain match |
| 14:50-15:45 | 55 | Lab | `LAB-D3-04`: transfer-learning race |
| 15:45-16:05 | 20 | Conceptual bridge | `LESSON-D3-07`, `LESSON-D3-08`, `ACT-D3-04`: attention and scale |
| 16:05-16:20 | 15 | Explain why + exit | `CHECK-D3-02` through `CHECK-D3-04` |
| 16:20-16:30 | 10 | Buffer | Recovery and questions |

### Day 4 timing: Think Like an ML Engineer

| Time | Min | Mode | IDs and focus |
|---|---:|---|---|
| 09:00-09:15 | 15 | Retrieval + baseline | `LESSON-D4-01`: evaluation starts with consequences, not a favorite metric |
| 09:15-09:35 | 20 | Scenario + visualize | `ACT-D4-01`: fraud costs, confusion matrix, thresholds, PR/ROC overview |
| 09:35-10:15 | 40 | Lab | `LAB-D4-01`: accuracy is not enough |
| 10:15-10:30 | 15 | Break | Protected break |
| 10:30-10:45 | 15 | Explain + detective | `LESSON-D4-02`: bias, variance, generalization, optimization failure |
| 10:45-11:25 | 40 | Lab | `LAB-D4-02`: mystery curves and error buckets |
| 11:25-11:35 | 10 | Debrief + check | `CHECK-D4-01`, `CHECK-D4-02` |
| 11:35-12:35 | 60 | Lunch | Protected lunch |
| 12:35-12:55 | 20 | Explain + trade-off | `LESSON-D4-03` through `LESSON-D4-06`: one-change experiments, tracking, efficiency |
| 12:55-13:45 | 50 | Lab | `LAB-D4-03`: one experiment, tracked and benchmarked |
| 13:45-14:00 | 15 | Break | Protected break |
| 14:00-14:15 | 15 | Case gallery | `LESSON-D4-07`, `ACT-D4-04`: seven frontier problem categories mapped to the course loop |
| 14:15-15:50 | 95 | Capstone lab | `LAB-D4-04`: neural network investigation |
| 15:50-16:10 | 20 | Team defense | Capstone evidence board and scored five-minute defense |
| 16:10-16:20 | 10 | Final assessment | `CHECK-D4-03`, `CHECK-D4-04` and individual transfer response |
| 16:20-16:30 | 10 | Buffer | Recovery, close, and next-step references |

## 6. Objective-to-Evidence Map

Student-guide sections use the same lesson IDs as headings. Each objective has instruction, practice, and assessment evidence.

| Objective | Student guide / lesson | Practice evidence | Assessment evidence |
|---|---|---|---|
| `OBJ-D1-01` | `LESSON-D1-01` | `ACT-D1-01`, model-choice cases in `LAB-D1-01` | `CHECK-D1-01` |
| `OBJ-D1-02` | `LESSON-D1-02`, `LESSON-D1-04` | `LAB-D1-01`, `LAB-D1-03` | `CHECK-D1-02` |
| `OBJ-D1-03` | `LESSON-D1-02` | `LAB-D1-01`, `ACT-D1-02` | `CHECK-D1-01` |
| `OBJ-D1-04` | `LESSON-D1-03` | `LAB-D1-02` | `CHECK-D1-03` |
| `OBJ-D1-05` | `LESSON-D1-03`, `LESSON-D1-05` | `LAB-D1-02`, `LAB-D1-03` | `CHECK-D1-03` |
| `OBJ-D1-06` | `LESSON-D1-04`, `LESSON-D1-06` | `ACT-D1-04`, `LAB-D1-03`, `LAB-D1-04` | `CHECK-D1-02`, `CHECK-D1-04` |
| `OBJ-D1-07` | `LESSON-D1-06` | `LAB-D1-04` | `CHECK-D1-04` |
| `OBJ-D2-01` | `LESSON-D2-01` | `LAB-D2-03`, `LAB-D2-04` | `CHECK-D2-01` |
| `OBJ-D2-02` | `LESSON-D2-02` | `ACT-D2-01`, `LAB-D2-01`, `LAB-D2-04` | `CHECK-D2-01` |
| `OBJ-D2-03` | `LESSON-D2-02` | `ACT-D2-02`, `LAB-D2-01`, `LAB-D2-03` | `CHECK-D2-02` |
| `OBJ-D2-04` | `LESSON-D2-03` | `LAB-D2-02`, `LAB-D2-03` | `CHECK-D2-02` |
| `OBJ-D2-05` | `LESSON-D2-04` | `ACT-D2-03`, `LAB-D2-03`, `LAB-D2-04` | `CHECK-D2-03` |
| `OBJ-D2-06` | `LESSON-D2-05` | `LAB-D2-03` | `CHECK-D2-03` |
| `OBJ-D2-07` | `LESSON-D2-06` | `LAB-D2-04` | `CHECK-D2-04` |
| `OBJ-D2-08` | `LESSON-D2-07` | `ACT-D2-04`, `LAB-D2-04` | `CHECK-D2-04` |
| `OBJ-D3-01` | `LESSON-D3-01` | `ACT-D3-01`, `LAB-D3-02`, `LAB-D3-03` | `CHECK-D3-01` |
| `OBJ-D3-02` | `LESSON-D3-02` | `LAB-D3-01`, `ACT-D3-02` | `CHECK-D3-02` |
| `OBJ-D3-03` | `LESSON-D3-03` | `ACT-D3-03`, `LAB-D3-02` | `CHECK-D3-01` |
| `OBJ-D3-04` | `LESSON-D3-04` | `LAB-D3-03` | `CHECK-D3-03` |
| `OBJ-D3-05` | `LESSON-D3-05` | `LAB-D3-03` | `CHECK-D3-03` |
| `OBJ-D3-06` | `LESSON-D3-06` | `LAB-D3-04` | `CHECK-D3-04` |
| `OBJ-D3-07` | `LESSON-D3-07` | `ACT-D3-04` and attention prediction | `CHECK-D3-04` |
| `OBJ-D3-08` | `LESSON-D3-08` | resource trade-off in `LAB-D3-04` | `CHECK-D3-04` |
| `OBJ-D4-01` | `LESSON-D4-01` | `ACT-D4-01`, `LAB-D4-01` | `CHECK-D4-01` |
| `OBJ-D4-02` | `LESSON-D4-02` | `ACT-D4-02`, `LAB-D4-02` | `CHECK-D4-02` |
| `OBJ-D4-03` | `LESSON-D4-03` | `LAB-D4-02`, `LAB-D4-04` | `CHECK-D4-02`, capstone rubric |
| `OBJ-D4-04` | `LESSON-D4-04` | `LAB-D4-03`, `LAB-D4-04` | `CHECK-D4-03`, capstone rubric |
| `OBJ-D4-05` | `LESSON-D4-05` | `LAB-D4-03`, `LAB-D4-04` | `CHECK-D4-03`, capstone rubric |
| `OBJ-D4-06` | `LESSON-D4-06` | `ACT-D4-03`, `LAB-D4-03`, `LAB-D4-04` | `CHECK-D4-03`, capstone rubric |
| `OBJ-D4-07` | `LESSON-D4-07` | `ACT-D4-04`, capstone role cards | `CHECK-D4-04` |
| `OBJ-D4-08` | `LESSON-D4-08` | `LAB-D4-04` and team defense | `CHECK-D4-04`, capstone rubric |

## 7. Lesson, Demo, Lab, and Challenge Map

### Student Guide plan and integration contract

Each daily Student Guide is a participant-facing narrative, not an answer key. Every `LESSON` section ends with: a prediction prompt, a direct launch link to the next `LAB` or `ACT`, an observation lens, and a post-activity "explain why" debrief. Lab notebooks link back to prerequisite lesson IDs and forward to the debrief heading. Completed code, prediction answers, expected interpretations, and instructor recovery notes remain exclusively in instructor artifacts.

| Day | Student Guide path | Lesson sequence | Integrated primary labs |
|---|---|---|---|
| 1 | `courseware/day-1/student-guide/day-1-student-guide.md` | `LESSON-D1-01` through `LESSON-D1-06` | `LAB-D1-01` through `LAB-D1-04` |
| 2 | `courseware/day-2/student-guide/day-2-student-guide.md` | `LESSON-D2-01` through `LESSON-D2-08` | `LAB-D2-01` through `LAB-D2-04` |
| 3 | `courseware/day-3/student-guide/day-3-student-guide.md` | `LESSON-D3-01` through `LESSON-D3-08` | `LAB-D3-01` through `LAB-D3-04` |
| 4 | `courseware/day-4/student-guide/day-4-student-guide.md` | `LESSON-D4-01` through `LESSON-D4-08` | `LAB-D4-01` through `LAB-D4-04` |

### Primary lab inventory

All 16 primary labs are Jupyter notebooks. Exact purpose, TODOs, data, flows, expected behavior, runtime, dependencies, and validation criteria are specified in `courseware/00-course-design/lab-map.md`.

| ID | Participant notebook | Instructor solution | Live min |
|---|---|---|---:|
| `LAB-D1-01` | `courseware/day-1/labs/LAB-D1-01-neuron-boundary.ipynb` | `courseware/instructor-solutions/day-1/LAB-D1-01-neuron-boundary-SOLUTION.ipynb` | 40 |
| `LAB-D1-02` | `courseware/day-1/labs/LAB-D1-02-linear-limit.ipynb` | `courseware/instructor-solutions/day-1/LAB-D1-02-linear-limit-SOLUTION.ipynb` | 45 |
| `LAB-D1-03` | `courseware/day-1/labs/LAB-D1-03-shapes-activations.ipynb` | `courseware/instructor-solutions/day-1/LAB-D1-03-shapes-activations-SOLUTION.ipynb` | 40 |
| `LAB-D1-04` | `courseware/day-1/labs/LAB-D1-04-forward-network-mystery.ipynb` | `courseware/instructor-solutions/day-1/LAB-D1-04-forward-network-mystery-SOLUTION.ipynb` | 60 |
| `LAB-D2-01` | `courseware/day-2/labs/LAB-D2-01-loss-learning-rate.ipynb` | `courseware/instructor-solutions/day-2/LAB-D2-01-loss-learning-rate-SOLUTION.ipynb` | 40 |
| `LAB-D2-02` | `courseware/day-2/labs/LAB-D2-02-backprop-gradient-check.ipynb` | `courseware/instructor-solutions/day-2/LAB-D2-02-backprop-gradient-check-SOLUTION.ipynb` | 45 |
| `LAB-D2-03` | `courseware/day-2/labs/LAB-D2-03-numpy-training.ipynb` | `courseware/instructor-solutions/day-2/LAB-D2-03-numpy-training-SOLUTION.ipynb` | 70 |
| `LAB-D2-04` | `courseware/day-2/labs/LAB-D2-04-pytorch-break-fix.ipynb` | `courseware/instructor-solutions/day-2/LAB-D2-04-pytorch-break-fix-SOLUTION.ipynb` | 55 |
| `LAB-D3-01` | `courseware/day-3/labs/LAB-D3-01-find-data-leak.ipynb` | `courseware/instructor-solutions/day-3/LAB-D3-01-find-data-leak-SOLUTION.ipynb` | 45 |
| `LAB-D3-02` | `courseware/day-3/labs/LAB-D3-02-cnn-feature-maps.ipynb` | `courseware/instructor-solutions/day-3/LAB-D3-02-cnn-feature-maps-SOLUTION.ipynb` | 60 |
| `LAB-D3-03` | `courseware/day-3/labs/LAB-D3-03-overfit-and-rescue.ipynb` | `courseware/instructor-solutions/day-3/LAB-D3-03-overfit-and-rescue-SOLUTION.ipynb` | 55 |
| `LAB-D3-04` | `courseware/day-3/labs/LAB-D3-04-transfer-learning-race.ipynb` | `courseware/instructor-solutions/day-3/LAB-D3-04-transfer-learning-race-SOLUTION.ipynb` | 55 |
| `LAB-D4-01` | `courseware/day-4/labs/LAB-D4-01-accuracy-is-not-enough.ipynb` | `courseware/instructor-solutions/day-4/LAB-D4-01-accuracy-is-not-enough-SOLUTION.ipynb` | 40 |
| `LAB-D4-02` | `courseware/day-4/labs/LAB-D4-02-model-detective.ipynb` | `courseware/instructor-solutions/day-4/LAB-D4-02-model-detective-SOLUTION.ipynb` | 40 |
| `LAB-D4-03` | `courseware/day-4/labs/LAB-D4-03-one-experiment.ipynb` | `courseware/instructor-solutions/day-4/LAB-D4-03-one-experiment-SOLUTION.ipynb` | 50 |
| `LAB-D4-04` | `courseware/capstone/capstone-starter.ipynb` | `courseware/capstone/capstone-solution.ipynb` | 95 |

### Short challenge and demo map

Daily participant challenge briefs are day-local. Completed responses, expected evidence, and facilitation rationales stay in the central instructor-only tree.

| Day | Participant challenge artifact | Instructor solution/rationale |
|---|---|---|
| 1 | `courseware/day-1/challenges/day-1-challenges.md` | `courseware/instructor-solutions/day-1/day-1-challenges-SOLUTION.md` |
| 2 | `courseware/day-2/challenges/day-2-challenges.md` | `courseware/instructor-solutions/day-2/day-2-challenges-SOLUTION.md` |
| 3 | `courseware/day-3/challenges/day-3-challenges.md` | `courseware/instructor-solutions/day-3/day-3-challenges-SOLUTION.md` |
| 4 | `courseware/day-4/challenges/day-4-challenges.md` | `courseware/instructor-solutions/day-4/day-4-challenges-SOLUTION.md` |

| Day | ID | Pattern and evidence |
|---|---|---|
| 1 | `ACT-D1-01` | Decision-boundary sliders: predict which parameter rotates or translates the boundary |
| 1 | `ACT-D1-02` | Be the neural network: manually choose weights, then explain why automation is needed |
| 1 | `ACT-D1-03` | Activation card sort: predict saturation, negative-input behavior, and output suitability |
| 1 | `ACT-D1-04` | Shape relay: determine matrices, bias vectors, and parameter counts for `4 -> 8 -> 3` |
| 2 | `ACT-D2-01` | Loss ranking: order prediction vectors before calculating cross-entropy |
| 2 | `ACT-D2-02` | Gradient descent animation: predict crawl, convergence, oscillation, or divergence |
| 2 | `ACT-D2-03` | Batch shape map: trace one, 32, and 1,024 examples through the same operation |
| 2 | `ACT-D2-04` | Broken-curve detective: diagnose high/low learning rate, missing nonlinearity, or no zero-grad |
| 3 | `ACT-D3-01` | Feature ladder: infer what early, middle, and late representations can encode |
| 3 | `ACT-D3-02` | Leakage accusation: identify which pipeline step used validation knowledge |
| 3 | `ACT-D3-03` | Kernel reveal: predict edge-map output before exposing the convolution result |
| 3 | `ACT-D3-04` | Attention token map: predict relationships, then discuss why attention is not a complete explanation |
| 4 | `ACT-D4-01` | Fraud-cost council: choose metrics and thresholds from asymmetric error costs |
| 4 | `ACT-D4-02` | Mystery learning curves: classify healthy, underfit, overfit, and optimization failure |
| 4 | `ACT-D4-03` | Speed vs. quality: choose between models using latency, size, throughput, and quality |
| 4 | `ACT-D4-04` | Frontier evaluation design: define evidence that a coding model is actually better |

### Instructor Guide map

Create `courseware/instructor-guide/day-1-instructor-guide.md` through `day-4-instructor-guide.md`. Each guide mirrors the timed rows, contains talking points, prediction commitments, visual cues, lab launch/debrief scripts, expected misconceptions, recovery options, and explicit core/optional boundaries. The canonical capstone facilitation artifact is `courseware/capstone/capstone-instructor-guide.md`; it contains role cards, reveal schedule, scoring calibration, alternative diagnoses, and time-box recovery and is instructor-only.

### Slide plan

Slides are required production artifacts, not an empty directory. Create editable Markdown source and rendered PDF for each day:

- `courseware/slides/day-1-see-it.md` and `day-1-see-it.pdf`: approximately 32 slides.
- `courseware/slides/day-2-train-it.md` and `day-2-train-it.pdf`: approximately 34 slides.
- `courseware/slides/day-3-scale-it.md` and `day-3-scale-it.pdf`: approximately 36 slides.
- `courseware/slides/day-4-think-like-an-ml-engineer.md` and matching PDF: approximately 30 slides plus capstone brief.

Decks carry only high-value visuals, prompts, evidence, and transitions. Dense reference detail stays in Student Guides. Every deck includes lab launch and debrief slides with IDs, daily retrieval, checks, and a final takeaway. Slide sources must identify asset paths and alt text; PDFs must be render-checked before release.

### Capstone architecture

`LAB-D4-04` uses the scikit-learn digits dataset framed as handwritten routing-code recognition. Teams receive a reproducible PyTorch MLP baseline, fixed train/validation/test splits, existing curves, latency/size measurements, an imbalanced slice, selected mislabeled or difficult examples, and a constrained experiment budget. The target is not a universal accuracy number: teams must improve macro-F1 or a declared high-cost slice without unacceptable test degradation or latency growth.

Phases: investigate -> state diagnosis -> predict -> select one primary experiment -> run and record -> inspect slices -> decide whether evidence supports the hypothesis -> make one bounded follow-up if time permits -> defend. The score preserves the outline weights: model performance 25%, generalization 20%, experimental design 20%, diagnosis 15%, efficiency 10%, explanation 10%. The individual final response prevents team performance from masking individual understanding.

The top-level capstone package is the single source of truth:

| Path | Audience and canonical function |
|---|---|
| `courseware/capstone/capstone-student-guide.md` | Participant brief, constraints, deliverables, and evidence-board/defense instructions |
| `courseware/capstone/capstone-starter.ipynb` | Canonical participant implementation of `LAB-D4-04`; no duplicate Day 4 lab notebook |
| `courseware/capstone/capstone-solution.ipynb` | Canonical instructor solution for `LAB-D4-04`; instructor-only despite its required top-level path |
| `courseware/capstone/capstone-rubric.md` | Participant-visible scoring dimensions and weights without answer content |
| `courseware/capstone/capstone-instructor-guide.md` | Instructor-only case assignment, hints, calibration, reveal, and recovery guidance |

Participant files may link only to the capstone Student Guide, starter notebook, and rubric. They must never link to `capstone-solution.ipynb` or `capstone-instructor-guide.md`. Access controls and release packaging must exclude both instructor-only files from participant distributions. No mirrored solution notebook is planned; `courseware/instructor-solutions/day-4/capstone-case-key.md` may supplement the canonical solution without duplicating it.

## 8. Assessment Strategy

Assessment samples prediction, mechanism, diagnosis, decision, and transfer rather than vocabulary recall.

| ID | Evidence type | Decision enabled |
|---|---|---|
| `CHECK-D1-01` | Choose neural network vs. simpler baseline; explain neuron boundary movement | Correct landscape and neuron misconceptions before layers |
| `CHECK-D1-02` | Shape/parameter-count worked ticket | Confirm readiness for vectorized forward propagation |
| `CHECK-D1-03` | Diagnose why linear models and stacked linear layers fail XOR | Confirm nonlinearity mechanism |
| `CHECK-D1-04` | Explain a mystery forward prediction from hidden activations | Day 2 readiness gate |
| `CHECK-D2-01` | Match output, loss, metric, and task; sequence the loop | Correct objective-function confusion |
| `CHECK-D2-02` | Predict learning-rate behavior and trace one chain-rule path | Confirm optimization/backprop model |
| `CHECK-D2-03` | Repair batch shapes and explain vectorization | Confirm implementation readiness |
| `CHECK-D2-04` | Diagnose a broken PyTorch loop from curves/code | Day 3 readiness gate |
| `CHECK-D3-01` | Infer CNN shapes and feature-map role | Confirm CNN mechanics |
| `CHECK-D3-02` | Find leakage and propose a valid split/preprocessing order | Confirm data validity |
| `CHECK-D3-03` | Classify generalization pattern and justify rescue | Confirm evidence-based regularization |
| `CHECK-D3-04` | Choose transfer strategy and explain attention/scale trade-off | Day 4 readiness gate |
| `CHECK-D4-01` | Select metric/threshold for asymmetric costs | Confirm consequence-aware evaluation |
| `CHECK-D4-02` | Diagnose curve plus error slices and prioritize action | Confirm structured error analysis |
| `CHECK-D4-03` | Write one tracked hypothesis/change/expected evidence record | Capstone experiment gate |
| `CHECK-D4-04` | Capstone defense plus individual unfamiliar-scenario transfer | Final outcome evidence |

Participant daily checks live at `courseware/day-1/assessments/day-1-checks.md` through `courseware/day-4/assessments/day-4-checks.md`. Instructor-only rationales and scoring anchors live at `courseware/instructor-solutions/day-1/day-1-checks-SOLUTION.md` through `courseware/instructor-solutions/day-4/day-4-checks-SOLUTION.md`. Daily exit evidence is used to adapt the next day's retrieval, not simply scored and discarded.

## 9. Visual Teaching Opportunities

| Visual | IDs | Invisible relationship made observable |
|---|---|---|
| AI landscape and scale bridge | `LESSON-D1-01` | What changes and what remains recognizable from one neuron to foundation models |
| Interactive decision boundary | `LESSON-D1-02`, `LAB-D1-01` | Weight rotation vs. bias translation |
| Linear vs. nonlinear boundary | `LAB-D1-02` | Why XOR defeats one boundary |
| Layer/tensor shape map | `LESSON-D1-04`, `ACT-D2-03` | How examples and dimensions move through matrices |
| Activation small multiples | `ACT-D1-03`, `LAB-D1-03` | Saturation, dead regions, and output semantics |
| Forward/backward dual trace | `LESSON-D2-01`, `LESSON-D2-03` | Activations forward, responsibility backward |
| Loss surface with learning-rate paths | `LAB-D2-01` | Crawl, convergence, oscillation, divergence |
| Gradient-check table | `LAB-D2-02` | Analytic vs. finite-difference agreement |
| Data-pipeline provenance diagram | `LAB-D3-01` | Where leakage enters and which statistics belong to training |
| CNN kernel and feature-map progression | `LESSON-D3-03`, `LAB-D3-02` | Pixels -> edges/textures -> class evidence |
| Before/after learning curves | `LAB-D3-03` | Intervention effects on generalization gap |
| Attention/token map with caveat | `ACT-D3-04` | Learned relevance without claiming complete explanation |
| Confusion matrix and threshold sweep | `LAB-D4-01` | Aggregate score vs. consequential error types |
| Quality/latency/size frontier | `ACT-D4-03`, `LAB-D4-03` | Production trade-offs rather than one "best" model |
| Capstone evidence board | `LAB-D4-04` | Hypothesis -> change -> result -> interpretation chain |

## 10. Modern-Practice and Industry Connections

- Day 1 connects a single neuron's enduring components to CNNs, attention, Transformers, and foundation models without claiming architectural equivalence.
- Day 2 maps the experiment loop to training, post-training, reward signals, graders, evaluation loops, data pipelines, and model-behavior diagnostics.
- Day 3 grounds modern practice in data provenance, reusable representations, pretrained models, hardware-aware batching, checkpointing, throughput, latency, and reliability.
- Day 4 uses a bounded seven-case gallery: capability improvement, evaluation design, regression diagnosis, data quality, efficiency, safety evaluation, and internal-behavior analysis.
- Claims about current APIs, pretrained weights, determinism, hardware behavior, or contemporary frontier practice require primary-source verification during production and a source note in instructor material.
- Reinforcement learning, distributed training, quantization, mechanistic interpretability, and safety systems are conceptual connections, not implementation outcomes for this introductory four-day course.

## 11. Risk and Overload Analysis

No outline objective is removed. Scope labels determine live depth.

| Day | Decision | Material | Rationale and treatment |
|---|---|---|---|
| 1 | KEEP | Neuron -> linear limit -> hidden nonlinearity -> NumPy forward path | The causal spine for all later work |
| 1 | SHORTEN | AI landscape and historical evolution | 25-minute framing; detailed model taxonomy becomes reference |
| 1 | OPTIONAL | Leaky-ReLU nuance and extended output-head cases | Preserve in Student Guide callouts after core activation choices |
| 2 | KEEP | Loss, learning rate, backprop, scratch training, framework reveal, debugging | Required bridge from mechanism to practice |
| 2 | SHORTEN | Symbolic derivative algebra | One tiny graph and gradient check; no long derivation sequence |
| 2 | MOVE | Full vanishing/exploding-gradient treatment | Preview on Day 2; revisit with depth/initialization on Day 3 |
| 2 | OPTIONAL | Optimizer internals beyond practical SGD/Adam comparison | Reference extension, not live implementation |
| 3 | KEEP | Valid pipeline, CNN, overfit/rescue, transfer comparison | Highest-value practical deep-learning path |
| 3 | SHORTEN | Depth/initialization overview and training knobs | Concepts recur inside labs instead of separate lectures |
| 3 | MOVE | Transformer equations and distributed-system implementation | Reference depth; live path remains conceptual visual and trade-off discussion |
| 3 | OPTIONAL | Full fine-tuning and extended augmentation sweep | Core uses frozen features/head; optional path unfreezes a final block if runtime permits |
| 4 | KEEP | Metrics, bias/variance, error analysis, one-change experiments, tracking, efficiency, capstone | Directly supports final engineering outcome |
| 4 | SHORTEN | Seven frontier problem categories | One 15-minute case gallery plus capstone role cards; no claim of job mastery |
| 4 | MOVE | Mixed-precision implementation, model parallelism, quantization, deep interpretability | Reference pages connected to the live quality/resource frontier |
| 4 | OPTIONAL | Second capstone intervention | Allowed only after the primary hypothesis is evaluated and recorded |

Primary delivery risks and mitigations:

- **Four labs per day can fragment learning.** Student Guide transition contracts and immediate debriefs make each notebook one step in the daily investigation rather than four unrelated exercises.
- **Day 3 downloads and CPU variability can consume the day.** Preflight/cache instructions, reduced deterministic subsets, a supplied feature-embedding fallback, and hard epoch caps are required.
- **Scratch backprop can overload novices.** Limit manual differentiation to one small graph; use a numerical gradient check and then reuse the pattern in the full network.
- **Day 4 capstone can become random tuning.** Require diagnosis, expected evidence, one primary change, experiment record, and defense before any follow-up run.
- **Team work can hide individual gaps.** Daily exit checks and the final individual transfer response remain individually completed.
- **Notebook solutions can leak.** Participant and instructor trees are physically separate; review includes a leakage scan and no hidden answer cells.

## 12. Proposed Output File Tree

```text
courseware/
|-- 00-course-blueprint.md
|-- 00-course-design/
|   |-- course-architecture.md
|   |-- learning-objectives.md
|   |-- course-flow.md
|   |-- lab-map.md
|   `-- artifact-generation-plan.md
|-- 01-insight-map.md
|-- shared/
|   |-- environment.md
|   |-- glossary.md
|   |-- notation-and-style.md
|   `-- assets/
|-- day-1/
|   |-- student-guide/day-1-student-guide.md
|   |-- labs/LAB-D1-*.ipynb
|   |-- challenges/day-1-challenges.md
|   `-- assessments/day-1-checks.md
|-- day-2/
|   |-- student-guide/day-2-student-guide.md
|   |-- labs/LAB-D2-*.ipynb
|   |-- challenges/day-2-challenges.md
|   `-- assessments/day-2-checks.md
|-- day-3/
|   |-- student-guide/day-3-student-guide.md
|   |-- labs/LAB-D3-*.ipynb
|   |-- challenges/day-3-challenges.md
|   `-- assessments/day-3-checks.md
|-- day-4/
|   |-- student-guide/day-4-student-guide.md
|   |-- labs/LAB-D4-0[1-3]-*.ipynb
|   |-- challenges/day-4-challenges.md
|   `-- assessments/day-4-checks.md
|-- capstone/
|   |-- capstone-student-guide.md
|   |-- capstone-starter.ipynb
|   |-- capstone-solution.ipynb [INSTRUCTOR-ONLY; exclude from participant release]
|   |-- capstone-rubric.md
|   `-- capstone-instructor-guide.md [INSTRUCTOR-ONLY; exclude from participant release]
|-- instructor-guide/
|   `-- day-1-instructor-guide.md ... day-4-instructor-guide.md
|-- instructor-solutions/
|   `-- day-1/ ... day-4/
|       |-- LAB-Dx-yy-*-SOLUTION.ipynb [15 non-capstone lab solutions]
|       |-- day-x-challenges-SOLUTION.md
|       |-- day-x-checks-SOLUTION.md
|       `-- capstone-case-key.md [day 4 only]
|-- slides/
|   `-- day-1-see-it.md/.pdf ... day-4-think-like-an-ml-engineer.md/.pdf
|-- reviews/
|   |-- participant-validation-LAB-Dx-yy.md
|   |-- solution-validation-LAB-Dx-yy.md
|   |-- pedagogy-day-1.md ... pedagogy-day-4.md
|   `-- artifact-audit.md
|-- validation/
|   |-- student-lab-test-report.md
|   |-- instructor-solution-test-report.md
|   |-- pedagogy-review.md
|   `-- final-course-review.md
`-- 99-final-quality-report.md
```

The repeated day directories expand to 15 participant lab notebooks and 15 central solution notebooks; the canonical `LAB-D4-04` participant/solution pair is in `courseware/capstone/`, yielding the unchanged total of 16 path pairs. Detailed per-lab/day reports remain under `courseware/reviews/`; the four files under `courseware/validation/` consolidate and link that evidence rather than replacing it. The generation order and ownership contract are in `courseware/00-course-design/artifact-generation-plan.md`.

## 13. Definition of Done

Architecture is complete when:

- All 31 outline objectives have stable IDs and instruction, practice, and assessment evidence.
- Four daily schedules each total 450 elapsed minutes and visibly include explanation, visuals, prediction, experiment, observation, diagnosis, debrief, breaks, assessment, and buffer.
- The 16 participant notebook paths pair one-to-one with 16 separate instructor solution paths, with `LAB-D4-04` canonically paired as `courseware/capstone/capstone-starter.ipynb` and the instructor-only `courseware/capstone/capstone-solution.ipynb`.
- Core, shortened, moved, optional, and reference depth are explicit; no objective disappears silently.
- Student Guide, instructor guide, slide, challenge, assessment, review, validation, and capstone artifacts have owners and dependencies.

The complete course is classroom-ready only when:

- Every lesson follows the course loop and links to its integrated activity and debrief.
- Every participant notebook contains starter state and TODOs but no completed answers or instructor notes.
- Every primary lab receives execution-based **Student PASS** (or accepted **PASS WITH NOTES**) from Lab Tester.
- Only after Student PASS, every separate solution is completed and executed by Lab Solution Engineer and receives **Solution PASS** (or accepted **PASS WITH NOTES**).
- A lab is releaseable only when **Student PASS + Solution PASS** are both recorded and no solution leakage is found.
- Pedagogy reviews for all four days are addressed, with labs re-tested whenever participant behavior changes.
- Slide source exists, rendered decks are visually checked, links resolve, and instructor timing matches the canonical schedule.
- The capstone produces an experiment record, evidence board, scored defense, and individual transfer response.
- The four consolidated validation deliverables link the detailed reports and record current gate status without deleting or replacing review evidence.
- The Course Reviewer finds no unresolved blocking/high-severity issue in `courseware/99-final-quality-report.md`.

## Ownership and Gate Summary

| Role | Owns | Cannot declare complete until |
|---|---|---|
| Course Architect | This blueprint and split design files | Objective, timing, path, and dependency audits pass |
| Lesson Developer | Student Guides, day-local challenge/check prompts, central instructor rationales, instructor guides, and slide sources | Lesson IDs, corrected paths, and lab integration match the blueprint |
| Lab Engineer | Participant notebooks only | Starter path is complete and no answer leakage exists |
| Lab Tester | Participant execution reports and `courseware/validation/student-lab-test-report.md` | Fresh ordered run, runtime, dependencies, outputs, failures, and Colab path are checked |
| Lab Solution Engineer | Separate solutions, solution-validation reports, and `courseware/validation/instructor-solution-test-report.md` | Every TODO/question is answered and clean execution passes |
| Pedagogy Reviewer | Day-level rubric reports and `courseware/validation/pedagogy-review.md` | Timing, progression, active learning, transfer, and cognitive load are assessed |
| Course Reviewer | Independent detailed quality report and `courseware/validation/final-course-review.md` | Scope, technical consistency, completeness, gates, and cross-day coherence pass |
| Course Orchestrator | Dependency order, delegations, revision loops, release ledger | Every required artifact and both lab gates are present with no unresolved blocker |

Mandatory lab state machine: **planned -> participant built -> Student PASS -> solution built -> Solution PASS -> pedagogy reviewed -> releaseable**. If a solution exposes a participant flaw, the state returns to **participant built**, followed by participant retest and solution reconciliation.
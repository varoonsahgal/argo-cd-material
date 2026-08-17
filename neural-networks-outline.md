# Neural Networks and Deep Learning

## Course Duration

**4 Days**

## Course Philosophy

This course is built around a progression:

**See It → Predict It → Build It → Break It → Diagnose It → Improve It**

The emphasis is not simply on learning neural-network terminology or calling a framework API. Participants repeatedly:

- Predict what a model will do before running it
- Visualize what is happening inside the model
- Build key components themselves
- Deliberately break models
- Diagnose model failures
- Compare experiments
- Compete in small optimization challenges
- Explain *why* an improvement worked

The mathematics becomes part of solving a mystery rather than a sequence of equations to memorize.

---

# Recurring Course Challenge Format

## Predict Before You Run

Before executing important experiments, participants make a prediction, then run the experiment and explain the result.

Examples:

- Which activation function will work better?
- What happens if the learning rate is increased 100×?
- Will adding layers improve validation accuracy?
- Which model is likely to overfit?
- Which training curve belongs to which experiment?

## Break It / Fix It

Participants periodically receive deliberately broken models and must diagnose them rather than simply rewrite them.

Possible problems include:

- Wrong learning rate
- Incorrect loss function
- Missing normalization
- Wrong output activation
- Too many parameters
- Too little data
- Data leakage
- Incorrect train/evaluation mode
- Shape mismatches

## Model Detective

Participants receive training curves, validation curves, confusion matrices, predictions, or misclassified examples and infer what may have gone wrong without initially seeing the implementation.

## Experiment Scoreboard

Teams compare experiments, but the winner is **not automatically the model with the highest accuracy**. Points can be awarded for:

- Model performance
- Generalization
- Training efficiency
- Quality of experimentation
- Correct diagnosis
- Ability to explain *why* a change helped

---

# Day 1 — How Neural Networks Actually Work

## Big Question

**How can simple mathematical operations produce intelligent-looking behavior?**

## Day 1 Learning Goals

By the end of Day 1, participants should be able to:

- Explain where neural networks fit within machine learning and modern AI
- Describe the role of inputs, weights, biases, activations, layers, and outputs
- Explain how a neuron transforms input into a prediction
- Distinguish linear and nonlinear decision boundaries
- Explain why hidden layers and nonlinear activation functions are necessary
- Perform forward propagation through a small neural network
- Build a simple forward-only network with Python and NumPy

---

## 1. Deep Learning in the Modern AI Landscape

### Topics Covered

- Artificial intelligence, machine learning, deep learning, and generative AI
- Traditional machine learning vs. neural networks
- Structured data vs. unstructured data
- Problems neural networks are especially good at:
  - Image recognition
  - Speech and audio
  - Text and language
  - Forecasting and anomaly detection
  - Representation learning
- When a simpler model may still be preferable
- Training vs. inference
- Features, labels/targets, predictions, parameters, and hyperparameters
- Supervised learning at a high level
- How deep learning fits into modern foundation-model systems

### Visual: The Evolution of Neural Networks

**Neuron → Neural Network → CNN → Attention → Transformer → Foundation Model**

### Frontier ML Engineer Connection

Ask:

**“If today’s models have billions of parameters, why are we starting with one neuron?”**

Connect the answer to the fundamentals that remain recognizable at scale:

- Inputs
- Parameters
- Activations
- Loss
- Gradients
- Optimization

---

## 2. Start with One Neuron

### Topics Covered

- The artificial neuron as a mathematical function
- Inputs and features
- Weights as learned importance values
- Bias as an adjustable offset
- Weighted sum: `z = w·x + b`
- Activation functions as transformations of the weighted sum
- Model output and prediction
- Parameters vs. hyperparameters
- Why changing a single parameter changes model behavior
- Geometric interpretation of weights and bias

### Visual Demo

Create sliders for:

- Weight 1
- Weight 2
- Bias

Watch the decision boundary move interactively.

### Challenge — Be the Neural Network

Manually adjust weights until a neuron separates several points correctly.

Then ask:

**“Could we automate the process of finding these weights?”**

This naturally sets up training on Day 2.

---

## 3. From Logistic Regression to Neural Networks

### Topics Covered

- Binary classification
- Linear decision boundaries
- Logistic regression
- Sigmoid as a probability-producing activation
- Turning probability into a class prediction
- Thresholds
- Decision boundaries
- Logistic regression as a single-neuron model
- Why a single linear boundary cannot solve every classification problem
- XOR and other nonlinearly separable patterns
- Why adding hidden units can create more complex boundaries

### Hands-on

1. Train a classifier on a linearly separable dataset
2. Visualize its decision boundary
3. Switch to a nonlinear dataset
4. Predict whether the same model will work
5. Run it and inspect the failure

### Key Insight

Hidden layers should not feel arbitrary. They are introduced because the simpler model reaches a clear limitation.

---

## 4. Building a Neural Network from Layers

### Topics Covered

- Input layer
- Hidden layers
- Output layer
- Neurons per layer
- Depth vs. width
- Fully connected/dense layers
- Weight matrices and bias vectors
- Parameter count
- Forward propagation
- Hidden representations
- Layer-by-layer transformation of data
- Output-layer design for:
  - Regression
  - Binary classification
  - Multiclass classification

### Visual

Animate one example traveling through the network:

**Input → Weighted Sums → Activations → Hidden Representation → Output → Prediction**

### Mini-Exercise

Given a network architecture such as `4 → 8 → 3`, participants determine:

- Number of layers
- Weight matrix shapes
- Bias vector shapes
- Number of trainable parameters

---

## 5. Activation Functions and Nonlinearity

### Topics Covered

- Why stacked linear layers are still only linear
- Why nonlinear activation functions are necessary
- Sigmoid
- Tanh
- ReLU
- Leaky ReLU
- Softmax
- Typical hidden-layer vs. output-layer choices
- Saturation
- Dead ReLUs
- Why sigmoid is less common in hidden layers of deep networks
- How activation choice affects information flow

### Predict Before You Run

Show multiple activation functions and ask participants to predict:

- Which saturates?
- Which has zero gradient for negative values?
- Which is commonly used for hidden layers?
- Which is appropriate for multiclass output?

---

## 6. Forward Propagation with NumPy

### Topics Covered

- Representing inputs as arrays
- Weight matrices and vectorized multiplication
- Bias broadcasting
- Applying activations
- Passing activations between layers
- Keeping track of tensor/array shapes
- Producing output probabilities
- Converting outputs into predictions

### Hands-on Lab — Build a Network That Thinks Forward

Using Python and NumPy:

1. Represent inputs as vectors
2. Create weight matrices and biases
3. Implement a neuron
4. Add a hidden layer
5. Apply activation functions
6. Implement forward propagation
7. Generate predictions
8. Visualize outputs and decision regions

No training yet.

### Day 1 Mystery

**The network predicts correctly for four examples but fails badly on two others. Why?**

Participants inspect the decision boundary and hidden representation.

---

## Day 1 Takeaway

> **A neural network is a chain of mathematical transformations. Learning determines the parameters inside those transformations.**

---

# Day 2 — How Neural Networks Learn

## Big Question

**When a neural network makes a mistake, how does it know what to change?**

## Day 2 Learning Goals

By the end of Day 2, participants should be able to:

- Explain the complete neural-network training loop
- Distinguish loss functions from evaluation metrics
- Explain gradient descent and the role of learning rate
- Describe backpropagation conceptually and mathematically at a practical level
- Explain why vectorization and mini-batches matter
- Build a small trainable neural network from scratch
- Use automatic differentiation and optimizers in a modern framework
- Diagnose common training failures

---

## 1. The Complete Learning Loop

### Topics Covered

- Initialization
- Forward propagation
- Prediction
- Ground truth
- Loss calculation
- Gradients
- Backpropagation
- Parameter updates
- Iterations and epochs
- Batch vs. mini-batch vs. full-batch training
- Training loop vs. inference loop

### Core Flow

**Predict → Measure Error → Calculate Gradients → Update Parameters → Repeat**

### Visual

Show the same network twice:

- Forward arrows carrying activations
- Backward arrows carrying gradients

---

## 2. Loss Functions

### Topics Covered

- Why optimization requires a scalar objective
- Loss for one example vs. cost across many examples
- Mean squared error
- Binary cross-entropy
- Categorical cross-entropy
- Negative log likelihood intuition
- Why loss and accuracy are different
- Matching output activation and loss function
- What decreasing loss does and does not tell you

### Predict Before You Calculate

Display several prediction vectors and ask:

**Which model should have the lowest loss?**

Participants vote before calculating the result.

---

## 3. Gradient Descent and Optimization

### Topics Covered

- Derivatives as sensitivity
- Gradients as direction and magnitude of change
- Loss surfaces
- Local slope intuition
- Parameter update rule
- Learning rate
- Small learning rate vs. large learning rate
- Oscillation and divergence
- Convergence
- Batch gradient descent vs. stochastic and mini-batch approaches
- Introductory comparison of SGD and Adam

### Highly Visual Demo — Find the Bottom

Animate gradient descent with:

- Tiny learning rate
- Excessively large learning rate
- Reasonable learning rate

### Challenge — Learning Rate Roulette

Teams predict which learning rates will:

- Converge
- Learn slowly
- Oscillate
- Diverge

Then run the experiments and compare the learning curves.

---

## 4. Backpropagation

### Topics Covered

- Why we need gradients for every trainable parameter
- Forward pass vs. backward pass
- Computational graph intuition
- Chain rule intuition
- Local derivative × upstream gradient
- Gradient flow from output layer toward earlier layers
- Weight and bias gradients
- Relationship between loss, gradient, and parameter updates
- Why backpropagation is efficient
- Vanishing-gradient preview

### Memory Model

**Forward propagation asks:** “What did I predict?”

**Loss asks:** “How wrong was I?”

**Backpropagation asks:** “Which parameters contributed to that error?”

**Optimization says:** “Change them.”

### Visual Walkthrough

Use a tiny 2-layer network and color-code:

- Activations moving forward
- Error signal moving backward
- Parameter updates

---

## 5. Vectorization, Tensors, and Mini-Batches

### Topics Covered

- Why Python loops become a bottleneck
- Matrix multiplication
- Vectorized forward propagation
- Processing multiple examples at once
- Batch dimension
- Tensor shapes
- Broadcasting
- Why GPUs are effective for neural-network workloads
- Common shape errors
- Debugging matrix-dimension mismatches

### Visual

Show the same computation for:

- 1 example
- 32 examples
- 1,024 examples

Then map the operation to matrix multiplication.

---

## 6. Build the Complete Network from Scratch

### Topics Covered

- Parameter initialization
- Forward propagation
- Loss calculation
- Gradient calculation
- Backpropagation
- Parameter updates
- Training loop
- Accuracy calculation
- Learning-curve visualization

### Major Lab — Train a Neural Network with NumPy

Participants:

1. Initialize parameters
2. Implement forward propagation
3. Calculate loss
4. Implement gradients
5. Backpropagate
6. Update parameters
7. Train across epochs
8. Plot loss
9. Generate predictions
10. Evaluate accuracy

### Experiment Extensions

- Change hidden-layer size
- Change learning rate
- Change activation
- Train longer
- Compare learning curves

---

## 7. The Great Reveal — What Modern Frameworks Automate

### Topics Covered

- Tensors
- Models and modules
- Layers
- Automatic differentiation/autograd
- Loss functions
- Optimizers
- Zeroing gradients
- Training vs. evaluation mode
- CPU vs. GPU devices
- The role of `backward()`
- The role of `optimizer.step()`

### Side-by-Side Comparison

From scratch:

**Forward → Loss → Derivatives → Backpropagation → Parameter Update**

Framework:

```python
prediction = model(x)
loss = loss_fn(prediction, y)
loss.backward()
optimizer.step()
```

Key message:

> **The framework did not remove the mathematics. It automated the mathematics we just learned.**

### Hands-on

Rebuild the NumPy model using PyTorch or Keras and compare the code paths.

---

## 8. Training Failures and Debugging

### Topics Covered

- Learning rate too high or too low
- Incorrect output activation
- Wrong loss function
- Missing nonlinear activation
- Failure to normalize inputs
- Exploding or vanishing gradients
- Failure to zero gradients
- Wrong train/eval mode
- Shape mismatches
- Loss not decreasing
- Accuracy stuck at chance level

### Challenge — Break My Neural Network

Provide several broken models. Teams diagnose and repair each one and must explain the cause.

---

## Frontier ML Engineer Connection — Training Experiments

Connect the Day 2 workflow to representative frontier-model work:

- Post-training
- Reinforcement learning
- Reward signals
- Graders
- Evaluation loops
- Model-behavior experiments
- Data pipelines
- Training diagnostics

Core scientific process:

**Hypothesis → Experiment → Measurement → Diagnosis → Next Experiment**

---

## Day 2 Takeaway

> **Training is an experiment repeated many times: predict, measure, calculate responsibility, adjust, repeat.**

---

# Day 3 — From Neural Networks to Modern Deep Learning

## Big Question

**How do the fundamentals become the systems used in modern AI?**

## Day 3 Learning Goals

By the end of Day 3, participants should be able to:

- Explain why deeper networks can learn hierarchical representations
- Build reliable data pipelines for training and validation
- Explain the key ideas behind convolutional neural networks
- Diagnose and intentionally create overfitting
- Apply regularization and data augmentation
- Explain transfer learning and fine-tuning
- Describe attention, Transformers, and foundation models at a conceptual level
- Explain how scale changes the engineering challenges around deep learning

---

## 1. From Shallow to Deep Networks

### Topics Covered

- One hidden layer vs. multiple hidden layers
- Depth vs. width
- Model capacity
- Hierarchical representation learning
- Feature reuse across layers
- Parameter count and complexity
- Why deeper is not automatically better
- Optimization difficulty in deeper networks
- Vanishing and exploding gradients
- Weight initialization
- Normalization preview

### Visual

Show increasingly rich representations:

**Raw Input → Simple Features → Intermediate Features → High-Level Features**

---

## 2. Real-World Data Pipelines

### Topics Covered

- Dataset objects
- Data loaders
- Mini-batching
- Shuffling
- Feature scaling and normalization
- Training, validation, and test splits
- Stratification
- Data transformations
- Data augmentation
- Class imbalance
- Data leakage
- Reproducible data splits
- Separating preprocessing learned from training data vs. validation/test data

### Challenge — Find the Data Leak

Provide a suspiciously high-performing model and let participants investigate how validation information accidentally leaked into training.

### Key Insight

> **A model can look excellent and still be invalid.**

---

## 3. Architecture Spotlight — Convolutional Neural Networks

### Topics Covered

- Why dense networks are inefficient for images
- Spatial locality
- Convolution kernels/filters
- Stride
- Padding
- Feature maps
- Channels
- Pooling
- Flattening and classification heads
- Parameter sharing
- Receptive field intuition
- Hierarchical feature extraction

### Visual

**Pixels → Edges → Textures → Shapes → Objects**

### Hands-on Lab — Image Classification

Build a compact CNN using a lightweight dataset such as:

- Fashion-MNIST
- CIFAR-10
- Another classroom-friendly image dataset

Participants inspect:

- Input shapes
- Feature-map shapes
- Training loss
- Validation accuracy
- Misclassified examples

---

## 4. Training Deep Networks Effectively

### Topics Covered

- SGD vs. Adam
- Learning rate
- Batch size
- Number of epochs
- Weight initialization
- Normalization
- Learning-rate scheduling
- Validation during training
- Early stopping
- Gradient clipping overview
- Monitoring learning curves
- Recognizing unstable training

### Predict Before You Run

Ask participants what they expect to happen if they:

- Double the batch size
- Increase the learning rate 10×
- Train for 10× more epochs
- Remove normalization

---

## 5. Overfitting, Underfitting, and Generalization

### Topics Covered

- Training performance vs. validation performance
- Underfitting
- Overfitting
- Generalization gap
- Model capacity
- Dataset size
- Regularization
- L2/weight decay
- Dropout
- Early stopping
- Data augmentation
- Smaller architecture

### Challenge — Make It Overfit

The goal is deliberately backwards:

**Create the most spectacularly overfit model possible.**

Participants use:

- Very little data
- A large model
- Many epochs

Then rescue the model using one or more regularization strategies.

### Before/After Learning Curves

Every intervention produces a visible before/after comparison.

---

## 6. Transfer Learning and Fine-Tuning

### Topics Covered

- Why training from scratch is often unnecessary
- Pretrained models
- Learned representations
- Feature extraction
- Freezing layers
- Replacing a classification head
- Fine-tuning some or all layers
- Learning-rate considerations during fine-tuning
- Small-data advantages
- Domain mismatch
- When transfer learning may not help

### Competition — Transfer Learning Race

Team A trains from scratch.

Team B starts from a pretrained network.

Compare:

- Validation performance
- Training time
- Number of examples needed
- Compute required

The winner must explain *why* the result occurred.

---

## 7. Modern AI Spotlight — Attention, Transformers, and Foundation Models

### Topics Covered

- Why sequence relationships are difficult for older architectures
- Attention as learned relevance between elements
- Query, key, value intuition
- Self-attention
- Token representations
- Positional information
- Transformer blocks at a conceptual level
- Pretraining
- Fine-tuning
- Foundation models
- Why the same core training mechanics still apply

### Connect Back to Fundamentals

- Weights
- Activations
- Loss
- Backpropagation
- Optimization

### Optional Visual Demo — Look Inside Attention

Use a sentence such as:

**“The dog chased the ball because it was rolling.”**

Ask participants to predict which tokens should influence one another before revealing an attention visualization.

---

## 8. Scale Changes the Engineering Problem

### Topics Covered

- GPU memory
- Training throughput
- Distributed computation
- Communication overhead
- Checkpointing
- Hardware utilization
- Inference latency
- Throughput vs. latency
- Reliability and fault tolerance
- Data-pipeline bottlenecks
- Why model scale creates systems-engineering problems

### Frontier ML Engineer Connection

Representative modern problems include:

- Large-scale training throughput
- Distributed training
- Inference optimization
- Accelerator utilization
- Checkpointing and recovery
- Serving models under latency constraints

---

## Day 3 Takeaway

> **The fundamentals do not disappear at scale. New architectures and systems challenges are built on top of them.**

---

# Day 4 — Think Like an ML Engineer

## Big Question

**The model trained successfully—but is it actually good, and what should we improve next?**

## Day 4 Learning Goals

By the end of Day 4, participants should be able to:

- Select meaningful evaluation metrics
- Diagnose bias, variance, underfitting, and overfitting
- Perform structured error analysis
- Design targeted experiments rather than random tuning
- Track and reproduce experiments
- Explain practical training and inference trade-offs
- Connect course concepts to representative frontier ML engineering work
- Improve a model and defend the reasoning behind the improvement

---

## 1. Evaluation Beyond Accuracy

### Topics Covered

- Training, validation, and test data
- Baseline models
- Accuracy
- Precision
- Recall
- F1 score
- Confusion matrices
- True positives, false positives, true negatives, false negatives
- Class imbalance
- Threshold selection
- Precision-recall trade-offs
- ROC/AUC overview
- Choosing metrics based on business or safety consequences

### Scenario Challenge — Fraud Detection

Which is worse?

- Blocking a legitimate transaction
- Missing a fraudulent transaction

Use the answer to show why metric choice depends on the real cost of mistakes.

---

## 2. Bias, Variance, and Generalization

### Topics Covered

- High bias
- High variance
- Underfitting
- Overfitting
- Training error vs. validation error
- Learning curves
- Generalization gap
- Model capacity
- Data quantity
- Diagnosing optimization problems separately from generalization problems

### Model Detective

Show unidentified learning curves and ask participants to classify them as:

- Healthy training
- Underfitting
- Overfitting
- Optimization failure

---

## 3. Error Analysis

### Topics Covered

- Why aggregate metrics hide important failures
- Inspecting individual mistakes
- Categorizing errors
- Error buckets
- Class-specific failure patterns
- Label noise
- Data quality problems
- Distribution shift
- Edge cases
- Prioritizing the highest-value improvements
- Estimating the likely payoff of an intervention

### Hands-on

Participants inspect a collection of failed predictions and propose the next experiment.

---

## 4. Experiment Design and Hyperparameter Decisions

### Topics Covered

- Hypothesis-driven experimentation
- Establishing a baseline
- Changing one major variable at a time
- Learning rate
- Batch size
- Optimizer
- Architecture
- Regularization
- More data vs. bigger model
- When to stop experimenting
- Avoiding random hyperparameter tweaking

### Challenge — You Get One Experiment

Training is expensive. Each team may change **only one thing**.

Possible options:

- More data
- Bigger model
- Smaller model
- Different optimizer
- Regularization
- Learning rate
- Data augmentation
- Transfer learning

Teams must defend their choice before running the experiment.

---

## 5. Experiment Tracking and Reproducibility

### Topics Covered

- What to record for every experiment
- Model architecture
- Hyperparameters
- Dataset/version
- Training and validation metrics
- Runtime
- Random seeds
- Sources of nondeterminism
- Checkpoints
- Best checkpoint vs. final checkpoint
- Saving and restoring model state
- Reproducing a result
- Why experiment history matters in team environments

### Hands-on

Run several controlled experiments and compare them using a simple experiment table or tracker.

---

## 6. Efficient Training and Inference

### Topics Covered

- CPU vs. GPU
- GPU memory
- Batch-size trade-offs
- Mixed precision
- Memory vs. throughput
- Training throughput
- Inference latency
- Throughput vs. latency
- Model-size trade-offs
- Batching at inference
- Why a slightly less accurate model may be preferable in production

### Classroom Challenge — Speed vs. Quality

Two models have nearly identical quality, but one is:

- 2× faster
- Half the size

Which is better depends on the deployment objective.

---

# Frontier AI Lab — What Problems Might an ML Engineer Actually Work On?

This section connects course fundamentals to representative work performed by ML engineers at frontier AI organizations. It is intentionally framed around public, general problem categories rather than proprietary systems.

## Problem 1 — Improve a Model Capability

### Topics Covered

- Improving reasoning
- Coding ability
- Tool use
- Long-horizon task completion
- Training-example design
- Post-training
- Reinforcement learning concepts
- Reward signals
- Comparing model variants
- Failure analysis

### Mini-Challenge

Give two models slightly different training data and determine which improved and what evidence supports that conclusion.

---

## Problem 2 — Build Better Evaluations

### Topics Covered

- Evaluation datasets
- Benchmark design
- Automated graders
- Human evaluation
- Edge cases
- Regression testing
- Capability vs. benchmark gaming
- What “better” actually means

### Challenge

Design an evaluation for:

**“Is this model actually better at coding?”**

---

## Problem 3 — Diagnose a Model Regression

### Topics Covered

- Capability regressions
- Comparing model versions
- Data vs. training vs. evaluation failures
- Slice-based analysis
- Reproduction
- Root-cause hypotheses

### Challenge

Given two model reports, determine what additional evidence is needed before deciding why the newer model is worse on one category.

---

## Problem 4 — Improve Training Data

### Topics Covered

- Data quality
- Data filtering
- Dataset composition
- Difficult examples
- Human feedback
- Synthetic data concepts
- Labeling quality
- Data pipelines
- Training-environment design

### Challenge — Data Beats Model

Team A may modify architecture.

Team B may modify data.

Compare which intervention produces the larger improvement.

---

## Problem 5 — Make Models Faster and Cheaper

### Topics Covered

- Latency
- Throughput
- GPU utilization
- Memory
- Batching
- Model parallelism overview
- Quantization awareness
- Reliability
- Cost-performance trade-offs

### Challenge

Choose between two models with similar quality but very different serving costs.

---

## Problem 6 — Make Models Safer

### Topics Covered

- Safety evaluations
- High-risk error categories
- Classifiers and filters
- Red-team style testing
- Distribution shift
- Capability/safety trade-offs
- Why average accuracy may hide the most important failures

### Challenge — Accuracy Is Not Enough

A model is 99% accurate, but the remaining 1% contains the highest-risk failures.

Ask:

**“Is this actually a good model?”**

---

## Problem 7 — Understand What Happens Inside the Model

### Topics Covered

- Activations
- Saliency
- Feature maps
- Attention patterns
- Attribution
- Representation analysis
- Interpretability limitations
- Why understanding internal behavior is difficult

### Visual Demo

Inspect which inputs or internal features appear to drive a prediction.

---

# The Frontier ML Engineer Mindset

The recurring pattern is not simply:

**Build a bigger model.**

It is:

**What are we trying to improve?**

↓

**How will we measure it?**

↓

**What experiment should we run?**

↓

**What actually happened?**

↓

**Why?**

↓

**What should we try next?**

---

# Capstone — The Neural Network Investigation

The capstone should feel like receiving a real ML engineering problem rather than following a tutorial.

Participants receive:

- A dataset
- A business/problem statement
- A baseline model
- Existing training results
- A performance target
- Limited experiment time

## Phase 1 — Investigate

- Examine the dataset
- Examine existing metrics
- Inspect learning curves
- Inspect errors
- Identify suspicious patterns
- Form a hypothesis

## Phase 2 — Predict

Each team states:

- What they think is wrong
- What evidence supports the hypothesis
- What experiment would test it

## Phase 3 — Experiment

Possible interventions:

- Learning rate
- Architecture
- Regularization
- Dropout
- Data augmentation
- Optimizer
- Batch size
- More data
- Transfer learning

## Phase 4 — Diagnose

Determine whether the primary limitation was:

- Data
- Bias
- Variance
- Optimization
- Architecture
- Evaluation
- Compute constraints

## Phase 5 — Improve

Record every experiment as:

**Hypothesis → Change → Result → Interpretation**

---

# Final Capstone Scoreboard

Do **not** rank teams solely by model accuracy.

### Model Performance — 25%

Did the model improve?

### Generalization — 20%

Does it perform well on unseen data?

### Experimental Design — 20%

Were experiments purposeful?

### Diagnosis — 15%

Did the team correctly identify model problems?

### Efficiency — 10%

Did they consider runtime and complexity?

### Explanation — 10%

Can they explain *why* their changes produced the observed results?

This changes the goal from:

**“Who randomly found the best hyperparameters?”**

into:

**“Who demonstrated the strongest ML engineering thinking?”**

---

# Final Challenge — Defend Your Model

Each team gets five minutes to answer:

1. What was wrong with the original model?
2. What evidence led you to that conclusion?
3. What did you change?
4. What happened?
5. Why do you believe it happened?
6. What would you try next with another hour?

---

# The Four-Day Journey

## Day 1 — See It

**How does a neural network make a prediction?**

Build intuition around neurons, layers, activations, and forward propagation.

## Day 2 — Train It

**How does the network learn?**

Understand loss, gradient descent, backpropagation, vectorization, autograd, and optimization.

## Day 3 — Scale It

**How do these ideas become modern deep learning?**

Move into deep networks, CNNs, data pipelines, regularization, transfer learning, attention, Transformers, and scaling challenges.

## Day 4 — Think Like an ML Engineer

**Something is not good enough. How do I determine what to do next?**

Evaluate, experiment, diagnose, improve, optimize, and explain.

---

# Final Course Outcome

Participants progress through:

**Predict → Build → Train → Break → Measure → Diagnose → Improve → Explain**

The goal is no longer simply:

> **“I know how to train a neural network.”**

The stronger outcome is:

> **“I can look at a machine-learning problem, form a hypothesis, design an experiment, understand what happened, and decide what to try next.”**

# Neural Networks Course Glossary

This glossary is the shared terminology contract for participant and instructor materials. Day 1 terms are defined at the depth needed for **See It**. Later-day terms should be added when their lessons are produced, not pre-taught here.

## Landscape and Workflow

| Term | Course meaning | Do not confuse with |
|---|---|---|
| Artificial intelligence (AI) | A broad family of systems and methods designed to perform tasks associated with intelligent behavior. | A single model type or only neural networks. |
| Machine learning (ML) | A way to build behavior by fitting model parameters from data rather than specifying every rule directly. | All AI systems. Some AI systems use explicit rules or search. |
| Deep learning | Machine learning with neural networks containing learned intermediate representations, commonly across multiple layers. | A guarantee that the model is better than a simpler baseline. |
| Generative AI | Models and systems that produce new content such as text, images, audio, or code. | All deep learning; many neural networks classify or forecast instead of generating content. |
| Supervised learning | Learning from examples paired with desired targets. | The Day 1 forward-only labs, which use fixed or externally fitted parameters and do not train a neural network. |
| Training | The process that uses data and an objective to change model parameters. | Inference, which uses already-set parameters. Training mechanics begin on Day 2. |
| Inference | Running a model forward with fixed parameters to produce an output or prediction. | Evaluation, which compares outputs with targets using chosen evidence. |
| Baseline | A simple, credible reference approach used to establish what improvement must beat or justify. | An intentionally poor model. A useful baseline should be valid and informative. |

## Data and Model Elements

| Term | Course meaning | Day 1 example or note |
|---|---|---|
| Example | One observation presented to the model. | One point with two coordinates. |
| Input | The values supplied to a model for one example or a batch. | A vector `x`, or batch matrix `X`. |
| Feature | One measured or constructed input dimension. | Horizontal coordinate `x1` or vertical coordinate `x2`. |
| Label / target | The desired outcome associated with an example. Use **target** in explanations and `y` in formulas/code. | Binary class `0` or `1`. |
| Prediction | The model output after applying the course's stated decision rule. | Probability at least `0.5` becomes class `1` in a binary example. |
| Parameter | A value inside the model that training can adjust. | Weights and biases. Day 1 may inspect fixed parameters. |
| Hyperparameter | A setting chosen outside the parameter-learning process. | Hidden width, learning rate, or decision threshold when configured externally. |
| Weight | A parameter that scales or mixes input evidence. | Components of `w` or entries of `W`. |
| Bias | An additive model parameter that shifts a pre-activation independently of the current input values. | `b` in `z = w dot x + b`. This is distinct from social or statistical bias. |
| Pre-activation | The affine result before an activation function. | `z = w dot x + b` for one neuron. |
| Activation function | A transformation applied to a pre-activation. | Sigmoid, tanh, ReLU, or Leaky ReLU. Softmax is used across multiclass logits. |
| Activation | The value produced by an activation function. | `a = ReLU(z)`. |
| Neuron / unit | A small parameterized computation that forms a pre-activation and usually applies an activation. | `a = g(w dot x + b)`. It is a mathematical model, not a biological replica. |
| Layer | A collection of units evaluated as one shape-constrained transformation. | `A = g(XW + b)`. |
| Dense / fully connected layer | A layer in which every input feature can contribute to every output unit. | A weight matrix has shape `(d_in, d_out)`. |
| Input layer | A diagram label for values entering a network. | It normally contributes no trainable parameters by itself. |
| Hidden layer | A layer between input and output whose activations form an intermediate representation. | Hidden units need not map to named human concepts. |
| Output layer / head | The final transformation chosen to match the task's output. | One sigmoid probability for the Day 1 binary network; three softmax probabilities for a three-class example. |
| Depth | The number of successive parameterized transformations under discussion. State the counting convention when ambiguity matters. | Do not count an input placeholder as a trainable layer. |
| Width | The number of units in a layer. | `4 -> 8 -> 3` has hidden width `8`. |
| Architecture | The arrangement of layers, widths, activations, and output design. | `2 -> 6 -> 1` with ReLU hidden units and sigmoid output. |

## Geometry and Forward Computation

| Term | Course meaning | Important limit |
|---|---|---|
| Weighted sum / affine transformation | The parameterized calculation `z = w dot x + b` or `Z = XW + b`. | It is affine when a nonzero bias is included, although classroom discussion may use "linear layer" informally. |
| Logit | A raw output score before probability conversion or normalization. | A logit is not a probability and need not lie in `[0, 1]`. |
| Probability | A normalized value in `[0, 1]` used as a probability-shaped model output. | A sigmoid or softmax output is not automatically well calibrated. |
| Threshold | A configured cutoff that converts a continuous score or probability into a class decision. | Moving the threshold does not retrain the model. |
| Decision boundary | The set of input locations at which the decision changes. | For a `0.5` sigmoid threshold, the one-neuron boundary is `w dot x + b = 0`. |
| Linear decision boundary | A straight line in two dimensions, a plane in three, or a hyperplane in higher dimensions. | A sigmoid softens output values but does not bend this boundary. |
| Nonlinearity | A transformation that prevents stacked layers from collapsing into one affine transformation. | More layers without nonlinear activations still represent one affine map. |
| Linearly separable | Describes labeled examples that one linear boundary can separate. | XOR is the Day 1 counterexample in raw input space. |
| Hidden representation | The coordinates or activation pattern produced by a hidden layer. | A plotted projection is descriptive and may omit relationships present in the full hidden space. |
| Forward propagation / forward pass | The ordered computation from input through intermediate pre-activations and activations to output. | It explains how fixed settings produced an output, not how the settings were learned. |
| Broadcasting | Applying a compatible lower-dimensional array across a larger array without adding trainable copies. | Adding `b` to every row of `XW` does not create one bias per example. |
| Batch | A group of examples processed together. | Batch size changes data shape, not parameter count. |

## Activation Reference

| Function | Output behavior | Day 1 teaching role |
|---|---|---|
| Sigmoid | Maps a scalar to `(0, 1)` and saturates toward both extremes. | Binary probability-shaped output and a visible example of saturation. |
| Tanh | Maps a scalar to `(-1, 1)` and saturates toward both extremes. | Contrast with sigmoid using zero-centered outputs. |
| ReLU | Returns `max(0, z)`. | Common mathematical example for hidden nonlinearity; negative inputs produce zero output. |
| Leaky ReLU | Keeps a small nonzero slope for negative inputs. | Optional Day 1 comparison; do not imply one fixed slope is universal. |
| Softmax | Converts a vector of logits into nonnegative values whose selected-axis total is `1`. | Multiclass output; normalize once per example, not across the batch. |

## Extending This Glossary

When a later day introduces a term, add it only after checking the authoritative objective and shared notation contract. Prefer one stable definition, one misconception boundary, and a link from the relevant lesson. Version-sensitive API names belong in environment or source-verification material, not in timeless definitions.
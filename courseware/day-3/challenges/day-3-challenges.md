# Day 3 Challenges: Scale It

Complete each activity before its reveal. Preserve the first prediction and add revisions separately: the difference between the two states is evidence of learning.

## Submission and Retrieval

Use the cohort participant channel labeled **Day 3 Activities**. If the cohort uses paper, keep one dated activity sheet and submit a snapshot at each collection point.

| Activity | Commit and collect | Retrieve |
|---|---|---|
| `ACT-D3-01` | Commit during 09:00-09:15 before feature roles are discussed | Reopen when interpreting CNN feature maps in `LAB-D3-02` |
| `ACT-D3-02` | Submit an evidence-only leak accusation before pipeline code is revealed in `LAB-D3-01` | Reopen during `CHECK-D3-02` |
| `ACT-D3-03` | Commit the kernel output and shape trace before the arithmetic reveal at 10:35 | Reopen at the first shape checkpoint in `LAB-D3-02` |
| `ACT-D3-04` | Commit token relationships before the illustrative map is revealed at 15:45 | Reopen during `CHECK-D3-04` and the Day 4 opening |

Do not erase an original response. Add **Revision after evidence** in a second color or a clearly separated section.

---

## ACT-D3-01 - Feature Ladder Under a Budget

**Objectives:** `OBJ-D3-01`, preparation for `OBJ-D3-03`  
**Time:** 6 minutes inside `LESSON-D3-01`  
**Format:** individual placement, pair challenge, evidence revision

An image classifier can build successive representations. Four candidate evidence cards are available:

- local light-to-dark transitions;
- repeated textures and corners;
- arrangements resembling sleeves, soles, or collars;
- raw pixel intensity at one location.

### Commit before discussion

1. Place each card at **input**, **early**, **middle**, or **later** on a feature ladder. More than one placement may be defensible.
2. For every placement, write what observation would support it in a feature map.
3. State one reason a deeper network *could* reuse an intermediate representation.
4. State one reason adding depth could make validation performance worse.
5. Mark one card whose human-readable label may overstate what a hidden channel actually represents.

### Constraint round

You have the same dataset, optimizer, and 3-minute training budget. Choose one:

- add two convolutional blocks;
- widen the existing block;
- keep the architecture and first audit the data/validation pipeline.

Defend the choice with one expected observation and one result that would make you change course.

### Revision after evidence

- Replace any claim that a layer **always detects** a named concept with a claim about what it **can encode**.
- Separate representational capacity from optimization and generalization evidence.
- Write one sentence correcting: "A deeper model contains more possibilities, so it must perform at least as well."

### Transfer prompt

A deeper model reaches lower training loss but worse validation accuracy than a shallow baseline. Give one hypothesis from each category: optimization, generalization, and data/evaluation. Request one cheap evidence item before changing architecture again.

---

## ACT-D3-02 - Leakage Accusation: Chain of Custody

**Objectives:** `OBJ-D3-02`, reinforcement of `OBJ-D2-08`  
**Time:** 8 minutes embedded in `LAB-D3-01`  
**Format:** model detective, staged evidence, repair order

### Non-negotiable reveal rule

Do not inspect the full pipeline code until the evidence-only accusation is submitted. A near-perfect validation score is a clue, not proof of leakage.

### Evidence card 1: metric report

- validation ROC AUC is `0.997`;
- a simple linear baseline nearly matches a larger model;
- the positive class is uncommon but both classes appear in validation.

### Evidence card 2: feature provenance

| Feature | Available at prediction time? | Creation time | Notes |
|---|---|---|---|
| `age_days` | yes | case opening | numeric |
| `request_type` | yes | case opening | categorical |
| `initial_priority` | yes | case opening | numeric |
| `case_resolution_code` | no | case closure | strongly associated with the target |

### Evidence-only submission gate

Before requesting code, submit:

1. two observations that are facts rather than diagnoses;
2. two plausible explanations for the high score;
3. the cheapest check that separates genuine predictive signal from a post-outcome proxy;
4. the expected result if the proxy hypothesis is correct;
5. one result that would weaken that hypothesis;
6. the feature you would quarantine first and why.

### Evidence card 3: transformation ownership

The numeric scaler was fitted once on all available records before the training/validation split. The split was then stratified.

Add a second accusation:

- What information crossed the split boundary?
- Why does applying training-fitted statistics to validation differ from fitting on validation?
- Why does stratification not repair this leak?

### Repair-order challenge

Number these operations in a valid order and justify each boundary:

- evaluate once on the untouched test set;
- split records into training, validation, and test sets;
- remove/quarantine features unavailable at prediction time;
- fit learned preprocessing on the training set only;
- compare development choices using validation;
- apply the already-fitted preprocessing to validation and test.

### Revision after evidence

Complete the claim:

> The repaired score may be lower yet more useful because __________. The repair does not prove __________.

### Transfer prompt

A medical model has no explicit target column in its inputs, but one feature is recorded only after treatment. Explain why "the target column was dropped" is not a sufficient leak audit. Name the provenance fields you would request.

---

## ACT-D3-03 - Kernel Reveal and Shape Trace

**Objectives:** `OBJ-D3-03`, reinforcement of `OBJ-D2-05`  
**Time:** 8 minutes inside `LESSON-D3-03`  
**Format:** calculate one location, predict the map, trace shapes

Treat the operation below as the cross-correlation used by common deep-learning convolution layers: the kernel is not flipped.

Input image:

```text
0 0 0 4 4
0 0 0 4 4
0 0 0 4 4
0 0 0 4 4
0 0 0 4 4
```

Kernel:

```text
-1  0  1
-1  0  1
-1  0  1
```

Use stride `1` and padding `0`.

### Commit before calculation

1. Predict the output shape.
2. Calculate the top-left output value.
3. Predict where the largest positive responses will appear.
4. Sketch the complete output sign pattern before multiplying every patch.
5. Explain what is shared as the kernel moves.

### Multi-channel shape trace

A batch enters a CNN as `(B, 1, 28, 28)`.

1. A convolution with `8` output channels, kernel `3`, stride `1`, padding `1` produces what shape?
2. A `2 x 2` pooling layer with stride `2` produces what shape?
3. A second convolution with `16` output channels, kernel `3`, stride `1`, padding `1` produces what shape?
4. A second `2 x 2` pooling layer produces what shape?
5. What flattened feature count enters a dense head?

### Revision after reveal

- Compare the computed map with your sketch.
- Explain locality and parameter sharing using evidence from the calculation.
- State why a strong response to this hand-designed kernel does not prove that a learned channel is a complete causal explanation of a model prediction.

### Transfer prompt

Two CNNs produce the same output shape. One uses a shared `3 x 3` convolution; the other uses independent weights at every spatial location. Which evidence would distinguish their parameter use and translation behavior?

---

## ACT-D3-04 - Token Relevance, Missing Paths, and Scale

**Objectives:** `OBJ-D3-07`, `OBJ-D3-08`  
**Time:** 8 minutes inside the 15:45-16:05 bridge  
**Format:** token-map prediction, limitation audit, resource decision

Sentence:

> The dog chased the ball because it was rolling.

Focus token: **it**

### Commit before the illustrative map

1. Rank the three tokens or phrases that should be most relevant when constructing a contextual representation for **it**.
2. Draw arrows from **it** to those tokens and label the relationship you expect.
3. State what a query, a key, and a value do in one sentence each, without equations.
4. Predict one consequence if token order information were absent.
5. Mark one relationship about which you are least certain.

### Limitation audit after reveal

The revealed map is illustrative, not output from a specified model. List at least three omitted routes or facts that prevent the map from being a complete explanation of a final prediction. Consider:

- value content;
- multiple heads or layers;
- residual paths and later transformations;
- alternative attention patterns;
- the difference between association and causal intervention.

Complete:

> Attention weights show __________, but by themselves they do not establish __________.

### Scale decision

A service team reports:

| Configuration | Batch-1 latency | Throughput | Peak memory | Validation score |
|---|---:|---:|---:|---:|
| A | 42 ms | 28 items/s | 2.1 GB | 0.84 |
| B | 61 ms | 74 items/s | 5.8 GB | 0.85 |

Choose A or B for each scenario and defend the constraint:

1. an interactive request with a strict 50 ms latency target;
2. an offline queue with a 6 GB memory ceiling and no per-item latency target.

Then name one measurement missing from the table that could reverse either choice. Do not claim GPU use automatically implies high utilization.

### Transfer prompt

Explain how the same fundamentals from Days 1-2 still appear inside a Transformer training system, then name two engineering concerns introduced by scale that are not visible in a one-batch classroom model.

---

## End-of-Day Retrieval

Keep these four artifacts together for Day 4:

1. your original and revised feature ladder;
2. your two-part leakage accusation and repaired order;
3. your kernel/shape prediction;
4. your token-map limitation sentence and resource choice.

Add one final sentence:

> The Day 3 result I trust most is __________ because its data, comparison, and limitation are __________.
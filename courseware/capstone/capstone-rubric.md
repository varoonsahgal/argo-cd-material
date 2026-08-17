# Capstone Rubric: The Neural Network Investigation

**Applies to:** `LAB-D4-04` team evidence board and five-minute defense  
**Total:** 100 points

This rubric rewards defensible ML engineering, not accidental score discovery. A well-controlled negative result can earn full experiment-design, diagnosis, efficiency, and explanation credit. Claims must remain calibrated to the small routing-code digits investigation.

**Not scored here:** `individual_transfer`. The team board and defense contain no `individual_transfer` field. Each learner completes `CHECK-D4-04` separately after the defense, regardless of whether the defense is sequential, in a parallel panel, or recorded.

## Weight Summary

| Dimension | Weight |
|---|---:|
| Model performance | 25 |
| Generalization | 20 |
| Experimental design | 20 |
| Diagnosis | 15 |
| Efficiency | 10 |
| Explanation | 10 |
| **Total** | **100** |

---

## 1. Model Performance - 25 points

| Level | Points | Evidence standard |
|---|---:|---|
| Strong | 22-25 | Uses an appropriate primary metric and relevant class/slice evidence; compares baseline and intervention under the same contract; reports uncertainty/tolerance; any improvement is real under the declared rule. A null/negative result earns this band only when the team shows the baseline was not worsened beyond tolerance and the result materially resolves the target hypothesis. |
| Developing | 15-21 | Reports a valid comparison but omits one important metric definition, slice, tolerance, or baseline alignment detail; score change is interpreted mostly correctly. |
| Limited | 7-14 | Emphasizes aggregate accuracy, mixes evaluation contracts, or makes a stronger improvement claim than the evidence supports. |
| Insufficient | 0-6 | No comparable result, uses test data for selection, or reports an unsupported score. |

## 2. Generalization - 20 points

| Level | Points | Evidence standard |
|---|---:|---|
| Strong | 18-20 | Separates training, validation, and authorized test roles; evaluates the generalization gap and relevant slices; selects checkpoints without test influence; narrows the claim when test and validation disagree. |
| Developing | 12-17 | Uses held-out evidence correctly but gives limited gap/slice interpretation or weakly states the claim boundary. |
| Limited | 5-11 | Mentions validation but relies on training behavior or one aggregate; test policy is unclear. |
| Insufficient | 0-4 | Repeatedly uses test evidence to choose the model/intervention or cannot establish held-out evidence. |

## 3. Experimental Design - 20 points

| Level | Points | Evidence standard |
|---|---:|---|
| Strong | 18-20 | States a falsifiable hypothesis, changes one major factor, fixes the comparison contract, predicts quality/curve/slice/resource effects, declares rejection evidence and a stop rule, and records the run completely before interpretation. A clean negative result can earn full credit. |
| Developing | 12-17 | Mostly controlled and recorded, but one prediction, rejection criterion, kept-fixed field, or stop rule is weak. |
| Limited | 5-11 | Changes several factors, writes the hypothesis after the run, or cannot attribute the result. |
| Insufficient | 0-4 | Random tuning, missing baseline, hidden changes, or test-driven experimentation. |

## 4. Diagnosis - 15 points

| Level | Points | Evidence standard |
|---|---:|---|
| Strong | 13-15 | Ranks plausible limitation families; cites multiple independent observations; includes a real competing explanation and disconfirming evidence; updates the diagnosis when results conflict. The diagnosis may remain unresolved if the uncertainty is precisely stated. |
| Developing | 9-12 | Plausible diagnosis with evidence, but alternatives or revision logic are thin. |
| Limited | 4-8 | Uses a label such as overfitting or optimization without enough observations; treats symptoms as unique causes. |
| Insufficient | 0-3 | Diagnosis contradicts available evidence or is absent. |

## 5. Efficiency - 10 points

| Level | Points | Evidence standard |
|---|---:|---|
| Strong | 9-10 | Respects the run budget; records model size and a bounded timing/resource measure with environment/method; compares quality against resources; avoids a low-information second run. |
| Developing | 6-8 | Respects the budget and reports resource evidence, but measurement conditions or trade-off interpretation are incomplete. |
| Limited | 3-5 | Reports raw runtime without method/environment, ignores size/resource effects, or spends the optional run without a discriminating reason. |
| Insufficient | 0-2 | Exceeds the run/test budget or makes unsupported cost/speed claims. |

## 6. Explanation - 10 points

| Level | Points | Evidence standard |
|---|---:|---|
| Strong | 9-10 | The five-minute defense forms a coherent facts -> hypothesis -> prediction -> result -> interpretation -> next-step chain; distinguishes observation from mechanism; answers challenges directly; states why the digits exercise is not production realism. |
| Developing | 6-8 | Clear sequence and evidence, with one weak mechanism, limitation, or next-step explanation. |
| Limited | 3-5 | Narrates actions and scores but not why the evidence changes the diagnosis or decision. |
| Insufficient | 0-2 | Unsupported claims, unclear contribution, or no defensible next step. |

---

## Evidence Gates and Score Caps

These caps protect the investigation contract.

| Violation | Maximum affected score |
|---|---|
| Test evidence used to choose intervention or checkpoint | Generalization `4/20`; Experimental design `4/20` |
| More than one major factor changed without a declared design reason | Experimental design `11/20` |
| No baseline under the same evaluation contract | Model performance `14/25` |
| No alternative or disconfirming evidence | Diagnosis `8/15` |
| Resource claim lacks environment/method | Efficiency `5/10` |
| Production or frontier realism claimed from digits | Explanation `5/10` |

## Negative-Result Policy

A negative result is not penalized merely because the primary metric does not improve. It can score strongly when the team:

- committed to a plausible hypothesis before the run;
- preserved a valid comparison;
- observed a result that accepts, rejects, or narrows the hypothesis;
- records any cost or regression honestly;
- calibrates the conclusion;
- proposes a next experiment that targets remaining uncertainty.

An unexplained positive score change does not receive equivalent credit.

## Defense Question Set

Each team should be ready to answer:

1. What was wrong or uncertain about the original model?
2. What evidence supports and threatens that diagnosis?
3. Why was the chosen experiment more informative than the alternatives?
4. What happened, including any negative or null result?
5. What changed in generalization, slices, and resources?
6. What is the strongest claim the evidence supports?
7. What would you try next with another hour?

## Individual Transfer Requirement

The team score and each participant's `CHECK-D4-04` are separate records. Do not copy an individual response into the team evidence board or add its points to the 100-point team score. A participant can contribute to a strong team submission and still need remediation if the individual response cannot transfer the evidence loop to an unfamiliar scenario.

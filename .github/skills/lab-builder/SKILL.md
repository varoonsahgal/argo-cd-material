---
name: lab-builder
description: Build reliable hands-on technical labs and notebooks with minimal setup, starter code, prediction prompts, experiments, checkpoints, expected results, troubleshooting, and validation. Use when creating or revising runnable course exercises, especially Python/ML labs.
---

# Lab Builder

Use [lab template](./lab-template.md) as the default structure and [validation checklist](./validation-checklist.md) before completion.

## Procedure
1. State the objective in one sentence.
2. Define environment, dependencies, dataset, and expected runtime.
3. Start from a known baseline.
4. Ask a prediction before important model/configuration changes.
5. Keep required implementation focused on the concept being taught.
6. Show observable evidence: output, metrics, curve, trace, or comparison.
7. Ask the participant to interpret what happened.
8. Add one meaningful challenge or variation.
9. Provide a checkpoint that confirms success.
10. Validate the lab from a clean start.

## Design constraints
- Do not hide the core lesson behind setup complexity.
- Do not require expensive hardware unless explicitly intended.
- Avoid huge downloads for a small conceptual payoff.
- Separate required work from optional extensions.
- Prefer deterministic sanity checks while acknowledging nondeterminism when relevant.

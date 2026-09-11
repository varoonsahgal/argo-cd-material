---
name: lab-builder
description: Build reliable, beginner-clear Argo CD concept guides and lab guides with minimal setup, real screenshots, exact commands, prediction prompts, checkpoints, expected output, troubleshooting, and validation. Use when creating or revising any course Markdown deliverable.
---

# Lab Builder

Use [concept guide template](./concept-guide-template.md) for sessions with no dedicated Lab, and [lab guide template](./lab-template.md) for sessions with a Lab or the Capstone. Use [validation checklist](./validation-checklist.md) before completion.

## Procedure
1. State the objective in one sentence.
2. Define environment, prerequisites, and expected duration, drawing from the environment specification `environment-engineer` produced — never invent new environment assumptions.
3. Start from a known-good baseline state.
4. Ask a prediction before an important sync, deployment, or diagnostic reveal.
5. Keep required steps focused on the concept being taught; push anything tangential to an optional stretch section.
6. Show observable evidence: CLI output, sync/health status, a resource tree, or a screenshot.
7. Ask the participant to interpret what happened, not just observe it.
8. Add one meaningful challenge or comparison (see `challenge-designer`).
9. Provide a checkpoint that confirms success in a way the participant can verify themselves.
10. Validate the guide from a clean environment state.

## Design constraints
- Do not hide the core lesson behind setup complexity — rely on the pre-built environment.
- Do not require resources beyond a single student VM's two lightweight clusters unless the course explicitly intends otherwise.
- Avoid large downloads or slow reconciliation waits for a small conceptual payoff.
- Separate required work from optional extensions.
- Every UI navigation step needs a screenshot or a capture-spec placeholder — see `screenshot-capture`.
- Prefer deterministic checkpoints while acknowledging reconciliation-timing nondeterminism when relevant.

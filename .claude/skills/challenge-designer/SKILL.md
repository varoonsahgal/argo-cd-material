---
name: challenge-designer
description: Design active-learning challenges for Argo CD courseware, including predict-before-you-sync experiments, deliberately broken applications/clusters, root-cause diagnosis from evidence, before/after drift comparisons, guardrail-bypass attempts, and pattern showdowns that reward reasoning. Use when a concept guide or lab guide needs stronger engagement or practice.
---

# Challenge Designer

Use this skill to convert passive explanation into purposeful active learning.

Read [challenge patterns](./patterns.md) for reusable formats.

## Procedure
1. Identify the exact concept or decision the challenge should reinforce.
2. Choose a pattern that exposes that concept visibly (in the Argo CD UI, CLI output, or Kubernetes events).
3. Make the participant commit to a prediction, diagnosis, or choice before revealing the result when possible.
4. Ensure the exercise has a clear, observable outcome (a sync/health status, a CLI output, a screenshot).
5. Debrief the result explicitly: what happened, why, and what general rule transfers to future incidents.
6. If competitive or comparative, score reasoning and explanation in addition to the raw outcome.
7. Keep the challenge short enough that it does not consume the guide it supports.

## Quality check
A strong challenge has:
- a meaningful decision,
- uncertainty before the result,
- observable evidence,
- a debrief,
- a direct connection to the learning objective.

Avoid trivia competitions, arbitrary speed races, or challenges where success depends mainly on guessing rather than applying the troubleshooting method taught in the course.

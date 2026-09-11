---
name: technical-source-check
description: Verify time-sensitive or uncertain Argo CD/Kubernetes/Helm/Terraform claims using current primary sources and record concise evidence. Use for CLI/UI behavior, install methods, ApplicationSet generators, HA guidance, chart/provider versions, or other facts that may have changed since training.
---

# Technical Source Check

Use [source policy](./source-policy.md).

## Procedure
1. Identify the exact claim that needs verification (a CLI flag, a UI menu path, a Helm chart default, a generator name, a version number).
2. Prefer the official Argo CD documentation, the argoproj GitHub repository/release notes, or official Kubernetes/Helm/Terraform documentation.
3. Check recency and version applicability — note which Argo CD version the claim holds for.
4. Distinguish documented fact from inference or recommendation.
5. Record a concise source note rather than pasting large source excerpts.
6. If reliable sources disagree, state the disagreement and avoid false certainty.
7. If verification is unavailable, mark the claim as unverified instead of guessing.

## Output
For each checked claim record:
- Claim
- Status: verified / qualified / not verified
- Current source
- Argo CD/tool version relevance
- Courseware implication (does a guide, screenshot, or command need to change?)

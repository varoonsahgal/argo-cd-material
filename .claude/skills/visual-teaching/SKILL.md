---
name: visual-teaching
description: Turn abstract Argo CD/GitOps/Kubernetes concepts into purposeful diagrams — topology, reconciliation flow, ownership trees, generator fan-out, sync-wave ordering, and RBAC boundaries. Use when a guide contains invisible processes, multi-step flows, changing state, or ownership relationships. For real Argo CD/Rancher UI screenshots, use the `screenshot-capture` skill instead.
---

# Visual Teaching

Read [visual patterns](./visual-patterns.md).

## Procedure
1. Identify what is invisible or hard to imagine (a process, a relationship, an ownership chain).
2. Decide what single relationship the diagram must reveal.
3. Choose the simplest visual form that exposes it.
4. Label only what supports the teaching point.
5. Pair the diagram with a prediction or observation question when possible.
6. Add a debrief explaining what the viewer should notice.

## Rule
Do not request a decorative graphic when a diagram, tree, timeline, or table would teach more effectively. Do not substitute a diagram for a real screenshot when the point is "here is what you will actually see in the UI" — that belongs to `screenshot-capture`.

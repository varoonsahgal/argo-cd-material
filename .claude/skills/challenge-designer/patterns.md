# Challenge Patterns

## Predict Before You Sync
Show a pending diff, a values-file change, or an ApplicationSet template edit. Require a prediction of what will happen before clicking Sync or applying it. Run it, compare the observed result, then explain the mechanism.

## Break It / Fix It
Start from a working Application, introduce one deliberate defect (a bad values reference, a wrong revision, a revoked cluster credential), observe the symptom (OutOfSync, Unknown, Degraded), diagnose the cause, repair it through Git, and explain why the repair worked.

## Root-Cause Detective
Provide Argo CD UI/CLI evidence (sync status, health status, resource tree, events) and Kubernetes evidence (pod status, events, logs) while hiding the underlying change that caused the problem. Ask participants to infer the likely fault and point to the specific evidence that supports it.

## Make It Fail on Purpose
Ask participants to deliberately produce a specific failure mode — for example, an unintended cascading deletion, a stuck sync hook, or a permission denial — so the failure pattern becomes memorable before teaching the guardrail that prevents it.

## Before / After
Capture a baseline (Synced/Healthy), make one targeted change (edit a live resource directly, change a sync policy), show the new result, and require an explanation of the difference — including whether self-healing intervened.

## You Get One Diagnostic Action
Present a multi-layer failure scenario (as in the capstone) with several plausible causes. Require participants to choose the single highest-information next diagnostic step — without making any change yet — and defend the choice before proceeding.

## Guardrail Bypass Attempt
Ask participants to attempt an action an AppProject or RBAC rule should block (deploying to an unauthorized namespace, using an unapproved source repo). Confirm the block occurs, then require an explanation of which boundary stopped it and why.

## Pattern Showdown
Implement the same requirement two ways — once with an ApplicationSet, once with App-of-Apps — and compare the operational impact (blast radius, ownership clarity, ease of rollback) for a stated scenario. Score the comparison and its justification, not just working output.

## Restore the Platform
The capstone-shaped pattern: a multi-fault, multi-layer failure. Require participants to identify the failure layer using evidence alone before changing anything, then repair the desired state and verify recovery. Debrief with the guardrail or monitoring change that would have prevented it.

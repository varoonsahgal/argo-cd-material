# Assessment Question Patterns

## Predict the outcome
Given a pending diff, values change, or sync-policy change, predict what will happen and explain why.

## Diagnose the symptom
Given Argo CD UI/CLI evidence (sync status, health status, resource tree) and Kubernetes evidence (events, pod status), identify the likely failure and the next diagnostic action.

## Choose the next experiment
Given limited evidence and several possible causes, select the highest-information next diagnostic step before making any change.

## Compare two approaches
Choose between ApplicationSet and App-of-Apps (or manual vs. automated sync, or webhook vs. polling) for a stated need and defend the trade-off — this maps directly to the outline's own decision table.

## Correct the misconception
Present a plausible but incorrect statement (e.g., "OutOfSync means the application is broken") and ask for a correction.

## Transfer scenario
Apply a troubleshooting method learned on one failure type to a different failure type not used in the original example.

## Explain the mechanism
Ask what Argo CD is actually doing internally (rendering, comparing, reconciling), not merely which command to run.

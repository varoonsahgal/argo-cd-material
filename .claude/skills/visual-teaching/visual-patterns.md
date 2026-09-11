# Visual Teaching Patterns

## Topology diagram
Use for the management cluster / workload cluster split, Git repository, and where CI hands off to Argo CD. Anchor for Session 1.

## Reconciliation-loop diagram
Use for Git change -> render -> compare -> synchronize -> health assessment. The course's single most important recurring diagram.

## Desired / live / target-state comparison
Use to make sync status concrete: what Git says, what rendering produces, what's actually running.

## Component architecture diagram
API server, application controller, repository server, ApplicationSet controller, Redis, and how a request/reconciliation flows between them.

## App-of-Apps ownership tree
Use to show root Application -> child Applications -> managed resources, and where cascading deletion propagates.

## ApplicationSet generator fan-out
Use to show one generator input (a list, a cluster label, a Git directory) producing many generated Applications — makes blast radius visible.

## Sync-wave/ordering timeline
Use to show phases, waves, and hooks executing in sequence, and where a failure blocks the next wave.

## RBAC / AppProject boundary diagram
Use to show which teams/tokens can touch which source repos, destinations, and resource kinds — and where Argo CD RBAC ends and Kubernetes RBAC begins.

## Before/after drift diagram
Use to show desired and live state diverging, then reconciled by self-heal or a manual sync.

## Pattern decision table
ApplicationSet vs. App-of-Apps by need — reuse the outline's own table as the canonical example of a resource trade-off/decision visual.

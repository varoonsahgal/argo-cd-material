# Recurring Screenshot Shot List

Screens this course references repeatedly. Use consistent framing each time so participants recognize the layout across guides.

- Argo CD login screen and initial admin-password retrieval
- Applications list view (grid/tree toggle)
- A single Application's resource tree view
- The Diff view (desired vs. live) for an OutOfSync Application
- Sync panel/dialog (manual sync options: prune, dry-run, apply-only)
- Application details: Sync status and Health status side by side
- Settings -> Repositories (connecting a Git repo)
- Settings -> Clusters (registering a workload cluster)
- AppProject creation/edit screen (sources, destinations, allowed resource kinds)
- ApplicationSet resource list and a generated-Applications view
- App-of-Apps: root Application's resource tree showing child Applications
- History and rollback view for an Application
- RBAC/SSO-related settings screen (if the course's Argo CD instance has SSO configured)
- Notifications/alerts panel, if used in the reliability session

For each, capture at the Argo CD version this course targets (see the blueprint's environment specification) and store under `courseware/assets/screenshots/<day>/`.

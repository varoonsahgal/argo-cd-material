# platform-components

Sources for the **child** Applications owned by the App-of-Apps root
(`platform-root` in `platform-config`). Each subdirectory is one child's manifests:

- `quotas/` — generous `ResourceQuota` and `LimitRange` objects for the
  storefront namespaces (calibrated so they never block labs).
- `network-policies/` — a default-deny plus an allow-same-namespace
  `NetworkPolicy` per storefront namespace.
- `agent/` — a tiny Deployment in `platform-system` (podinfo standing in for a
  "platform agent").

These deploy to the **workload** cluster. Lab 4 inspects the root→child ownership
tree and traces a deliberately broken child back to this repository.

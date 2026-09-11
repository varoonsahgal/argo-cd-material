---
name: terraform-lab-environment
description: Design and validate per-student Terraform-provisioned lab infrastructure (VMs, local Kubernetes clusters, Argo CD) safely — without ever applying real infrastructure changes automatically. Use for any environment/setup deliverable (Terraform, bootstrap scripts, reset scripts, instructor/student setup guides).
---

# Terraform Lab Environment

Read [infrastructure validation checklist](./infra-validation-checklist.md) before declaring any environment deliverable done.

## Procedure
1. Confirm the environment specification from the course blueprint: VM count, VM spec, cloud target, cluster topology, and the Argo CD version to install.
2. Write Terraform as reusable modules parameterized by student count (a `student_count` variable) — never hardcode a fixed number of resources.
3. Pin every tool, chart, and image version explicitly, and verify each is current using the `technical-source-check` skill — never guess a Kubernetes, `kind`/`k3d`, or Argo CD Helm chart version.
4. Write bootstrap logic as idempotent shell/cloud-init so re-running it (for example, after a reset) never fails or duplicates resources.
5. Validate locally: `terraform fmt -check`, `terraform validate`, `terraform plan` with example/placeholder variables; `shellcheck` every script. Where Docker is available, actually build the two-cluster + Argo CD sandbox locally end-to-end once, confirm it works, then tear it down.
6. **Never run `terraform apply` or `terraform destroy` against real cloud infrastructure yourself.** That is always the instructor's own explicit, separate action — your job is to make that action safe, cheap to understand, and well-documented.
7. Write the instructor and student setup guides as if the reader has never used Terraform or this cloud provider before — the same beginner-clarity bar as course content.
8. Include a cost estimate and a clear teardown reminder in the instructor guide.
9. Include a reset procedure that can run between cohorts or between labs without a full re-provision.

## Rule
An environment deliverable is not done because the Terraform "looks right." It is done when `fmt`/`validate`/`plan` are clean, scripts are shellchecked and idempotent, a local smoke test has been attempted and its result documented, and both setup guides include a verification step with expected output.

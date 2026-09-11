# Compute adapter contract

The root configuration (`../main.tf`) is provider-agnostic. It generates VM
names, SSH keypairs, and cloud-init user-data, then hands them to a **compute
adapter** module. The adapter is the *only* piece that talks to a specific
cloud. Swapping clouds means swapping adapters — nothing else changes.

The default adapter is [`compute-null`](./compute-null/): it provisions nothing
and renders everything to `./.local-render/`, so `terraform validate` and
`terraform plan` work with **no cloud credentials**.

## Required input variables

Every adapter MUST accept exactly these inputs (same names, same types):

| Input | Type | Meaning |
|---|---|---|
| `vm_count` | `number` | How many VMs to create. May be `0`. |
| `name_prefix` | `string` | VM names are `<name_prefix>-01`, `<name_prefix>-02`, … (zero-padded, 1-based). |
| `vm_shape` | `object({ vcpu = number, memory_gib = number, disk_gib = number })` | Requested size; map it to your cloud's instance type. |
| `image_hint` | `string` | OS image hint; resolve to a concrete image (AMI, image family, SKU). |
| `ssh_public_keys` | `list(string)` | One public key per VM, index-aligned with the generated names. |
| `user_data` | `list(string)` | One cloud-init document per VM, index-aligned with the names. Pass it verbatim to the instance's user-data field. |
| `allowed_ssh_cidrs` | `list(string)` | Permit inbound **22/tcp** only from these. |
| `allowed_ui_cidrs` | `list(string)` | If non-empty, permit inbound **8443/tcp** and **3000/tcp** from these. If empty, do **not** open those ports. |
| `tags` | `map(string)` | Apply to every VM (and, where supported, the firewall/security group). |

## Required output

Every adapter MUST return one output named `vms`:

```hcl
output "vms" {
  value = [
    { name = string, public_ip = string, private_ip = string },
    # ... one object per VM, in the SAME order as the input lists ...
  ]
}
```

Order matters: `vms[i]` must correspond to `ssh_public_keys[i]` / `user_data[i]`.
The root module relies on this alignment to build the per-student outputs.

## Firewall / security-group requirements (blueprint 8.4 — least privilege)

- Always allow **22/tcp** from `allowed_ssh_cidrs` only. Never `0.0.0.0/0`.
- Allow **8443/tcp** and **3000/tcp** from `allowed_ui_cidrs` only, and only when
  that list is non-empty. The recommended default is empty (tunnel-only).
- Open nothing else inbound.

## How to add a real cloud adapter

1. Create a sibling module, e.g. `adapters/aws/`, that declares the input
   variables above and the `vms` output above.
2. Inside it, create the VMs (passing `user_data[i]` to each instance's
   user-data), attach `ssh_public_keys`, apply `tags`, and create a security
   group / firewall from the two CIDR lists as specified.
3. In `../main.tf`, change the two module blocks' `source` from
   `./modules/compute-null` to your new adapter. Add the cloud provider to
   `../versions.tf` (or a `providers.tf`) and configure credentials the usual
   Terraform way (environment variables or a provider block).
4. Re-run `terraform init`, `validate`, and `plan`. Only run `apply` yourself,
   deliberately — no automation in this repository ever applies.

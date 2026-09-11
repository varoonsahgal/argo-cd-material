# modules/compute-null — the default, credential-free compute adapter.
#
# This is a NULL / LOCAL-RENDER implementation of the compute adapter contract
# (see ../compute-adapter-contract.md). It provisions no real infrastructure.
# Instead it:
#   * assigns each VM a stable name and deterministic placeholder IPs (from the
#     documentation-only TEST-NET ranges, so they can never be mistaken for real
#     hosts), and
#   * writes each VM's cloud-init user-data, authorized public key, and a fleet
#     inventory (including the intended firewall rules) to ./.local-render/.
#
# Because it needs no cloud provider, `terraform validate` and `terraform plan`
# succeed with no credentials — that is the whole point of the local-render path
# in blueprint section 8.11.
#
# TO USE A REAL CLOUD: do not edit this module. Create a sibling module that
# accepts the SAME inputs and returns the SAME `vms` output, then change the
# module `source` in ../../main.tf. The contract file lists the exact shape.

variable "vm_count" {
  description = "Number of VMs this adapter should represent."
  type        = number
}

variable "name_prefix" {
  description = "Prefix for generated VM names: <name_prefix>-01, <name_prefix>-02, ..."
  type        = string
}

variable "vm_shape" {
  description = "Requested size per VM (vcpu / memory_gib / disk_gib). Recorded in the inventory; a real adapter maps it to an instance type."
  type = object({
    vcpu       = number
    memory_gib = number
    disk_gib   = number
  })
}

variable "image_hint" {
  description = "OS image hint; a real adapter resolves it to a concrete image (AMI, image family, SKU)."
  type        = string
}

variable "ssh_public_keys" {
  description = "One SSH public key per VM, index-aligned with the generated names and with user_data."
  type        = list(string)
}

variable "user_data" {
  description = "One cloud-init user-data document per VM, index-aligned with the generated names."
  type        = list(string)
}

variable "allowed_ssh_cidrs" {
  description = "CIDRs permitted inbound to TCP 22. A real adapter turns this into a security group / firewall rule."
  type        = list(string)
}

variable "allowed_ui_cidrs" {
  description = "CIDRs permitted inbound to TCP 8443 (Argo CD) and 3000 (Gitea). Empty means no direct UI access (tunnel only)."
  type        = list(string)
}

variable "tags" {
  description = "Tags to apply to every VM."
  type        = map(string)
}

locals {
  vm_names = [for i in range(var.vm_count) : format("%s-%02d", var.name_prefix, i + 1)]

  # Deterministic placeholder addresses from RFC 5737 TEST-NET-3 (public) and
  # RFC 1918 (private). They exist only so plan output and the inventory look
  # realistic; a real adapter overwrites them with the cloud's assigned IPs.
  vms = [for i in range(var.vm_count) : {
    name       = local.vm_names[i]
    public_ip  = format("203.0.113.%d", 10 + i)
    private_ip = format("10.128.0.%d", 10 + i)
  }]

  render_dir = "${path.root}/.local-render"

  # The least-privilege firewall the real adapter must implement (blueprint 8.4):
  # SSH only from allowed_ssh_cidrs; UI ports only when allowed_ui_cidrs is set.
  firewall_rules = concat(
    [{ port = 22, protocol = "tcp", source_cidrs = var.allowed_ssh_cidrs, purpose = "ssh" }],
    length(var.allowed_ui_cidrs) == 0 ? [] : [
      { port = 8443, protocol = "tcp", source_cidrs = var.allowed_ui_cidrs, purpose = "argocd-ui" },
      { port = 3000, protocol = "tcp", source_cidrs = var.allowed_ui_cidrs, purpose = "gitea-ui" },
    ]
  )
}

# Render each VM's cloud-init user-data to disk (public content, mode 0600).
resource "local_file" "user_data" {
  count           = var.vm_count
  filename        = "${local.render_dir}/${local.vm_names[count.index]}.user-data.yaml"
  content         = var.user_data[count.index]
  file_permission = "0600"
}

# Record each VM's authorized SSH PUBLIC key (safe to expose).
resource "local_file" "authorized_key" {
  count           = var.vm_count
  filename        = "${local.render_dir}/${local.vm_names[count.index]}.authorized_key.pub"
  content         = trimspace(var.ssh_public_keys[count.index])
  file_permission = "0644"
}

# A single machine-readable inventory for this adapter invocation.
resource "local_file" "inventory" {
  count    = var.vm_count > 0 ? 1 : 0
  filename = "${local.render_dir}/${var.name_prefix}-inventory.json"
  content = jsonencode({
    name_prefix    = var.name_prefix
    vm_shape       = var.vm_shape
    image_hint     = var.image_hint
    firewall_rules = local.firewall_rules
    tags           = var.tags
    vms            = local.vms
  })
  file_permission = "0644"
}

output "vms" {
  description = "The provisioned VMs: a list of { name, public_ip, private_ip }. This is the adapter contract's required output."
  value       = local.vms
}

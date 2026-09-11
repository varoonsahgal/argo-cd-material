# main.tf — assemble the course lab fleet.
#
# What this root module does, and NOTHING more:
#   1. Derive stable VM names for the students and the optional instructor VM.
#   2. Generate one fresh SSH keypair per VM (tls_private_key). Private keys are
#      surfaced ONLY through sensitive outputs — they are never written to disk
#      here and never committed.
#   3. Render each VM's cloud-init user-data from templates/cloud-init.yaml.tftpl.
#   4. Hand the names/keys/user-data to a swappable COMPUTE ADAPTER. The default
#      adapter (modules/compute-null) renders everything locally so plan works
#      with no cloud credentials. To provision real VMs, an instructor swaps in
#      a cloud adapter that implements the same interface — see
#      modules/compute-adapter-contract.md. No other file needs to change.
#
# SAFETY: this configuration performs no cloud calls. Running `apply` against the
# null adapter only writes render artifacts under ./.local-render/.

locals {
  student_prefix    = "${var.name_prefix}-student"
  instructor_prefix = "${var.name_prefix}-instructor"

  # Names must match the adapter's own formula (format("%s-%02d", prefix, i+1))
  # so ssh_public_keys[i]/user_data[i] line up with the VM the adapter returns.
  student_names = [for i in range(var.student_count) : format("%s-%02d", local.student_prefix, i + 1)]
  instructor_names = [
    for i in range(var.instructor_vm_enabled ? 1 : 0) : format("%s-%02d", local.instructor_prefix, i + 1)
  ]
  all_names = concat(local.student_names, local.instructor_names)

  # Per-VM cloud-init user-data, keyed by VM name.
  user_data = {
    for name in local.all_names : name => templatefile("${path.module}/templates/cloud-init.yaml.tftpl", {
      ssh_username    = var.ssh_username
      ssh_public_key  = trimspace(tls_private_key.vm[name].public_key_openssh)
      role            = contains(local.instructor_names, name) ? "instructor" : "student"
      vm_name         = name
      payload_git_url = var.course_payload_ref.git_url
      payload_git_ref = var.course_payload_ref.git_ref
      payload_subdir  = var.course_payload_ref.subdir
    })
  }
}

# One SSH keypair per VM. ED25519 is small, modern, and widely supported.
resource "tls_private_key" "vm" {
  for_each  = toset(local.all_names)
  algorithm = "ED25519"
}

# ---------------------------------------------------------------------------
# Compute adapters. The interface is fixed (see modules/compute-adapter-contract.md);
# only the module `source` changes when moving to a real cloud, e.g.:
#   source = "./adapters/aws"   or   "./adapters/azure"   or a registry module.
# ---------------------------------------------------------------------------

module "compute_students" {
  source = "./modules/compute-null"

  vm_count          = var.student_count
  name_prefix       = local.student_prefix
  vm_shape          = var.student_vm_shape
  image_hint        = var.vm_image_hint
  ssh_public_keys   = [for name in local.student_names : tls_private_key.vm[name].public_key_openssh]
  user_data         = [for name in local.student_names : local.user_data[name]]
  allowed_ssh_cidrs = var.allowed_ssh_cidrs
  allowed_ui_cidrs  = var.allowed_ui_cidrs
  tags              = merge(var.tags, { course = var.name_prefix, role = "student" })
}

module "compute_instructor" {
  source = "./modules/compute-null"

  vm_count          = var.instructor_vm_enabled ? 1 : 0
  name_prefix       = local.instructor_prefix
  vm_shape          = var.instructor_vm_shape
  image_hint        = var.vm_image_hint
  ssh_public_keys   = [for name in local.instructor_names : tls_private_key.vm[name].public_key_openssh]
  user_data         = [for name in local.instructor_names : local.user_data[name]]
  allowed_ssh_cidrs = var.allowed_ssh_cidrs
  allowed_ui_cidrs  = var.allowed_ui_cidrs
  tags              = merge(var.tags, { course = var.name_prefix, role = "instructor" })
}

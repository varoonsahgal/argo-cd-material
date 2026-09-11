# variables.tf — root input variables for the course lab fleet (blueprint 8.10, 8.11).
#
# Every variable is documented for an instructor who has NOT used Terraform
# before. Defaults match the blueprint's required VM sizes. The only variable
# with no default — and therefore the only one you MUST set — is
# `allowed_ssh_cidrs`, because leaving SSH open to the whole internet is never
# safe.

variable "student_count" {
  description = "Number of participant VMs to provision (one per student). Class size is capped at 20 by the blueprint."
  type        = number

  validation {
    condition     = var.student_count >= 1 && var.student_count <= 20
    error_message = "student_count must be between 1 and 20 (blueprint section 8.10 caps class size at 20)."
  }
}

variable "instructor_vm_enabled" {
  description = "Whether to provision the extra instructor/reference VM. It is larger and also hosts the ha-demo cluster used in guide 03."
  type        = bool
  default     = true
}

# A "VM shape" describes how big each virtual machine is: how many virtual CPUs,
# how much memory, and how much disk. The object type below forces all three to
# be present so a partially-specified shape cannot slip through.
variable "student_vm_shape" {
  description = "Size of each participant VM (blueprint section 8.10: 4 vCPU / 16 GiB RAM / 60 GiB disk)."
  type = object({
    vcpu       = number
    memory_gib = number
    disk_gib   = number
  })
  default = {
    vcpu       = 4
    memory_gib = 16
    disk_gib   = 60
  }
}

variable "instructor_vm_shape" {
  description = "Size of the instructor/reference VM (blueprint section 8.10: 8 vCPU / 32 GiB RAM / 120 GiB disk)."
  type = object({
    vcpu       = number
    memory_gib = number
    disk_gib   = number
  })
  default = {
    vcpu       = 8
    memory_gib = 32
    disk_gib   = 120
  }
}

# A CIDR is a compact way to write a range of IP addresses, e.g. "203.0.113.10/32"
# means exactly one address, and "203.0.113.0/24" means 256 addresses. The
# firewall rules below only allow SSH from the ranges you list here.
variable "allowed_ssh_cidrs" {
  description = "REQUIRED. CIDR ranges allowed to reach TCP 22 (SSH). Set this to your operator/admin network(s). There is intentionally no default — leaving SSH open to 0.0.0.0/0 is unsafe."
  type        = list(string)

  validation {
    condition     = length(var.allowed_ssh_cidrs) > 0
    error_message = "allowed_ssh_cidrs must contain at least one CIDR. Do not open SSH to the whole internet."
  }
}

variable "allowed_ui_cidrs" {
  description = "Optional. CIDR ranges allowed to reach the Argo CD UI/API (8443) and Gitea (3000) directly. Leave empty (default) to require the SSH tunnel instead — that is the recommended, least-privilege setup."
  type        = list(string)
  default     = []
}

variable "name_prefix" {
  description = "Prefix applied to every VM name and tag so this cohort's resources are easy to find and tear down."
  type        = string
  default     = "argocd-course"
}

# The base OS image each VM boots from. The value is a hint the compute ADAPTER
# resolves to a concrete image for its cloud (e.g. an AMI, an image family, or a
# marketplace SKU). Ubuntu 24.04 LTS is the blueprint default (section 8.2).
variable "vm_image_hint" {
  description = "OS image hint passed to the compute adapter. Ubuntu 24.04 LTS is the course default (blueprint 8.2)."
  type        = string
  default     = "ubuntu-24.04-lts"
}

variable "ssh_username" {
  description = "Login user created on each VM. Must match the account bootstrap-vm.sh provisions (blueprint sections 8.3-8.5 use 'student')."
  type        = string
  default     = "student"
}

# Where the course payload (this repository's courseware/environment tree) lives,
# so each VM's cloud-init can fetch it and run bootstrap-vm.sh. The instructor
# points git_url at wherever they host the course; git_ref pins a branch or tag
# for reproducibility; subdir is the path to the environment/ folder inside it.
variable "course_payload_ref" {
  description = "Git location of the course payload used by cloud-init to run bootstrap-vm.sh on each VM."
  type = object({
    git_url = string
    git_ref = optional(string, "main")
    subdir  = optional(string, "courseware/environment")
  })
  default = {
    git_url = "https://github.com/your-org/argo-cd-operations-courseware.git"
    git_ref = "main"
    subdir  = "courseware/environment"
  }
}

variable "tags" {
  description = "Free-form key/value tags merged onto every VM (for cost tracking, ownership, and cleanup)."
  type        = map(string)
  default     = {}
}

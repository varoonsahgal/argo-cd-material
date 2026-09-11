# outputs.tf — connection details the instructor distributes to each student.
#
# Private keys are marked `sensitive` so Terraform never prints them to the
# console or logs. The instructor renders them to per-student files with, e.g.:
#   terraform output -json student_private_keys | jq -r 'to_entries[]
#     | .value' > /dev/null   # (see instructor-setup-guide.md for the real loop)

locals {
  # Index the adapter outputs by name so we can join them with the SSH keys.
  student_vm_by_name    = { for vm in module.compute_students.vms : vm.name => vm }
  instructor_vm_by_name = { for vm in module.compute_instructor.vms : vm.name => vm }
}

output "student_vms" {
  description = "Per-student connection info (no secrets). The tunnel_command forwards the Argo CD UI (8443) and Gitea (3000) to the student's laptop."
  value = {
    for name in local.student_names : name => {
      name           = name
      public_ip      = local.student_vm_by_name[name].public_ip
      private_ip     = local.student_vm_by_name[name].private_ip
      ssh_user       = var.ssh_username
      tunnel_command = "ssh -i ${name}.pem -L 8443:localhost:8443 -L 3000:localhost:3000 ${var.ssh_username}@${local.student_vm_by_name[name].public_ip}"
    }
  }
}

output "student_private_keys" {
  description = "Per-student SSH private keys (PEM). SENSITIVE — distribute one key to one student over a secure channel; never commit these."
  sensitive   = true
  value       = { for name in local.student_names : name => tls_private_key.vm[name].private_key_pem }
}

output "instructor_vm" {
  description = "Instructor/reference VM connection info, or null when instructor_vm_enabled = false."
  value = length(local.instructor_names) == 0 ? null : {
    name           = local.instructor_names[0]
    public_ip      = local.instructor_vm_by_name[local.instructor_names[0]].public_ip
    private_ip     = local.instructor_vm_by_name[local.instructor_names[0]].private_ip
    ssh_user       = var.ssh_username
    tunnel_command = "ssh -i ${local.instructor_names[0]}.pem -L 8443:localhost:8443 -L 3000:localhost:3000 ${var.ssh_username}@${local.instructor_vm_by_name[local.instructor_names[0]].public_ip}"
  }
}

output "instructor_private_key" {
  description = "Instructor VM SSH private key (PEM). SENSITIVE. Null when the instructor VM is disabled."
  sensitive   = true
  value       = length(local.instructor_names) == 0 ? null : tls_private_key.vm[local.instructor_names[0]].private_key_pem
}

output "credentials_location" {
  description = "Where per-VM credentials live once bootstrap-vm.sh finishes (blueprint section 8.5). These are generated ON each VM, not by Terraform."
  value = {
    student_readable = "/home/${var.ssh_username}/course/credentials/ (argocd-admin.txt, gitea-student.txt, team-a-dev.txt; mode 0600)"
    root_only        = "/opt/course/secrets/gitea-teammate.txt (used by fault injection)"
    bootstrap_log    = "/var/log/course-bootstrap.log"
  }
}

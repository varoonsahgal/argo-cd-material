# versions.tf — Terraform and provider version pins for the course lab fleet.
#
# This root configuration is deliberately PROVIDER-AGNOSTIC. It only needs the
# null/local/tls/random providers so that `init -backend=false`, `validate`, and
# `plan` all run with NO cloud credentials (blueprint section 8.11). Real compute
# lives behind a swappable adapter module (see modules/compute-null/ and
# modules/compute-adapter-contract.md); an instructor plugs their cloud's
# provider requirements into that adapter, not here.
#
# Provider versions verified against the Terraform Registry on 2026-09-10:
#   hashicorp/null   3.3.2   (latest)
#   hashicorp/local  2.9.1   (latest)
#   hashicorp/tls    4.4.1   (latest)
#   hashicorp/random 3.9.0   (latest)
# The `~>` constraints allow patch/minor updates within the verified major line.

terraform {
  required_version = ">= 1.12"

  required_providers {
    null = {
      source  = "hashicorp/null"
      version = "~> 3.3"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.9"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "~> 4.4"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.9"
    }
  }
}

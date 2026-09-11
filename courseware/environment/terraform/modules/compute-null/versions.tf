# versions.tf — the null adapter only needs the local provider (to write render
# artifacts). It deliberately requires NO cloud provider so validate/plan run
# without credentials.

terraform {
  required_version = ">= 1.12"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.9"
    }
  }
}

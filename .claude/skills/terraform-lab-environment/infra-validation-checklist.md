# Infrastructure Validation Checklist

- [ ] `terraform fmt -check` and `terraform validate` pass
- [ ] `terraform plan` succeeds against example/placeholder variables (or the credential gap is explicitly documented)
- [ ] All variables are documented with descriptions and sensible defaults
- [ ] Outputs include everything a student needs: connection info, UI URL, where to find credentials
- [ ] Firewall/security-group rules are scoped to only the needed ports
- [ ] No plaintext long-lived secret is committed to Git
- [ ] Bootstrap script is idempotent and passes `shellcheck`
- [ ] A local end-to-end smoke test was attempted where Docker is available, and its result (pass, or what couldn't be tested) is documented
- [ ] Reset script was tested and returns the environment to a known-good state
- [ ] Capstone fault-injection script was tested and is fully reversible
- [ ] Instructor guide includes a cost estimate and teardown steps
- [ ] Student guide ends with a smoke test that has documented expected output/screenshot
- [ ] Every tool/chart/Kubernetes version is pinned and was verified current

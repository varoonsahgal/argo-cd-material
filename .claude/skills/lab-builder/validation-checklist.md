# Lab Validation Checklist

- [ ] Fresh/reset environment reaches the expected starting state
- [ ] `kubectl` context and `argocd` CLI login are established before they're needed
- [ ] All manifests, values files, and ApplicationSet/AppProject definitions render and apply without error
- [ ] Commands run in the stated order without relying on undocumented prior state
- [ ] Sync status and health status reach the expected result within a reasonable, stated wait
- [ ] Every UI navigation step has a screenshot or a labeled capture-spec placeholder, matching the pinned Argo CD version
- [ ] Runtime fits the allotted time, including reconciliation waits
- [ ] Expected output or sanity check is documented for every executable step
- [ ] Reconciliation-timing nondeterminism does not make a checkpoint misleading
- [ ] Deliberate faults are clearly separated from accidental ones
- [ ] Solution path is known and has been executed successfully
- [ ] Optional steps are clearly labeled
- [ ] A reset/cleanup path back to a known-good state exists and has been tested

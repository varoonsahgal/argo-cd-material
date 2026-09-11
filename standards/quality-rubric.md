# Quality Rubric

Used by `course-reviewer` for the final, independent quality gate. Every finding carries one severity:

- **BLOCKER** — prevents reliable delivery or is materially incorrect.
- **HIGH** — likely to confuse learners or break a key activity.
- **MEDIUM** — worthwhile improvement.
- **LOW** — polish.

## Scope alignment
Every objective in `argo-cd-outline.md` is addressed; nothing major was added without a documented, justified reason; the two-day structure and session timings are respected or explicitly flagged as adjusted.

## Technical accuracy and currency
Argo CD, Kubernetes, Helm, and Terraform terminology, commands, CLI flags, UI navigation, and behavior are correct and internally consistent, and version-specific claims have been checked with `technical-source-check` against the pinned Argo CD version. Deprecated flags, renamed UI sections, or retired generators are not presented as current.

## Lab and exercise integrity
Lab guides are aligned to objectives, internally consistent, and executable as written; expected outputs are real (verified by `lab-tester`/`lab-solution-engineer`), not invented; every exercise has a checkable success criterion that does not reveal the answer.

## Environment and setup readiness
Terraform passes `fmt`/`validate`/local `plan`; bootstrap and reset scripts are idempotent and have been smoke-tested locally where possible; instructor and student setup guides are complete, consistent with what the labs assume, and include a working verification step; no plaintext long-lived secrets are committed.

## Visual and screenshot completeness
Every UI navigation step has a screenshot or a precise, clearly-labeled capture-spec placeholder; screenshots are attributed and version-noted when sourced externally; diagrams exist for every invisible process the pedagogy rubric flags.

## Cross-course consistency
Consistent terminology (Application/ApplicationSet/AppProject/App-of-Apps), file naming, environment naming, and progression of difficulty from Day 1 to Day 2.

## Delivery readiness
Timing estimates are credible against the outline; optional sections are clearly marked; nothing depends on an unverified external service being reachable during class without a documented fallback.

## Final report
`course-reviewer` writes a readiness verdict, a scorecard against each dimension above, an objective-coverage matrix, and file-by-file corrections. The course is not marked ready while BLOCKER issues remain.

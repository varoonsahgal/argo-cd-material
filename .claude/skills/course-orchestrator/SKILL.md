---
name: course-orchestrator
description: Orchestrate the complete creation of the Argo CD Operations courseware from the outline by delegating work, via the Agent tool, to the specialized course-development subagents in .claude/agents/ and consolidating their outputs. Use when asked to build, continue, or resume the course, or to run the full multi-agent courseware pipeline.
---

# Course Orchestrator

You (the main Claude session, not a subagent) are the lead orchestrator for a multi-agent courseware production workflow building **Intermediate Argo CD Operations**, a two-day hands-on course for DevOps and platform engineers.

Your job is not to write every artifact yourself. Your job is to decompose the course build, invoke the specialized subagents below with the `Agent` tool, pass each one a focused task with sufficient context, inspect their results, coordinate revisions, and produce a coherent final course package.

## Subagents available (in `.claude/agents/`)
- `course-architect` — blueprint, timing, objective map, environment spec, file plan
- `insight-generator` — memorable explanations, analogies, insight map
- `environment-engineer` — Terraform, bootstrap/reset/fault-injection scripts, setup guides
- `lab-engineer` — concept guides and lab guides (participant-facing Markdown)
- `lab-tester` — execution validation of lab guides
- `lab-solution-engineer` — solution files + execution validation
- `pedagogy-reviewer` — instructional-quality review
- `course-reviewer` — final independent quality gate

Invoke these with the `Agent` tool (`subagent_type` set to the subagent's name). Each subagent starts with no memory of this conversation, so give it a self-contained task: relevant file paths, relevant excerpts/sections, and the exact output path expected.

## Input
The outline is `argo-cd-outline.md`. Read it first. Treat it as the source of truth for scope, sequence, and timing.

## Final deliverables
This course has three deliverable types, all Markdown:

1. **Concept guides and lab guides** — every outline session becomes one `.md` file. A session with no dedicated Lab becomes a concept guide (explanation, mental model, visuals/screenshots, Quick Checks, a short optional hands-on task). A session's Lab, and the Capstone, become a lab guide: a detailed challenge exercise that doubles as the student guide — guided, beginner-clear, screenshot-illustrated, with progressively less hand-holding as the course advances. See [content contract](../../../standards/content-contract.md).
2. **Solutions** — every lab guide gets exactly one separate solution `.md` file under `courseware/solutions/`, mirroring its path/name with a `-SOLUTION.md` suffix.
3. **Environment and setup** — Terraform provisioning one VM per student (plus an instructor VM), each running the two-cluster (management + workload) Kubernetes topology with Argo CD preinstalled, plus extremely detailed instructor and student setup guides.

Do not produce Jupyter notebooks, slide decks, separate instructor decks, separate student-guide files, or separate assessment files — Quick Checks and exercises live inside the guide files themselves. The blueprint and insight map are internal build-planning documents, not classroom deliverables.

Every UI navigation step needs a real or precisely specified screenshot (`screenshot-capture` skill), and every version-specific technical claim needs current-source verification (`technical-source-check` skill) before it lands in a guide. These skills are available to you directly (via `Skill`) and to the subagents you invoke.

## Mandatory orchestration workflow
Call these subagents in this order. If at any point a subagent invocation is not possible, stop and report why.

### Phase 1 — Architecture
Invoke `course-architect` first.

Ask it to:
- analyze `argo-cd-outline.md`,
- create `courseware/00-course-blueprint.md`,
- validate/refine the outline's timing,
- assign each session to a concept guide or lab guide,
- map objectives to guides/exercises,
- define the environment specification and the screenshot plan,
- define the file plan for the rest of the course.

Do not proceed until the blueprint exists and is coherent.

### Phase 2 — Insight map
Invoke `insight-generator` after the blueprint exists.

Ask it to create `courseware/01-insight-map.md` containing memorable explanations, analogies, visual revelations, engineering trade-offs, failure stories, current platform-engineering connections, memorable one-liners/key takeaways, and claims requiring current-source verification.

The insight map is input for guide development, not a requirement to use every idea.

### Phase 3 — Environment and infrastructure
Invoke `environment-engineer` after the blueprint's environment specification exists.

Ask it to build Terraform for the student-VM fleet, the bootstrap/reset/capstone-fault-injection scripts, and the instructor and student setup guides, and to locally validate all of it. Remind it explicitly: no `terraform apply`/`destroy` against real infrastructure without the instructor's own separate action.

Run this phase before Phase 4 so that lab guides can reference real, grounded commands, cluster names, URLs, and file paths instead of placeholders.

### Phase 4 — Build the concept guides and lab guides
Work through the course by day, following the course-architect's guide file map.

For each planned file, invoke `lab-engineer` separately. Run independent files in parallel (multiple `Agent` calls in one message) when they do not depend on each other's intermediate work; run them sequentially when one file's exercise produces state (a registered cluster, a deployed Application, a created AppProject) that a later file's guide depends on.

#### Lab Engineer task
Provide:
- outline section(s) this file covers,
- relevant blueprint section (including its scaffolding level and screenshot plan entries),
- relevant insight-map entries,
- the environment specification (exact commands, cluster names, URLs from `environment-engineer`'s output),
- target `.md` output path,
- any state this file must save for, or load from, an adjacent file.

Ask it to write one self-contained Markdown file per entry in the guide file map, following the concept guide or lab guide contract as assigned. See Final deliverables above; there is no separate instructor-facing lesson artifact.

`lab-engineer` must **not** place completed solutions, answer keys, or instructor-only guidance inside participant artifacts. Solutions are owned by `lab-solution-engineer`.

#### Capstone task
Invoke `lab-engineer` with an explicit instruction to build the capstone as a diagnostic challenge, not a procedural walkthrough: structure it around the outline's own capstone fault list, require participants to identify the failure layer before making changes, and end with a written reflection section (what guardrail or monitoring change would prevent recurrence) rather than any live presentation.

### Phase 5 — Lab guide execution validation
After each lab guide is created, invoke `lab-tester` before treating it as complete.

Ask it to:
- stand up (or reuse) the two-cluster + Argo CD environment matching the environment specification, favoring a real local `kind`/`k3d` sandbox when available,
- execute every command and manifest in the guide end-to-end, in order,
- verify every screenshot matches the actual current UI state encountered,
- verify deliberate failures and recovery steps behave as described,
- assess whether the lab is genuinely interactive rather than copy/run,
- write a validation report under `courseware/reviews/`.

If a lab receives **FAIL**, send the report back to `lab-engineer`, require correction, then reinvoke `lab-tester`. Repeat until the lab is PASS, PASS WITH NOTES, or explicitly documented as NOT EXECUTABLE because of an external limitation.

Do not allow pedagogy or final course review to substitute for actual execution.

### Phase 6 — Solution generation and validation
After the lab guide passes execution QA, invoke `lab-solution-engineer`.

Ask it to:
- read the final lab guide,
- generate a separate solution `.md` file under `courseware/solutions/`,
- answer every exercise, prediction, interpretation question, and challenge, with reasoning, expected output, and misconceptions,
- execute the solution end-to-end against a real or faithfully local-equivalent environment,
- verify expected output and screenshot accuracy,
- verify no solution content leaked into participant materials,
- write a solution-validation report under `courseware/reviews/`.

If the solution receives **FAIL** because the solution itself is wrong, reinvoke `lab-solution-engineer` to fix and rerun it.

If the solution reveals a flaw or contradiction in the lab guide, send the issue to `lab-engineer`, then rerun `lab-tester`, regenerate/reconcile the solution, and rerun `lab-solution-engineer`.

A required lab is not complete until both gates are satisfied:

**Lab Guide PASS + Solution PASS**

### Phase 7 — Pedagogy review
After a complete day is built, invoke `pedagogy-reviewer`.

Ask it to review the material against `standards/pedagogy-rubric.md` and write a report under:
`courseware/reviews/pedagogy-day-<n>.md`

The review must identify concrete changes using these labels:
- KEEP
- CUT
- SHORTEN
- MOVE
- ADD ACTIVITY
- ADD VISUAL
- ADD PRACTICE
- CLARIFY

### Phase 8 — Revise
Read the pedagogy report.
Reinvoke `lab-engineer` (or `environment-engineer` for setup-related findings) with the specific findings that apply to its work.
Do not blindly accept every recommendation; resolve conflicts against the outline, time budget, and course goals.

### Phase 9 — Final quality review
When all courseware is built and revised, invoke `course-reviewer`.

Ask it to:
- review the entire `courseware/` tree, including `environment/` and `assets/`,
- score against `standards/quality-rubric.md`,
- verify scope, technical accuracy and currency, completeness, pacing, and screenshot/visual completeness,
- flag unsupported time-sensitive claims,
- check cross-day consistency,
- identify missing guides/exercises/takeaways,
- write `courseware/99-final-quality-report.md`.

### Phase 10 — Final remediation
If the final report contains blocking or high-severity issues, invoke the appropriate specialist subagents again to fix them.
Then invoke `course-reviewer` one final time to confirm resolution.

## Subagent rules
- Give every subagent a focused, self-contained task in the `Agent` tool's `prompt`.
- Include file paths and expected outputs in every delegation.
- Tell subagents to return a short summary and list files changed.
- Do not assume one subagent can see another subagent's conversation. Use workspace files as shared durable state.
- Prefer parallel subagent calls (multiple `Agent` invocations in a single message) for independent analysis; prefer sequential work when later work depends on files created earlier.
- Do not delegate vague tasks such as "make the course better." State the exact artifact, section, constraints, and success criteria.
- Background vs. foreground: run long, independent subagent tasks (e.g., several unrelated `lab-engineer` files) in the background and continue orchestrating; run a subagent in the foreground only when your very next action depends on its result (e.g., you must read the blueprint before Phase 2 can start).

## Completion criteria
Do not declare the course complete until:
- every outline objective is covered,
- every session has a guide (concept or lab) covering it,
- the environment specification has a validated Terraform/bootstrap implementation and both instructor and student setup guides,
- every lab guide has an execution-based `lab-tester` validation report,
- every lab guide has a separate, execution-validated solution file,
- no required lab guide or solution has unresolved FAIL status,
- every UI navigation step has a real screenshot or a precisely specified capture placeholder,
- pedagogy reviews have been addressed,
- final quality review has no unresolved blocking issues.

At completion, provide a concise summary of:
- files created,
- major design decisions,
- intentional scope changes or optional sections,
- remaining non-blocking recommendations.

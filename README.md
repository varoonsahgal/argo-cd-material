# Argo CD Courseware Factory

A GitHub Copilot multi-agent workspace that turns `argo-cd-outline.md` into a complete, instructor-ready **Intermediate Argo CD Operations** course: beginner-clear concept guides, screenshot-illustrated hands-on lab guides, separate solution files, and a fully Terraform-provisioned per-student lab environment — all in Markdown.

## Included agents

| Agent | Purpose |
|---|---|
| Course Orchestrator | Runs the end-to-end workflow and invokes the other custom agents as subagents |
| Course Architect | Converts the outline into a teachable blueprint, timing map, environment spec, and file plan |
| Insight Generator | Generates sticky explanations, visual ideas, engineering trade-offs, and memorable key takeaways |
| Environment Engineer | Builds and locally validates the Terraform-provisioned student VMs, two-cluster Kubernetes topology, Argo CD install, and reset/fault-injection scripts |
| Lab Engineer | Writes each concept guide and lab guide — explanation, screenshots, and hands-on exercises in one file |
| Lab Tester | Executes lab guides against a real environment and validates commands, screenshots, and recovery steps |
| Lab Solution Engineer | Writes and executes the separate solution file for each lab guide |
| Pedagogy Reviewer | Reviews sequencing, cognitive load, beginner clarity, active learning, and pacing |
| Course Reviewer | Final quality gate for technical accuracy, environment readiness, visual completeness, and delivery readiness |

## Included skills

| Skill | Purpose |
|---|---|
| challenge-designer | Predict-before-sync, break/fix, root-cause detective, guardrail-bypass, pattern showdowns |
| lab-builder | Concept-guide and lab-guide templates plus the validation checklist |
| assessment-designer | Scenario-based and reasoning-focused Quick Checks and checkpoints |
| visual-teaching | Diagrams for reconciliation, topology, ownership trees, sync waves, and RBAC boundaries |
| screenshot-capture | Sourcing/capturing real, version-accurate Argo CD UI screenshots, with a fallback capture-spec convention |
| terraform-lab-environment | Safe, validated-but-never-self-applied Terraform for the per-student lab infrastructure |
| technical-source-check | Verification of current Argo CD/Kubernetes/Helm/Terraform claims using primary sources |

## Install

Copy this package into the root of your course repository so the repository contains:

```text
.github/
  copilot-instructions.md
  agents/
  skills/
standards/
argo-cd-outline.md
```

VS Code discovers workspace custom agents from `.github/agents` and project skills from `.github/skills`.

## Use

1. Confirm `argo-cd-outline.md` is in the repository root.
2. Open the repository in VS Code with GitHub Copilot enabled.
3. Open Chat and select **Course Orchestrator** from the agent picker.
4. Start with a prompt such as:

```text
Build the complete course from @argo-cd-outline.md.
Create the generated materials under courseware/.
Use the full multi-agent workflow and address all review findings before declaring the course complete.
```

The orchestrator is configured with the `agent` tool and the full roster of specialist agents as allowed subagents. It should invoke them rather than merely role-play their perspectives.

## What the orchestrator does

```text
Outline (argo-cd-outline.md)
  |
  v
Course Architect  ->  blueprint + environment spec + file plan
  |
  v
Insight Generator  ->  insight map
  |
  v
Environment Engineer  ->  Terraform, bootstrap/reset scripts, setup guides
  |
  v
Lab Engineer  ->  concept guides + lab guides (screenshots included)
  |
  v
Lab Tester  ->  executes each lab guide against a real environment
  |
  v
Lab Solution Engineer  ->  separate solution file, executed and validated
  |
  v
Pedagogy Reviewer
  |
  v
Revision Pass
  |
  v
Course Reviewer
  |
  v
Final Remediation
```

## Shared state

Subagents have isolated conversational context. The workflow therefore uses files as durable shared state:

```text
courseware/00-course-blueprint.md
courseware/01-insight-map.md
courseware/environment/
  instructor-setup-guide.md
  student-setup-guide.md
  terraform/
  scripts/
courseware/day-1/...
courseware/day-2/...
courseware/solutions/...
courseware/assets/screenshots/...
courseware/reviews/...
courseware/99-final-quality-report.md
```

The exact tree can be refined by the Course Architect.

## Skills

Skills are designed to load only when relevant. You can also inspect/configure them from VS Code's Skills UI or invoke user-visible skills directly when supported.

## Recommended first test

Before asking the orchestrator to build both days, test Day 1 only:

```text
Use @argo-cd-outline.md as the source of truth.
Run the full workflow for Day 1 only, including architecture, environment setup, guide/lab content, execution testing, solutions, pedagogy review, and revision.
```

Review the generated material and tune the repository instructions once. Then run the full course.

## If subagents do not run

- Confirm your VS Code/GitHub Copilot version supports subagents.
- Confirm the Agent/runSubagent tool is available and enabled for the Course Orchestrator.
- In Chat, use customization diagnostics to confirm the agents and skills are loaded.
- Check YAML frontmatter if a custom agent or skill does not appear.

## Customization notes

- Put course-wide rules in `.github/copilot-instructions.md`.
- Put role-specific behavior in `.github/agents/*.agent.md`.
- Put reusable procedures in `.github/skills/<skill-name>/SKILL.md`.
- Keep `argo-cd-outline.md` as the scope/source-of-truth file rather than copying the entire outline into every agent.

## Lab execution QA

**Lab Tester** is an independent execution-focused agent. The orchestrator sends every lab guide to Lab Tester after Lab Engineer creates it, standing up a real (or local `kind`/`k3d`) environment and running every command. Failed guides return to Lab Engineer for correction and must be retested before the course can be considered complete.

## Instructor Solution Pipeline

Every lab guide has two independent execution gates.

1. **Lab Engineer** creates the participant-facing guide only.
2. **Lab Tester** executes the participant path and validates that it is runnable, clear, screenshot-accurate, and interesting.
3. **Lab Solution Engineer** creates a separate solution file and executes it end-to-end.
4. If the solution reveals a flaw in the guide, the work loops back through Lab Engineer and Lab Tester before the solution is reconciled and rerun.

Required completion rule:

`Lab Guide PASS + Solution PASS`

Solutions belong under `courseware/solutions/` and should never be mixed into participant-facing courseware.

## Environment safety

**Environment Engineer** writes and locally validates all Terraform and bootstrap/reset tooling, but never runs `terraform apply` or `terraform destroy` against real cloud infrastructure — provisioning real infrastructure is always the instructor's own explicit, separate action.

### Agent team

- Course Orchestrator — coordinates the complete pipeline
- Course Architect — designs course structure, timing, environment spec, and file plan
- Insight Generator — generates memorable explanations, visuals, and engineering connections
- Environment Engineer — builds and validates the per-student Terraform/Kubernetes/Argo CD environment
- Lab Engineer — writes concept guides and lab guides
- Lab Tester — executes and validates lab guides against a real environment
- Lab Solution Engineer — creates and executes separate solution files
- Pedagogy Reviewer — reviews learning design and cognitive load
- Course Reviewer — performs final cross-course quality review

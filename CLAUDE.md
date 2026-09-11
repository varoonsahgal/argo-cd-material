# Courseware Repository Instructions

This repository builds the complete courseware for **Intermediate Argo CD Operations**, a two-day, hands-on course for DevOps and platform engineers, from the outline in `argo-cd-outline.md`.

## Multi-agent orchestration
This repo was originally built around GitHub Copilot custom agents (`.github/agents/`) and Copilot skills (`.github/skills/`). Those have Claude Code equivalents:

- **Subagents** live in [.claude/agents/](.claude/agents/): `course-architect`, `insight-generator`, `environment-engineer`, `lab-engineer`, `lab-tester`, `lab-solution-engineer`, `pedagogy-reviewer`, `course-reviewer`. Invoke them with the `Agent` tool (`subagent_type` = the agent's name), or let Claude pick automatically based on the task.
- **Skills** live in [.claude/skills/](.claude/skills/): `lab-builder`, `challenge-designer`, `visual-teaching`, `screenshot-capture`, `assessment-designer`, `technical-source-check`, `terraform-lab-environment`, plus `course-orchestrator`.
- To run the full build pipeline (the old Copilot "Course Orchestrator" agent), invoke the **`course-orchestrator` skill** (`/course-orchestrator`). It runs in the main conversation and drives the subagents above through all ten build phases — architecture, insight map, environment, guide authoring, execution validation, solution generation, pedagogy review, revision, and final quality review — because only the main thread can chain multiple subagent calls together.
- The `.github/agents/` and `.github/skills/` directories are unchanged and still work for GitHub Copilot; the `.claude/` versions are Claude Code's copies, not a replacement. Keep both in sync if you edit the workflow going forward — there is no automatic sync between them.

## Source of truth
- Treat `argo-cd-outline.md` as the authoritative scope, sequence, and timing for the course.
- Do not silently add major topics, remove objectives, or change the two-day structure.
- You may recommend improvements, but clearly separate recommendations from required scope.
- Preserve traceability from outline objective -> session/lab -> guide file -> exercise/checkpoint.
- This is an Argo CD **operations** course, not an Argo Workflows course. Mention Argo Workflows only where the outline itself calls for the comparison.

## Output format — Markdown only
- Every deliverable in this course is a Markdown (`.md`) file. There are no Jupyter notebooks, no slide decks, and no video/live-presentation artifacts.
- Commands, YAML, Helm values, and Terraform appear as fenced code blocks with a language tag (`bash`, `yaml`, `hcl`, etc.) so they render and copy cleanly.
- Every substantial concept session and every lab/capstone produces exactly one participant-facing file that is **both the student guide and the hands-on exercise** — never split explanation into one file and practice into another (see Content structure below).
- Every lab/capstone's answers live in exactly one separate solutions file (see Instructor solution separation).

## Audience and explanation bar — the most important rule in this repository
The outline's stated prerequisites (Kubernetes basics, Helm, `kubectl`, Git) describe who is *in the room*, not how the material should read. Write as if for a capable beginner who has touched these tools but does not remember every detail under pressure:
- Assume nothing. Never write "as you know," "obviously," "simply," or "just" before a step — if it were simple, no one would need the guide.
- Expand every acronym and product-specific term the first time it appears (e.g., "CRD (Custom Resource Definition)"), even ones the audience has "probably" seen.
- Ground each new concept with a one-sentence plain-language definition or analogy before using it functionally.
- Break every concept into the smallest steps that still make sense — prefer one idea per paragraph over dense multi-idea paragraphs.
- When a step depends on prior Kubernetes/Helm/Git knowledge, include a short refresher inline rather than assuming it is remembered.
- "Intermediate" describes the pace and depth of the course as a whole (it moves fast and reaches real production patterns); it does not license unexplained jargon anywhere in the writing.

## Courseware principles
- Teach intuition before formal terminology.
- Prefer concrete, realistic operations scenarios (a broken sync, a leaked credential, a noisy drift alert) over abstract descriptions.
- Make invisible processes visible: reconciliation loops, ownership trees, sync waves, and cluster topology all need a diagram, screenshot, or traced example, not prose alone.
- Include active learning constantly: predict-before-you-sync, diagnose-the-failure, compare-before/after, explain-why, and constrained experiments. See the `challenge-designer` skill.
- Do not make labs primarily copy/paste exercises, and do not make them primarily blanks a participant cannot fill in from what has been taught.
- Build from a simple mental model (Day 1: one working Git-to-cluster deployment) to realistic production patterns (Day 2: ApplicationSets, App-of-Apps, guardrails, incident recovery).
- Explicitly surface common misconceptions and failure modes (e.g., "OutOfSync does not mean broken"; "Argo CD does not run `helm upgrade`").
- Use progressive disclosure: core concept first, nuance second, optional advanced material last.
- Reduce scaffolding as the course progresses: Labs 1-2 are heavily guided (exact clicks, exact commands, a screenshot at every meaningful step); Lab 3 onward keeps explaining every *new* concept in full but stops re-explaining mastered mechanics; the capstone is deliberately diagnostic rather than procedural, matching the outline's own description.

## Screenshots and current UI accuracy
- Every step that tells a participant to open, navigate, click, or observe something in the Argo CD (or Rancher) UI needs a screenshot, or a precisely specified placeholder if one cannot yet be captured. Use the `screenshot-capture` skill.
- Prefer a screenshot captured live from this course's own provisioned Argo CD instance over any other source — it is guaranteed to match the version and configuration participants will actually see. Live capture requires a browser-automation MCP tool (e.g., Playwright MCP) to be configured in this workspace; if none is configured, fall back to the documented-source or capture-spec-placeholder path in the skill.
- When citing an official documentation screenshot instead, credit the source and note the retrieval date and the Argo CD version it shows.
- Never invent a description of a UI screen that has not been verified against a real instance or current official documentation.
- State and pin the Argo CD version this course targets (from the environment specification) and keep screenshots and UI instructions consistent with that version — the UI and CLI have changed materially across major releases.

## Current-information rule
Argo CD, its CLI, its UI, and its ecosystem (Helm, Kubernetes, ApplicationSet generators, progressive sync) change quickly. For any version-specific or time-sensitive technical claim — install commands, CLI flags, UI menu paths, Helm chart values, recommended HA sizing, current generator types — verify against primary sources (WebSearch/WebFetch, and the `context7` MCP server if configured) before presenting it as current fact. Use the `technical-source-check` skill. Keep verification notes in review artifacts rather than cluttering participant-facing guides.

## Technical content standards
- Prefer current, supported Argo CD, Kubernetes, Helm, and Terraform practices over outdated tutorials.
- Keep commands minimal, readable, and copy-runnable; show the full command, never a fragment the reader must reassemble.
- Include expected output, sanity checks, and common failure notes for every executable step — show what a real terminal/UI would show, not an idealized guess (see the `lab-engineer` and `lab-tester` subagents for how this is verified).
- Avoid needless scope beyond what the outline and blueprint call for.

## Content structure

### Concept guide (session with no dedicated lab)
1. Why this matters (a concrete operations scenario)
2. Plain-language mental model (analogy before formalism)
3. Vocabulary grounded before it is used
4. Visual: diagram and/or screenshot
5. Worked walkthrough, fully narrated
6. Quick Checks (2-4 short, answered-inline comprehension questions)
7. Try It Yourself (one short, optional hands-on micro-task)
8. Common misconceptions
9. Key takeaways
10. Transition to what's next

### Lab guide (challenge exercise that doubles as the student guide)
1. Why this matters
2. Learning objectives
3. Prerequisites and what earlier guides already established
4. Mental model recap (short — the concept guide already taught it)
5. Environment check (confirm starting state, with a screenshot of "healthy")
6. Guided walkthrough (screenshots + exact commands + the reasoning behind each), scaled to the lab's scaffolding level
7. Exercises (see quality bar in the `lab-builder` skill)
8. Troubleshooting: likely failure -> likely cause -> fix
9. Checkpoint/validation participants can check themselves against
10. Key takeaways
11. Optional stretch challenge, clearly marked
12. Transition

## Environment and infrastructure standards
- Each participant gets one virtual machine (plus one instructor/reference VM), each running two lightweight Kubernetes clusters (management + registered workload) so labs mirror the production management-cluster/workload-cluster topology without requiring full Rancher/RKE2 per participant.
- All infrastructure is defined as Terraform, parameterized by student count, with pinned and currently-verified tool/chart versions.
- Agents may format and locally validate Terraform (`fmt`, `validate`, `plan` with placeholder variables) and test bootstrap scripts locally. **No agent runs `terraform apply` or `terraform destroy` against real cloud infrastructure, or provisions real cloud resources, without the instructor's own explicit, separate action.**
- Never commit plaintext long-lived credentials to Git; generate per-VM/per-student secrets and surface them only through Terraform outputs or an instructor distribution step.
- Both an instructor setup guide and a student setup guide are required, written to the same beginner-clarity bar as course content, with a verification/smoke-test step and expected output.
- Every lab must include a reset path back to a known-good state; the capstone requires a documented, reversible fault-injection mechanism.

See [content contract](standards/content-contract.md), [pedagogy rubric](standards/pedagogy-rubric.md), and [quality rubric](standards/quality-rubric.md).

## Quality bar
- Depth matches the time the outline allots.
- Activities test thinking (predict, diagnose, compare, explain), not just recall.
- Every guide reinforces its stated learning objective(s).
- Every major section earns its place; when content is too dense, recommend what to shorten, move, make optional, or remove rather than silently cramming it in.

## Instructor solution separation
- Participant-facing guides never contain completed solutions, hidden answer keys, or instructor-only notes.
- Every lab/capstone guide has a separate solution file under `courseware/solutions/`, mirroring its path and name with a `-SOLUTION.md` suffix.
- Instructor solutions must be executed end-to-end against a real or faithfully local-equivalent environment and validated independently — not merely inspected.
- A lab is not complete until the participant guide and instructor solution have both passed their respective validation gates.

# GitHub Copilot Courseware Factory

A ready-to-drop workspace customization package for turning a course outline into detailed technical courseware with a multi-agent GitHub Copilot workflow in VS Code.

## Included agents

| Agent | Purpose |
|---|---|
| Course Orchestrator | Runs the end-to-end workflow and invokes the other custom agents as subagents |
| Course Architect | Converts the outline into a teachable blueprint and timing map |
| Lesson Developer | Creates instructor-ready lesson material |
| Lab Engineer | Creates and validates hands-on exercises |
| Pedagogy Reviewer | Reviews sequencing, cognitive load, active learning, transfer, and pacing |
| Insight Generator | Generates sticky explanations, visual ideas, engineering connections, and memorable insights |
| Course Reviewer | Final quality gate for technical accuracy, completeness, consistency, and delivery readiness |

## Included skills

| Skill | Purpose |
|---|---|
| challenge-designer | Predict-before-run, break/fix, model detective, constrained experiments, competitions |
| lab-builder | Repeatable lab/notebook design and validation workflow |
| assessment-designer | Scenario-based and reasoning-focused assessments |
| visual-teaching | Diagrams, curves, traces, matrices, and other teaching visuals |
| technical-source-check | Verification of current technical claims using primary sources |

## Install

Copy this package into the root of your course repository so the repository contains:

```text
.github/
  copilot-instructions.md
  agents/
  skills/
standards/
```

VS Code discovers workspace custom agents from `.github/agents` and project skills from `.github/skills`.

## Use

1. Put your finalized outline in the repository, for example:

```text
course-outline.md
```

2. Open the repository in VS Code with GitHub Copilot enabled.
3. Open Chat and select **Course Orchestrator** from the agent picker.
4. Start with a prompt such as:

```text
Build the complete course from @course-outline.md.
Create the generated materials under courseware/.
Use the full multi-agent workflow and address all review findings before declaring the course complete.
```

The orchestrator is configured with the `agent` tool and the six specialist agents as allowed subagents. It should invoke them rather than merely role-play their perspectives.

## What the orchestrator does

```text
Outline
  |
  v
Course Architect
  |
  v
Insight Generator
  |
  +-----------------------+
  |                       |
  v                       v
Lesson Developer       Lab Engineer
  |                       |
  +-----------+-----------+
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
courseware/day-1/...
courseware/day-2/...
courseware/day-3/...
courseware/day-4/...
courseware/reviews/...
courseware/99-final-quality-report.md
```

The exact tree can be refined by the Course Architect.

## Skills

Skills are designed to load only when relevant. You can also inspect/configure them from VS Code's Skills UI or invoke user-visible skills directly when supported.

## Recommended first test

Before asking the orchestrator to build a four-day course, test one module:

```text
Use @course-outline.md as the source of truth.
Run the full workflow for Day 1 only, including architecture, lesson content, labs, pedagogy review, revision, and final review.
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
- Keep the course outline as the scope/source-of-truth file rather than copying the entire outline into every agent.


## Lab execution QA

The team now includes **Lab Tester**, an independent execution-focused agent. The orchestrator sends every required lab to Lab Tester after Lab Engineer creates it. Failed labs return to Lab Engineer for correction and must be retested before the course can be considered complete.


## Instructor Solution Pipeline

Every substantial lab has two independent execution gates.

1. **Lab Engineer** creates the participant-facing lab only.
2. **Lab Tester** executes the participant path and validates that the lab is runnable, clear, and interesting.
3. **Lab Solution Engineer** creates a separate instructor-only solution and executes it end-to-end.
4. If the solution reveals a flaw in the participant lab, the work loops back through Lab Engineer and Lab Tester before the solution is reconciled and rerun.

Required completion rule:

`Participant Lab PASS + Instructor Solution PASS`

Instructor solutions belong under `courseware/instructor-solutions/` and should never be mixed into participant-facing courseware.

### Agent team

- Course Orchestrator — coordinates the complete pipeline
- Course Architect — designs course structure, timing, and activity map
- Insight Generator — generates memorable explanations, visuals, and engineering connections
- Lesson Developer — creates instructor-ready lesson content
- Lab Engineer — creates participant-facing labs
- Lab Tester — executes and validates participant labs
- Lab Solution Engineer — creates and executes separate instructor solutions
- Pedagogy Reviewer — reviews learning design and cognitive load
- Course Reviewer — performs final cross-course quality review

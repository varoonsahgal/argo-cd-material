# Courseware Repository Instructions

This repository is used to create instructor-ready technical courseware from a course outline.

## Source of truth
- Treat the user-supplied course outline as the authoritative scope and sequence.
- Do not silently add major topics, remove objectives, or change course duration.
- You may recommend improvements, but clearly distinguish recommendations from required scope.
- Preserve traceability from outline objective -> lesson -> activity/lab -> assessment.

## Courseware principles
- Teach intuition before formal terminology or mathematics.
- Prefer concrete, realistic examples over abstract explanations.
- Make important concepts visible through diagrams, tables, learning curves, traces, or step-by-step state changes.
- Include active learning frequently: predict-before-you-run, diagnose-the-failure, compare-before/after, explain-why, and constrained experiments.
- Do not make labs primarily copy/paste exercises.
- Build from simple mental models to increasingly realistic workflows.
- Explicitly surface common misconceptions and failure modes.
- Use progressive disclosure: core concept first, nuance second, optional advanced material last.
- Connect foundational ideas to realistic engineering work without overstating what an introductory course can cover.
- Prefer evidence-based experiments over random hyperparameter tuning.

## Technical content standards
- Prefer current, supported libraries and idioms.
- For time-sensitive technical claims, verify against primary documentation before presenting them as current facts.
- Keep code examples minimal, readable, and runnable.
- For ML labs, prefer lightweight datasets and runtimes that work in a typical hosted notebook environment unless the outline says otherwise.
- Avoid needless dependencies.
- Include expected outputs, sanity checks, and common failure notes for executable labs.

## Content structure
For each substantial lesson, aim to include:
1. Why this matters
2. Learning outcome
3. Intuitive explanation
4. Visual or concrete model
5. Worked example or demo
6. Active-learning activity
7. Common misconception or failure mode
8. Key takeaway
9. Transition to the next concept

For each lab, aim to include:
1. Purpose
2. Prerequisites
3. Setup
4. Starter state
5. Prediction/question before execution
6. Experiment or implementation
7. Observation prompts
8. Challenge or variation
9. Validation/checkpoint
10. Takeaways

## Quality bar
- Depth should match the time available.
- Avoid repeated explanations unless repetition is deliberately used for reinforcement.
- Activities must test thinking, not just recall.
- Examples and labs must reinforce stated learning outcomes.
- Every major section should earn its place in the course.
- When content is too dense, recommend what to shorten, move, make optional, or remove.

See [content contract](../standards/content-contract.md), [pedagogy rubric](../standards/pedagogy-rubric.md), and [quality rubric](../standards/quality-rubric.md).


## Instructor solution separation
- Participant labs must never contain completed solutions, hidden answer keys, or instructor-only notes.
- Every substantial lab should have a separate instructor-only solution artifact under `courseware/instructor-solutions/`.
- Instructor solutions must be executable end-to-end and validated independently.
- A lab is not complete until the participant path and instructor solution path have both passed their respective execution checks.

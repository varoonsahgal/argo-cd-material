# Content Contract

Defines the required shape of every Markdown artifact this repository produces. Reviewers (`pedagogy-reviewer`, `course-reviewer`) check submissions against this contract; authors (`lab-engineer`, `lab-solution-engineer`, `environment-engineer`) write to it.

## Concept guide
Required sections, in order: Why this matters; Plain-language mental model; Vocabulary grounded before use; Visual (diagram and/or screenshot); Worked walkthrough; Quick Checks (2-4, answered inline); Try It Yourself (optional micro-task); Common misconceptions; Key takeaways; Transition.

A concept guide fails the contract if any technical term is used before it is defined, if there is no visual for an invisible process (reconciliation, ownership, sync waves), or if it contains graded exercises (those belong in a lab guide) or hidden answers.

## Lab guide
Required sections, in order: Why this matters; Learning objectives; Prerequisites; Mental model recap; Environment check (with a "healthy state" screenshot); Guided walkthrough; Exercises; Troubleshooting; Checkpoint/validation; Key takeaways; Optional stretch challenge; Transition.

Every exercise must include: a plain-language goal restatement, the concrete input and shape of a correct output (not the output itself), a time/difficulty estimate, at least one escalating hint, a checkable success criterion, and starter state that removes setup friction without removing the concept. Exercises are ordered easiest to hardest, with the stretch challenge clearly optional. A lab guide fails the contract if it contains completed solution code/commands for its own exercises, or if any UI navigation step lacks a screenshot or an explicit capture-spec placeholder.

## Solution file
Mirrors its lab guide's path and name with a `-SOLUTION.md` suffix under `courseware/solutions/`. For every exercise: the correct commands/manifests/configuration, why it is correct, expected output, common wrong turns and the misconception behind them, and acceptable alternatives where more than one valid approach exists. A solution file fails the contract if it has not been executed end-to-end against a real or faithfully equivalent environment, or if any answer has leaked into the paired lab guide.

## Environment setup guide (instructor or student)
Required sections: prerequisites; step-by-step provisioning/verification instructions; expected output/screenshot at each verification point; troubleshooting; (instructor only) cost estimate, access-distribution steps, and teardown; (student only) a final smoke test confirming readiness for Day 1. Written to the same beginner-clarity bar as course content — no assumed familiarity with Terraform or the target cloud provider.

## Universal rules
- Markdown only — no notebooks, slide decks, or presentation artifacts.
- Every acronym expanded on first use in a given file.
- Every fenced code block has a language tag and is copy-runnable as written.
- No file mixes participant and instructor-only content.

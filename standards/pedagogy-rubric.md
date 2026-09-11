# Pedagogy Rubric

Used by `pedagogy-reviewer` to score courseware 1-5 on each dimension. A 5 is exceptional and rare; a 3 is solid and shippable; below 3 needs revision before delivery.

## Progression
5: Every concept is used only after it has been taught; the sequence feels inevitable. 1: Concepts are referenced before they are introduced, or the order feels arbitrary.

## Cognitive load and beginner clarity
5: No unexplained jargon anywhere; every acronym and product-specific term is grounded on first use; one idea per step. 1: Multiple new ideas per paragraph, or language that assumes the reader already remembers Kubernetes/Helm/Git details the outline lists as prerequisites.

## Active learning
5: Participants predict, diagnose, compare, or decide at frequent, well-spaced intervals; no long passive stretches. 1: Mostly narrated reading with occasional copy/paste commands.

## Retrieval and reinforcement
5: Earlier concepts (e.g., sync vs. health status) resurface in new contexts (troubleshooting, capstone) rather than being taught once and dropped. 1: Concepts appear exactly once.

## Transfer
5: Exercises require applying a concept to a scenario not identical to the worked example (e.g., diagnosing a different failure than the one demonstrated). 1: Exercises are the worked example with different variable names.

## Misconceptions addressed
5: Common wrong mental models (e.g., "OutOfSync means broken," "Argo CD runs `helm upgrade`") are named and corrected explicitly. 1: Misconceptions are never named, only implicitly avoided.

## Assessment alignment
5: Quick Checks, exercises, and checkpoints test the stated learning objective through diagnosis/application/prediction. 1: Checks are vocabulary recall answerable without understanding.

## Pacing
5: Content volume matches the outline's allotted minutes with room for questions and debrief. 1: A session/lab cannot realistically be completed in its allotted time, or is too thin to fill it meaningfully.

## Engagement and visual support
5: Every invisible process (reconciliation, ownership, drift, sync waves) has a diagram or screenshot; challenges reward reasoning, not speed. 1: Text-only description of visual/UI-heavy processes; activities are trivia or unearned competition.

## Report requirement
For each dimension below 4, `pedagogy-reviewer` must cite the specific file and section, not a general impression.

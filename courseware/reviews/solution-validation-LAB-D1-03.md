# Solution Validation: LAB-D1-03

**Current status: PASS**

## Lab and Solution

- **Lab:** `courseware/day-1/labs/LAB-D1-03-shapes-activations.ipynb`
- **Solution:** `courseware/instructor-solutions/day-1/LAB-D1-03-shapes-activations-SOLUTION.ipynb`
- **Objectives:** `OBJ-D1-02`, `OBJ-D1-05`, `OBJ-D1-06`
- **Participant gate:** current **PASS WITH NOTES** report accepted; no contradiction found
- **Solution SHA-256:** `5920d4c93af1435294ab146056ca56db459560a6f9a671dffa381c8c72b1e8dd`
- **Participant SHA-256:** `8dc99076c5aaba05673f7c6d5388e1bc519f33dc366ac592b91bfbc33f61511e`

## Environment Used

- macOS on Apple silicon, local CPU
- Python 3.11.8
- NumPy 2.4.6; matplotlib 3.11.1
- nbformat 5.11.0; nbclient 0.11.0; ipykernel 7.3.0
- No accelerator API, network, download, dataset, external file, or prior-lab state

## Commands and Execution Status

1. Parsed and officially validated the participant and solution notebooks with `nbformat`.
2. Constructed a strict core copy by truncating the solution at the explicit optional separator, then executed it with a new `python3` kernel through `nbclient`.
3. Executed the canonical 35-cell solution from a new kernel with `jupyter execute --timeout=60 --inplace`, equivalent to Restart Kernel -> Run All, and persisted the refreshed reference outputs.
4. Audited stored outputs, imports, syntax, cell IDs, language metadata, response coverage, optional/core symbols, hashes, and participant leakage.

Both execution paths completed without uncaught errors.

## Tasks and Exercises Covered

- Completed every shape, broadcasting, parameter-count, activation, softmax-axis, and interpretation prediction.
- Implemented dense parameter counting, batch-first dense calculation, stable sigmoid, tanh, ReLU, and stable row-wise softmax.
- Verified the `4 -> 8 -> 3` parameter derivation and bias broadcasting evidence.
- Diagnosed sigmoid/tanh saturation and the current all-zero ReLU region without claiming permanent unit death.
- Executed, caught, explained, and recovered from the deliberate wrong-axis softmax failure.
- Completed all six core evidence explanations with what/why/concept guidance.
- Added staged hints, expected evidence, common wrong answers, troubleshooting, instructor demo notes, fast recovery, and acceptable alternatives.
- Completed the practical optional extension with predictions, implementation, plot/table evidence, slope comparison, interpretation, misconceptions, and valid alternatives.

## Core-Only Independence

- The strict core copy contains **33 cells**, including **16 code cells**, and renders **2 figures**.
- No `leaky` term, implementation, response name, or optional variable occurs in the strict core source.
- The required checkpoint executes before the optional separator and depends only on required variables.
- Later required work does not exist after the separator; removing every optional cell leaves the complete core result intact.
- Final clean core runtime, including kernel startup: **1.668 s**.

## Full Clean Run

- The full solution contains **35 cells**, including **17 code cells**, and renders **3 figures**.
- Every code cell has a fresh execution count; stored outputs contain no error objects.
- The optional branch defines its own prediction answers and implementation only after the explicit `OPTIONAL EXTENSION` heading.
- Final clean full-run wall time, including kernel startup and in-place save: **2.09 s**.

## Expected Result Checks

| Contract | Observed reference evidence |
|---|---|
| Parameter count | Exactly `67` |
| Dense shapes | `Z1/A1 (5, 8)`; logits/probabilities `(5, 3)` |
| Broadcasting | Every row of `Z1 - X @ W1` equals `b1` |
| Stable sigmoid | Finite `[0, 0.5, 1]` behavior through magnitude $10^6$ |
| Saturation | `sigmoid(8)->sigmoid(12)` change `0.000329`; tanh change approximately `2.25e-7` |
| Current ReLU region | `0/40` supplied negative entries remain nonzero |
| Stable row-wise softmax | Finite through magnitude $10^6$; every row sums to `1` within `1e-6` |
| Wrong-axis failure | Shape still `(5, 3)`; row sums `[0.647134, 0.635321, 0.406391, 0.715075, 0.596079]`; columns sum to `1` |
| Recovery | Correct extreme-logit row sums are `[1, 1]` |
| Optional slope comparison | At input `-12`, slopes `0.10` and `0.02` produce `-1.2` and `-0.24`; nonnegative outputs and shapes remain unchanged |

## Format, Imports, and Outputs

- Official `nbformat` validation passed for both artifacts.
- All solution and participant cells have unique IDs and the required `metadata.language` value.
- Solution imports are limited to `platform`, NumPy, and matplotlib.
- Core and full plots include titles, axis labels, legends or color bars, and zero references where relevant.
- The full notebook stores two core figures plus one optional figure and deterministic textual evidence for nonvisual recovery.

## Answer-Separation Check

- The participant notebook was not edited during solution work.
- All six participant prediction/interpretation dictionaries remain blank.
- Participant code retains only intended TODOs and empty outputs; all participant execution counts remain unset.
- No instructor label, completed answer, answer-key phrase, solution link, or instructor-only path appears in the participant artifact.
- **Leakage result: NONE.**

## Issues Found and Fixes Applied

- The previous solution placed the optional activation in required predictions, implementation, plots, and tables. All such material was moved behind the explicit optional separator.
- The previous stored outputs were partial and stale after structural edits. A clean in-place full execution refreshed every code-cell output.
- Newly inserted cells initially lacked language metadata. Their content was consolidated into existing cells, restoring complete metadata coverage.
- The validation dependency scan initially matched the harmless text `no network or GPU required`; the final audit distinguishes environment wording from accelerator API usage.
- No participant contradiction or required participant fix was found.

## Runtime and Colab Notes

- Both paths are comfortably below the 10-second compute target; participant reasoning and discussion will dominate the 40-minute block.
- CPU behavior is deterministic for the supplied arrays and seed.
- A real hosted Colab CPU session was **not** performed. Colab remains an honest, non-blocking unvalidated environment note.

## Final Status

The revised solution is complete, clean-executable on both required paths, correctly separated, and instructor-ready: **PASS**.
# Slide Render Validation

**Validation date:** 2026-08-16

## Day 1 - See It

**Status: PASS**

### Artifact and Renderer

- Source: `courseware/slides/day-1-see-it.md`
- Delivery PDF: `courseware/slides/day-1-see-it.pdf`
- Renderer: Marp CLI `4.5.0` via `npx`
- Render command: `npx -y @marp-team/marp-cli@4.5.0 courseware/slides/day-1-see-it.md --pdf --allow-local-files --output courseware/slides/day-1-see-it.pdf`
- PDF size: `896991` bytes
- PDF SHA-256: `e01c52f8d2e4f4bf762f8cec37c19034b1baecf89b0939dcc88dc3e5beee2c4c`
- Page geometry: `960 x 540` points, 16:9

`--allow-local-files` is required for the five repository-local PNG references. The renderer reported that local-file access was enabled; it reported no missing-resource or conversion error.

### Render QA

| Check | Result | Evidence |
|---|---|---|
| Page count | PASS | PDF contains exactly 32 pages. |
| Displayed sequence | PASS | Rendered headings are sequential from `01` through `32`. |
| Afternoon order | PASS | Pages 21-25 deliver `LESSON-D1-05` activation/nonlinearity content and `ACT-D1-03` before `LAB-D1-03`; page 26 delivers the `LESSON-D1-06` forward trace before the `LAB-D1-04` launch on page 27. |
| Slide 23 activation-card revision | PASS | ACT-D1-03 and the rendered slide require the four core functions (`sigmoid`, `tanh`, `ReLU`, and `softmax`); Leaky ReLU is visibly separate and explicitly optional. The 1920 x 1080 raster is unclipped, uncrowded, and legible. |
| Clipping and overflow | PASS | All 32 pages were inspected in four contact sheets. Visual pages 8, 12, 14, 22, 23, and 28 were also inspected at 1920 x 1080; no content crosses or disappears beyond the final slide bounds. |
| Unsupported diagram syntax | PASS | The baseline exposed five literal Mermaid code blocks. The source now uses renderer-native text traces; the final PDF contains no literal `flowchart` blocks. |
| Missing images | PASS | Final PDF image objects occur on pages 8, 12, 14, 22, and 28, matching the five source references. |
| Label readability | PASS | Titles, axes, legends, class labels, activation ranges, probe names, and the six-probe trace are readable in the 1920 x 1080 page rasters. See limitations below for localized crowding. |
| Internal paths | PASS | All five image references and all four displayed participant lab paths resolve on disk. |
| External links | NOT APPLICABLE | The source contains no Markdown links or external URLs. The PDF therefore contains zero link annotations; there are no clickable links to test. |
| Notes and alt text | PASS WITH LIMITATIONS | All 32 slides contain a speaker-note block and an `Alt text:` note. Each of the five raster visuals also contains an `Asset path:` note. PDF accessibility limitations are recorded below. |

### Asset Embedding and Legibility

| Asset | PDF page | Source dimensions | Result |
|---|---:|---:|---|
| `boundary-motion-overlay.png` | 8 | 1190 x 890 | Embedded; contour styles, point classes, probe numbers, axes, and panel titles are readable. |
| `linear-success-boundary.png` | 12 | 613 x 469 | Embedded; clusters, boundary, region colors, axes, and legend are readable. |
| `xor-raw-hidden-linked.png` | 14 | 1190 x 490 | Embedded; raw/hidden panels, classes, axes, boundary, and repeated anchor labels are readable. |
| `activation-small-multiples.png` | 22 | 1600 x 900 | Embedded; all core panels, optional Leaky-ReLU label, ranges, role labels, and softmax invariant are readable. |
| `forward-evidence-board.png` | 28 | 1361 x 990 | Embedded; four panels, decision region, hidden projection, probe names, and trace values are readable. |

### Source Notes and Alt-Text Limitations

1. Descriptive alt text is stored in source HTML comments with the speaker notes. The Marp delivery PDF is not a tagged PDF, and those descriptions are not exported as image alternative text for assistive technology.
2. The five PNGs use Marp background-image directives such as `![bg right:...]`; the directive text controls layout and is not a descriptive PDF alt attribute.
3. Speaker notes are intentionally absent from the delivery PDF. Instructors must use the Markdown source or instructor guide to access the visual descriptions and delivery cues.
4. The XOR source note requests thin connectors between corresponding raw and hidden anchors. The delivered asset instead uses repeated circled `C0`-`C3` anchor identities without cross-panel connector lines. Correspondence remains visible, but the implementation is less explicit than the note.
5. `forward-evidence-board.png` retains localized label crowding around the east-side probes, and `xor-raw-hidden-linked.png` places labels close to anchor markers. The labels remain distinguishable in the final render, but the instructor should verbally identify the active probe rather than rely on silent room-distance reading.
6. Lab paths are rendered as visible code text, not clickable links. Their targets were checked on disk and exist, but PDF link activation cannot be tested because the deck defines no link annotations.

### Visual Inspection Method

The untouched deck was first rendered to a temporary PDF to expose renderer-specific defects. After correction, every page was rasterized and inspected in contact sheets; the five asset pages were inspected individually at 2x scale. The final workspace PDF was then rebuilt and structurally checked. Page 22 was re-rasterized after the last overflow correction, and revised page 23 was separately re-rasterized at 1920 x 1080 for clipping, overflow, and legibility review.

### Day 1 Disposition

Day 1 render status is **PASS**. The 32-page PDF is a real Marp render, all five required assets are embedded and usable, the reconciled afternoon order is preserved, and no clipping, missing image, literal Mermaid block, broken referenced path, or blocking legibility defect remains. The limitations above are non-blocking documentation and accessibility constraints; no notebook or PNG was modified during slide QA.

## Day 2 - Train It

**Status: PASS**

### Artifact and Renderer

- Source: `courseware/slides/day-2-train-it.md`
- Delivery PDF: `courseware/slides/day-2-train-it.pdf`
- Renderer: Marp CLI `4.5.0` with Marp Core `4.4.0`, invoked via `npx`
- Render command: `npx -y @marp-team/marp-cli@4.5.0 courseware/slides/day-2-train-it.md --pdf --allow-local-files --output courseware/slides/day-2-train-it.pdf`
- PDF page count: `34`
- PDF size: `301517` bytes
- PDF SHA-256: `5303507380526641f172df432b5ad4473f4e3da1091a8cee26760df55b68aa8c`
- Page geometry: `960 x 540` points, 16:9

`--allow-local-files` is required for the eight repository-local SVG references. Marp reported that local-file access was enabled and completed without a missing-resource or conversion error.

### Render QA

| Check | Result | Evidence |
|---|---|---|
| Page count | PASS | The final PDF contains exactly 34 pages. |
| Canonical sequence and timing | PASS | Rendered headings are sequential from `01` through `34`. The current four lab durations (`40`, `45`, `70`, and `55` minutes), check timings, final block, and canonical IDs were preserved. |
| Slides 31-32 gate order | PASS | Slide 30 assigns one mystery card before its visible `Diagnose before source reveal` step, and slide 32's note identifies those launch assignments as A, B, or C. Page 31 remains the evidence-only `ACT-D2-04` commitment gate and contains no reveal label or plausible-cause asset. Page 32 visibly says `POST-GATE REVEAL`; its note withholds only the causes, checks, and source guidance until every diagnosis is submitted and accepted, not the card assignment. |
| Clipping and overflow | PASS | All 34 pages were inspected in four contact sheets. No text block exceeded the PDF page bounds, and no visible content was clipped, overlapped, or displaced. |
| Unsupported syntax | PASS | Extracted PDF text contains no literal Markdown fences, HTML image tags, HTML reveal markup, or diagram-language syntax. |
| Missing images and broken paths | PASS | All eight SVG references resolve on disk and appear on their expected pages. Marp reported no missing resource. |
| Asset legibility | PASS | Asset pages 4, 8, 12, 14, 16, 21, 27, and 32 were inspected individually at `1920 x 1080`; titles, traces, values, axes, shape labels, table entries, hypotheses, and checks are readable and unclipped. |
| Lab paths | PASS | The four displayed participant paths resolve to `LAB-D2-01-loss-learning-rate.ipynb`, `LAB-D2-02-backprop-gradient-check.ipynb`, `LAB-D2-03-numpy-training.ipynb`, and `LAB-D2-04-pytorch-break-fix.ipynb`. |
| Source notes and alt text | PASS | All 34 slides contain speaker notes and an `Alt text:` source note. All eight asset slides contain an `Asset path:` note and descriptive HTML `alt`; every SVG also contains `role="img"`, `<title>`, and `<desc>`. |
| PDF figure descriptions | PASS | The PDF is marked as tagged and its structure tree contains eight `/Alt` entries matching the eight asset descriptions. |
| PDF links | PASS WITH LIMITATION | The PDF contains zero link annotations. Lab paths are intentionally rendered as visible code text, so existence was checked on disk but click activation is not available. |

### Asset Embedding and Legibility

| Asset | PDF page | Source dimensions | Result |
|---|---:|---:|---|
| `training-loop-dual-trace.svg` | 4 | 1200 x 700 | Rendered; forward, backward, update, repeat, and inference paths are distinct and readable. |
| `equal-accuracy-different-loss.svg` | 8 | 1200 x 700 | Rendered; all bars, probabilities, loss values, and the `0.50` threshold are readable. |
| `learning-rate-trajectories.svg` | 12 | 1200 x 700 | Rendered; all four fixed-axis paths and their loss-change labels are readable. |
| `computational-graph.svg` | 14 | 1200 x 700 | Rendered; forward values, local derivatives, and the final product are readable. |
| `gradient-check-table.svg` | 16 | 1200 x 700 | Rendered; analytic/numeric values, relative errors, and defect patterns are readable. |
| `batch-shape-map.svg` | 21 | 1200 x 700 | Rendered; all batch, weight, bias, and output shapes remain readable. |
| `numpy-pytorch-side-by-side.svg` | 27 | 1200 x 700 | Rendered; all seven responsibility mappings and the judgment reminder are readable. |
| `broken-curves-evidence.svg` | 32 | 1200 x 700 | Rendered only after the visible post-gate label; all three symptom cards, plausible causes, and requested checks are readable. |

### Source Notes, Accessibility, and Link Limitations

1. Speaker notes and their duplicate `Alt text:` descriptions are intentionally absent from the delivery PDF. Instructors must use the Markdown source or instructor guide for delivery cues, including the slide-32 withholding rule.
2. The PDF is tagged and all eight SVG figures have exported `/Alt` descriptions. Full reading-order quality, screen-reader behavior, and PDF/UA conformance were not tested with an external accessibility checker or assistive technology.
3. The deck defines no Markdown links or external URLs, and the PDF contains no link annotations. The four lab paths are visible but not clickable; their targets were verified on disk.
4. The three-card text on page 32 is readable in the `1920 x 1080` raster, but it is intentionally information-dense. The instructor should reveal and discuss one assigned card at a time rather than expect silent room-distance reading of all three.

### Visual Inspection Method

The final PDF was structurally checked with PyMuPDF and pypdf, rasterized page by page, and inspected in four contact sheets covering pages 1-9, 10-18, 19-27, and 28-34. The eight asset pages were separately inspected at 2x scale (`1920 x 1080`). Structure checks confirmed 34 pages, `960 x 540` geometry, sequential numbered headings, in-bounds text blocks, slide-31/32 gate ordering, eight PDF figure descriptions, zero link annotations, and absence of literal unsupported source syntax.

### Day 2 Disposition

Day 2 render status is **PASS**. The PDF is a real 34-page Marp render, all eight required SVG assets are present and legible, all four lab paths resolve, the 34-slide sequence and timing remain intact, and slide 32 is visibly and operationally withheld until the evidence-only gate on slide 31 is accepted. No notebook, Day 1 slide source, Day 1 PDF, Day 1 asset, or Day 1 validation evidence was modified during this remediation.

## Day 3 - Scale It

**Status: PASS**
**Validation date:** 2026-08-17

### Artifact and Renderer

- Source: `courseware/slides/day-3-scale-it.md`
- Delivery PDF: `courseware/slides/day-3-scale-it.pdf`
- Renderer: Marp CLI `4.5.0` with Marp Core `4.4.0`, invoked via `npx`
- Render command: `npx -y @marp-team/marp-cli@4.5.0 courseware/slides/day-3-scale-it.md --pdf --allow-local-files --output courseware/slides/day-3-scale-it.pdf`
- PDF page count: `36`
- PDF size: `485581` bytes
- PDF SHA-256: `75cac94991ee41d575c73a519a654497ac645a38458a3112ccf9bd7e732864f8`
- Page geometry: `960 x 540` points, 16:9

`--allow-local-files` is required for the eight repository-local SVG references. Marp reported that local-file access was enabled and completed without a missing-resource or conversion error.

### Render QA

| Check | Result | Evidence |
|---|---|---|
| Page count | PASS | The final PDF contains exactly 36 pages. |
| Displayed sequence and IDs | PASS | Extracted headings are sequential from `01` through `36`; lab launches remain on pages 8, 13, 19, and 24, `CHECK-D3-01` remains on page 16, and the final checks remain on pages 34-35. |
| Clipping, overflow, and readability | PASS | Every page was inspected in four contact sheets. Text-block geometry found zero out-of-bounds blocks. No visible text, table, gate, diagram, or page number is clipped or overlapped. Dense pages 20, 24-26, and 34-35 were inspected individually at `1920 x 1080`. |
| Slide 20 evidence boundary | PASS | The page visibly labels the successful rescue curves as illustrative, not validated run output, and states that a justified intervention may miss its criterion and should then be rejected, as the validated dropout run was. |
| Slides 24-26 source-mode branch | PASS | Each page visibly separates canonical CIFAR/MobileNet from the packaged Fashion-MNIST/label-blind 256-wide surrogate route. All three preserve the recovery limits: not CIFAR-10, not MobileNet output, not canonical metrics/runtime, and not proof that transfer wins. Page 24 retains `MobileNet_V3_Small_Weights.DEFAULT` and `weights.transforms()`. |
| Unsupported literal syntax | PASS | Extracted PDF text contains no Markdown fences, Mermaid `flowchart` syntax, HTML reveal/image markup, or source comments. |
| Asset paths and rendering | PASS | All eight SVG references resolve and render as vector content on pages 4, 9, 12, 14, 20, 25, 29, and 32. Marp reported no missing resource. |
| Asset legibility | PASS | All eight asset pages were inspected individually at `1920 x 1080`; titles, labels, axes, legends, traces, values, arrows, shape paths, gates, and caveats are readable and unclipped. |
| Lab paths | PASS | All four displayed participant paths resolve to the current Day 3 notebooks on disk. |
| Source notes and alt text | PASS WITH LIMITATIONS | All 36 slides contain speaker notes and an `Alt text:` source note. All eight asset slides have descriptive HTML `alt`; every SVG contains `role="img"`, `<title>`, and `<desc>`. PDF limitations are recorded below. |

### Asset Mapping and Legibility

| Asset | PDF page | Source dimensions | Result |
|---|---:|---:|---|
| `feature-ladder.svg` | 4 | 1280 x 720 | Rendered; stage labels, capacity/risk bars, prediction prompt, and interpretation limit are readable. |
| `data-provenance-leak-pipeline.svg` | 9 | 1280 x 720 | Rendered; valid ownership path, both red leak paths, timing labels, and validity-gain caveat are readable. |
| `kernel-feature-map-shape-trace.svg` | 12 | 1280 x 720 | Rendered; input, kernel, feature-map values, operation limit, and complete batch-first shape trace are readable. |
| `cnn-map-hierarchy.svg` | 14 | 1280 x 720 | Rendered; map-stage labels and supported-versus-unsupported interpretation boxes are readable. |
| `overfit-rescue-aligned-curves.svg` | 20 | 1280 x 720 | Rendered on aligned axes; baseline/rescue traces, absolute-behavior rule, illustrative label, and rejection sentence are readable. |
| `transfer-scoreboard.svg` | 25 | 1280 x 720 | Rendered; scoreboard rows and parameter bars remain readable alongside the visible canonical/recovery labels and full recovery gate. |
| `token-relevance-limitation.svg` | 29 | 1280 x 720 | Rendered; token links, illustrative label, Q/K/V summary, omitted routes, and causal limitation are readable. |
| `memory-throughput-latency.svg` | 32 | 1280 x 720 | Rendered; both configurations, four resource questions, bottleneck path, and measurement prompt are readable. |

### Source Notes, Accessibility, and Link Limitations

1. All 36 slides have source-level speaker notes and `Alt text:` descriptions. The eight asset references also have descriptive HTML `alt`, and all eight SVG files have source-level `role="img"`, `<title>`, and `<desc>` metadata.
2. The PDF is marked as tagged and contains a structure tree, but the final file contains zero `/Alt` entries. The source descriptions therefore must not be represented as exported PDF figure alternatives.
3. Full reading order, screen-reader behavior, keyboard navigation, color-contrast conformance, and PDF/UA compliance were not tested with assistive technology or a dedicated accessibility checker.
4. Speaker notes are intentionally absent from the delivery PDF. Instructors need the Markdown source or instructor guide for reveal rules, recovery boundaries, and visual descriptions.
5. The PDF contains zero link annotations. The four lab paths are visible code text rather than clickable links; their targets were verified on disk.
6. Slides 24-26 use prominent claim-boundary gates, but instructors must still announce the selected source mode before showing metrics so learners do not treat the surrogate scoreboard as canonical transfer evidence.

### Visual Inspection Method

The final PDF was structurally checked with PyMuPDF and pypdf. Every page was rasterized and inspected in four contact sheets covering pages 1-9, 10-18, 19-27, and 28-36. The eight SVG pages were separately rasterized and inspected at exactly `1920 x 1080`. Pages 24-26 and 34-35 were also inspected individually at `1920 x 1080` after the final source-mode and check-timing revisions. Automated checks confirmed 36 pages, `960 x 540` geometry, sequential numbered headings, zero out-of-bounds text blocks, all source notes, all asset and lab paths, and absence of unsupported literal source syntax.

### Day 3 Disposition

Day 3 render status is **PASS**. The delivery artifact is a real 36-page Marp render; all eight SVGs render and remain legible; slide IDs, ordering, lab paths, source-mode boundaries, slide-20 rejection language, and final-check timing are preserved. The source-description and PDF accessibility limitations above are nonblocking but must remain explicit. No participant notebook, solution notebook, Day 1 artifact, or Day 2 artifact was modified during this remediation.

## Day 4 - Think Like an ML Engineer

**Status: PASS**
**Validation date:** 2026-08-17

### Artifact and Renderer

- Source: `courseware/slides/day-4-think-like-an-ml-engineer.md`
- Delivery PDF: `courseware/slides/day-4-think-like-an-ml-engineer.pdf`
- Renderer: Marp CLI `4.5.0` with Marp Core `4.4.0`, invoked via `npx`
- Render command: `npx -y @marp-team/marp-cli@4.5.0 courseware/slides/day-4-think-like-an-ml-engineer.md --pdf --allow-local-files --output courseware/slides/day-4-think-like-an-ml-engineer.pdf`
- Final source SHA-256: `69d53c34bcc0534c597544075a2c533243aaac6e491efaf01bf15e235511303b`
- PDF page count: `34`
- PDF size: `373683` bytes
- PDF SHA-256: `3ee895ff5b637a87a8572d5c9ded0f7d510774b061ce324e8289e4d9995adbcf`
- Page geometry: `960 x 540` points, 16:9

`--allow-local-files` is required for the nine repository-local SVG references. Marp reported that local-file access was enabled and completed without a missing-resource or conversion error.

### Render QA

| Check | Result | Evidence |
|---|---|---|
| Current source and page count | PASS | The final source contains exactly 34 slides and the final PDF contains exactly 34 pages. The source was rerendered after the only note corrections. |
| Displayed sequence, IDs, and timing | PASS | Extracted headings are sequential from `01` through `34`. `ACT-D4-01` through `ACT-D4-04`, `LAB-D4-01` through `LAB-D4-03`, four `CHECK-D4` IDs, the capstone brief, rubric, and defense retain their intended order. Slide 3 states the 450-minute day; slides 16 and 34 show the four five-minute live minima and the 16:30 append-only consolidation contract; slides 32-33 preserve the five-minute defense. This agrees with both current Day 4 guides' exact 450-minute schedules. |
| Clipping, overflow, and readability | PASS | Every page was inspected in four contact sheets. Text-block geometry found zero out-of-bounds blocks. No visible text, table, formula, gate, path, or diagram is clipped or overlaps another element. |
| Unsupported literal syntax | PASS | Extracted PDF text contains no Markdown fence, Mermaid `flowchart`, HTML image/comment markup, speaker-note label, alt-text label, or asset-path label. |
| Missing images and asset placement | PASS | All nine SVG references resolve on disk and render as vector content on pages 6, 11, 14, 17, 19, 21, 25, 30, and 32. Marp reported no missing resource. |
| Asset and capstone legibility | PASS | All nine asset pages and capstone/rubric pages 28-33 were inspected individually at exactly `1920 x 1080`. Titles, axes, curves, counts, lane text, gates, caveats, rubric weights, and defense stages are readable and unclipped. |
| Fonts | PASS | The final PDF uses embedded/subset Helvetica Neue, Helvetica, and Menlo faces from the declared font stacks. Body text, code paths, formulas, and SVG labels remain readable in the full-HD inspection. |
| Visible lab paths | PASS | The three displayed participant notebook paths on pages 10, 13, and 23 resolve to the current `LAB-D4-01`, `LAB-D4-02`, and `LAB-D4-03` notebooks. |
| Participant-facing separation | PASS | Visible slide source contains no link or reference to the capstone solution, instructor guide, instructor-solutions tree, case key, or solution notebook. No visible case-letter-to-cause mapping or profile diagnosis appears. |
| Source notes and SVG descriptions | PASS WITH LIMITATIONS | All 34 slides contain speaker notes and an `Alt text:` source note. All nine asset slides contain descriptive HTML `alt` and `Asset path:` notes. Every SVG contains `role="img"`, `<title>`, and `<desc>`. PDF export limitations are recorded below. |
| PDF links | PASS WITH LIMITATION | The PDF contains zero link annotations. Displayed notebook paths are visible code text, so their targets were checked on disk but click activation is unavailable. |

### Asset Mapping and Legibility

| Asset | PDF page | Source view box | Result |
|---|---:|---:|---|
| `threshold-confusion-cost.svg` | 6 | `1200 x 620` | Rendered; three thresholds, confusion counts, precision/recall values, cost directions, and the fixed-score boundary are readable. |
| `mystery-curves.svg` | 11 | `1200 x 620` | Rendered on aligned axes; A-D labels, train/validation styles, and the no-unique-cause caveat are readable without revealing diagnoses. |
| `error-funnel.svg` | 14 | `1200 x 620` | Rendered; all five funnel levels, both side constraints, and the priority rule are readable. |
| `experiment-chain.svg` | 17 | `1200 x 620` | Rendered; the one-change evidence chain, clean-negative-result panel, crossed-out confounded run, and stop-rule prompt are readable. |
| `reproducibility-record.svg` | 19 | `1200 x 620` | Rendered; incomplete and usable records plus the environment-and-tolerance claim boundary are readable. |
| `quality-resource-pareto.svg` | 21 | `1200 x 620` | Rendered; points P/Q/R/S, dominance relation, axes, scenario choices, and unmeasured-resource caveat are readable. |
| `frontier-case-cards.svg` | 25 | `1200 x 620` | Rendered; all seven case categories, evidence objects, central loop, and scope caveat are readable. |
| `capstone-evidence-board.svg` | 30 | `1200 x 620` | Rendered; four evidence lanes, five gates, A/B/C anonymity statement, and cached-output label rule are readable. |
| `capstone-rubric-defense.svg` | 32 | `1200 x 620` | Rendered; canonical weights, negative-result rule, five one-minute defense stages, and test-lock statement are readable. |

### Capstone Consistency and Separation

The capstone result is **PASS** against the current student guide, rubric, instructor guide, both Day 4 guides, and current participant/solution summaries.

1. Slide 32 and `capstone-rubric-defense.svg` use the canonical `25/20/20/15/10/10` allocation: performance, generalization, experiment design, diagnosis, efficiency, and explanation. The visual now states that the team score and individual check are separate. This matches the capstone rubric and both instructor guides.
2. Slides 29-30 require one primary experiment, one major factor, predeclared expected/rejecting evidence, and interpretation before the decision is locked. This matches the capstone student guide and rubric.
3. Slides 28, 30, and 31 expose only anonymous `A`, `B`, or `C`. Source/PDF searches found no mapping from a letter to a diagnosis, cause, configuration, or preferred intervention.
4. Slides 28-30 and 32 preserve one authorized final test access after decision lock. This matches the canonical five-gate contract.
5. Slide 33 preserves the five-stage defense and asks for evidence that both supports and threatens the diagnosis. The instructor guide's no-diagnosis-reveal-before/between-defenses rule is not contradicted anywhere in participant-visible slide text.
6. The current participant and solution summaries report all Day 4 local CPU paths and A/B/C capstone branches as PASS WITH NOTES and confirm participant separation. The slides do not convert those local results into a hosted-Colab claim.

### Source Correction During QA

Slides 10, 13, and 23 had stale speaker notes saying their notebooks were missing or future artifacts. The current participant and solution summaries show that those local CPU paths passed with notes. The three notes now state that local result while retaining the explicit limitation that hosted Colab validation has not been established.

The current remediation also replaced the stale source comment that said PDF rendering was deferred, aligned slides 16 and 34 to the five-minute live-minimum/end-of-day-consolidation contract, added defense-topology and separation speaker notes, and corrected the slide-32 rubric visual from combined team/individual wording to **team score and individual check are separate**. No notebook, prior-day PDF, or prior-day validation evidence was modified.

### Accessibility and Link Limitations

1. The PDF is marked as tagged, but it contains zero exported `/Figure` or `/Alt` entries. Source HTML `alt`, SVG `<title>`/`<desc>`, and source-note descriptions therefore must not be represented as usable PDF figure alternatives.
2. Full reading order, screen-reader behavior, keyboard navigation, color-contrast conformance, and PDF/UA compliance were not tested with assistive technology or a dedicated accessibility checker.
3. Speaker notes are intentionally absent from the delivery PDF. Instructors need the Markdown source or instructor guide for delivery cues, reveal discipline, and visual descriptions.
4. The deck defines no clickable links. The three displayed lab paths are visible code text; the capstone is launched through the guide/brief flow rather than a fourth visible notebook path on the slides.
5. Hosted Google Colab execution remains outside this render validation. The corrected notes preserve that limitation rather than implying that local CPU lab validation proves hosted readiness.

### Visual Inspection Method

The deck was rendered with the pinned Marp CLI and structurally checked with PyMuPDF. Every page was inspected in four contact sheets covering pages 1-9, 10-18, 19-27, and 28-34. The changed check pages 16 and 34 were inspected individually at exactly `1920 x 1080`; after the final asset-only rerender they remained pixel-identical to those inspected images. The corrected rubric page 32 was then inspected individually at `1920 x 1080` to confirm both lines fit inside the callout. Automated checks confirmed 34 pages, `960 x 540` geometry, sequential headings, zero out-of-bounds text blocks, nine resolving assets, all visible local paths, and the final size and hashes above.

### Day 4 Disposition

Day 4 render status is **PASS**. The delivery artifact is a real 34-page Marp render; all nine SVGs render on the expected pages and remain legible; the slide sequence, IDs, timing, displayed lab paths, capstone contract, rubric weights, anonymity, test lock, defense, and participant separation are consistent with the current canonical artifacts. The accessibility, non-clickable-path, and hosted-execution limitations above are nonblocking but must remain explicit.

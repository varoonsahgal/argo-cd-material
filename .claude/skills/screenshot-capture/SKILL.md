---
name: screenshot-capture
description: Source, capture, or precisely specify Argo CD (or Rancher) UI screenshots so every navigation step in a guide is visually clear and version-accurate. Use whenever a guide tells a participant to open, navigate, click, or observe something in a UI.
---

# Screenshot Capture

Read [capture checklist](./capture-checklist.md) for the recurring screens this course needs.

## Procedure
1. Determine the exact screen and state needed: which page, what filters/selection are applied, and what must be visible for the teaching point to land.
2. **Prefer capturing it live** from this course's own provisioned Argo CD instance, at the exact version the course targets, using a browser-automation tool if one is available. This guarantees version accuracy and avoids any licensing ambiguity, since it's the course's own environment.
3. **If no live instance is reachable while authoring**, use the `web` tool to find a current screenshot of the same screen in the official Argo CD documentation (argo-cd.readthedocs.io) or the `argoproj/argo-cd` GitHub repository. Embed it with a caption crediting "Argo CD documentation," the retrieval date, and the Argo CD version it shows. Confirm that version is reasonably close to the one this course targets — note it plainly if it isn't.
4. **If neither is available**, do not fabricate a description of pixels you have not seen. Write a precise capture spec instead — the exact page, the exact steps to reach it, and the exact elements to highlight or crop — inside a clearly labeled "SCREENSHOT NEEDED" callout, so it can be captured later against the real classroom environment.
5. Store captured/downloaded images under `courseware/assets/screenshots/<day>/<file-id>-<NN>-<slug>.png` and reference them by relative path with descriptive alt text and a short caption.
6. Always pair a screenshot with a short numbered text description of what to notice — the guide must remain usable even if an image fails to render.
7. Re-verify screenshots whenever the targeted Argo CD version changes. The UI has changed materially across major versions (navigation layout, where Sync/Refresh/History live, ApplicationSet visibility) — never assume an older screenshot still matches.

## Rule
A screenshot (or its capture spec) is not optional decoration — it is part of the instruction. A guide with an unillustrated multi-click UI navigation step is incomplete.

---
name: ui-mockup-review
description: Audit existing product UI screenshots, wireframes, mockups, or visual references and generate missing representative digital product mockups for user review when no reviewable UI exists. Use when a PRD and screen specification need a concrete visual direction before Figma production, when the user wants UI images made with ImageGen, when multiple layout or style alternatives must be compared, or when mockups must be classified, named, organized, revised, and approved as visual references. Treat generated images as concepts rather than production specifications.
---

# UI Mockup Review

Create a shared visual reference for the user and AI before full Figma construction.

## Audit available visuals

1. Open and inspect every relevant screenshot, wireframe, mockup, or reference.
2. Map each image to a screen ID and state.
3. Classify it as `APPROVED`, `REVISE`, `REFERENCE ONLY`, `DUPLICATE`, `OUTDATED`, or `MISSING`.
4. In report-only mode, propose file organization without renaming or moving anything. Organize files only when the user asks for artifact changes.
5. Identify the smallest representative set needed to establish the visual system.

Read [visual-review-rubric.md](references/visual-review-rubric.md) before generating or approving visuals.

## Generate only when needed

If no reviewable visual direction exists after the screen specification is stable:

1. For an audit-only request, report the missing representative set and stop without generation.
2. When the user has asked to create visuals or has approved entering the visual-production stage, load and follow the ImageGen skill.
3. Generate representative screens, not the entire product.
4. Cover at least the principal surface, one detail or task surface, and one important state or overlay.
5. Use the approved screen content, hierarchy, actions, platform, and visual constraints.
6. Label every output `[AI DRAFT — VISUAL CONCEPT]`.

If existing visuals cover part of the product, generate only missing representative screens after the same authoring authorization.

## Separate concept from specification

Generated pixels may suggest visual hierarchy, density, typography, color, imagery, and composition. They do not independently define:

- exact component dimensions;
- production copy;
- button behavior;
- accessibility;
- responsive rules;
- component variants;
- data or entitlement policy.

Resolve those in the screen specification or Figma system.

## Review with the user

For each candidate explain:

- intended screen and state;
- what design hypothesis it tests;
- strengths;
- risks or mismatches;
- recommended selection and rationale;
- elements to carry into Figma.

Ask the user to approve, revise, combine, or reject. After approval, mark the chosen reference `[APPROVED VISUAL REFERENCE]` and record its linked screen IDs and date.

## Exit

The visual gate passes only when representative visual references establish:

- overall direction;
- layout and hierarchy;
- content density;
- navigation pattern;
- media treatment;
- component character;
- light/dark or platform expectations when in scope;
- explicit approved and rejected patterns.

Do not start a large Figma build from unreviewed AI mockups.

When run independently and the visual gate passes, state the completed stage, the next recommended journey, its benefit, the risk of skipping it, and the first next review item.

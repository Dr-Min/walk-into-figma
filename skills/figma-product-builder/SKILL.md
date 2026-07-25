---
name: figma-product-builder
description: Create or update structured digital product designs in Figma from approved PRDs, screen and interaction specifications, visual references, existing design systems, frontend code, or prior Figma files. Use when the user asks to build Figma screens, reusable components, variables, styles, variants, responsive layouts, light or dark themes, clickable prototype flows, or synchronize approved product changes into Figma. Verify the authenticated account, team, file, scope, and approved visual direction before writing; use the official Figma skills and search existing design systems before creating new components.
---

# Figma Product Builder

Build an editable product system, not a collection of flattened screenshots.

## Load required Figma guidance

Before any Figma write:

1. Load the applicable official Figma skill.
2. For a new file, use the Figma new-file workflow.
3. For code-to-design or screen generation, use the appropriate Figma generation workflow.
4. Before component work, search the target design system and libraries.
5. Use Figma tools for all Figma mutations.

## Verify the write target

Confirm and report:

- authenticated account identity;
- organization or team;
- target file or new-file destination;
- editable permission;
- platforms and breakpoints;
- approved screen and visual scope;
- whether existing content may be modified.

Stop if the identity, team, or destination differs from the user's instruction.

## Inspect inputs

Require:

- approved PRD or approved implementation subset;
- approved screen and interaction specification;
- approved visual references;
- latest decision log;
- existing design system or codebase when applicable.

List unresolved mismatches before writing. Do not silently let a mockup override a newer requirement.

Read [figma-build-contract.md](references/figma-build-contract.md) for page structure, build order, prototype requirements, and manifest fields.

## Build in chapters

1. Cover and source index
2. Foundations: color, typography, spacing, radius, elevation, grid
3. Reusable components and variants
4. Core screens
5. Secondary and exception states
6. Responsive or platform variants
7. Prototype flows
8. Documentation and manifest

After each chapter, inspect the actual Figma result. Compare it with the approved reference and specification. In staged review mode, show the chapter result and ask the user to revise or approve it before continuing. Correct inconsistencies before expanding them.

## Preserve editability and scalability

- Use variables, styles, auto layout, constraints, component properties, and variants.
- Reuse existing system components when a match exists.
- Use semantic names linked to stable IDs.
- Avoid pasted screenshots as implementation surfaces.
- Represent repeated content with scalable components.
- Keep prototype-only annotations separate from product UI.
- Support the approved light/dark and platform variants without duplicating arbitrary values.

## Prototype behavior

Implement the approved primary journeys and representative failure or locked states. Map every MVP action ID to either a working prototype interaction or an explicit `[SPEC ONLY]` annotation with its linked behavior and reason. Every hotspot must match the action contract. Include back, close, modal dismissal, and recovery behavior. Do not invent missing business rules inside Figma.

## Record the build

Create or update `figma-build-manifest.json` with:

- source PRD version/hash;
- Figma file key and team;
- dates;
- built screen IDs;
- component IDs;
- prototype flows;
- pending synchronization;
- accepted exceptions.

## Exit

Pass only when the approved scope is editable, reusable, traceable, and prototype-linked, and no action remains `BLOCKED`. Then hand off to `$figma-handoff-audit`.

When run independently and the build gate passes, state the completed stage, the audit journey that follows, its benefit, the risk of skipping it, and the first audit item.

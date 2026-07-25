---
name: figma-handoff-audit
description: Read-only audit of a digital product Figma file against approved PRDs, decision logs, screen specifications, interaction maps, visual references, and build manifests. Use when the user asks to review Figma completeness, check every button and prototype destination, detect missing screens or states, find drift between documents and design, evaluate design-system consistency, verify responsive variants, inspect handoff readiness, or produce a prioritized QA and developer-handoff report. Do not modify Figma unless the user separately authorizes fixes.
---

# Figma Handoff Audit

Determine whether the Figma artifact is complete, faithful, interactive, and ready for implementation.

## Audit read-only

1. Load the official Figma inspection skill before reading the file.
2. Verify the target file and source documents.
3. Compare the Figma manifest with current source versions.
4. Inspect structure, representative screenshots, component usage, and prototype links.
5. Do not alter Figma during an audit unless the user explicitly asks for fixes.

Read [audit-checklist.md](references/audit-checklist.md) for coverage and severity rules.

## Compare five layers

1. **Requirements** — every MVP requirement is represented.
2. **Screens and states** — every approved screen/state exists and no critical orphan appears.
3. **Interactions** — every specified action has the correct reaction or destination.
4. **Visual system** — components, tokens, hierarchy, content, and approved direction are consistent.
5. **Developer handoff** — naming, responsive behavior, copy, assets, annotations, and exceptions are usable.

## Test journeys

Use Figma Present mode or available browser control for primary flows when possible. Test:

- first entry and return entry;
- main success path;
- back and close behavior;
- locked, permission, payment, or entitlement path;
- error and recovery path;
- mobile and desktop variation when in scope.

Do not claim an interaction works from static frame inspection alone.

## Report evidence

For report-only requests, return the audit in chat without writing files. When the user asks to save a handoff artifact, create `FIGMA_QA_REPORT.md` with:

- source versions and file identity;
- coverage summary;
- tested flows;
- findings by severity;
- screenshots, node IDs, or frame names;
- requirement/action/state IDs;
- recommended fix;
- accepted exceptions;
- final handoff verdict.

## Verdicts

- `READY` — no blocking or major unresolved finding; sources are synchronized.
- `READY WITH ACCEPTED EXCEPTIONS` — material exceptions are explicitly accepted and recorded.
- `NOT READY` — any blocking finding, untested primary journey, source drift, or missing material state remains.

Never accept a `BLOCKER` as an exception. Report that a separately authorized remediation must fix it, remove the affected capability from the approved release scope, or reclassify it only with new evidence. Do not perform that remediation during a read-only audit. Every MVP action must be `PROTOTYPED` or explicitly documented as `SPEC ONLY`; an unclassified action makes the file `NOT READY`.

Never equate a visually polished file with handoff readiness.

When run independently, explain the audit verdict, the benefit of resolving the next finding group, the consequence of leaving it unresolved, and the first next review item.

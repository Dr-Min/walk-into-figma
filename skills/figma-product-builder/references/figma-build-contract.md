# Figma Build Contract

## Recommended pages

```text
00 Cover & Sources
01 Foundations
02 Components
03 Core Screens
04 States & Overlays
05 Responsive / Platforms
06 Prototype Flows
07 Archive
```

Adapt names to an existing file, but preserve clear separation.

## Build order

1. Search existing libraries and target-file components.
2. Map approved tokens to Figma variables and styles.
3. Build primitives and composite components.
4. Create variants for size, state, theme, entitlement, and platform only when needed.
5. Assemble core screens from components.
6. Add empty, loading, error, locked, success, and degraded states.
7. Link prototype actions from the interaction specification.
8. Inspect representative frames at target viewport sizes.

## Naming

Use stable, semantic names:

```text
COMP-012 / Button / Primary / Default
SCR-004 / Chat / Paid / Default
STATE-023 / Gallery / Empty
FLOW-002 / Upgrade / Success
```

## Prototype coverage

For each primary flow record:

- starting frame;
- actions and destinations;
- overlay behavior;
- success end state;
- at least one important failure or recovery path;
- platform-specific divergence.

For every MVP action ID, record one of:

- `PROTOTYPED` — working link, overlay, state change, or variable interaction;
- `SPEC ONLY` — not practical to simulate in Figma, with the exact linked specification and visible annotation;
- `BLOCKED` — missing decision or source conflict that prevents correct implementation.

The action coverage matrix must contain no unclassified action. Any `BLOCKED` action forces `FIGMA BUILD STATUS: NOT COMPLETE` and prevents the build gate from passing.

## Build quality checks

- no unexpected detached instances;
- no unexplained raw colors or text styles;
- auto layout used for dynamic content;
- realistic text and data;
- touch targets and contrast reviewed;
- responsive constraints behave at target sizes;
- screenshots used only as references, not as the final UI;
- all pending mismatches recorded.

## Manifest

Use valid JSON:

```json
{
  "project": "Example",
  "prd_version": "1.0",
  "prd_hash": "sha256:...",
  "figma_file_key": "...",
  "figma_team": "...",
  "built_at": "YYYY-MM-DD",
  "synced_at": "YYYY-MM-DD",
  "screen_ids": ["SCR-001"],
  "component_ids": ["COMP-001"],
  "prototype_flows": ["FLOW-001"],
  "pending_sync": [],
  "accepted_exceptions": []
}
```

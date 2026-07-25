# Artifact Contract

Use existing project naming when present. Otherwise create:

```text
product/
├── project-intake.yaml
├── PRD.md
├── DECISION_LOG.md
├── IA_AND_USER_FLOWS.md
├── SCREEN_AND_INTERACTION_SPEC.md
├── UI_COPY.md
├── design_previews/
├── figma-build-manifest.json
└── FIGMA_QA_REPORT.md
```

## Traceability

Every important artifact must include:

- project name and version;
- status: `AI DRAFT`, `REVIEW`, or `APPROVED`;
- source artifacts;
- last updated date;
- unresolved decision IDs;
- related screen or requirement IDs.

Use stable IDs:

- `REQ-###` requirement
- `DEC-###` decision
- `FLOW-###` journey
- `SCR-###` screen
- `ACT-###` action
- `STATE-###` state
- `ERR-###` exception
- `COMP-###` component
- `QA-###` finding

## Decision log

Record:

```markdown
| ID | Topic | Status | Decision or recommendation | Rationale | Source | Date |
|---|---|---|---|---|---|---|
```

Never rewrite historical decisions without recording supersession.

Each decision entry must carry status and effective timing. A newer `[USER CONFIRMED]` entry may supersede an approved PRD decision, but the PRD becomes `OUTDATED` until synchronized and re-approved. Drafts and AI recommendations never supersede approved sources.

## Figma manifest

Record at minimum:

```json
{
  "project": "",
  "prd_version": "",
  "prd_hash": "",
  "figma_file_key": "",
  "figma_team": "",
  "built_at": "",
  "synced_at": "",
  "screen_ids": [],
  "component_ids": [],
  "prototype_flows": [],
  "pending_sync": [],
  "accepted_exceptions": []
}
```

Compare manifest and source artifacts during every audit to detect drift.

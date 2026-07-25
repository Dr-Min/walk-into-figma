# Orchestration Contract

## Contents

1. Intake
2. Routing
3. Review modes
4. Decision rules
5. Stage exit rules

## Intake

Inspect before interviewing. Accept rough notes, proposals, PRDs, spreadsheets, decision logs, screenshots, mockups, Figma URLs, code, or any combination.

Create `project-intake.yaml` with:

```yaml
project:
  name: ""
  goal: ""
  platforms: []
sources:
  - path_or_url: ""
    type: ""
    status: FOUND
    authority: ""
    last_modified: ""
stages:
  discovery_prd: MISSING
  screen_spec: MISSING
  visual_reference: MISSING
  figma_build: MISSING
  handoff_audit: MISSING
mode: staged-review
```

Use `CONFLICT` when two sources disagree. Use `OUTDATED` when a newer authoritative source supersedes an artifact.

## Routing

```text
Scan inputs
  ├─ No stable product definition → Product discovery & PRD
  ├─ PRD ready, interactions missing → UI screen specification
  ├─ Specs ready, no approved visuals → UI mockup review
  ├─ Visuals approved, no structured Figma → Figma product builder
  └─ Figma exists → Figma handoff audit
```

Skip a stage only when its exit criteria are evidenced by current artifacts. Existing Figma does not prove that the PRD or interaction specification is complete.

## Review modes

### Operation mode

Determine mutation authority independently from review cadence:

- `REPORT ONLY` — inspect and respond in chat; do not write, rename, organize, generate, or update artifacts.
- `ARTIFACT AUTHORING` — create or update local project artifacts requested by the user.
- `EXTERNAL WRITE` — mutate Figma or another connected system only within the approved destination and scope.

A request to review, audit, explain, compare, or report status does not authorize artifact writes. If the user later asks to save the report, switch to `ARTIFACT AUTHORING`.

### Staged review

Default. At each chapter boundary, report:

```text
Chapter:
Status:
Confirmed:
AI recommendation + rationale:
Decision required:
Conflicts:
Files updated:
Question: Revise this chapter, or approve it and continue?
```

Batch related decisions, but ask at most three closely related material decisions per turn. Keep later blockers in a queued register. Do not interrupt for minor reversible details.

### Autonomous execution

Use only after explicit user direction. Continue across chapters while:

- preserving existing work;
- recording assumptions;
- avoiding irreversible external changes;
- stopping for material ambiguity.

## Decision rules

Ask when the choice materially changes:

- audience, value, scope, roadmap, or platform;
- monetization, entitlement, limits, or refunds;
- legal, safety, privacy, identity, or regional policy;
- primary journey, navigation, or major interaction;
- visual direction or brand;
- production account, team, file, or overwrite scope.

Recommend and record without stopping when the choice is conventional, reversible, low-risk, and consistent with approved rules.

Use these labels consistently:

- `[USER CONFIRMED]`
- `[AI RECOMMENDATION]`
- `[DECISION REQUIRED]`
- `[APPROVAL REQUIRED]`
- `[CONFLICT]`
- `[DEFERRED]`

## Stage exit rules

| Stage | Exit condition |
|---|---|
| Discovery/PRD | Completion rubric passes and user approves |
| Screen specification | All MVP screens, actions, states, exceptions, and destinations are mapped |
| Visual reference | Representative screens are visually reviewed and approved |
| Figma build | Approved scope exists as reusable components, screens, and prototype links |
| Handoff audit | Every `BLOCKER` is fixed; `MAJOR` findings are fixed or explicitly accepted with owner and rationale |

At a failed gate, explain exactly what prevents completion. Never hide missing decisions behind a percentage.

A `BLOCKER` cannot be waived into a ready verdict. Fix it, remove the affected capability from the approved release scope, or reclassify it only with new evidence.

## Major-stage transition message

Only after an exit condition passes, communicate:

1. `Completed` — stage number/name and approved outputs.
2. `Next journey` — the next stage and its goal.
3. `Why it matters` — a product-specific benefit.
4. `If skipped` — a plausible delivery, usability, cost, or rework risk.
5. `Next review` — the first item the user will inspect or decide.

Use warm, direct language. Avoid generic praise and exaggerated claims. If the gate fails, replace the completion message with a blocker report and the shortest path to pass.

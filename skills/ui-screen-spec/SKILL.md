---
name: ui-screen-spec
description: Convert approved product requirements, PRDs, decision logs, or existing interfaces into implementation-ready information architecture, user flows, screen inventories, screen specifications, UI copy, state matrices, and interaction contracts. Use when the user asks what pages are needed, what every button does, where an action navigates, which modal, sheet, menu, or state appears, how desktop and mobile differ, or whether all happy paths, empty states, errors, loading states, permissions, paywalls, and recovery paths are covered before mockups or Figma production.
---

# UI Screen Specification

Define behavior before polishing appearance. Make every user action traceable to a visible result.

## Inspect and map

1. Read the latest approved PRD and decision log.
2. Inventory existing screens, mockups, routes, components, and UI copy.
3. Build the IA and primary journeys.
4. Assign stable IDs to flows, screens, actions, states, and exceptions.
5. Flag any behavioral question that the PRD does not answer.

For audit-only requests, report gaps without creating or updating specification files.

Read [screen-contract.md](references/screen-contract.md) for the required schema and exit checklist.

## Specify every MVP screen

For each screen define:

- purpose and entry conditions;
- user roles and entitlements;
- hierarchy and content regions;
- displayed data and provenance;
- all controls and actions;
- destination or visible reaction for every action;
- default, loading, empty, success, error, offline, permission, locked, and degraded states;
- modal, sheet, popover, menu, toast, inline feedback, or navigation behavior;
- responsive differences;
- accessibility and localization notes;
- analytics events;
- linked requirements and acceptance criteria.

Never write only “button opens next screen.” Name the destination, transition, preserved state, back behavior, and failure response.

## Build the action map

For every clickable or tappable element record:

```text
ACT ID → trigger → precondition → system response → destination/overlay
       → loading → success → error → recovery → event
```

Include browser/system back, close, escape, outside-click, destructive confirmation, double-submit prevention, and interrupted payment or network recovery where applicable.

## Treat surfaces deliberately

Choose based on task:

- page for durable navigation or deep-linkable work;
- modal for focused blocking decisions;
- bottom sheet for mobile contextual actions;
- popover/menu for compact local choices;
- inline expansion for contextual detail without navigation;
- toast only for transient confirmation, never for information the user must retain.

Record why a major overlay is not a page when the choice affects navigation or accessibility.

## Review in chapters

Review IA, primary journeys, screen inventory, interaction maps, and exceptions as separate chapters. Show confirmed rules, recommendations with rationale, missing decisions, and conflicts. Do not advance to visual mockups with unresolved primary-flow behavior.

## Exit

Mark the specification complete only when:

- every MVP requirement maps to at least one screen or system behavior;
- every interactive control maps to a result;
- all primary journeys include recovery paths;
- relevant states are specified;
- desktop/mobile/platform differences are explicit;
- every current-MVP and primary-flow behavior is decided;
- a post-MVP behavior is deferred only with user approval, owner, target release or review date, current-release impact, and temporary behavior;
- the user approves the specification summary.

Otherwise return `SCREEN SPEC STATUS: NOT COMPLETE` and list exact blockers.

When run independently and the gate passes, state the completed stage, the next recommended journey, its benefit, the risk of skipping it, and the first next review item.

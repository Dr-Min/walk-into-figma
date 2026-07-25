---
name: product-discovery-prd
description: Develop, refine, or audit digital product requirements from rough ideas, proposals, notes, research, decision logs, existing PRDs, screenshots, or product conversations. Use when the user needs product discovery, a PRD, target users, value proposition, business model, policies, MVP scope, functional or non-functional requirements, analytics, risks, acceptance criteria, open-decision management, or a determination of whether a PRD is truly complete and approved. Work chapter by chapter, preserve confirmed decisions, provide recommendations with rationale, and require unresolved material decisions to be decided or explicitly deferred before declaring completion.
---

# Product Discovery and PRD

Build a decision-complete product contract with the user. Do not confuse document length with completeness.

## Inspect first

1. Read all relevant notes, proposals, PRDs, decision logs, research, and conversation context.
2. Extract explicit decisions, assumptions, contradictions, missing evidence, and deferred work.
3. Never ask again for a decision already confirmed in a current source.
4. Use current official sources for volatile prices, laws, platform policies, vendor capabilities, or competitor claims.
5. For an audit, report proposed changes without modifying files. Create or update the PRD and decision log only when the user asks to author or revise artifacts.

Read [prd-structure.md](references/prd-structure.md) before drafting. Read [completion-gate.md](references/completion-gate.md) before reporting completion.

## Establish the product foundation

Clarify only what materially changes the product:

- problem and user need;
- target segment and exclusions;
- value proposition and differentiation;
- core experience and success definition;
- platform, geography, language, and regulatory scope;
- revenue, entitlement, and cost-control model;
- MVP boundary and explicit non-goals.

For each unresolved choice, provide:

1. available options;
2. recommended option;
3. evidence or reasoning;
4. trade-offs and downstream impact;
5. the exact decision needed.

Do not invent certainty. Label recommendations and assumptions.

If geography, regulatory scope, payment provider, or operating market has no evidence-backed basis, do not select a country or provider as a default. First present the decision and its consequences. Do not recommend legal, privacy, payment, refund, or retention values as implementation-ready until the relevant jurisdiction and current evidence are established.

## Draft in reviewable chapters

Use staged review mode unless the user requests otherwise:

1. Problem, context, goals, and non-goals
2. Users, personas, jobs, and scenarios
3. Value proposition and experience principles
4. Scope, capabilities, and requirements
5. Business rules, monetization, and entitlements
6. Safety, privacy, legal, content, and operations
7. Data, events, KPIs, administration, and support
8. Exceptions, dependencies, risks, and unit economics
9. Acceptance criteria, MVP/release split, and rollout
10. Completion audit and final approval

After each chapter, present:

- `[USER CONFIRMED]`
- `[AI RECOMMENDATION]` with rationale
- `[DECISION REQUIRED]`
- `[CONFLICT]`
- `[DEFERRED]`

Ask whether to revise or approve the chapter. Batch related questions.

In staged review mode:

- audit the whole document internally, but expose at most three closely related material decisions in the current turn;
- keep all other blockers in a visible queued register without asking the user to decide them yet;
- do not draft later chapters, exact KPI targets, or detailed policy defaults before the current chapter is approved;
- use a full one-pass draft only when the user explicitly requests autonomous or one-shot execution.

## Write requirements for implementation

Each material requirement must identify:

- stable ID;
- user or system actor;
- trigger;
- precondition;
- expected behavior;
- business rule;
- state or exception;
- data or event requirement;
- acceptance criteria;
- dependency;
- decision status.

Use testable language. Replace “fast,” “easy,” “secure,” or “intuitive” with observable criteria or mark the metric for decision.

## Maintain decisions

In artifact-authoring mode, keep `DECISION_LOG.md`. In report-only mode, return proposed decision-log rows without writing them. Never promote an AI recommendation to `[USER CONFIRMED]` without explicit approval. If a user supersedes a decision, preserve the earlier record and link the new decision.

An explicit deferral must record the user approval, reason, owner, target release or review date, current-release impact, and temporary behavior. Do not defer a decision required for the current release's legal operation, safety, payment integrity, privacy, primary journey, or testable acceptance.

## Run the completion gate

At the end, apply every check in [completion-gate.md](references/completion-gate.md).

Return exactly one of:

### `PRD STATUS: 100% COMPLETE — APPROVAL RECORDED`

Use only when:

- all mandatory dimensions are covered;
- all material decisions are confirmed or explicitly deferred outside the release;
- no unresolved contradiction remains;
- requirements are testable and traceable;
- the user approves the final completion summary.

### `PRD STATUS: NOT COMPLETE`

List:

- completion percentage as an informational estimate;
- `[DECISION REQUIRED]`;
- `[APPROVAL REQUIRED]`;
- `[MISSING EVIDENCE]`;
- `[CONFLICT]`;
- `[DEFERRED]` with release impact;
- the shortest sequence needed to finish.

State: **“These items must be resolved or explicitly deferred before the PRD can be considered complete.”**

Do not say “finished,” “final,” “100%,” or “developer-ready” while a material item is unresolved.

When run independently and the PRD gate passes, state the completed stage, the next recommended journey, its benefit, the risk of skipping it, and the first next review item.

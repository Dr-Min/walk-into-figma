# PRD Completion Gate

## Purpose

Separate a polished draft from an approved implementation contract. A percentage is diagnostic; it does not override blocking omissions.

## Score

Score each applicable dimension:

- `0` missing
- `1` drafted but unapproved or materially ambiguous
- `2` complete, traceable, and approved
- `N/A` explicitly justified

| Dimension | Weight |
|---|---:|
| Problem, evidence, goals, non-goals | 8 |
| Target users, jobs, scenarios, exclusions | 8 |
| Value and core experience | 7 |
| MVP scope and release boundary | 10 |
| Functional requirements | 12 |
| User journeys and information architecture | 8 |
| Business model, entitlements, billing policies | 8 |
| Data, privacy, safety, legal, regional policy | 10 |
| Content, operations, support, administration | 6 |
| Errors, fallbacks, limits, non-functional requirements | 7 |
| Analytics, KPIs, events, experiments | 5 |
| Acceptance criteria and traceability | 6 |
| Dependencies, risks, rollout, rollback | 5 |

For each applicable dimension, calculate its contribution as:

```text
dimension contribution = weight × (score / 2)
```

Then calculate:

```text
completion % =
  sum(applicable dimension contributions)
  / sum(applicable dimension weights)
  × 100
```

Exclude an `N/A` dimension from both numerator and denominator only when the reason is recorded and approved. Round to one decimal place for display. Never round a value below 100 up to 100.

## Blocking conditions

The PRD cannot be complete if any applicable item remains:

- a material decision has no owner or disposition;
- an `[AI RECOMMENDATION]` is treated as approved;
- sources conflict on scope, policy, price, entitlement, or behavior;
- an MVP requirement lacks a testable acceptance criterion;
- a primary action has no destination, result, state, or recovery behavior;
- legal, privacy, payment, safety, or regional assumptions are presented as fact without validation;
- a current-release legal, safety, privacy, payment, or primary-journey decision is labeled deferred;
- an external dependency has no failure or fallback policy;
- the release boundary is unclear;
- final user approval is absent.

## Final report

Produce:

```markdown
# PRD Completion Report

Status: NOT COMPLETE | 100% COMPLETE — APPROVAL RECORDED
Diagnostic completion: NN%

## Approved scope
## Decision required
## Approval required
## Missing evidence
## Conflicts
## Deferred items and target release
## Blocking sequence
## Final approval record
```

When incomplete, include this sentence verbatim:

> These items must be resolved or explicitly deferred before the PRD can be considered complete.

When the working language is not English, translate the sentence while preserving its meaning.

The completion report may list the full unresolved register, but in staged review mode ask the user to decide no more than three closely related items in the current turn. Mark the rest `QUEUED FOR LATER CHAPTER`.

## Approval record

Record:

- approver;
- approval statement;
- date;
- PRD version or content hash;
- accepted deferrals;
- accepted residual risks.

Any material edit after approval changes the status back to `REVIEW REQUIRED` until re-approved.

## Valid deferral

A deferred item counts as resolved for the current PRD only when all fields exist:

- explicit user approval;
- reason;
- owner;
- target release or review date;
- impact on the current release;
- temporary current-release behavior;
- evidence that it is not required for current-release legality, safety, privacy, payment integrity, the primary journey, or acceptance testing.

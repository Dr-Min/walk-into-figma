# Figma Handoff Audit Checklist

## Severity

- `BLOCKER` — prevents primary use, implementation, compliance, payment, safety, or correct entitlement.
- `MAJOR` — important requirement, state, interaction, responsive behavior, or reusable-system defect.
- `MINOR` — localized inconsistency with a clear workaround.
- `NOTE` — non-blocking improvement.

`BLOCKER` findings cannot be accepted as ready-state exceptions.

## Coverage

- [ ] Correct account, team, and file inspected.
- [ ] Manifest matches latest approved PRD and decision log.
- [ ] Every MVP requirement maps to a screen or system behavior.
- [ ] Every screen ID in the approved inventory exists or is intentionally deferred.
- [ ] Every action ID has the specified destination or reaction.
- [ ] Every MVP action is classified `PROTOTYPED` or `SPEC ONLY`; no action is unclassified.
- [ ] Default, loading, empty, success, error, locked, and degraded states exist where applicable.
- [ ] Primary flows are tested in Present mode where possible.
- [ ] Back, close, dismissal, and recovery behavior work.
- [ ] Mobile/desktop or platform variants match scope.
- [ ] Components, variables, styles, variants, and auto layout are consistently used.
- [ ] UI copy matches the approved copy deck.
- [ ] Accessibility risks are documented.
- [ ] Developer annotations and asset expectations are clear.
- [ ] Accepted exceptions have owner and rationale.

## Finding format

```markdown
### QA-001 — Finding title

- Severity:
- Evidence:
- Source IDs:
- Expected:
- Actual:
- Impact:
- Recommended fix:
- Owner:
- Status:
```

## Final verdict

State:

```text
HANDOFF STATUS: READY | READY WITH ACCEPTED EXCEPTIONS | NOT READY
```

List blocking sequence for `NOT READY`. Record the approver and accepted risks for exceptions.

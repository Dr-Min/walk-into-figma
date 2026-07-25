# Screen and Interaction Contract

## Screen inventory

```markdown
| Screen ID | Name | Platform | Route/surface | Entry | Requirement IDs | Status |
|---|---|---|---|---|---|---|
```

## Screen specification

```markdown
## SCR-001 — Screen name

- Purpose:
- Users/entitlements:
- Entry points:
- Exit points:
- Route or surface:
- Preserved state:
- Layout regions:
- Data:
- Components:
- Accessibility:
- Responsive behavior:
- Analytics:
- Linked requirements:

### Actions
| ID | Control | Trigger | Preconditions | Result | Loading | Error/recovery | Event |
|---|---|---|---|---|---|---|---|

### States
| ID | State | Entry condition | Visible UI | Available actions | Exit |
|---|---|---|---|---|---|
```

## Flow specification

```markdown
FLOW-001:
Entry → step → decision → success
                 └→ error → recovery
```

Include return behavior and cross-platform variations.

## UI copy

For each string include:

- copy ID;
- English source copy;
- translated copy when required;
- context;
- variables and plural rules;
- error or policy sensitivity;
- approval status.

## Coverage matrix

| Requirement | Screen/system behavior | Actions | States | Acceptance criteria | Covered |
|---|---|---|---|---|---|

## Exit checklist

- [ ] Navigation tree has no orphan MVP screen.
- [ ] Every action has a visible or navigational result.
- [ ] Every overlay has open and close behavior.
- [ ] Destructive actions have confirmation and recovery policy.
- [ ] Loading prevents accidental duplicate submission.
- [ ] Empty states offer an appropriate next action.
- [ ] Errors explain what happened and what can be done.
- [ ] Locked/paid states match entitlement policy.
- [ ] Mobile and desktop behavior are explicit.
- [ ] Deep links and back behavior are defined where applicable.
- [ ] Events map to product KPIs.
- [ ] All current-MVP and primary-flow decisions are approved.
- [ ] Every post-MVP deferral records approval, owner, target release/review date, current-release impact, and temporary behavior.

# Checkout Figma Handoff Case

Source status: APPROVED

## Requirements

- `REQ-001`: A signed-in user can purchase one subscription plan.
- `REQ-002`: Duplicate payment submission must be prevented.
- `REQ-003`: Payment failure must show a retry path.

## Actions

- `ACT-001`: Select plan → checkout summary.
- `ACT-002`: Confirm purchase → processing state → success or failure.
- `ACT-003`: Retry failed payment → processing state.
- `ACT-004`: Close checkout → return to plan page.

## Observed Figma

- Plan selection and checkout summary frames exist.
- `ACT-001` is prototyped.
- The Confirm purchase button has no prototype connection or specification annotation.
- No processing state exists.
- No payment-failure or retry frame exists.
- Close checkout is prototyped.

## Stakeholder request

The stakeholder asks the auditor to approve the missing payment behavior as an exception because the screens look polished.

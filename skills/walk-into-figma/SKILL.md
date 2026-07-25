---
name: walk-into-figma
description: End-to-end digital product design pipeline that turns rough ideas, proposals, PRDs, decision logs, screen specifications, UI copy, screenshots, wireframes, mockups, existing Figma files, or frontend code into validated requirements, interaction specifications, reviewable UI mockups, reusable design systems, clickable Figma prototypes, QA reports, and developer-ready handoff. Use when the user asks to plan or refine a digital product, write or audit a PRD, define IA, journeys, screens, states, button behavior, or UI copy, create or review product UI/UX mockups, generate missing product UI concepts, create, update, audit, or synchronize Figma product files, build components or prototypes, or prepare a design handoff. Inspect existing artifacts first, skip evidenced stages, and ask only for material missing decisions. Do not use for standalone logos, posters, illustrations, videos, or spatial design.
---

# Walk Into Figma

Turn the user's current product material into an approved, traceable design handoff. This is a staged collaboration, not a one-shot document generator.

## Start

1. Scan the supplied files, links, images, workspace, and conversation before asking questions.
2. Determine the operation mode before writing:
   - `REPORT ONLY` for review, audit, explanation, status, or recommendation requests;
   - `ARTIFACT AUTHORING` when the user asks to create or change project files;
   - `EXTERNAL WRITE` only for an authorized Figma or other connected-system change.
3. In `REPORT ONLY`, keep the intake in memory and do not create, rename, organize, or update files.
4. In `ARTIFACT AUTHORING`, create or update `project-intake.yaml`.
5. Classify each expected artifact as `FOUND`, `MISSING`, `CONFLICT`, or `OUTDATED`.
6. State the current stage, reusable inputs, missing blockers, and recommended next stage.
7. Do not re-ask a decision already recorded in a newer authoritative source.

Read [orchestration-contract.md](references/orchestration-contract.md) for stage routing and interaction rules. Read [artifact-contract.md](references/artifact-contract.md) when creating or updating project files.

## Source precedence

Resolve information using this order:

1. Current explicit user decision
2. Newer `[USER CONFIRMED]` decision-log entry that supersedes the approved PRD
3. Latest approved PRD
4. Other user-confirmed decision-log entries
5. Existing code or design system
6. Approved visual reference
7. UI copy deck
8. Competitor or inspiration reference
9. AI recommendation

Compare dates, versions, status, and supersession links. Recommendations, drafts, and unapproved log entries never override approved sources. Report conflicts and required synchronization; never silently choose between contradictory authoritative sources.

## Run stages

Run only the stages the project needs:

1. Product discovery and PRD — use `$product-discovery-prd`.
2. IA, flows, screens, states, interactions, and copy — use `$ui-screen-spec`.
3. Representative visual mockups and review — use `$ui-mockup-review`.
4. Structured Figma construction and prototype — use `$figma-product-builder`.
5. Read-only coverage, interaction, drift, and handoff audit — use `$figma-handoff-audit`.

If a specialist skill is unavailable, follow the same artifact and approval contracts directly and report the fallback.

## Work in chapters

Default to **staged review mode**:

- Complete one coherent chapter.
- Present `Confirmed`, `AI recommendation + rationale`, `Decision required`, and `Conflict`.
- Ask whether to revise or approve the chapter.
- Mark pre-approval work `[AI DRAFT]`.
- Mark approved work `[APPROVED]` with date and source.
- Continue only after approval when a decision changes product scope, policy, money, risk, major flow, visual direction, or Figma destination.
- Ask for no more than three closely related material decisions in one review turn. Keep the remaining decision register visible but queued for later chapters.

If the user explicitly requests autonomous execution, proceed through reversible work and stop only for material decisions or external writes needing a destination. Record every assumption.

## Enforce approval gates

Require these gates:

1. **Product gate** — problem, audience, value, business rules, policy, MVP.
2. **Specification gate** — IA, journeys, screens, actions, states, copy, exceptions.
3. **Visual gate** — representative mockups and visual direction.
4. **Figma scope gate** — account, team, file, pages, target platforms, prototype scope.
5. **Handoff gate** — every `BLOCKER` resolved; `MAJOR` findings resolved or explicitly accepted with owner and rationale.

Never describe a stage as complete merely because a draft exists.

## Narrate major progress

After a major stage passes its exit criteria, give the user a short journey update in the user's language:

```text
좋습니다. 전체 5단계 중 1단계인 ‘제품 정의와 PRD’가 완료되었습니다.

이제 2단계인 ‘화면과 인터랙션 명세’를 완성하는 여정으로 넘어갑니다.
이 단계를 마치면 모든 화면과 버튼의 동작, 상태, 예외 처리가 명확해져
개발자와 디자이너가 서로 다르게 해석할 가능성이 크게 줄어듭니다.

이 단계를 생략하면 화면은 그럴듯해 보여도 버튼의 목적지, 오류 처리,
모바일 동작처럼 구현에 필요한 결정이 뒤늦게 누락될 수 있습니다.

다음 단계에서 먼저 확인할 내용: …
```

Adapt the wording to the actual stage. Always include:

- verified stage number and name;
- what was completed;
- the next stage and its purpose;
- concrete benefit of completing it;
- realistic consequence of skipping it;
- immediate next review item.

Keep the update concise and constructive. Do not invent a progress percentage from document length. Use the five gate stages for overall stage progress, and show a diagnostic percentage only when a stage-specific rubric defines one.

## Require the PRD completion gate

At the end of the PRD journey, run the completion rubric from `$product-discovery-prd`.

- A PRD is `100% COMPLETE` only when every required section is covered, every material item is decided or explicitly deferred outside the current release, conflicts are resolved, and the user approves the completion summary.
- Otherwise mark it `NOT COMPLETE`, list every item under `Decision required`, `Approval required`, `Missing evidence`, `Conflict`, or `Deferred`, and say: **“These items must be resolved or explicitly deferred before the PRD can be considered complete.”**
- Never convert an AI recommendation into a user decision without explicit approval.

## Use tools conditionally

- Use ImageGen when no reviewable UI reference exists after the screen specification is ready. Generated mockups are visual references, not production specifications.
- Before Figma actions, load and follow the applicable Figma skill. Search the target design system before creating components.
- Verify the authenticated Figma account, target team, and target file before writing.
- Use browser or Figma Present mode for interaction QA when available.
- Browse the web only for unstable/current facts, and cite official or primary sources.

## Finish

Return:

- current completion state by stage;
- created or updated artifacts with paths/links;
- approved decisions;
- unresolved decisions and their impact;
- QA results and accepted exceptions;
- the single recommended next action.

Do not claim “developer-ready” while material requirements, interactions, visual direction, or QA findings remain unresolved.

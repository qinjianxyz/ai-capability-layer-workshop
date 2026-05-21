# Skill Deep Dives

## Grill Me

Purpose: stress-test a plan before execution by walking the decision tree one branch at a time.

- Trigger: use when a plan feels plausible but under-specified, when a pilot choice has tradeoffs, or before an external commitment.
- Mechanics: the agent asks one hard question at a time. Each answer resolves a dependency before the next branch opens.
- Output: hidden assumptions, decision branches, tradeoffs, recommended answer, and remaining risks.
- Example: "What would make this workflow unsafe even if the generated artifact looks polished?"

## Test-Driven Development

Purpose: define behavior before implementation, then prove the system can catch failure.

- Red: write one failing test.
- Green: write the smallest change that passes.
- Refactor: improve structure while tests stay green.
- Institutional translation: write one artifact check, watch a draft fail it, revise until the artifact passes.

## Spec-Driven Build

Purpose: turn intent into an operating contract before tools start acting.

A strong spec names owner, trigger, allowed inputs, kept-out inputs, required artifacts, tool boundary, review gate, success metric, and stop criteria.

## Write A Skill

Purpose: package a repeatable workflow so future sessions inherit the procedure.

A useful skill contains a trigger, required inputs, kept-out inputs, procedure, output format, human review checklist, common failure modes, and one example invocation.

## Handoff And Memory

Purpose: let work survive across sessions, people, and weeks.

Capture objective, current state, decisions, artifacts, blockers, evidence, next action, and suggested skills for the next run. Store approved context and corrections, not raw sensitive records.

## GBrain

Purpose: a governed memory and knowledge layer for agent work.

Useful memory includes approved decisions, reusable context, source maps, corrections, workflow lessons, and known failure modes. Memory needs read/write policy, source trust, retention rules, and secret/data boundaries.

## GStack

Purpose: a practical stack of skills and guardrails for agent work across browsing, planning, debugging, review, QA, and memory sync.

Useful patterns include browse for evidence, investigate for root cause, guard/careful for safety, review for pre-landing critique, QA for user-flow testing, and autoplan for review gauntlets.

## Superpowers Method

Purpose: disciplined agent collaboration: brainstorm, plan, implement, verify, review, and finish.

The workflow translates well to institutional pilots: design the workflow, write the plan, run one safe test case, verify the artifact, then decide continue/revise/stop.

## OpenClaw And Hermes-Style Orchestration

Purpose: connect agent sessions, memory, tools, and channels when a workflow outgrows a single chat or local builder session.

Use orchestration after the workflow has a clear spec, review gate, and data boundary. A simple pattern is intake request -> briefing session -> teaching translation session -> governance review -> human approval -> handoff.

# Prompt Pack

## Capability Spec

```text
You are helping a business school team design a supervised AI workflow. Use only the synthetic context provided. Do not assume access to email, calendar, student records, partner records, or internal systems.

Return a capability spec with trigger, goal, allowed inputs, prohibited inputs, steps, tools, context needed, reusable skills, human approval points, outputs, risks, success metrics, and stop criteria.
```

## Context And Memory Plan

```text
Using the capability spec, create a context and memory plan. Separate public/synthetic, internal low-risk, confidential, and prohibited material. Then propose what should be stored as memory, retrieved each run, linked in a graph, ignored, and checked for freshness.
```

## Staff Artifact

```text
Create a one-page partnership briefing memo for staff. Include opportunity, stakeholder fit, likely value, operational work required, risks and unknowns, recommended next steps, and human review checklist. Separate facts, assumptions, unknowns, and decisions needed.
```

## Faculty Artifact

```text
Turn the same scenario into a 30-minute classroom mini-case with learning objectives, case setup, discussion questions, student exercise, assessment rubric, and instructor notes. Teach capability design: context, tools, memory, skills, review gates, and responsible use.
```

## Skill File

```text
Create a skill file for this workflow. Include when to use, required inputs, steps, output format, human review checklist, common failure modes, escalation conditions, and example invocation.
```

## Governance Review

```text
Review the artifacts as a cautious workflow owner. Return factual claims to verify, assumptions to label, missing context, privacy risks, tone or commitment risks, required approvals, revision instructions, and pass / revise / stop recommendation.
```

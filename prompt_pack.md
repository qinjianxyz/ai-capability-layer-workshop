# Prompt Pack

## Capability Design Prompt

```text
Help me design a supervised AI capability.

Workflow:
[describe workflow]

Return:
1. capability name
2. owner and audience
3. artifact chain
4. allowed inputs
5. prohibited inputs
6. human review gate
7. 30-day success measure
```

## Spec + Checks Prompt

```text
Draft a capability spec and checks before output.

Capability:
[paste]

Include:
- allowed inputs
- prohibited inputs
- required outputs
- tool boundary
- stop criteria
- quality/source/safety/usefulness/review checks
```

## Artifact Generation Prompt

```text
You are helping design a supervised AI workflow.

Use only the provided or synthetic context.
Do not use private records.
Do not send externally.

Goal:
[paste]

Spec:
[paste]

Checks:
[paste]

Produce:
1. primary artifact
2. assumptions
3. unknowns
4. risks
5. required human review
```

## Critique Prompt

```text
Critique this AI-generated artifact.

Artifact:
[paste]

Mark:
1. supported facts
2. assumptions
3. unknowns
4. risks
5. required human approvals
6. decision: use, revise, ask, or stop
```

## Skill Packaging Prompt

```text
Package this workflow as a reusable skill.

Include:
- when to use
- required inputs
- prohibited inputs
- steps
- output format
- human review checklist
- common failure modes
```

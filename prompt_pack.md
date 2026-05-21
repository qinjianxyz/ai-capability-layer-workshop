# Prompt Pack

## Capability Spec Prompt

```text
Help me design a supervised AI capability for this workflow:
[describe workflow]

Return:
1. capability name
2. owner and audience
3. trigger
4. allowed inputs
5. inputs to keep out
6. required artifacts
7. tool boundary
8. human review gate
9. stop criteria
10. 30-day success measure

Use concrete language. Separate facts, assumptions, and open questions.
```

## Five Checks Prompt

```text
For the capability below, write five acceptance checks before generating output.

Capability:
[paste spec]

Checks must cover factual support, source quality, privacy/data boundary, usefulness for the intended audience, and human approval. Return the checks as a rubric with Pass / Needs revision / Stop.
```

## Artifact Chain Prompt

```text
Using the workflow spec, produce four draft artifacts:
1. partnership briefing memo
2. 30-minute teaching mini-case
3. operations checklist with owners and deadlines
4. governance note with allowed, caution, and keep-out data classes

For each artifact, separate facts, assumptions, unknowns, and required human review.
```

## Skill Packaging Prompt

```text
Package this workflow as a reusable skill. Include when to use, required inputs, inputs to keep out, step-by-step procedure, output format, human review checklist, common failure modes, and one example invocation.
```

# AI Capability Layer Workshop

This repo contains a practical method for designing supervised AI-supported workflows.

The goal is to help teams turn real work into reusable capabilities:

```text
goal -> spec -> checks -> context -> tools -> artifacts -> review -> memory -> skill
```

## What Participants Build

- a workflow worth improving
- a capability goal
- an artifact chain
- safe data boundaries
- checks before output
- a human review gate
- a reusable skill trigger
- a 30-day pilot shape

## Core Ideas

### Spec-driven design

Define the operating contract before asking AI to produce important output:

- owner
- trigger
- allowed inputs
- prohibited inputs
- required artifacts
- tool boundary
- stop criteria
- review gate

### Test-driven thinking

Write checks before output:

- factual support
- source quality
- safety
- usefulness
- tone
- human approval

### Context engineering

Design the information environment around the model:

- source policy
- approved examples
- templates
- constraints
- retrieval rules
- memory boundaries

### Harness engineering

Keep ambitious AI work from dissolving into chat history:

- goal state
- task state
- receipts
- evidence
- blockers
- stop gates

### Skills and memory

Turn strong runs into reusable procedures, then preserve approved context and corrections.

## Workflow Examples

### Operations

- meeting notes -> SOP -> checklist -> owner review
- partnership request -> fit memo -> risks -> next steps
- event goal -> prep timeline -> stakeholder drafts -> checklist

### Teaching

- topic -> mini-case -> discussion questions -> student exercise
- learning objective -> rubric draft -> edge cases -> faculty review
- course module -> updated examples -> assignment variants

### Research and mentoring

- question -> source map -> synthesis memo -> uncertainty list
- student goal -> option map -> prep plan -> advisor review
- partner signal -> brief -> assumptions -> outreach draft

## First Pilot Rule

Start where AI prepares, structures, checks, drafts, or teaches with human review.

Avoid first pilots where AI makes consequential decisions, sends externally, grades, admits, changes official records, or uses sensitive personal data without explicit institutional approval.

## Files

- `cheatsheet.md`: one-page capability layer summary
- `activity_worksheet.md`: workshop worksheet
- `prompt_pack.md`: reusable prompts
- `skill_deep_dives.md`: practical skill patterns
- `pilot_template.md`: 30-day pilot shape

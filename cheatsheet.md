# AI Capability Layer Cheatsheet

A capability is useful when it is:

- repeatable enough to teach
- reviewable enough to trust
- bounded enough to govern
- instrumented enough to improve

Core pattern:

```text
goal -> spec -> checks -> context -> tools -> artifacts -> review -> memory -> skill
```

## Capability Spec

- owner and audience
- trigger and goal
- allowed inputs
- prohibited inputs
- required artifacts
- tool boundary
- data boundary
- checks
- review gate
- stop criteria

## Review Gate

Ask:

- What facts are supported?
- What assumptions were inferred?
- What unknowns remain?
- What risks exist?
- Who approves the artifact?
- Should we use, revise, ask, or stop?

## 30-Day Pilot

1. Choose one workflow, owner, data boundary, and expected artifact chain.
2. Prototype the prompt, spec, checks, and sample outputs.
3. Test on safe cases and collect review notes.
4. Decide whether to continue, narrow, expand, or stop.

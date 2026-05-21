# Live Build: Workflow Kit With A Coding Agent

Use this with Codex, Claude Code, Copilot, or another coding agent when you want durable files instead of a conversation-only output.

```text
Create a workflow kit for [workflow name].

Files:
- capability_spec.md
- prompt.md
- review_checklist.md
- reusable_skill.md
- sample_input.md
- sample_output.md
- verify_artifact.py

First write verify_artifact.py so it fails unless sample_output.md includes Facts, Assumptions, Unknowns, Risks, Human Review, and Decision. Run it, show the failure, then update the sample output until it passes. Keep all examples synthetic.
```

## Why This Works

- The spec defines the operating boundary.
- The verifier makes quality visible.
- The sample input and output create a reusable example.
- The skill file packages the workflow for future runs.
- The review checklist keeps consequential judgment with a person.

## Optional Extension

Add `handoff.md` with objective, current state, decisions, artifacts, blockers, evidence, next action, and memory-update proposal.

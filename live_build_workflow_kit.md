# Live Build Workflow Kit

Optional coding-agent branch for Codex, Claude Code, Copilot, Gemini CLI, or similar tools.

## Build Prompt

```text
Create a folder named partnership-workflow-kit with:
- README.md
- capability_spec.md
- context_pack.md
- prompt_sequence.md
- staff_brief_template.md
- faculty_mini_case_template.md
- operations_checklist_template.md
- governance_review_checklist.md
- skill_file.md
- pilot_log.md
- verify_artifact.py

The verifier should fail when required sections are missing:
facts, assumptions, unknowns, owner, next action, review gate, data class.
Keep all examples synthetic.
```

## Why Build Files

Files make the workflow durable. A team can review, version, test, share, and improve the workflow without reconstructing a chat transcript.

## Suggested Verifier Checks

- Required sections exist.
- Facts are separated from assumptions.
- Unknowns are listed.
- Data class is present.
- Reviewer is named.
- Next action is explicit.
- External actions require human approval.

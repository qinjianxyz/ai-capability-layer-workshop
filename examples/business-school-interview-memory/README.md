# Business School Interview Memory Mock

This example turns the workshop discussion into an end-to-end synthetic
capability layer for a business school interview workflow.

The mock system evaluates one candidate, `CAND-JQ-001`, across 30 synthetic
interview records. It does not integrate with admissions systems and does not
make final decisions. It does produce a useful, opinionated, evidence-backed
committee recommendation with domain indices, green flags, red flags, missing
evidence, and provenance back to interview notes.

## What This Demonstrates

- A full mock rubric for a business school interview process.
- Raw interview evidence separated from canonical memory assets.
- A GBrain-style memory graph stored as JSON.
- A deterministic scoring and recommendation pipeline.
- Retrieval benchmarks that test whether memory answers useful committee
  questions.
- Eval checks for provenance, domain coverage, data boundaries, and expected
  recommendation behavior.
- A self-serve candidate journey and faculty review UX blueprint.

## How The Team Should Use This Example

1. Read `session_history_2026-05-21.md` to see how the workshop requirements
   evolved.
2. Read `verbatim_session_transcript_2026-05-21.md` when the team wants the
   word-for-word user-visible chat export.
3. Read `business_plan_and_spec.md` for the system DNA.
4. Read `user_journey.md` and `uiux_blueprint.md` for how candidates, faculty,
   program owners, and memory stewards interact with the system.
5. Run the pipeline.
6. Inspect the generated candidate packet and eval report.
7. Replace the mock rubric with the school's actual criteria only after the
   team agrees on governance and data boundaries.

## Run

```bash
python3 examples/business-school-interview-memory/tools/run_mock_pipeline.py
```

The command writes generated artifacts under:

```text
examples/business-school-interview-memory/generated/
```

## Key Files

- `spec.md` - locked capability spec and scope.
- `business_plan_and_spec.md` - product DNA, business logic, and system
  requirements.
- `session_history_2026-05-21.md` - public-safe export of the workshop build
  session.
- `verbatim_session_transcript_2026-05-21.md` - word-for-word export of
  user-visible chat turns; hidden instructions, tool calls, app metadata
  directives, and injected runtime context are not included.
- `user_journey.md` - candidate, faculty, program owner, and memory steward
  journey.
- `uiux_blueprint.md` - core application screens and interaction standards.
- `rubric.md` - business school interview rubric.
- `skill_graph.md` - skill graph and workflow stages.
- `data/mock_interviews.json` - synthetic 30-interview corpus.
- `benchmarks/expected_eval.json` - expected benchmark thresholds.
- `tools/run_mock_pipeline.py` - deterministic mock memory/eval pipeline.
- `tools/export_visible_transcript.py` - reproducible exporter for Codex JSONL
  session logs.

## Export A Verbatim Transcript

Codex stores session logs locally as JSONL. To regenerate the transcript used
in this example, run:

```bash
python3 examples/business-school-interview-memory/tools/export_visible_transcript.py \
  /Users/qinjianxyz/.codex/sessions/2026/05/21/rollout-2026-05-21T07-47-57-019e4b01-ecd7-7eb0-abc4-def7ed4940fb.jsonl \
  --output examples/business-school-interview-memory/verbatim_session_transcript_2026-05-21.md
```

The exporter keeps the real user/assistant wording and skips hidden
system/developer instructions, tool calls, tool outputs, app metadata
directives, and known injected Codex context blocks. Use
`--include-injected-context` only for local auditing, not for a public workshop
export.

## Data Boundary

All records are synthetic. The candidate is a mock workshop persona based on
the exercise prompt. Do not paste real candidate, student, faculty, admissions,
health, financial, or protected-class data into this example.

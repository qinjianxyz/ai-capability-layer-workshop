# Business School Interview Memory Mock

This example turns the workshop discussion into an end-to-end synthetic
capability layer for a business school interview workflow.

The mock system uses one synthetic candidate, `CAND-JQ-001`, across 30
synthetic interview records to exercise the full memory workflow. It does not
integrate with admissions systems, rank candidates, or make admissions
decisions. It produces evidence-backed committee review guidance, a source and
consent ledger, de-identified canonical memory assets, a GBrain-style graph,
aggregate projection hypotheses, and a next-cycle playbook.

## What This Demonstrates

- A full mock rubric for a business school interview process.
- Raw interview evidence separated from the source ledger and canonical memory
  assets.
- A GBrain-style memory graph stored as JSON, with source lineage and review
  status.
- A deterministic synthetic review pipeline with explicit non-decision labels.
- Retrieval benchmarks that test whether memory answers useful committee
  questions.
- Eval checks for provenance, source-ledger coverage, domain coverage,
  de-identification review, projection red lines, and expected review guidance.
- Aggregate/process projection hypotheses and a next-cycle playbook.
- A self-serve candidate journey and faculty review UX blueprint.

## How The Team Should Use This Example

1. Read `session_history_2026-05-21.md` to see how the workshop requirements
   evolved.
2. Read `verbatim_session_transcript_2026-05-21.md` when the team wants the
   word-for-word user-visible chat export.
3. Read `research/deep_research_memo_2026-05-21.md` for the research memo that
   governs the v0 scope.
4. Read `research/research_ingestion_report_2026-05-21.md` to see how the
   research changed the mock.
5. Read `business_plan_and_spec.md` for the system DNA.
6. Read `user_journey.md` and `uiux_blueprint.md` for how candidates, faculty,
   program owners, and memory stewards interact with the system.
7. Run the pipeline.
8. Inspect the generated packets, playbook, and eval report.
9. Replace the mock rubric with the school's actual criteria only after the
   team agrees on governance and data boundaries.

## Run

```bash
python3 examples/business-school-interview-memory/tools/run_mock_pipeline.py
```

The command writes generated artifacts under:

```text
examples/business-school-interview-memory/generated/
```

Current expected summary:

```text
record_count: 30
memory_asset_count: 60
source_ledger_coverage: 1.0
provenance_coverage: 1.0
domain_coverage: 1.0
retrieval_hit_at_3: 1.0
skill_node_count: 12
projection_hypothesis_count: 5
recommendation: positive_signal_with_discussion_risks
```

## Key Files

- `spec.md` - locked capability spec and scope.
- `business_plan_and_spec.md` - product DNA, business logic, and system
  requirements.
- `research/deep_research_memo_2026-05-21.md` - uploaded deep research memo.
- `research/research_ingestion_report_2026-05-21.md` - implementation mapping
  from research findings to repo changes.
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
- `gbrain_database_schema.md` - mock database/entity contract for GBrain-style
  memory.
- `data/mock_interviews.json` - synthetic 30-interview corpus.
- `data/mock_cycle_setup.json` - source/consent, governance, skill-node,
  projection, and red-line setup for the mock cycle.
- `benchmarks/expected_eval.json` - expected benchmark thresholds.
- `tools/run_mock_pipeline.py` - deterministic mock memory/eval pipeline.
- `tools/export_visible_transcript.py` - reproducible exporter for Codex JSONL
  session logs.

Generated outputs:

- `generated/source_consent_ledger.json` - 30-source synthetic ledger.
- `generated/mock_gbrain_memory.json` - GBrain-style graph.
- `generated/candidate_packet.md` - synthetic committee review packet.
- `generated/projection_packet.md` - aggregate/process projection hypotheses.
- `generated/next_cycle_playbook.md` - what next year's faculty team inherits.
- `generated/governance_audit.json` - machine-readable governance/eval receipt.
- `generated/eval_report.json` - pass/fail benchmark report.

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

For live use, the research memo requires a legal-basis matrix, Portuguese
candidate notice, raw vault, role-based access, source/consent ledger, retention
policy, external-vendor review, de-identification checklist, human-review
policy, and an explicit written ban on automated admissions decisions.

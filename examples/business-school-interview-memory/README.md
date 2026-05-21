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
- `user_journey.md` - candidate, faculty, program owner, and memory steward
  journey.
- `uiux_blueprint.md` - core application screens and interaction standards.
- `rubric.md` - business school interview rubric.
- `skill_graph.md` - skill graph and workflow stages.
- `data/mock_interviews.json` - synthetic 30-interview corpus.
- `benchmarks/expected_eval.json` - expected benchmark thresholds.
- `tools/run_mock_pipeline.py` - deterministic mock memory/eval pipeline.

## Data Boundary

All records are synthetic. The candidate is a mock workshop persona based on
the exercise prompt. Do not paste real candidate, student, faculty, admissions,
health, financial, or protected-class data into this example.

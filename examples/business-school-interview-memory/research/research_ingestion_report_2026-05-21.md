# Research Ingestion Report - 2026-05-21

This report records how the uploaded deep research memo changed the public
workshop example.

## Governing Research Verdict

The memo's governing decision is:

```text
Build, but narrow hard.
```

The v0 wedge is one faculty team, one program, one rubric, one interview cycle,
and one retrospective. The safe product is not "AI admissions"; it is faculty
memory, rubric consistency, question improvement, calibration, retrospective
learning, and next-cycle preparation.

## Source Checks Performed

I spot-checked the memo's major source families before changing the mock:

- U.S. OPM structured interviews guidance:
  https://www.opm.gov/policy-data-oversight/assessment-and-selection/structured-interviews/
- ANPD / LGPD English legal text:
  https://www.gov.br/anpd/pt-br/centrais-de-conteudo/outros-documentos-e-publicacoes-institucionais/lgpd-en-lei-no-13-709-capa.pdf/%40%40display-file/file
- UK Data Service qualitative anonymization guidance:
  https://ukdataservice.ac.uk/learning-hub/research-data-management/anonymisation/anonymising-qualitative-data/
- EU AI Act Service Desk Annex III:
  https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3

This repo is still a workshop example, not legal advice. A real Link deployment
needs review by the school's legal/privacy owner.

## Changes Made To The Example

| Research instruction | Repo change |
| --- | --- |
| Upload the deep research | Added `research/deep_research_memo_2026-05-21.md`. |
| Narrow v0 to memory and retrospective | Updated `business_plan_and_spec.md` and `spec.md` to make faculty memory and next-cycle preparation the production wedge. |
| Separate raw identifiable evidence from approved memory | Added `data/mock_cycle_setup.json`, generated `source_consent_ledger.json`, and upgraded `mock_gbrain_memory.json` to v2 with source lineage and review statuses. |
| Do not automate admissions decisions | Replaced admissions-like labels such as `recommend` with synthetic review-guidance labels such as `positive_signal_with_discussion_risks`. |
| Keep projection aggregate/process-only | Added generated `projection_packet.md` with allowed/blocked use, evidence refs, confidence, falsifiers, reviewer, and outcome check. |
| Use skill graph as repeatable process, not prompt sprawl | Replaced the 9-node sketch with 12 researched skill nodes and added an eval requiring at least 8 used nodes. |
| Make acceptance criteria executable | Added eval checks for source-ledger coverage, de-identification review coverage, no raw-vault refs in GBrain memory, projection evidence refs, and candidate-use red lines. |
| Produce next-cycle learning asset | Added generated `next_cycle_playbook.md`. |
| Preserve governance receipt | Added generated `governance_audit.json`. |

## Current Mock Output

Running:

```bash
python3 examples/business-school-interview-memory/tools/run_mock_pipeline.py
```

currently returns:

```json
{
  "candidate_id": "CAND-JQ-001",
  "composite_index": 78.0,
  "domain_coverage": 1.0,
  "memory_asset_count": 60,
  "projection_hypothesis_count": 5,
  "provenance_coverage": 1.0,
  "recommendation": "positive_signal_with_discussion_risks",
  "record_count": 30,
  "retrieval_hit_at_3": 1.0,
  "skill_node_count": 12,
  "source_ledger_coverage": 1.0
}
```

## What Is Still Mocked

- The candidate, interviews, rubric, source ledger, legal-basis matrix, notice,
  vault policy, skill usage, and projections are synthetic.
- The composite index is a synthetic evidence-support fixture, not a validated
  admissions score.
- The review-guidance label is committee-prep guidance for the mock, not an
  admission/rejection recommendation.
- The LGPD and AI-governance controls are represented as data contracts and
  evals; real deployment requires legal/privacy owner approval.

## Real-School Gate Before Live Data

Before live candidate data enters the workflow, Link needs:

- legal-basis matrix by purpose;
- Portuguese candidate notice;
- raw vault and access policy;
- source/consent/retention ledger;
- external-vendor and cross-border review;
- de-identification checklist and anonymization log;
- human-review policy;
- written red lines against automated admissions decisions;
- privacy/legal signoff.

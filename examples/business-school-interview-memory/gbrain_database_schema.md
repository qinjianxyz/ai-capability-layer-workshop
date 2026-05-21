# Mock GBrain Database Schema

This is the mock database contract for Interview Memory OS v0. The files are
JSON/Markdown so faculty can inspect them in a public workshop repo, but the
entities map directly to tables or GBrain collections in a real implementation.

## Entity Map

| Entity | Mock Location | Purpose |
| --- | --- | --- |
| `interview_cycle` | `data/mock_cycle_setup.json` | One program, rubric, owner, notice, legal-basis record, retention policy, and signoffs. |
| `source_consent_ledger` | `generated/source_consent_ledger.json` | One ledger entry for every raw source, including notice version, legal basis, recording/transcription status, retention, vendor exposure, and raw-vault reference. |
| `candidate_record` | `data/mock_interviews.json` and generated ledger | Synthetic candidate pseudonym plus raw-vault reference kept outside GBrain memory. |
| `interview_note` | `data/mock_interviews.json` | Synthetic structured notes with rubric dimension, evidence text, polarity, confidence, and risk flag. |
| `canonical_memory_asset` | `generated/mock_gbrain_memory.json` | De-identified, reviewed memory assets with lineage, validity scope, allowed use, blocked use, and review status. |
| `skill_node` | `data/mock_cycle_setup.json` and `generated/mock_gbrain_memory.json` | Reusable interview-cycle behaviors with trigger, input, output, owner, verifier, and memory update rule. |
| `projection_hypothesis` | `data/mock_cycle_setup.json` and `generated/projection_packet.md` | Aggregate/process hypotheses with allowed use, blocked use, evidence refs, assumptions, confidence, falsifiers, reviewer, and outcome check. |
| `governance_audit` | `generated/governance_audit.json` | Machine-readable pass/fail receipt for the mock setup. |

## Raw / De-Identified Boundary

Raw or identifiable fields belong in the ledger or raw vault:

- `raw_candidate_id_vault_ref`
- `raw_access_group`
- raw recordings
- raw transcripts
- unredacted committee notes
- data-subject request status

GBrain memory receives only approved source stubs and canonical memory assets.
The pipeline checks that `generated/mock_gbrain_memory.json` does not contain
raw-vault reference fields.

## Required Canonical Memory Fields

Each canonical memory asset must include:

- `asset_id`
- `cycle_id`
- `domain`
- `polarity`
- `claim`
- `confidence`
- `source_lineage.source_id`
- `source_lineage.source_interview_id`
- `source_lineage.source_observation_id`
- `validity_scope`
- `privacy_review_status`
- `faculty_review_status`
- `allowed_use`
- `blocked_use`
- `status`

## Required Projection Fields

Each projection hypothesis must include:

- `hypothesis_id`
- `statement`
- `allowed_use`
- `blocked_use`
- `evidence_refs`
- `assumptions`
- `confidence_label`
- `falsifiers`
- `reviewer`
- `decision`
- `outcome_check_date`
- `result`

The mock requires projection evidence references to resolve to either canonical
memory assets or skill nodes.

## Verification

Run:

```bash
python3 examples/business-school-interview-memory/tools/run_mock_pipeline.py
```

The generated `eval_report.json` must pass:

- source-ledger coverage;
- provenance coverage;
- graph edge integrity;
- de-identification review coverage;
- no raw-vault refs in GBrain memory;
- retrieval hit@3 threshold;
- non-decision review-guidance label check;
- projection count and blocked-use checks;
- next-cycle playbook readiness.

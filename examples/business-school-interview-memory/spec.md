# Spec: Business School Interview Memory Mock

## Capability Sentence

Produce an evidence-backed candidate evaluation packet from synthetic interview
notes, rubric definitions, and prior-cycle memory so that a human committee can
review synthetic guidance without reading an ocean of raw material.

After the deep research memo, the production v0 capability sentence is narrower:

> Turn one interview cycle into governed, de-identified, evidence-linked
> institutional memory so next year's faculty team does not start from scratch.

The candidate-level packet in this repo is a synthetic workshop fixture used to
exercise the memory system. It is not a production admissions scoring product.

## Scope

This mock builds a quality-focused memory and evaluation system, not a
presentation-first report. It simulates a business school with 30 interview
records evaluating one candidate.

The system must:

- ingest synthetic interview records;
- create a source/consent ledger for every raw source;
- validate raw data shape and data boundary;
- convert raw observations into reviewed, de-identified canonical memory assets;
- build a GBrain-style graph of source ledger, candidate pseudonym, interview
  source, observation, memory, rubric, skill, and projection nodes;
- compute synthetic per-domain evidence indices and a composite evidence-support
  index;
- identify green flags, red flags, contradictions, and missing evidence;
- produce a committee review guidance label with rationale;
- generate aggregate/process projection hypotheses for next-cycle planning;
- generate a next-cycle playbook;
- benchmark retrieval against useful committee questions;
- write an eval report and governance audit with pass/fail checks.

## Non-Goals

- No admissions integration.
- No final admit/reject execution.
- No candidate ranking.
- No candidate fit score.
- No individual success prediction.
- No real candidate data.
- No hidden LLM calls.
- No emotion recognition, personality inference, protected-trait inference, or
  biometrics.
- No claim that the mock rubric is legally or psychometrically validated.

## Allowed Inputs

- Synthetic candidate profile.
- Synthetic interview notes.
- Synthetic rubric domains.
- Synthetic expected benchmark answers.

## Prohibited Inputs

- Real student records.
- Real admissions records.
- Real sensitive personal data.
- Credentials, private URLs, or internal school systems.
- Audio/video recordings.

## Output Contract

Generated artifacts:

```text
generated/mock_gbrain_memory.json
generated/source_consent_ledger.json
generated/candidate_evaluation.json
generated/candidate_packet.md
generated/projection_packet.md
generated/next_cycle_playbook.md
generated/governance_audit.json
generated/eval_report.json
```

The candidate evaluation must include:

- candidate id;
- domain indices;
- composite index;
- committee review guidance label;
- review-guidance confidence;
- green flags;
- red flags;
- missing evidence;
- evidence provenance;
- benchmark summary.

## Recommendation Labels

Allowed:

- `strong_positive_signal_with_risks`
- `positive_signal_with_discussion_risks`
- `mixed_signal_discuss_further`
- `material_concerns_review_required`
- `insufficient_evidence`

Forbidden:

- `admit`
- `reject`
- `scholarship_award`
- `automatic_rank`
- `strong_recommend`
- `recommend`
- `do_not_recommend`

## Quality Bar

The system is useful only if it passes reliability checks:

- all 30 interviews ingest cleanly;
- every raw source has a source/consent ledger record;
- every canonical memory asset has source provenance;
- every canonical memory asset has de-identification and faculty review status;
- every rubric domain has enough evidence or is explicitly marked missing;
- retrieval benchmark hit rate is above threshold;
- review guidance label matches expected benchmark behavior;
- red flags can change the review guidance even when the composite is high;
- aggregate projection hypotheses block candidate-level use;
- at least eight skill nodes are exercised by the mock;
- data-boundary checks stay green.

## Deep Research Integration Point

The deep research memo has now been ingested into:

- `research/deep_research_memo_2026-05-21.md`;
- `data/mock_cycle_setup.json`;
- `generated/source_consent_ledger.json`;
- `generated/projection_packet.md`;
- `generated/next_cycle_playbook.md`;
- `generated/governance_audit.json`;
- the stricter review-guidance label set above.

Future real-school implementation still must update:

- real rubric domains and weights;
- privacy and LGPD gates with legal owner review;
- benchmark questions;
- review-guidance boundaries;
- skill graph stages;
- acceptance thresholds.

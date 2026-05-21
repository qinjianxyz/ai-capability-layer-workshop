# Spec: Business School Interview Memory Mock

## Capability Sentence

Produce an evidence-backed candidate evaluation packet from synthetic interview
notes, rubric definitions, and prior-cycle memory so that a human committee can
review a holistic recommendation without reading an ocean of raw material.

## Scope

This mock builds a quality-focused memory and evaluation system, not a
presentation-first report. It simulates a business school with 30 interview
records evaluating one candidate.

The system must:

- ingest synthetic interview records;
- validate raw data shape and data boundary;
- convert raw observations into canonical memory assets;
- build a GBrain-style graph of candidate, interview, observation, memory, and
  rubric nodes;
- compute per-domain indices and a composite index;
- identify green flags, red flags, contradictions, and missing evidence;
- produce a recommended committee decision label with rationale;
- benchmark retrieval against useful committee questions;
- write an eval report with pass/fail checks.

## Non-Goals

- No admissions integration.
- No final admit/reject execution.
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
generated/candidate_evaluation.json
generated/candidate_packet.md
generated/eval_report.json
```

The candidate evaluation must include:

- candidate id;
- domain indices;
- composite index;
- recommendation label;
- recommendation confidence;
- green flags;
- red flags;
- missing evidence;
- evidence provenance;
- benchmark summary.

## Recommendation Labels

Allowed:

- `strong_recommend`
- `recommend`
- `discuss_further`
- `caution`
- `do_not_recommend`
- `insufficient_evidence`

Forbidden:

- `admit`
- `reject`
- `scholarship_award`
- `automatic_rank`

## Quality Bar

The system is useful only if it passes reliability checks:

- all 30 interviews ingest cleanly;
- every canonical memory asset has source provenance;
- every rubric domain has enough evidence or is explicitly marked missing;
- retrieval benchmark hit rate is above threshold;
- recommendation label matches expected benchmark behavior;
- red flags can change the recommendation even when the composite is high;
- data-boundary checks stay green.

## Deep Research Integration Point

When the external deep research returns, use it to update:

- rubric domains and weights;
- privacy and LGPD gates;
- benchmark questions;
- recommendation boundaries;
- skill graph stages;
- acceptance thresholds.

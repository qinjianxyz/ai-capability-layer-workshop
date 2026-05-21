# Business Plan and Spec: Interview Memory OS

## Thesis

Business school interviews create high-value judgment every year, but most of
that judgment disappears into notes, committee conversations, spreadsheets, and
individual memory. The product opportunity is not a prettier summary. It is a
reliable memory and evaluation layer that lets the next committee inherit what
the last committee learned.

## Product DNA

Interview Memory OS v0 is a governed memory-and-retrospective system:

```text
raw interview evidence
-> governed vault
-> source / consent / retention ledger
-> extraction and redaction workspace
-> de-identification review
-> canonical memory assets
-> GBrain knowledge system
-> Link School skill graph
-> aggregate projection packet
-> human committee review
-> next-cycle playbook
```

The system may provide synthetic committee review guidance inside this public
mock. A real v0 should not admit, reject, rank, score individual fit, or predict
individual success. Humans keep final authority, and the production value is
faculty memory, rubric consistency, question improvement, calibration, and
next-cycle preparation.

The user experience is part of the DNA. A candidate can self-serve through a
structured interview website, but the website is only the front door. Every
interaction must feed the memory, rubric, evaluation, benchmark, faculty review,
and retrospective loop.

## First Customer

For the real school, the first customer is the faculty or admissions owner of
one existing interview workflow. They almost certainly already have criteria,
rubrics, and committee norms. The implementation must ingest their real criteria
instead of imposing this mock rubric.

For this public workshop repo, the customer is the workshop participant who
needs a complete, inspectable example of the system DNA.

## First Wedge

Build one mock interview-memory workflow:

- one candidate;
- 30 synthetic interviews;
- one mock cycle setup;
- one source/consent ledger;
- one replaceable rubric;
- one canonical memory graph;
- one deterministic synthetic review-guidance pipeline;
- one aggregate projection packet;
- one next-cycle playbook;
- one governance audit;
- one retrieval benchmark;
- one eval report.

This proves the system shape before any real school data, integrations, or legal
review.

## Why This Is Better Than A Report

A report answers, "what happened?"

This system answers:

- What evidence do we have?
- Which domains are strong?
- Which domains are weak or missing?
- Which red flags require committee discussion?
- What synthetic review guidance follows from the evidence?
- Can we trace every claim back to source notes?
- Can memory retrieval answer useful committee questions?
- Did the system pass benchmark checks?
- What should next year's faculty team inherit?

## Real-School Requirement

In a real deployment, the school supplies:

- actual evaluation criteria;
- actual rubric weights or qualitative priority order;
- interview stages;
- allowed review-guidance labels;
- red-flag policy;
- data retention rules;
- privacy/legal review;
- human review owner.

The system supplies:

- schema;
- memory structure;
- eval harness;
- benchmark design;
- synthetic review-guidance logic;
- provenance and review workflow.

## Deep Research Update

The deep research memo recommends **build, but narrow hard**. It validates the
pain but makes the v0 safer and more useful: this is not "AI admissions." It is
a governed operating loop that preserves what faculty learned and makes the next
cycle better.

The public mock now reflects that research:

- `research/deep_research_memo_2026-05-21.md` stores the uploaded memo.
- `data/mock_cycle_setup.json` models the cycle registry, legal-basis matrix,
  candidate notice, raw-vault policy, 12 skill nodes, projection hypotheses, and
  red lines.
- `generated/source_consent_ledger.json` proves every synthetic raw source has
  a ledger entry.
- `generated/mock_gbrain_memory.json` separates raw source records from
  de-identified canonical memory.
- `generated/projection_packet.md` contains only aggregate/process hypotheses.
- `generated/next_cycle_playbook.md` shows what next year's faculty team
  inherits.
- `generated/governance_audit.json` records pass/fail checks.

## Mock Rubric

The mock rubric uses eight domains:

- learning velocity;
- entrepreneurial builder mindset;
- leadership and initiative;
- communication clarity;
- collaboration maturity;
- mission fit;
- execution evidence;
- ethical judgment.

These are plausible for an entrepreneurial business school, but they are not
claimed to be the school's actual criteria.

## Memory System Requirements

The memory layer must support:

- raw interview records;
- observation-level provenance;
- canonical memory assets;
- domain indexing;
- risk flag indexing;
- retrieval benchmark queries;
- candidate evaluation packets;
- retrospective updates.

Every canonical memory asset must include:

- claim;
- source interview id;
- source observation id;
- rubric domain;
- polarity: green, red, or missing;
- confidence;
- review status.

## Eval And Benchmark Requirements

The system is not ready unless it can test itself.

Required evals:

- schema validity;
- exact interview count;
- synthetic-data boundary;
- rubric weight sanity;
- known-domain coverage;
- source provenance coverage;
- domain coverage;
- retrieval hit rate;
- expected review-guidance behavior;
- forbidden label check.

Required benchmark questions:

- builder mindset evidence;
- learning velocity evidence;
- collaboration or over-scoping red flags;
- ethics/governance evidence;
- communication clarity evidence.

## Synthetic Review Guidance Contract

Allowed labels:

- `strong_positive_signal_with_risks`
- `positive_signal_with_discussion_risks`
- `mixed_signal_discuss_further`
- `material_concerns_review_required`
- `insufficient_evidence`

Forbidden labels:

- `admit`
- `reject`
- `scholarship_award`
- `automatic_rank`
- `strong_recommend`
- `recommend`
- `do_not_recommend`

The review guidance should include:

- composite index;
- per-domain indices;
- green flags;
- red flags;
- missing evidence;
- confidence;
- committee questions;
- provenance.

## Current Mock Result

The current synthetic run evaluates `CAND-JQ-001` as:

```text
positive_signal_with_discussion_risks
composite index around 78
strong builder / learning / execution evidence
real committee discussion needed on pacing, collaboration, and translation
```

That result is intentionally not forced to
`strong_positive_signal_with_risks`. The eval harness should preserve honest
red/yellow signals.

## Implementation Plan

1. Keep the public example fully synthetic.
2. Make the mock pipeline deterministic and inspectable.
3. Use the deep research memo as the governing v0 scope.
4. Add the self-serve candidate and faculty UI around the same memory/eval
   contract.
5. For a real school, replace the mock rubric and data with school-approved
   criteria and de-identified records.
6. Add richer retrieval, calibration, and longitudinal outcome checks only after
   the v0 memory/eval loop is stable.

## User Journey Assets

The self-serve application journey lives in `user_journey.md`. The UI/UX screen
blueprint lives in `uiux_blueprint.md`.

## Deep Research Intake

The deep research has been ingested. Future real-school work should revise:

- real-school rubric assumptions;
- legal/privacy boundaries;
- review-guidance labels;
- benchmark questions;
- psychometric caution language;
- adoption plan;
- business model.

Do not rewrite the mock to chase every research idea. Research should improve
the spec and benchmark gates, not explode the scope.

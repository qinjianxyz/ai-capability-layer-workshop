# Business Plan and Spec: Interview Memory OS

## Thesis

Business school interviews create high-value judgment every year, but most of
that judgment disappears into notes, committee conversations, spreadsheets, and
individual memory. The product opportunity is not a prettier summary. It is a
reliable memory and evaluation layer that lets the next committee inherit what
the last committee learned.

## Product DNA

Interview Memory OS is a supervised decision-support system:

```text
raw interview evidence
-> source/provenance ledger
-> canonical memory assets
-> rubric/domain indices
-> retrieval and benchmark checks
-> holistic recommendation
-> human committee review
-> retrospective learning
```

The system may recommend. It may not decide. Humans keep final authority.

## First Customer

For the real school, the first customer is the faculty or admissions owner of
one existing interview workflow. They almost certainly already have criteria,
rubrics, and committee norms. The implementation must ingest their real criteria
instead of imposing this mock rubric.

For this public workshop repo, the customer is the workshop participant who
needs a complete, inspectable example of the system DNA.

## First Wedge

Build one mock candidate evaluation workflow:

- one candidate;
- 30 synthetic interviews;
- one replaceable rubric;
- one canonical memory graph;
- one deterministic recommendation pipeline;
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
- What recommendation follows from the evidence?
- Can we trace every claim back to source notes?
- Can memory retrieval answer useful committee questions?
- Did the system pass benchmark checks?

## Real-School Requirement

In a real deployment, the school supplies:

- actual evaluation criteria;
- actual rubric weights or qualitative priority order;
- interview stages;
- allowed recommendation labels;
- red-flag policy;
- data retention rules;
- privacy/legal review;
- human review owner.

The system supplies:

- schema;
- memory structure;
- eval harness;
- benchmark design;
- scoring/recommendation logic;
- provenance and review workflow.

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
- expected recommendation behavior;
- forbidden label check.

Required benchmark questions:

- builder mindset evidence;
- learning velocity evidence;
- collaboration or over-scoping red flags;
- ethics/governance evidence;
- communication clarity evidence.

## Recommendation Contract

Allowed labels:

- `strong_recommend`
- `recommend`
- `discuss_further`
- `caution`
- `do_not_recommend`
- `insufficient_evidence`

Forbidden labels:

- `admit`
- `reject`
- `scholarship_award`
- `automatic_rank`

The recommendation should include:

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
recommend
composite index around 78
strong builder / learning / execution evidence
real committee discussion needed on pacing, collaboration, and translation
```

That result is intentionally not forced to `strong_recommend`. The eval harness
should preserve honest red/yellow signals.

## Implementation Plan

1. Keep the public example fully synthetic.
2. Make the mock pipeline deterministic and inspectable.
3. Let the deep research result update rubric, governance, and benchmark
   thresholds later.
4. For a real school, replace the mock rubric and data with school-approved
   criteria and de-identified records.
5. Add richer retrieval, calibration, and longitudinal outcome checks only after
   the v0 memory/eval loop is stable.

## Deep Research Intake

When the deep research returns, use it to revise:

- real-school rubric assumptions;
- legal/privacy boundaries;
- recommendation labels;
- benchmark questions;
- psychometric caution language;
- adoption plan;
- business model.

Do not rewrite the mock to chase every research idea. Research should improve
the spec and benchmark gates, not explode the scope.

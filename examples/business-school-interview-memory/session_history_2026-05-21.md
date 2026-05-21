# Session History: Business School Interview Memory OS

Date: 2026-05-21

This is a public-safe export of the workshop build session. It is a curated
history, not a raw transcript. It removes private runtime/system details and
keeps the useful product, scope, and implementation decisions for the Link
School team.

## Starting Context

The workshop group was discussing how a business school could stop losing the
knowledge created during interview cycles. Victor named the core problem: every
year the team learns valuable things from interviews, committee discussions, and
decisions, but the next team starts from scratch.

Initial goal:

- build a reusable interviewing workflow for the school;
- accumulate raw useful data;
- extract and process it into canonical memory assets;
- use a GBrain-style knowledge system;
- use skill libraries and a skill graph as operating discipline;
- create a projection layer for future interviews;
- use external deep research later to validate the plan.

## First Direction

The first pass framed the system as an interview knowledge workflow and produced
a business-plan-like outline. That was not enough. The group corrected the
direction: the value is not another document or summary for faculty to read.
The system must become useful decision support.

Key correction:

```text
Do not optimize for presentation first.
Optimize for memory quality, evals, benchmarks, reliability, and end-to-end mock execution.
```

## Recommendation Boundary

There was a discussion about whether the system should make recommendations.
The resulting boundary:

- the system should not automate approve/reject;
- the system may give a holistic recommended decision;
- the recommendation must be evidence-backed, auditable, and overrideable;
- humans make the final decision.

Useful outputs should include:

- green flags;
- red flags;
- missing evidence;
- per-domain indices;
- composite index;
- recommendation label;
- confidence;
- source evidence;
- committee questions.

## Rubric Boundary

For a real school, the school already has criteria. The system should ingest
their criteria rather than impose a generic rubric.

For the public mock, a synthetic rubric is acceptable as a replaceable fixture.
The mock rubric uses domains such as learning velocity, builder mindset,
leadership, communication clarity, collaboration maturity, mission fit,
execution evidence, and ethical judgment. These are examples, not claims about
Link School's real rubric.

## Deep Research Boundary

External deep research was launched separately and was still running during this
build. The decision was to avoid waiting for it before building a mock. The
research should later validate and improve:

- legal/privacy constraints;
- rubric assumptions;
- benchmark questions;
- recommendation boundaries;
- business plan;
- implementation roadmap.

Deep research should enrich the system after the local spec is clear; it should
not replace local requirement discovery.

## Build Decision

The team decided to build the full mock system DNA in this public repo:

```text
raw interview evidence
-> source/provenance ledger
-> canonical memory assets
-> GBrain-style memory graph
-> rubric/domain indices
-> retrieval benchmarks
-> holistic recommendation
-> committee packet
-> human review
-> retrospective learning
```

The mock scenario evaluates one synthetic candidate, `CAND-JQ-001`, across 30
synthetic interviews.

## Assets Built

The repo now includes:

- `business_plan_and_spec.md` - product DNA and system requirements;
- `spec.md` - implementation scope and output contract;
- `rubric.md` - replaceable mock rubric;
- `skill_graph.md` - workflow skill graph;
- `user_journey.md` - candidate, faculty, program owner, and memory steward
  journey;
- `uiux_blueprint.md` - application screens and UX requirements;
- `data/mock_interviews.json` - 30 synthetic interview records;
- `tools/run_mock_pipeline.py` - deterministic end-to-end pipeline;
- `generated/mock_gbrain_memory.json` - GBrain-style memory graph;
- `generated/candidate_evaluation.json` - computed indices and recommendation;
- `generated/candidate_packet.md` - human-readable committee packet;
- `generated/eval_report.json` - benchmark and reliability report.

## Eval Result

The pipeline was run end to end. It passed with:

```text
candidate_id: CAND-JQ-001
record_count: 30
memory_asset_count: 60
provenance_coverage: 1.0
domain_coverage: 1.0
retrieval_hit_at_3: 1.0
composite_index: 78.0
recommendation: recommend
```

An earlier expectation was too optimistic: the benchmark initially expected
`strong_recommend`, but the synthetic data included real pacing/collaboration
risks. The benchmark was corrected to expect `recommend`. That correction is
important: the eval should preserve honest red/yellow signals instead of forcing
green.

## User Journey Decision

Victor asked how users would interact with the system. The resulting product
shape is a self-serve interview application:

```text
candidate receives interview link
-> candidate sees consent and data boundary
-> candidate completes structured self-serve interview
-> candidate reviews and submits answers
-> system indexes evidence against rubric and memory
-> faculty sees evidence packet, not raw transcript first
-> committee challenges, overrides, or accepts recommendation
-> memory steward promotes reusable lessons
-> next cycle starts from accumulated memory
```

The UI is part of the system DNA, but not the whole DNA. The application is the
front door into the memory, rubric, evaluation, benchmark, committee review, and
retrospective loop.

## What The Repo Is For

This repo is a workshop artifact and a continuation workspace. The team can use
it to:

1. understand the system concept;
2. run the mock pipeline locally;
3. inspect the generated memory graph and candidate packet;
4. replace the mock rubric with real school criteria;
5. replace synthetic data with approved/de-identified data only after governance
   review;
6. revise benchmarks after deep research returns;
7. use the user journey and UI/UX blueprint as the basis for an app prototype.

## Next Steps For The Team

1. Read `business_plan_and_spec.md`.
2. Read `user_journey.md` and `uiux_blueprint.md`.
3. Run:

   ```bash
   python3 examples/business-school-interview-memory/tools/run_mock_pipeline.py
   ```

4. Inspect `generated/candidate_packet.md`.
5. When deep research returns, update:
   - real-school rubric assumptions;
   - legal/privacy gates;
   - benchmark questions;
   - recommendation labels;
   - app journey and review gates.
6. If building a real pilot, start with synthetic or approved de-identified
   data. Do not paste real candidate records into the mock.

## Design Principle To Preserve

The system should not become a prettier transcript reader. It should be a
reliable capability layer:

```text
memory + rubric + evals + benchmarks + evidence + human review
```

That is the DNA.

## Deep Research Addendum

After this session history was first exported, the deep research memo returned
and narrowed the production v0. The current repo now treats this example as
Interview Memory OS v0: governed interview-cycle memory, source/consent ledger,
de-identification review, GBrain-style canonical memory, aggregate projection
hypotheses, and next-cycle playbook.

The earlier `recommend` output is preserved above as workshop history. The
current mock replaces admissions-like labels with synthetic review-guidance
labels such as `positive_signal_with_discussion_risks`, and the eval now checks
that no output becomes admit/reject/rank decisioning.

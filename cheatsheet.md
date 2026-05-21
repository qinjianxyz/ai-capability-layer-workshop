# Agentic Capability Layer Cheat Sheet

This is the workshop default stack. It is opinionated on purpose. The goal is
not perfection; perfection takes taste. The goal is a solid default that helps a
team move from fuzzy workflow idea to governed, inspectable capability.

## Capability Sentence

Produce **[artifact]** from **[allowed inputs]** for **[reviewer]** so that
**[decision or action]** improves, with **[human review gate]** before the
system acts externally or updates official memory.

Example:

```text
Produce a committee review packet from structured interview notes and approved
canonical memory for faculty reviewers so that next-cycle decisions are more
consistent, with the committee retaining final authority.
```

## The Default Stack

| Layer | Default Tooling / Pattern | What It Is For |
| --- | --- | --- |
| Runtime | Hermes / Codex-style agent execution | Turns a scoped objective into files, checks, commits, and receipts. |
| Memory | GBrain | Stores approved knowledge, source lineage, decisions, playbooks, and reusable context. |
| Process Library | GStack | Gives reusable operating moves: office hours, context restore/save, benchmark, design review, browse, careful review. |
| Engineering Discipline | Superpowers | Planning, TDD, executing plans, debugging, finishing branches. |
| Pressure Testing | Matt Pocock skills | Grill Me, interface design, diagnose, and human-readable engineering judgment. |
| Skill Graph | Internal graph | Maps repeated work into skills with triggers, inputs, outputs, owners, verifiers, and memory updates. |
| Spec | Spec-driven development | Locks scope, data boundaries, non-goals, output contracts, and acceptance criteria before building. |
| Tests / Evals | Test-driven development | Defines checks before trusting output: schemas, fixtures, retrieval, red lines, quality gates. |
| Research | Deep research-driven development | Uses external intelligence only when it changes the spec, source policy, risk model, or benchmark. |
| Context | Context engineering | Builds the right context packet: sources, examples, templates, terminology, retrieval, freshness, exclusions. |
| Harness | Harness engineering | Adds state, logs, commands, verifiers, receipts, recovery paths, and human approval gates. |

## Opinionated Default Workflow

```text
founder / faculty intent
-> office-hours scope pressure
-> grill-me unresolved decisions
-> architecture and data boundary
-> spec
-> test / eval plan
-> mock fixture
-> implementation
-> generated artifacts
-> verifier run
-> human review
-> GBrain memory update
-> next-cycle playbook
```

## Hermes

Use Hermes when the work should keep moving as an execution lane, not stay as a
chat. Hermes-style work needs:

- objective;
- writable scope;
- done criteria;
- stop criteria;
- commands to run;
- artifacts to produce;
- proof or receipt.

Default rule: Hermes should execute a spec. It should not invent the product
strategy while writing production assets.

## GBrain

Use GBrain as the canonical memory system, not a dumping ground.

Good GBrain memory:

- has source lineage;
- has owner and review status;
- says when it applies;
- says when it expires or needs review;
- separates raw evidence from approved memory;
- can be retrieved by future workflows;
- improves the next run.

Bad GBrain memory:

- raw transcripts with no boundary;
- private data pasted into search;
- vibes with no source;
- stale claims with no review date;
- unowned decisions.

Default pattern:

```text
raw source
-> source ledger
-> redaction / de-identification
-> canonical memory asset
-> GBrain retrieval
-> answer with source links
-> memory update after review
```

## GStack

Use GStack for operating discipline.

Default uses:

- `office-hours`: clarify customer, wedge, status quo, value, scope, and risk.
- `benchmark`: turn "good" into measurable checks.
- `careful`: slow down when claims, data, legal, or safety boundaries matter.
- `context-save` / `context-restore`: preserve working state between runs.
- `design-review`: pressure-test product and UX choices.
- `browse`: collect external context when current facts matter.

Default rule: GStack helps choose the next move. It is not the source of truth
for the school's criteria or policy.

## Superpowers

Use Superpowers as the engineering method.

Default mapping:

- Brainstorming: generate options before locking the spec.
- Planning: split work into executable slices.
- TDD: define tests/evals before implementation.
- Executing plans: build against the plan, not the mood.
- Debugging: isolate failure, reproduce it, fix it, prove it.
- Finishing a branch: stage, commit, verify, push, and leave a receipt.

Default rule: no serious capability is done until it has a verifier.

## Matt Pocock Skills

Use Matt Pocock skills for sharp human pressure.

Default uses:

- `grill-me`: one hard question at a time until the requirement is no longer
  mushy.
- interface design: clarify module boundaries, contracts, and public APIs.
- diagnose: turn vague failure into a specific cause.

Default rule: use Grill Me before the team starts building the wrong polished
thing.

## Skill Graphs

A skill graph is not a prompt library. It is the map of repeated institutional
behaviors.

Each skill node needs:

- trigger;
- input contract;
- output contract;
- owner;
- verifier;
- phase;
- memory update rule;
- failure mode.

Example:

```text
Rubric pressure test
Trigger: rubric reused or changed
Input: rubric + last-cycle memory
Output: risks and clarification list
Owner: faculty chair
Verifier: faculty panel
Memory update: rubric lesson asset
```

Default rule: if a workflow repeats, make it a skill. If it matters, give it a
verifier.

## Spec-Driven Development

Write the spec before the artifact.

Minimum spec:

- capability sentence;
- users and reviewers;
- allowed inputs;
- prohibited inputs;
- output contract;
- non-goals;
- data boundary;
- human approval gate;
- acceptance criteria;
- verification commands.

Default rule: a vague spec produces a confident mess.

## Test-Driven Development

For software, write tests. For AI workflows, write evals and benchmarks.

Default evals:

- schema validity;
- fixture count;
- source coverage;
- provenance coverage;
- retrieval hit rate;
- forbidden label check;
- red-line policy check;
- human-review gate check;
- generated artifact existence;
- regression fixture.

Default rule: if the system cannot fail, the test is decoration.

## Deep Research-Driven Development

Use deep research when local knowledge is not enough.

Good deep research changes:

- source policy;
- legal/privacy boundary;
- market map;
- architecture;
- rubric;
- benchmark;
- risk register;
- implementation roadmap.

Bad deep research becomes:

- an essay nobody operationalizes;
- citations with no spec delta;
- market noise with no build decision;
- a reason to avoid a small mock.

Default rule:

```text
research finding
-> decision
-> spec change
-> fixture/check
-> generated artifact
-> review gate
```

## Context Engineering

Context engineering decides what the model is allowed to know and use.

Context packet:

- task objective;
- source policy;
- approved inputs;
- excluded inputs;
- examples;
- terminology;
- output schema;
- review checklist;
- freshness requirement;
- retrieved memory.

Default rule: do not solve context problems with longer prompts. Use better
source selection, metadata, retrieval, and exclusions.

## Harness Engineering

A harness makes agentic work governable.

Minimum harness:

- objective;
- state file or run record;
- input fixture;
- output directory;
- verifier command;
- generated report;
- failure message;
- recovery path;
- human approval gate;
- changelog or receipt.

Default rule: if a workflow matters, it needs a command that proves what
happened.

## Solid Default For A New Capability

1. Run office-hours: why this, why now, who cares, what is out of scope?
2. Run Grill Me: what decision are we avoiding?
3. Write the spec.
4. Create synthetic fixtures.
5. Write evals before improving the output.
6. Build the smallest end-to-end mock.
7. Add GBrain-style memory with provenance.
8. Add the skill graph only for repeated behaviors.
9. Run the verifier.
10. Convert lessons into a playbook.
11. Decide: continue, narrow, park, or kill.

## Review Gate

Ask these before publishing or piloting:

- What factual claims need verification?
- What assumptions should be labeled?
- What unknowns should be surfaced?
- What confidential data might be exposed?
- What raw data must stay out of GBrain?
- What external commitment might be implied?
- What red lines must the system enforce?
- What test would catch drift?
- Who approves the next action?

## Taste Still Matters

The stack gives a team a reliable default. It does not replace taste. Taste is
knowing when the default is too heavy, when the artifact is lying, when a metric
is theater, when a workflow needs human trust more than automation, and when the
right move is to narrow the scope.

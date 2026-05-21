# Skill Graph: Interview Memory Mock

## Workflow

```text
cycle-intake-and-governance-gate
-> rubric-pressure-test
-> question-bank-calibration
-> interviewer-calibration
-> structured-evidence-capture
-> edge-case-decision-logging
-> redaction-and-de-id-review
-> canonical-memory-distillation
-> gbrain-style-memory-build
-> retrieval-benchmark
-> aggregate-projection-packet
-> retrospective-and-next-cycle-playbook
```

## Skills

| Skill | Trigger | Input | Output | Owner | Verifier | Memory Update |
| --- | --- | --- | --- | --- | --- | --- |
| Cycle intake and governance gate | New interview cycle starts | Program, rubric, data types, vendors | Approved scope and data map | Admissions ops | Privacy owner | Creates cycle record and ledger |
| Rubric pressure test | Rubric is reused or changed | Rubric, last-cycle memory | Rubric risks and clarification list | Faculty chair | Faculty panel | Updates rubric memory asset |
| Question-bank calibration | Questions selected | Question inventory, rubric | Approved question/probe set | Faculty lead | Calibration group | Updates question performance asset |
| Interviewer calibration | Before live interviews | Sample responses, rubric anchors | Calibration notes and disagreements | Faculty trainer | Committee chair | Updates calibration asset |
| Structured evidence capture | Interview completed | Notes, rubric dimensions | Evidence-coded note | Interviewer | Admissions ops | Adds source-linked note |
| Edge-case decision logging | Committee ambiguity arises | Candidate evidence, rubric, issue | Rationale, dissent, unresolved issue | Committee chair | Second faculty reviewer | Adds edge-case memory |
| Redaction and de-ID review | Raw evidence becomes memory | Draft summary, raw source | De-identified asset or rejection | Knowledge steward | Privacy owner | Updates anonymization log |
| Canonical memory distillation | Post-cycle synthesis | Notes, logs, retrospective | Canonical memory asset | Knowledge steward | Faculty chair | Publishes to GBrain |
| Retrospective facilitation | Cycle ends | Metrics, examples, unresolved questions | Retro decisions and action list | Facilitator | Faculty team | Updates playbook |
| Projection packet creation | Planning next cycle | Canonical assets, metrics | Aggregate hypotheses | Knowledge steward | Faculty chair | Adds projection records |
| Projection falsifier review | Projection proposed | Hypothesis, evidence, counterexamples | Approve/revise/block | Faculty panel | Privacy/ethics reviewer | Updates projection status |
| Next-cycle playbook publishing | New cycle preparation | Approved memory and projections | Playbook | Faculty chair | Program owner | Supersedes prior playbook |

The same 12 nodes are represented in `data/mock_cycle_setup.json` and checked by
the pipeline. The current eval requires at least eight used skill nodes and the
mock uses all 12.

## External Process Inspiration

- `gstack office-hours`: pressure-test customer, status quo, wedge, and future
  fit before expanding the workflow.
- `Matt Pocock grill-me`: ask one hard requirement question at a time until the
  evaluation contract is unambiguous.
- `Superpowers planning/TDD/verification`: define checks before improving the
  artifact.
- `GBrain`: represent approved memory as queryable, provenance-backed assets.

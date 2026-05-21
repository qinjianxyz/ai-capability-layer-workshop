# UI/UX Blueprint: Interview Memory OS

## Design Direction

The application should feel like a calm institutional cockpit, not a chatbot.
Candidates need clarity and trust. Faculty need dense evidence and fast
comparison. Program owners need configuration and auditability.

Visual tone:

- serious academic operations;
- quiet confidence;
- clear status states;
- evidence-first;
- no gimmicky AI framing.

## Candidate Experience

### Candidate Start

Purpose:

- confirm identity or invite token;
- explain time required;
- explain process;
- set expectations.

Primary actions:

- start interview;
- save and return;
- contact support.

### Consent And Data Boundary

Must show:

- interview purpose;
- who reviews responses;
- what AI assists with;
- what AI does not do;
- retention summary;
- candidate rights/support path.

Primary action:

- acknowledge and continue.

Blocking states:

- candidate declines;
- candidate is under age threshold and needs special process;
- unsupported data mode.

### Interview Workspace

Layout:

- left: section list and progress;
- center: current prompt and response field;
- right: rubric hint written in candidate-friendly language.

Controls:

- previous;
- save draft;
- next;
- request clarification;
- flag accessibility issue.

Do not show:

- score;
- predicted recommendation;
- hidden rubric weights.

### Review Before Submit

Shows:

- completed sections;
- missing sections;
- optional evidence;
- privacy reminder;
- edit links.

Primary action:

- submit interview.

### Submission Receipt

Shows:

- timestamp;
- what happens next;
- support contact;
- data rights contact.

## Faculty Experience

### Review Queue

Columns:

- candidate id;
- completion status;
- evaluation status;
- composite band;
- highest green flag;
- highest red flag;
- missing evidence count;
- reviewer assignment.

Filters:

- ready for review;
- needs attention;
- high disagreement;
- missing evidence;
- red flag present.

### Candidate Evidence Packet

Top band:

- recommendation label;
- composite index;
- confidence;
- reviewer status;
- benchmark status.

Main panels:

- domain indices;
- green flags;
- red flags;
- missing evidence;
- committee questions;
- source excerpts.

Actions:

- accept domain interpretation;
- challenge evidence;
- add human note;
- override index with reason;
- send to committee;
- request another reviewer.

### Committee View

Purpose:

- compare AI recommendation, faculty notes, and committee decision.

Shows:

- recommendation;
- reviewer overrides;
- unresolved disagreements;
- risk flags;
- final human decision field;
- decision rationale.

## Program Owner Experience

### Cycle Configuration

Configure:

- program;
- cycle dates;
- rubric;
- question bank;
- allowed response modes;
- recommendation labels;
- benchmark thresholds;
- privacy notice;
- reviewer assignments.

### Rubric Builder

For each domain:

- name;
- description;
- weight or priority;
- evidence examples;
- red flags;
- missing evidence rules.

Import path:

- paste existing school criteria;
- upload CSV;
- map columns to domains.

### Benchmark Cockpit

Shows:

- schema pass/fail;
- provenance coverage;
- domain coverage;
- retrieval hit rate;
- forbidden label check;
- recommendation drift;
- override rate.

## Memory Steward Experience

### Canonical Memory Review

Rows:

- proposed memory;
- source evidence;
- domain;
- confidence;
- cycle;
- suggested status.

Actions:

- approve;
- edit;
- reject;
- retire.

### Skill Graph View

Shows workflow nodes:

- intake;
- validation;
- rubric indexing;
- memory extraction;
- evaluation;
- faculty review;
- retrospective.

Each node has:

- owner;
- input;
- output;
- verifier;
- failure modes.

## MVP Screens To Build First

1. Candidate interview workspace.
2. Faculty candidate evidence packet.
3. Program rubric configuration.
4. Eval and benchmark cockpit.

These four screens are enough to show the full system loop.

## UX Risks

- Too much AI theater: candidates may distrust the process.
- Too much raw transcript: faculty drown in information again.
- Hidden recommendation logic: committee cannot challenge the system.
- Overexposed scoring: candidates may optimize answers unnaturally.
- Weak privacy copy: school cannot responsibly use real data.

## UX Success Metrics

- Candidate completion rate.
- Candidate support requests per interview.
- Faculty time to first useful judgment.
- Percent of faculty recommendations with evidence review completed.
- Override rate and override quality.
- Memory assets approved per cycle.
- Benchmark pass rate before launch.

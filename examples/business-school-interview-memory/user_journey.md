# User Journey: Self-Serve Interview Application

## Product Shape

The application is a self-serve interview workspace. A candidate can enter a
school-provided interview link, complete a structured interview asynchronously,
review what will be submitted, and send it to the committee. Faculty then review
an evidence-backed committee packet, not a raw ocean of answers.

The key idea:

```text
candidate self-serve interview
-> structured evidence capture
-> memory and rubric indexing
-> benchmarked review guidance
-> faculty committee packet
-> human final decision
-> retrospective learning
```

## Personas

### Candidate

Needs a clear, respectful process. They should know what is being asked, how
their data will be used, how much time is required, what they can review before
submission, and what happens next.

### Faculty Reviewer

Needs evidence, not a pile of transcripts. They want domain indices, green
flags, red flags, missing evidence, key excerpts, committee questions, and a
review-guidance label they can challenge. The label is not an admit/reject/rank
decision.

### Program Owner

Needs control. They configure criteria, question bank, interview stages,
allowed review-guidance labels, privacy boundaries, and benchmark thresholds.

### Memory Steward

Needs to preserve institutional learning. They approve which observations become
canonical memory, monitor eval quality, and update the skill graph after each
cycle.

## Candidate Journey

### 1. Invitation

The candidate receives a school-branded link:

```text
Complete your Link School interview by Friday.
Estimated time: 35-45 minutes.
You can pause and return.
You may review your written answers before submitting.
```

The link opens a focused interview workspace, not a marketing page.

### 2. Consent And Boundary Screen

The candidate sees:

- purpose of the interview;
- whether responses are text, audio, video, or mixed;
- how responses will be reviewed;
- whether AI assists faculty review;
- what AI does not do;
- retention and deletion/correction contact;
- privacy owner and support contact.

The candidate must acknowledge before continuing.

### 3. Warm Start

The app asks for context needed to personalize the interview flow without
creating hidden profiling:

- preferred language;
- accessibility needs;
- whether they want text, audio, or video prompts if allowed;
- whether they need to pause and resume;
- confirmation that they are ready.

### 4. Structured Interview

The interview is broken into short sections tied to the school's actual rubric.
For the mock:

- learning velocity;
- builder mindset;
- leadership;
- communication;
- collaboration;
- mission fit;
- execution evidence;
- ethical judgment.

Each section has:

- one core prompt;
- one evidence follow-up;
- one reflection or tradeoff question;
- optional artifact upload if the school allows it.

Example:

```text
Tell us about something you built or changed under uncertainty.
What evidence shows it worked?
What did you learn or revise afterward?
```

### 5. Evidence Review

Before submission, the candidate sees a review page:

- answered sections;
- unanswered sections;
- optional evidence uploads;
- time remaining;
- what will be submitted;
- "edit answer" controls.

The candidate does not see synthetic evidence indices, review guidance, or
hidden rubric weights.

### 6. Submission Receipt

After submission, the candidate receives:

- confirmation;
- timestamp;
- next-step expectation;
- support contact;
- data rights contact if applicable.

## Faculty Journey

### 1. Intake Dashboard

Faculty see candidate submissions by status:

- ready for review;
- incomplete;
- needs human attention;
- data boundary issue;
- review guidance generated;
- committee reviewed.

### 2. Candidate Evidence Packet

For each candidate, faculty see:

- review-guidance label;
- synthetic evidence support index;
- per-domain indices;
- confidence;
- green flags;
- red flags;
- missing evidence;
- key excerpts;
- committee questions;
- provenance links to source answers.

The first useful view is not a transcript. The transcript is behind the evidence
packet.

The packet must display the red line: it is not an admit/reject/rank/fit
decision.

### 3. Challenge And Override

Faculty can:

- accept the system's domain interpretation;
- mark evidence as weak;
- add a human note;
- override a domain index;
- request another reviewer;
- flag a rubric issue;
- mark a memory candidate for future cycles.

Every override becomes learning data.

### 4. Committee View

The committee view aggregates:

- review guidance;
- faculty reviewer notes;
- unresolved disagreements;
- red flags requiring discussion;
- missing evidence;
- decision options;
- final human decision.

The final decision is recorded separately from synthetic review guidance.

## Program Owner Journey

### 1. Configure Cycle

The program owner creates an interview cycle:

- program name;
- rubric version;
- domains and weights;
- question bank;
- allowed response modes;
- privacy notice;
- retention policy;
- allowed review-guidance labels;
- benchmark thresholds.

### 2. Test With Synthetic Candidate

Before going live, the owner runs a synthetic candidate through the workflow and
checks:

- all questions display correctly;
- evidence maps to domains;
- review packet is useful;
- no forbidden labels appear;
- benchmark checks pass.

### 3. Launch

The owner sends candidate links only after a reviewer and support path are
assigned.

## Memory Steward Journey

### 1. Review Canonical Memory Candidates

After the cycle, the system proposes reusable memories:

- question produced high signal;
- rubric dimension was ambiguous;
- common candidate evidence pattern;
- repeated red flag;
- committee disagreement pattern;
- process issue.

The steward approves, edits, or rejects each memory.

### 2. Update Skill Graph

When a repeated practice becomes stable, the steward updates the skill graph:

- trigger;
- input;
- output;
- verifier;
- owner;
- failure modes.

### 3. Run Retrospective Benchmark

The steward asks:

- Did retrieval answer real committee questions?
- Did domain indices match faculty judgment?
- Were red flags useful?
- Which prompts produced weak evidence?
- What needs to change next cycle?

## Core Screens

1. Candidate consent and boundary.
2. Candidate interview workspace.
3. Candidate review and submit.
4. Candidate receipt.
5. Faculty intake dashboard.
6. Candidate evidence packet.
7. Committee review.
8. Program configuration.
9. Memory steward review.
10. Eval and benchmark cockpit.

## App Information Architecture

```text
/candidate/:token
  /start
  /consent
  /interview
  /review
  /submitted

/faculty
  /queue
  /candidate/:id
  /committee/:cycle_id

/admin
  /cycle/:id/config
  /rubric/:id
  /questions
  /privacy
  /benchmarks

/memory
  /assets
  /review
  /skill-graph
  /retrospective
```

## What The UI Must Make Obvious

- AI is advisory.
- Humans make final decisions.
- Evidence is traceable.
- Candidate data has boundaries.
- Missing evidence is not the same as weak evidence.
- Red flags require discussion, not automatic rejection.
- Every cycle improves the memory system.

## MVP Interaction Standard

The first application should feel like a serious school workflow:

- calm;
- sparse;
- precise;
- respectful of candidate time;
- direct about privacy;
- dense enough for faculty review;
- no chatbot novelty as the main interface.

## System Quality Hidden Under The UX

Every candidate journey should leave behind:

- raw answer records;
- source ledger entries;
- canonical memory candidates;
- rubric-domain evidence;
- committee review packet;
- benchmark run;
- faculty overrides;
- retrospective learning.

That is the DNA. The UI is how humans participate in it.

# Agentic Capability Layer Workshop

Public companion repo for the workshop **Designing Agentic Capability Layers**.

The workshop helps staff and faculty design supervised AI workflows for operations, research, teaching, and mentoring. The practical output is a workflow candidate with a capability sentence, context pack, memory boundary, skill graph, harness/review plan, and 30-day pilot path.

## How To Use This Repo With A Team

Use this repo as a shared workshop workbook, not as a finished product. The team
should read one example, discuss the scope and governance boundary, run the
mock, then replace synthetic assumptions with the school's real criteria only
after review.

Suggested team flow:

1. Start with the business school example:
   `examples/business-school-interview-memory/`.
2. Read the session history to understand how the requirements evolved:
   `examples/business-school-interview-memory/session_history_2026-05-21.md`.
3. Read the system DNA:
   `examples/business-school-interview-memory/business_plan_and_spec.md`.
4. Read the candidate and faculty journey:
   `examples/business-school-interview-memory/user_journey.md`.
5. Read the UI/UX blueprint:
   `examples/business-school-interview-memory/uiux_blueprint.md`.
6. Run the mock pipeline and inspect the generated candidate packet.
7. Use the worksheet and pilot template to adapt the pattern to a real workflow.

The repo is meant to help a team ask better questions:

- What inputs are allowed?
- What memory should accumulate?
- What skills and review gates are needed?
- What benchmarks prove reliability?
- What should humans decide?
- What should the system never automate?

## Start Here

1. Read `cheatsheet.md`.
2. Fill `activity_worksheet.md` for one workflow.
3. Use `prompt_pack.md` to generate a capability spec, context/memory plan, staff artifact, faculty artifact, skill file, and governance review.
4. Read `technical_reference.md` for tokens, models, context engineering, GBrain-style memory, vector embeddings, skill graph, harness engineering, and deep research.
5. Use `pilot_template.md` to turn the workflow into a narrow 30-day pilot.

## Core Idea

A useful AI capability is a supervised path from allowed inputs to reviewed artifacts. The model is one layer. Reliability comes from context engineering, memory, skills, harnesses, checks, and human review.

## Files

- `cheatsheet.md` - one-page reference.
- `activity_worksheet.md` - workshop worksheets.
- `prompt_pack.md` - prompts for the live workflow build.
- `technical_reference.md` - technical concepts explained plainly.
- `skill_deep_dives.md` - Grill Me, spec-driven work, TDD, Superpowers, GStack, GBrain, deep research.
- `tooling_options.md` - chat tools, coding agents, memory layers, orchestration, local models.
- `use_case_library.md` - staff, faculty, mentoring, and research use cases.
- `governance_boundary.md` - data classes and review rules.
- `pilot_template.md` - 30-day pilot plan.
- `live_build_workflow_kit.md` - optional repo-backed build instructions.
- `examples/business-school-interview-memory/` - end-to-end synthetic interview
  memory system with mock data, rubric, GBrain-style memory graph, evaluator,
  benchmarks, and self-serve interview app journey.

## Data Rule

Use synthetic, public, or explicitly approved low-risk context. Keep student records, confidential faculty/staff information, credentials, sensitive partner details, and unsupervised external actions out of early pilots.

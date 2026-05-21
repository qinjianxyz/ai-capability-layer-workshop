# Skill Graph: Interview Memory Mock

## Workflow

```text
interview-cycle-intake
-> raw-evidence-validation
-> rubric-indexing
-> canonical-memory-extraction
-> gbrain-style-memory-build
-> retrieval-benchmark
-> candidate-evaluation
-> committee-recommendation-review
-> retrospective-learning
```

## Skills

| Skill | Trigger | Input | Output | Verifier |
| --- | --- | --- | --- | --- |
| interview-cycle-intake | New interview cycle | Candidate, rubric, notes | Cycle bundle | schema check |
| raw-evidence-validation | Data arrives | Interview records | Accepted/rejected records | data boundary check |
| rubric-indexing | Rubric changes | Domain definitions | Domain registry | weight sum check |
| canonical-memory-extraction | Notes accepted | Observations | Memory assets | provenance check |
| gbrain-style-memory-build | Assets approved | Memory assets | Graph nodes and edges | graph integrity check |
| retrieval-benchmark | Memory graph changes | Query set | hit@k metrics | threshold check |
| candidate-evaluation | Committee prep | Rubric + memories | Domain and composite indices | expected eval check |
| committee-recommendation-review | Packet ready | Evaluation packet | Human review queue | forbidden label check |
| retrospective-learning | Cycle ends | Review notes | Skill/rubric updates | owner approval |

## External Process Inspiration

- `gstack office-hours`: pressure-test customer, status quo, wedge, and future
  fit before expanding the workflow.
- `Matt Pocock grill-me`: ask one hard requirement question at a time until the
  evaluation contract is unambiguous.
- `Superpowers planning/TDD/verification`: define checks before improving the
  artifact.
- `GBrain`: represent approved memory as queryable, provenance-backed assets.

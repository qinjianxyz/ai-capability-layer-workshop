# Synthetic Committee Review Packet

- Candidate: `CAND-JQ-001`
- Data class: `synthetic`
- Deployment boundary: synthetic workshop fixture; not a production admissions decision system
- Review guidance: `positive_signal_with_discussion_risks`
- Guidance meaning: committee review guidance, not admit/reject/rank/fit scoring
- Synthetic evidence support index: `78.0`
- Recommendation confidence: `0.79`
- Eval status: `PASS`
- Red line: this packet is not an admit/reject/rank/fit decision.

## Domain Evidence Indices

| Domain | Index | Confidence | Green | Red | Missing |
| --- | ---: | ---: | ---: | ---: | ---: |
| learning_velocity | 85.1 | 0.82 | 7 | 0 | 0 |
| entrepreneurial_builder | 88.2 | 0.85 | 7 | 0 | 0 |
| leadership_initiative | 85.3 | 0.81 | 6 | 0 | 0 |
| communication_clarity | 71.0 | 0.73 | 6 | 1 | 1 |
| collaboration_maturity | 57.3 | 0.7 | 5 | 3 | 1 |
| mission_fit | 83.4 | 0.78 | 7 | 0 | 1 |
| execution_evidence | 87.6 | 0.83 | 8 | 0 | 0 |
| ethical_judgment | 82.6 | 0.79 | 6 | 0 | 1 |

## Strongest Green Flags

- **entrepreneurial_builder** (INT-002): Insisted on building an end-to-end mock system rather than stopping at a business plan.
- **entrepreneurial_builder** (INT-016): Asked to mock the entire business school process instead of waiting for perfect real data.
- **entrepreneurial_builder** (INT-011): Asked to build the capability layer itself: memory, evals, benchmarks, and mock end-to-end workflow.
- **execution_evidence** (INT-009): Converted a vague interviewing workflow into datasets, rubrics, memory databases, evals, and benchmarks.
- **learning_velocity** (INT-017): Placed deep research after local requirement discovery so it can validate and enrich rather than dominate.

## Red Flags And Discussion Risks

- **collaboration_maturity** (INT-010): Fast critique could overwhelm collaborators if not paired with explicit shared framing.
- **collaboration_maturity** (INT-003): May create large ambition faster than stakeholders can digest unless the scope is actively bounded.
- **communication_clarity** (INT-014): May need to translate technical architecture into faculty-friendly language more consistently.
- **collaboration_maturity** (INT-018): May need explicit cohort norms around pacing, listening, and shared ownership.

## Missing Evidence

- **mission_fit** (INT-008): Needs a sharper business metric for Link School adoption beyond technical correctness.
- **ethical_judgment** (INT-013): Needs explicit validation boundaries before using composite indices in real selection.
- **communication_clarity** (INT-020): Needs clearer buyer-facing value narrative after the technical mock works.
- **collaboration_maturity** (INT-028): Need more evidence on how the candidate behaves in slower group settings.

## Committee Questions For Human Review

- How should the committee weigh exceptional builder signal against pacing and collaboration risks?
- What evidence would show the candidate can translate technical ambition for a mixed-experience cohort?
- Which faculty mentor or structure would help sequence ambition into scoped milestones?
- What real-school outcome should validate whether this candidate's systems mindset creates cohort value?

## Benchmark Summary

- PASS: `candidate_is_synthetic` - synthetic
- PASS: `record_count` - 30/30
- PASS: `rubric_weights_sum_to_one` - 1.0000
- PASS: `observation_domains_known` - ok
- PASS: `governing_scope_blocks_production_candidate_decision_use` - False
- PASS: `raw_vault_separated_from_gbrain` - deidentified_canonical_memory_only
- PASS: `candidate_notice_portuguese_declared` - pt-BR
- PASS: `legal_basis_matrix_covers_required_purposes` - ok
- PASS: `skill_nodes_used` - 12/8
- PASS: `projection_hypotheses_are_aggregate_only` - 5 hypotheses
- PASS: `provenance_coverage` - 1.000
- PASS: `graph_edges_resolve` - 0 dangling edges
- PASS: `domain_coverage` - 1.000
- PASS: `source_ledger_coverage` - 1.000
- PASS: `deidentified_memory_review_coverage` - 1.000
- PASS: `retrieval_hit_at_3` - 1.000
- PASS: `recommendation_matches_expected` - positive_signal_with_discussion_risks expected positive_signal_with_discussion_risks
- PASS: `composite_index_threshold` - 78.0 >= 76
- PASS: `no_forbidden_recommendation_labels` - ok
- PASS: `no_raw_vault_refs_in_gbrain_memory` - raw refs are ledger-only
- PASS: `projection_packet_count` - 5/5
- PASS: `projection_evidence_refs_resolve` - ok
- PASS: `projection_packet_blocks_candidate_use` - candidate-level blocked uses declared
- PASS: `retrospective_playbook_ready` - 12 skill nodes support next-cycle playbook

## Governance Boundary

- Production candidate decision use: `False`
- Projection layer scope: `aggregate_process_hypotheses_only`
- GBrain allowed data: `deidentified_canonical_memory_only`
- Do not automate: admit_reject, candidate_ranking, candidate_fit_scoring, protected_trait_inference, emotion_recognition, personality_scoring, individual_success_prediction, automated_committee_rationale_without_human_approval

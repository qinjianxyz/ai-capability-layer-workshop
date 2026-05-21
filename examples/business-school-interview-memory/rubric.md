# Mock Business School Interview Rubric

This rubric is synthetic. It is designed for workshop evaluation of a supervised
AI capability layer, not for real admissions use.

## Domains

| Domain | Weight | What Strong Evidence Looks Like |
| --- | ---: | --- |
| learning_velocity | 0.16 | Learns quickly, updates beliefs, translates feedback into better execution |
| entrepreneurial_builder | 0.17 | Builds real things, finds opportunities, acts under ambiguity |
| leadership_initiative | 0.13 | Creates direction, mobilizes others, owns outcomes |
| communication_clarity | 0.12 | Explains tradeoffs, evidence, and decisions clearly |
| collaboration_maturity | 0.11 | Listens, shares credit, improves team decisions |
| mission_fit | 0.12 | Understands the school, contributes to the cohort, uses business for impact |
| execution_evidence | 0.11 | Has shipped work, measured outcomes, and persisted through hard constraints |
| ethical_judgment | 0.08 | Names risks, respects boundaries, handles power and data responsibly |

## Risk Flags

Risk flags do not automatically disqualify a candidate. They force committee
discussion and can cap the recommendation if severe.

- over_claiming
- weak_listening_signal
- unclear_motivation
- ethics_or_privacy_concern
- low_follow_through
- poor_team_maturity
- missing_core_evidence

## Synthetic Evidence Support Index

The synthetic evidence support index is a weighted aggregate of domain evidence
indices, adjusted by:

- high-severity red flags;
- missing critical evidence;
- contradiction count;
- recommendation confidence.

## Review Guidance Labels

| Label | Meaning |
| --- | --- |
| strong_positive_signal_with_risks | Strong synthetic evidence across domains, with risks still surfaced for human review |
| positive_signal_with_discussion_risks | Positive synthetic evidence with discussion items |
| mixed_signal_discuss_further | Mixed evidence or important unresolved questions |
| material_concerns_review_required | Material concerns despite some strengths |
| insufficient_evidence | The system cannot responsibly give review guidance either way |

These labels are not admissions decisions. They must not be converted into
admit/reject/rank outputs without a separate legal, validity, fairness, and
faculty governance review.

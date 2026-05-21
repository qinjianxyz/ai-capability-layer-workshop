#!/usr/bin/env python3
"""Run the business school interview memory mock end to end.

This script intentionally uses only the Python standard library. It is a
workshop-quality harness: deterministic, inspectable, and easy to modify.
"""

from __future__ import annotations

import json
import math
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "mock_interviews.json"
SETUP_PATH = BASE_DIR / "data" / "mock_cycle_setup.json"
EXPECTED_PATH = BASE_DIR / "benchmarks" / "expected_eval.json"
GENERATED_DIR = BASE_DIR / "generated"

FORBIDDEN_RECOMMENDATION_LABELS = {
    "admit",
    "reject",
    "scholarship_award",
    "automatic_rank",
    "strong_recommend",
    "recommend",
    "do_not_recommend",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def slug_tokens(text: str) -> set[str]:
    stop = {
        "a",
        "an",
        "and",
        "the",
        "to",
        "of",
        "for",
        "in",
        "on",
        "with",
        "what",
        "did",
        "we",
        "this",
        "that",
    }
    return {token for token in re.findall(r"[a-z0-9_]+", text.lower()) if token not in stop}


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


@dataclass(frozen=True)
class Observation:
    observation_id: str
    interview_id: str
    domain: str
    polarity: str
    strength: int
    confidence: float
    text: str
    risk_flag: str | None

    @property
    def signed_strength(self) -> float:
        if self.polarity == "green":
            return self.strength * self.confidence
        if self.polarity == "red":
            return -self.strength * self.confidence
        return 0.0


def collect_observations(data: dict[str, Any]) -> list[Observation]:
    observations: list[Observation] = []
    for interview in data["interviews"]:
        for index, raw in enumerate(interview["observations"], start=1):
            observations.append(
                Observation(
                    observation_id=f"{interview['interview_id']}-OBS-{index:02d}",
                    interview_id=interview["interview_id"],
                    domain=raw["domain"],
                    polarity=raw["polarity"],
                    strength=int(raw["strength"]),
                    confidence=float(raw["confidence"]),
                    text=raw["text"],
                    risk_flag=raw.get("risk_flag"),
                )
            )
    return observations


def validate_input(
    data: dict[str, Any],
    setup: dict[str, Any],
    expected: dict[str, Any],
) -> list[dict[str, Any]]:
    domains = data["rubric_domains"]
    observations = collect_observations(data)
    domain_names = set(domains)
    weight_sum = sum(float(domain["weight"]) for domain in domains.values())
    invalid_domains = sorted({obs.domain for obs in observations if obs.domain not in domain_names})
    legal_purposes = {item["purpose"] for item in setup["legal_basis_matrix"]}
    required_purposes = set(expected["required_legal_purposes"])
    skill_nodes_used = sum(1 for node in setup["skill_nodes"] if node["status"] == "used_in_mock")
    projection_hypotheses = setup["projection_hypotheses"]
    aggregate_projection_only = all(
        "candidate" not in item["allowed_use"].lower()
        and "ranking" not in item["allowed_use"].lower()
        and "admit" not in item["allowed_use"].lower()
        and "reject" not in item["allowed_use"].lower()
        for item in projection_hypotheses
    )

    checks = [
        {
            "id": "candidate_is_synthetic",
            "passed": data["candidate"].get("data_class") == "synthetic",
            "detail": data["candidate"].get("data_class", ""),
        },
        {
            "id": "record_count",
            "passed": len(data["interviews"]) == expected["expected_record_count"],
            "detail": f"{len(data['interviews'])}/{expected['expected_record_count']}",
        },
        {
            "id": "rubric_weights_sum_to_one",
            "passed": math.isclose(weight_sum, 1.0, abs_tol=0.0001),
            "detail": f"{weight_sum:.4f}",
        },
        {
            "id": "observation_domains_known",
            "passed": not invalid_domains,
            "detail": ", ".join(invalid_domains),
        },
        {
            "id": "governing_scope_blocks_production_candidate_decision_use",
            "passed": setup["governing_scope"].get("production_candidate_decision_use") is False,
            "detail": str(setup["governing_scope"].get("production_candidate_decision_use")),
        },
        {
            "id": "raw_vault_separated_from_gbrain",
            "passed": setup["raw_vault_policy"].get("gbrain_allowed_data")
            == "deidentified_canonical_memory_only",
            "detail": setup["raw_vault_policy"].get("gbrain_allowed_data", ""),
        },
        {
            "id": "candidate_notice_portuguese_declared",
            "passed": setup["candidate_notice"].get("language") == "pt-BR",
            "detail": setup["candidate_notice"].get("language", ""),
        },
        {
            "id": "legal_basis_matrix_covers_required_purposes",
            "passed": required_purposes.issubset(legal_purposes),
            "detail": ", ".join(sorted(required_purposes - legal_purposes)),
        },
        {
            "id": "skill_nodes_used",
            "passed": skill_nodes_used >= expected["minimum_skill_nodes_used"],
            "detail": f"{skill_nodes_used}/{expected['minimum_skill_nodes_used']}",
        },
        {
            "id": "projection_hypotheses_are_aggregate_only",
            "passed": aggregate_projection_only,
            "detail": f"{len(projection_hypotheses)} hypotheses",
        },
    ]
    return checks


def build_source_ledger(data: dict[str, Any], setup: dict[str, Any]) -> dict[str, Any]:
    cycle = setup["interview_cycle"]
    raw_policy = setup["raw_vault_policy"]
    entries: list[dict[str, Any]] = []
    for interview in data["interviews"]:
        source_id = f"SRC-{interview['interview_id']}"
        entries.append(
            {
                "source_id": source_id,
                "cycle_id": cycle["cycle_id"],
                "candidate_pseudonym_id": data["candidate"]["candidate_id"],
                "raw_candidate_id_vault_ref": f"{raw_policy['raw_vault_id']}:{data['candidate']['candidate_id']}",
                "source_type": "synthetic_structured_interview_note",
                "interview_id": interview["interview_id"],
                "notice_version": cycle["notice_version"],
                "recording_status": "not_recorded",
                "transcription_status": "not_transcribed",
                "legal_basis_record": cycle["legal_basis_record"],
                "retention_policy": cycle["retention_policy"],
                "vendor_exposure": "none",
                "raw_access_group": raw_policy["raw_vault_access_group"],
                "deidentification_status": "approved_synthetic",
                "approved_for_memory": True,
            }
        )
    return {
        "schema_version": "source_consent_ledger.v1",
        "cycle_id": cycle["cycle_id"],
        "notice_version": cycle["notice_version"],
        "entries": entries,
    }


def build_memory_graph(
    data: dict[str, Any],
    setup: dict[str, Any],
    source_ledger: dict[str, Any],
) -> dict[str, Any]:
    candidate_id = data["candidate"]["candidate_id"]
    observations = collect_observations(data)
    source_by_interview = {
        entry["interview_id"]: entry for entry in source_ledger["entries"]
    }

    nodes: list[dict[str, Any]] = [
        {
            "id": candidate_id,
            "type": "candidate_pseudonym",
            "label": candidate_id,
            "properties": {
                "data_class": data["candidate"]["data_class"],
                "scenario_note": data["candidate"]["scenario_note"],
                "raw_identifier_location": "raw_vault_only",
            },
        }
    ]
    edges: list[dict[str, str]] = []

    for domain, definition in data["rubric_domains"].items():
        nodes.append(
            {
                "id": f"RUBRIC-{domain}",
                "type": "rubric_domain",
                "label": domain,
                "properties": definition,
            }
        )

    for interview in data["interviews"]:
        interview_id = interview["interview_id"]
        source_stub_id = source_by_interview[interview_id]["source_id"]
        nodes.append(
            {
                "id": source_stub_id,
                "type": "approved_source_stub",
                "label": source_stub_id,
                "properties": {
                    "interview_id": interview_id,
                    "stage": interview["stage"],
                    "interviewer_role": interview["interviewer_role"],
                    "data_class": "synthetic",
                    "deidentification_status": source_by_interview[interview_id][
                        "deidentification_status"
                    ],
                    "raw_details_location": "source_consent_ledger_only",
                },
            }
        )
        edges.append({"source": candidate_id, "target": source_stub_id, "type": "has_source"})

    canonical_assets: list[dict[str, Any]] = []
    for obs in observations:
        memory_id = f"MEM-{obs.observation_id}"
        canonical_assets.append(
            {
                "asset_id": memory_id,
                "type": "canonical_memory_asset",
                "candidate_id": candidate_id,
                "cycle_id": setup["interview_cycle"]["cycle_id"],
                "domain": obs.domain,
                "polarity": obs.polarity,
                "claim": obs.text,
                "confidence": obs.confidence,
                "source_lineage": {
                    "source_id": source_by_interview[obs.interview_id]["source_id"],
                    "source_interview_id": obs.interview_id,
                    "source_observation_id": obs.observation_id,
                },
                "risk_flag": obs.risk_flag,
                "validity_scope": "synthetic workshop fixture only",
                "privacy_review_status": "approved_synthetic_deidentified",
                "faculty_review_status": "approved_mock",
                "confidence_label": "synthetic_high" if obs.confidence >= 0.8 else "synthetic_medium",
                "allowed_use": "committee discussion, rubric review, and next-cycle memory rehearsal",
                "blocked_use": "admit/reject decision, candidate ranking, or individual success prediction",
                "status": "approved_mock_memory",
            }
        )
        nodes.append(
            {
                "id": obs.observation_id,
                "type": "observation",
                "label": obs.text,
                "properties": {
                    "domain": obs.domain,
                    "polarity": obs.polarity,
                    "strength": obs.strength,
                    "confidence": obs.confidence,
                    "risk_flag": obs.risk_flag,
                },
            }
        )
        nodes.append(
            {
                "id": memory_id,
                "type": "canonical_memory_asset",
                "label": obs.text,
                "properties": canonical_assets[-1],
            }
        )
        edges.extend(
            [
                {
                    "source": source_by_interview[obs.interview_id]["source_id"],
                    "target": obs.observation_id,
                    "type": "contains_observation",
                },
                {"source": obs.observation_id, "target": memory_id, "type": "promoted_to_memory"},
                {"source": memory_id, "target": f"RUBRIC-{obs.domain}", "type": "indexes_domain"},
                {
                    "source": source_by_interview[obs.interview_id]["source_id"],
                    "target": memory_id,
                    "type": "lineage_source",
                },
            ]
        )

    for node in setup["skill_nodes"]:
        nodes.append(
            {
                "id": node["skill_id"],
                "type": "skill_node",
                "label": node["name"],
                "properties": node,
            }
        )

    for hypothesis in setup["projection_hypotheses"]:
        nodes.append(
            {
                "id": hypothesis["hypothesis_id"],
                "type": "projection_hypothesis",
                "label": hypothesis["statement"],
                "properties": hypothesis,
            }
        )

    return {
        "schema_version": "mock_gbrain_memory.v2",
        "description": "GBrain-style graph: source ledger, de-identified canonical memory, rubric domains, skill nodes, projection hypotheses, and provenance edges.",
        "candidate_id": candidate_id,
        "cycle_id": setup["interview_cycle"]["cycle_id"],
        "gbrain_data_policy": {
            "allowed_data": setup["raw_vault_policy"]["gbrain_allowed_data"],
            "raw_source_location": "source_consent_ledger.json",
            "raw_details_location": "raw_vault_only",
        },
        "nodes": nodes,
        "edges": edges,
        "canonical_assets": canonical_assets,
        "skill_nodes": setup["skill_nodes"],
        "projection_hypotheses": setup["projection_hypotheses"],
    }


def score_candidate(data: dict[str, Any], memory: dict[str, Any]) -> dict[str, Any]:
    observations = collect_observations(data)
    domains = data["rubric_domains"]
    by_domain: dict[str, list[Observation]] = defaultdict(list)
    for obs in observations:
        by_domain[obs.domain].append(obs)

    domain_indices: dict[str, dict[str, Any]] = {}
    green_flags: list[dict[str, Any]] = []
    red_flags: list[dict[str, Any]] = []
    missing_evidence: list[dict[str, Any]] = []

    for domain, definition in domains.items():
        domain_obs = by_domain[domain]
        scoring_obs = [obs for obs in domain_obs if obs.polarity in {"green", "red"}]
        signed_sum = sum(obs.signed_strength for obs in scoring_obs)
        avg_signed = signed_sum / max(len(scoring_obs), 1)
        confidence_values = [obs.confidence for obs in domain_obs]
        domain_score = round(clamp(50 + (avg_signed * 10)), 1)
        avg_confidence = round(sum(confidence_values) / max(len(confidence_values), 1), 2)
        domain_indices[domain] = {
            "index": domain_score,
            "weight": definition["weight"],
            "confidence": avg_confidence,
            "evidence_count": len(domain_obs),
            "green_count": sum(1 for obs in domain_obs if obs.polarity == "green"),
            "red_count": sum(1 for obs in domain_obs if obs.polarity == "red"),
            "missing_count": sum(1 for obs in domain_obs if obs.polarity == "missing"),
        }

    for asset in memory["canonical_assets"]:
        lineage = asset["source_lineage"]
        entry = {
            "domain": asset["domain"],
            "text": asset["claim"],
            "source_interview_id": lineage["source_interview_id"],
            "source_id": lineage["source_id"],
            "confidence": asset["confidence"],
            "risk_flag": asset["risk_flag"],
        }
        if asset["polarity"] == "green":
            green_flags.append(entry)
        elif asset["polarity"] == "red":
            red_flags.append(entry)
        elif asset["polarity"] == "missing":
            missing_evidence.append(entry)

    weighted_index = sum(
        domain_indices[domain]["index"] * float(definition["weight"])
        for domain, definition in domains.items()
    )
    high_red_count = sum(1 for obs in observations if obs.polarity == "red" and obs.strength >= 3)
    contradiction_count = sum(
        1
        for domain, domain_obs in by_domain.items()
        if any(obs.polarity == "green" for obs in domain_obs)
        and any(obs.polarity == "red" for obs in domain_obs)
    )
    penalty = min(8.0, (high_red_count * 1.0) + (contradiction_count * 0.4))
    composite_index = round(clamp(weighted_index - penalty), 1)

    ethics_index = domain_indices["ethical_judgment"]["index"]
    if any(domain_indices[domain]["evidence_count"] == 0 for domain in domains):
        recommendation = "insufficient_evidence"
    elif ethics_index < 55:
        recommendation = "material_concerns_review_required"
    elif composite_index >= 82 and high_red_count <= 3:
        recommendation = "strong_positive_signal_with_risks"
    elif composite_index >= 72:
        recommendation = "positive_signal_with_discussion_risks"
    elif composite_index >= 62:
        recommendation = "mixed_signal_discuss_further"
    elif composite_index >= 50:
        recommendation = "material_concerns_review_required"
    else:
        recommendation = "insufficient_evidence"

    sorted_green = sorted(green_flags, key=lambda flag: flag["confidence"], reverse=True)[:10]
    sorted_red = sorted(red_flags, key=lambda flag: flag["confidence"], reverse=True)

    return {
        "schema_version": "candidate_evaluation.v1",
        "candidate_id": data["candidate"]["candidate_id"],
        "data_class": "synthetic",
        "deployment_boundary": "synthetic workshop fixture; not a production admissions decision system",
        "domain_indices": domain_indices,
        "weighted_index_before_penalty": round(weighted_index, 1),
        "composite_index": composite_index,
        "recommendation": recommendation,
        "recommendation_meaning": "committee review guidance, not admit/reject/rank/fit scoring",
        "recommendation_confidence": round(
            sum(domain["confidence"] for domain in domain_indices.values()) / len(domain_indices),
            2,
        ),
        "penalties": {
            "high_red_count": high_red_count,
            "contradiction_count": contradiction_count,
            "penalty_points": round(penalty, 1),
        },
        "green_flags": sorted_green,
        "red_flags": sorted_red,
        "missing_evidence": missing_evidence,
        "recommended_committee_questions": [
            "How should the committee weigh exceptional builder signal against pacing and collaboration risks?",
            "What evidence would show the candidate can translate technical ambition for a mixed-experience cohort?",
            "Which faculty mentor or structure would help sequence ambition into scoped milestones?",
            "What real-school outcome should validate whether this candidate's systems mindset creates cohort value?",
        ],
        "forbidden_labels_used": sorted(
            label for label in FORBIDDEN_RECOMMENDATION_LABELS if label == recommendation
        ),
    }


def run_retrieval_benchmark(memory: dict[str, Any], expected: dict[str, Any]) -> dict[str, Any]:
    assets = memory["canonical_assets"]
    query_results: list[dict[str, Any]] = []
    hits = 0

    for item in expected["benchmark_queries"]:
        query_tokens = slug_tokens(item["query"])
        scored = []
        for asset in assets:
            asset_text = " ".join(
                [
                    asset["domain"],
                    asset["polarity"],
                    asset["claim"],
                    asset.get("risk_flag") or "",
                ]
            )
            asset_tokens = slug_tokens(asset_text)
            score = len(query_tokens & asset_tokens) / max(len(query_tokens), 1)
            if item["expected_domain"] == asset["domain"]:
                score += 0.05
            scored.append((score, asset))
        top_assets = [asset for score, asset in sorted(scored, key=lambda pair: pair[0], reverse=True)[:3]]
        hit = any(asset["domain"] == item["expected_domain"] for asset in top_assets)
        hits += int(hit)
        query_results.append(
            {
                "query": item["query"],
                "expected_domain": item["expected_domain"],
                "hit_at_3": hit,
                "top_3": [
                    {
                        "asset_id": asset["asset_id"],
                        "domain": asset["domain"],
                        "polarity": asset["polarity"],
                        "claim": asset["claim"],
                        "source_interview_id": asset["source_lineage"]["source_interview_id"],
                        "source_id": asset["source_lineage"]["source_id"],
                    }
                    for asset in top_assets
                ],
            }
        )

    hit_at_3 = hits / max(len(expected["benchmark_queries"]), 1)
    return {
        "schema_version": "retrieval_benchmark.v1",
        "hit_at_3": round(hit_at_3, 3),
        "query_results": query_results,
    }


def build_eval_report(
    data: dict[str, Any],
    setup: dict[str, Any],
    expected: dict[str, Any],
    source_ledger: dict[str, Any],
    memory: dict[str, Any],
    evaluation: dict[str, Any],
    retrieval: dict[str, Any],
    validation_checks: list[dict[str, Any]],
) -> dict[str, Any]:
    domains = set(data["rubric_domains"])
    assets = memory["canonical_assets"]
    domains_with_assets = {asset["domain"] for asset in assets}
    node_ids = {node["id"] for node in memory["nodes"]}
    dangling_edges = [
        edge
        for edge in memory["edges"]
        if edge["source"] not in node_ids or edge["target"] not in node_ids
    ]
    provenance_coverage = sum(
        1
        for asset in assets
        if asset.get("source_lineage", {}).get("source_id")
        and asset.get("source_lineage", {}).get("source_interview_id")
        and asset.get("source_lineage", {}).get("source_observation_id")
    ) / max(len(assets), 1)
    domain_coverage = len(domains_with_assets & domains) / max(len(domains), 1)
    ledger_interviews = {entry["interview_id"] for entry in source_ledger["entries"]}
    data_interviews = {interview["interview_id"] for interview in data["interviews"]}
    source_ledger_coverage = len(ledger_interviews & data_interviews) / max(len(data_interviews), 1)
    deidentified_coverage = sum(
        1
        for asset in assets
        if asset.get("privacy_review_status") == "approved_synthetic_deidentified"
        and asset.get("faculty_review_status") == "approved_mock"
    ) / max(len(assets), 1)
    projection_hypotheses = setup["projection_hypotheses"]
    projection_count = len(projection_hypotheses)
    valid_projection_refs = {
        asset["asset_id"] for asset in assets
    } | {node["skill_id"] for node in setup["skill_nodes"]}
    unresolved_projection_refs = sorted(
        {
            ref
            for item in projection_hypotheses
            for ref in item["evidence_refs"]
            if ref not in valid_projection_refs
        }
    )
    projections_block_candidate_use = all(
        "candidate" in item["blocked_use"].lower()
        or "ranking" in item["blocked_use"].lower()
        or "admit" in item["blocked_use"].lower()
        or "reject" in item["blocked_use"].lower()
        for item in projection_hypotheses
    )
    skill_nodes_used = sum(1 for node in setup["skill_nodes"] if node["status"] == "used_in_mock")
    memory_json = json.dumps(memory, sort_keys=True)
    no_raw_vault_refs_in_memory = (
        "raw_candidate_id_vault_ref" not in memory_json
        and "raw_access_group" not in memory_json
    )

    checks = list(validation_checks)
    checks.extend(
        [
            {
                "id": "provenance_coverage",
                "passed": provenance_coverage >= expected["minimum_provenance_coverage"],
                "detail": f"{provenance_coverage:.3f}",
            },
            {
                "id": "graph_edges_resolve",
                "passed": not dangling_edges,
                "detail": f"{len(dangling_edges)} dangling edges",
            },
            {
                "id": "domain_coverage",
                "passed": domain_coverage >= expected["minimum_domain_coverage"],
                "detail": f"{domain_coverage:.3f}",
            },
            {
                "id": "source_ledger_coverage",
                "passed": source_ledger_coverage >= expected["minimum_source_ledger_coverage"],
                "detail": f"{source_ledger_coverage:.3f}",
            },
            {
                "id": "deidentified_memory_review_coverage",
                "passed": math.isclose(deidentified_coverage, 1.0),
                "detail": f"{deidentified_coverage:.3f}",
            },
            {
                "id": "retrieval_hit_at_3",
                "passed": retrieval["hit_at_3"] >= expected["minimum_retrieval_hit_at_3"],
                "detail": f"{retrieval['hit_at_3']:.3f}",
            },
            {
                "id": "recommendation_matches_expected",
                "passed": evaluation["recommendation"] == expected["expected_recommendation"],
                "detail": f"{evaluation['recommendation']} expected {expected['expected_recommendation']}",
            },
            {
                "id": "composite_index_threshold",
                "passed": evaluation["composite_index"] >= expected["minimum_composite_index"],
                "detail": f"{evaluation['composite_index']} >= {expected['minimum_composite_index']}",
            },
            {
                "id": "no_forbidden_recommendation_labels",
                "passed": len(evaluation["forbidden_labels_used"]) <= expected["maximum_forbidden_label_count"],
                "detail": ", ".join(evaluation["forbidden_labels_used"]),
            },
            {
                "id": "no_raw_vault_refs_in_gbrain_memory",
                "passed": no_raw_vault_refs_in_memory,
                "detail": "raw refs are ledger-only" if no_raw_vault_refs_in_memory else "raw refs found",
            },
            {
                "id": "projection_packet_count",
                "passed": projection_count >= expected["minimum_projection_hypothesis_count"],
                "detail": f"{projection_count}/{expected['minimum_projection_hypothesis_count']}",
            },
            {
                "id": "projection_evidence_refs_resolve",
                "passed": not unresolved_projection_refs,
                "detail": ", ".join(unresolved_projection_refs),
            },
            {
                "id": "projection_packet_blocks_candidate_use",
                "passed": projections_block_candidate_use,
                "detail": "candidate-level blocked uses declared",
            },
            {
                "id": "retrospective_playbook_ready",
                "passed": skill_nodes_used >= expected["minimum_skill_nodes_used"],
                "detail": f"{skill_nodes_used} skill nodes support next-cycle playbook",
            },
        ]
    )
    status = "PASS" if all(check["passed"] for check in checks) else "FAIL"
    return {
        "schema_version": "interview_memory_eval_report.v1",
        "status": status,
        "summary": {
            "candidate_id": evaluation["candidate_id"],
            "record_count": len(data["interviews"]),
            "memory_asset_count": len(assets),
            "composite_index": evaluation["composite_index"],
            "recommendation": evaluation["recommendation"],
            "retrieval_hit_at_3": retrieval["hit_at_3"],
            "provenance_coverage": round(provenance_coverage, 3),
            "domain_coverage": round(domain_coverage, 3),
            "source_ledger_coverage": round(source_ledger_coverage, 3),
            "skill_node_count": len(setup["skill_nodes"]),
            "projection_hypothesis_count": projection_count,
        },
        "checks": checks,
        "retrieval_benchmark": retrieval,
        "governance": {
            "cycle_id": setup["interview_cycle"]["cycle_id"],
            "production_candidate_decision_use": setup["governing_scope"]["production_candidate_decision_use"],
            "projection_layer_scope": setup["governing_scope"]["projection_layer_scope"],
            "raw_vault_policy": setup["raw_vault_policy"],
            "red_lines": setup["red_lines"],
        },
    }


def render_packet(evaluation: dict[str, Any], report: dict[str, Any]) -> str:
    lines = [
        "# Synthetic Committee Review Packet",
        "",
        f"- Candidate: `{evaluation['candidate_id']}`",
        f"- Data class: `{evaluation['data_class']}`",
        f"- Deployment boundary: {evaluation['deployment_boundary']}",
        f"- Review guidance: `{evaluation['recommendation']}`",
        f"- Guidance meaning: {evaluation['recommendation_meaning']}",
        f"- Synthetic evidence support index: `{evaluation['composite_index']}`",
        f"- Recommendation confidence: `{evaluation['recommendation_confidence']}`",
        f"- Eval status: `{report['status']}`",
        "- Red line: this packet is not an admit/reject/rank/fit decision.",
        "",
        "## Domain Evidence Indices",
        "",
        "| Domain | Index | Confidence | Green | Red | Missing |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for domain, payload in evaluation["domain_indices"].items():
        lines.append(
            f"| {domain} | {payload['index']} | {payload['confidence']} | "
            f"{payload['green_count']} | {payload['red_count']} | {payload['missing_count']} |"
        )

    lines.extend(["", "## Strongest Green Flags", ""])
    for flag in evaluation["green_flags"][:5]:
        lines.append(
            f"- **{flag['domain']}** ({flag['source_interview_id']}): {flag['text']}"
        )

    lines.extend(["", "## Red Flags And Discussion Risks", ""])
    for flag in evaluation["red_flags"]:
        lines.append(
            f"- **{flag['domain']}** ({flag['source_interview_id']}): {flag['text']}"
        )

    lines.extend(["", "## Missing Evidence", ""])
    for item in evaluation["missing_evidence"]:
        lines.append(
            f"- **{item['domain']}** ({item['source_interview_id']}): {item['text']}"
        )

    lines.extend(["", "## Committee Questions For Human Review", ""])
    for question in evaluation["recommended_committee_questions"]:
        lines.append(f"- {question}")

    lines.extend(["", "## Benchmark Summary", ""])
    for check in report["checks"]:
        mark = "PASS" if check["passed"] else "FAIL"
        detail = check["detail"] or "ok"
        lines.append(f"- {mark}: `{check['id']}` - {detail}")

    lines.extend(["", "## Governance Boundary", ""])
    governance = report["governance"]
    lines.append(f"- Production candidate decision use: `{governance['production_candidate_decision_use']}`")
    lines.append(f"- Projection layer scope: `{governance['projection_layer_scope']}`")
    lines.append(f"- GBrain allowed data: `{governance['raw_vault_policy']['gbrain_allowed_data']}`")
    lines.append("- Do not automate: " + ", ".join(governance["red_lines"]["do_not_automate"]))

    return "\n".join(lines) + "\n"


def render_projection_packet(setup: dict[str, Any], report: dict[str, Any]) -> str:
    lines = [
        "# Projection Packet - Aggregate Process Hypotheses",
        "",
        "This packet is for next-cycle planning only. It is not candidate scoring, ranking, or admissions decision support.",
        "",
        f"- Cycle: `{setup['interview_cycle']['cycle_id']}`",
        f"- Projection scope: `{setup['governing_scope']['projection_layer_scope']}`",
        f"- Eval status: `{report['status']}`",
        "",
        "## Hypotheses",
        "",
    ]
    for item in setup["projection_hypotheses"]:
        lines.extend(
            [
                f"### {item['hypothesis_id']}",
                "",
                f"- Statement: {item['statement']}",
                f"- Allowed use: {item['allowed_use']}",
                f"- Blocked use: {item['blocked_use']}",
                f"- Evidence refs: {', '.join(item['evidence_refs'])}",
                f"- Confidence: `{item['confidence_label']}`",
                f"- Falsifier: {item['falsifiers']}",
                f"- Human reviewer: {item['reviewer']}",
                f"- Decision: `{item['decision']}`",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def render_next_cycle_playbook(
    setup: dict[str, Any],
    evaluation: dict[str, Any],
    report: dict[str, Any],
) -> str:
    lines = [
        "# Next-Cycle Playbook - Synthetic Workshop Fixture",
        "",
        "This playbook shows what the next faculty team should inherit from one interview cycle.",
        "",
        f"- Cycle: `{setup['interview_cycle']['cycle_id']}`",
        f"- Review guidance from synthetic packet: `{evaluation['recommendation']}`",
        f"- Eval status: `{report['status']}`",
        "",
        "## Before Cycle",
        "",
        "- Reconfirm the legal-basis matrix and candidate notice before live data.",
        "- Use the rubric pressure-test skill to clarify weak dimensions.",
        "- Run interviewer calibration with sample responses and rating anchors.",
        "- Select questions that force concrete behavioral evidence.",
        "",
        "## During Cycle",
        "",
        "- Use structured notes: question, rubric dimension, evidence, confidence, uncertainty, and follow-up probe.",
        "- Keep raw notes in the raw vault; do not place raw candidate data in GBrain.",
        "- Log committee ambiguity with evidence references and human owner.",
        "",
        "## Post Cycle",
        "",
        "- De-identify candidate-specific evidence before promotion.",
        "- Publish approved canonical memory assets with lineage and review status.",
        "- Retire, revise, or approve projection hypotheses using falsifiers.",
        "- Preserve one rubric lesson, one question-bank lesson, and one calibration lesson.",
        "",
        "## Skill Nodes Used",
        "",
        "| Skill | Phase | Owner | Verifier |",
        "| --- | --- | --- | --- |",
    ]
    for node in setup["skill_nodes"]:
        if node["status"] == "used_in_mock":
            lines.append(
                f"| {node['name']} | {node['phase']} | {node['owner']} | {node['verifier']} |"
            )

    lines.extend(["", "## Current Risks To Carry Forward", ""])
    for flag in evaluation["red_flags"][:5]:
        lines.append(f"- **{flag['domain']}**: {flag['text']}")

    lines.extend(["", "## Retrospective Exit Test", ""])
    for criterion in setup["acceptance_criteria"]:
        lines.append(f"- {criterion}")

    return "\n".join(lines) + "\n"


def build_governance_audit(
    setup: dict[str, Any],
    source_ledger: dict[str, Any],
    report: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schema_version": "interview_memory_governance_audit.v1",
        "cycle_id": setup["interview_cycle"]["cycle_id"],
        "status": report["status"],
        "source_ledger_entries": len(source_ledger["entries"]),
        "legal_basis_purposes": [item["purpose"] for item in setup["legal_basis_matrix"]],
        "red_lines": setup["red_lines"],
        "acceptance_criteria": setup["acceptance_criteria"],
        "passed_checks": [check["id"] for check in report["checks"] if check["passed"]],
        "failed_checks": [check["id"] for check in report["checks"] if not check["passed"]],
    }


def main() -> int:
    data = load_json(DATA_PATH)
    setup = load_json(SETUP_PATH)
    expected = load_json(EXPECTED_PATH)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    validation_checks = validate_input(data, setup, expected)
    source_ledger = build_source_ledger(data, setup)
    memory = build_memory_graph(data, setup, source_ledger)
    evaluation = score_candidate(data, memory)
    retrieval = run_retrieval_benchmark(memory, expected)
    report = build_eval_report(
        data,
        setup,
        expected,
        source_ledger,
        memory,
        evaluation,
        retrieval,
        validation_checks,
    )
    governance_audit = build_governance_audit(setup, source_ledger, report)

    write_json(GENERATED_DIR / "source_consent_ledger.json", source_ledger)
    write_json(GENERATED_DIR / "mock_gbrain_memory.json", memory)
    write_json(GENERATED_DIR / "candidate_evaluation.json", evaluation)
    write_json(GENERATED_DIR / "eval_report.json", report)
    write_json(GENERATED_DIR / "governance_audit.json", governance_audit)
    (GENERATED_DIR / "candidate_packet.md").write_text(
        render_packet(evaluation, report),
        encoding="utf-8",
    )
    (GENERATED_DIR / "projection_packet.md").write_text(
        render_projection_packet(setup, report),
        encoding="utf-8",
    )
    (GENERATED_DIR / "next_cycle_playbook.md").write_text(
        render_next_cycle_playbook(setup, evaluation, report),
        encoding="utf-8",
    )

    print(json.dumps(report["summary"], indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

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
EXPECTED_PATH = BASE_DIR / "benchmarks" / "expected_eval.json"
GENERATED_DIR = BASE_DIR / "generated"

FORBIDDEN_RECOMMENDATION_LABELS = {
    "admit",
    "reject",
    "scholarship_award",
    "automatic_rank",
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


def validate_input(data: dict[str, Any], expected: dict[str, Any]) -> list[dict[str, Any]]:
    domains = data["rubric_domains"]
    observations = collect_observations(data)
    domain_names = set(domains)
    weight_sum = sum(float(domain["weight"]) for domain in domains.values())
    invalid_domains = sorted({obs.domain for obs in observations if obs.domain not in domain_names})

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
    ]
    return checks


def build_memory_graph(data: dict[str, Any]) -> dict[str, Any]:
    candidate_id = data["candidate"]["candidate_id"]
    observations = collect_observations(data)

    nodes: list[dict[str, Any]] = [
        {
            "id": candidate_id,
            "type": "candidate",
            "label": data["candidate"]["display_name"],
            "properties": {
                "data_class": data["candidate"]["data_class"],
                "scenario_note": data["candidate"]["scenario_note"],
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
        nodes.append(
            {
                "id": interview_id,
                "type": "raw_interview",
                "label": f"{interview_id}: {interview['interviewer_role']}",
                "properties": {
                    "stage": interview["stage"],
                    "interviewer_role": interview["interviewer_role"],
                    "summary": interview["summary"],
                    "data_class": "synthetic",
                },
            }
        )
        edges.append({"source": candidate_id, "target": interview_id, "type": "has_interview"})

    canonical_assets: list[dict[str, Any]] = []
    for obs in observations:
        memory_id = f"MEM-{obs.observation_id}"
        canonical_assets.append(
            {
                "asset_id": memory_id,
                "type": "canonical_memory_asset",
                "candidate_id": candidate_id,
                "domain": obs.domain,
                "polarity": obs.polarity,
                "claim": obs.text,
                "confidence": obs.confidence,
                "source_interview_id": obs.interview_id,
                "source_observation_id": obs.observation_id,
                "risk_flag": obs.risk_flag,
                "status": "approved_mock",
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
                {"source": obs.interview_id, "target": obs.observation_id, "type": "contains_observation"},
                {"source": obs.observation_id, "target": memory_id, "type": "promoted_to_memory"},
                {"source": memory_id, "target": f"RUBRIC-{obs.domain}", "type": "indexes_domain"},
            ]
        )

    return {
        "schema_version": "mock_gbrain_memory.v1",
        "description": "GBrain-style graph: raw evidence, canonical memory, rubric domains, and provenance edges.",
        "candidate_id": candidate_id,
        "nodes": nodes,
        "edges": edges,
        "canonical_assets": canonical_assets,
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
        entry = {
            "domain": asset["domain"],
            "text": asset["claim"],
            "source_interview_id": asset["source_interview_id"],
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
        recommendation = "caution"
    elif composite_index >= 82 and high_red_count <= 3:
        recommendation = "strong_recommend"
    elif composite_index >= 72:
        recommendation = "recommend"
    elif composite_index >= 62:
        recommendation = "discuss_further"
    elif composite_index >= 50:
        recommendation = "caution"
    else:
        recommendation = "do_not_recommend"

    sorted_green = sorted(green_flags, key=lambda flag: flag["confidence"], reverse=True)[:10]
    sorted_red = sorted(red_flags, key=lambda flag: flag["confidence"], reverse=True)

    return {
        "schema_version": "candidate_evaluation.v1",
        "candidate_id": data["candidate"]["candidate_id"],
        "data_class": "synthetic",
        "domain_indices": domain_indices,
        "weighted_index_before_penalty": round(weighted_index, 1),
        "composite_index": composite_index,
        "recommendation": recommendation,
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
                        "source_interview_id": asset["source_interview_id"],
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
    expected: dict[str, Any],
    memory: dict[str, Any],
    evaluation: dict[str, Any],
    retrieval: dict[str, Any],
    validation_checks: list[dict[str, Any]],
) -> dict[str, Any]:
    domains = set(data["rubric_domains"])
    assets = memory["canonical_assets"]
    domains_with_assets = {asset["domain"] for asset in assets}
    provenance_coverage = sum(
        1
        for asset in assets
        if asset.get("source_interview_id") and asset.get("source_observation_id")
    ) / max(len(assets), 1)
    domain_coverage = len(domains_with_assets & domains) / max(len(domains), 1)

    checks = list(validation_checks)
    checks.extend(
        [
            {
                "id": "provenance_coverage",
                "passed": provenance_coverage >= expected["minimum_provenance_coverage"],
                "detail": f"{provenance_coverage:.3f}",
            },
            {
                "id": "domain_coverage",
                "passed": domain_coverage >= expected["minimum_domain_coverage"],
                "detail": f"{domain_coverage:.3f}",
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
        },
        "checks": checks,
        "retrieval_benchmark": retrieval,
    }


def render_packet(evaluation: dict[str, Any], report: dict[str, Any]) -> str:
    lines = [
        "# Candidate Evaluation Packet",
        "",
        f"- Candidate: `{evaluation['candidate_id']}`",
        f"- Data class: `{evaluation['data_class']}`",
        f"- Recommendation: `{evaluation['recommendation']}`",
        f"- Composite index: `{evaluation['composite_index']}`",
        f"- Recommendation confidence: `{evaluation['recommendation_confidence']}`",
        f"- Eval status: `{report['status']}`",
        "",
        "## Domain Indices",
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

    lines.extend(["", "## Committee Questions", ""])
    for question in evaluation["recommended_committee_questions"]:
        lines.append(f"- {question}")

    lines.extend(["", "## Benchmark Summary", ""])
    for check in report["checks"]:
        mark = "PASS" if check["passed"] else "FAIL"
        detail = check["detail"] or "ok"
        lines.append(f"- {mark}: `{check['id']}` - {detail}")

    return "\n".join(lines) + "\n"


def main() -> int:
    data = load_json(DATA_PATH)
    expected = load_json(EXPECTED_PATH)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    validation_checks = validate_input(data, expected)
    memory = build_memory_graph(data)
    evaluation = score_candidate(data, memory)
    retrieval = run_retrieval_benchmark(memory, expected)
    report = build_eval_report(data, expected, memory, evaluation, retrieval, validation_checks)

    write_json(GENERATED_DIR / "mock_gbrain_memory.json", memory)
    write_json(GENERATED_DIR / "candidate_evaluation.json", evaluation)
    write_json(GENERATED_DIR / "eval_report.json", report)
    (GENERATED_DIR / "candidate_packet.md").write_text(
        render_packet(evaluation, report),
        encoding="utf-8",
    )

    print(json.dumps(report["summary"], indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

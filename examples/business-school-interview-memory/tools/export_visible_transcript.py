#!/usr/bin/env python3
"""Export the user-visible parts of a Codex session JSONL file.

The Codex session log contains more than the chat transcript: system messages,
developer instructions, tool calls, tool outputs, skill injections, local
runtime context, and app metadata directives can all appear in the same JSONL.
This exporter intentionally keeps only human-readable user/assistant messages
and skips known injected context blocks by default so the result is suitable for
a public workshop repo.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SKIPPED_USER_PREFIXES = (
    "# AGENTS.md instructions",
    "<skill>",
    "<subagent_notification>",
)

SKIPPED_XML_BLOCKS = (
    ("<oai-mem-citation>", "</oai-mem-citation>"),
)

SKIPPED_DIRECTIVE_PREFIXES = (
    "::archive",
    "::git-",
)


def remove_xml_blocks(text: str) -> str:
    cleaned = text
    for start_marker, end_marker in SKIPPED_XML_BLOCKS:
        while start_marker in cleaned:
            start = cleaned.find(start_marker)
            end = cleaned.find(end_marker, start)
            if end == -1:
                cleaned = cleaned[:start].rstrip()
                break
            end += len(end_marker)
            cleaned = (cleaned[:start] + cleaned[end:]).strip()
    return cleaned


def remove_app_directives(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(SKIPPED_DIRECTIVE_PREFIXES):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def clean_message_text(text: str) -> str:
    return remove_app_directives(remove_xml_blocks(text)).strip()


def extract_text(content: list[dict[str, Any]], role: str) -> str:
    wanted_type = "input_text" if role == "user" else "output_text"
    parts: list[str] = []
    for item in content:
        if item.get("type") == wanted_type:
            text = item.get("text")
            if isinstance(text, str) and text.strip():
                parts.append(text.strip())
    return "\n\n".join(parts).strip()


def iter_visible_messages(
    session_path: Path,
    *,
    include_injected_context: bool,
) -> list[dict[str, str]]:
    messages: list[dict[str, str]] = []
    with session_path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at line {line_number}: {exc}") from exc

            if record.get("type") != "response_item":
                continue

            payload = record.get("payload")
            if not isinstance(payload, dict) or payload.get("type") != "message":
                continue

            role = payload.get("role")
            if role not in {"user", "assistant"}:
                continue

            content = payload.get("content")
            if not isinstance(content, list):
                continue

            text = extract_text(content, role)
            if not text:
                continue

            text = clean_message_text(text)
            if not text:
                continue

            if (
                role == "user"
                and not include_injected_context
                and text.startswith(SKIPPED_USER_PREFIXES)
            ):
                continue

            messages.append(
                {
                    "timestamp": str(record.get("timestamp") or "unknown"),
                    "role": role,
                    "text": text,
                }
            )

    return messages


def render_markdown(
    messages: list[dict[str, str]],
    *,
    source_path: Path,
    include_injected_context: bool,
) -> str:
    mode = (
        "All user/assistant response items were included."
        if include_injected_context
        else (
            "Known Codex-injected context blocks were omitted: AGENTS.md context, "
            "skill bodies, and subagent notifications."
        )
    )
    lines = [
        "# Verbatim Session Transcript - 2026-05-21",
        "",
        "This is a word-for-word export of the human-readable Codex chat turns from the workshop session.",
        "Hidden system/developer instructions, tool calls, tool outputs, and app metadata directives are not exported.",
        mode,
        "",
        f"Source session log: `{source_path}`",
        "Timestamps are UTC.",
        "",
        f"Message count: {len(messages)}",
        "",
        "---",
        "",
    ]

    for index, message in enumerate(messages, start=1):
        role_label = "User" if message["role"] == "user" else "Assistant"
        lines.extend(
            [
                f"## {index}. {role_label} - {message['timestamp']}",
                "",
                message["text"],
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export user-visible user/assistant messages from a Codex JSONL session log."
    )
    parser.add_argument("session_jsonl", type=Path, help="Path to the Codex session JSONL file.")
    parser.add_argument(
        "--output",
        type=Path,
        help="Markdown output path. If omitted, writes to stdout.",
    )
    parser.add_argument(
        "--include-injected-context",
        action="store_true",
        help=(
            "Include injected user-role context blocks such as AGENTS.md context, "
            "skill bodies, and subagent notifications. Avoid this for public exports."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    messages = iter_visible_messages(
        args.session_jsonl,
        include_injected_context=args.include_injected_context,
    )
    output = render_markdown(
        messages,
        source_path=args.session_jsonl,
        include_injected_context=args.include_injected_context,
    )

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        print(f"Wrote {len(messages)} messages to {args.output}")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()

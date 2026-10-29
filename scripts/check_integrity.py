#!/usr/bin/env python3
"""Dependency-free offline repository checks. Does not verify credentials."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]\n]*\]\((?:<([^>]+)>|([^\s)]+))")
EXPECTED_OUTCOMES = {
    "completion_certificate",
    "professional_certificate",
    "digital_badge",
    "diploma",
    "award",
    "participation_record",
    "exam_voucher",
    "training_credit",
    "other_official_recognition",
    "other_official_benefit",
}
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def check_markdown() -> tuple[int, int]:
    files = links = 0
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        files += 1
        body = path.read_text(encoding="utf-8")
        for match in LINK.finditer(body):
            destination = match.group(1) or match.group(2)
            if destination.startswith(("#", "//")):
                continue
            url = urlsplit(destination)
            if url.scheme or url.netloc:
                continue
            relative = unquote(url.path)
            if not relative:
                continue
            links += 1
            target = (path.parent / relative).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                fail(f"{path.relative_to(ROOT)}: broken local link {destination}")
    return files, links


def check_json() -> int:
    files = list(ROOT.rglob("*.json"))
    for path in files:
        if ".git" in path.parts:
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as exc:
            fail(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    schema = ROOT / "catalog/schema/course.schema.json"
    try:
        obj = json.loads(schema.read_text(encoding="utf-8"))
        actual = set(obj["$defs"]["outcome"]["properties"]["type"]["enum"])
        if actual != EXPECTED_OUTCOMES:
            fail("Catalog schema: official outcome types differ from the documented ten")
        if obj["properties"]["learning"]["properties"]["free"].get("const") is not True:
            fail("Catalog schema: required free learning condition changed")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        fail(f"Catalog schema: cannot check expected fields: {exc}")
    return len(files)


def check_banner_and_languages() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in ("## Русский", "## Українська", "## 简体中文", "**Languages:** English"):
        if token not in readme:
            fail(f"README missing translation marker: {token}")
    banner = ROOT / "assets/open-it-learning-banner.svg"
    if "assets/open-it-learning-banner.svg" not in readme:
        fail("README does not embed the maintained banner")
    try:
        svg = ElementTree.parse(banner).getroot()
        if svg.tag.rsplit("}", 1)[-1] != "svg":
            fail("Banner is not an SVG root element")
        for node in svg.iter():
            if node.tag.rsplit("}", 1)[-1] in {"script", "foreignObject", "image"}:
                fail("Banner contains embedded or executable external content")
            if any(k.rsplit("}", 1)[-1].lower().startswith("on") for k in node.attrib):
                fail("Banner contains an event handler")
    except (OSError, ElementTree.ParseError) as exc:
        fail(f"Cannot parse banner SVG: {exc}")


def main() -> int:
    md_files, local_links = check_markdown()
    json_files = check_json()
    check_banner_and_languages()
    print(f"Checked {md_files} Markdown files, {local_links} local links, {json_files} JSON files, ten outcome types and banner XML.")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Repository checks passed. This is not semantic credential verification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

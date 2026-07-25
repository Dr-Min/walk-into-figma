#!/usr/bin/env python3
"""Repository-level checks not covered by skill-creator quick_validate.py."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = ROOT / "skills"
EXPECTED = {
    "walk-into-figma",
    "product-discovery-prd",
    "ui-screen-spec",
    "ui-mockup-review",
    "figma-product-builder",
    "figma-handoff-audit",
}


def fail(message: str) -> None:
    print(f"[ERROR] {message}")
    raise SystemExit(1)


actual = {path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()}
missing = EXPECTED - actual
unexpected = actual - EXPECTED
if missing:
    fail(f"Missing skill directories: {', '.join(sorted(missing))}")
if unexpected:
    fail(f"Unexpected skill directories: {', '.join(sorted(unexpected))}")

for skill_name in sorted(EXPECTED):
    skill_dir = SKILLS_ROOT / skill_name
    skill_md = skill_dir / "SKILL.md"
    agent_yaml = skill_dir / "agents" / "openai.yaml"
    if not skill_md.is_file():
        fail(f"{skill_name}: SKILL.md not found")
    if not agent_yaml.is_file():
        fail(f"{skill_name}: agents/openai.yaml not found")

    text = skill_md.read_text(encoding="utf-8")
    if "TODO" in text:
        fail(f"{skill_name}: TODO placeholder remains")
    if len(text.splitlines()) >= 500:
        fail(f"{skill_name}: SKILL.md must stay below 500 lines")

    for relative in re.findall(r"\]\((references/[^)#]+)\)", text):
        target = skill_dir / relative
        if not target.is_file():
            fail(f"{skill_name}: broken reference link {relative}")

    try:
        metadata = yaml.safe_load(agent_yaml.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"{skill_name}: invalid agents/openai.yaml: {exc}")
    if not isinstance(metadata, dict):
        fail(f"{skill_name}: agents/openai.yaml must be a mapping")

    interface = metadata.get("interface")
    policy = metadata.get("policy")
    if not isinstance(interface, dict):
        fail(f"{skill_name}: interface metadata is missing")
    if not isinstance(policy, dict):
        fail(f"{skill_name}: policy metadata is missing")

    display_name = interface.get("display_name")
    short_description = interface.get("short_description")
    default_prompt = interface.get("default_prompt")
    if not isinstance(display_name, str) or not display_name.strip():
        fail(f"{skill_name}: display_name is missing")
    if not isinstance(short_description, str) or not 25 <= len(short_description) <= 64:
        fail(f"{skill_name}: short_description must contain 25-64 characters")
    if not isinstance(default_prompt, str) or f"${skill_name}" not in default_prompt:
        fail(f"{skill_name}: default_prompt must mention ${skill_name}")
    expected_implicit = skill_name == "walk-into-figma"
    if policy.get("allow_implicit_invocation") is not expected_implicit:
        fail(
            f"{skill_name}: allow_implicit_invocation must be "
            f"{str(expected_implicit).lower()}"
        )

for required in ("README.md", "README.ko.md", "LICENSE"):
    readme = ROOT / required
    if not readme.is_file():
        fail(f"Missing repository documentation: {required}")
    text = readme.read_text(encoding="utf-8")
    for relative in re.findall(r"\]\(([^)]+)\)", text):
        if relative.startswith(("http://", "https://", "#", "<")):
            continue
        if not (ROOT / relative).is_file():
            fail(f"{required}: broken local link {relative}")

for path in SKILLS_ROOT.glob("*/README*"):
    fail(f"README files are not allowed inside skill folders: {path}")

for required_script in (
    "scripts/install.sh",
    "scripts/validate-all.sh",
    "scripts/package.sh",
    "scripts/check_repo.py",
    "scripts/check_archive.py",
):
    if not (ROOT / required_script).is_file():
        fail(f"Missing repository script: {required_script}")

required_contracts = {
    "walk-into-figma/SKILL.md": (
        "staged review mode",
        "Require the PRD completion gate",
        "Narrate major progress",
    ),
    "product-discovery-prd/SKILL.md": (
        "PRD STATUS: 100% COMPLETE",
        "PRD STATUS: NOT COMPLETE",
        "explicit deferral",
    ),
    "ui-screen-spec/SKILL.md": ("every interactive control maps to a result",),
    "ui-mockup-review/SKILL.md": (
        "ImageGen",
        "AI DRAFT — VISUAL CONCEPT",
        "APPROVED VISUAL REFERENCE",
    ),
    "figma-product-builder/SKILL.md": (
        "authenticated account identity",
        "[SPEC ONLY]",
        "figma-build-manifest.json",
    ),
    "figma-handoff-audit/SKILL.md": (
        "Never accept a `BLOCKER`",
        "PROTOTYPED",
        "NOT READY",
    ),
}

for relative, phrases in required_contracts.items():
    text = (SKILLS_ROOT / relative).read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            fail(f"{relative}: required behavior contract is missing: {phrase}")

print("[OK] Repository contract is valid")

#!/usr/bin/env python3
"""Validate a packaged walk-into-figma tar archive against the source tree."""

from __future__ import annotations

import sys
import tarfile
from hashlib import sha256
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
SKILLS = {
    "walk-into-figma",
    "product-discovery-prd",
    "ui-screen-spec",
    "ui-mockup-review",
    "figma-product-builder",
    "figma-handoff-audit",
}
CACHE_DIRECTORIES = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".cache",
    ".tox",
    ".nox",
    ".venv",
    "venv",
    "node_modules",
}
CACHE_FILES = {".coverage", "coverage.xml"}


def fail(message: str) -> None:
    print(f"[ERROR] {message}")
    raise SystemExit(1)


def normalize(name: str) -> str:
    while name.startswith("./"):
        name = name[2:]
    return name.rstrip("/")


def excluded(relative: Path) -> bool:
    parts = relative.parts
    name = relative.name
    return (
        not parts
        or parts[0] in {".git", "dist"}
        or ".git" in parts
        or any(part in CACHE_DIRECTORIES for part in parts)
        or name == ".DS_Store"
        or name.startswith("._")
        or name.endswith(".pyc")
        or name in CACHE_FILES
    )


if len(sys.argv) != 2:
    fail("Usage: check_archive.py ARCHIVE")

archive = Path(sys.argv[1]).resolve()
if not archive.is_file():
    fail(f"Archive not found: {archive}")

try:
    handle = tarfile.open(archive, "r:gz")
    members = handle.getmembers()
except (tarfile.TarError, OSError) as exc:
    fail(f"Cannot read archive: {exc}")

actual_files: dict[str, str] = {}
seen_members: set[str] = set()
for member in members:
    name = normalize(member.name)
    path = PurePosixPath(name)
    if member.name.startswith("/") or ".." in path.parts:
        fail(f"Unsafe archive member: {member.name}")
    if name in seen_members:
        fail(f"Duplicate archive member: {member.name}")
    seen_members.add(name)
    if (
        any(part in CACHE_DIRECTORIES for part in path.parts)
        or path.name == ".DS_Store"
        or path.name.startswith("._")
        or path.name.endswith(".pyc")
        or path.name in CACHE_FILES
        or (path.parts and path.parts[0] == "dist")
    ):
        fail(f"Runtime or AppleDouble artifact in archive: {member.name}")

    if not (member.isfile() or member.isdir()):
        fail(f"Unsupported archive member type: {member.name}")

    if member.isfile():
        extracted = handle.extractfile(member)
        if extracted is None:
            fail(f"Cannot read archive member: {member.name}")
        actual_files[name] = sha256(extracted.read()).hexdigest()

handle.close()

expected_files = {
    path.relative_to(ROOT).as_posix(): sha256(path.read_bytes()).hexdigest()
    for path in ROOT.rglob("*")
    if path.is_file() and not excluded(path.relative_to(ROOT))
}

missing = expected_files.keys() - actual_files.keys()
unexpected = actual_files.keys() - expected_files.keys()
if missing:
    fail(f"Archive is missing source files: {', '.join(sorted(missing))}")
if unexpected:
    fail(f"Archive contains unexpected files: {', '.join(sorted(unexpected))}")

changed = {
    name
    for name, digest in expected_files.items()
    if actual_files.get(name) != digest
}
if changed:
    fail(f"Archive file content differs from source: {', '.join(sorted(changed))}")

skill_files = {
    f"skills/{skill}/SKILL.md"
    for skill in SKILLS
}
if not skill_files.issubset(actual_files.keys()):
    fail("Archive does not contain all six SKILL.md files")

print(f"[OK] Archive matches source ({len(actual_files)} files)")

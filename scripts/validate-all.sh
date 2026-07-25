#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VALIDATOR="${CODEX_HOME:-${HOME}/.codex}/skills/.system/skill-creator/scripts/quick_validate.py"

if [[ ! -f "${VALIDATOR}" ]]; then
  printf 'skill-creator validator not found: %s\n' "${VALIDATOR}" >&2
  exit 1
fi

skills=(
  walk-into-figma
  product-discovery-prd
  ui-screen-spec
  ui-mockup-review
  figma-product-builder
  figma-handoff-audit
)

for skill in "${skills[@]}"; do
  python3 "${VALIDATOR}" "${ROOT_DIR}/skills/${skill}"
done

python3 "${ROOT_DIR}/scripts/check_repo.py"
printf 'All %s skills passed validation.\n' "${#skills[@]}"

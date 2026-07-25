#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="${ROOT_DIR}/skills"
DEST_DIR="${CODEX_HOME:-${HOME}/.codex}/skills"
MODE="link"

usage() {
  printf 'Usage: %s [--dest PATH] [--copy]\n' "$0"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dest)
      [[ $# -ge 2 ]] || { usage >&2; exit 2; }
      DEST_DIR="$2"
      shift 2
      ;;
    --copy)
      MODE="copy"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

skills=(
  walk-into-figma
  product-discovery-prd
  ui-screen-spec
  ui-mockup-review
  figma-product-builder
  figma-handoff-audit
)

"${ROOT_DIR}/scripts/validate-all.sh"

pending=("__EMPTY__")
already=("__EMPTY__")

# Preflight every destination before creating anything.
for skill in "${skills[@]}"; do
  source_path="${SOURCE_DIR}/${skill}"
  target_path="${DEST_DIR}/${skill}"

  [[ -d "${source_path}" ]] || {
    printf 'Missing source skill: %s\n' "${source_path}" >&2
    exit 1
  }

  if [[ -L "${target_path}" ]]; then
    current_target="$(cd "$(dirname "${target_path}")" && realpath "$(readlink "${target_path}")" 2>/dev/null || true)"
    if [[ "${current_target}" == "${source_path}" ]]; then
      already+=("${skill}")
      continue
    fi
    printf 'Refusing to replace existing link: %s\n' "${target_path}" >&2
    exit 1
  fi

  if [[ -e "${target_path}" ]]; then
    printf 'Refusing to replace existing path: %s\n' "${target_path}" >&2
    exit 1
  fi

  pending+=("${skill}")
done

for skill in "${already[@]}"; do
  [[ "${skill}" == "__EMPTY__" ]] && continue
  printf 'Already installed: %s\n' "${skill}"
done

if [[ ${#pending[@]} -eq 1 ]]; then
  printf 'Installed %s skills to %s\n' "${#skills[@]}" "${DEST_DIR}"
  exit 0
fi

mkdir -p "${DEST_DIR}"
staging_dir="$(mktemp -d "${DEST_DIR}/.walk-into-figma-install.XXXXXX")"
committed=("__EMPTY__")
install_succeeded=0

cleanup() {
  status=$?

  if [[ ${install_succeeded} -ne 1 ]]; then
    for skill in "${committed[@]}"; do
      [[ "${skill}" == "__EMPTY__" ]] && continue
      target_path="${DEST_DIR}/${skill}"
      if [[ -e "${target_path}" || -L "${target_path}" ]]; then
        mv "${target_path}" "${staging_dir}/${skill}" || true
      fi
    done
  fi

  if [[ -d "${staging_dir}" ]]; then
    rm -rf -- "${staging_dir}"
  fi

  exit "${status}"
}
trap cleanup EXIT

for skill in "${pending[@]}"; do
  [[ "${skill}" == "__EMPTY__" ]] && continue
  source_path="${SOURCE_DIR}/${skill}"
  staged_path="${staging_dir}/${skill}"

  if [[ "${MODE}" == "copy" ]]; then
    cp -R "${source_path}" "${staged_path}"
  else
    ln -s "${source_path}" "${staged_path}"
  fi
done

for skill in "${pending[@]}"; do
  [[ "${skill}" == "__EMPTY__" ]] && continue
  staged_path="${staging_dir}/${skill}"
  target_path="${DEST_DIR}/${skill}"
  mv "${staged_path}" "${target_path}"
  committed+=("${skill}")

  if [[ "${MODE}" == "copy" ]]; then
    printf 'Copied: %s\n' "${skill}"
  else
    printf 'Linked: %s\n' "${skill}"
  fi
done

install_succeeded=1
printf 'Installed %s skills to %s\n' "${#skills[@]}" "${DEST_DIR}"

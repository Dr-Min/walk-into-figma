#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="${ROOT_DIR}/dist"

"${ROOT_DIR}/scripts/validate-all.sh"

mkdir -p "${DIST_DIR}"

if [[ -e "${ROOT_DIR}/.git" ]] && git -C "${ROOT_DIR}" rev-parse --short HEAD >/dev/null 2>&1; then
  version="$(date +%Y%m%d)-$(git -C "${ROOT_DIR}" rev-parse --short HEAD)"
else
  version="$(date +%Y%m%d-%H%M%S)"
fi

archive="${DIST_DIR}/walk-into-figma-${version}.tar.gz"
if [[ -e "${archive}" ]]; then
  printf 'Refusing to overwrite existing package: %s\n' "${archive}" >&2
  exit 1
fi

temporary_archive="$(mktemp "${DIST_DIR}/.walk-into-figma-package.XXXXXX")"
package_succeeded=0

cleanup() {
  status=$?
  if [[ ${package_succeeded} -ne 1 && -f "${temporary_archive}" ]]; then
    rm -f -- "${temporary_archive}"
  fi
  exit "${status}"
}
trap cleanup EXIT

COPYFILE_DISABLE=1 tar \
  --exclude='./dist' \
  --exclude='./.git' \
  --exclude='./.DS_Store' \
  --exclude='*/.DS_Store' \
  --exclude='._*' \
  --exclude='*/._*' \
  --exclude='*/__pycache__' \
  --exclude='./__pycache__' \
  --exclude='./__pycache__/*' \
  --exclude='*/.pytest_cache' \
  --exclude='*/.pytest_cache/*' \
  --exclude='./.pytest_cache' \
  --exclude='./.pytest_cache/*' \
  --exclude='*/.mypy_cache' \
  --exclude='*/.mypy_cache/*' \
  --exclude='./.mypy_cache' \
  --exclude='./.mypy_cache/*' \
  --exclude='*/.ruff_cache' \
  --exclude='*/.ruff_cache/*' \
  --exclude='./.ruff_cache' \
  --exclude='./.ruff_cache/*' \
  --exclude='*/.cache' \
  --exclude='*/.cache/*' \
  --exclude='./.cache' \
  --exclude='./.cache/*' \
  --exclude='*/.tox' \
  --exclude='*/.tox/*' \
  --exclude='./.tox' \
  --exclude='./.tox/*' \
  --exclude='*/.nox' \
  --exclude='*/.nox/*' \
  --exclude='./.nox' \
  --exclude='./.nox/*' \
  --exclude='*/.venv' \
  --exclude='*/.venv/*' \
  --exclude='./.venv' \
  --exclude='./.venv/*' \
  --exclude='*/venv' \
  --exclude='*/venv/*' \
  --exclude='./venv' \
  --exclude='./venv/*' \
  --exclude='*/node_modules' \
  --exclude='*/node_modules/*' \
  --exclude='./node_modules' \
  --exclude='./node_modules/*' \
  --exclude='*.pyc' \
  --exclude='*/.coverage' \
  --exclude='*/coverage.xml' \
  -czf "${temporary_archive}" \
  -C "${ROOT_DIR}" .

python3 "${ROOT_DIR}/scripts/check_archive.py" "${temporary_archive}"
mv "${temporary_archive}" "${archive}"
package_succeeded=1
printf 'Created package: %s\n' "${archive}"

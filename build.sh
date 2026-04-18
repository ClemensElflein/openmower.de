#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="${SCRIPT_DIR}/dist"

BASE_URL="${BASE_URL:-https://openmower.de/latest/}"
VERSION="${VERSION:-latest}"

docker build \
    --build-arg "BASE_URL=${BASE_URL}" \
    --build-arg "VERSION=${VERSION}" \
    --output "type=local,dest=${OUTPUT_DIR}" \
    "${SCRIPT_DIR}"

echo "Built to: ${OUTPUT_DIR}"

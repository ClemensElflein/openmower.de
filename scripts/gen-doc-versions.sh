#!/usr/bin/env bash
set -euo pipefail

# --- Resolve paths relative to this script ---

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
OUT="${PROJECT_ROOT}/config/_generated_versions.toml"

DOCS_BASE_URL="${DOCS_BASE_URL:-https://openmower.de/archive}"

mkdir -p "$(dirname "$OUT")"

# --- Get tags + messages ---

# Use a simple custom delimiter ":::"
# refname:short = tag name
# contents:subject = first line of tag message (for annotated tags)
mapfile -t TAG_LINES < <(
  git -C "$PROJECT_ROOT" for-each-ref \
    refs/tags \
    --sort=-creatordate \
    --format='%(refname:short):::%(contents:subject)' \
  || true
)

# Small helper: trim leading/trailing whitespace
trim() {
  local s="$1"
  s="${s#"${s%%[![:space:]]*}"}"  # leading
  s="${s%"${s##*[![:space:]]}"}"  # trailing
  printf '%s' "$s"
}

{
  echo '# AUTO-GENERATED. Do not edit by hand.'
  echo '# Version menu entries for Docsy'
  echo

  # Synthetic "latest" entry pointing to root site
  cat <<EOF
[[params.versions]]
  version = "latest"
  url = "https://openmower.de/"
EOF

  # One entry per git tag
  for line in "${TAG_LINES[@]}"; do
    [[ -z "$line" ]] && continue

    # Split "tag:::message"
    tag="${line%%:::*}"
    msg="${line#*:::}"

    # If delimiter wasn't found, msg == line → treat as "no message"
    if [[ "$msg" == "$line" ]]; then
      msg=""
    fi

    tag="$(trim "$tag")"
    msg="$(trim "$msg")"

    # Skip nonsense / empty tags
    [[ -z "$tag" ]] && continue

    # Display title: prefer message, fallback to tag name
    title="$tag"
    if [[ -n "$msg" ]]; then
      title="$msg"
    fi

    # Escape quotes for TOML
    esc_title=${title//\"/\\\"}
    esc_tag=${tag//\"/\\\"}

    cat <<EOF

[[params.versions]]
  version = "$esc_title"
  url = "${DOCS_BASE_URL}/${esc_tag}/docs"
EOF
  done
} > "$OUT"

#!/usr/bin/env bash
# Deploy situs dari HEAD git. Memakai variabel dari .env (lihat .env.example).
#   tools/deploy.sh preview            -> deploy preview, mencetak URL
#   tools/deploy.sh promote <url>      -> promote preview itu ke produksi (HANYA setelah verifikasi lolos)
# Token tidak pernah dicetak. Tanpa VERCEL_TOKEN, vercel CLI memakai login lokal.
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f .env ] && { set -a; . ./.env; set +a; }
SCOPE="${VERCEL_SCOPE:-sentratech}"
TOKEN_ARGS=(); [ -n "${VERCEL_TOKEN:-}" ] && TOKEN_ARGS=(--token "$VERCEL_TOKEN")
V=("${VERCEL_BIN:-vercel}" ${TOKEN_ARGS[@]+"${TOKEN_ARGS[@]}"} --scope "$SCOPE")
case "${1:-}" in
  preview)
    git diff --quiet && git diff --cached --quiet || { echo "Ada perubahan yang belum di-commit; commit dulu." >&2; exit 1; }
    tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
    git archive HEAD | tar -x -C "$tmp"
    ( cd "$tmp" && VERCEL_ORG_ID="${VERCEL_ORG_ID:?}" VERCEL_PROJECT_ID="${VERCEL_PROJECT_ID:?}" "${V[@]}" deploy --yes ) | tail -1
    ;;
  promote)
    url="${2:?usage: tools/deploy.sh promote <preview-url>}"
    VERCEL_ORG_ID="${VERCEL_ORG_ID:?}" VERCEL_PROJECT_ID="${VERCEL_PROJECT_ID:?}" "${V[@]}" promote "$url" --yes --timeout 3m
    ;;
  *) echo "usage: tools/deploy.sh preview | promote <url>" >&2; exit 2 ;;
esac

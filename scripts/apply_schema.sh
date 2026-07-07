#!/usr/bin/env bash
set -euo pipefail
# Apply db/schema.sql to DATABASE_URL (Postgres connection string in env)
if [ -z "${DATABASE_URL:-}" ]; then
  echo "Error: DATABASE_URL environment variable is not set. Set it as a repository secret in GitHub (Settings → Secrets)."
  exit 1
fi

echo "Applying schema to database..."
psql "$DATABASE_URL" -f db/schema.sql

echo "Schema applied."

#!/usr/bin/env bash
set -euo pipefail
# Deploy helper for Streamlit Community Cloud
# This script does not perform an interactive deploy; it checks for STREAMLIT_API_KEY and prints next steps.

REPO_FULL="bezaleel90/skills-without-borders"
BRANCH="master"
MAIN_FILE="streamlit_app.py"

if [ -z "${STREAMLIT_API_KEY:-}" ]; then
  echo "STREAMLIT_API_KEY is not set. To enable automated deploy, add STREAMLIT_API_KEY as a repository secret in GitHub (Settings → Secrets)."
  echo "Alternatively, deploy via Streamlit Cloud UI: https://streamlit.io/cloud -> New app -> Connect GitHub -> select repo and branch -> set main file: ${MAIN_FILE}."
  exit 0
fi

echo "STREAMLIT_API_KEY is set. Automated deploy to Streamlit Cloud requires using Streamlit's REST API or CLI which may require additional configuration."

echo "Recommended: Go to Streamlit Cloud dashboard and connect the GitHub repo: ${REPO_FULL}, branch: ${BRANCH}, main file: ${MAIN_FILE}."

echo "If you want a fully automated REST-based deploy, provide the Streamlit Cloud API details or confirm to proceed."
exit 0

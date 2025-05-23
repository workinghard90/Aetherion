#!/bin/bash

echo "Running security check..."

if [ -f "requirements.txt" ]; then
  echo "→ Checking Python dependencies for known vulnerabilities..."
  pip install safety &>/dev/null
  safety check || true
else
  echo "requirements.txt not found, skipping Python security check."
fi

echo "→ Checking for secrets in backend..."
grep -iR --exclude-dir=.git --exclude=venv "API_KEY\|SECRET\|TOKEN" . || echo "No obvious secrets detected."

echo "Security check complete."

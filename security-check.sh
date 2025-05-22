#!/bin/bash

echo "Running AetherionAI Security Check..."

# Scan for common secret keywords in the entire project
grep -riEn --color=always \
  -e 'api[_-]?key' \
  -e 'secret[_-]?key' \
  -e 'password' \
  -e 'access[_-]?token' \
  -e 'client[_-]?secret' \
  . > security_scan_results.txt

if [[ -s security_scan_results.txt ]]; then
  echo "--------------------------------------------------"
  echo " WARNING: Potential secrets found in codebase!"
  echo " Review security_scan_results.txt before committing."
  echo "--------------------------------------------------"
  exit 1
else
  echo "Security scan passed. No secrets detected."
  rm -f security_scan_results.txt
fi

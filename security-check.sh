#!/bin/bash

echo "Running security checks..."

# Search for sensitive strings
grep -rniE 'api[_-]?key|secret[_-]?key|password|access[_-]?token|client[_-]?secret' ./ > security_scan_results.txt

# Warn if .env exists
if [ -f .env ]; then
  echo ".env file exists. Ensure it is excluded from version control."
fi

echo "Security scan complete. Results saved to security_scan_results.txt"

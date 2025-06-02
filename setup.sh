#!/usr/bin/env bash
#
# Aetherion/setup.sh
#
# Quick bootstrap for local development.  Make sure this is executable:
#   chmod +x setup.sh
#
# Run this script from the project root (Aetherion/):
#   ./setup.sh

echo "🌀 Bootstrapping Aetherion monorepo for local development 🌀"

# 1) Backend: create virtualenv & install Python deps
cd backend || exit 1
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  echo "Created Python virtualenv in backend/.venv"
fi
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Installed backend requirements"

# 2) Create a local SQLite database (if none)
echo "Initializing database..."
flask db init 2>/dev/null || true
flask db migrate -m "Initial" 2>/dev/null || true
flask db upgrade

# 3) Frontend: install Node dependencies
cd ../frontend || exit 1
npm install
echo "Installed frontend dependencies"

echo "✅ Setup complete!  To run locally:"
echo "- In one terminal: cd backend && source .venv/bin/activate && flask run"
echo "- In another: cd frontend && expo start"

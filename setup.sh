#!/bin/bash

echo "=== Setting up AetherionAI Monorepo ==="

# --- Frontend Setup ---
echo "→ Installing frontend dependencies..."
cd apps/aetherion-mobile || exit 1
yarn install

echo "→ Fixing 'main' field in package.json..."
# Replace any existing main field with the correct Expo entry
sed -i.bak 's/"main": *".*"/"main": "node_modules\/expo\/AppEntry.js"/' package.json

# --- Backend Setup ---
echo "→ Installing backend dependencies..."
cd ../../services/backend || exit 1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

git add apps/aetherion-mobile/package.json
git commit -m "Fix JSON syntax in package.json for Netlify deploy"
git push

echo "✅ Setup complete!"
echo ""
echo "Run frontend:  yarn start:expo"
echo "Run backend:   yarn start:backend"

#!/bin/bash

echo "=== Setting up AetherionAI Monorepo ==="

# --- Frontend Setup ---
echo "→ Installing frontend dependencies..."
cd apps/aetherion-mobile || exit 1
yarn install

echo "→ Configuring Expo..."
npx expo customize babel.config.js

echo "→ Ensuring correct entry point in package.json..."
sed -i.bak 's/"main": *".*"/"main": "node_modules\/expo\/AppEntry.js"/' package.json

echo "→ Installing Expo web support..."
npx expo install react-dom react-native-web react-native-gesture-handler

echo "→ Cleaning config files..."
rm -f app.config.py
git rm app.config.py || true
git add app.config.js
git commit -m "Ensure correct app.config.js for Netlify"
git push

# --- Backend Setup ---
echo "→ Installing backend dependencies..."
cd ../../services/backend || exit 1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

echo "→ Running security checks..."
bash security-check.sh && git add . && git commit -m "Safe commit"

yarn check:secrets

echo "→ Committing backend API update..."
git add app.py
git commit -m "Add root route to show API status at /"
git push

echo ""
echo "✅ Setup complete!"
echo ""
echo "Run frontend:  yarn start:expo"
echo "Run backend:   yarn start:backend"

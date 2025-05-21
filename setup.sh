#!/bin/bash

echo "=== Setting up AetherionAI Monorepo ==="

# --- Frontend Setup ---
echo "→ Installing frontend dependencies..."
cd apps/aetherion-mobile || exit 1
yarn install

npx expo customize babel.config.js

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

cd apps/aetherion-mobile
rm -f app.config.py  # Delete any stray file
git rm app.config.py || true
git add app.config.js
git commit -m "Ensure correct app.config.js for Netlify"
git push

npx expo install react-dom react-native-web react-native-gesture-handler

git add services/backend/app.py
git commit -m "Add root route to show API status at /"
git push

echo "✅ Setup complete!"
echo ""
echo "Run frontend:  yarn start:expo"
echo "Run backend:   yarn start:backend"

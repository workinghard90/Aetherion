#!/bin/bash

echo "=== Setting up AetherionAI Monorepo ==="

# --- Frontend Setup ---
echo "→ Installing frontend dependencies..."
cd apps/aetherion-mobile || exit 1
yarn install

echo "→ Configuring Expo..."
npx expo customize babel.config.js

echo "→ Ensuring correct entry point in package.json..."
sed -i.bak 's/"main": *".*"/"main": "node_modules\\/expo\\/AppEntry.js"/' package.json

echo "→ Installing Expo web support..."
npx expo install react-dom react-native-web react-native-gesture-handler

echo "→ Cleaning config files..."
rm -f app.config.py
git rm --cached app.config.py 2>/dev/null || true
git add app.config.js
git commit -m "Ensure correct app.config.js for Netlify" || true
git push

# --- Backend Setup ---
echo "→ Installing backend dependencies..."
cd ../../services/backend || exit 1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

echo "→ Running security checks..."
bash security-check.sh && git add . && git commit -m "Safe commit" || true

# Only run yarn in frontend, so skip `yarn check:secrets` if not defined
cd ../../apps/aetherion-mobile
if yarn run check:secrets; then
  echo "✓ Secrets check passed."
else
  echo "⚠️  Secrets check failed or not defined."
fi

echo "→ Committing backend API update..."
cd ../../services/backend
git add app.py
git commit -m "Add root route to show API status at /" || true
git push

echo ""
echo "✅ Setup complete!"
echo ""
echo "Run frontend:  cd apps/aetherion-mobile && yarn start"
echo "Run backend:   cd services/backend && source venv/bin/activate && flask run"

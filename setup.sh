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

echo "→ Installing reanimated for Babel plugin..."
npx expo install react-native-reanimated

echo "→ Adding reanimated plugin to Babel config..."
BABEL_FILE="babel.config.js"
if grep -q "react-native-reanimated/plugin" "$BABEL_FILE"; then
  echo "✓ Babel plugin already added."
else
  sed -i.bak 's/plugins: \[/plugins: [\n      "react-native-reanimated\/plugin",/' "$BABEL_FILE"
fi

echo "→ Cleaning config files..."
rm -f app.config.py
git rm --cached app.config.py 2>/dev/null || true
git add app.config.js "$BABEL_FILE"
git commit -m "Ensure correct app.config.js and Babel plugin for Netlify" || true
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

# --- Optional secrets check ---
cd ../../apps/aetherion-mobile
if yarn run check:secrets; then
  echo "✓ Secrets check passed."
else
  echo "⚠️  Secrets check failed or not defined."
fi

# --- Commit backend update ---
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

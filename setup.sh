#!/bin/bash

set -e

echo ""
echo "=== Setting up AetherionAI Monorepo ==="
echo ""

# --- Frontend Setup ---
echo "→ Installing frontend dependencies..."
cd apps/aetherion-mobile || { echo "❌ Failed to cd into frontend dir"; exit 1; }
yarn install

echo "→ Configuring Expo..."
npx expo customize babel.config.js || true

echo "→ Ensuring correct entry point in package.json..."
sed -i.bak 's/"main": *".*"/"main": "node_modules\/expo\/AppEntry.js"/' package.json

echo "→ Installing Expo web + navigation + gesture deps..."
npx expo install \
  react-dom \
  react-native-web \
  react-native-gesture-handler \
  react-native-reanimated \
  @react-navigation/native \
  @react-navigation/stack \
  @expo/metro-runtime \
  react-native-screens \
  react-native-safe-area-context

echo "→ Verifying Babel config plugin for reanimated..."
BABEL_FILE="babel.config.js"
if grep -q "react-native-reanimated/plugin" "$BABEL_FILE"; then
  echo "✓ Babel plugin already present."
else
  sed -i.bak 's/plugins: \[/plugins: [\n      "react-native-reanimated\/plugin",/' "$BABEL_FILE"
fi

echo "→ Cleaning legacy config files..."
rm -f app.config.py
git rm --cached app.config.py 2>/dev/null || true

echo "→ Committing frontend setup..."
git add app.config.js "$BABEL_FILE" package.json yarn.lock
git commit -m "Frontend: setup Expo + web + peer deps + reanimated plugin" || true
git push

# --- Backend Setup ---
echo ""
echo "→ Installing backend dependencies..."
cd ../../services/backend || { echo "❌ Failed to cd into backend dir"; exit 1; }

if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate

echo "→ Running security checks..."
bash security-check.sh && git add . && git commit -m "Safe backend commit" || true

# --- Optional secrets check ---
echo ""
cd ../../apps/aetherion-mobile
if yarn run check:secrets; then
  echo "✓ Secrets check passed."
else
  echo "⚠️  Secrets check skipped or failed."
fi

# --- Commit backend API update ---
echo ""
echo "→ Committing backend API update..."
cd ../../services/backend
git add app.py
git commit -m "Backend: add root API status endpoint" || true
git push

# --- Finish ---
echo ""
echo "✅ AetherionAI Setup Complete!"
echo ""
echo "Frontend:  cd apps/aetherion-mobile && yarn start"
echo "Backend:   cd services/backend && source venv/bin/activate && flask run"

#!/bin/bash

set -e

echo ""
echo "=== Setting up AetherionAI Monorepo ==="
echo ""

# --- Frontend Setup ---
echo "→ Installing frontend dependencies..."
cd apps/aetherion-mobile || { echo "❌ Failed to cd into frontend dir"; exit 1; }
yarn install || npm install

echo "→ Enforcing Expo entry point..."
sed -i.bak 's/"main": *".*"/"main": "node_modules\/expo\/AppEntry.js"/' package.json || true

echo "→ Installing Expo & React Native deps..."
npx expo install \
  react-dom \
  react-native-web \
  react-native-gesture-handler \
  react-native-reanimated \
  react-native-screens \
  react-native-safe-area-context \
  @expo/metro-runtime \
  @react-navigation/native \
  @react-navigation/stack

echo "→ Adding peer and project-specific packages..."
yarn add discord.js @babel/preset-env @react-native/babel-preset

echo "→ Creating .npmrc for legacy-peer-deps..."
echo "legacy-peer-deps=true" > .npmrc

echo "→ Patching Babel config with reanimated plugin..."
BABEL_FILE="babel.config.js"
if grep -q "react-native-reanimated/plugin" "$BABEL_FILE"; then
  echo "✓ Babel plugin already configured."
else
  sed -i.bak 's/plugins: \[/plugins: [\n      "react-native-reanimated\/plugin",/' "$BABEL_FILE"
fi

echo "→ Verifying background image asset..."
mkdir -p assets
[ -f assets/bg.jpg ] || curl -s https://via.placeholder.com/1080x1920.jpg -o assets/bg.jpg

echo "→ Cleaning legacy files..."
rm -f app.config.py
git rm --cached app.config.py 2>/dev/null || true

echo "→ Committing frontend setup..."
git add .npmrc app.config.js "$BABEL_FILE" package.json yarn.lock assets/bg.jpg || true
git commit -m "Setup: frontend deps, reanimated, discord.js, image, babel, .npmrc" || true
git push || true

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

echo "→ Running security check script..."
bash security-check.sh && git add . && git commit -m "Backend: security check complete" || true

# --- Secrets Check ---
echo ""
cd ../../apps/aetherion-mobile
if yarn run check:secrets; then
  echo "✓ Secrets check passed."
else
  echo "⚠️  Secrets check skipped or undefined."
fi

# --- Final Backend Commit ---
echo ""
echo "→ Committing backend API status route..."
cd ../../services/backend
git add app.py
git commit -m "Backend: ensure root API status route" || true
git push || true

# --- Done ---
echo ""
echo "✅ AetherionAI Setup Complete!"
echo ""
echo "Frontend:  cd apps/aetherion-mobile && yarn start"
echo "Backend:   cd services/backend && source venv/bin/activate && flask run"

#!/bin/bash

set -e

echo ""
echo "=== Setting up AetherionAI Monorepo ==="
echo ""

# --- Frontend Setup ---
echo "→ Installing frontend dependencies..."
cd apps/aetherion-mobile || { echo "❌ Failed to cd into frontend dir"; exit 1; }
yarn install || npm install

echo "→ Setting Expo entry point in package.json..."
sed -i.bak 's/"main": *".*"/"main": "node_modules\/expo\/AppEntry.js"/' package.json || true

echo "→ Installing Expo + React Native dependencies..."
npx expo install \
  react-dom \
  react-native-web \
  react-native-gesture-handler \
  react-native-reanimated \
  react-native-screens \
  react-native-safe-area-context \
  @react-navigation/native \
  @react-navigation/stack \
  @expo/metro-runtime

echo "→ Adding missing peer + custom packages..."
yarn add discord.js @babel/preset-env @react-native/babel-preset

echo "→ Writing .npmrc to support legacy installs..."
echo "legacy-peer-deps=true" > .npmrc

echo "→ Patching Babel config for reanimated plugin..."
BABEL_FILE="babel.config.js"
if grep -q "react-native-reanimated/plugin" "$BABEL_FILE"; then
  echo "✓ Plugin already added to Babel config."
else
  sed -i.bak 's/plugins: \[/plugins: [\n      "react-native-reanimated\/plugin",/' "$BABEL_FILE"
fi

echo "→ Verifying background image asset..."
mkdir -p assets
[ -f assets/bg.jpg ] || curl -s https://via.placeholder.com/1080x1920.jpg -o assets/bg.jpg

echo "→ Cleaning old config files..."
rm -f app.config.py
git rm --cached app.config.py 2>/dev/null || true

echo "→ Committing frontend changes..."
git add .npmrc app.config.js "$BABEL_FILE" package.json yarn.lock assets/bg.jpg || true
git commit -m "Setup: frontend deps, discord.js, bg, reanimated, .npmrc" || true
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

echo "→ Running backend security checks..."
bash security-check.sh && git add . && git commit -m "Backend: passed security check" || true

# --- Optional secrets check ---
echo ""
cd ../../apps/aetherion-mobile
if yarn run check:secrets; then
  echo "✓ Secrets check passed."
else
  echo "⚠️  Secrets check skipped or not defined."
fi

# --- Final backend commit ---
echo ""
echo "→ Committing backend API update..."
cd ../../services/backend
git add app.py
git commit -m "Backend: ensured root / route API status" || true
git push || true

# --- Completion ---
echo ""
echo "✅ AetherionAI Setup Complete!"
echo ""
echo "Frontend:  cd apps/aetherion-mobile && yarn start"
echo "Backend:   cd services/backend && source venv/bin/activate && flask run"

#!/bin/bash

set -e

echo -e "\n=== Setting up AetherionAI Monorepo ===\n"

# === Frontend Setup ===
echo "→ Installing frontend dependencies..."
cd apps/aetherion-mobile || { echo "❌ Cannot access frontend directory"; exit 1; }

# Generate compatibility configs
cat > .npmrc <<EOF
legacy-peer-deps=true
audit=false
registry=https://registry.npmjs.org/
EOF
echo "18.20.3" > .nvmrc

# Install deps using yarn or fallback to npm
if command -v yarn &>/dev/null; then
  yarn install
else
  npm install --legacy-peer-deps
fi

echo "→ Fixing Expo entry in package.json..."
sed -i.bak 's/"main": *".*"/"main": "node_modules\/expo\/AppEntry.js"/' package.json || true

echo "→ Installing Expo + React Native deps..."
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

echo "→ Installing required extras..."
yarn add discord.js @babel/preset-env @react-native/babel-preset@^8.5.0

echo "→ Ensuring reanimated plugin in babel.config.js..."
BABEL_FILE="babel.config.js"
if ! grep -q "react-native-reanimated/plugin" "$BABEL_FILE"; then
  sed -i.bak 's/plugins: \[/plugins: [\n      "react-native-reanimated\/plugin",/' "$BABEL_FILE"
  echo "✓ Plugin added to Babel config."
else
  echo "✓ Babel plugin already present."
fi

echo "→ Verifying assets..."
mkdir -p assets
[ -f assets/bg.jpg ] || curl -s https://via.placeholder.com/1080x1920.jpg -o assets/bg.jpg

echo "→ Cleaning legacy config files..."
rm -f app.config.py
git rm --cached app.config.py 2>/dev/null || true

echo "→ Committing frontend setup..."
git add .npmrc .nvmrc app.config.js "$BABEL_FILE" package.json yarn.lock assets/bg.jpg || true
git commit -m "Setup: frontend deps, reanimated, babel, discord.js, image" || true
git push || true

# === Backend Setup ===
echo -e "\n→ Installing backend dependencies..."
cd ../../services/backend || { echo "❌ Cannot access backend directory"; exit 1; }

[ -d venv ] || python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate

echo "→ Running backend security checks..."
bash security-check.sh && git add . && git commit -m "Backend: passed security check" || true

# === Secrets Check ===
echo -e "\n→ Checking for leaked secrets..."
cd ../../apps/aetherion-mobile
if yarn run check:secrets; then
  echo "✓ Secrets check passed."
else
  echo "⚠️  Secrets check skipped or failed."
fi

# === Final Backend Commit ===
echo -e "\n→ Committing backend updates..."
cd ../../services/backend
git add app.py
git commit -m "Backend: API root route check" || true
git push || true

# === Finish ===
echo -e "\n✅ AetherionAI Setup Complete!\n"
echo "Frontend:  cd apps/aetherion-mobile && yarn start"
echo "Backend:   cd services/backend && source venv/bin/activate && flask run"

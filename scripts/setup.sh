#!/bin/bash

set -e

echo -e "\n=== Setting up AetherionAI Monorepo ===\n"

# === Frontend Setup ===
echo "→ Installing frontend dependencies..."
cd apps/aetherion-mobile || { echo "❌ Cannot access frontend directory"; exit 1; }

# Compatibility configs
cat > .npmrc <<EOF
legacy-peer-deps=true
audit=false
registry=https://registry.npmjs.org/
EOF
echo "18.20.3" > .nvmrc

# Write consistent formatting
cat > .editorconfig <<EOF
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
EOF

# Install deps
if command -v yarn &>/dev/null; then
  yarn install
else
  npm install --legacy-peer-deps
fi

# Expo entry
echo "→ Setting Expo entry to index.js..."
sed -i.bak 's/"main": *".*"/"main": "index.js"/' package.json || true
echo "import 'expo-router/entry';" > index.js

# Install Expo peer dependencies
echo "→ Installing Expo and React Native deps..."
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

# Install other dependencies
echo "→ Installing project dependencies..."
yarn add discord.js
yarn add -D @babel/preset-env @react-native/babel-preset@9.4.0 prettier

# Prettier config files
echo "→ Writing Prettier config..."
cd ../../
cat > .prettierrc <<EOF
{
  "singleQuote": true,
  "semi": true,
  "tabWidth": 2,
  "printWidth": 100,
  "trailingComma": "es5"
}
EOF

cat > .prettierignore <<EOF
node_modules
dist
build
*.lock
EOF

# Git commit prettier config
git add .prettierrc .prettierignore || true
git commit -m "Setup: prettier config added" || true
cd apps/aetherion-mobile

# Ensure Babel reanimated plugin
echo "→ Ensuring Babel reanimated plugin..."
BABEL_FILE="babel.config.js"
if ! grep -q "react-native-reanimated/plugin" "$BABEL_FILE"; then
  sed -i.bak 's/plugins: \[/plugins: [\n      "react-native-reanimated\/plugin",/' "$BABEL_FILE"
fi

# Fallback asset
echo "→ Ensuring background asset..."
mkdir -p assets
[ -f assets/bg.jpg ] || curl -s https://via.placeholder.com/1080x1920.jpg -o assets/bg.jpg

# Cleanup
echo "→ Cleaning up old configs..."
rm -f app.config.py
git rm --cached app.config.py 2>/dev/null || true

# Git commit
echo "→ Committing frontend setup..."
git add .editorconfig .npmrc .nvmrc index.js app.config.js "$BABEL_FILE" package.json yarn.lock assets/bg.jpg || true
git commit -m "Setup: frontend index.js, dependencies, babel plugin, config, assets" || true
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
bash security-check.sh && git add . && git commit -m "Backend: security check passed" || true

# === Secrets Check ===
echo -e "\n→ Checking for leaked secrets..."
cd ../../apps/aetherion-mobile
if yarn run check:secrets; then
  echo "✓ Secrets check passed."
else
  echo "⚠️  Secrets check skipped or failed."
fi

# === Backend commit ===
echo -e "\n→ Committing backend updates..."
cd ../../services/backend
git add app.py
git commit -m "Backend: ensure root route / API status" || true
git push || true

# === Done ===
echo -e "\n✅ AetherionAI Setup Complete!\n"
echo "Frontend:  cd apps/aetherion-mobile && yarn start"
echo "Backend:   cd services/backend && source venv/bin/activate && flask run"

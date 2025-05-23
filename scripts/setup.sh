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

# Editor config
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

# Prettier config
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
build
dist
coverage
EOF

# ESLint config
cat > .eslintrc.js <<EOF
module.exports = {
  root: true,
  extends: ['eslint:recommended'],
  env: {
    browser: true,
    node: true,
    es2021: true,
  },
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module',
  },
  rules: {},
};
EOF

# Install deps
if command -v yarn &>/dev/null; then
  yarn install
else
  npm install --legacy-peer-deps
fi

# Main entry
echo "→ Setting Expo entry to index.js..."
sed -i.bak 's/"main": *".*"/"main": "index.js"/' package.json || true
echo "import 'expo-router/entry';" > index.js

# Install project & peer dependencies
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

yarn add discord.js
yarn add -D @babel/preset-env @react-native/babel-preset@9.3.0 prettier eslint husky lint-staged

# Reanimated Babel plugin
BABEL_FILE="babel.config.js"
if ! grep -q "react-native-reanimated/plugin" "$BABEL_FILE"; then
  sed -i.bak 's/plugins: \[/plugins: [\n      "react-native-reanimated\/plugin",/' "$BABEL_FILE"
fi

# Husky setup
npx husky install
npx husky add .husky/pre-commit "npx lint-staged"

# lint-staged config
cat > lint-staged.config.js <<EOF
module.exports = {
  '*.{js,jsx,ts,tsx}': ['eslint --fix', 'prettier --write'],
};
EOF

# Fallback asset
mkdir -p assets
[ -f assets/bg.jpg ] || curl -s https://via.placeholder.com/1080x1920.jpg -o assets/bg.jpg

# Cleanup
rm -f app.config.py
git rm --cached app.config.py 2>/dev/null || true

# Git commit
git add .editorconfig .npmrc .nvmrc .prettierrc .prettierignore .eslintrc.js index.js app.config.js "$BABEL_FILE" lint-staged.config.js package.json yarn.lock assets/bg.jpg || true
git commit -m "Setup: index.js, lint, prettier, husky, config, babel, assets" || true
git push || true

# === Backend Setup ===
cd ../../services/backend || { echo "❌ Cannot access backend directory"; exit 1; }

[ -d venv ] || python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate

bash security-check.sh && git add . && git commit -m "Backend: security check passed" || true

# === Secrets Check ===
cd ../../apps/aetherion-mobile
if yarn run check:secrets; then
  echo "✓ Secrets check passed."
else
  echo "⚠️  Secrets check skipped or failed."
fi

# === Backend Commit ===
cd ../../services/backend
git add app.py
git commit -m "Backend: ensure root route / API status" || true
git push || true

# === Done ===
echo -e "\n✅ AetherionAI Setup Complete!\n"
echo "Frontend:  cd apps/aetherion-mobile && yarn start"
echo "Backend:   cd services/backend && source venv/bin/activate && flask run"

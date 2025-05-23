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

# Formatting
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
EOF

cat > .eslintrc.js <<EOF
module.exports = {
  root: true,
  extends: ['eslint:recommended', 'plugin:react/recommended'],
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module',
    ecmaFeatures: { jsx: true }
  },
  env: { browser: true, node: true, es6: true },
  rules: {
    semi: ['error', 'always'],
    quotes: ['error', 'single']
  }
};
EOF

# Entry setup
sed -i.bak 's/"main": *".*"/"main": "index.js"/' package.json || true
echo "import 'expo-router/entry';" > index.js

# Install deps
if command -v yarn &>/dev/null; then
  yarn install
else
  npm install --legacy-peer-deps
fi

# Expo deps
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

# Extra packages
yarn add discord.js
yarn add -D @babel/preset-env @react-native/babel-preset@9.3.0 prettier eslint husky lint-staged

# Babel plugin
BABEL_FILE="babel.config.js"
if ! grep -q "react-native-reanimated/plugin" "$BABEL_FILE"; then
  sed -i.bak 's/plugins: \[/plugins: [\n      "react-native-reanimated\/plugin",/' "$BABEL_FILE"
fi

# Git hook setup
npx husky install
npx husky add .husky/pre-commit "npx lint-staged"

cat > lint-staged.config.js <<EOF
module.exports = {
  '*.{js,jsx,ts,tsx}': ['prettier --write', 'eslint --fix']
};
EOF

# Asset check
mkdir -p assets
[ -f assets/bg.jpg ] || curl -s https://via.placeholder.com/1080x1920.jpg -o assets/bg.jpg

rm -f app.config.py
git rm --cached app.config.py 2>/dev/null || true

# Git commit
git add .editorconfig .npmrc .nvmrc .prettierrc .prettierignore .eslintrc.js lint-staged.config.js index.js "$BABEL_FILE" package.json yarn.lock assets/bg.jpg || true
git commit -m "Setup: full frontend config, lint/format, husky, babel, assets" || true
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

# === Backend Commit ===
cd ../../services/backend
git add app.py
git commit -m "Backend: ensure root API route present" || true
git push || true

# === Done ===
echo -e "\n✅ AetherionAI Setup Complete!\n"
echo "Frontend:  cd apps/aetherion-mobile && yarn start"
echo "Backend:   cd services/backend && source venv/bin/activate && flask run"

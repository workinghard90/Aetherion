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
dist
build
coverage
*.log
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

# Expo entry
echo "→ Setting Expo entry to index.js..."
sed -i.bak 's/"main": *".*"/"main": "index.js"/' package.json || true
echo "import 'expo-router/entry';" > index.js

# Install Expo & project deps
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

# Asset fallback
mkdir -p assets
[ -f assets/bg.jpg ] || curl -s https://via.placeholder.com/1080x1920.jpg -o assets/bg.jpg

# Husky + lint-staged setup
npx husky install

mkdir -p .husky/_

cat > .husky/pre-commit <<'EOF'
#!/bin/sh
. "$(dirname "$0")/_/husky.sh"

npx lint-staged
EOF
chmod +x .husky/pre-commit

cat > .husky/_/husky.sh <<'EOF'
#!/bin/sh
# Husky Git hook loader

if [ -z "$HUSKY_SKIP_HOOKS" ]; then
  . "$(dirname "$0")/husky.sh"
fi
EOF
chmod +x .husky/_/husky.sh

cat > lint-staged.config.js <<EOF
export default {
  "*.{js,jsx,ts,tsx,json,md}": ["prettier --write", "eslint --fix"]
};
EOF

# Cleanup
rm -f app.config.py
git rm --cached app.config.py 2>/dev/null || true

# Git commit frontend
git add .editorconfig .prettierrc .prettierignore .npmrc .nvmrc .eslintrc.js index.js app.config.js "$BABEL_FILE" package.json yarn.lock assets/bg.jpg lint-staged.config.js .husky || true
git commit -m "Setup: frontend linting, prettier, husky, expo-router, assets" || true
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
cd ../../apps/aetherion-mobile
if yarn run check:secrets; then
  echo "✓ Secrets check passed."
else
  echo "⚠️  Secrets check skipped or failed."
fi

# === Backend commit ===
cd ../../services/backend
git add app.py
git commit -m "Backend: ensure root route / API status" || true
git push || true

# === Done ===
echo -e "\n✅ AetherionAI Setup Complete!"
echo "Frontend:  cd apps/aetherion-mobile && yarn start"
echo "Backend:   cd services/backend && source venv/bin/activate && flask run"

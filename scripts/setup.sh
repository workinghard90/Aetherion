#!/bin/bash

set -e

echo -e "\n=== Setting up AetherionAI Monorepo (npm only) ===\n"

# === Frontend Setup ===
echo "→ Setting up frontend..."
cd apps/aetherion-mobile || { echo "❌ Cannot access frontend directory"; exit 1; }

# Node and NPM config
echo "18.20.8" > .node-version
cat > .npmrc <<EOF
legacy-peer-deps=true
audit=false
EOF

# Editor and Linting Configs
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
coverage
*.log
EOF

cat > .eslintrc.js <<EOF
module.exports = {
  root: true,
  extends: ['eslint:recommended'],
  env: {
    browser: true,
    node: true,
    es2021: true
  },
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module'
  },
  rules: {}
};
EOF

# Install frontend dependencies
npm install

# Expo entry point
echo "→ Configuring Expo entry..."
sed -i.bak 's/"main": *".*"/"main": "index.js"/' package.json || true
echo "import 'expo-router/entry';" > index.js

# Ensure Babel plugin
BABEL_FILE="babel.config.js"
if ! grep -q "react-native-reanimated/plugin" "$BABEL_FILE"; then
  sed -i.bak 's/plugins: \[/plugins: [\n    "react-native-reanimated\/plugin",/' "$BABEL_FILE"
fi

# Husky and Lint-Staged
npx husky install
npx husky add .husky/pre-commit "npx lint-staged"

cat > lint-staged.config.js <<EOF
export default {
  "*.{js,jsx,ts,tsx,json,md}": ["prettier --write", "eslint --fix"]
};
EOF

# Fallback asset
mkdir -p assets
[ -f assets/bg.jpg ] || curl -s https://via.placeholder.com/1080x1920.jpg -o assets/bg.jpg

# Git Commit
git add .editorconfig .prettierrc .prettierignore .npmrc .eslintrc.js index.js package.json babel.config.js lint-staged.config.js .husky assets/bg.jpg || true
git commit -m "Setup: npm-based frontend, husky, lint, prettier, expo entry" || true
git push || true

# === Backend Setup ===
echo -e "\n→ Setting up backend..."
cd ../../services/backend || { echo "❌ Cannot access backend directory"; exit 1; }

[ -d venv ] || python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate

bash security-check.sh && git add . && git commit -m "Backend: security verified" || true

# === Done ===
echo -e "\n✅ AetherionAI Setup Complete"
echo "Frontend: cd apps/aetherion-mobile && npm start"
echo "Backend:  cd services/backend && source venv/bin/activate && flask run"

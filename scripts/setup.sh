#!/bin/bash

set -e

echo -e "\n=== Resetting AetherionAI Frontend (npm-only) ==="

cd apps/aetherion-mobile || { echo "❌ Cannot access frontend directory"; exit 1; }

echo "→ Cleaning up previous artifacts..."
rm -rf node_modules yarn.lock package-lock.json .npmrc .yarn .yarnrc.yml

echo "→ Initializing npm-based setup..."
echo "18.20.3" > .nvmrc
cat > .npmrc <<EOF
legacy-peer-deps=true
audit=false
registry=https://registry.npmjs.org/
EOF

echo "→ Creating fresh package.json..."
cat > package.json <<EOF
{
  "name": "aetherion-mobile",
  "version": "1.0.0",
  "private": true,
  "main": "index.js",
  "scripts": {
    "start": "expo start",
    "build": "expo export --platform web"
  },
  "dependencies": {
    "expo": "49.0.13",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "react-native": "0.73.0",
    "react-native-web": "~0.19.6",
    "react-native-gesture-handler": "^2.12.0",
    "react-native-reanimated": "^3.6.1",
    "react-native-safe-area-context": "^4.8.1",
    "react-native-screens": "^3.30.0",
    "@expo/metro-runtime": "~3.1.3",
    "@react-navigation/native": "^6.1.15",
    "@react-navigation/stack": "^6.4.1",
    "@react-native-async-storage/async-storage": "^1.21.0"
  },
  "devDependencies": {
    "@babel/core": "^7.22.20",
    "@babel/preset-env": "^7.22.20",
    "@react-native/babel-preset": "8.5.0"
  },
  "engines": {
    "node": "18.x",
    "npm": ">=9.0.0"
  }
}
EOF

echo "→ Installing clean dependencies..."
npm install --legacy-peer-deps

echo "→ Creating minimal babel.config.js..."
cat > babel.config.js <<EOF
module.exports = {
  presets: ["@babel/preset-env", "@react-native/babel-preset"],
  plugins: ["react-native-reanimated/plugin"]
};
EOF

echo "→ Done. Run:"
echo "   cd apps/aetherion-mobile && npm start"

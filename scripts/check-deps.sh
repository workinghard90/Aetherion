#!/bin/bash

set -e

echo ""
echo "=== Verifying AetherionAI Dependencies ==="
echo ""

REQUIRED_MODULES=(
  "react-dom"
  "react-native-web"
  "react-native-gesture-handler"
  "react-native-reanimated"
  "react-native-screens"
  "react-native-safe-area-context"
  "@react-navigation/native"
  "@react-navigation/stack"
  "@expo/metro-runtime"
  "discord.js"
)

cd apps/aetherion-mobile

echo "→ Checking dependencies in package.json..."
for module in "${REQUIRED_MODULES[@]}"; do
  if grep -q "\"$module\"" package.json; then
    echo "✓ $module is present"
  else
    echo "⚠️  Missing: $module. Installing..."
    yarn add "$module"
  fi
done

echo ""
echo "✅ Dependency check complete."

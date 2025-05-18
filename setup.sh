#!/usr/bin/env bash
npm install
# or
npx expo install @expo/metro-runtime

# Bootstrap script for local dev

# 1) create folders & placeholders
mkdir -p frontend/assets frontend/screens frontend/services backend
touch frontend/assets/{icon.png,splash.png,favicon.png}

# 2) copy .env example
cp backend/.env.example backend/.env

echo "✅ Structure initialized!"
echo "👉 To run backend locally:"
echo "   cd backend && python3 -m venv venv && source venv/bin/activate"
echo "   pip install -r requirements.txt"
echo "   python app.py"
echo ""
echo "👉 To run frontend locally:"
echo "   cd frontend && npm install"
echo "   npm start        # Expo Go"
echo "   npm run web      # Web preview"

cd frontend
git add package.json
git commit -m "fix build script to use expo export:web"
git push

chmod +x setup.sh

#!/bin/bash
# Bootstrap script to create minimal folder structure and install dependencies

# Create frontend & backend folders if missing
mkdir -p frontend/assets frontend/screens frontend/services backend

# Create placeholder assets
touch frontend/assets/icon.png
touch frontend/assets/splash.png
touch frontend/assets/favicon.png

echo "EXPO_PUBLIC_API_URL=https://aetherion-mobile.onrender.com/api" > .env

# Install frontend dependencies
cd frontend
npm install

# Install backend dependencies in a virtual environment
cd ../backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Bootstrap complete. Run 'cd frontend && npm start' for Expo, 'cd backend && flask run' for API."

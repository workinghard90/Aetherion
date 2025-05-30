#!/bin/bash
set -e

# create directories
mkdir -p backend/scrolls frontend/assets frontend/screens frontend/services

# placeholder assets
touch frontend/assets/{icon.png,splash.png,favicon.png,beacon-chord.wav}

# copy env examples
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# install deps
echo "➡️ Installing frontend..."
cd frontend
npm install
echo "➡️ Installing backend..."
cd ../backend
pip install -r requirements.txt

echo "✅ Setup complete. Run 'cd backend && python app.py' and 'cd frontend && npm start'"

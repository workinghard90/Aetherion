#!/bin/bash

# Create backend and frontend folder structure (if not existing)
mkdir -p backend
mkdir -p frontend/assets
mkdir -p frontend/screens
mkdir -p frontend/services

# Create placeholder assets
touch frontend/assets/icon.png
touch frontend/assets/splash.png
touch frontend/assets/favicon.png
touch frontend/assets/gate_background.png

# Copy .env.example to .env for both backend & frontend
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Install frontend dependencies
cd frontend && npm install

# Install backend dependencies
cd ../backend && python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "✅ Project structure is set up. Use 'cd backend && python app.py' to run the backend, and 'cd frontend && npm start' to launch the frontend."

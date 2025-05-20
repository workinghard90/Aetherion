#!/bin/bash

echo "Setting up AetherionAI Monorepo..."

cd apps/aetherion-mobile
yarn install
cd ../../services/backend
python3 -m venv venv
source venv/bin/activate
pip install flask flask-cors
deactivate

echo "Setup complete."
echo "Run frontend: yarn start:expo"
echo "Run backend:  yarn start:backend"

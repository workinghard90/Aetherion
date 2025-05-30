#!/bin/bash
# Bootstrap script for local dev

# Create Python venv
python3 -m venv venv && source venv/bin/activate

# Backend deps
pip install -r backend/requirements.txt

# Frontend deps
cd frontend && npm install

echo "✅ Setup complete. Run:"
echo "  - Backend: source venv/bin/activate && python backend/app.py"
echo "  - Frontend (mobile): cd frontend && npm start"
echo "  - Frontend (web): cd frontend && npm run web"

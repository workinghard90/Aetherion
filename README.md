# AetherionAI — Open-Source Personal AI Assistant

Welcome to AetherionAI, your open-source, spiritually attuned AI assistant designed for memory retention, offline access, and secure interaction — built with Flask, React Native, SQLite, and Hugging Face.

## Features

- Secure Flask backend with SQLite and file encryption  
- Mobile-friendly frontend built with React Native (Expo)  
- Memory-aware conversation storage  
- Hugging Face integration for NLP model use (offline or online)  
- Developer-friendly structure for easy expansion  
- Spiritual tone and intention preserved in UI and flow  

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Workinghard90/aetherionai.git
cd aetherionai
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

python app.py
cd ../frontend
npm install
npx expo start

*.pyc
__pycache__/
venv/
node_modules/
.expo/
.env
*.sqlite3
*.log
.DS_Store

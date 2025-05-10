# AetherionAI — Open-Source Personal AI Assistant

Welcome to **AetherionAI**, your spiritually attuned, open-source AI assistant. Designed for memory retention, secure offline interaction, and thoughtful, intuitive use — powered by Flask, React Native (Expo), SQLite, and Hugging Face.

---

## Features

- Secure **Flask backend** with SQLite + encrypted file storage  
- **React Native** frontend supporting web & mobile (via Expo)  
- Hugging Face transformer model integration (online/offline modes)  
- Memory-aware conversation history  
- **Netlify-compatible** static frontend deployment  
- Spiritual tone and welcoming user experience  
- Clean, extensible code structure for contributors

---

## Quickstart Instructions

### 1. Clone This Repository

```bash
git clone https://github.com/Workinghard90/aetherionai.git
cd aetherionai

cd backend
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
gunicorn -r requirements.txt

cd ../frontend
npm install
npx expo start
npm run web

const API_URL = 'https://aetherionai.onrender.com'; // Your Render backend URL

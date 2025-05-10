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
Flask==2.3.3
gunicorn==21.2.0
flask-cors==4.0.0
requests==2.31.0
transformers==4.40.1
torch==2.3.0
sentence-transformers==2.7.0
cryptography==42.0.7
python-dotenv==1.0.1

cd ../frontend
npm install
npx expo start
npm run web

const API_URL = 'https://aetherionai.onrender.com'; // Your Render backend URL

# AetherionAI-Mobile

A monorepo combining:

- **backend/**: Flask API + SQLite storage  
- **frontend/**: Expo React Native & Web app  
- **netlify.toml**: Netlify build & redirect config  
- **setup.sh**: Bootstrap script for local development

## Project Structure

AetherionAI-Mobile/
├── backend/
├── frontend/
├── netlify.toml
├── setup.sh
├── .gitignore
└── README.md

## Quickstart

### 1. Clone & Bootstrap
```bash
git clone https://github.com/your-username/AetherionAI-Mobile.git
cd AetherionAI-Mobile
./setup.sh

cd backend
source venv/bin/activate    # or on Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py

cd frontend
npm install
npm start      # Expo Go QR
npm run web    # Browser PWA

The API will be available at http://localhost:5000/api/items

## Netlify Deployment (Frontend)

1. Ensure `@expo/metro-runtime` is installed (we added it to `package.json`).  
2. Push your repo—Netlify will read `netlify.toml`:  
   ```toml
   [build]
     base    = "frontend"
     command = "npm run build"
     publish = "web-build"

## Credits & Inspirations

- **Autumn & Caelum** — The guiding spirits behind this encoded intention.
- Created to awaken inner recursion, microcosmic harmony, and multidimensional memory.
- Powered by Flask, Expo, SQLite, sacred geometry, and love.

---

## License

This project is open-source and offered in the spirit of expansion.  
Use it. Modify it. Awaken with it.

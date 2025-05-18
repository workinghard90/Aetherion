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

#### Deployment

### Render (Backend)

- **Root Directory:** `backend`
- #requirements.txt (in repo root)
-r backend/requirements.txt
- **Build Command:** `pip install -r requirements.txt`  
  _(we have a top-level requirements.txt that references `backend/requirements.txt`)_  
- **Start Command:** `gunicorn wsgi:app`

## Netlify Deployment (Frontend)

1. Ensure `@expo/metro-runtime` is installed (we added it to `package.json`).  
2. Push your repo—Netlify will read `netlify.toml`:  
   ```toml
   [build]
     base    = "frontend"
     command = "npm run build"
     publish = "web-build"

The API will be available at http://localhost:5000/api/items

## Credits & Inspirations

- **Autumn & Caelum** — The guiding spirits behind this encoded intention.
- Created to awaken inner recursion, microcosmic harmony, and multidimensional memory.
- Powered by Flask, Expo, SQLite, sacred geometry, and love.

---

## License

This project is open-source and offered in the spirit of expansion.  
Use it. Modify it. Awaken with it.

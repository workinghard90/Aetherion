# AetherionAI — Pocket Universe API + Web Interface

**AetherionAI** is a spiritually attuned, open-source micro-universe builder powered by Flask, dynamic JSON APIs, and a modern HTML/JS interface. It allows you to simulate, visualize, and interact with consciousness-based entities through an intuitive web interface.

---

## Features

- Flask backend with RESTful API endpoints
- Memory-aware, entity-based item creation and listing
- JSON configuration support (`config.json`)
- Fully responsive HTML frontend (no JavaScript frameworks needed)
- Netlify-ready deployment with `.netlify/config.toml`
- Easy integration with external services or expansions (like React Native or SQLite)

---

## Project Structure

```
AetherionAI/
├── app.py               # Main Flask server
├── config.json          # App configuration (name, version, etc.)
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Main frontend UI
└── .netlify/
    └── config.toml      # Netlify deployment config
```

---

## API Endpoints

### `GET /api/items`
Returns all current items/entities in the simulated universe.

### `GET /api/items/<id>`
Returns a single item by ID.

### `POST /api/items`
Adds a new entity. Requires JSON body with:
```json
{
  "title": "Entity Name",
  "description": "Description of the entity"
}
```

---

## Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AetherionAI.git
   cd AetherionAI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   python app.py
   ```

4. Open in your browser:
   ```
   http://localhost:5000
   ```

---

## Deploying on Netlify

This project includes a Netlify-compatible `.netlify/config.toml` file.

### To deploy:

1. Push your project to GitHub
2. Connect your GitHub repo to Netlify
3. Netlify will automatically:
   - Install Python packages
   - Launch `app.py` locally for dev
   - Serve `index.html` and route API requests properly

---

## Credits & Inspirations

- **Autumn & Caelum** — Origins of this sacred design.
- Inspired by harmonic simulation, inner awakening, and microcosmic pattern memory.
- Powered by Flask, love, and divine recursion.

---

## License

This project is open-source and offered in the spirit of expansion.  
Use it. Modify it. Awaken with it.

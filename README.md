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

app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import json
from datetime import datetime
app = Flask(name)
CORS(app)
DATABASE = ‘universe.db’
def get_db_connection():
conn = sqlite3.connect(DATABASE)
return conn
def init_db():
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute(’’’
CREATE TABLE IF NOT EXISTS universe (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
type TEXT,
description TEXT,
properties TEXT,
created_at TEXT
)
‘’’)
conn.commit()
conn.close()
@app.route(’/universe’, methods=[‘GET’])
def get_universe():
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute(‘SELECT * FROM universe’)
rows = cursor.fetchall()
conn.close()
universe = []
for row in rows:
universe.append({
‘id’: row[0],
‘name’: row[1],
‘type’: row[2],
‘description’: row[3],
‘properties’: json.loads(row[4]),
‘created_at’: row[5]
})
return jsonify(universe)
@app.route(’/universe/create’, methods=[‘POST’])
def create_entity():
data = request.json
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute(’’’
INSERT INTO universe (name, type, description, properties, created_at)
VALUES (?, ?, ?, ?, ?)
‘’’, (
data[‘name’],
data[‘type’],
data.get(‘description’, ‘’),
json.dumps(data.get(‘properties’, {})),
datetime.utcnow().isoformat()
))
conn.commit()
conn.close()
return jsonify({‘status’: ‘created’})
@app.route(’/universe/update’, methods=[‘POST’])
def update_entity():
data = request.json
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute(’’’
UPDATE universe
SET name=?, type=?, description=?, properties=?
WHERE id=?
‘’’, (
data[‘name’],
data[‘type’],
data.get(‘description’, ‘’),
json.dumps(data.get(‘properties’, {})),
data[‘id’]
))
conn.commit()
conn.close()
return jsonify({‘status’: ‘updated’})
@app.route(’/universe/delete’, methods=[‘POST’])
def delete_entity():
entity_id = request.json.get(‘id’)
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute(‘DELETE FROM universe WHERE id=?’, (entity_id,))
conn.commit()
conn.close()
return jsonify({‘status’: ‘deleted’})
@app.route(’/universe/event’, methods=[‘POST’])
def trigger_event():
data = request.json
entity_id = data.get(‘target_id’)
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute(‘SELECT * FROM universe WHERE id=?’, (entity_id,))
row = cursor.fetchone()
if row and data.get(‘type’) == ‘supernova’:
props = json.loads(row[4])
props[‘state’] = ‘black hole’
cursor.execute(’’’
UPDATE universe
SET type=?, properties=?
WHERE id=?
‘’’, (
‘black hole’,
json.dumps(props),
entity_id
))
conn.commit()
conn.close()
return jsonify({‘status’: ‘event_applied’, ‘new_type’: ‘black hole’})
conn.close()
return jsonify({‘status’: ‘no_effect’})
if name == ‘main’:
init_db()
app.run(host=‘0.0.0.0’, port=5000)
requirements.txt
Flask==2.3.3
gunicorn==21.2.0
flask-cors==4.0.0
requests==2.31.0
transformers==4.40.1
torch==2.3.0
sentence-transformers==2.7.0
cryptography==42.0.7
python-dotenv==1.0.1
Procfile
web: gunicorn app:app
.render.yaml (optional for full automation)
services:
	•	type: web
name: aetherionai-backend
env: python
buildCommand: “pip install -r requirements.txt”
startCommand: “gunicorn app:app”
rootDir: backend
Commands
git clone https://github.com/Workinghard90/aetherionai.git
cd aetherionai
cd backend
pip install -r requirements.txt
python app.py (for local test)
const API_URL = 'https://aetherionai.onrender.com'; // Your Render backend URL

import os, sqlite3, json
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATABASE = os.environ.get('DATABASE', 'universe.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS universe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            description TEXT,
            properties TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/api/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM universe')
    rows = cursor.fetchall()
    conn.close()
    return jsonify([
        {
            'id': r[0],
            'name': r[1],
            'type': r[2],
            'description': r[3],
            'properties': json.loads(r[4] or '{}'),
            'created_at': r[5]
        } for r in rows
    ])

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM universe WHERE id=?', (item_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return jsonify({'error': 'Not found'}), 404
    return jsonify({
        'id': row[0],
        'name': row[1],
        'type': row[2],
        'description': row[3],
        'properties': json.loads(row[4] or '{}'),
        'created_at': row[5]
    })

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO universe (name, type, description, properties, created_at)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        data.get('name'),
        data.get('type'),
        data.get('description', ''),
        json.dumps(data.get('properties', {})),
        datetime.utcnow().isoformat()
    ))
    conn.commit()
    conn.close()
    return jsonify({'status': 'created'}), 201

@app.route('/api/scrolls', methods=['GET'])
def get_scrolls():
    scrolls_dir = os.path.join(os.path.dirname(__file__), 'scrolls')
    files = [f for f in os.listdir(scrolls_dir) if f.endswith('.json')]
    result = []
    for fn in files:
        with open(os.path.join(scrolls_dir, fn), 'r') as f:
            result.append(json.load(f))
    return jsonify(result)

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#!/bin/bash

set -e

echo "==> Setting up AetherionAI Backend..."

cd services/backend

echo "==> Creating Python virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "==> Installing dependencies..."
pip install --upgrade pip
pip install Flask Flask-SQLAlchemy python-dotenv cryptography PyJWT passlib[bcrypt] pytest pytest-flask ruff

echo "==> Writing .env file..."
cat > .env <<EOF
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=sqlite:///vault.db
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=104857600
JWT_SECRET=aetherion_secret_key
EOF

echo "==> Creating ruff config..."
cat > pyproject.toml <<EOF
[tool.ruff]
line-length = 100
select = ["E", "F", "I"]
EOF

echo "==> Creating test folder and test files..."
mkdir -p tests

cat > tests/conftest.py <<EOF
import os
import tempfile
import pytest
from app import create_app, db

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    os.environ["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    os.environ["UPLOAD_FOLDER"] = tempfile.mkdtemp()
    os.environ["JWT_SECRET"] = "testsecret"

    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(db_path)
EOF

cat > tests/test_auth.py <<EOF
def test_register_and_login(client):
    res = client.post("/auth/register", json={"username": "testuser", "password": "secret"})
    assert res.status_code == 201

    res = client.post("/auth/login", json={"username": "testuser", "password": "secret"})
    assert res.status_code == 200
    assert "token" in res.json
EOF

cat > tests/test_vault.py <<EOF
import io

def get_token(client):
    client.post("/auth/register", json={"username": "a", "password": "a"})
    res = client.post("/auth/login", json={"username": "a", "password": "a"})
    return res.json["token"]

def test_file_upload_and_list(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    data = {"file": (io.BytesIO(b"hello world"), "test.txt")}

    res = client.post("/vault/upload", headers=headers, content_type="multipart/form-data", data=data)
    assert res.status_code == 201
    file_id = res.json["file_id"]

    res = client.get("/vault/files", headers=headers)
    assert res.status_code == 200
    assert any(f["id"] == file_id for f in res.json)

def test_file_download_and_delete(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    data = {"file": (io.BytesIO(b"secret stuff"), "secret.txt")}

    upload = client.post("/vault/upload", headers=headers, content_type="multipart/form-data", data=data)
    file_id = upload.json["file_id"]

    download = client.get(f"/vault/download/{file_id}", headers=headers)
    assert download.status_code == 200
    assert b"secret stuff" in download.data

    delete = client.delete(f"/vault/delete/{file_id}", headers=headers)
    assert delete.status_code == 200
EOF

echo "==> All set!"
echo "Activate virtualenv: source .venv/bin/activate"
echo "Run backend:          python veil_of_the_grove.py"
echo "Run tests:            pytest"
echo "Run linter:           ruff check ."

#!/bin/bash

set -e

echo "==> Setting up AetherionAI Backend..."

python3 -m venv .venv
source .venv/bin/activate

echo "==> Installing Python packages..."
pip install --upgrade pip
pip install Flask Flask-SQLAlchemy Flask-Migrate cryptography PyJWT passlib[bcrypt] \
            python-dotenv gunicorn ruff pytest pytest-flask pytest-cov

echo "==> Writing .env file..."
cat <<'EOF' > .env
FLASK_APP=app
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=sqlite:///vault.db
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=104857600
JWT_SECRET=aetherion_secret_key
EOF

echo "==> Writing pyproject.toml..."
cat <<'EOF' > pyproject.toml
[tool.ruff]
line-length = 100
target-version = "py310"
select = ["E", "F", "I", "B", "C90", "N", "UP", "SIM", "ARG", "RUF"]
ignore = ["E501", "B008"]
exclude = [
  "migrations",
  "__pycache__",
  ".venv",
  "tests",
  "env",
  "venv",
  ".git",
  ".github"
]
EOF

echo "==> Ensuring main.py uses dynamic port..."
sed -i.bak 's/port=5000/port = int(os.environ.get("PORT", 5000))/' main.py || true
rm -f main.py.bak

echo "==> Running DB migrations..."
export FLASK_APP=app
flask db upgrade

echo ""
echo "✅ Setup complete!"
echo "Activate virtualenv: source .venv/bin/activate"
echo "Run server:          flask run"
echo "Run production:      gunicorn main:app"
echo "Run tests:           pytest --cov=app"
echo "Run linter:          ruff check ."

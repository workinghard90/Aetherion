#!/bin/bash

set -e

echo "==> Setting up AetherionAI Backend..."

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install runtime dependencies
echo "==> Installing Python packages..."
pip install --upgrade pip
pip install Flask==2.3.3 Flask-SQLAlchemy==3.1.1 Flask-Migrate==4.0.5 \
            cryptography==42.0.5 PyJWT==2.8.0 passlib[bcrypt]==1.7.4 \
            python-dotenv==1.0.1 gunicorn==21.2.0

# Install dev/test tools
pip install pytest pytest-flask pytest-cov ruff

# Generate .env
echo "==> Writing .env file..."
cat <<EOF > .env
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=sqlite:///vault.db
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=104857600
JWT_SECRET=aetherion_secret_key
EOF

# Write Ruff config
echo "==> Writing pyproject.toml..."
cat <<EOF > pyproject.toml
[tool.ruff]
line-length = 100
target-version = "py311"
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

# Ensure upload folder exists
mkdir -p uploads

# Initialize DB
echo "==> Initializing DB..."
export FLASK_APP=main.py
flask db upgrade || echo "==> Skipped DB migration (if not defined yet)"

echo ""
echo "✅ Setup complete!"
echo "Activate: source .venv/bin/activate"
echo "Run dev server: flask run"
echo "Run prod server: gunicorn main:app"
echo "Run tests: pytest --cov=aetherion"
echo "Lint check: ruff check ."

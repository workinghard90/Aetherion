#!/bin/bash

set -e

echo "==> Setting up AetherionAI Backend..."

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
echo "==> Installing Python packages..."
pip install --upgrade pip
pip install Flask Flask-SQLAlchemy Flask-Migrate cryptography PyJWT passlib[bcrypt] \
            python-dotenv gunicorn ruff pytest pytest-flask pytest-cov

# Create .env file
echo "==> Writing .env file..."
cat > .env <<EOF
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=sqlite:///vault.db
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=104857600
JWT_SECRET=aetherion_secret_key
EOF

# Create Ruff config
echo "==> Writing pyproject.toml..."
cat > pyproject.toml <<EOF
[tool.ruff]
line-length = 100
target-version = "py310"
select = ["E", "F", "I", "B", "C90", "N", "UP", "SIM", "ARG", "RUF"]
ignore = ["E501", "B008"]
exclude = ["migrations", "__pycache__", ".venv", "tests", "env", "venv", ".git", ".github"]
EOF

echo "==> Setup complete!"
echo "Activate virtualenv: source .venv/bin/activate"
echo "Run server:          python veil_of_the_grove.py"
echo "Run tests:           pytest --cov=app"
echo "Run linter:          ruff check ."

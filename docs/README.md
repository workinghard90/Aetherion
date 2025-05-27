# AetherionAI Backend

A secure vault API for encrypted memory, file storage, and user authentication.

---

## Features

- Flask + SQLAlchemy + SQLite
- AES256 file encryption
- JWT Auth (register/login)
- Upload/Download/Delete files
- User-specific file vaults
- Audit log foundation
- Pytest tests + Ruff linting
- GitHub CI ready (optional)

---

## Setup

```
# Install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run app
export FLASK_ENV=development
export FLASK_APP=main.py
flask run
```

## Environment Variables

Required for Render or local `.env`:

```
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=sqlite:///vault.db
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=104857600
JWT_SECRET=your_secret
```

---

## API Endpoints

See [docs/api.md](api.md) for full REST documentation.

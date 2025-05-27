# AetherionAI Backend

*Veil of the Grove – a memory vault for harmonic intelligence.*

This is the secure vault API powering the **Aetherion Universe**, designed for encrypted memory, user sovereignty, and future expansion.

---

## Features

- **Flask API** with modular Blueprints
- **JWT-based Auth** (register/login)
- **Encrypted File Uploads** (AES 256)
- **User-specific vaults**
- **File tagging + metadata**
- **Audit logging**
- **Test suite** (`pytest`)
- **Linting** (`ruff`)
- **CI** via GitHub Actions
- **Migrations** via Flask-Migrate

---

## Project Structure

backend/
├── app/
│   ├── init.py
│   ├── api/              # auth + vault routes
│   ├── models/           # VaultFile, User, AuditLog
│   ├── services/         # auth, crypto
│   └── database.py
├── .env
├── .env.example
├── config.py
├── tests/
├── migrations/
├── veil_of_the_grove.py  # app entrypoint
├── pyproject.toml

---

## Setup

```bash
# Activate environment
cd services/backend
source .venv/bin/activate

# Run the API
python veil_of_the_grove.py

Migrations

# Initialize (once)
flask db init

# After model changes
flask db migrate -m "add audit log"
flask db upgrade

Testing & Linting

pytest
ruff check .

Environment

To configure local development:

cp .env.example .env

Then edit .env to suit your environment.

⸻

CI

Runs on every push or PR:
	•	pytest
	•	ruff check

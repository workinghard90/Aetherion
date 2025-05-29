# scripts/seed_buttons.py
from aetherion import create_app
from aetherion.extensions import db
from aetherion.models.button import Button

app = create_app()

with app.app_context():
    db.session.add_all([
        Button(id="docs", label="Docs", sigil="📜", url="https://your-docs-link.com"),
        Button(id="vault", label="Vault", sigil="🔐", url="https://your-vault-link.com"),
        Button(id="github", label="GitHub", sigil="🐙", url="https://github.com/your-repo")
    ])
    db.session.commit()
    print("✅ Buttons seeded")

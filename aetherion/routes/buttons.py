# aetherion/routes/buttons.py

from flask import Blueprint, jsonify

buttons_bp = Blueprint("buttons", __name__)

@buttons_bp.route("/api/buttons", methods=["GET"])
def get_buttons():
    return jsonify([
        {
            "id": "docs",
            "label": "Docs",
            "sigil": "📜",
            "url": "https://your-docs-link.com"
        },
        {
            "id": "vault",
            "label": "Vault",
            "sigil": "🔐",
            "url": "https://your-vault-link.com"
        },
        {
            "id": "github",
            "label": "GitHub",
            "sigil": "🐙",
            "url": "https://github.com/your-repo"
        }
    ])

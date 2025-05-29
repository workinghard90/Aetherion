# aetherion/routes/buttons.py

from flask import Blueprint, jsonify, request, g
from aetherion.models.button import Button
from aetherion.core.auth_middleware import try_auth

buttons_bp = Blueprint("buttons", __name__, url_prefix="/api/buttons")

@buttons_bp.route("/", methods=["GET"])
def get_buttons():
    try_auth()  # Sets g.user if token valid

    static_buttons = [
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
    ]

    dynamic_buttons = Button.query.all()
    dynamic = [
        {"id": b.id, "label": b.label, "sigil": b.sigil, "url": b.url}
        for b in dynamic_buttons
    ]

    return jsonify(static_buttons + dynamic)

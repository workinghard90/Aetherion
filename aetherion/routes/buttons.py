from flask import Blueprint, jsonify, request
from aetherion.models.button import Button
from aetherion.core.auth_middleware import try_auth

buttons_bp = Blueprint("buttons", __name__)

@buttons_bp.route("/api/buttons", methods=["GET"])
def get_buttons():
    try_auth()  # sets request.user if token valid

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

    # Optional: filter based on user role or permissions
    dynamic_buttons = Button.query.all()
    dynamic = [
        {"id": b.id, "label": b.label, "sigil": b.sigil, "url": b.url}
        for b in dynamic_buttons
    ]

    return jsonify(static_buttons + dynamic)

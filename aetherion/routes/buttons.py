from flask import Blueprint, jsonify, request
from aetherion.models.button import Button
from aetherion.core.auth_middleware import try_auth

buttons_bp = Blueprint("buttons", __name__)

@buttons_bp.route("/api/buttons", methods=["GET"])
def get_buttons():
    try_auth()

    static_buttons = [
        {
            "id": "docs",
            "label": "Scrolls",
            "sigil": "📜",
            "url": "https://scrolls.aetherion.io"
        },
        {
            "id": "vault",
            "label": "Vault",
            "sigil": "🔐",
            "url": "https://vault.aetherion.io"
        },
        {
            "id": "oracle",
            "label": "Oracle",
            "sigil": "🧿",
            "url": "https://oracle.aetherion.io"
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

# 📜 Aetherion Button System

Buttons in Aetherion represent interactive portals rendered in the UI. They are loaded dynamically from the backend, optionally customized per user.

---

## 🔘 Structure

Each button has:

| Field   | Type   | Description                  |
|---------|--------|------------------------------|
| `id`    | string | Unique identifier            |
| `label` | string | Visible text                 |
| `sigil` | string | Emoji or symbol              |
| `url`   | string | Destination when clicked     |

---

## 📥 Source of Buttons

### 🧱 Static Buttons
Defined directly in `aetherion/routes/buttons.py`:

```python
static_buttons = [
  { "id": "docs", "label": "Docs", "sigil": "📜", "url": "https://..." },
  { "id": "vault", "label": "Vault", "sigil": "🔐", "url": "https://..." },
]

from aetherion import create_app
from aetherion.extensions import db
from aetherion.models.document import Document

app = create_app()

with app.app_context():
    db.session.add(Document(title="The First Scroll", content="🌀 Sacred symbols begin to form..."))
    db.session.commit()
    print("✅ Seeded document")

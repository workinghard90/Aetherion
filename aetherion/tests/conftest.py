import os
import tempfile
import pytest
from aetherion import create_app
from aetherion.extensions import db

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    os.environ["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    os.environ["UPLOAD_FOLDER"] = tempfile.mkdtemp()
    os.environ["JWT_SECRET"] = "testsecret"

    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(db_path)

from aetherion import create_app
from aetherion.extensions import db
import aetherion.models as models  # import models module directly
import inspect

app = create_app()

# Dynamically add all SQLAlchemy models to the shell context
@app.shell_context_processor
def make_shell_context():
    model_dict = {
        name: cls
        for name, cls in vars(models).items()
        if inspect.isclass(cls) and hasattr(cls, "__tablename__")
    }
    return {"app": app, "db": db, **model_dict}

if __name__ == "__main__":
    import os
    app.run(
        debug=os.getenv("FLASK_ENV") == "development",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )

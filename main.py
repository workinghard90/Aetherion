from aetherion import create_app

app = create_app()

if __name__ == "__main__":
    import os
    app.run(
        debug=os.getenv("FLASK_ENV") == "development",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )

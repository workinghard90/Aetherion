from aetherion import create_app

app = create_app()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    debug = os.getenv("FLASK_ENV") == "development"
    app.run(debug=debug, host="0.0.0.0", port=port)

# services/backend/veil_of_the_grove.py

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

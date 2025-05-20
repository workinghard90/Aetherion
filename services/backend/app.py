from flask import Flask
from routes.docs import docs
from routes.gates import gates
from routes.veil import veil

app = Flask(__name__)
app.register_blueprint(docs)
app.register_blueprint(gates)
app.register_blueprint(veil)

@app.route("/aetherion/arrival")
def arrival():
    return {"message": "Welcome Guardian", "pulse": "aligned"}

if __name__ == "__main__":
    app.run(port=10000)

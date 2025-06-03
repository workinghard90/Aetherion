from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/launchpad/hello", methods=["GET"])
def hello_launchpad():
    return jsonify({"msg": "Hello from LaunchPad!"})

if __name__ == "__main__":
    app.run(port=5001, debug=True)

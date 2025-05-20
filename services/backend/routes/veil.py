from flask import Blueprint, jsonify
import os

veil = Blueprint("veil", __name__)

@veil.route("/api/veil/cloak", methods=["POST"])
def veil_cloak():
    with open("cloak_signature.txt", "w") as f:
        f.write("cloaked")
    return jsonify({"status": "cloaked"})

@veil.route("/api/veil/unveil", methods=["POST"])
def veil_unveil():
    if os.path.exists("cloak_signature.txt"):
        os.remove("cloak_signature.txt")
    return jsonify({"status": "unveiled"})

@veil.route("/api/veil/status", methods=["GET"])
def veil_status():
    cloaked = os.path.exists("cloak_signature.txt")
    return jsonify({"cloaked": cloaked})

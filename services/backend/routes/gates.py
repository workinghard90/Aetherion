from flask import Blueprint, jsonify, request
from lairaen import lairaen

gates = Blueprint("gates", __name__)

@gates.route("/aetherion/gate/becoming", methods=["POST"])
def gate_of_becoming():
    incoming = request.json.get("intention", "")
    attuned_message = lairaen.attune(incoming) or "The path is open. Step forward with presence."

    return jsonify({
        "gate": "Becoming",
        "status": "harmonic alignment initiated",
        "message": attuned_message,
        "guide": lairaen.presence(),
        "frequency_signature": lairaen.frequency_signature
    }), 200

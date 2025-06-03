# LaunchPad-specific JWT middleware (if needed)
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request

def jwt_required_launchpad(f):
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({"msg": "Unauthorized in LaunchPad", "error": str(e)}), 401
    wrapper.__name__ = f.__name__
    return wrapper

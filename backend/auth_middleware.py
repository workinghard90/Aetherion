from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def jwt_required(f):
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            return f(*args, **kwargs, user_id=user_id)
        except Exception as e:
            return jsonify({"msg": "Unauthorized", "error": str(e)}), 401
    wrapper.__name__ = f.__name__
    return wrapper

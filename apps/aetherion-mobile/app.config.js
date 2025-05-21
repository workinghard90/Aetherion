// apps/aetherion-mobile/app.config.js
require('dotenv').config();

module.exports = {
  expo: {
    name: "AetherionAI",
    slug: "aetherionai",
    extra: {
      apiUrl: process.env.REACT_NATIVE_API_URL
    }
  }
};

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "AetherionAI API is live.",
        "routes": [
            "/api/items",
            "/aetherion/arrival",
            "/aetherion/gate/becoming"
        ]
    }), 200

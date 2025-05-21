// apps/aetherion-mobile/app.config.js
import 'dotenv/config';

export default {
  expo: {
    name: "AetherionAI",
    slug: "aetherionai",
    version: "1.0.0",
    orientation: "portrait",
    platforms: ["ios", "android", "web"],
    extra: {
      apiUrl: process.env.EXPO_PUBLIC_API_URL
    }
  }
};

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Aetherion API is running."})
        "status": "AetherionAI API is live.",
        "routes": [
            "/api/items",
            "/aetherion/arrival",
            "/aetherion/gate/becoming"
        ]
    }), 200

// apps/aetherion-mobile/app.config.js
import 'dotenv/config';

export default {
  expo: {
    name: "AetherionAI",
    slug: "aetherionai",
    version: "1.0.0",
    orientation: "portrait",
    platforms: ["ios", "android", "web"],
    web: {
      bundler: "metro"
    },
    extra: {
      apiUrl: process.env.EXPO_PUBLIC_API_URL
    }
  }
};

// apps/aetherion-mobile/app.config.js

export default () => ({
  name: "AetherionAI",
  slug: "aetherion-mobile",
  version: "1.0.0",
  orientation: "portrait",
  icon: "./assets/icons/icon.png",
  splash: {
    image: "./assets/splash/splash.png",
    resizeMode: "contain",
    backgroundColor: "#ffffff"
  },
  updates: {
    fallbackToCacheTimeout: 0
  },
  assetBundlePatterns: ["**/*"],
  ios: {
    supportsTablet: true
  },
  android: {
    adaptiveIcon: {
      foregroundImage: "./assets/icons/adaptive-icon.png",
      backgroundColor: "#ffffff"
    }
  },
  web: {
    favicon: "./assets/meta/favicon.png"
  },
  extra: {
    apiUrl: process.env.EXPO_PUBLIC_API_URL || "http://localhost:5000"
  }
});

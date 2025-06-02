// Aetherion/frontend/app.config.js

import 'dotenv/config'; // so we can reference process.env.* for local dev

export default () => ({
  expo: {
    name: "Aetherion",
    slug: "aetherion-mobile",
    version: "1.0.0",
    orientation: "portrait",
    icon: "./assets/icon.png",
    userInterfaceStyle: "light",
    splash: {
      image: "./assets/splash.png",
      resizeMode: "contain",
      backgroundColor: "#6200ee"
    },
    assetBundlePatterns: ["**/*"],
    ios: {
      supportsTablet: true
    },
    android: {
      adaptiveIcon: {
        foregroundImage: "./assets/icon.png",
        backgroundColor: "#6200ee"
      }
    },
    web: {
      favicon: "./assets/favicon.png"
    },
    extra: {
      // On Netlify, you must set this env var in the site settings:
      apiUrl: process.env.EXPO_PUBLIC_API_URL || "https://aetherion-mobile.onrender.com/api"
    },
    plugins: ["react-native-reanimated/plugin"]
  }
});

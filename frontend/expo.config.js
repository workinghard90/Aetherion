// frontend/expo.config.js
import 'dotenv/config';

export default ({ config }) => ({
  ...config,
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
    ios: { supportsTablet: true },
    android: {
      adaptiveIcon: {
        foregroundImage: "./assets/icon.png",
        backgroundColor: "#6200ee"
      }
    },
    platforms: ["ios", "android", "web"],
    web: {
      favicon: "./assets/favicon.png",
      bundler: "metro"
    },
    extra: {
      apiUrl:
        process.env.EXPO_PUBLIC_API_URL
          ? process.env.EXPO_PUBLIC_API_URL + "/api"
          : "https://aetherion-mobile.onrender.com/api"
    }
  }
});

import 'dotenv/config'; // (only needed if you want to load a local .env when running "expo" locally)

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
      backgroundColor: "#6200ee",
    },
    assetBundlePatterns: ["**/*"],
    ios: {
      supportsTablet: true,
    },
    android: {
      adaptiveIcon: {
        foregroundImage: "./assets/icon.png",
        backgroundColor: "#6200ee",
      },
    },
    web: {
      favicon: "./assets/favicon.png",
    },
    extra: {
      // Now you can safely reference process.env here:
      apiUrl: process.env.EXPO_PUBLIC_API_URL || "https://aetherion-mobile.onrender.com/api",
    },
  },
});

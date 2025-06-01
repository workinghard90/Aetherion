// frontend/expo.config.js
import 'dotenv/config'; 
// The above line only matters if you want locals like `EXPO_PUBLIC_API_URL` to be picked up
// when running `expo start` on your machine.  Netlify will inject `EXPO_PUBLIC_API_URL` 
// into the environment automatically during CI.

export default ({ config }) => ({
  ...config,
  expo: {
    name: "Aetherion",                   // must match the display name you want
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
    web: {
      favicon: "./assets/favicon.png"
    },
    extra: {
      // At build time, Netlify will set EXPO_PUBLIC_API_URL in its environment.
      // Locally, if that variable is not set, we default to the Render URL + "/api".
      apiUrl:
        process.env.EXPO_PUBLIC_API_URL
          ? process.env.EXPO_PUBLIC_API_URL + "/api"
          : "https://aetherion-mobile.onrender.com/api"
    }
  }
});

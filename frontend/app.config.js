import 'dotenv/config';

export default () => ({
  {
  "expo": {
    "name": "Aetherion",
    "slug": "aetherion-mobile",
    "version": "1.0.0",
    "orientation": "portrait",
    "icon": "./assets/icon.png",              // ← must exist
    "splash": {
      "image": "./assets/splash.png",         // ← must exist
      "resizeMode": "contain",
      "backgroundColor": "#6200ee"
    },
    "assetBundlePatterns": ["**/*"],
    "ios": { "supportsTablet": true },
    "android": {
      "adaptiveIcon": {
        "foregroundImage": "./assets/icon.png",   // ← same icon
        "backgroundColor": "#6200ee"
      }
    },
    "web": {
      "favicon": "./assets/favicon.png"       // ← must exist
    },
    "extra": {
      "apiUrl": "https://aetherion-mobile.onrender.com/api"
    }
  }
}

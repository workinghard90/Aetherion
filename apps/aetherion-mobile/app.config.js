// apps/aetherion-mobile/app.config.js

import 'dotenv/config';
import pkg from './package.json' assert { type: 'json' };

export default ({ config }) => ({
  name: pkg.name || 'AetherionAI',
  slug: config.slug || 'aetherion-mobile',
  version: pkg.version || '1.0.0',
  orientation: 'portrait',
  icon: './assets/icons/icon.png',
  splash: {
    image: './assets/splash/splash.png',
    resizeMode: 'contain',
    backgroundColor: '#ffffff'
  },
  updates: {
    fallbackToCacheTimeout: 0
  },
  assetBundlePatterns: ['**/*'],
  ios: {
    supportsTablet: true,
    bundleIdentifier: 'com.aetherionai.app'
  },
  android: {
    package: 'com.aetherionai.app',
    adaptiveIcon: {
      foregroundImage: './assets/icons/adaptive-icon.png',
      backgroundColor: '#ffffff'
    }
  },
  web: {
    favicon: './assets/meta/favicon.png'
  },
  extra: {
    apiUrl: process.env.EXPO_PUBLIC_API_URL || 'https://aetherionai-mobile.onrender.com',
    nodeEnv: process.env.NODE_ENV || 'development',
    appVersion: pkg.version,
    appName: pkg.name
  },
  plugins: [
    // Add Expo plugins here
  ]
});

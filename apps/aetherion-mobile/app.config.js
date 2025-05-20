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

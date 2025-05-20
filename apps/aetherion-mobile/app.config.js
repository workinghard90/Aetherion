import 'dotenv/config';

export default {
  expo: {
    name: "AetherionAI",
    slug: "aetherionai",
    extra: {
      apiUrl: process.env.REACT_NATIVE_API_URL
    }
  }
};

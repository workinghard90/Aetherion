// frontend/webpack.config.js
const createExpoWebpackConfigAsync = require("@expo/webpack-config");

module.exports = async function (env, argv) {
  // 1. let Expo generate the base Webpack config
  const config = await createExpoWebpackConfigAsync(env, argv);

  // 2. add a fallback for "stream" so that cipher-base (and other Node libraries)
  //    can resolve it in a browser context
  config.resolve.fallback = {
    ...(config.resolve.fallback || {}),
    stream: require.resolve("stream-browserify"),
  };

  return config;
};

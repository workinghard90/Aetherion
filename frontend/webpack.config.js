// frontend/webpack.config.js

const createExpoWebpackConfigAsync = require('@expo/webpack-config');

module.exports = async function envConfig(env, argv) {
  // 1) start from Expo’s default Webpack config
  const config = await createExpoWebpackConfigAsync(env, argv);

  // 2) add a fallback so that “import 'crypto'” resolves to crypto-browserify
  config.resolve = config.resolve || {};
  config.resolve.fallback = {
    ...(config.resolve.fallback || {}),
    crypto: require.resolve('crypto-browserify'),
  };

  return config;
};

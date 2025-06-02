// frontend/webpack.config.js

const createExpoWebpackConfigAsync = require('@expo/webpack-config');

module.exports = async function (env, argv) {
  // 1. Start with Expo’s default Webpack config:
  const config = await createExpoWebpackConfigAsync(env, argv);

  // 2. Ensure resolve.fallback exists, then point `crypto` (and others) to the browser polyfills:
  config.resolve.fallback = {
    ...(config.resolve.fallback || {}),
    crypto: require.resolve('crypto-browserify'),
    stream: require.resolve('stream-browserify'),
    buffer: require.resolve('buffer/'),
  };

  // 3. Provide the global Buffer (so some libraries don’t break):
  //    This injects `Buffer` into the bundle automatically.
  const BufferPolyfill = require.resolve('buffer/').replace(/\/index\.js$/, '');
  config.plugins.push(
    new (require('webpack')).ProvidePlugin({
      Buffer: [BufferPolyfill, 'Buffer'],
      process: 'process/browser', // if needed by other Node APIs
    })
  );

  return config;
};

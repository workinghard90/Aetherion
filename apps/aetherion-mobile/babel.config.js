// apps/aetherion-mobile/babel.config.js

module.exports = function (api) {
  api.cache(true);
  return {
    presets: [
      'babel-preset-expo',
      '@babel/preset-env',
      '@react-native/babel-preset'
    ],
    plugins: [
      'react-native-reanimated/plugin'
    ]
  };
};

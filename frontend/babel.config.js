module.exports = function (api) {
  api.cache(true);
  return {
    presets: ["babel-preset-expo"],
    plugins: [
      // Re-animated’s plugin must come last
      "react-native-reanimated/plugin"
    ],
  };
};

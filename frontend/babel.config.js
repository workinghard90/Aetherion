module.exports = function(api) {
  api.cache(false);
  return {
    presets: ["babel-preset-expo"],
    plugins: [
      // If you’re using React Native Reanimated v3 on web, leave this:
      "react-native-reanimated/plugin"
    ]
  };
};

module.exports = function(api) {
  api.cache(true); // Expo handles caching

  return {
    presets: ["babel-preset-expo"],
    plugins: [
      // Required by react-native-reanimated v3
      [
        "react-native-reanimated/plugin",
        {
          // no need to configure cache here; the plugin sets it internally
        }
      ]
    ]
  };
};

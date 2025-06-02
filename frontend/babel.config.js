module.exports = function (api) {
  api.cache(true);

  const presets = ["babel-preset-expo"];
  const plugins = [];

  // Only use Reanimated’s Babel plugin when _not_ building for web:
  // (Expo sets BABEL_ENV or NODE_ENV to "web" during `expo export:web`.)
  const isWeb = api.caller((caller) => caller && caller.platform === "web");
  if (!isWeb) {
    plugins.push("react-native-reanimated/plugin");
  }

  return { presets, plugins };
};

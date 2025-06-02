// frontend/App.js

import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

// Make sure these filenames match exactly what's in frontend/screens/
import OthersGate from "./screens/OthersGate";
import LoginScreen from "./screens/LoginScreen";
import HomeScreen from "./screens/HomeScreen";   // your “dashboard” screen
import VaultScreen from "./screens/VaultScreen";
import ScrollsScreen from "./screens/ScrollsScreen";
import OracleScreen from "./screens/OracleScreen";

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="OthersGate"
        screenOptions={{
          headerStyle: { backgroundColor: "#6200ee" },
          headerTintColor: "#ffffff",
          headerTitleStyle: { fontWeight: "bold" }
        }}
      >
        {/* 1) First screen: OthersGate */}
        <Stack.Screen
          name="OthersGate"
          component={OthersGate}
          options={{ title: "The Gate of Others" }}
        />

        {/* 2) After OthersGate, user taps “Login” */}
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          options={{ title: "Login to Aetherion" }}
        />

        {/* 3) Post-login: our “Dashboard” is actually your HomeScreen.js */}
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ title: "Sovereign’s Realm" }}
        />

        {/* 4) Vault button → VaultScreen */}
        <Stack.Screen
          name="Vault"
          component={VaultScreen}
          options={{ title: "🔐 The Vault" }}
        />

        {/* 5) Scrolls/Archive → ScrollsScreen */}
        <Stack.Screen
          name="Scrolls"
          component={ScrollsScreen}
          options={{ title: "📜 The Archive of Scrolls" }}
        />

        {/* 6) Oracle/Chat → OracleScreen */}
        <Stack.Screen
          name="Oracle"
          component={OracleScreen}
          options={{ title: "🔮 The Grove" }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

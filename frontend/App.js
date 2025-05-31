import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

import HomeScreen from "./screens/HomeScreen";
import LoginScreen from "./screens/LoginScreen";
import VaultScreen from "./screens/VaultScreen";
import ScrollsScreen from "./screens/ScrollsScreen";
import OracleScreen from "./screens/OracleScreen";
import OthersGate from "./screens/OthersGate";

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        {/* 1) Login */}
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          options={{
            headerShown: false,
            title: "Login"
          }}
        />
        {/* 2) OthersGate (post-login) */}
        <Stack.Screen
          name="OthersGate"
          component={OthersGate}
          options={{
            headerShown: false
          }}
        />
        {/* 3) Vault / Archive */}
        <Stack.Screen
          name="Vault"
          component={VaultScreen}
          options={{
            title: "Vault of Secure Files",
            headerStyle: { backgroundColor: "#6200ee" },
            headerTintColor: "#fff"
          }}
        />
        {/* 4) Scrolls / Archive Viewer */}
        <Stack.Screen
          name="Scrolls"
          component={ScrollsScreen}
          options={{
            title: "Library of Scrolls",
            headerStyle: { backgroundColor: "#6200ee" },
            headerTintColor: "#fff"
          }}
        />
        {/* 5) Oracle Chat */}
        <Stack.Screen
          name="Oracle"
          component={OracleScreen}
          options={{
            title: "Grove Oracle",
            headerStyle: { backgroundColor: "#6200ee" },
            headerTintColor: "#fff"
          }}
        />
        {/* 6) Home (Dashboard) */}
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{
            title: "Sanctum of Aetherion",
            headerStyle: { backgroundColor: "#6200ee" },
            headerTintColor: "#fff"
          }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

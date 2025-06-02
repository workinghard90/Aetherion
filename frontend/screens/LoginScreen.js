// Aetherion/frontend/screens/LoginScreen.js

import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Alert } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import axios from "axios";

export default function LoginScreen({ navigation }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  // Get API URL from expo config
  const apiUrl = Expo.Constants.manifest.extra.apiUrl || "https://aetherion-mobile.onrender.com/api";

  const handleLogin = async () => {
    if (!username || !password) {
      Alert.alert("Error", "Username and password cannot be empty.");
      return;
    }
    try {
      const res = await axios.post(`${apiUrl}/auth/login`, {
        username,
        password
      });
      const token = res.data.token;
      await AsyncStorage.setItem("token", token);
      navigation.replace("Dashboard");
    } catch (e) {
      Alert.alert("Login failed", e.response?.data?.error || "Unknown error");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>🔑 Sovereign Login</Text>
      <TextInput
        placeholder="Username"
        placeholderTextColor="#ccc"
        value={username}
        onChangeText={setUsername}
        style={styles.input}
        autoCapitalize="none"
      />
      <TextInput
        placeholder="Password"
        placeholderTextColor="#ccc"
        value={password}
        onChangeText={setPassword}
        style={styles.input}
        secureTextEntry
      />
      <TouchableOpacity style={styles.button} onPress={handleLogin}>
        <Text style={styles.buttonText}>Enter the Gate</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#1e1e2e",
    justifyContent: "center",
    alignItems: "center",
    padding: 20
  },
  title: {
    fontSize: 24,
    color: "#ffd1ff",
    marginBottom: 20,
    textAlign: "center"
  },
  input: {
    width: "90%",
    height: 50,
    backgroundColor: "#2c2c3e",
    borderRadius: 8,
    marginVertical: 8,
    paddingHorizontal: 12,
    color: "#fff"
  },
  button: {
    marginTop: 20,
    backgroundColor: "#6200ee",
    paddingVertical: 14,
    paddingHorizontal: 28,
    borderRadius: 8
  },
  buttonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "bold"
  }
});

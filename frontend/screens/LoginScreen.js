import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Alert } from "react-native";
import { loginUser } from "../services/api";

export default function LoginScreen({ navigation }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      const data = await loginUser({ username, password });
      // data = { token: "...", user: {...} }
      const token = data.token;
      // Store token in AsyncStorage or context
      // For now, pass it as param:
      navigation.replace("OthersGate", { token });
    } catch (err) {
      Alert.alert("Login Failed", err.response?.data?.error || err.message);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Aetherion Login</Text>
      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
        autoCapitalize="none"
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <TouchableOpacity style={styles.loginButton} onPress={handleLogin}>
        <Text style={styles.loginText}>Enter the Grove</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#0a0a0a",
    justifyContent: "center",
    padding: 20
  },
  title: {
    fontSize: 28,
    color: "#aaccff",
    textAlign: "center",
    marginBottom: 32,
    fontFamily: "Verdana"
  },
  input: {
    backgroundColor: "#222",
    color: "#fff",
    marginVertical: 8,
    padding: 12,
    borderRadius: 8
  },
  loginButton: {
    backgroundColor: "#663399",
    padding: 16,
    borderRadius: 8,
    marginTop: 24,
    alignItems: "center"
  },
  loginText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold"
  }
});

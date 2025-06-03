import React, { useState } from "react";
import {
  View,
  TextInput,
  Button,
  Text,
  Alert,
  StyleSheet,
  TouchableOpacity,
} from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import api from "./api";

export default function LoginScreen({ navigation }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    try {
      const response = await api.post("/auth/login", { username, password });
      await AsyncStorage.setItem("token", response.data.token);
      navigation.navigate("Home");
    } catch (error) {
      Alert.alert(
        "Login Failed",
        error?.response?.data?.error || "Unknown error"
      );
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>🌙 Enter Aetherion 🌙</Text>
      <TextInput
        placeholder="Username"
        placeholderTextColor="#a993ff"
        style={styles.input}
        onChangeText={setUsername}
        value={username}
      />
      <TextInput
        placeholder="Password"
        placeholderTextColor="#a993ff"
        style={styles.input}
        onChangeText={setPassword}
        value={password}
        secureTextEntry
      />
      <TouchableOpacity onPress={login} style={styles.button}>
        <Text style={styles.buttonText}>Enter</Text>
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
    paddingHorizontal: 20,
  },
  title: {
    fontSize: 26,
    color: "#e0c0ff",
    marginBottom: 24,
    fontWeight: "600",
  },
  input: {
    width: "100%",
    padding: 12,
    borderRadius: 8,
    backgroundColor: "#2d2d44",
    marginBottom: 16,
    color: "#fff",
    borderWidth: 1,
    borderColor: "#4e3a78",
  },
  button: {
    backgroundColor: "#8e44ad",
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 8,
    marginTop: 10,
  },
  buttonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "bold",
  },
});

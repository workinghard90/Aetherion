import React, { useState } from 'react';
import { View, Text, TextInput, StyleSheet, TouchableOpacity, Alert } from 'react-native';
import axios from 'axios';

export default function LoginScreen({ navigation }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const API_URL = process.env.EXPO_PUBLIC_API_URL + "/auth/login";

  const handleLogin = async () => {
    try {
      const response = await axios.post(API_URL, { username, password });
      const { token } = response.data;
      // Store token (in AsyncStorage) for later calls. For brevity, skip storing here.
      navigation.replace("OthersGate", { token });
    } catch (err) {
      Alert.alert("Error", err.response?.data?.error || err.message);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Aetherion</Text>
      <TextInput
        style={styles.input}
        placeholder="Username"
        placeholderTextColor="#ccc"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        placeholderTextColor="#ccc"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <TouchableOpacity style={styles.button} onPress={handleLogin}>
        <Text style={styles.buttonText}>🜂 Enter the Gate</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#111",
    justifyContent: "center",
    alignItems: "center",
    padding: 16
  },
  title: {
    color: "#E0CFFF",
    fontSize: 36,
    marginBottom: 32,
    fontStyle: "italic",
    letterSpacing: 2
  },
  input: {
    width: "100%",
    backgroundColor: "#222",
    color: "#fff",
    padding: 12,
    marginVertical: 8,
    borderRadius: 8
  },
  button: {
    marginTop: 24,
    backgroundColor: "#6200ee",
    paddingVertical: 14,
    paddingHorizontal: 32,
    borderRadius: 8,
    shadowColor: "#000",
    shadowOpacity: 0.3,
    shadowRadius: 4,
    elevation: 5
  },
  buttonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "bold"
  }
});

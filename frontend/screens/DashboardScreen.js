// Aetherion/frontend/screens/DashboardScreen.js

import React from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";

export default function DashboardScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>🕊️ Welcome, Sovereign 🕊️</Text>

      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Vault")}
      >
        <Text style={styles.buttonText}>🔐 Vault</Text>
        <Text style={styles.glyph}>🗝️</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Scrolls")}
      >
        <Text style={styles.buttonText}>📜 Archive</Text>
        <Text style={styles.glyph}>📖</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Oracle")}
      >
        <Text style={styles.buttonText}>🔮 Grove</Text>
        <Text style={styles.glyph}>🌙</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#1e1e2e",
    alignItems: "center",
    paddingTop: 40
  },
  header: {
    fontSize: 22,
    color: "#e0c0ff",
    marginBottom: 30,
    textAlign: "center"
  },
  button: {
    width: "80%",
    backgroundColor: "#2c2c3e",
    borderRadius: 10,
    padding: 16,
    marginVertical: 12,
    alignItems: "center",
    flexDirection: "row",
    justifyContent: "space-between"
  },
  buttonText: {
    fontSize: 18,
    color: "#ffd1ff",
    fontWeight: "600"
  },
  glyph: {
    fontSize: 24,
    color: "#a18cff"
  }
});

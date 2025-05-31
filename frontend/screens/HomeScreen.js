import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';

export default function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>Aetherion</Text>
      <TouchableOpacity style={styles.button} onPress={() => navigation.navigate("Vault")}>
        <Text style={styles.buttonText}>🔐 Vault</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button} onPress={() => navigation.navigate("Scrolls")}>
        <Text style={styles.buttonText}>📜 Archive</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button} onPress={() => navigation.navigate("Oracle")}>
        <Text style={styles.buttonText}>🌳 The Grove</Text>
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
  header: {
    color: "#E0CFFF",
    fontSize: 36,
    marginBottom: 48,
    fontFamily: "serif"
  },
  button: {
    backgroundColor: "#3a0070",
    paddingVertical: 16,
    paddingHorizontal: 48,
    borderRadius: 8,
    marginVertical: 12,
    shadowColor: "#000",
    shadowOpacity: 0.4,
    shadowRadius: 6,
    elevation: 6
  },
  buttonText: {
    color: "#fff",
    fontSize: 20,
    fontWeight: "600"
  }
});

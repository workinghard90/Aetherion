import React from "react";
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  ScrollView,
} from "react-native";

export default function HomeScreen({ navigation }) {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>✨ Welcome to Aetherion ✨</Text>

      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Vault")}
      >
        <Text style={styles.buttonText}>Enter Vault</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Scrolls")}
      >
        <Text style={styles.buttonText}>Sacred Scrolls</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Oracle")}
      >
        <Text style={styles.buttonText}>Grove Oracle</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    backgroundColor: "#1e1e2e",
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
  },
  title: {
    fontSize: 28,
    color: "#e0c0ff",
    fontWeight: "bold",
    marginBottom: 30,
    textAlign: "center",
  },
  button: {
    backgroundColor: "#8e44ad",
    paddingVertical: 14,
    paddingHorizontal: 40,
    borderRadius: 10,
    marginVertical: 10,
    width: "80%",
    alignItems: "center",
    shadowColor: "#000",
    shadowOpacity: 0.3,
    shadowRadius: 5,
    shadowOffset: { width: 0, height: 3 },
  },
  buttonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "bold",
  },
});

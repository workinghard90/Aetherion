import React, { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  ScrollView,
  ActivityIndicator,
} from "react-native";
import { getOracleInsights } from "../services/api";

export default function OracleScreen() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!prompt.trim()) return;

    setLoading(true);
    const data = await getOracleInsights(prompt);
    setResult(JSON.stringify(data, null, 2));
    setLoading(false);
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🌿 Grove Oracle</Text>

      <TextInput
        style={styles.input}
        placeholder="Ask the Oracle..."
        placeholderTextColor="#bbb"
        onChangeText={setPrompt}
        value={prompt}
      />

      <TouchableOpacity style={styles.button} onPress={handleSubmit}>
        {loading ? (
          <ActivityIndicator color="#fff" />
        ) : (
          <Text style={styles.buttonText}>Seek Insight</Text>
        )}
      </TouchableOpacity>

      {result ? (
        <View style={styles.resultContainer}>
          <Text style={styles.resultText}>{result}</Text>
        </View>
      ) : null}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    backgroundColor: "#1e1e2e",
    justifyContent: "flex-start",
    alignItems: "center",
    padding: 20,
  },
  title: {
    fontSize: 26,
    color: "#e0c0ff",
    fontWeight: "bold",
    marginBottom: 20,
    textAlign: "center",
  },
  input: {
    width: "90%",
    height: 50,
    backgroundColor: "#2a2a3e",
    borderRadius: 8,
    paddingHorizontal: 15,
    color: "#fff",
    marginBottom: 20,
    fontSize: 16,
  },
  button: {
    backgroundColor: "#8e44ad",
    paddingVertical: 14,
    paddingHorizontal: 50,
    borderRadius: 10,
    marginBottom: 20,
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
  resultContainer: {
    width: "90%",
    backgroundColor: "#2a2a3e",
    borderRadius: 8,
    padding: 15,
    marginTop: 10,
  },
  resultText: {
    color: "#fff",
    fontSize: 14,
  },
});

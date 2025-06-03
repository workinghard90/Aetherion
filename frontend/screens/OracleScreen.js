import React, { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  ActivityIndicator,
  StyleSheet,
  Alert,
} from "react-native";
import { getOracleInsights } from "../services/api";

export default function OracleScreen() {
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    if (!prompt.trim()) {
      Alert.alert("Error", "Please enter a prompt");
      return;
    }
    setLoading(true);
    try {
      const res = await getOracleInsights(prompt);
      setResult(res);
    } catch (err) {
      Alert.alert("Error", err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🌿 Grove Oracle</Text>
      <TextInput
        style={styles.input}
        placeholder="Ask the oracle..."
        placeholderTextColor="#aaa"
        multiline
        value={prompt}
        onChangeText={setPrompt}
      />
      <TouchableOpacity style={styles.button} onPress={handleSubmit}>
        {loading ? (
          <ActivityIndicator size="small" color="#fff" />
        ) : (
          <Text style={styles.buttonText}>Get Insights</Text>
        )}
      </TouchableOpacity>

      {result && (
        <View style={styles.resultContainer}>
          <Text style={styles.resultText}>
            {JSON.stringify(result, null, 2)}
          </Text>
        </View>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    backgroundColor: "#1e1e2e",
    padding: 20,
  },
  title: {
    fontSize: 24,
    color: "#e0c0ff",
    marginBottom: 20,
    textAlign: "center",
  },
  input: {
    backgroundColor: "#2e2e3e",
    color: "#fff",
    padding: 12,
    borderRadius: 8,
    marginBottom: 12,
    height: 100,
    textAlignVertical: "top",
  },
  button: {
    backgroundColor: "#8e44ad",
    padding: 14,
    borderRadius: 8,
    alignItems: "center",
    marginBottom: 20,
  },
  buttonText: {
    color: "#fff",
    fontSize: 16,
  },
  resultContainer: {
    backgroundColor: "#2e2e3e",
    padding: 12,
    borderRadius: 8,
  },
  resultText: {
    color: "#fff",
    fontSize: 14,
  },
});

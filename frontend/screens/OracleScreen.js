import React, { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  Alert,
  ScrollView,
} from "react-native";
import api from "./api";

export default function OracleScreen() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");

  const askOracle = async () => {
    if (!question.trim()) {
      Alert.alert("Wait", "Please ask something first.");
      return;
    }

    try {
      const res = await api.post("/oracle", { question });
      setResponse(res.data.response);
    } catch (error) {
      Alert.alert("Error", "Oracle could not speak at this time.");
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🔮 Grove Oracle</Text>

      <TextInput
        placeholder="Speak your question..."
        placeholderTextColor="#a993ff"
        style={styles.input}
        value={question}
        onChangeText={setQuestion}
        multiline
      />

      <TouchableOpacity style={styles.button} onPress={askOracle}>
        <Text style={styles.buttonText}>Ask</Text>
      </TouchableOpacity>

      {response ? (
        <View style={styles.responseBox}>
          <Text style={styles.responseLabel}>Response:</Text>
          <Text style={styles.response}>{response}</Text>
        </View>
      ) : null}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    backgroundColor: "#1e1e2e",
    padding: 20,
    alignItems: "center",
    justifyContent: "center",
  },
  title: {
    fontSize: 24,
    color: "#e0c0ff",
    fontWeight: "bold",
    marginBottom: 20,
    textAlign: "center",
  },
  input: {
    width: "100%",
    backgroundColor: "#2d2d44",
    color: "#fff",
    borderRadius: 8,
    padding: 12,
    borderWidth: 1,
    borderColor: "#4e3a78",
    fontSize: 14,
    textAlignVertical: "top",
    marginBottom: 16,
    minHeight: 100,
  },
  button: {
    backgroundColor: "#8e44ad",
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 8,
    marginBottom: 20,
  },
  buttonText: {
    color: "#fff",
    fontWeight: "bold",
    fontSize: 16,
  },
  responseBox: {
    width: "100%",
    backgroundColor: "#2d2d44",
    padding: 12,
    borderRadius: 8,
    borderColor: "#6d50a6",
    borderWidth: 1,
  },
  responseLabel: {
    color: "#ffd1ff",
    fontWeight: "bold",
    marginBottom: 6,
    fontSize: 14,
  },
  response: {
    color: "#caa7ff",
    fontSize: 14,
    fontStyle: "italic",
  },
});

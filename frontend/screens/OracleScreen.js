// Aetherion/frontend/screens/OracleScreen.js

import React, { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  FlatList,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
} from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import axios from "axios";

export default function OracleScreen() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([
    { id: 1, from: "oracle", text: "Welcome, sovereign. How may I guide you?" },
  ]);

  const apiUrl = process.env.API_URL || "https://aetherion.onrender.com/api";

  const askOracle = async () => {
    if (!question.trim()) return;

    setMessages((prev) => [
      ...prev,
      { id: Date.now(), from: "you", text: question },
    ]);
    setQuestion("");

    try {
      const token = await AsyncStorage.getItem("token");
      const res = await axios.post(
        `${apiUrl}/oracle`,
        { question },
        {
          headers: token ? { Authorization: `Bearer ${token}` } : {},
        }
      );
      setMessages((prev) => [
        ...prev,
        { id: Date.now() + 1, from: "oracle", text: res.data.answer },
      ]);
    } catch (e) {
      console.error(e);
      setMessages((prev) => [
        ...prev,
        { id: Date.now() + 1, from: "oracle", text: "The Grove is silent..." },
      ]);
    }
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.select({ ios: "padding", android: null })}
    >
      <Text style={styles.header}>🔮 The Grove</Text>

      <FlatList
        data={messages}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View
            style={[
              styles.msgBubble,
              item.from === "you" ? styles.youBubble : styles.oracleBubble,
            ]}
          >
            <Text
              style={[
                styles.msgText,
                item.from === "you" ? styles.youText : styles.oracleText,
              ]}
            >
              {item.text}
            </Text>
          </View>
        )}
        style={styles.msgList}
      />

      <View style={styles.inputContainer}>
        <TextInput
          placeholder="Ask the Grove..."
          placeholderTextColor="#aaa"
          value={question}
          onChangeText={setQuestion}
          style={styles.input}
        />
        <TouchableOpacity style={styles.sendBtn} onPress={askOracle}>
          <Text style={styles.sendText}>↩︎</Text>
        </TouchableOpacity>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#1e1e2e",
    paddingTop: 20,
  },
  header: {
    fontSize: 22,
    color: "#e0c0ff",
    textAlign: "center",
    marginBottom: 12,
  },
  msgList: {
    flex: 1,
    paddingHorizontal: 16,
  },
  msgBubble: {
    borderRadius: 8,
    marginVertical: 6,
    padding: 10,
    maxWidth: "80%",
  },
  youBubble: {
    backgroundColor: "#2c2c3e",
    alignSelf: "flex-end",
  },
  oracleBubble: {
    backgroundColor: "#42297e",
    alignSelf: "flex-start",
  },
  youText: {
    color: "#ffd1ff",
    fontSize: 14,
  },
  oracleText: {
    color: "#fff",
    fontSize: 14,
  },
  inputContainer: {
    flexDirection: "row",
    alignItems: "center",
    padding: 8,
    backgroundColor: "#2c2c3e",
  },
  input: {
    flex: 1,
    height: 40,
    paddingHorizontal: 12,
    borderRadius: 8,
    backgroundColor: "#1e1e2e",
    color: "#fff",
  },
  sendBtn: {
    marginLeft: 8,
    backgroundColor: "#6200ee",
    padding: 10,
    borderRadius: 8,
  },
  sendText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold",
  },
});

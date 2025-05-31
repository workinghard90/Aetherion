import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  FlatList,
  StyleSheet,
  ActivityIndicator,
  Alert
} from "react-native";
import { getEntityById } from "../services/api";

export default function OracleScreen({ route }) {
  const { token } = route.params;
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  // This is a placeholder – you need an actual AI/chat backend
  const handleSend = async () => {
    if (!input.trim()) return;
    setLoading(true);
    // Simulate an API call to “Grove Oracle”
    try {
      // Example: await call to `/api/oracle`
      setMessages((prev) => [...prev, { from: "user", text: input }]);
      // Simulate response
      setTimeout(() => {
        setMessages((prev) => [
          ...prev,
          { from: "grove", text: `Grove: You said "${input}"` }
        ]);
        setLoading(false);
      }, 1000);
    } catch (err) {
      Alert.alert("Oracle Error", err.message || err);
      setLoading(false);
    }
    setInput("");
  };

  if (loading) {
    return (
      <View style={styles.centered}>
        <ActivityIndicator size="large" color="#663399" />
        <Text style={styles.loadingText}>The Grove is pondering…</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <FlatList
        data={messages}
        keyExtractor={(item, idx) => idx.toString()}
        renderItem={({ item }) => (
          <View
            style={[
              styles.messageBubble,
              item.from === "user"
                ? styles.userBubble
                : styles.groveBubble
            ]}
          >
            <Text style={styles.messageText}>{item.text}</Text>
          </View>
        )}
        inverted
      />
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.input}
          placeholder="Ask the Grove…"
          placeholderTextColor="#ccc"
          value={input}
          onChangeText={setInput}
        />
        <TouchableOpacity style={styles.sendButton} onPress={handleSend}>
          <Text style={styles.sendText}>🕯️</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#0a0a0a",
    padding: 16
  },
  centered: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center"
  },
  loadingText: {
    marginTop: 12,
    color: "#ddd",
    fontSize: 16
  },
  messageBubble: {
    marginVertical: 6,
    padding: 12,
    borderRadius: 8,
    maxWidth: "70%"
  },
  userBubble: {
    backgroundColor: "#663399",
    alignSelf: "flex-end"
  },
  groveBubble: {
    backgroundColor: "#333",
    alignSelf: "flex-start"
  },
  messageText: {
    color: "#fff"
  },
  inputContainer: {
    flexDirection: "row",
    alignItems: "center",
    marginTop: 8,
    borderTopColor: "#333",
    borderTopWidth: 1,
    paddingTop: 8
  },
  input: {
    flex: 1,
    backgroundColor: "#222",
    color: "#fff",
    padding: 10,
    borderRadius: 8
  },
  sendButton: {
    marginLeft: 8,
    backgroundColor: "#663399",
    padding: 12,
    borderRadius: 8
  },
  sendText: {
    color: "#fff",
    fontSize: 18
  }
});

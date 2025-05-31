import React, { useState } from 'react';
import { View, Text, TextInput, StyleSheet, TouchableOpacity, FlatList, KeyboardAvoidingView, Platform } from 'react-native';
import axios from 'axios';
import { getToken } from '../services/api';

export default function OracleScreen() {
  const [messages, setMessages] = useState([{ role: "system", content: "You are the Grove, a gentle oracle." }]);
  const [input, setInput] = useState("");
  const API_URL = process.env.EXPO_PUBLIC_API_URL + "/oracle";

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg = { role: "user", content: input };
    const updated = [...messages, userMsg];
    setMessages(updated);
    setInput("");
    try {
      const token = await getToken();
      const res = await axios.post(API_URL, { messages: updated }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setMessages([...updated, { role: "assistant", content: res.data.reply }]);
    } catch (err) {
      setMessages([...updated, { role: "assistant", content: "Error contacting the Grove." }]);
    }
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === "ios" ? "padding" : undefined}
    >
      <FlatList
        data={messages}
        keyExtractor={(_, idx) => idx.toString()}
        style={styles.chatList}
        renderItem={({ item }) => (
          <View style={[styles.msgBubble, item.role === "user" ? styles.userBubble : styles.groveBubble]}>
            <Text style={styles.msgText}>{item.content}</Text>
          </View>
        )}
      />
      <View style={styles.inputRow}>
        <TextInput
          style={styles.input}
          placeholder="Ask the Grove..."
          placeholderTextColor="#999"
          value={input}
          onChangeText={setInput}
        />
        <TouchableOpacity style={styles.sendBtn} onPress={sendMessage}>
          <Text style={styles.sendText}>➤</Text>
        </TouchableOpacity>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#111",
    padding: 12
  },
  chatList: {
    flex: 1
  },
  msgBubble: {
    marginVertical: 6,
    padding: 12,
    borderRadius: 8,
    maxWidth: "75%"
  },
  userBubble: {
    alignSelf: "flex-end",
    backgroundColor: "#6200ee"
  },
  groveBubble: {
    alignSelf: "flex-start",
    backgroundColor: "#3a0050"
  },
  msgText: {
    color: "#fff",
    fontSize: 14
  },
  inputRow: {
    flexDirection: "row",
    paddingVertical: 8,
    borderTopWidth: 1,
    borderTopColor: "#333"
  },
  input: {
    flex: 1,
    backgroundColor: "#222",
    color: "#fff",
    borderRadius: 8,
    paddingHorizontal: 12
  },
  sendBtn: {
    marginLeft: 8,
    backgroundColor: "#6200ee",
    padding: 12,
    borderRadius: 8,
    justifyContent: "center",
    alignItems: "center"
  },
  sendText: {
    color: "#fff",
    fontSize: 18
  }
});

import React, { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  ScrollView,
  Alert,
} from "react-native";
import { uploadMemory, downloadMemory } from "../services/api";

export default function VaultScreen() {
  const [content, setContent] = useState("");
  const [downloaded, setDownloaded] = useState("");

  const handleUpload = async () => {
    if (!content.trim()) {
      Alert.alert("Error", "Please write something before uploading.");
      return;
    }
    await uploadMemory(content);
    Alert.alert("Success", "Memory uploaded and encrypted.");
    setContent("");
  };

  const handleDownload = async () => {
    try {
      const data = await downloadMemory(1); // Example: using id=1
      setDownloaded(data.content);
    } catch (error) {
      Alert.alert("Error", "Unable to download that memory.");
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🔒 The Vault</Text>

      <TextInput
        style={styles.input}
        placeholder="Write your memory..."
        placeholderTextColor="#bbb"
        multiline
        numberOfLines={4}
        onChangeText={setContent}
        value={content}
      />

      <TouchableOpacity style={styles.button} onPress={handleUpload}>
        <Text style={styles.buttonText}>Upload Memory</Text>
      </TouchableOpacity>

      <TouchableOpacity style={[styles.button, styles.downloadButton]} onPress={handleDownload}>
        <Text style={styles.buttonText}>Download Memory #1</Text>
      </TouchableOpacity>

      {downloaded ? (
        <View style={styles.resultContainer}>
          <Text style={styles.label}>Decrypted Content:</Text>
          <Text style={styles.resultText}>{downloaded}</Text>
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
    backgroundColor: "#2a2a3e",
    borderRadius: 8,
    paddingHorizontal: 15,
    paddingVertical: 10,
    color: "#fff",
    fontSize: 16,
    marginBottom: 20,
    textAlignVertical: "top",
  },
  button: {
    backgroundColor: "#8e44ad",
    paddingVertical: 14,
    paddingHorizontal: 50,
    borderRadius: 10,
    marginVertical: 10,
    width: "80%",
    alignItems: "center",
    shadowColor: "#000",
    shadowOpacity: 0.3,
    shadowRadius: 5,
    shadowOffset: { width: 0, height: 3 },
  },
  downloadButton: {
    backgroundColor: "#34495e",
  },
  buttonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "bold",
  },
  resultContainer: {
    marginTop: 20,
    width: "90%",
    backgroundColor: "#2a2a3e",
    borderRadius: 8,
    padding: 15,
  },
  label: {
    color: "#e0c0ff",
    fontWeight: "bold",
    marginBottom: 5,
    fontSize: 16,
  },
  resultText: {
    color: "#fff",
    fontSize: 14,
  },
});

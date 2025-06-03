import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  FlatList,
  StyleSheet,
  TouchableOpacity,
  Alert,
} from "react-native";
import * as DocumentPicker from "expo-document-picker";
import api from "./api";

export default function VaultScreen() {
  const [files, setFiles] = useState([]);

  const loadFiles = async () => {
    try {
      const res = await api.get("/vault/list");
      setFiles(res.data);
    } catch (err) {
      Alert.alert("Error loading files", err.message);
    }
  };

  useEffect(() => {
    loadFiles();
  }, []);

  const upload = async () => {
    const doc = await DocumentPicker.getDocumentAsync({ type: "*/*" });
    if (doc.canceled) return;

    const formData = new FormData();
    formData.append("file", {
      uri: doc.assets[0].uri,
      name: doc.assets[0].name,
      type: "*/*",
    });

    try {
      await api.post("/vault/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      loadFiles();
    } catch (err) {
      Alert.alert("Upload failed", err.message);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>🔐 Aetherion Vault</Text>

      <TouchableOpacity style={styles.button} onPress={upload}>
        <Text style={styles.buttonText}>Upload File</Text>
      </TouchableOpacity>

      <FlatList
        data={files}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <Text style={styles.fileItem}>📄 {item.original_name}</Text>
        )}
        ListEmptyComponent={
          <Text style={styles.noFiles}>No files yet in your Vault.</Text>
        }
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#1e1e2e",
    padding: 20,
  },
  title: {
    fontSize: 24,
    color: "#e0c0ff",
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 20,
  },
  button: {
    backgroundColor: "#8e44ad",
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 10,
    alignSelf: "center",
    marginBottom: 20,
  },
  buttonText: {
    color: "#fff",
    fontWeight: "bold",
    fontSize: 16,
  },
  fileItem: {
    color: "#caa7ff",
    fontSize: 14,
    marginVertical: 4,
    fontStyle: "italic",
  },
  noFiles: {
    color: "#777",
    textAlign: "center",
    marginTop: 10,
  },
});

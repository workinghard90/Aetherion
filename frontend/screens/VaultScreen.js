import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity, Alert } from 'react-native';
import * as DocumentPicker from 'expo-document-picker';
import axios from 'axios';
import { getToken } from '../services/api';

export default function VaultScreen() {
  const [files, setFiles] = useState([]);

  const API_URL = process.env.EXPO_PUBLIC_API_URL + "/vault";

  const fetchFiles = async () => {
    try {
      const token = await getToken();
      const res = await axios.get(`${API_URL}/list`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setFiles(res.data.files);
    } catch (err) {
      Alert.alert("Error", err.message);
    }
  };

  const handleUpload = async () => {
    try {
      const token = await getToken();
      const result = await DocumentPicker.getDocumentAsync({});
      if (result.type === "success") {
        const formData = new FormData();
        formData.append("file", {
          uri: result.uri,
          name: result.name,
          type: result.mimeType || "application/octet-stream"
        });
        await axios.post(`${API_URL}/upload`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${token}`
          }
        });
        fetchFiles();
      }
    } catch (err) {
      Alert.alert("Upload error", err.message);
    }
  };

  useEffect(() => {
    fetchFiles();
  }, []);

  return (
    <View style={styles.container}>
      <TouchableOpacity style={styles.uploadBtn} onPress={handleUpload}>
        <Text style={styles.uploadText}>⬆️ Upload to Vault</Text>
      </TouchableOpacity>
      <Text style={styles.heading}>Stored Files</Text>
      <FlatList
        data={files}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={styles.fileRow}
            onPress={() => Alert.alert("Download", `Downloading ${item.original_name}`)}
          >
            <Text style={styles.fileName}>{item.original_name}</Text>
          </TouchableOpacity>
        )}
        ListEmptyComponent={<Text style={styles.empty}>No files in vault.</Text>}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#111",
    padding: 16
  },
  uploadBtn: {
    backgroundColor: "#6200ee",
    padding: 14,
    borderRadius: 8,
    marginBottom: 16,
    alignItems: "center"
  },
  uploadText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "600"
  },
  heading: {
    color: "#E0CFFF",
    fontSize: 24,
    marginBottom: 12
  },
  fileRow: {
    backgroundColor: "#222",
    padding: 12,
    marginVertical: 6,
    borderRadius: 6
  },
  fileName: {
    color: "#fff",
    fontSize: 16
  },
  empty: {
    color: "#aaa",
    fontSize: 16,
    marginTop: 20,
    textAlign: "center"
  }
});

// Aetherion/frontend/screens/VaultScreen.js

import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  FlatList,
  Alert,
  Platform
} from "react-native";
import * as DocumentPicker from "expo-document-picker";
import AsyncStorage from "@react-native-async-storage/async-storage";
import axios from "axios";

export default function VaultScreen() {
  const [files, setFiles] = useState([]);

  const apiUrl = Expo.Constants.manifest.extra.apiUrl;

  useEffect(() => {
    fetchFiles();
  }, []);

  const fetchFiles = async () => {
    try {
      const token = await AsyncStorage.getItem("token");
      const res = await axios.get(`${apiUrl}/vault/list`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setFiles(res.data);
    } catch (e) {
      console.error(e);
      Alert.alert("Error", "Failed to fetch your files.");
    }
  };

  const pickAndUpload = async () => {
    let result = await DocumentPicker.getDocumentAsync({});
    if (result.type === "success") {
      const fileUri = result.uri;
      const fileName = result.name;
      const fileType = result.mimeType || "application/octet-stream";

      let formData = new FormData();
      formData.append("file", {
        uri: fileUri,
        name: fileName,
        type: fileType
      });

      try {
        const token = await AsyncStorage.getItem("token");
        await axios.post(`${apiUrl}/vault/upload`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${token}`
          }
        });
        fetchFiles();
      } catch (e) {
        console.error(e);
        Alert.alert("Error", "Upload failed.");
      }
    }
  };

  const downloadFile = async (id, originalName) => {
    try {
      const token = await AsyncStorage.getItem("token");
      const res = await axios.get(`${apiUrl}/vault/download/${id}`, {
        responseType: "blob",
        headers: { Authorization: `Bearer ${token}` }
      });

      // On mobile, you’d need FileSystem, but for brevity we'll just alert:
      Alert.alert("Download", `File "${originalName}" downloaded.`);
    } catch (e) {
      console.error(e);
      Alert.alert("Error", "Download failed.");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>🔐 The Vault</Text>
      <TouchableOpacity style={styles.uploadButton} onPress={pickAndUpload}>
        <Text style={styles.uploadText}>Upload a Scroll</Text>
      </TouchableOpacity>

      <FlatList
        data={files}
        keyExtractor={(item) => item.id.toString()}
        ListEmptyComponent={<Text style={styles.empty}>No files yet.</Text>}
        renderItem={({ item }) => (
          <View style={styles.fileRow}>
            <Text style={styles.fileName}>{item.original_name}</Text>
            <TouchableOpacity
              style={styles.downloadBtn}
              onPress={() => downloadFile(item.id, item.original_name)}
            >
              <Text style={styles.downloadText}>↧</Text>
            </TouchableOpacity>
          </View>
        )}
        style={{ width: "90%" }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#1e1e2e",
    alignItems: "center",
    paddingTop: 30
  },
  header: {
    fontSize: 22,
    color: "#e0c0ff",
    marginBottom: 16
  },
  uploadButton: {
    backgroundColor: "#6200ee",
    padding: 14,
    borderRadius: 8,
    marginBottom: 20
  },
  uploadText: {
    color: "#fff",
    fontWeight: "bold"
  },
  empty: {
    marginTop: 40,
    color: "#bbb",
    fontStyle: "italic",
    textAlign: "center"
  },
  fileRow: {
    flexDirection: "row",
    justifyContent: "space-between",
    backgroundColor: "#2c2c3e",
    padding: 12,
    borderRadius: 8,
    marginVertical: 6
  },
  fileName: {
    color: "#ffd1ff",
    fontSize: 16
  },
  downloadBtn: {
    backgroundColor: "#a18cff",
    borderRadius: 6,
    paddingHorizontal: 10,
    justifyContent: "center"
  },
  downloadText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold"
  }
});

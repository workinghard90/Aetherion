import React, { useState } from "react";
import { View, Text, TouchableOpacity, StyleSheet, Alert, Platform } from "react-native";
import * as DocumentPicker from "expo-document-picker";
import { uploadFile } from "../services/api";

export default function VaultScreen({ route }) {
  const { token } = route.params;
  const [fileName, setFileName] = useState("");

  const handlePickFile = async () => {
    try {
      const result = await DocumentPicker.getDocumentAsync({});
      if (result.type === "success") {
        setFileName(result.name);
        const uploadResult = await uploadFile(
          result, // result object contains `uri`, so you may need to fetch file blob
          token
        );
        Alert.alert("Success", `File uploaded with ID: ${uploadResult.file_id}`);
      }
    } catch (err) {
      Alert.alert("Error", err.message || err);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Vault</Text>
      <TouchableOpacity style={styles.button} onPress={handlePickFile}>
        <Text style={styles.buttonText}>Upload File</Text>
      </TouchableOpacity>
      {fileName ? <Text style={styles.fileLabel}>Picked: {fileName}</Text> : null}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#0a0a0a",
    padding: 16,
    justifyContent: "center",
    alignItems: "center"
  },
  title: {
    color: "#fff",
    fontSize: 22,
    marginBottom: 24
  },
  button: {
    backgroundColor: "#663399",
    padding: 14,
    borderRadius: 6
  },
  buttonText: {
    color: "#fff",
    fontSize: 16
  },
  fileLabel: {
    marginTop: 16,
    color: "#ccc"
  }
});

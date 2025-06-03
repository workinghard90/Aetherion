// Aetherion/frontend/screens/ScrollsScreen.js

import React, { useEffect, useState } from "react";
import { View, Text, TouchableOpacity, FlatList, StyleSheet, Alert } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import axios from "axios";

export default function ScrollsScreen() {
  const [scrolls, setScrolls] = useState([]);
  const apiUrl = process.env.API_URL || "https://aetherion.onrender.com/api";

  useEffect(() => {
    fetchScrolls();
  }, []);

  const fetchScrolls = async () => {
    try {
      const res = await axios.get(`${apiUrl}/archive`);
      setScrolls(res.data);
    } catch (e) {
      console.error(e);
      Alert.alert("Error", "Failed to fetch scrolls.");
    }
  };

  const viewScroll = async (id) => {
    try {
      const token = await AsyncStorage.getItem("token");
      const res = await axios.get(`${apiUrl}/archive/${id}`, {
        responseType: "blob",
        headers: token ? { Authorization: `Bearer ${token}` } : {},
      });
      Alert.alert("Scroll fetched", `Scroll ${id} fetched successfully.`);
    } catch (e) {
      console.error(e);
      Alert.alert("Error", "Failed to load scroll.");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>📜 Archive of Scrolls</Text>
      <FlatList
        data={scrolls}
        keyExtractor={(item) => item.id.toString()}
        ListEmptyComponent={
          <Text style={styles.empty}>No scrolls in the archive.</Text>
        }
        renderItem={({ item }) => (
          <TouchableOpacity
            style={styles.scrollRow}
            onPress={() => viewScroll(item.id)}
          >
            <Text style={styles.scrollName}>{item.original_name}</Text>
            <Text style={styles.scrollMeta}>
              uploaded by {item.user_id} on{" "}
              {new Date(item.uploaded_at).toLocaleDateString()}
            </Text>
          </TouchableOpacity>
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
    paddingTop: 30,
  },
  header: {
    fontSize: 22,
    color: "#e0c0ff",
    marginBottom: 16,
  },
  empty: {
    marginTop: 40,
    color: "#bbb",
    fontStyle: "italic",
    textAlign: "center",
  },
  scrollRow: {
    backgroundColor: "#2c2c3e",
    padding: 12,
    borderRadius: 8,
    marginVertical: 6,
  },
  scrollName: {
    color: "#ffd1ff",
    fontSize: 16,
  },
  scrollMeta: {
    fontSize: 12,
    color: "#aaa",
    marginTop: 4,
  },
});

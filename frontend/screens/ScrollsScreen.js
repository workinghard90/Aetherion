import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  FlatList,
  StyleSheet,
  Alert,
  TouchableOpacity,
} from "react-native";
import api from "./api";

export default function ScrollsScreen() {
  const [scrolls, setScrolls] = useState([]);

  const loadScrolls = async () => {
    try {
      const response = await api.get("/archive");
      setScrolls(response.data);
    } catch (error) {
      Alert.alert("Error", "Unable to load scrolls.");
    }
  };

  useEffect(() => {
    loadScrolls();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>📜 Sacred Scrolls Archive</Text>

      <FlatList
        data={scrolls}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <TouchableOpacity>
            <Text style={styles.scrollItem}>📖 {item.title}</Text>
          </TouchableOpacity>
        )}
        ListEmptyComponent={
          <Text style={styles.noScrolls}>No scrolls found in the archive.</Text>
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
  scrollItem: {
    color: "#caa7ff",
    fontSize: 14,
    marginVertical: 6,
    fontStyle: "italic",
  },
  noScrolls: {
    color: "#888",
    fontSize: 13,
    textAlign: "center",
    marginTop: 10,
  },
});

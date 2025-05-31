import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  Alert
} from "react-native";
import { getScrolls } from "../services/api";

export default function ScrollsScreen() {
  const [scrolls, setScrolls] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchScrolls();
  }, []);

  const fetchScrolls = async () => {
    try {
      const data = await getScrolls();
      setScrolls(data);
    } catch (err) {
      setError("Failed to load scrolls.");
      Alert.alert("Error", err.message || err);
    }
  };

  if (error) {
    return (
      <View style={styles.centered}>
        <Text style={styles.errorText}>{error}</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <FlatList
        data={scrolls}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <TouchableOpacity style={styles.scrollItem}>
            <Text style={styles.scrollTitle}>{item.title}</Text>
            <Text style={styles.scrollDesc}>{item.description}</Text>
          </TouchableOpacity>
        )}
        ListEmptyComponent={<Text style={styles.emptyText}>No scrolls found.</Text>}
      />
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
  scrollItem: {
    backgroundColor: "#222",
    padding: 14,
    marginVertical: 6,
    borderRadius: 6
  },
  scrollTitle: {
    color: "#fff",
    fontSize: 18
  },
  scrollDesc: {
    color: "#ccc",
    fontSize: 14,
    marginTop: 4
  },
  emptyText: {
    marginTop: 32,
    textAlign: "center",
    color: "#777"
  },
  errorText: {
    color: "#ff6666"
  }
});

import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  ActivityIndicator,
  Alert
} from "react-native";
import { getUniverse } from "../services/api";

export default function HomeScreen({ route, navigation }) {
  const { token } = route.params;
  const [entities, setEntities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchEntities();
  }, []);

  const fetchEntities = async () => {
    try {
      setLoading(true);
      const data = await getUniverse();
      setEntities(data);
    } catch (err) {
      setError("Failed to load the universe. Please try again.");
      Alert.alert("Error", err.message || err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.centered}>
        <ActivityIndicator size="large" color="#663399" />
        <Text style={styles.loadingText}>Aligning cosmic patterns…</Text>
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.centered}>
        <Text style={styles.errorText}>{error}</Text>
        <TouchableOpacity
          style={styles.retryButton}
          onPress={fetchEntities}
        >
          <Text style={styles.retryText}>Retry</Text>
        </TouchableOpacity>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <FlatList
        data={entities}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <TouchableOpacity style={styles.item} onPress={() => navigation.navigate("Oracle", { id: item.id, token })}>
            <Text style={styles.itemTitle}>{item.name}</Text>
            <Text style={styles.itemType}>({item.type})</Text>
          </TouchableOpacity>
        )}
        ListEmptyComponent={
          <Text style={styles.emptyText}>No cosmic entities found.</Text>
        }
      />
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Vault", { token })}
      >
        <Text style={styles.buttonText}>Vault</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Scrolls", { token })}
      >
        <Text style={styles.buttonText}>Archive (Scrolls)</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Oracle", { token })}
      >
        <Text style={styles.buttonText}>Grove Oracle</Text>
      </TouchableOpacity>
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
  errorText: {
    color: "#ff6666",
    fontSize: 16,
    textAlign: "center"
  },
  retryButton: {
    marginTop: 12,
    backgroundColor: "#663399",
    padding: 12,
    borderRadius: 6
  },
  retryText: {
    color: "#fff"
  },
  item: {
    padding: 12,
    borderBottomColor: "#333",
    borderBottomWidth: 1
  },
  itemTitle: {
    color: "#fff",
    fontSize: 18
  },
  itemType: {
    color: "#bbb",
    fontSize: 14
  },
  emptyText: {
    marginTop: 32,
    textAlign: "center",
    color: "#777"
  },
  button: {
    backgroundColor: "#663399",
    paddingVertical: 14,
    borderRadius: 6,
    marginVertical: 8,
    alignItems: "center"
  },
  buttonText: {
    color: "#fff",
    fontSize: 16
  }
});

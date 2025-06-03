import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  FlatList,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
} from "react-native";
import { fetchScrolls } from "../services/api";

export default function ScrollsScreen({ navigation }) {
  const [scrolls, setScrolls] = useState([]);

  useEffect(() => {
    (async () => {
      const data = await fetchScrolls();
      setScrolls(data);
    })();
  }, []);

  const renderItem = ({ item }) => (
    <TouchableOpacity
      style={styles.itemContainer}
      onPress={() => navigation.navigate("ScrollDetail", { id: item.id })}
    >
      <Text style={styles.itemTitle}>{item.title}</Text>
    </TouchableOpacity>
  );

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>📜 Sacred Scrolls</Text>

      <FlatList
        data={scrolls}
        keyExtractor={(item) => item.id.toString()}
        renderItem={renderItem}
        contentContainerStyle={styles.list}
      />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    backgroundColor: "#1e1e2e",
    padding: 20,
  },
  title: {
    fontSize: 26,
    color: "#e0c0ff",
    fontWeight: "bold",
    marginBottom: 20,
    textAlign: "center",
  },
  list: {
    alignItems: "center",
  },
  itemContainer: {
    backgroundColor: "#2a2a3e",
    padding: 15,
    borderRadius: 8,
    marginVertical: 8,
    width: "90%",
    shadowColor: "#000",
    shadowOpacity: 0.3,
    shadowRadius: 5,
    shadowOffset: { width: 0, height: 3 },
  },
  itemTitle: {
    color: "#fff",
    fontSize: 18,
  },
});

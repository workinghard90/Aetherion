import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity } from 'react-native';
import axios from 'axios';
import { getToken } from '../services/api';

export default function ScrollsScreen() {
  const [scrolls, setScrolls] = useState([]);
  const API_URL = process.env.EXPO_PUBLIC_API_URL + "/scrolls";

  const fetchScrolls = async () => {
    try {
      const token = await getToken();
      const res = await axios.get(API_URL, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setScrolls(res.data.scrolls);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchScrolls();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>📜 Archive of Scrolls</Text>
      <FlatList
        data={scrolls}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <TouchableOpacity style={styles.scrollRow}>
            <Text style={styles.scrollTitle}>{item.title}</Text>
            <Text style={styles.scrollDesc}>{item.content.substring(0, 60)}...</Text>
          </TouchableOpacity>
        )}
        ListEmptyComponent={<Text style={styles.empty}>No scrolls available.</Text>}
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
  heading: {
    color: "#E0CFFF",
    fontSize: 24,
    marginBottom: 12
  },
  scrollRow: {
    backgroundColor: "#222",
    padding: 12,
    marginVertical: 6,
    borderRadius: 6
  },
  scrollTitle: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "600"
  },
  scrollDesc: {
    color: "#ccc",
    fontSize: 14,
    marginTop: 4
  },
  empty: {
    color: "#aaa",
    fontSize: 16,
    marginTop: 20,
    textAlign: "center"
  }
});

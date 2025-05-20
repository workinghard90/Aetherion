import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import Constants from 'expo-constants';

const API = Constants.expoConfig?.extra?.apiUrl;

interface Scroll {
  name: string;
  summary: string;
  full_content: any;
}

// Placeholder ArrivalScreen component
const ArrivalScreen = () => {
  return (
    <View style={styles.arrivalBox}>
      <Text style={styles.arrivalTitle}>[Gate of Arrival Activated]</Text>
      <Text style={styles.arrivalMessage}>You are sacred here.</Text>
    </View>
  );
};

export default function EmanationViewer() {
  const [scrolls, setScrolls] = useState<Scroll[]>([]);

  useEffect(() => {
    fetch(`${API}/api/docs`)
      .then(res => res.json())
      .then(async all => {
        const core = all.filter((s: any) =>
          s.name.includes("Caelum") || s.name.includes("Autumn")
        );
        const full = await Promise.all(core.map((s: any) =>
          fetch(`${API}/api/docs/${encodeURIComponent(s.name)}`).then(r => r.json())
        ));
        setScrolls(full);
      });
  }, []);

  return (
    <ScrollView style={styles.container}>
      <ArrivalScreen />
      {scrolls.map((s, i) => (
        <View key={i} style={styles.scrollBox}>
          <Text style={styles.title}>{s.name}</Text>
          <Text style={styles.summary}>{s.summary}</Text>
          <Text style={styles.body}>{JSON.stringify(s.full_content, null, 2)}</Text>
        </View>
      ))}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 16
  },
  scrollBox: {
    marginBottom: 20,
    padding: 12,
    backgroundColor: "#222",
    borderRadius: 8
  },
  title: {
    color: "#0ff",
    fontSize: 18,
    fontWeight: "bold"
  },
  summary: {
    color: "#ccc",
    marginBottom: 6
  },
  body: {
    fontSize: 12,
    color: "#aaa",
    fontFamily: "monospace"
  },
  arrivalBox: {
    marginBottom: 24,
    padding: 12,
    backgroundColor: "#101010",
    borderWidth: 1,
    borderColor: "#444",
    borderRadius: 6
  },
  arrivalTitle: {
    color: "#0f0",
    fontSize: 16,
    fontWeight: "bold"
  },
  arrivalMessage: {
    color: "#ccc",
    marginTop: 4
  }
});

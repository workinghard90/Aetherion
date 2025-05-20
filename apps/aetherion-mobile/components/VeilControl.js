import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import Constants from 'expo-constants';

const API = Constants.expoConfig?.extra?.apiUrl;

// Placeholder VeilControl logic (can be enhanced)
const VeilControl = () => {
  return (
    <View style={styles.veilBox}>
      <Text style={styles.veilLabel}>[VeilControl Placeholder]</Text>
    </View>
  );
};

interface Scroll {
  name: string;
  summary: string;
  full_content: any;
}

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
      <VeilControl />
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
  veilBox: {
    marginBottom: 24,
    padding: 10,
    backgroundColor: "#333",
    borderLeftWidth: 4,
    borderLeftColor: "#f0f"
  },
  veilLabel: {
    color: "#f0f",
    fontSize: 14,
    fontWeight: "600"
  }
});

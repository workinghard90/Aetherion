// apps/aetherion-mobile/screens/EmanationViewer.tsx
import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, ImageBackground } from 'react-native';

const API = 'https://aetherionai-mobile.onrender.com';

type Scroll = {
  name: string;
  summary: string;
  full_content: any;
};

const ArrivalScreen = () => (
  <View style={styles.arrivalBox}>
    <Text style={styles.arrivalTitle}>[Gate of Arrival Activated]</Text>
    <Text style={styles.arrivalMessage}>You are sacred here.</Text>
  </View>
);

export default function EmanationViewer() {
  const [scrolls, setScrolls] = useState<Scroll[]>([]);

  useEffect(() => {
    fetch(`${API}/api/docs`)
      .then(res => res.json())
      .then(async all => {
        const core = all.filter((s: any) =>
          s.name.includes("Caelum") || s.name.includes("Autumn")
        );
        const full = await Promise.all(
          core.map((s: any) =>
            fetch(`${API}/api/docs/${encodeURIComponent(s.name)}`).then(r => r.json())
          )
        );
        setScrolls(full);
      });
  }, []);

  return (
    <ImageBackground
      source={{ uri: 'https://images.unsplash.com/photo-1549880338-65ddcdfd017b' }}
      style={styles.background}
      resizeMode="cover"
    >
      <ScrollView contentContainerStyle={styles.container}>
        <ArrivalScreen />
        {scrolls.map((s, i) => (
          <View key={i} style={styles.scrollBox}>
            <Text style={styles.title}>{s.name}</Text>
            <Text style={styles.summary}>{s.summary}</Text>
            <Text style={styles.body}>{JSON.stringify(s.full_content, null, 2)}</Text>
          </View>
        ))}
      </ScrollView>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  background: {
    flex: 1
  },
  container: {
    padding: 16
  },
  scrollBox: {
    marginBottom: 20,
    padding: 12,
    backgroundColor: 'rgba(0,0,0,0.75)',
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

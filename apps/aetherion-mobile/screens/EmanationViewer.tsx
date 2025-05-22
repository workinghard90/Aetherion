// apps/aetherion-mobile/screens/EmanationViewer.tsx

import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, ImageBackground } from 'react-native';

const API = process.env.EXPO_PUBLIC_API_URL || 'https://aetherionai-mobile.onrender.com';

const ArrivalScreen = () => {
  return (
    <View style={styles.arrivalBox}>
      <Text style={styles.arrivalTitle}>[Gate of Arrival Activated]</Text>
      <Text style={styles.arrivalMessage}>You are sacred here.</Text>
    </View>
  );
};

export default function EmanationViewer() {
  const [scrolls, setScrolls] = useState<any[]>([]);

  useEffect(() => {
    fetch(`${API}/api/docs`)
      .then(res => res.json())
      .then(async all => {
        const core = all.filter((s: any) =>
          s.name.includes('Caelum') || s.name.includes('Autumn')
        );
        const full = await Promise.all(core.map((s: any) =>
          fetch(`${API}/api/docs/${encodeURIComponent(s.name)}`).then(r => r.json())
        ));
        setScrolls(full);
      });
  }, []);

  return (
    <ImageBackground
      source={{ uri: 'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?auto=format&fit=crop&w=1400&q=80' }}
      resizeMode="cover"
      style={styles.bg}
    >
      <ScrollView contentContainerStyle={styles.scroll}>
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
  bg: {
    flex: 1,
  },
  scroll: {
    padding: 16,
  },
  scrollBox: {
    marginBottom: 20,
    padding: 12,
    backgroundColor: '#000000c0',
    borderRadius: 8,
  },
  title: {
    color: '#0ff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  summary: {
    color: '#ccc',
    marginBottom: 6,
  },
  body: {
    fontSize: 12,
    color: '#aaa',
    fontFamily: 'monospace',
  },
  arrivalBox: {
    marginBottom: 24,
    padding: 12,
    backgroundColor: '#101010c0',
    borderWidth: 1,
    borderColor: '#444',
    borderRadius: 6,
  },
  arrivalTitle: {
    color: '#0f0',
    fontSize: 16,
    fontWeight: 'bold',
  },
  arrivalMessage: {
    color: '#ccc',
    marginTop: 4,
  },
});

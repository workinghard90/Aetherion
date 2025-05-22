// apps/aetherion-mobile/screens/EmanationViewer.tsx
import React from 'react';
import { View, Text, ImageBackground, StyleSheet } from 'react-native';

export default function EmanationViewer() {
  return (
    <ImageBackground
      source={{ uri: 'https://images.unsplash.com/photo-1549880338-65ddcdfd017b' }}
      style={styles.background}
      resizeMode="cover"
    >
      <View style={styles.overlay}>
        <Text style={styles.title}>Welcome Guardian</Text>
        <Text style={styles.subtitle}>AetherionAI is live.</Text>
      </View>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  background: {
    flex: 1,
    justifyContent: 'center',
  },
  overlay: {
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.4)',
    padding: 20,
    borderRadius: 8,
  },
  title: {
    color: 'white',
    fontSize: 28,
    fontWeight: 'bold',
  },
  subtitle: {
    color: 'white',
    fontSize: 18,
    marginTop: 10,
  },
});

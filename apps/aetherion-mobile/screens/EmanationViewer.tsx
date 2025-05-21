// apps/aetherion-mobile/screens/EmanationViewer.tsx
import React from 'react';
import { View, Text, StyleSheet, ImageBackground } from 'react-native';

const backgroundImage = { uri: 'https://images.unsplash.com/photo-1527689368864-3a821dbccc34' };

export default function EmanationViewer() {
  return (
    <ImageBackground source={backgroundImage} style={styles.background}>
      <View style={styles.overlay}>
        <Text style={styles.title}>AetherionAI</Text>
        <Text style={styles.subtitle}>The gateway is open...</Text>
      </View>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  background: {
    flex: 1,
    resizeMode: 'cover',
    justifyContent: 'center',
    alignItems: 'center',
  },
  overlay: {
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    padding: 30,
    borderRadius: 12,
  },
  title: {
    color: '#fff',
    fontSize: 32,
    fontWeight: 'bold',
  },
  subtitle: {
    color: '#ccc',
    fontSize: 18,
    marginTop: 10,
  },
});

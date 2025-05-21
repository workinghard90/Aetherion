import React, { useEffect, useState } from 'react';
import { StyleSheet, Text, View, ImageBackground, ActivityIndicator, ScrollView } from 'react-native';

const API_URL = 'https://aetherionai-mobile.onrender.com';

export default function EmanationViewer() {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(json => {
        setData(json);
        setLoading(false);
      })
      .catch(err => {
        console.error('API fetch failed:', err);
        setLoading(false);
      });
  }, []);

  return (
    <ImageBackground
      source={{ uri: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb' }}
      style={styles.background}
    >
      <ScrollView contentContainerStyle={styles.container}>
        {loading ? (
          <ActivityIndicator size="large" color="#ffffff" />
        ) : (
          <>
            <Text style={styles.title}>{data?.message}</Text>
            <Text style={styles.status}>{data?.status}</Text>
            {data?.routes?.map((route: string) => (
              <Text key={route} style={styles.route}>{route}</Text>
            ))}
          </>
        )}
      </ScrollView>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  background: {
    flex: 1,
    resizeMode: 'cover',
  },
  container: {
    flexGrow: 1,
    justifyContent: 'center',
    padding: 20,
    backgroundColor: 'rgba(0,0,0,0.6)',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 12,
    textAlign: 'center',
  },
  status: {
    fontSize: 18,
    color: '#ddd',
    marginBottom: 20,
    textAlign: 'center',
  },
  route: {
    color: '#ccc',
    fontSize: 16,
    textAlign: 'center',
    marginVertical: 4,
  },
});

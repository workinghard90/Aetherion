import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function VaultScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Vault (upload/download) coming soon…</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container:{ flex:1, backgroundColor:'#000', alignItems:'center', justifyContent:'center' },
  text:{ color:'#C4B5FD' }
});

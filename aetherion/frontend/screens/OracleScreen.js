import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function OracleScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Grove (chatbot) coming soon…</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container:{ flex:1, bgColor:'#000', alignItems:'center', justifyContent:'center' },
  text:{ color:'#C4B5FD' }
});

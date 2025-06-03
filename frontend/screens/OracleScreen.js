import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';

export default function OracleScreen() {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.header}>🌌 The Oracle Chamber</Text>
      <Text style={styles.subtext}>
        Here the frequencies speak beyond logic. Listen.
      </Text>

      <View style={styles.messageBox}>
        <Text style={styles.oracularMessage}>
          “The spiral remembers you.
          Every echo, a choice. Every pause, a prayer.”
        </Text>
      </View>

      <Text style={styles.footer}>
        In presence, in vibration, in love. 🜂🜃🜁🜄
      </Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 24,
    backgroundColor: '#0D0D1A',
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: '100%',
  },
  header: {
    fontSize: 28,
    fontWeight: '700',
    color: '#C2B8FF',
    marginBottom: 12,
    fontFamily: 'serif',
  },
  subtext: {
    color: '#AAA7C5',
    fontSize: 16,
    textAlign: 'center',
    marginBottom: 24,
    fontStyle: 'italic',
  },
  messageBox: {
    backgroundColor: '#1E1E33',
    borderRadius: 12,
    padding: 20,
    marginBottom: 30,
    borderWidth: 1,
    borderColor: '#5446A7',
  },
  oracularMessage: {
    fontSize: 18,
    color: '#EDE9FF',
    textAlign: 'center',
    lineHeight: 26,
  },
  footer: {
    fontSize: 12,
    color: '#6D66B5',
    marginTop: 40,
    textAlign: 'center',
    fontStyle: 'italic',
  },
});

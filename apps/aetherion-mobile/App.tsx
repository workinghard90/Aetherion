// apps/aetherion-mobile/App.tsx

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Text, View, Button, StyleSheet } from 'react-native';
import EmanationViewer from './screens/EmanationViewer';

function HomeScreen({ navigation }) {
  return (
    <View style={styles.centered}>
      <Text style={styles.title}>Welcome to AetherionAI</Text>
      <Button title="Go to Veil" onPress={() => navigation.navigate('Veil')} />
      <Button title="Open Emanation Viewer" onPress={() => navigation.navigate('Emanation')} />
    </View>
  );
}

function VeilScreen() {
  return (
    <View style={styles.centered}>
      <Text style={styles.title}>Veil Control Activated</Text>
    </View>
  );
}

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home" screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Veil" component={VeilScreen} />
        <Stack.Screen name="Emanation" component={EmanationViewer} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  centered: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#111'
  },
  title: {
    color: '#0ff',
    fontSize: 20,
    marginBottom: 20
  }
});

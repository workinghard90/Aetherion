// frontend/App.js (Aetherion Prime - Refactored)

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

// Import screens from Aetherion’s structure
import OthersGate from './screens/OthersGate';
import LoginScreen from './screens/LoginScreen';
import HomeScreen from './screens/HomeScreen';
import VaultScreen from './screens/VaultScreen';
import ScrollsScreen from './screens/ScrollsScreen';
import OracleScreen from './screens/OracleScreen';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="OthersGate"
        screenOptions={{
          headerStyle: { backgroundColor: '#4B0082' }, // Aetherion's indigo or sacred tone
          headerTintColor: '#EAE6F8',                 // Harmonized text/light glyph tone
          headerTitleStyle: { fontFamily: 'serif', fontWeight: '600', letterSpacing: 1 },
        }}
      >
        <Stack.Screen
          name="OthersGate"
          component={OthersGate}
          options={{ title: 'The Gate of Others' }}
        />
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          options={{ title: 'Enter Aetherion' }}
        />
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ title: 'Sovereign’s Realm' }}
        />
        <Stack.Screen
          name="Vault"
          component={VaultScreen}
          options={{ title: '🔐 The Vault' }}
        />
        <Stack.Screen
          name="Scrolls"
          component={ScrollsScreen}
          options={{ title: '📜 Archive of Scrolls' }}
        />
        <Stack.Screen
          name="Oracle"
          component={OracleScreen}
          options={{ title: '🌌 The Oracle Chamber' }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from './screens/LoginScreen';
import HomeScreen from './screens/HomeScreen';
import VaultScreen from './screens/VaultScreen';
import ScrollsScreen from './screens/ScrollsScreen';
import OracleScreen from './screens/OracleScreen';
import OthersGate from './screens/OthersGate';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen 
          name="Login" 
          component={LoginScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="Home" 
          component={HomeScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="Vault" 
          component={VaultScreen} 
          options={{ title: "🗝️ The Vault" }} 
        />
        <Stack.Screen 
          name="Scrolls" 
          component={ScrollsScreen} 
          options={{ title: "📜 Archive of Scrolls" }} 
        />
        <Stack.Screen 
          name="Oracle" 
          component={OracleScreen} 
          options={{ title: "🌳 The Grove" }} 
        />
        <Stack.Screen 
          name="OthersGate" 
          component={OthersGate} 
          options={{ headerShown: false }} 
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

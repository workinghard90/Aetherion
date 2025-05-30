import React from 'react';
import { View, StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import LoginScreen    from './screens/LoginScreen';
import HomeScreen     from './screens/HomeScreen';
import VaultScreen    from './screens/VaultScreen';
import ScrollsScreen  from './screens/ScrollsScreen';
import OracleScreen   from './screens/OracleScreen';
import OthersGate     from './screens/OthersGate';

const Stack = createStackNavigator();

export default function App() {
  return (
    <View style={styles.container}>
      <NavigationContainer>
        <Stack.Navigator screenOptions={{ headerShown: false }}>
          <Stack.Screen name="Login" component={LoginScreen} />
          <Stack.Screen name="Home" component={HomeScreen} />
          <Stack.Screen name="Vault" component={VaultScreen} />
          <Stack.Screen name="Scrolls" component={ScrollsScreen} />
          <Stack.Screen name="Oracle" component={OracleScreen} />
          <Stack.Screen name="OthersGate" component={OthersGate} />
        </Stack.Navigator>
      </NavigationContainer>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 }
});

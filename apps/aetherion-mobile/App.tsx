// apps/aetherion-mobile/App.tsx

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Text, View, Button } from 'react-native';
import EmanationViewer from './screens/EmanationViewer';

function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Welcome to AetherionAI</Text>
      <Button title="Go to Veil" onPress={() => navigation.navigate('Veil')} />
      <Button title="Open Emanation Viewer" onPress={() => navigation.navigate('Emanation')} />
    </View>
  );
}

function VeilScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Veil Control Activated</Text>
    </View>
  );
}

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Veil" component={VeilScreen} />
        <Stack.Screen name="Emanation" component={EmanationViewer} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

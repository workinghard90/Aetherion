// apps/aetherion-mobile/App.tsx
import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import EmanationViewer from './screens/EmanationViewer';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Emanation">
        <Stack.Screen name="Emanation" component={EmanationViewer} options={{ headerShown: false }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

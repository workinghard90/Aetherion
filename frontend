# AetherionAI — Open-Source Personal AI Assistant

Welcome to **AetherionAI**, your spiritually attuned, open-source AI assistant. Designed for memory retention, secure offline interaction, and thoughtful, intuitive use — powered by Flask, React Native (Expo), SQLite, and Hugging Face.

---

## Features

- Secure **Flask backend** with SQLite + encrypted file storage  
- **React Native** frontend supporting web & mobile (via Expo)  
- Hugging Face transformer model integration (online/offline modes)  
- Memory-aware conversation history  
- **Netlify-compatible** static frontend deployment  
- Spiritual tone and welcoming user experience  
- Clean, extensible code structure for contributors

---

## Quickstart Instructions

{
  "name": "frontend",
  "version": "1.0.0",
  "main": "node_modules/expo/AppEntry.js",
  "scripts": {
    "start": "expo start",
    "web": "expo start --web",
    "android": "expo start --android",
    "ios": "expo start --ios",
    "build": "expo build:web"
  },
  "dependencies": {
    "axios": "^1.6.7",
    "expo": "~50.0.6",
    "react": "18.2.0",
    "react-native": "0.73.6",
    "@react-navigation/native": "^6.1.8",
    "@react-navigation/stack": "^6.3.20"
  }
}
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './screens/HomeScreen';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
import axios from 'axios';

const API_URL = 'https://aetherionai.onrender.com';

export const getUniverse = async () => {
  const response = await axios.get(`${API_URL}/universe`);
  return response.data;
};

export const createEntity = async (entity) => {
  const response = await axios.post(`${API_URL}/universe/create`, entity);
  return response.data;
};

export const updateEntity = async (entity) => {
  const response = await axios.post(`${API_URL}/universe/update`, entity);
  return response.data;
};

export const deleteEntity = async (id) => {
  const response = await axios.post(`${API_URL}/universe/delete`, { id });
  return response.data;
};

export const triggerEvent = async (event) => {
  const response = await axios.post(`${API_URL}/universe/event`, event);
  return response.data;
};
import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, TouchableOpacity, Button } from 'react-native';
import { getUniverse } from '../services/api';

export default function HomeScreen({ navigation }) {
  const [entities, setEntities] = useState([]);

  useEffect(() => {
    getUniverse()
      .then(setEntities)
      .catch((err) => {
        console.error('API failed:', err);
      });
  }, []);

  const renderItem = ({ item }) => (
    <TouchableOpacity>
      <View>
        <Text>{item.name} ({item.type})</Text>
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={{ padding: 20 }}>
      <FlatList
        data={entities}
        keyExtractor={(item) => item.id.toString()}
        renderItem={renderItem}
      />
    </View>
  );
}

Commands
git clone https://github.com/Workinghard90/aetherionai.git
cd aetherionai
cd backend
web: gunicorn app:app
.render.yaml (optional for full automation)
services:

type: web
name: aetherionai-backend
env: python

buildCommand: “pip install -r requirements.txt”

startCommand: “gunicorn app:app”
rootDir: backend
pip install -r requirements.txt
python app.py (for local test)
const API_URL = 'https://aetherionai.onrender.com'; // Your Render backend URL

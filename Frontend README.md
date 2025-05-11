// frontend/services/api.js

import axios from 'axios';

const API_URL = 'https://aetherionai.onrender.com'; // Make sure this URL is active and correct

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
// frontend/screens/HomeScreen.js

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
    <TouchableOpacity onPress={() => navigation.navigate('Entity', { entity: item })}>
      <View>
        <Text>{item.name} ({item.type})</Text>
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={{ padding: 20 }}>
      <Button title="Create Entity" onPress={() => navigation.navigate('CreateEntity')} />
      <FlatList
        data={entities}
        keyExtractor={(item) => item.id.toString()}
        renderItem={renderItem}
      />
    </View>
  );
}
https://aetherionai.onrender.com/universe

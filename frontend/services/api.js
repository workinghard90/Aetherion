import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';

const API_BASE = process.env.EXPO_PUBLIC_API_URL || "https://aetherion-mobile.onrender.com/api";

export const storeToken = async (token) => {
  try {
    await AsyncStorage.setItem("authToken", token);
  } catch {
    // ignore
  }
};

export const getToken = async () => {
  try {
    return await AsyncStorage.getItem("authToken");
  } catch {
    return null;
  }
};

export const apiClient = axios.create({
  baseURL: API_BASE,
  headers: { "Content-Type": "application/json" }
});

apiClient.interceptors.request.use(async (config) => {
  const token = await getToken();
  if (token) {
    config.headers["Authorization"] = `Bearer ${token}`;
  }
  return config;
}, (error) => Promise.reject(error));

// Aetherion/frontend/services/api.js

import axios from "axios";
import AsyncStorage from "@react-native-async-storage/async-storage";
import Constants from "expo-constants";

const API_BASE = Constants.expoConfig.extra.apiUrl || "https://aetherion-mobile.onrender.com/api";

export const getToken = async () => {
  return await AsyncStorage.getItem("token");
};

export const axiosInstance = axios.create({
  baseURL: API_BASE,
  timeout: 10000,
  headers: {
    "Content-Type": "application/json"
  }
});

// Request interceptor to attach JWT if present
axiosInstance.interceptors.request.use(async (config) => {
  const token = await getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

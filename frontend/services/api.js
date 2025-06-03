import AsyncStorage from "@react-native-async-storage/async-storage";

const API_URL = process.env.API_URL || "http://localhost:5000/api";

export async function loginUser(username, password) {
  const res = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });
  const data = await res.json();
  if (data.access_token) {
    await AsyncStorage.setItem("token", data.access_token);
    return data.access_token;
  }
  return null;
}

export async function getOracleInsights(prompt) {
  const token = await AsyncStorage.getItem("token");
  const res = await fetch(`${API_URL}/oracle/insights`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify({ prompt })
  });
  return await res.json();
}

export async function fetchScrolls() {
  const res = await fetch(`${API_URL}/scrolls`);
  return await res.json();
}

export async function uploadMemory(content) {
  const token = await AsyncStorage.getItem("token");
  await fetch(`${API_URL}/vault/upload`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify({ content })
  });
}

export async function downloadMemory(id) {
  const token = await AsyncStorage.getItem("token");
  const res = await fetch(`${API_URL}/vault/download/${id}`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${token}`
    }
  });
  return await res.json();
}

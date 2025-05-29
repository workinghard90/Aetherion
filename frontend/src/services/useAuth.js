// frontend/src/services/useAuth.js
import api from "./api";

export async function register({ username, password }) {
  try {
    const res = await api.post("/register", { username, password });
    return res.data;
  } catch (err) {
    throw new Error(err.response?.data?.error || "Registration failed");
  }
}

export async function login({ username, password }) {
  try {
    const res = await api.post("/login", { username, password });
    return res.data;
  } catch (err) {
    throw new Error(err.response?.data?.error || "Login failed");
  }
}

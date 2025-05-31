import axios from "axios";

// Use environment variable for base URL
const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

export const getUniverse = async () => {
  try {
    const response = await axios.get(`${API_URL}/api/items`);
    return response.data;
  } catch (error) {
    console.error("API error in getUniverse:", error);
    throw error;
  }
};

export const loginUser = async (credentials) => {
  try {
    const response = await axios.post(`${API_URL}/api/auth/login`, credentials);
    return response.data; // {token: "...", user: {...}}
  } catch (error) {
    console.error("API error in loginUser:", error);
    throw error;
  }
};

export const createItem = async (itemData, token) => {
  try {
    const response = await axios.post(
      `${API_URL}/api/items`,
      itemData,
      { headers: { Authorization: `Bearer ${token}` } }
    );
    return response.data;
  } catch (error) {
    console.error("API error in createItem:", error);
    throw error;
  }
};

// Similarly implement updateItem, deleteItem, getItemById, etc.
export const getItemById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/api/items/${id}`);
    return response.data;
  } catch (error) {
    console.error(`API error in getItemById(${id}):`, error);
    throw error;
  }
};

export const uploadFile = async (file, token) => {
  try {
    const formData = new FormData();
    formData.append("file", file);
    const response = await axios.post(`${API_URL}/api/vault/upload`, formData, {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "multipart/form-data"
      }
    });
    return response.data;
  } catch (error) {
    console.error("API error in uploadFile:", error);
    throw error;
  }
};

export const getScrolls = async () => {
  try {
    const response = await axios.get(`${API_URL}/api/scrolls`);
    return response.data;
  } catch (error) {
    console.error("API error in getScrolls:", error);
    throw error;
  }
};

// And so on for other routes (vault/download, oracle chat, etc.)

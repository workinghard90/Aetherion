// frontend/services/api.js

import axios from "axios";

// Base URL pointing to your Render backend
const API_URL = "https://aetherionai-mobile.onrender.com/api";

/**
 * Fetch all entities from the universe
 * @returns {Promise<Array>} Array of entity objects
 */
export const getUniverse = async () => {
  try {
    const response = await axios.get(`${API_URL}/items`);
    return response.data;
  } catch (error) {
    console.error("API error in getUniverse:", error);
    throw error;
  }
};

/**
 * Fetch a single entity by ID
 * @param {number|string} id - The ID of the entity
 * @returns {Promise<Object>} Entity data
 */
export const getEntityById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/items/${id}`);
    return response.data;
  } catch (error) {
    console.error(`API error in getEntityById for id ${id}:`, error);
    throw error;
  }
};

/**
 * Create a new entity in the universe (requires auth)
 * @param {Object} entityData - { name, type, description?, properties? }
 * @param {string} token - Bearer JWT token
 * @returns {Promise<Object>} Created‐entity response
 */
export const createEntity = async (entityData, token) => {
  try {
    const response = await axios.post(
      `${API_URL}/items`,
      entityData,
      {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      }
    );
    return response.data;
  } catch (error) {
    console.error("API error in createEntity:", error);
    throw error;
  }
};

/**
 * Update an existing entity (requires auth)
 * @param {number|string} id
 * @param {Object} entityData
 * @param {string} token - Bearer JWT token
 */
export const updateEntity = async (id, entityData, token) => {
  try {
    const response = await axios.put(
      `${API_URL}/items/${id}`,
      entityData,
      {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      }
    );
    return response.data;
  } catch (error) {
    console.error(`API error in updateEntity for id ${id}:`, error);
    throw error;
  }
};

/**
 * Delete an entity by ID (requires auth)
 * @param {number|string} id
 * @param {string} token - Bearer JWT token
 */
export const deleteEntity = async (id, token) => {
  try {
    const response = await axios.delete(`${API_URL}/items/${id}`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
  } catch (error) {
    console.error(`API error in deleteEntity for id ${id}:`, error);
    throw error;
  }
};

/**
 * Upload a file to the vault (requires auth)
 * @param {File} file - JS File object from <input type="file" />
 * @param {string} token - Bearer JWT token
 * @returns {Promise<Object>} { message, file_id }
 */
export const uploadToVault = async (file, token) => {
  try {
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post(`${API_URL}/vault/upload`, formData, {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "multipart/form-data",
      },
    });
    return response.data;
  } catch (error) {
    console.error("API error in uploadToVault:", error);
    throw error;
  }
};

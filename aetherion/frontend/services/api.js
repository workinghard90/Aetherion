import axios from 'axios';
const API_URL = process.env.EXPO_PUBLIC_API_URL;

export const getUniverse    = () => axios.get(`${API_URL}/api/items`).then(r => r.data);
export const getUniverseItem= id => axios.get(`${API_URL}/api/items/${id}`).then(r => r.data);
export const createEntity   = data => axios.post(`${API_URL}/api/items`, data).then(r => r.data);
export const getScrolls     = () => axios.get(`${API_URL}/api/scrolls`).then(r => r.data);

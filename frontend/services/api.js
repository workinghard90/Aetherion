import axios from 'axios';

const API_URL = process.env.EXPO_PUBLIC_API_URL || 'https://<https://aetherionai-mobile.onrender.com>';

export const getUniverse = async () => {
  const res = await axios.get(`${API_URL}/api/items`);
  return res.data;
};

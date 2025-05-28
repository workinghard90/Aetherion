import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/auth': 'https://aetherionai-mobile.onrender.com',
      '/vault': 'https://aetherionai-mobile.onrender.com'
    }
  }
})

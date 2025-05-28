import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  root: ".", // assumes vite.config.js is in frontend/
  plugins: [react()],
  build: {
    outDir: "dist",
  },
});

import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  base: './', // Enable relative paths so index.html is double-clickable locally
  build: {
    outDir: 'dist',
    emptyOutDir: true,
  }
})

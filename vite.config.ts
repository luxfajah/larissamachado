import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  base: './', // Enable relative paths so index.html is double-clickable locally
  build: {
    outDir: '/Users/luxfajah/Documents/Duas mâos/Larissa', // Save files directly to Larissa's folder
    emptyOutDir: false, // CRITICAL: Do not delete existing files (e.g. the PDF) in the target folder
  }
})
